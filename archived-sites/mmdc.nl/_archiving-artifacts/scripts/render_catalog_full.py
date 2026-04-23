#!/usr/bin/env python3
"""
Render all mmdc.nl catalog pages to clean standalone HTML files.

Features:
- Resume capability: tracks progress, skips already-rendered pages
- Network resilience: retries on failure, continues on error
- Progress reporting: periodic status updates
- Error logging: saves failed IDs for later retry

Usage:
    python render_catalog_full.py              # Full run (11,738 pages)
    python render_catalog_full.py --test 100   # Test with first 100 pages
    python render_catalog_full.py --resume     # Resume interrupted run
"""

import os
import re
import sys
import json
import base64
import time
import requests
import argparse
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# Configuration
BASE_URL = "https://mmdc.nl"
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "rendered-catalog-pages"
PROGRESS_FILE = SCRIPT_DIR.parent / "data" / "render-progress.json"
ERROR_LOG = SCRIPT_DIR.parent / "data" / "render-errors.json"
EXCEL_FILE = SCRIPT_DIR.parent.parent / "mmdc-urls-UNIFIED.xlsx"

# Ensure directories exist
OUTPUT_DIR.mkdir(exist_ok=True)
(SCRIPT_DIR.parent / "data").mkdir(exist_ok=True)

# Rendering settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
PROGRESS_REPORT_INTERVAL = 10  # Report every N pages


def load_record_ids():
    """Load all record IDs from the Excel file."""
    try:
        import openpyxl
        wb = openpyxl.load_workbook(EXCEL_FILE, read_only=True, data_only=True)
        ws = wb.active

        record_ids = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[0] and str(row[0]).startswith("https://mmdc.nl/static/site/search/detail.html"):
                url = str(row[0])
                match = re.search(r'recordId=(\d+)', url)
                if match:
                    record_ids.append(int(match.group(1)))

        wb.close()
        print(f"Loaded {len(record_ids)} record IDs from Excel")
        return sorted(set(record_ids))
    except Exception as e:
        print(f"ERROR loading Excel: {e}")
        return []


def load_progress():
    """Load progress from previous run."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"completed": [], "failed": [], "last_id": None}


def save_progress(progress):
    """Save progress to file."""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)


def save_errors(errors):
    """Save error log."""
    with open(ERROR_LOG, 'w') as f:
        json.dump(errors, f, indent=2)


def fetch_css(url):
    """Fetch CSS file and return content."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass
    return ""


def remove_shutdown_banner(html):
    """Remove the shutdown banner from the HTML."""
    banner_pattern = r'<div><div style="[^"]*border:2px solid red[^"]*"[^>]*>.*?As of 15 December 2025.*?</div></div>'
    html = re.sub(banner_pattern, '', html, flags=re.DOTALL | re.IGNORECASE)
    return html


def remove_external_scripts(html):
    """Remove external script tags."""
    relative_pattern = r'<script[^>]*/static/assets/scripts/[^>]*>[^<]*</script>'
    html = re.sub(relative_pattern, '<!-- Script removed -->', html, flags=re.IGNORECASE)

    absolute_pattern = r'<script[^>]*mmdc\.nl[^>]*>[^<]*</script>'
    html = re.sub(absolute_pattern, '<!-- Script removed -->', html, flags=re.IGNORECASE)

    tracking_pattern = r'<script[^>]*(matomo|webstatistieken)[^>]*>[^<]*</script>'
    html = re.sub(tracking_pattern, '<!-- Tracking removed -->', html, flags=re.IGNORECASE)

    return html


def get_mime_type(url):
    """Get MIME type from URL extension."""
    ext = url.lower().split('.')[-1].split('?')[0]
    mime_types = {
        'gif': 'image/gif', 'png': 'image/png', 'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg', 'svg': 'image/svg+xml', 'ico': 'image/x-icon',
        'webp': 'image/webp',
    }
    return mime_types.get(ext, 'application/octet-stream')


def embed_images_as_base64(html, base_url):
    """Find all image src attributes and embed them as base64 data URIs.

    ROBUST VERSION: Retries failed fetches and logs failures.
    """
    page_dir = "/static/site/search"
    failed_images = []

    def resolve_relative_path(src):
        """Resolve relative paths like ../../assets/images/logo.gif"""
        if src.startswith('http'):
            return src
        if src.startswith('/'):
            return f"{base_url}{src}"
        if src.startswith('../') or src.startswith('./'):
            # Resolve relative to page directory
            full_path = f"{page_dir}/{src}"
            # Normalize path (resolve .. and .)
            parts = full_path.split('/')
            result = []
            for part in parts:
                if part == '..':
                    if result and result[-1] != '':
                        result.pop()
                elif part != '.' and part != '':
                    result.append(part)
            return f"{base_url}/{'/'.join(result)}"
        return f"{base_url}/{src}"

    def fetch_with_retry(url, max_retries=3):
        """Fetch URL with retry logic."""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=20)
                if response.status_code == 200:
                    return response
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(1)  # Wait before retry
        return None

    def replace_image(match):
        full_attr = match.group(0)
        src = match.group(1)

        # Skip already embedded
        if src.startswith('data:'):
            return full_attr

        # Resolve URL
        img_url = resolve_relative_path(src)

        response = fetch_with_retry(img_url)
        if response:
            # Detect mime type from content-type header or URL
            content_type = response.headers.get('content-type', '')
            if 'image/' in content_type:
                mime_type = content_type.split(';')[0].strip()
            else:
                mime_type = get_mime_type(img_url)
                if mime_type == 'application/octet-stream':
                    # Try to detect from content
                    content = response.content[:20]
                    if content.startswith(b'GIF'):
                        mime_type = 'image/gif'
                    elif content.startswith(b'\x89PNG'):
                        mime_type = 'image/png'
                    elif content.startswith(b'\xff\xd8'):
                        mime_type = 'image/jpeg'
                    else:
                        mime_type = 'image/jpeg'  # Default fallback

            b64_data = base64.b64encode(response.content).decode('utf-8')
            return f'src="data:{mime_type};base64,{b64_data}"'
        else:
            # Failed even after retries - log and keep original
            failed_images.append(img_url)
            print(f"    WARNING: Failed to embed image: {img_url}")
            return full_attr

    def replace_in_img(match):
        img_tag = match.group(0)
        src_match = re.search(r'src="([^"]+)"', img_tag)
        if src_match:
            old_src = f'src="{src_match.group(1)}"'
            new_src = replace_image(src_match)
            return img_tag.replace(old_src, new_src)
        return img_tag

    html = re.sub(r'<img[^>]+>', replace_in_img, html, flags=re.IGNORECASE)

    if failed_images:
        print(f"    FAILED to embed {len(failed_images)} images")

    return html


def normalize_path(path):
    """Resolve .. and . in paths."""
    parts = path.split('/')
    result = []
    for part in parts:
        if part == '..':
            if result and result[-1] != '':
                result.pop()
        elif part != '.':
            result.append(part)
    return '/'.join(result)


def make_urls_absolute(html, base_url):
    """Convert relative URLs to absolute URLs."""
    page_dir = "/static/site/search"

    def resolve_relative(match, attr, base_path):
        rel_path = match.group(1)
        full_path = f"{base_path}/{rel_path}"
        normalized = normalize_path(full_path)
        return f'{attr}="{base_url}{normalized}"'

    html = re.sub(r'href="(?!http)(?!#)(/[^"]*)"',
                  lambda m: f'href="{base_url}{normalize_path(m.group(1))}"', html)
    html = re.sub(r'href="(?!http)(?!#)(?!/)(\.\.\?/[^"]*)"',
                  lambda m: resolve_relative(m, 'href', page_dir), html)
    html = re.sub(r'src="(?!http)(?!data:)(/[^"]*)"',
                  lambda m: f'src="{base_url}{normalize_path(m.group(1))}"', html)
    html = re.sub(r'src="(?!http)(?!data:)(\.\.\?/[^"]*)"',
                  lambda m: resolve_relative(m, 'src', page_dir), html)

    return html


def render_page(browser, record_id, retry_count=0):
    """Render a single catalog page with retry logic."""
    url = f"https://mmdc.nl/static/site/search/detail.html?recordId={record_id}"

    page = browser.new_page()

    try:
        page.goto(url, wait_until="networkidle", timeout=60000)

        # Wait for content
        try:
            page.wait_for_selector("#recordDetail:not(:empty)", timeout=30000)
            page.wait_for_timeout(2000)
        except Exception:
            pass

        # Check if content loaded
        content_check = page.evaluate("document.getElementById('recordDetail')?.innerHTML?.length || 0")
        if content_check < 100:
            page.close()
            if retry_count < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                return render_page(browser, record_id, retry_count + 1)
            return None, f"No content (only {content_check} chars)"

        # Get full HTML with inlined CSS
        full_html = page.evaluate("""() => {
            let inlineCSS = '';
            for (let sheet of document.styleSheets) {
                try {
                    if (sheet.cssRules) {
                        for (let rule of sheet.cssRules) {
                            inlineCSS += rule.cssText + '\\n';
                        }
                    }
                } catch (e) {}
            }

            const doctype = '<!DOCTYPE html>';
            const head = document.head.innerHTML;
            const body = document.body.innerHTML;

            return doctype + '\\n<html>\\n<head>\\n' + head +
                   '\\n<style>\\n/* Inlined CSS */\\n' + inlineCSS + '\\n</style>\\n</head>\\n<body>\\n' +
                   body + '\\n</body>\\n</html>';
        }""")

        css_links = page.evaluate("""() => {
            const links = [];
            for (const link of document.querySelectorAll('link[rel="stylesheet"]')) {
                links.push(link.href);
            }
            return links;
        }""")

        page.close()

        # Fetch external CSS
        extra_css = ""
        for css_url in css_links:
            css_content = fetch_css(css_url)
            if css_content:
                extra_css += f"\n/* From: {css_url} */\n{css_content}\n"

        if extra_css:
            full_html = full_html.replace("</style>\n</head>", f"{extra_css}</style>\n</head>")

        # Apply transformations
        full_html = remove_shutdown_banner(full_html)
        full_html = remove_external_scripts(full_html)
        full_html = make_urls_absolute(full_html, BASE_URL)
        full_html = embed_images_as_base64(full_html, BASE_URL)

        return full_html, None

    except Exception as e:
        page.close()
        if retry_count < MAX_RETRIES:
            time.sleep(RETRY_DELAY)
            return render_page(browser, record_id, retry_count + 1)
        return None, str(e)


def main():
    parser = argparse.ArgumentParser(description='Render mmdc.nl catalog pages')
    parser.add_argument('--test', type=int, help='Test with first N pages')
    parser.add_argument('--resume', action='store_true', help='Resume from last run')
    args = parser.parse_args()

    print("=" * 70)
    print("MMDC.NL CATALOG PAGE RENDERER")
    print("=" * 70)
    print(f"Start time: {datetime.now().isoformat()}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Load record IDs
    all_record_ids = load_record_ids()
    if not all_record_ids:
        print("ERROR: No record IDs found!")
        return

    # Load or initialize progress
    progress = load_progress() if args.resume else {"completed": [], "failed": [], "last_id": None}
    errors = []

    # Determine which IDs to process
    if args.test:
        record_ids = all_record_ids[:args.test]
        print(f"TEST MODE: Processing first {args.test} pages")
    else:
        record_ids = all_record_ids
        print(f"FULL MODE: Processing all {len(all_record_ids)} pages")

    # Skip already completed
    completed_set = set(progress["completed"])
    to_process = [rid for rid in record_ids if rid not in completed_set]

    print(f"Already completed: {len(completed_set)}")
    print(f"To process: {len(to_process)}")
    print()

    if not to_process:
        print("All pages already rendered!")
        return

    # Start rendering
    success_count = 0
    fail_count = 0
    start_time = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for i, record_id in enumerate(to_process, 1):
            # Progress report
            if i % PROGRESS_REPORT_INTERVAL == 0 or i == 1:
                elapsed = time.time() - start_time
                rate = i / elapsed if elapsed > 0 else 0
                eta = (len(to_process) - i) / rate if rate > 0 else 0
                print(f"\n[PROGRESS] {i}/{len(to_process)} ({100*i/len(to_process):.1f}%) | "
                      f"Success: {success_count} | Failed: {fail_count} | "
                      f"Rate: {rate:.1f}/sec | ETA: {eta/60:.1f} min")

            # Check if file already exists
            output_path = OUTPUT_DIR / f"catalog-page-{record_id}.html"
            if output_path.exists():
                print(f"  Skip {record_id}: already exists")
                progress["completed"].append(record_id)
                success_count += 1
                continue

            # Render
            html, error = render_page(browser, record_id)

            if html:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"  OK {record_id}: {len(html):,} bytes")
                progress["completed"].append(record_id)
                success_count += 1
            else:
                print(f"  FAIL {record_id}: {error}")
                progress["failed"].append(record_id)
                errors.append({"id": record_id, "error": error, "time": datetime.now().isoformat()})
                fail_count += 1

            # Save progress periodically
            if i % 50 == 0:
                progress["last_id"] = record_id
                save_progress(progress)
                if errors:
                    save_errors(errors)

        browser.close()

    # Final save
    save_progress(progress)
    if errors:
        save_errors(errors)

    # Summary
    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total processed: {len(to_process)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Time elapsed: {elapsed/60:.1f} minutes")
    print(f"Average rate: {len(to_process)/elapsed:.2f} pages/sec")
    print()
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Progress file: {PROGRESS_FILE}")
    if errors:
        print(f"Error log: {ERROR_LOG}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
