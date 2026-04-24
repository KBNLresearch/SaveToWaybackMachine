"""
URL Spider for manuscripts.kb.nl
Discovers all URLs on the Medieval Illuminated Manuscripts site.
Created: 2025-12-10
"""

import asyncio
import json
import logging
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse, parse_qs, quote

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Add script directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    BASE_URL, SEED_URLS, CRAWL_SETTINGS, DATA_DIR, LOGS_DIR,
    EXCLUDE_EXTENSIONS, EXPECTED_COUNTS
)
from excel_writer import ExcelWriter, classify_url

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'crawl.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ManuscriptSpider:
    """Spider for manuscripts.kb.nl."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; KB-Archiver/1.0; +https://www.kb.nl/)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'nl,en;q=0.5',
        })

        self.seen_urls: Set[str] = set()
        self.to_crawl: List[str] = []
        self.discovered_urls: List[str] = []
        self.failed_urls: List[Tuple[str, str]] = []

        self.excel_writer = ExcelWriter()
        self.stats = {
            'pages_crawled': 0,
            'urls_discovered': 0,
            'errors': 0,
            'start_time': None,
            'end_time': None,
        }

    def normalize_url(self, url: str) -> Optional[str]:
        """Normalize URL and filter out unwanted URLs."""
        # Filter out javascript: URLs immediately
        if url.startswith('javascript:') or url.startswith('javascript://'):
            return None

        # Parse URL
        parsed = urlparse(url)

        # Filter out javascript: scheme (additional check after parsing)
        if parsed.scheme == 'javascript':
            return None

        # Only process manuscripts.kb.nl URLs
        if parsed.netloc and parsed.netloc != 'manuscripts.kb.nl':
            return None

        # Check for excluded extensions
        path_lower = parsed.path.lower()
        for ext in EXCLUDE_EXTENSIONS:
            if path_lower.endswith(ext):
                return None

        # FILTER: Exclude /search/manuscripts/extended/title/ URLs
        # These are image titles used to search manuscripts - they all return empty results
        # Valid patterns: /search/manuscripts/extended/shelfmark/, /authortitle/, /place/, /language/
        if '/search/manuscripts/extended/title/' in parsed.path:
            return None

        # FILTER: Exclude /show/images/ URLs (image-only pages without text)
        # We want to keep:
        #   /show/text/135+E+12 - text descriptions
        #   /show/images_text/135+E+12 - images with text (combined view)
        #   /show/manuscript/... - manuscript detail pages
        # We exclude:
        #   /show/images/135+E+12 - image-only view (redundant, no text)
        if '/show/images/' in parsed.path and '/show/images_text/' not in parsed.path:
            return None

        # FILTER: Exclude /iconclass/ URLs
        # These are iconclass search results - not needed for archiving
        # Example: /search/images_text/extended/iconclass/44A11%28%2B6%29%28MONS%20WATTENA%29
        if '/iconclass/' in parsed.path:
            return None

        # FILTER: Exclude /zoom/ URLs
        # These are image zoom viewer pages - not needed for archiving
        # Example: /zoom/?...
        if '/zoom/' in parsed.path or parsed.path.startswith('/zoom'):
            return None

        # FILTER: Exclude /haspart/ URLs
        # These are "has part" search results - not needed for archiving
        # Example: /search/images_text/extended/haspart/Epistle%20I%20of%20St.%20Paul%20to%20the%20Corinthians
        if '/haspart/' in parsed.path:
            return None

        # Clean up path - remove trailing encoded characters like %0D (carriage return)
        path = parsed.path.rstrip()
        # Remove URL-encoded control characters at end of path
        while path.endswith('%0D') or path.endswith('%0A') or path.endswith('%0d') or path.endswith('%0a'):
            path = path[:-3]

        # Rebuild URL without fragments
        normalized = f"{parsed.scheme or 'https'}://{parsed.netloc or 'manuscripts.kb.nl'}{path}"
        if parsed.query:
            normalized += f"?{parsed.query}"

        return normalized

    def extract_links(self, html: str, base_url: str) -> List[str]:
        """Extract all links from HTML."""
        links = []
        soup = BeautifulSoup(html, 'lxml')

        for tag in soup.find_all(['a', 'link'], href=True):
            href = tag['href']
            absolute_url = urljoin(base_url, href)
            normalized = self.normalize_url(absolute_url)
            if normalized and normalized not in self.seen_urls:
                links.append(normalized)

        return links

    def extract_pagination_links(self, html: str, base_url: str) -> List[str]:
        """Extract pagination links (page/N/ patterns)."""
        links = []
        soup = BeautifulSoup(html, 'lxml')

        # Look for pagination patterns
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Match pagination patterns like /page/2/, /page/3/
            if '/page/' in href:
                absolute_url = urljoin(base_url, href)
                normalized = self.normalize_url(absolute_url)
                if normalized and normalized not in self.seen_urls:
                    links.append(normalized)

        return links

    def extract_javascript_index_urls(self, html: str, base_url: str) -> List[str]:
        """Extract URLs from JavaScript getIndex() function calls on index pages.

        Index pages like /indexes/shelfmark contain JavaScript calls like:
          getIndex('shelfmark', '10 B 29')

        These convert to RESTful URLs like:
          https://manuscripts.kb.nl/search/manuscripts/extended/shelfmark/10%20B%2029
        """
        links = []

        # Determine index type from current URL path
        path = urlparse(base_url).path

        # Map index pages to their search URL patterns
        # Manuscript indexes use /search/manuscripts/extended/{indexType}/{value}
        # Image indexes use /search/images_text/extended/{indexType}/{value}
        manuscript_indexes = ['shelfmark', 'authortitle', 'place', 'language']
        image_indexes = ['titleImage', 'iconclass', 'haspart', 'imagetype', 'miniaturist']

        # Pattern: getIndex('indexType', 'value') or getIndex("indexType", "value")
        pattern = r"getIndex\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\)"

        matches = re.findall(pattern, html)

        for index_type, value in matches:
            # URL-encode the value (spaces become %20, etc.)
            encoded_value = quote(value, safe='')

            # Determine search type based on index
            if index_type in manuscript_indexes:
                url = f"{BASE_URL}/search/manuscripts/extended/{index_type}/{encoded_value}"
            elif index_type in image_indexes:
                url = f"{BASE_URL}/search/images_text/extended/{index_type}/{encoded_value}"
            else:
                # Fallback - try manuscript search
                url = f"{BASE_URL}/search/manuscripts/extended/{index_type}/{encoded_value}"
                logger.debug(f"Unknown index type '{index_type}', using manuscript search pattern")

            normalized = self.normalize_url(url)
            if normalized and normalized not in self.seen_urls:
                links.append(normalized)

        if matches:
            logger.info(f"Extracted {len(links)} URLs from {len(matches)} getIndex() calls on {base_url}")

        return links

    def extract_detail_links(self, html: str, base_url: str) -> List[str]:
        """Extract manuscript and image detail page links."""
        links = []
        soup = BeautifulSoup(html, 'lxml')

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Match detail patterns
            if '/show/manuscript/' in href or '/show/image/' in href:
                absolute_url = urljoin(base_url, href)
                normalized = self.normalize_url(absolute_url)
                if normalized and normalized not in self.seen_urls:
                    links.append(normalized)

        return links

    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch a single page with rate limiting and error handling."""
        try:
            # Random delay between requests
            delay = random.uniform(
                CRAWL_SETTINGS.request_delay_min,
                CRAWL_SETTINGS.request_delay_max
            )
            time.sleep(delay)

            response = self.session.get(
                url,
                timeout=CRAWL_SETTINGS.request_timeout,
                allow_redirects=True
            )
            response.raise_for_status()
            return response.text

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else 'unknown'
            logger.warning(f"HTTP error {status_code} for {url}")
            self.failed_urls.append((url, f"HTTP {status_code}"))
            self.stats['errors'] += 1

            # Back off on rate limiting
            if status_code == 429:
                logger.info("Rate limited, backing off for 30s...")
                time.sleep(30)

            return None

        except requests.exceptions.RequestException as e:
            logger.warning(f"Request error for {url}: {e}")
            self.failed_urls.append((url, str(e)))
            self.stats['errors'] += 1
            return None

    def crawl_page(self, url: str) -> List[str]:
        """Crawl a single page and return discovered URLs."""
        html = self.fetch_page(url)
        if not html:
            return []

        self.stats['pages_crawled'] += 1

        # Extract all types of links
        new_urls = []
        new_urls.extend(self.extract_links(html, url))
        new_urls.extend(self.extract_pagination_links(html, url))
        new_urls.extend(self.extract_detail_links(html, url))

        # On index pages, extract URLs from JavaScript getIndex() calls
        if '/indexes/' in url:
            new_urls.extend(self.extract_javascript_index_urls(html, url))

        # Deduplicate
        unique_new = []
        for u in new_urls:
            if u not in self.seen_urls:
                self.seen_urls.add(u)
                unique_new.append(u)
                self.excel_writer.add_url(u)
                self.stats['urls_discovered'] += 1

        return unique_new

    def probe_crawl(self, limit: int = 20) -> Dict:
        """Run a probe crawl to test connectivity and response times."""
        logger.info(f"=== PROBE CRAWL: Testing {limit} URLs ===")

        test_urls = SEED_URLS[:limit]
        results = {
            'success': 0,
            'failed': 0,
            'avg_response_time': 0,
            'response_times': []
        }

        for url in test_urls:
            start = time.time()
            html = self.fetch_page(url)
            elapsed = time.time() - start

            if html:
                results['success'] += 1
                results['response_times'].append(elapsed)
                logger.info(f"OK ({elapsed:.2f}s): {url[:60]}...")
            else:
                results['failed'] += 1
                logger.warning(f"FAILED: {url[:60]}...")

        if results['response_times']:
            results['avg_response_time'] = sum(results['response_times']) / len(results['response_times'])

        logger.info(f"Probe results: {results['success']}/{len(test_urls)} successful")
        logger.info(f"Average response time: {results['avg_response_time']:.2f}s")

        return results

    def run(self, probe_only: bool = False, max_pages: Optional[int] = None):
        """Run the spider."""
        self.stats['start_time'] = datetime.now()
        logger.info("=" * 60)
        logger.info("manuscripts.kb.nl URL Spider Starting")
        logger.info("=" * 60)

        # Run probe first
        probe_results = self.probe_crawl()
        if probe_results['success'] == 0:
            logger.error("Probe crawl failed completely. Aborting.")
            return

        if probe_only:
            logger.info("Probe crawl complete. Exiting.")
            return

        # Initialize queue with seed URLs
        for url in SEED_URLS:
            if url not in self.seen_urls:
                self.seen_urls.add(url)
                self.to_crawl.append(url)
                self.excel_writer.add_url(url)

        # Main crawl loop
        pages_limit = max_pages or float('inf')
        pbar = tqdm(desc="Crawling", unit="pages")

        while self.to_crawl and self.stats['pages_crawled'] < pages_limit:
            url = self.to_crawl.pop(0)

            # Classify URL to prioritize detail pages
            category = classify_url(url)

            new_urls = self.crawl_page(url)

            # Add new URLs to queue
            # Prioritize index and search pages for breadth-first discovery
            for new_url in new_urls:
                new_category = classify_url(new_url)
                if new_category in ['INDEX_PAGES', 'SEARCH_RESULTS']:
                    # Add to front for priority
                    self.to_crawl.insert(0, new_url)
                else:
                    self.to_crawl.append(new_url)

            pbar.update(1)
            pbar.set_postfix({
                'discovered': self.stats['urls_discovered'],
                'queue': len(self.to_crawl),
                'errors': self.stats['errors']
            })

            # Periodic checkpoint
            if self.stats['pages_crawled'] % 100 == 0:
                self.save_progress()

        pbar.close()
        self.stats['end_time'] = datetime.now()

        # Final save
        self.excel_writer.finalize()
        self.save_progress()
        self.print_summary()

    def save_progress(self):
        """Save current progress to JSON."""
        progress_file = DATA_DIR / 'crawl_progress.json'

        progress_data = {
            'timestamp': datetime.now().isoformat(),
            'stats': {
                **self.stats,
                'start_time': self.stats['start_time'].isoformat() if self.stats['start_time'] else None,
                'end_time': self.stats['end_time'].isoformat() if self.stats['end_time'] else None,
            },
            'queue_size': len(self.to_crawl),
            'seen_count': len(self.seen_urls),
            'failed_count': len(self.failed_urls),
        }

        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Progress saved: {len(self.seen_urls)} URLs discovered")

    def print_summary(self):
        """Print crawl summary."""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds() if self.stats['end_time'] and self.stats['start_time'] else 0

        logger.info("\n" + "=" * 60)
        logger.info("CRAWL SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Pages crawled: {self.stats['pages_crawled']}")
        logger.info(f"URLs discovered: {self.stats['urls_discovered']}")
        logger.info(f"Errors: {self.stats['errors']}")
        logger.info(f"Duration: {duration:.0f} seconds")

        if duration > 0:
            logger.info(f"Rate: {self.stats['pages_crawled'] / duration:.2f} pages/second")

        # Stats by category
        excel_stats = self.excel_writer.get_stats()
        logger.info("\nURLs by category:")
        for category, count in sorted(excel_stats['by_category'].items()):
            expected = EXPECTED_COUNTS.get(category, '?')
            logger.info(f"  {category}: {count} (expected: {expected})")

        logger.info(f"\nTotal unique URLs: {excel_stats['total_urls']}")
        logger.info("=" * 60)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='manuscripts.kb.nl URL Spider')
    parser.add_argument('--probe', action='store_true', help='Run probe crawl only')
    parser.add_argument('--max-pages', type=int, help='Maximum pages to crawl')
    args = parser.parse_args()

    spider = ManuscriptSpider()
    spider.run(probe_only=args.probe, max_pages=args.max_pages)


if __name__ == '__main__':
    main()
