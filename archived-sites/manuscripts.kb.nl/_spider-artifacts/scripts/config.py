"""
Configuration for the manuscripts.kb.nl URL spider.

Central config for all spider components (spider.py, excel_writer.py).
Defines seed URLs, crawl throttling, URL classification rules, Wikimedia
API endpoints for priority detection, and Excel output schema.

Created: 2025-12-10
"""

from pathlib import Path
from dataclasses import dataclass
from typing import Set

# === PATHS ===
SCRIPTS_ROOT = Path(__file__).parent
SPIDER_ROOT = SCRIPTS_ROOT.parent
PROJECT_ROOT = SPIDER_ROOT.parent
ARCHIVING_ROOT = PROJECT_ROOT / "_archiving-artifacts"

# Output paths
EXCEL_OUTPUT = SPIDER_ROOT / "manuscripts-urls-spider-output.xlsx"
CHECKPOINT_DIR = SPIDER_ROOT / "checkpoints"
LOGS_DIR = SPIDER_ROOT / "logs"
DATA_DIR = SPIDER_ROOT / "data"

# Ensure directories exist
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# === SITE CONFIGURATION ===
BASE_URL = "https://manuscripts.kb.nl"

# Seed URLs (entry points for crawling)
SEED_URLS = [
    "https://manuscripts.kb.nl",
    "https://manuscripts.kb.nl/advanced",
    "https://manuscripts.kb.nl/introduction",
    "https://manuscripts.kb.nl/background",
    # Manuscript indexes
    "https://manuscripts.kb.nl/indexes/shelfmark",
    "https://manuscripts.kb.nl/indexes/authortitle",
    "https://manuscripts.kb.nl/indexes/place",
    "https://manuscripts.kb.nl/indexes/language",
    # Image indexes
    "https://manuscripts.kb.nl/indexes/titleImage",
    "https://manuscripts.kb.nl/indexes/iconclass",
    "https://manuscripts.kb.nl/indexes/haspart",
    "https://manuscripts.kb.nl/indexes/imagetype",
    "https://manuscripts.kb.nl/indexes/miniaturist",
    # Initial search pages (will discover paginated results)
    "https://manuscripts.kb.nl/search/manuscripts/extended/shelfmark/*",
    "https://manuscripts.kb.nl/search/images_text/extended/titleImage/*",
]

# === CRAWL SETTINGS ===
@dataclass
class CrawlSettings:
    """Crawl configuration based on user decisions."""
    # Concurrency (conservative for KB servers)
    min_concurrency: int = 1
    max_concurrency: int = 3
    desired_concurrency: int = 2

    # Delays
    request_delay_min: float = 1.0  # seconds
    request_delay_max: float = 2.0  # seconds

    # Retry settings
    max_retries: int = 3
    retry_backoff: float = 30.0  # seconds

    # Timeouts
    request_timeout: int = 30  # seconds
    page_load_timeout: int = 60  # seconds

    # Content inclusion (based on user input)
    include_html: bool = True
    include_css: bool = True
    include_js: bool = True
    include_pdfs: bool = True
    include_images: bool = False  # User said: "niet de 11K jpg images"

    # Batch settings
    checkpoint_interval: int = 100  # Save checkpoint every N URLs
    excel_batch_size: int = 50  # Write to Excel every N URLs

    # Playwright settings
    use_playwright: bool = True  # Playwright is installed
    playwright_path: str = r"C:\Users\OJA010\AppData\Local\ms-playwright"

CRAWL_SETTINGS = CrawlSettings()

# === URL CLASSIFICATION ===
# Extensions to include
INCLUDE_EXTENSIONS: Set[str] = {".html", ".htm", ".php", ".asp", ".aspx", ""}
ASSET_EXTENSIONS: Set[str] = {".css", ".js"}
PDF_EXTENSIONS: Set[str] = {".pdf"}

# Extensions to exclude (images, CSS, JS - per user decision)
EXCLUDE_EXTENSIONS: Set[str] = {
    # Images
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff",
    ".bmp", ".ico", ".svg", ".webp",
    # Static assets (not needed for archiving)
    ".css", ".js", ".woff", ".woff2", ".ttf", ".eot",
}

# === WIKIMEDIA PRIORITY ===
WIKI_NL_API = "https://nl.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"

# API query parameters for external link search
WIKI_QUERY_PARAMS = {
    "action": "query",
    "list": "exturlusage",
    "euquery": "manuscripts.kb.nl",
    "eulimit": "500",
    "eunamespace": "0",  # Main namespace only
    "format": "json"
}

COMMONS_QUERY_PARAMS = {
    "action": "query",
    "list": "exturlusage",
    "euquery": "manuscripts.kb.nl",
    "eulimit": "500",
    "eunamespace": "6",  # File namespace only
    "format": "json"
}

# === URL CATEGORY DEFINITIONS ===
URL_CATEGORIES = {
    "STATIC_PAGES": ["/introduction", "/background", "/advanced"],
    "INDEX_PAGES": ["/indexes/"],
    "MANUSCRIPT_SEARCH": ["/search/manuscripts/"],
    "IMAGE_SEARCH": ["/search/images_text/", "/search/images/"],
    "MANUSCRIPT_DETAIL": ["/show/manuscript/", "/manuscript/"],
    "IMAGE_DETAIL": ["/show/image/", "/image/"],
}

# Priority levels
PRIORITY_LEVELS = {
    "WIKI_HIGH": 1,      # Linked from Dutch Wikipedia
    "COMMONS_HIGH": 2,   # Linked from Wikimedia Commons
    "MANUSCRIPT": 3,     # Manuscript detail page
    "IMAGE": 4,          # Image detail page
    "INDEX": 5,          # Index/navigation page
    "SEARCH": 6,         # Search result page
    "STATIC": 7,         # Static content page
    "NORMAL": 8,         # Other
}

# === EXCEL CONFIGURATION ===
# Single sheet format (like mmdc-urls-UNIFIED.xlsx)
# All URLs in one sheet with Category column for filtering

# Excel column headers
EXCEL_HEADERS = [
    "URL",
    "Path",
    "Category",
    "Priority",
    "Discovered",
    "WBM_Status",
    "WBM_URL",
    "WBM_Timestamp",
]

# === EXPECTED COUNTS (for progress tracking) ===
EXPECTED_COUNTS = {
    "MANUSCRIPT_DETAIL": 400,
    "IMAGE_DETAIL": 11141,
    "INDEX_PAGES": 50,
    "SEARCH_RESULTS": 200,
    "STATIC_PAGES": 10,
    "TOTAL": 12300,
}
