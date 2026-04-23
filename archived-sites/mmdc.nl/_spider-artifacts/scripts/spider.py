#!/usr/bin/env python3
"""
mmdc.nl URL Spider
==================
Crawls mmdc.nl to discover all URLs before site shutdown on December 15, 2025.

Usage:
    python spider.py              # Full crawl
    python spider.py --probe      # Probe crawl (20 URLs only)
    python spider.py --resume     # Resume from checkpoint

Output:
    - mmdc-urls-spider-output.xlsx (in parent directory)
    - checkpoints/*.json (for recovery)
    - logs/crawl.log
"""

import asyncio
import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from crawlee import ConcurrencySettings, service_locator
from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    START_URLS, TARGET_DOMAIN, LOGS_DIR,
    MAX_REQUESTS_PER_CRAWL, MAX_REQUEST_RETRIES,
    MIN_CONCURRENCY, MAX_CONCURRENCY, DESIRED_CONCURRENCY,
    MAX_TASKS_PER_MINUTE, PROBE_MAX_REQUESTS,
)
from url_classifier import classify_url, is_same_domain
from excel_writer import ExcelURLWriter


# Setup logging
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOGS_DIR / "crawl.log"),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger("mmdc-spider")


class MMDCSpider:
    """Spider for mmdc.nl URL discovery."""

    def __init__(self, probe_mode: bool = False, resume: bool = False):
        self.probe_mode = probe_mode
        self.resume = resume
        self.excel_writer = ExcelURLWriter()
        self.urls_found = 0
        self.start_time = None

        # Configure persistence for resume
        if resume:
            configuration = service_locator.get_configuration()
            configuration.purge_on_start = False

    async def run(self) -> None:
        """Run the spider."""
        self.start_time = datetime.now()
        logger.info("=" * 60)
        logger.info(f"mmdc.nl Spider - {'PROBE MODE' if self.probe_mode else 'FULL CRAWL'}")
        logger.info(f"Started: {self.start_time.isoformat()}")
        logger.info("=" * 60)

        # Initialize Excel
        self.excel_writer.initialize()

        # Configure concurrency
        concurrency = ConcurrencySettings(
            min_concurrency=MIN_CONCURRENCY,
            max_concurrency=MAX_CONCURRENCY,
            desired_concurrency=DESIRED_CONCURRENCY,
            max_tasks_per_minute=MAX_TASKS_PER_MINUTE,
        )

        # Set max requests
        max_requests = PROBE_MAX_REQUESTS if self.probe_mode else MAX_REQUESTS_PER_CRAWL

        # Create crawler
        crawler = BeautifulSoupCrawler(
            max_requests_per_crawl=max_requests,
            max_request_retries=MAX_REQUEST_RETRIES,
            concurrency_settings=concurrency,
        )

        @crawler.router.default_handler
        async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
            """Process each page."""
            url = context.request.url

            # Skip non-target domain URLs
            if not is_same_domain(url, TARGET_DOMAIN):
                return

            # Classify URL
            path = urlparse(url).path
            sheet_name = classify_url(url)

            # Add to Excel
            self.excel_writer.add_url(
                url=url,
                sheet_name=sheet_name,
                path=path,
            )
            self.urls_found += 1

            # Log progress
            if self.urls_found % 10 == 0:
                stats = self.excel_writer.get_stats()
                logger.info(
                    f"Progress | URLs: {self.urls_found} | "
                    f"Buffered: {stats['buffered']} | "
                    f"Written: {stats['total_urls']}"
                )

            # Flush buffer periodically
            if self.urls_found % 100 == 0:
                written = self.excel_writer.flush()
                if written > 0:
                    logger.info(f"Checkpoint | Wrote {written} URLs to Excel")

            # Enqueue links (same domain only)
            await context.enqueue_links(strategy='same-origin')

        @crawler.error_handler
        async def handle_error(context, error) -> None:
            """Handle crawl errors."""
            logger.warning(f"Error crawling {context.request.url}: {error}")

        @crawler.failed_request_handler
        async def handle_failed(context, error) -> None:
            """Handle failed requests after retries."""
            logger.error(f"Failed after retries: {context.request.url} - {error}")

        # Run crawler
        logger.info(f"Starting crawl with {len(START_URLS)} seed URLs...")
        await crawler.run(START_URLS)

        # Final flush
        self.excel_writer.close()

        # Print summary
        self._print_summary()

    def _print_summary(self) -> None:
        """Print crawl summary."""
        end_time = datetime.now()
        duration = end_time - self.start_time
        stats = self.excel_writer.get_stats()

        logger.info("=" * 60)
        logger.info("CRAWL COMPLETE")
        logger.info("=" * 60)
        logger.info(f"Duration: {duration}")
        logger.info(f"Total URLs found: {stats['total_urls']}")
        logger.info(f"Batches written: {stats['batch_number']}")
        logger.info("")
        logger.info("URLs by section:")
        for sheet, count in sorted(stats['sheet_counts'].items()):
            logger.info(f"  {sheet}: {count}")
        logger.info("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="mmdc.nl URL Spider")
    parser.add_argument(
        "--probe", action="store_true",
        help=f"Probe mode: crawl only {PROBE_MAX_REQUESTS} URLs"
    )
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume from previous crawl state"
    )
    args = parser.parse_args()

    spider = MMDCSpider(probe_mode=args.probe, resume=args.resume)
    asyncio.run(spider.run())


if __name__ == "__main__":
    main()
