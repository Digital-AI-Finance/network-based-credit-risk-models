#!/usr/bin/env python3
"""
Debug navigation issues on the live site.
Tests clicking each nav tab and checking scroll position.
"""

from playwright.sync_api import sync_playwright
import json
from pathlib import Path

SITE_URL = "https://digital-ai-finance.github.io/network-based-credit-risk-models/"
OUTPUT_DIR = Path(__file__).parent.parent / "debug_screenshots"


def debug_navigation():
    OUTPUT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible browser for debugging
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        print(f"Loading {SITE_URL}")
        page.goto(SITE_URL, wait_until='networkidle')

        # Get initial page height
        page_height = page.evaluate("document.body.scrollHeight")
        print(f"Page height: {page_height}px")

        # Get all sections and their positions
        sections_info = page.evaluate("""
            () => {
                const sections = document.querySelectorAll('section[id]');
                return Array.from(sections).map(s => ({
                    id: s.id,
                    top: s.offsetTop,
                    height: s.offsetHeight,
                    visible: s.offsetHeight > 0
                }));
            }
        """)

        print("\nSection positions:")
        for s in sections_info:
            print(f"  #{s['id']}: top={s['top']}px, height={s['height']}px, visible={s['visible']}")

        # Get nav links
        nav_links = page.query_selector_all('nav a[href^="#"]')
        print(f"\nFound {len(nav_links)} nav links")

        # Test each link
        results = []
        for link in nav_links:
            href = link.get_attribute('href')
            text = link.inner_text()
            section_id = href.replace('#', '')

            print(f"\n--- Testing '{text}' -> {href} ---")

            # Get scroll position before click
            scroll_before = page.evaluate("window.scrollY")
            print(f"  Scroll before: {scroll_before}px")

            # Click the link
            link.click()
            page.wait_for_timeout(1000)  # Wait for smooth scroll

            # Get scroll position after click
            scroll_after = page.evaluate("window.scrollY")
            print(f"  Scroll after: {scroll_after}px")

            # Get section position
            section_top = page.evaluate(f"document.getElementById('{section_id}')?.offsetTop || -1")
            print(f"  Section top: {section_top}px")

            # Check if scroll worked
            scroll_diff = abs(scroll_after - section_top)
            success = scroll_diff < 150  # Within 150px of section

            print(f"  Difference: {scroll_diff}px - {'OK' if success else 'FAILED'}")

            # Take screenshot
            screenshot_path = OUTPUT_DIR / f"nav_{section_id}.png"
            page.screenshot(path=str(screenshot_path))

            results.append({
                'section': section_id,
                'text': text,
                'scroll_before': scroll_before,
                'scroll_after': scroll_after,
                'section_top': section_top,
                'scroll_diff': scroll_diff,
                'success': success
            })

        # Summary
        print("\n" + "=" * 60)
        print("NAVIGATION TEST RESULTS")
        print("=" * 60)

        passed = sum(1 for r in results if r['success'])
        failed = len(results) - passed

        print(f"\nPassed: {passed}, Failed: {failed}")

        for r in results:
            status = "OK" if r['success'] else "FAIL"
            print(f"  [{status}] {r['text']}: scrolled to {r['scroll_after']}px (section at {r['section_top']}px)")

        if failed > 0:
            print("\nFailed sections need scroll to these positions:")
            for r in results:
                if not r['success']:
                    print(f"  #{r['section']}: {r['section_top']}px")

        browser.close()

        return results


if __name__ == "__main__":
    debug_navigation()
