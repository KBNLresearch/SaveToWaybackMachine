"""URL classification for mmdc.nl functional groups."""

from urllib.parse import urlparse


def classify_url(url: str) -> str:
    """Classify URL into functional group (Excel sheet name).

    Args:
        url: Full URL to classify

    Returns:
        Sheet name for the URL's functional group
    """
    path = urlparse(url).path.lower()
    query = urlparse(url).query.lower()

    # Search catalog (highest priority - many URLs)
    if '/search/' in path or 'searchmode=' in query:
        return "SEARCH_CATALOG"

    # Static content sections
    elif '/highlights/' in path:
        return "HIGHLIGHTS"
    elif '/research_and_education/' in path:
        return "RESEARCH_EDUCATION"
    elif '/literature/' in path:
        return "LITERATURE"
    elif '/collections/' in path:
        return "COLLECTIONS"
    elif '/links/' in path:
        return "LINKS"
    elif '/about/' in path:
        return "ABOUT"

    # Manuscript records (individual items)
    elif '/manuscripts/' in path or '/manuscript/' in path:
        return "MANUSCRIPT_RECORDS"

    # Static assets
    elif any(ext in path for ext in [
        '.css', '.js', '.png', '.jpg', '.jpeg', '.gif',
        '.svg', '.woff', '.woff2', '.ttf', '.eot', '.ico',
        '.pdf', '.xml', '.json'
    ]):
        return "STATIC_ASSETS"

    # Entry point
    elif path in ['/', '']:
        return "ENTRY_POINT"

    # Everything else
    else:
        return "OTHER"


def is_same_domain(url: str, target_domain: str = "mmdc.nl") -> bool:
    """Check if URL belongs to target domain.

    Args:
        url: URL to check
        target_domain: Domain to match against

    Returns:
        True if URL is on target domain
    """
    try:
        parsed = urlparse(url)
        return parsed.netloc.endswith(target_domain)
    except Exception:
        return False
