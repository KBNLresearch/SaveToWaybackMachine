---
layout: default
title: mmdc.nl
breadcrumb:
  - title: Archived sites
    url: /archived-sites/
  - title: mmdc.nl
---

# mmdc.nl - Wayback Machine archive

**[View on GitHub Pages]({{ site.url }}{{ site.baseurl }}/archived-sites/mmdc.nl/)**

*Archived: December 2025*

## About

This folder documents the archiving of [mmdc.nl](https://mmdc.nl/) — the **Medieval Manuscripts Digital Collection** of the KB, National Library of the Netherlands — to [The Wayback Machine](https://web.archive.org/).

The site was scheduled to be phased out on **15 December 2025**. URLs for static pages, catalog records, PDFs and images were submitted to the Wayback Machine in December 2025, and a full local copy was produced in parallel (the catalog is JavaScript-rendered, so a raw WBM capture is not always faithful).

## Statistics

| Category | Count | Status |
|----------|------:|--------|
| Static HTML pages | 317 | Submitted to WBM, local copies exist |
| Catalog pages | 11,738 | Rendered locally (100%) |
| PDFs | 112 | 26 indexed Dec 2025, 40 older only, 46 none |
| Static asset images | 38 | Downloaded locally |
| **Total WBM submissions** | **429** | Submitted, indexing verified |

Full per-URL status lives in [`mmdc-urls-unified_15042026.xlsx`](mmdc-urls-unified_15042026.xlsx).

## How the site was spidered

Because mmdc.nl is a JavaScript-rendered SPA, a custom spider was used (see `_spider-artifacts/`):

1. **Seeds** — `_spider-artifacts/input/seed-urls.txt` (homepage and top-level sections).
2. **Crawler** — `_spider-artifacts/scripts/spider.py` (Python + Crawlee, headless browser) renders each page, extracts links, and classifies them by URL pattern (`url_classifier.py`).
3. **Catalog expansion** — search results paginated; the 11,738 manuscript record URLs enumerated via `extract_catalog_ids.py` / `generate_catalog_urls.py`. PDFs harvested via `extract_pdfs.py`.
4. **Consolidation** — all URLs deduplicated and merged into one spreadsheet (`combine_all_urls.py`, `create_unified_excel.py`).

Plan: [`_spider-artifacts/docs/PLAN-url-spider-mmdc.md`](_spider-artifacts/docs/PLAN-url-spider-mmdc.md).

## How the site was archived

The discovered URLs were submitted to the Wayback Machine using the scripts in `../../scripts/wbm-archiver/`, and locally rendered copies are stored under `_archiving-artifacts/local-archive/`. Notes on which WBM method worked best: [`_archiving-artifacts/docs/EXPERIMENT-REPORT-wbm-methods.md`](_archiving-artifacts/docs/EXPERIMENT-REPORT-wbm-methods.md).

## Folder structure

```
mmdc.nl/
├── README.md                             # This file
├── index.md                              # GitHub Pages version
├── images/                               # Screenshots
├── mmdc-urls-unified_15042026.xlsx       # Master URL list with WBM status
├── _spider-artifacts/                    # URL discovery
│   ├── input/seed-urls.txt
│   ├── scripts/                          # spider.py, url_classifier.py, …
│   ├── docs/
│   └── runtime/                          # checkpoints, logs, storage
└── _archiving-artifacts/                 # WBM submission & local rendering
    ├── scripts/
    ├── data/
    ├── docs/
    ├── reports/
    ├── screenshots/before|after/
    ├── local-archive/
    └── warc/
```

## Notes

- Two minor source issues: `…/AccessibilityStatement` (missing `.html`) and `…/index_Bifolium.pdx` (typo).
- Large local artifacts (full rendered site, WARC bundle) are kept out of GitHub — total exceeds GitHub's 2 GB limit; IA hosting is being arranged.
