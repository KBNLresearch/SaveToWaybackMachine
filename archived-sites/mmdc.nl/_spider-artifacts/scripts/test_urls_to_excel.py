"""
Test all URLs and write HTTP status to Excel.
Updates mmdc-urls-UNIFIED.xlsx with Status column.
"""
import requests
import concurrent.futures
from collections import Counter
from openpyxl import Workbook
import csv
import time
import sys

def check_url(url):
    """Check URL and return status code."""
    try:
        response = requests.head(url, timeout=15, allow_redirects=True)
        return (url, response.status_code)
    except requests.exceptions.Timeout:
        return (url, 'TIMEOUT')
    except requests.exceptions.ConnectionError:
        return (url, 'CONN_ERR')
    except Exception as e:
        return (url, f'ERR')

def main():
    # Read CSV data
    print("Reading mmdc-urls-ALL.csv...")
    urls_data = []
    with open('../mmdc-urls-ALL.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            urls_data.append(row)

    total = len(urls_data)
    print(f"Testing {total} URLs...")
    print("This will take several minutes...")
    print()

    # Map URL to status
    url_status = {}
    results = Counter()
    tested = 0

    # Extract just URLs for testing
    urls = [item['URL'] for item in urls_data]

    # Test in batches
    batch_size = 100

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i+batch_size]
            futures = {executor.submit(check_url, url): url for url in batch}

            for future in concurrent.futures.as_completed(futures):
                url, status = future.result()
                url_status[url] = status
                results[status] += 1
                tested += 1

            # Progress update
            pct = (tested / total) * 100
            print(f"\rProgress: {tested}/{total} ({pct:.1f}%) - 200s: {results.get(200, 0)}", end='', flush=True)

            # Small delay between batches to be nice to the server
            time.sleep(0.3)

    print()
    print()
    print("="*60)
    print("RESULTS:")
    print("="*60)
    for status, count in sorted(results.items(), key=lambda x: -x[1]):
        print(f"  {status}: {count}")

    # Create new Excel with status
    print()
    print("Writing to Excel...")

    wb = Workbook()
    ws = wb.active
    ws.title = 'All URLs'

    # Headers
    headers = ['URL', 'Section', 'Title', 'HTTP_Status', 'Notes']
    ws.append(headers)

    # Add data with status
    for item in urls_data:
        url = item['URL']
        status = url_status.get(url, 'NOT_TESTED')
        ws.append([
            url,
            item.get('Section', ''),
            item.get('Title', ''),
            str(status),
            ''
        ])

    # Save
    wb.save('../mmdc-urls-UNIFIED.xlsx')
    print(f"Saved to mmdc-urls-UNIFIED.xlsx")

    # Also update CSV
    print("Updating CSV...")
    with open('../mmdc-urls-ALL.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['URL', 'Section', 'Title', 'HTTP_Status', 'Notes'])
        for item in urls_data:
            url = item['URL']
            status = url_status.get(url, 'NOT_TESTED')
            writer.writerow([
                url,
                item.get('Section', ''),
                item.get('Title', ''),
                str(status),
                ''
            ])
    print("Saved to mmdc-urls-ALL.csv")

    # Summary
    print()
    print("="*60)
    print("SUMMARY:")
    print(f"  Total URLs: {total}")
    print(f"  HTTP 200: {results.get(200, 0)}")
    print(f"  HTTP 404: {results.get(404, 0)}")
    print(f"  Other: {total - results.get(200, 0) - results.get(404, 0)}")
    print("="*60)

if __name__ == '__main__':
    main()
