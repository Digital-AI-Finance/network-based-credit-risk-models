#!/usr/bin/env python3
"""Fix publications.json by removing HTML tags from abstracts."""

import json
from pathlib import Path
import re
import html

pub_file = Path(__file__).parent.parent / "_data" / "publications.json"
data = json.loads(pub_file.read_text(encoding='utf-8'))

print("Fixing HTML tags in publications.json...\n")
fixed = 0

for i, pub in enumerate(data):
    abstract = pub.get('abstract', '')
    title = pub.get('title', '')

    # Clean abstract: remove HTML tags and unescape entities
    if abstract:
        original = abstract
        # Remove XML/HTML tags
        cleaned = re.sub(r'<[^>]+>', '', abstract)
        # Unescape HTML entities
        cleaned = html.unescape(cleaned)
        # Clean up extra whitespace
        cleaned = ' '.join(cleaned.split())

        if cleaned != original:
            pub['abstract'] = cleaned
            print(f"[{i}] Fixed abstract: {title[:50]}...")
            fixed += 1

    # Clean title: remove HTML tags and unescape entities
    if title:
        original = title
        cleaned = re.sub(r'<[^>]+>', '', title)
        cleaned = html.unescape(cleaned)
        cleaned = ' '.join(cleaned.split())

        if cleaned != original:
            pub['title'] = cleaned
            print(f"[{i}] Fixed title")
            fixed += 1

# Save fixed data
pub_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"\nFixed {fixed} entries. Saved to {pub_file}")
