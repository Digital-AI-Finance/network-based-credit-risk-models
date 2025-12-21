#!/usr/bin/env python3
"""
Sync SNSF grant data from official Data Portal.
Uses Playwright to render JavaScript and extract structured data.
Compares with existing data and updates files if changes detected.
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "_data"
SNSF_URL = "https://data.snf.ch/grants/grant/205487"


def parse_funding_amount(text: str) -> int:
    """Extract funding amount from text like '387,836 CHF'."""
    match = re.search(r"([\d,.']+)\s*CHF", text.replace("'", ","))
    if match:
        amount_str = match.group(1).replace(",", "").replace(".", "")
        return int(amount_str)
    return 0


def parse_date(text: str) -> str:
    """Parse date from format like '01.10.2022' to '2022-10-01'."""
    match = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", text)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
    return text


def fetch_snsf_data() -> dict:
    """Fetch and parse SNSF grant data using Playwright."""
    print(f"Fetching SNSF data from: {SNSF_URL}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(SNSF_URL, wait_until='networkidle', timeout=60000)
        page.wait_for_timeout(5000)  # Wait for JS to fully render

        # Get full page text
        main_text = ""
        main_el = page.query_selector('main, #app, [role="main"]')
        if main_el:
            main_text = main_el.inner_text()

        # Parse structured data
        data = {
            "fetched_at": datetime.now().isoformat(),
            "source_url": SNSF_URL,
            "grant_number": "205487",
        }

        # Extract key fields from text
        lines = main_text.split('\n')

        # Find funding amount
        for line in lines:
            if 'CHF' in line and any(c.isdigit() for c in line):
                amount = parse_funding_amount(line)
                if amount > 100000:  # Reasonable grant amount
                    data["approved_amount_chf"] = amount
                    break

        # Find status
        if 'Completed' in main_text:
            data["status"] = "Completed"
        elif 'Active' in main_text:
            data["status"] = "Active"

        # Find dates
        date_match = re.search(r"(\d{2}\.\d{2}\.\d{4})\s*[–-]\s*(\d{2}\.\d{2}\.\d{4})", main_text)
        if date_match:
            data["start_date"] = parse_date(date_match.group(1))
            data["end_date"] = parse_date(date_match.group(2))

        # Count outputs
        output_counts = {}
        patterns = [
            (r"(\d+)\s*Scientific publications?", "scientific_publications"),
            (r"(\d+)\s*Datasets?", "datasets"),
            (r"(\d+)\s*Collaborations?", "collaborations"),
            (r"(\d+)\s*Academic events?", "academic_events"),
            (r"(\d+)\s*Knowledge transfer events?", "knowledge_transfer_events"),
            (r"(\d+)\s*Public communications?", "public_communications"),
            (r"(\d+)\s*Use-inspired outputs?", "use_inspired_outputs"),
        ]

        for pattern, key in patterns:
            match = re.search(pattern, main_text, re.IGNORECASE)
            if match:
                output_counts[key] = int(match.group(1))

        if output_counts:
            data["output_counts"] = output_counts

        # Store raw text for reference
        data["raw_text"] = main_text[:10000]  # First 10k chars

        browser.close()

    return data


def load_current_data() -> dict:
    """Load current SNSF project data."""
    path = DATA_DIR / "snsf_project_complete.json"
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    return {}


def detect_changes(current: dict, fetched: dict) -> list:
    """Detect significant changes between current and fetched data."""
    changes = []

    # Check funding amount
    current_amount = current.get("project", {}).get("approved_amount_chf", 0)
    fetched_amount = fetched.get("approved_amount_chf", 0)
    if fetched_amount and current_amount != fetched_amount:
        changes.append({
            "field": "approved_amount_chf",
            "old": current_amount,
            "new": fetched_amount
        })

    # Check status
    current_status = current.get("project", {}).get("status", "")
    fetched_status = fetched.get("status", "")
    if fetched_status and current_status != fetched_status:
        changes.append({
            "field": "status",
            "old": current_status,
            "new": fetched_status
        })

    # Check output counts
    current_outputs = current.get("output_data", {})
    fetched_outputs = fetched.get("output_counts", {})
    for key, new_val in fetched_outputs.items():
        old_val = current_outputs.get(key, 0)
        if old_val != new_val:
            changes.append({
                "field": f"output_data.{key}",
                "old": old_val,
                "new": new_val
            })

    return changes


def update_config_yml(amount: int, status: str):
    """Update _config.yml with new funding amount and status."""
    config_path = PROJECT_ROOT / "_config.yml"
    content = config_path.read_text(encoding='utf-8')

    # Update funding
    content = re.sub(
        r'total_funding:\s*"[\d,]+ CHF"',
        f'total_funding: "{amount:,} CHF"',
        content
    )

    # Update or add status
    if 'status:' in content:
        content = re.sub(
            r'status:\s*"[^"]*"',
            f'status: "{status}"',
            content
        )
    else:
        content = re.sub(
            r'(total_funding:\s*"[^"]*")',
            f'\\1\n  status: "{status}"',
            content
        )

    config_path.write_text(content, encoding='utf-8')
    print(f"Updated _config.yml: funding={amount:,} CHF, status={status}")


def update_snsf_json(current: dict, fetched: dict) -> dict:
    """Update snsf_project_complete.json with fetched data."""
    # Update project section
    if "approved_amount_chf" in fetched:
        current["project"]["approved_amount_chf"] = fetched["approved_amount_chf"]
    if "status" in fetched:
        current["project"]["status"] = fetched["status"]

    # Update output counts
    if "output_counts" in fetched:
        for key, val in fetched["output_counts"].items():
            current["output_data"][key] = val

    # Add sync timestamp
    current["last_synced"] = fetched["fetched_at"]

    return current


def main():
    print("=" * 60)
    print("SNSF Data Sync")
    print("=" * 60)

    # Fetch new data
    fetched = fetch_snsf_data()
    print(f"\nFetched data:")
    print(f"  Amount: {fetched.get('approved_amount_chf', 'N/A'):,} CHF")
    print(f"  Status: {fetched.get('status', 'N/A')}")
    print(f"  Outputs: {fetched.get('output_counts', {})}")

    # Load current data
    current = load_current_data()

    # Detect changes
    changes = detect_changes(current, fetched)

    if not changes:
        print("\nNo changes detected. Data is up to date.")
        return 0

    print(f"\nDetected {len(changes)} change(s):")
    for change in changes:
        print(f"  {change['field']}: {change['old']} -> {change['new']}")

    # Update files
    print("\nUpdating files...")

    # Update _config.yml
    if any(c["field"] in ["approved_amount_chf", "status"] for c in changes):
        update_config_yml(
            fetched.get("approved_amount_chf", current["project"]["approved_amount_chf"]),
            fetched.get("status", current["project"]["status"])
        )

    # Update snsf_project_complete.json
    updated = update_snsf_json(current, fetched)
    json_path = DATA_DIR / "snsf_project_complete.json"
    json_path.write_text(json.dumps(updated, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Updated {json_path}")

    # Save fetched data for reference
    fetched_path = DATA_DIR / "snsf_fetched.json"
    fetched_path.write_text(json.dumps(fetched, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Saved fetched data to {fetched_path}")

    print("\nSync complete!")
    return len(changes)


if __name__ == "__main__":
    sys.exit(main())
