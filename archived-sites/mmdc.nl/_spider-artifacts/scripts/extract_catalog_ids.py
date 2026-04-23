#!/usr/bin/env python3
"""
Extract all record IDs from KB's SRU API for the PTP (mmdc.nl) collection.

The mmdc.nl site uses the KB's SRU API at jsru.kb.nl with collection=MISC
and filters by dcterms.isPartOf=PTP to get manuscript records.

Output: catalog-record-ids.txt (one ID per line)
"""

import requests
import time
from pathlib import Path

# SRU API configuration
SRU_BASE = "https://jsru.kb.nl/sru/sru"
COLLECTION = "MISC"
QUERY = "dcterms.isPartOf adj PTP"
BATCH_SIZE = 100  # Max allowed by API
OUTPUT_FILE = Path(__file__).parent.parent / "catalog-record-ids.txt"

def fetch_record_ids(start_record: int, max_records: int = BATCH_SIZE) -> list[str]:
    """Fetch a batch of record IDs from SRU API."""
    params = {
        "x-collection": COLLECTION,
        "operation": "searchRetrieve",
        "version": "1.2",
        "recordSchema": "dcx admin",
        "query": QUERY,
        "maximumRecords": max_records,
        "startRecord": start_record,
    }

    response = requests.get(SRU_BASE, params=params, timeout=60)
    response.raise_for_status()

    # Parse XML response - extract dc:identifier values
    import re
    ids = re.findall(r'<dc:identifier>(\d+)</dc:identifier>', response.text)
    return ids


def get_total_records() -> int:
    """Get total number of records in collection."""
    params = {
        "x-collection": COLLECTION,
        "operation": "searchRetrieve",
        "version": "1.2",
        "recordSchema": "dcx admin",
        "query": QUERY,
        "maximumRecords": 1,
    }

    response = requests.get(SRU_BASE, params=params, timeout=60)
    response.raise_for_status()

    import re
    match = re.search(r'<srw:numberOfRecords>(\d+)</srw:numberOfRecords>', response.text)
    return int(match.group(1)) if match else 0


def main():
    """Extract all record IDs."""
    print("=" * 60)
    print("MMDC Catalog Record ID Extractor")
    print("=" * 60)

    # Get total count
    total = get_total_records()
    print(f"Total records in PTP collection: {total:,}")

    all_ids = set()
    start = 1

    while start <= total:
        print(f"Fetching records {start:,} - {start + BATCH_SIZE - 1:,}...")

        try:
            ids = fetch_record_ids(start)
            all_ids.update(ids)
            print(f"  Got {len(ids)} IDs (total unique: {len(all_ids):,})")
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(5)
            continue

        start += BATCH_SIZE
        time.sleep(0.5)  # Be polite

    # Write to file
    sorted_ids = sorted(all_ids, key=int)
    OUTPUT_FILE.write_text("\n".join(sorted_ids) + "\n")

    print("=" * 60)
    print(f"Extracted {len(sorted_ids):,} unique record IDs")
    print(f"ID range: {sorted_ids[0]} - {sorted_ids[-1]}")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
