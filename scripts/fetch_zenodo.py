"""
Fetch metadata from Zenodo API for research outputs.
Creates _data/research_outputs.json with title, description, creators, etc.
"""
import json
import re
import requests
from pathlib import Path

# Zenodo DOIs - DO NOT MODIFY THESE URLs
ZENODO_DOIS = [
    "https://doi.org/10.5281/zenodo.17964900",
    "https://doi.org/10.5281/zenodo.17990398",
    "https://doi.org/10.5281/zenodo.17990873",
    "https://doi.org/10.5281/zenodo.17991107",
    "https://doi.org/10.5281/zenodo.17992215",
    "https://doi.org/10.5281/zenodo.17992322",
    "https://doi.org/10.5281/zenodo.17992484",
    "https://doi.org/10.5281/zenodo.17992591",
    "https://doi.org/10.5281/zenodo.17989119",
    "https://doi.org/10.5281/zenodo.17990002",
    "https://doi.org/10.5281/zenodo.17990140",
    "https://doi.org/10.5281/zenodo.17990581",
]

ZENODO_API_BASE = "https://zenodo.org/api/records"


def extract_record_id(doi_url: str) -> str:
    """Extract Zenodo record ID from DOI URL."""
    match = re.search(r"zenodo\.(\d+)$", doi_url)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract record ID from: {doi_url}")


def fetch_zenodo_metadata(record_id: str) -> dict:
    """Fetch metadata from Zenodo API for a given record ID."""
    url = f"{ZENODO_API_BASE}/{record_id}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def clean_html(text: str) -> str:
    """Remove HTML tags and decode HTML entities from text."""
    import html
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", "", text)
    clean = html.unescape(clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    # Add space after "Overview" if missing
    clean = re.sub(r"^Overview(?=[A-Z])", "Overview ", clean)
    return clean


def process_metadata(doi_url: str, data: dict) -> dict:
    """Process Zenodo API response into our format."""
    metadata = data.get("metadata", {})

    creators = []
    for creator in metadata.get("creators", []):
        name = creator.get("name", "")
        if name:
            creators.append(name)

    resource_type = metadata.get("resource_type", {})
    type_title = resource_type.get("title", "Unknown")

    description = clean_html(metadata.get("description", ""))

    keywords = metadata.get("keywords", [])

    license_info = metadata.get("license", {})
    license_id = license_info.get("id", "") if isinstance(license_info, dict) else str(license_info)

    return {
        "doi": doi_url,
        "record_id": str(data.get("id", "")),
        "title": metadata.get("title", "Untitled"),
        "description": description,
        "creators": creators,
        "resource_type": type_title,
        "publication_date": metadata.get("publication_date", ""),
        "keywords": keywords,
        "license": license_id,
        "zenodo_url": data.get("links", {}).get("html", f"https://zenodo.org/records/{data.get('id', '')}")
    }


def main():
    """Main function to fetch all Zenodo metadata and save to JSON."""
    script_dir = Path(__file__).parent
    output_path = script_dir.parent / "_data" / "research_outputs.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    outputs = []

    for doi_url in ZENODO_DOIS:
        print(f"Fetching: {doi_url}")
        try:
            record_id = extract_record_id(doi_url)
            data = fetch_zenodo_metadata(record_id)
            processed = process_metadata(doi_url, data)
            outputs.append(processed)
            print(f"  -> {processed['title'][:60]}...")
        except Exception as e:
            print(f"  ERROR: {e}")
            outputs.append({
                "doi": doi_url,
                "record_id": extract_record_id(doi_url) if "zenodo" in doi_url else "",
                "title": "Error fetching metadata",
                "description": str(e),
                "creators": [],
                "resource_type": "Unknown",
                "publication_date": "",
                "keywords": [],
                "license": "",
                "zenodo_url": doi_url
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(outputs, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(outputs)} records to: {output_path}")


if __name__ == "__main__":
    main()
