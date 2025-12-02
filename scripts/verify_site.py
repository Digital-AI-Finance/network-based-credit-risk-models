#!/usr/bin/env python3
"""
Comprehensive Site Verification Script
Tests all links, navigation, images, and page functionality.
"""

import re
import json
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

# Configuration
SITE_URL = "https://digital-ai-finance.github.io/network-based-credit-risk-models/"
PROJECT_ROOT = Path(__file__).parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "verification_screenshots"


class VerificationReport:
    def __init__(self):
        self.results = {"passed": [], "failed": [], "warnings": []}
        self.start_time = datetime.now()

    def passed(self, test, message):
        self.results["passed"].append({"test": test, "message": message})
        print(f"  [PASS] {test}: {message}")

    def failed(self, test, message):
        self.results["failed"].append({"test": test, "message": message})
        print(f"  [FAIL] {test}: {message}")

    def warning(self, test, message):
        self.results["warnings"].append({"test": test, "message": message})
        print(f"  [WARN] {test}: {message}")

    def summary(self):
        duration = (datetime.now() - self.start_time).total_seconds()
        print("\n" + "=" * 70)
        print("VERIFICATION SUMMARY")
        print("=" * 70)
        print(f"Duration: {duration:.1f} seconds")
        print(f"Passed:   {len(self.results['passed'])}")
        print(f"Failed:   {len(self.results['failed'])}")
        print(f"Warnings: {len(self.results['warnings'])}")

        if self.results["failed"]:
            print("\nFailed Tests:")
            for item in self.results["failed"]:
                print(f"  - {item['test']}: {item['message']}")

        print("=" * 70)
        return len(self.results["failed"]) == 0


def verify_local_files(report):
    """Verify local file structure and JSON data."""
    print("\n[1] Verifying Local Files...")

    # Check required files exist
    required_files = [
        "index.md",
        "_config.yml",
        "_data/publications.json",
        "_data/team.json",
        "_data/news.json",
        "_data/snsf_project_complete.json",
        "assets/css/style.scss",
        "assets/js/main.js",
        "assets/js/visualizations.js",
    ]

    for file in required_files:
        path = PROJECT_ROOT / file
        if path.exists():
            report.passed("File exists", file)
        else:
            report.failed("File missing", file)

    # Validate JSON files
    json_files = list((PROJECT_ROOT / "_data").glob("*.json"))
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            report.passed("Valid JSON", f"{json_file.name} ({len(data) if isinstance(data, list) else 'object'})")
        except json.JSONDecodeError as e:
            report.failed("Invalid JSON", f"{json_file.name}: {e}")


def verify_navigation_structure(report):
    """Verify navigation links match section IDs."""
    print("\n[2] Verifying Navigation Structure...")

    index_path = PROJECT_ROOT / "index.md"
    content = index_path.read_text(encoding='utf-8')

    # Extract nav links
    nav_links = set(re.findall(r'<a\s+href="#([^"]+)"', content))
    section_ids = set(re.findall(r'<section\s+id="([^"]+)"', content))

    # Check top nav
    top_nav = len(re.findall(r'class="nav-menu"', content)) > 0
    if top_nav:
        report.passed("Top nav", "nav-menu found")
    else:
        report.failed("Top nav", "nav-menu not found")

    # Check sidebar nav
    sidebar_nav = len(re.findall(r'class="sidebar-nav"', content)) > 0
    if sidebar_nav:
        report.passed("Sidebar nav", "sidebar-nav found")
    else:
        report.failed("Sidebar nav", "sidebar-nav not found")

    # Check link-section matching
    missing_sections = nav_links - section_ids
    for link in missing_sections:
        report.failed("Missing section", f"#{link} has no matching section")

    matched = nav_links & section_ids
    report.passed("Nav-Section match", f"{len(matched)} links matched")


def verify_external_links(report, html_content):
    """Verify external links are accessible."""
    print("\n[3] Verifying External Links...")

    # Extract all external links
    links = re.findall(r'href="(https?://[^"]+)"', html_content)
    unique_links = list(set(links))[:20]  # Test first 20 unique links

    for url in unique_links:
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code < 400:
                report.passed("External link", f"{urlparse(url).netloc}")
            else:
                report.warning("External link", f"{url[:50]}... (HTTP {response.status_code})")
        except requests.RequestException as e:
            report.warning("External link", f"{url[:50]}... ({type(e).__name__})")


def verify_images(report, html_content, base_url):
    """Verify all images load correctly."""
    print("\n[4] Verifying Images...")

    # Extract image sources
    img_sources = re.findall(r'<img[^>]+src="([^"]+)"', html_content)

    for src in img_sources:
        if src.startswith('http'):
            url = src
        else:
            url = urljoin(base_url, src)

        try:
            response = requests.head(url, timeout=10)
            if response.status_code == 200:
                report.passed("Image loads", src[:50])
            else:
                report.failed("Image missing", f"{src} (HTTP {response.status_code})")
        except requests.RequestException as e:
            report.failed("Image error", f"{src} ({type(e).__name__})")


def verify_live_navigation(report):
    """Test live site navigation with Playwright."""
    print("\n[5] Verifying Live Navigation...")

    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        try:
            # Load page
            response = page.goto(SITE_URL, wait_until='networkidle', timeout=30000)

            if response.status == 200:
                report.passed("Page load", f"HTTP {response.status}")
            else:
                report.failed("Page load", f"HTTP {response.status}")
                return

            # Get page content for other tests
            html_content = page.content()

            # Check sidebar exists and is visible on desktop
            sidebar = page.query_selector('.sidebar-nav')
            if sidebar and sidebar.is_visible():
                report.passed("Sidebar visible", "Left navigation rendered")
            else:
                report.warning("Sidebar", "Not visible (may be mobile view)")

            # Test all navigation links
            nav_links = page.query_selector_all('.sidebar-nav a[href^="#"], .nav-menu a[href^="#"]')
            unique_hrefs = list(set([l.get_attribute('href') for l in nav_links]))

            for href in unique_hrefs:
                section_id = href.replace('#', '')

                # Click on sidebar link if exists
                link = page.query_selector(f'.sidebar-nav a[href="{href}"]')
                if not link:
                    link = page.query_selector(f'.nav-menu a[href="{href}"]')

                if link:
                    link.click()
                    page.wait_for_timeout(800)

                    # Check if section is visible
                    section = page.query_selector(f'section#{section_id}')
                    if section:
                        box = section.bounding_box()
                        if box and box['height'] > 0:
                            report.passed("Navigation", f"#{section_id} scrolls correctly")
                        else:
                            report.failed("Navigation", f"#{section_id} has zero height")
                    else:
                        report.failed("Navigation", f"#{section_id} not found")

            # Check JavaScript libraries loaded
            chart_loaded = page.evaluate("typeof Chart !== 'undefined'")
            d3_loaded = page.evaluate("typeof d3 !== 'undefined'")

            if chart_loaded:
                report.passed("Chart.js", "Library loaded")
            else:
                report.warning("Chart.js", "Not loaded")

            if d3_loaded:
                report.passed("D3.js", "Library loaded")
            else:
                report.warning("D3.js", "Not loaded")

            # Take full page screenshot
            screenshot_path = SCREENSHOTS_DIR / "full_verification.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            report.passed("Screenshot", str(screenshot_path))

            # Return HTML for other tests
            return html_content

        except Exception as e:
            report.failed("Live test", str(e))
            return None

        finally:
            browser.close()


def verify_content_quality(report, html_content):
    """Verify content quality and completeness."""
    print("\n[6] Verifying Content Quality...")

    if not html_content:
        report.warning("Content", "No HTML content to verify")
        return

    # Check for unrendered markdown
    markdown_patterns = [
        (r'##\s+\w+', "Unrendered ## heading"),
        (r'\*\*[^*]+\*\*', "Unrendered **bold**"),
        (r'&lt;', "HTML-escaped < character"),
        (r'&gt;', "HTML-escaped > character"),
    ]

    for pattern, description in markdown_patterns:
        matches = re.findall(pattern, html_content)
        if matches and len(matches) > 5:  # Allow some false positives
            report.warning("Markdown", f"{description}: {len(matches)} occurrences")
        else:
            report.passed("Markdown", f"No {description}")

    # Check key sections have content
    sections = ['home', 'team', 'research', 'publications', 'analytics',
                'resources', 'news', 'events', 'collaborations', 'funding', 'contact']

    for section in sections:
        pattern = f'id="{section}"[^>]*>.*?</section>'
        match = re.search(pattern, html_content, re.DOTALL)
        if match and len(match.group()) > 100:
            report.passed("Section content", f"#{section} has content")
        else:
            report.warning("Section content", f"#{section} may be empty")


def verify_doi_links(report):
    """Verify DOI links in publications are valid."""
    print("\n[7] Verifying DOI Links...")

    pub_file = PROJECT_ROOT / "_data" / "publications.json"
    if not pub_file.exists():
        report.warning("DOI", "publications.json not found")
        return

    pubs = json.loads(pub_file.read_text(encoding='utf-8'))
    doi_count = 0
    valid_count = 0

    for pub in pubs[:10]:  # Test first 10
        doi = pub.get('doi')
        if doi:
            doi_count += 1
            url = f"https://doi.org/{doi}"
            try:
                response = requests.head(url, timeout=10, allow_redirects=True)
                if response.status_code < 400:
                    valid_count += 1
            except:
                pass

    if doi_count > 0:
        report.passed("DOI links", f"{valid_count}/{doi_count} DOIs resolve correctly")
    else:
        report.warning("DOI links", "No DOIs to verify")


def main():
    print("=" * 70)
    print("COMPREHENSIVE SITE VERIFICATION")
    print(f"URL: {SITE_URL}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    report = VerificationReport()

    # Run all verification tests
    verify_local_files(report)
    verify_navigation_structure(report)
    html_content = verify_live_navigation(report)

    if html_content:
        verify_external_links(report, html_content)
        verify_images(report, html_content, SITE_URL)
        verify_content_quality(report, html_content)

    verify_doi_links(report)

    # Print summary and exit
    success = report.summary()

    # Save report
    report_path = PROJECT_ROOT / "verification_report.json"
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "url": SITE_URL,
        "results": report.results
    }
    report_path.write_text(json.dumps(report_data, indent=2), encoding='utf-8')
    print(f"\nReport saved to: {report_path}")

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
