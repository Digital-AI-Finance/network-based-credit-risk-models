#!/usr/bin/env python3
"""Check publications.json for HTML tags in abstracts."""

import json
from pathlib import Path
import re

pub_file = Path(__file__).parent.parent / "_data" / "publications.json"
data = json.loads(pub_file.read_text(encoding='utf-8'))

print("Checking for HTML tags in publications.json...\n")

for i, pub in enumerate(data):
    abstract = pub.get('abstract', '')
    title = pub.get('title', '')

    # Check for HTML-like patterns
    if '<' in abstract or '>' in abstract:
        print(f"[{i}] HTML in abstract: {title[:60]}...")
        print(f"    Abstract preview: {abstract[:200]}...\n")

    if '<' in title or '>' in title:
        print(f"[{i}] HTML in title: {title[:100]}\n")
