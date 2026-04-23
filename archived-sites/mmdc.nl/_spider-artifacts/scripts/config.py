"""Configuration for mmdc.nl URL Spider."""

from pathlib import Path
from datetime import timedelta

# Paths
BASE_DIR = Path(__file__).parent.parent
ARTIFACTS_DIR = Path(__file__).parent
LOGS_DIR = ARTIFACTS_DIR / "logs"
CHECKPOINTS_DIR = ARTIFACTS_DIR / "checkpoints"
SEED_FILE = BASE_DIR / "seed-urls.txt"
OUTPUT_EXCEL = BASE_DIR / "mmdc-urls-spider-output.xlsx"

# Target site
TARGET_DOMAIN = "mmdc.nl"
# Start from homepage - spider will discover all other pages
START_URLS = [
    "https://mmdc.nl/",
]

# Crawl settings
MAX_REQUESTS_PER_CRAWL = None  # No limit - crawl everything
REQUEST_TIMEOUT = timedelta(seconds=60)
MAX_REQUEST_RETRIES = 3

# Concurrency (conservative for politeness)
MIN_CONCURRENCY = 1
MAX_CONCURRENCY = 5
DESIRED_CONCURRENCY = 3
MAX_TASKS_PER_MINUTE = 60  # ~1 request/second

# Checkpointing
CHECKPOINT_BATCH_SIZE = 100

# Excel sheet names (max 31 chars)
SHEET_NAMES = [
    "ENTRY_POINT",
    "SEARCH_CATALOG",
    "HIGHLIGHTS",
    "RESEARCH_EDUCATION",
    "LITERATURE",
    "COLLECTIONS",
    "LINKS",
    "ABOUT",
    "MANUSCRIPT_RECORDS",
    "STATIC_ASSETS",
    "OTHER",
]

# Probe crawl settings
PROBE_MAX_REQUESTS = 20
