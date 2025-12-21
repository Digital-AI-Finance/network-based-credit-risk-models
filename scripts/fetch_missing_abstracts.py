#!/usr/bin/env python3
"""
Fetch missing abstracts from OpenAlex API for publications.json
"""
import json
import time
import requests
from pathlib import Path

def fetch_abstract_from_openalex(openalex_id: str) -> str:
    """Fetch abstract from OpenAlex API using the work ID."""
    if not openalex_id:
        return ""

    # Convert ID format if needed (W1234567890 -> https://openalex.org/W1234567890)
    work_id = openalex_id if openalex_id.startswith('W') else openalex_id.split('/')[-1]
    url = f"https://api.openalex.org/works/{work_id}"

    try:
        response = requests.get(url, headers={
            'User-Agent': 'NetworkCreditRiskProject/1.0 (mailto:joerg.osterrieder@bfh.ch)'
        })
        if response.status_code == 200:
            data = response.json()
            # Try to get abstract from inverted index
            abstract_inverted = data.get('abstract_inverted_index', {})
            if abstract_inverted:
                # Reconstruct abstract from inverted index
                word_positions = []
                for word, positions in abstract_inverted.items():
                    for pos in positions:
                        word_positions.append((pos, word))
                word_positions.sort(key=lambda x: x[0])
                abstract = ' '.join([w for _, w in word_positions])
                # Truncate if too long
                if len(abstract) > 500:
                    abstract = abstract[:497] + "..."
                return abstract
        return ""
    except Exception as e:
        print(f"  Error fetching {work_id}: {e}")
        return ""

def main():
    # Path to publications.json
    script_dir = Path(__file__).parent
    pub_file = script_dir.parent / '_data' / 'publications.json'

    print(f"Loading publications from {pub_file}")
    with open(pub_file, 'r', encoding='utf-8') as f:
        publications = json.load(f)

    # Find publications with empty abstracts
    empty_abstracts = [(i, p) for i, p in enumerate(publications)
                       if not p.get('abstract') or p.get('abstract', '').strip() == '']

    print(f"Found {len(empty_abstracts)} publications with empty abstracts out of {len(publications)} total")

    updated_count = 0
    for i, pub in empty_abstracts:
        openalex_id = pub.get('openalex_id', '')
        if not openalex_id:
            continue

        print(f"Fetching abstract for: {pub.get('title', 'Unknown')[:60]}...")
        abstract = fetch_abstract_from_openalex(openalex_id)

        if abstract:
            publications[i]['abstract'] = abstract
            updated_count += 1
            print(f"  -> Got abstract ({len(abstract)} chars)")
        else:
            print(f"  -> No abstract available")

        # Rate limiting - be nice to OpenAlex API
        time.sleep(0.5)

    # Save updated publications
    print(f"\nUpdated {updated_count} abstracts")
    with open(pub_file, 'w', encoding='utf-8') as f:
        json.dump(publications, f, indent=2, ensure_ascii=False)

    print(f"Saved to {pub_file}")

if __name__ == '__main__':
    main()
