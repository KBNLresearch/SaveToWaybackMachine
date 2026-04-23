#!/usr/bin/env python3
"""
Generate catalog detail URLs from extracted record IDs.

Input: catalog-record-ids.txt
Output: catalog-urls.txt
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
IDS_FILE = BASE_DIR / "catalog-record-ids.txt"
URLS_FILE = BASE_DIR / "catalog-urls.txt"

# URL template for catalog detail pages
URL_TEMPLATE = "https://mmdc.nl/static/site/search/detail.html?recordId={id}#r{id}"


def main():
    """Generate catalog URLs from record IDs."""
    print("=" * 60)
    print("Generating Catalog URLs")
    print("=" * 60)

    # Read record IDs
    ids = IDS_FILE.read_text().strip().split("\n")
    print(f"Loaded {len(ids):,} record IDs")

    # Generate URLs
    urls = [URL_TEMPLATE.format(id=rid) for rid in ids]

    # Write to file
    URLS_FILE.write_text("\n".join(urls) + "\n")

    print(f"Generated {len(urls):,} catalog URLs")
    print(f"Output: {URLS_FILE}")
    print("=" * 60)

    # Show sample
    print("\nSample URLs:")
    for url in urls[:5]:
        print(f"  {url}")
    print("  ...")


if __name__ == "__main__":
    main()
