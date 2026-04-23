#!/usr/bin/env python3
"""
Combine all URLs into a comprehensive list for Wayback Machine archival.

Sources:
- all-crawled-urls.txt (438 static pages)
- catalog-urls.txt (11,738 catalog detail pages)
- pdf-urls.txt (63 PDF documents)
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

INPUT_FILES = [
    BASE_DIR / "all-crawled-urls.txt",
    BASE_DIR / "catalog-urls.txt",
    BASE_DIR / "pdf-urls.txt",
]

OUTPUT_FILE = BASE_DIR / "COMPLETE-url-list.txt"
SUMMARY_FILE = BASE_DIR / "URL-INVENTORY-SUMMARY.md"


def main():
    """Combine all URL sources."""
    print("=" * 60)
    print("Combining All URLs for Wayback Machine")
    print("=" * 60)

    all_urls = set()
    counts = {}

    for input_file in INPUT_FILES:
        if input_file.exists():
            urls = input_file.read_text().strip().split("\n")
            urls = [u for u in urls if u]  # Remove empty lines
            counts[input_file.stem] = len(urls)
            all_urls.update(urls)
            print(f"  {input_file.stem}: {len(urls):,} URLs")
        else:
            print(f"  {input_file.stem}: FILE NOT FOUND")
            counts[input_file.stem] = 0

    # Sort and save
    sorted_urls = sorted(all_urls)
    OUTPUT_FILE.write_text("\n".join(sorted_urls) + "\n")

    print("=" * 60)
    print(f"Total unique URLs: {len(sorted_urls):,}")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 60)

    # Create summary
    summary = f"""# MMDC.nl URL Inventory Summary

Generated: {__import__('datetime').datetime.now().isoformat()}

## URL Counts by Source

| Source | Count |
|--------|-------|
| Static Pages (crawled) | {counts.get('all-crawled-urls', 0):,} |
| Catalog Records (SRU API) | {counts.get('catalog-urls', 0):,} |
| PDF Documents | {counts.get('pdf-urls', 0):,} |
| **TOTAL UNIQUE** | **{len(sorted_urls):,}** |

## Files Generated

- `COMPLETE-url-list.txt` - All URLs for Wayback Machine submission
- `all-crawled-urls.txt` - URLs found by spider (static pages)
- `catalog-urls.txt` - Catalog detail page URLs
- `catalog-record-ids.txt` - Raw record IDs from SRU API
- `pdf-urls.txt` - PDF document URLs

## Key Discovery

The mmdc.nl catalog is a JavaScript SPA that loads data from KB's SRU API at:
```
https://jsru.kb.nl/sru/sru?x-collection=MISC&query=dcterms.isPartOf+adj+PTP
```

Record IDs range from 2 to 163,403 (sparse, non-sequential).

## Next Steps

1. Submit URLs to Wayback Machine (Save Page Now)
2. Verify archival success
3. Create local backup if needed

## Site Shutdown

mmdc.nl is scheduled to shut down on **December 15, 2025**.
"""

    SUMMARY_FILE.write_text(summary)
    print(f"Summary: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
