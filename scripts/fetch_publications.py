"""
Fetch publications from OpenAlex.org for team members
Outputs to _data/publications.json for Jekyll site
"""

import requests
import json
from pathlib import Path
from datetime import datetime

# Configuration
OUTPUT_FILE = Path(__file__).parent.parent / "_data" / "publications.json"
OUTPUT_FILE.parent.mkdir(exist_ok=True)

# Team members to search
TEAM_MEMBERS = [
    {"name": "Joerg Osterrieder", "affiliation": "Bern"},
    {"name": "Lennart John Baals", "affiliation": "Bern"},
    {"name": "Branka Hadji Misheva", "affiliation": "Bern"},
    {"name": "Yiting Liu", "affiliation": "Twente"},
]

# OpenAlex API settings
OPENALEX_BASE = "https://api.openalex.org"
HEADERS = {"User-Agent": "mailto:research@digital-finance.org"}

def search_author(name, affiliation=None):
    """Search for author ID by name"""
    url = f"{OPENALEX_BASE}/authors"
    params = {"search": name, "per_page": 10}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=30)
        response.raise_for_status()
        data = response.json()

        if data.get("results"):
            # Try to find best match (with affiliation if provided)
            for author in data["results"]:
                if affiliation:
                    affiliations = author.get("affiliations", [])
                    aff_names = [a.get("institution", {}).get("display_name", "") for a in affiliations]
                    if any(affiliation.lower() in aff.lower() for aff in aff_names):
                        return author.get("id")
                else:
                    return author.get("id")
            # Return first result if no affiliation match
            return data["results"][0].get("id")
    except Exception as e:
        print(f"  Error searching for {name}: {e}")

    return None

def get_author_works(author_id, limit=50):
    """Get works by author ID"""
    url = f"{OPENALEX_BASE}/works"
    params = {
        "filter": f"author.id:{author_id}",
        "sort": "publication_date:desc",
        "per_page": limit
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.json().get("results", [])
    except Exception as e:
        print(f"  Error fetching works: {e}")

    return []

def format_authors(authorships):
    """Format author list"""
    authors = []
    for a in authorships[:5]:  # Limit to first 5 authors
        author = a.get("author", {})
        name = author.get("display_name", "")
        if name:
            # Convert to "Last, F." format
            parts = name.split()
            if len(parts) >= 2:
                formatted = f"{parts[-1]}, {parts[0][0]}."
            else:
                formatted = name
            authors.append(formatted)

    if len(authorships) > 5:
        authors.append("et al.")

    return ", ".join(authors)

def process_work(work):
    """Extract relevant fields from a work"""
    # Get journal/source
    primary_location = work.get("primary_location", {}) or {}
    source = primary_location.get("source", {}) or {}
    journal = source.get("display_name", "")

    # Get DOI
    doi = work.get("doi", "")
    if doi and doi.startswith("https://doi.org/"):
        doi = doi.replace("https://doi.org/", "")

    # Get publication year
    pub_date = work.get("publication_date", "")
    year = int(pub_date[:4]) if pub_date else None

    return {
        "title": work.get("title", ""),
        "authors": format_authors(work.get("authorships", [])),
        "journal": journal,
        "year": year,
        "doi": doi,
        "citations": work.get("cited_by_count", 0),
        "openalex_id": work.get("id", "").replace("https://openalex.org/", ""),
        "type": work.get("type", ""),
        "open_access": work.get("open_access", {}).get("is_oa", False),
    }

def fetch_all_publications():
    """Fetch publications for all team members"""
    all_publications = {}

    print("Fetching publications from OpenAlex.org...")
    print("=" * 50)

    for member in TEAM_MEMBERS:
        name = member["name"]
        affiliation = member.get("affiliation")

        print(f"\nSearching: {name}")
        author_id = search_author(name, affiliation)

        if not author_id:
            print(f"  Author not found")
            continue

        print(f"  Found: {author_id}")
        works = get_author_works(author_id)
        print(f"  Works: {len(works)}")

        for work in works:
            processed = process_work(work)
            if processed["title"] and processed["openalex_id"]:
                # Use OpenAlex ID as key to avoid duplicates
                all_publications[processed["openalex_id"]] = processed

    # Convert to list and sort by year (newest first)
    publications = list(all_publications.values())
    publications.sort(key=lambda x: (x.get("year") or 0, x.get("citations") or 0), reverse=True)

    # Filter to recent publications (last 5 years)
    current_year = datetime.now().year
    publications = [p for p in publications if p.get("year") and p["year"] >= current_year - 5]

    return publications

def main():
    publications = fetch_all_publications()

    print(f"\n{'=' * 50}")
    print(f"Total unique publications: {len(publications)}")

    # Save to JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(publications, f, indent=2, ensure_ascii=False)

    print(f"Saved to: {OUTPUT_FILE}")

    # Print summary
    print(f"\nTop 5 publications:")
    for i, pub in enumerate(publications[:5], 1):
        print(f"  {i}. {pub['title'][:60]}... ({pub['year']}, {pub['citations']} citations)")

if __name__ == "__main__":
    main()
