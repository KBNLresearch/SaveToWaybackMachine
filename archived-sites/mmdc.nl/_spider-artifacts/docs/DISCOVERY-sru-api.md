# MMDC Catalog Discovery via KB's SRU API

## Key Discovery
The mmdc.nl catalog is a **JavaScript SPA** that loads manuscript data dynamically from the KB's (Koninklijke Bibliotheek) SRU API.

## API Details

| Parameter | Value |
|-----------|-------|
| **Endpoint** | `https://jsru.kb.nl/sru/sru` |
| **Collection** | `x-collection=MISC` |
| **Filter** | `dcterms.isPartOf adj PTP` |
| **Total Records** | **11,754** |
| **Unique IDs Extracted** | **11,738** |
| **ID Range** | 2 - 163,403 (sparse, non-sequential) |

## URL Patterns

### Catalog Detail Page
```
https://mmdc.nl/static/site/search/detail.html?recordId={ID}#r{ID}
```

### SRU Search Query (used by site JavaScript)
```
https://jsru.kb.nl/sru/sru?x-collection=MISC&operation=searchRetrieve&version=1.2&recordSchema=dcx+admin&query=dcterms.isPartOf+adj+PTP&maximumRecords=100&startRecord=1
```

### How the site fetches record details
The JavaScript (`ptp_v3.js`) builds this query:
```
( (dcterms.isPartOf=PTP) and ( (dc.identifier="{recordId}") or (dcterms.isPartOf="PTPFra{recordId}") or (dcterms.isPartOf="PTPFaa{recordId}") ) )
```

## Why BeautifulSoupCrawler Missed These
The catalog pages return a shell HTML that looks the same for all records. The actual manuscript data is:
1. Loaded via JavaScript after page load
2. Fetched from the SRU API
3. Transformed via XSL stylesheets

## Extraction Process
1. Query SRU API for total count: `11,754`
2. Paginate through results (100 per batch)
3. Extract `<dc:identifier>` values from XML responses
4. Save unique IDs to `catalog-record-ids.txt`

## Files Generated
- `catalog-record-ids.txt` - 11,738 unique record IDs
- `catalog-urls.txt` - Full URLs for each record (to be generated)

## Next Steps
1. Generate catalog URLs from record IDs
2. Extract PDF links from static pages
3. Combine all URLs for Wayback Machine archival
