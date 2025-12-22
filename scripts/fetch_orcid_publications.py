#!/usr/bin/env python3
"""
Fetch publications from ORCID for PhD researchers.
Uses ORCID Public API (no authentication required).
"""

import json
import requests
from pathlib import Path

# ORCID identifiers for PhD researchers
ORCIDS = {
    "Lennart John Baals": "0000-0002-7737-9675",
    "Yiting Liu": "0009-0006-9554-8205"
}

OUTPUT_PATH = Path(__file__).parent.parent / "_data" / "phd_publications.json"

def fetch_orcid_works(orcid: str) -> list:
    """Fetch all works from ORCID Public API."""
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching ORCID {orcid}: {response.status_code}")
        return []

    data = response.json()
    return data.get("group", [])

def extract_publication_details(work_group: dict) -> dict:
    """Extract publication details from a work group."""
    work_summary = work_group.get("work-summary", [{}])[0]

    # Get title
    title_info = work_summary.get("title", {})
    title = title_info.get("title", {}).get("value", "Untitled")

    # Get publication year
    pub_date = work_summary.get("publication-date", {})
    year = pub_date.get("year", {}).get("value", "") if pub_date else ""

    # Get type
    work_type = work_summary.get("type", "other")

    # Get journal name
    journal = work_summary.get("journal-title", {})
    journal_name = journal.get("value", "") if journal else ""

    # Get external IDs (DOI, etc.)
    external_ids = work_summary.get("external-ids", {}).get("external-id", [])
    doi = None
    for ext_id in external_ids:
        if ext_id.get("external-id-type") == "doi":
            doi = ext_id.get("external-id-value")
            break

    # Get put-code for fetching full details
    put_code = work_summary.get("put-code")

    return {
        "title": title,
        "year": year,
        "type": work_type,
        "journal": journal_name,
        "doi": doi,
        "doi_url": f"https://doi.org/{doi}" if doi else None,
        "put_code": put_code
    }

def fetch_work_abstract(orcid: str, put_code: int) -> str:
    """Fetch abstract for a specific work."""
    url = f"https://pub.orcid.org/v3.0/{orcid}/work/{put_code}"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return ""

    data = response.json()
    short_desc = data.get("short-description")
    return short_desc if short_desc else ""

def format_citation(pub: dict, author: str) -> str:
    """Format publication as citation string."""
    parts = [author]
    if pub["year"]:
        parts.append(f"({pub['year']})")
    parts.append(f'"{pub["title"]}"')
    if pub["journal"]:
        parts.append(pub["journal"])
    if pub["doi"]:
        parts.append(f"DOI: {pub['doi']}")
    return ". ".join(parts) + "."

def format_citation_multi(pub: dict, authors: str) -> str:
    """Format publication as citation string with multiple authors."""
    parts = [authors]
    if pub.get("year"):
        parts.append(f"({pub['year']})")
    parts.append(f'"{pub["title"]}"')
    if pub.get("journal"):
        parts.append(pub["journal"])
    if pub.get("doi"):
        parts.append(f"DOI: {pub['doi']}")
    return ". ".join(parts) + "."

def main():
    all_publications = []

    for author, orcid in ORCIDS.items():
        print(f"\nFetching publications for {author} (ORCID: {orcid})...")

        works = fetch_orcid_works(orcid)
        print(f"  Found {len(works)} works")

        for work_group in works:
            pub = extract_publication_details(work_group)
            pub["author"] = author
            pub["orcid"] = orcid

            # Fetch abstract if put_code available
            if pub.get("put_code"):
                abstract = fetch_work_abstract(orcid, pub["put_code"])
                pub["abstract"] = abstract
                del pub["put_code"]  # Remove put_code from output

            pub["citation"] = format_citation(pub, author)
            all_publications.append(pub)
            print(f"  - {pub['title'][:60]}...")

    # Deduplicate by DOI (co-authored papers appear for both authors)
    unique_pubs = {}
    for pub in all_publications:
        doi = pub.get("doi")
        if doi:
            if doi not in unique_pubs:
                unique_pubs[doi] = pub
                unique_pubs[doi]["authors"] = [pub["author"]]
            else:
                if pub["author"] not in unique_pubs[doi]["authors"]:
                    unique_pubs[doi]["authors"].append(pub["author"])
        else:
            # No DOI, keep as separate entry
            key = pub["title"][:50]
            unique_pubs[key] = pub
            unique_pubs[key]["authors"] = [pub["author"]]

    all_publications = list(unique_pubs.values())

    # Update citations to include all authors
    for pub in all_publications:
        authors_str = ", ".join(pub.get("authors", [pub.get("author", "")]))
        pub["citation"] = format_citation_multi(pub, authors_str)

    # Sort by year (descending)
    all_publications.sort(key=lambda x: x.get("year", "0000"), reverse=True)

    # Save to JSON
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_publications, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(all_publications)} publications to {OUTPUT_PATH}")

    # Print summary
    print("\n--- Publication Summary ---")
    for author in ORCIDS.keys():
        count = len([p for p in all_publications if p["author"] == author])
        print(f"{author}: {count} publications")

    return all_publications

if __name__ == "__main__":
    main()
