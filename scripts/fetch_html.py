#!/usr/bin/env python3
"""Fetch and analyze the live site HTML."""

import requests
from pathlib import Path

URL = "https://digital-ai-finance.github.io/network-based-credit-risk-models/"
OUTPUT = Path(__file__).parent.parent / "debug_live_site.html"

response = requests.get(URL)
print(f"Status: {response.status_code}")
print(f"Content length: {len(response.text)} chars")

# Save full HTML
OUTPUT.write_text(response.text, encoding='utf-8')
print(f"Saved to: {OUTPUT}")

# Check for section IDs
html = response.text
sections = ['home', 'team', 'research', 'publications', 'analytics', 'resources', 'news', 'events', 'collaborations', 'funding', 'contact']

print("\nSection presence in HTML:")
for section in sections:
    pattern = f'id="{section}"'
    found = pattern in html
    print(f"  {section}: {'FOUND' if found else 'MISSING'}")

# Check if content is truncated
if 'analytics' not in html:
    # Find what comes after publications section
    pub_idx = html.find('id="publications"')
    if pub_idx > 0:
        after_pub = html[pub_idx:pub_idx+5000]
        print(f"\nAfter publications section:\n{after_pub[:2000]}...")
