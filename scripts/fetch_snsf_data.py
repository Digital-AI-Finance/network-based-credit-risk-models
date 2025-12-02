#!/usr/bin/env python3
"""Fetch SNSF grant data using Playwright (JavaScript-rendered page)."""

from playwright.sync_api import sync_playwright
import json
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "_data" / "snsf_official.json"

def fetch_snsf_grant():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Fetching SNSF grant page...")
        page.goto("https://data.snf.ch/grants/grant/205487", wait_until='networkidle', timeout=60000)
        page.wait_for_timeout(3000)  # Wait for JS to render

        # Extract all text content
        content = page.content()

        # Try to extract structured data
        data = {
            "source_url": "https://data.snf.ch/grants/grant/205487",
            "raw_content": {}
        }

        # Get all text from the page
        try:
            # Project title
            title_el = page.query_selector('h1, .project-title, [class*="title"]')
            if title_el:
                data["raw_content"]["title"] = title_el.inner_text()

            # Get all definition list items (common pattern for grant data)
            dl_items = page.query_selector_all('dt, dd')
            if dl_items:
                items = [el.inner_text() for el in dl_items]
                data["raw_content"]["definition_list"] = items

            # Get all table data
            tables = page.query_selector_all('table')
            for i, table in enumerate(tables):
                data["raw_content"][f"table_{i}"] = table.inner_text()

            # Get main content area
            main = page.query_selector('main, .main-content, #app, [role="main"]')
            if main:
                data["raw_content"]["main_text"] = main.inner_text()

            # Get all links
            links = page.query_selector_all('a[href]')
            data["raw_content"]["links"] = [
                {"text": l.inner_text(), "href": l.get_attribute("href")}
                for l in links[:50]  # First 50 links
            ]

        except Exception as e:
            print(f"Error extracting: {e}")

        # Save HTML for inspection
        html_path = Path(__file__).parent.parent / "debug_snsf_page.html"
        html_path.write_text(content, encoding='utf-8')
        print(f"Saved HTML to: {html_path}")

        # Take screenshot
        screenshot_path = Path(__file__).parent.parent / "screenshots" / "snsf_grant_page.png"
        screenshot_path.parent.mkdir(exist_ok=True)
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"Saved screenshot to: {screenshot_path}")

        browser.close()

        return data


if __name__ == "__main__":
    data = fetch_snsf_grant()
    OUTPUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nSaved data to: {OUTPUT}")
    print("\nExtracted content:")
    print(json.dumps(data["raw_content"], indent=2, ensure_ascii=False)[:2000])
