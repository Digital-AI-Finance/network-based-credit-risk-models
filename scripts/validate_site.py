#!/usr/bin/env python3
"""
Site Validation Script for Network-Based Credit Risk Models GitHub Pages
Validates navigation, markdown, JSON data, and tests live site with Playwright.
"""

import re
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Configuration
SITE_URL = "https://digital-ai-finance.github.io/network-based-credit-risk-models/"
PROJECT_ROOT = Path(__file__).parent.parent
INDEX_FILE = PROJECT_ROOT / "index.md"
DATA_DIR = PROJECT_ROOT / "_data"
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"


class ValidationReport:
    """Collects validation results."""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = []

    def add_error(self, category, message):
        self.errors.append(f"[ERROR] {category}: {message}")

    def add_warning(self, category, message):
        self.warnings.append(f"[WARN] {category}: {message}")

    def add_pass(self, category, message):
        self.passed.append(f"[OK] {category}: {message}")

    def print_report(self):
        print("\n" + "=" * 60)
        print("SITE VALIDATION REPORT")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

        if self.passed:
            print(f"\nPASSED ({len(self.passed)}):")
            for item in self.passed:
                print(f"  {item}")

        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            for item in self.warnings:
                print(f"  {item}")

        if self.errors:
            print(f"\nERRORS ({len(self.errors)}):")
            for item in self.errors:
                print(f"  {item}")

        print("\n" + "-" * 60)
        print(f"Summary: {len(self.passed)} passed, {len(self.warnings)} warnings, {len(self.errors)} errors")
        print("=" * 60)

        return len(self.errors) == 0


def validate_navigation(report):
    """Check that all nav links have matching section IDs."""
    print("\n[1] Validating Navigation Links...")

    if not INDEX_FILE.exists():
        report.add_error("Navigation", f"index.md not found at {INDEX_FILE}")
        return

    content = INDEX_FILE.read_text(encoding='utf-8')

    # Extract nav links (href="#...")
    nav_links = re.findall(r'<a\s+href="#([^"]+)"', content)
    print(f"    Found {len(nav_links)} navigation links: {nav_links}")

    # Extract section IDs (<section id="...">)
    section_ids = re.findall(r'<section\s+id="([^"]+)"', content)
    print(f"    Found {len(section_ids)} section IDs: {section_ids}")

    # Compare
    nav_set = set(nav_links)
    section_set = set(section_ids)

    # Links without matching sections
    missing_sections = nav_set - section_set
    for link in missing_sections:
        report.add_error("Navigation", f"Nav link '#{link}' has no matching <section id=\"{link}\">")

    # Sections without nav links (warning only)
    orphan_sections = section_set - nav_set
    for section in orphan_sections:
        report.add_warning("Navigation", f"Section '{section}' has no navigation link")

    # Successful matches
    matched = nav_set & section_set
    for item in matched:
        report.add_pass("Navigation", f"#{item} -> section#{item}")

    return nav_links, section_ids


def validate_markdown(report):
    """Check for unrendered markdown patterns inside HTML."""
    print("\n[2] Checking for Unrendered Markdown...")

    if not INDEX_FILE.exists():
        return

    content = INDEX_FILE.read_text(encoding='utf-8')
    lines = content.split('\n')

    issues_found = 0

    for i, line in enumerate(lines, 1):
        # Skip lines that are pure markdown (not inside HTML)
        # Check for **text** that should be <strong>
        bold_matches = re.findall(r'\*\*([^*]+)\*\*', line)
        for match in bold_matches:
            # Check if this is inside an HTML tag context
            if '<' in line or '>' in line:
                report.add_warning("Markdown", f"Line {i}: **{match}** may not render inside HTML - use <strong>")
                issues_found += 1

        # Check for *text* (single asterisk) that should be <em>
        italic_matches = re.findall(r'(?<!\*)\*([^*]+)\*(?!\*)', line)
        for match in italic_matches:
            if '<' in line or '>' in line:
                # Exclude already correct HTML
                if f"<em>{match}</em>" not in line:
                    report.add_warning("Markdown", f"Line {i}: *{match}* may not render inside HTML - use <em>")
                    issues_found += 1

        # Check for [text](url) links that should be <a href>
        link_matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
        for text, url in link_matches:
            if '<section' in line or '<div' in line or '<table' in line:
                report.add_warning("Markdown", f"Line {i}: [{text}]({url}) may not render - use <a href>")
                issues_found += 1

    if issues_found == 0:
        report.add_pass("Markdown", "No unrendered markdown patterns detected")
    else:
        print(f"    Found {issues_found} potential markdown issues")


def validate_json_data(report):
    """Validate JSON data files in _data directory."""
    print("\n[3] Validating JSON Data Files...")

    if not DATA_DIR.exists():
        report.add_error("Data", f"_data directory not found at {DATA_DIR}")
        return

    json_files = list(DATA_DIR.glob("*.json"))
    print(f"    Found {len(json_files)} JSON files")

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if isinstance(data, list):
                report.add_pass("Data", f"{json_file.name}: Valid JSON array with {len(data)} items")
            elif isinstance(data, dict):
                report.add_pass("Data", f"{json_file.name}: Valid JSON object with {len(data)} keys")
            else:
                report.add_pass("Data", f"{json_file.name}: Valid JSON")

        except json.JSONDecodeError as e:
            report.add_error("Data", f"{json_file.name}: Invalid JSON - {e}")
        except Exception as e:
            report.add_error("Data", f"{json_file.name}: Error reading file - {e}")


def validate_image_paths(report):
    """Check that referenced images exist."""
    print("\n[4] Validating Image Paths...")

    if not INDEX_FILE.exists():
        return

    content = INDEX_FILE.read_text(encoding='utf-8')

    # Find image references
    img_patterns = [
        r'<img\s+src="([^"]+)"',  # HTML img tags
        r'!\[.*?\]\(([^)]+)\)',    # Markdown images
    ]

    images = []
    for pattern in img_patterns:
        images.extend(re.findall(pattern, content))

    print(f"    Found {len(images)} image references")

    for img_path in images:
        # Skip external URLs
        if img_path.startswith('http://') or img_path.startswith('https://'):
            report.add_pass("Images", f"External: {img_path[:50]}...")
            continue

        # Check local path
        full_path = PROJECT_ROOT / img_path
        if full_path.exists():
            report.add_pass("Images", f"Found: {img_path}")
        else:
            report.add_error("Images", f"Missing: {img_path}")


def validate_jekyll_syntax(report):
    """Check Jekyll/Liquid template syntax."""
    print("\n[5] Validating Jekyll Syntax...")

    if not INDEX_FILE.exists():
        return

    content = INDEX_FILE.read_text(encoding='utf-8')

    # Check for unclosed Liquid tags
    for_opens = len(re.findall(r'\{%\s*for\s+', content))
    for_closes = len(re.findall(r'\{%\s*endfor\s*%\}', content))

    if for_opens != for_closes:
        report.add_error("Jekyll", f"Mismatched for/endfor: {for_opens} opens, {for_closes} closes")
    else:
        report.add_pass("Jekyll", f"for/endfor loops balanced ({for_opens} pairs)")

    if_opens = len(re.findall(r'\{%\s*if\s+', content))
    if_closes = len(re.findall(r'\{%\s*endif\s*%\}', content))

    if if_opens != if_closes:
        report.add_error("Jekyll", f"Mismatched if/endif: {if_opens} opens, {if_closes} closes")
    else:
        report.add_pass("Jekyll", f"if/endif blocks balanced ({if_opens} pairs)")

    # Check for common syntax errors
    broken_liquid = re.findall(r'\{\{[^}]*\{', content)
    if broken_liquid:
        report.add_error("Jekyll", f"Potentially broken Liquid syntax found")


def test_live_site(report, take_screenshots=True):
    """Test the live deployed site using Playwright."""
    print("\n[6] Testing Live Site with Playwright...")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        report.add_warning("Live Test", "Playwright not installed. Run: pip install playwright && playwright install chromium")
        return

    if take_screenshots:
        SCREENSHOTS_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        try:
            # Load the page
            print(f"    Loading {SITE_URL}")
            response = page.goto(SITE_URL, wait_until='networkidle', timeout=30000)

            if response.status == 200:
                report.add_pass("Live Site", f"Page loaded successfully (HTTP {response.status})")
            else:
                report.add_error("Live Site", f"Page returned HTTP {response.status}")
                return

            # Take full page screenshot
            if take_screenshots:
                screenshot_path = SCREENSHOTS_DIR / "full_page.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                print(f"    Saved: {screenshot_path}")

            # Get all navigation links
            nav_links = page.query_selector_all('nav a[href^="#"]')
            print(f"    Found {len(nav_links)} navigation links")

            # Test each navigation link
            for link in nav_links:
                href = link.get_attribute('href')
                link_text = link.inner_text()
                section_id = href.replace('#', '')

                try:
                    # Click the link
                    link.click()
                    page.wait_for_timeout(500)  # Wait for scroll animation

                    # Check if the section is now visible/scrolled to
                    section = page.query_selector(f'section#{section_id}')

                    if section:
                        # Check if section is in viewport
                        is_visible = section.is_visible()
                        box = section.bounding_box()

                        if is_visible and box:
                            report.add_pass("Navigation", f"Click '{link_text}' scrolls to #{section_id}")

                            # Screenshot of this section
                            if take_screenshots:
                                screenshot_path = SCREENSHOTS_DIR / f"section_{section_id}.png"
                                page.screenshot(path=str(screenshot_path))
                                print(f"    Saved: {screenshot_path}")
                        else:
                            report.add_error("Navigation", f"Click '{link_text}' - section #{section_id} not visible after click")
                    else:
                        report.add_error("Navigation", f"Click '{link_text}' - section #{section_id} not found in DOM")

                except Exception as e:
                    report.add_error("Navigation", f"Click '{link_text}' failed: {str(e)}")

            # Check for JavaScript errors
            console_errors = []
            page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
            page.reload()
            page.wait_for_timeout(2000)

            if console_errors:
                for error in console_errors[:5]:  # Show first 5 errors
                    report.add_error("JavaScript", f"Console error: {error[:100]}")
            else:
                report.add_pass("JavaScript", "No console errors detected")

            # Check if Chart.js loaded
            chart_loaded = page.evaluate("typeof Chart !== 'undefined'")
            if chart_loaded:
                report.add_pass("Libraries", "Chart.js loaded successfully")
            else:
                report.add_warning("Libraries", "Chart.js may not have loaded")

            # Check if D3.js loaded
            d3_loaded = page.evaluate("typeof d3 !== 'undefined'")
            if d3_loaded:
                report.add_pass("Libraries", "D3.js loaded successfully")
            else:
                report.add_warning("Libraries", "D3.js may not have loaded")

        except Exception as e:
            report.add_error("Live Site", f"Failed to test: {str(e)}")

        finally:
            browser.close()


def auto_fix_issues(report, dry_run=True):
    """Attempt to auto-fix identified issues."""
    print("\n[7] Auto-Fix Mode...")

    if dry_run:
        print("    DRY RUN - no changes will be made")
        print("    Run with --fix to apply changes")
        return

    if not INDEX_FILE.exists():
        return

    content = INDEX_FILE.read_text(encoding='utf-8')
    original_content = content
    fixes_made = 0

    # Fix **text** -> <strong>text</strong> inside HTML sections
    # Only fix within <section> tags
    def replace_bold(match):
        nonlocal fixes_made
        fixes_made += 1
        return f"<strong>{match.group(1)}</strong>"

    # This is a simplified fix - in reality, need more sophisticated parsing
    # to only replace markdown inside HTML contexts

    if content != original_content:
        INDEX_FILE.write_text(content, encoding='utf-8')
        print(f"    Applied {fixes_made} fixes to index.md")
    else:
        print("    No automatic fixes available")


def main():
    """Run all validations."""
    print("=" * 60)
    print("SITE VALIDATION SCRIPT")
    print(f"Project: {PROJECT_ROOT}")
    print(f"Target: {SITE_URL}")
    print("=" * 60)

    # Parse command line args
    args = sys.argv[1:]
    test_live = '--live' in args or '--all' in args
    take_screenshots = '--screenshots' in args or '--all' in args
    apply_fixes = '--fix' in args

    if not args:
        print("\nUsage:")
        print("  python validate_site.py           # Local validation only")
        print("  python validate_site.py --live    # Include live site test")
        print("  python validate_site.py --all     # All tests + screenshots")
        print("  python validate_site.py --fix     # Apply auto-fixes")
        print("\nRunning local validation by default...\n")

    report = ValidationReport()

    # Run validations
    validate_navigation(report)
    validate_markdown(report)
    validate_json_data(report)
    validate_image_paths(report)
    validate_jekyll_syntax(report)

    if test_live:
        test_live_site(report, take_screenshots=take_screenshots)

    if apply_fixes:
        auto_fix_issues(report, dry_run=False)

    # Print report
    success = report.print_report()

    # Return exit code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
