#!/usr/bin/env python3
"""
Render static HTML pages from mmdc.nl with Playwright.

This script:
1. Loads static page URLs from the Excel file (non-catalog pages)
2. Renders each page with Playwright (to execute JavaScript)
3. Removes the shutdown banner div injected by default.js
4. Embeds images as BASE64
5. Removes external script tags
6. Saves clean standalone HTML files

Usage:
    python render_static_pages.py              # Render all static pages
    python render_static_pages.py --test 10    # Test with first 10 pages
    python render_static_pages.py --resume     # Resume from last position

Requirements:
    pip install playwright openpyxl requests
    playwright install chromium
"""

import os
import re
import sys
import json
import time
import base64
import hashlib
import argparse
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
import openpyxl

# Try to import playwright
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)

# Configuration
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
OUTPUT_DIR = SCRIPT_DIR.parent / "rendered-static-pages"
EXCEL_FILE = SCRIPT_DIR.parent.parent / "mmdc-urls-UNIFIED.xlsx"
PROGRESS_FILE = DATA_DIR / "static-render-progress.json"
ERRORS_FILE = DATA_DIR / "static-render-errors.json"

BASE_URL = "https://mmdc.nl"


def get_static_urls_from_excel():
    """Extract static page URLs (non-catalog) from Excel file."""
    wb = openpyxl.load_workbook(EXCEL_FILE, read_only=True)
    ws = wb.active

    static_urls = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        url = row[0]
        if url and 'recordId=' not in str(url):
            # Only HTML pages (not PDFs, images, CSS, JS)
            url_str = str(url)
            if url_str.endswith('.pdf') or url_str.endswith('.gif') or \
               url_str.endswith('.css') or url_str.endswith('.js') or \
               url_str.endswith('.png') or url_str.endswith('.jpg'):
                continue
            static_urls.append(url_str)

    wb.close()
    return static_urls


def url_to_filename(url):
    """Convert URL to a safe filename."""
    # Remove protocol and domain
    path = url.replace("https://mmdc.nl", "").replace("http://mmdc.nl", "")
    if not path or path == "/":
        return "index.html"

    # Clean up path
    path = path.strip("/")
    # Replace slashes with double underscores
    filename = path.replace("/", "__")
    # Ensure .html extension
    if not filename.endswith(".html"):
        filename += ".html"

    return filename


def get_page_dir(url):
    """Get the directory path from URL for relative path resolution."""
    parsed = urlparse(url)
    path = parsed.path
    if path.endswith('.html') or path.endswith('/'):
        # Get parent directory
        parts = path.rstrip('/').rsplit('/', 1)
        return parts[0] if len(parts) > 1 else ''
    return path


def get_mime_type(url):
    """Get MIME type from URL extension."""
    ext = url.lower().split('.')[-1].split('?')[0]
    mime_types = {
        'gif': 'image/gif', 'png': 'image/png', 'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg', 'svg': 'image/svg+xml', 'ico': 'image/x-icon',
        'webp': 'image/webp',
    }
    return mime_types.get(ext, 'application/octet-stream')


def fetch_with_retry(url, max_retries=3, delay=1):
    """Fetch URL with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                return response
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(delay)
    return None


def embed_images_as_base64(html, page_url):
    """Find all image src attributes and embed them as base64 data URIs."""
    page_dir = get_page_dir(page_url)
    failed_images = []

    def resolve_relative_path(src):
        """Resolve relative paths like ../../assets/images/logo.gif"""
        if src.startswith('http'):
            return src
        if src.startswith('//'):
            return f"https:{src}"
        if src.startswith('/'):
            return f"{BASE_URL}{src}"
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
            return f"{BASE_URL}/{'/'.join(result)}"
        return f"{BASE_URL}{page_dir}/{src}"

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

            # Encode as base64
            b64_data = base64.b64encode(response.content).decode('utf-8')
            data_uri = f'data:{mime_type};base64,{b64_data}'
            return f'src="{data_uri}"'
        else:
            failed_images.append(img_url)
            return full_attr  # Keep original if fetch failed

    # Match src="..." patterns for images
    pattern = r'src="([^"]+\.(?:gif|png|jpg|jpeg|svg|ico|webp)[^"]*)"'
    html = re.sub(pattern, replace_image, html, flags=re.IGNORECASE)

    # Also handle src='...' (single quotes)
    pattern_sq = r"src='([^']+\.(?:gif|png|jpg|jpeg|svg|ico|webp)[^']*)'"
    html = re.sub(pattern_sq, replace_image, html, flags=re.IGNORECASE)

    if failed_images:
        print(f"    WARNING: {len(failed_images)} images failed to embed")

    return html


def remove_shutdown_banner(html):
    """Remove the shutdown notice banner injected by default.js."""
    # Pattern for the shutdown banner (red border div with date)
    banner_pattern = r'<div><div style="[^"]*border:2px solid red[^"]*"[^>]*>.*?As of 15 December 2025.*?</div></div>'
    html = re.sub(banner_pattern, '', html, flags=re.DOTALL | re.IGNORECASE)

    # Also try alternative patterns
    banner_pattern2 = r'<div[^>]*style="[^"]*red[^"]*"[^>]*>.*?(?:shut down|December 2025).*?</div>'
    html = re.sub(banner_pattern2, '', html, flags=re.DOTALL | re.IGNORECASE)

    return html


def embed_css_inline(html, page_url):
    """Fetch external CSS and embed as inline <style> tags."""
    page_dir = get_page_dir(page_url)
    failed_css = []

    def resolve_css_url(href):
        """Resolve CSS href to full URL."""
        if href.startswith('http'):
            return href
        if href.startswith('//'):
            return f"https:{href}"
        if href.startswith('/'):
            return f"{BASE_URL}{href}"
        if href.startswith('../') or href.startswith('./'):
            # Resolve relative to page directory
            full_path = f"{page_dir}/{href}"
            parts = full_path.split('/')
            result = []
            for part in parts:
                if part == '..':
                    if result and result[-1] != '':
                        result.pop()
                elif part != '.' and part != '':
                    result.append(part)
            return f"{BASE_URL}/{'/'.join(result)}"
        return f"{BASE_URL}{page_dir}/{href}"

    def replace_css_link(match):
        full_tag = match.group(0)
        href = match.group(1)

        # Skip if not a CSS link
        if 'rel="stylesheet"' not in full_tag.lower() and 'rel=\'stylesheet\'' not in full_tag.lower():
            if '.css' not in href.lower():
                return full_tag

        # Resolve URL
        css_url = resolve_css_url(href)

        response = fetch_with_retry(css_url)
        if response:
            try:
                css_content = response.content.decode('utf-8', errors='ignore')
                # Return as inline style tag
                return f'<style type="text/css">/* Inlined from: {href} */\n{css_content}\n</style>'
            except Exception:
                failed_css.append(css_url)
                return full_tag
        else:
            failed_css.append(css_url)
            return full_tag

    # Match <link> tags with href
    link_pattern = r'<link[^>]*href=["\']([^"\']+\.css[^"\']*)["\'][^>]*/?>'
    html = re.sub(link_pattern, replace_css_link, html, flags=re.IGNORECASE)

    # Also match with href before rel
    link_pattern2 = r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*/?>'
    html = re.sub(link_pattern2, replace_css_link, html, flags=re.IGNORECASE)

    if failed_css:
        print(f"    WARNING: {len(failed_css)} CSS files failed to embed")

    return html


def remove_external_scripts(html):
    """Remove external script tags to prevent banner re-injection."""
    # Remove mmdc.nl scripts
    relative_pattern = r'<script[^>]*/static/assets/scripts/[^>]*>[^<]*</script>'
    html = re.sub(relative_pattern, '<!-- Script removed -->', html, flags=re.IGNORECASE)

    absolute_pattern = r'<script[^>]*mmdc\.nl[^>]*>[^<]*</script>'
    html = re.sub(absolute_pattern, '<!-- Script removed -->', html, flags=re.IGNORECASE)

    # Remove tracking scripts
    tracking_pattern = r'<script[^>]*(matomo|webstatistieken)[^>]*>[^<]*</script>'
    html = re.sub(tracking_pattern, '<!-- Tracking removed -->', html, flags=re.IGNORECASE)

    return html


def render_page(page, url):
    """Render a single page with Playwright and clean it."""
    try:
        # Navigate to page
        page.goto(url, wait_until='networkidle', timeout=30000)

        # Wait for content to load
        page.wait_for_timeout(2000)

        # Get rendered HTML
        html_content = page.content()

        # Clean up the HTML
        # 1. Remove shutdown banner
        html_content = remove_shutdown_banner(html_content)

        # 2. Embed images as base64
        html_content = embed_images_as_base64(html_content, url)

        # 3. Embed CSS inline
        html_content = embed_css_inline(html_content, url)

        # 4. Remove external scripts (prevent banner re-injection)
        html_content = remove_external_scripts(html_content)

        return html_content, None

    except Exception as e:
        return None, str(e)


def load_progress():
    """Load progress from JSON file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"completed": [], "last_index": 0}


def save_progress(progress):
    """Save progress to JSON file."""
    DATA_DIR.mkdir(exist_ok=True)
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Render static pages from mmdc.nl')
    parser.add_argument('--test', type=int, help='Test with first N pages')
    parser.add_argument('--resume', action='store_true', help='Resume from last position')
    args = parser.parse_args()

    print("=" * 70)
    print("MMDC.NL STATIC PAGE RENDERER")
    print("=" * 70)
    print(f"Start time: {datetime.now().isoformat()}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

    # Get URLs from Excel
    print("Loading URLs from Excel...")
    all_urls = get_static_urls_from_excel()
    print(f"Found {len(all_urls)} static page URLs")

    # Apply test limit
    if args.test:
        all_urls = all_urls[:args.test]
        print(f"TEST MODE: Processing first {args.test} pages")

    # Load progress
    progress = load_progress()
    completed_urls = set(progress.get("completed", []))

    # Filter out already completed if resuming
    if args.resume and completed_urls:
        urls_to_process = [u for u in all_urls if u not in completed_urls]
        print(f"Resuming: {len(completed_urls)} already done, {len(urls_to_process)} remaining")
    else:
        urls_to_process = all_urls
        progress = {"completed": [], "last_index": 0}

    if not urls_to_process:
        print("All pages already rendered!")
        return

    print(f"\nRendering {len(urls_to_process)} pages...")
    print()

    errors = []
    start_time = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        )
        page = context.new_page()

        for i, url in enumerate(urls_to_process):
            filename = url_to_filename(url)
            output_path = OUTPUT_DIR / filename

            # Render page
            html_content, error = render_page(page, url)

            if html_content:
                # Save HTML
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)

                # Update progress
                progress["completed"].append(url)
                progress["last_index"] = i

                # Report progress every 10 pages
                if (i + 1) % 10 == 0 or (i + 1) == len(urls_to_process):
                    elapsed = time.time() - start_time
                    rate = (i + 1) / elapsed if elapsed > 0 else 0
                    print(f"  [{i+1}/{len(urls_to_process)}] {rate:.2f} pages/sec - {filename[:50]}...")
                    save_progress(progress)
            else:
                errors.append({"url": url, "error": error})
                print(f"  ERROR: {url} - {error}")

        browser.close()

    # Save final progress
    save_progress(progress)

    # Save errors
    if errors:
        with open(ERRORS_FILE, 'w') as f:
            json.dump(errors, f, indent=2)

    # Summary
    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("RENDERING COMPLETE")
    print("=" * 70)
    print(f"Total processed: {len(urls_to_process)}")
    print(f"Successful: {len(urls_to_process) - len(errors)}")
    print(f"Failed: {len(errors)}")
    print(f"Time elapsed: {elapsed/60:.1f} minutes")
    print(f"Output directory: {OUTPUT_DIR}")
    if errors:
        print(f"Errors logged to: {ERRORS_FILE}")


if __name__ == "__main__":
    main()
