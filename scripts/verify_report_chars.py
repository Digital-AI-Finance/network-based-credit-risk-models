#!/usr/bin/env python3
"""
Verify character counts for SNSF Final Scientific Report sections.

SNSF Template Requirements:
- Section 1.1: max 6000 characters (with spaces)
- Section 1.2: max 2000 characters (with spaces)
- Section 1.3: max 2000 characters (with spaces)
"""

import re
from pathlib import Path


def extract_section_content(html_content: str, section_id: str) -> str:
    """Extract text content from a section, stripping HTML tags."""
    # Find section by looking for the section header
    patterns = {
        '1.1': r'1\.1 Achievement of research objectives.*?</div>\s*<div class="section-content">(.*?)</div>\s*(?=<!-- Section 1\.2|$)',
        '1.2': r'1\.2 Challenges, negative results.*?</div>\s*<div class="section-content">(.*?)</div>\s*(?=<!-- Section 1\.3|$)',
        '1.3': r'1\.3 Contribution to knowledge advancement.*?</div>\s*<div class="section-content">(.*?)</div>\s*(?=<!-- Collapsible|$)',
    }

    pattern = patterns.get(section_id)
    if not pattern:
        return ""

    match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
    if not match:
        return ""

    content = match.group(1)

    # Strip HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Normalize whitespace
    content = re.sub(r'\s+', ' ', content).strip()

    return content


def main():
    """Main function to verify character counts."""
    report_path = Path(__file__).parent.parent / 'final-report.md'

    if not report_path.exists():
        print(f"ERROR: Report file not found: {report_path}")
        return 1

    content = report_path.read_text(encoding='utf-8')

    limits = {
        '1.1': 6000,
        '1.2': 2000,
        '1.3': 2000,
    }

    print("=" * 60)
    print("SNSF Final Scientific Report - Character Count Verification")
    print("=" * 60)
    print()

    all_ok = True

    for section_id, limit in limits.items():
        section_content = extract_section_content(content, section_id)
        char_count = len(section_content)
        status = "OK" if char_count <= limit else "OVER LIMIT"

        if char_count > limit:
            all_ok = False
            status_symbol = "X"
        else:
            status_symbol = "V"

        print(f"Section {section_id}: {char_count:,} / {limit:,} chars - [{status_symbol}] {status}")

        if char_count > limit:
            over_by = char_count - limit
            print(f"           -> Over by {over_by} characters")

    print()
    print("-" * 60)

    if all_ok:
        print("RESULT: All sections within character limits")
    else:
        print("RESULT: Some sections exceed character limits - NEEDS TRIMMING")

    print("=" * 60)

    return 0 if all_ok else 1


if __name__ == '__main__':
    exit(main())
