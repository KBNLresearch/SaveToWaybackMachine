---
layout: default
title: mmdc.nl
breadcrumb:
  - title: Archived sites
    url: /archived-sites/
  - title: mmdc.nl
---

[← Back to Archived sites](../)

# Saving mmdc.nl to the Wayback Machine
*Latest update: 15-04-2026*

<img src="images/homepage.png" width="500"/><br clear="all"/>

## Wayback Machine screenshots

| Homepage | Collections | Highlights |
|:--------:|:-----------:|:----------:|
| <img src="images/wbm_homepage.png" width="280"/> | <img src="images/collections-index.png" width="280"/> | <img src="images/highlights-index.png" width="280"/> |

| Literature | Research & Education | About |
|:----------:|:--------------------:|:-----:|
| <img src="images/literature-index.png" width="280"/> | <img src="images/research-education-index.png" width="280"/> | <img src="images/about.png" width="280"/> |

## About

[mmdc.nl](https://mmdc.nl/) — the **Medieval Manuscripts Digital Collection** of the KB, National Library of the Netherlands — was scheduled to be phased out on **15 December 2025**.

To preserve its content, its URLs (static pages, catalog records, PDFs and images) were submitted to [The Wayback Machine](https://web.archive.org/) (WBM) of The Internet Archive during **December 2025**. In addition, a full local rendering of the site was produced, because the catalog pages are JavaScript-rendered and the WBM capture alone does not always reproduce them faithfully.

The results are listed in [`mmdc-urls-unified_15042026.xlsx`](mmdc-urls-unified_15042026.xlsx).

## Statistics

| Category | Count | Status |
|----------|------:|--------|
| Static HTML pages | 317 | Submitted to WBM, local copies exist |
| Catalog pages | 11,738 | Rendered locally (100%) |
| PDFs | 112 | 26 indexed in Dec 2025, 40 older only, 46 none |
| Static asset images | 38 | Downloaded locally |
| **Total WBM submissions** | **429** | Submitted, indexing verified |

## How the site was spidered

Because mmdc.nl is a JavaScript-rendered single-page application, a simple HTTP crawler could not discover all URLs. A custom spider was built in the `_spider-artifacts/` folder:

1. **Seed URLs** (`_spider-artifacts/input/seed-urls.txt`) — a handful of top-level section pages (homepage, `/collections/`, `/highlights/`, `/literature/`, `/research_and_education/`, `/about/`, `/links/`).
2. **Crawler** (`_spider-artifacts/scripts/spider.py`, Python + Crawlee with a headless browser) — renders each page, extracts internal links, and classifies them by URL pattern (`SEARCH_CATALOG`, `HIGHLIGHTS`, `LITERATURE`, `COLLECTIONS`, `STATIC_ASSETS`, …) via `url_classifier.py`.
3. **Catalog expansion** — search results were paginated and catalog IDs extracted (`extract_catalog_ids.py`, `generate_catalog_urls.py`) to enumerate all **11,738** manuscript records. PDF links were harvested separately (`extract_pdfs.py`).
4. **Consolidation** — all discovered URLs were deduplicated and written to a single spreadsheet (`combine_all_urls.py`, `create_unified_excel.py`), producing `mmdc-urls-unified_15042026.xlsx`.

Full planning notes are in [`_spider-artifacts/docs/PLAN-url-spider-mmdc.md`](_spider-artifacts/docs/PLAN-url-spider-mmdc.md).

## How the site was archived

Once the full URL list was known, the URLs were submitted to the Wayback Machine via the scripts in `scripts/wbm-archiver/` (top-level of this repo) and locally rendered copies were saved under `_archiving-artifacts/local-archive/`. Experiment notes on which WBM submission method worked best are in [`_archiving-artifacts/docs/EXPERIMENT-REPORT-wbm-methods.md`](_archiving-artifacts/docs/EXPERIMENT-REPORT-wbm-methods.md).

## Folder structure

```
mmdc.nl/
├── index.md                              # This page
├── README.md                             # GitHub-view version
├── images/                               # Screenshots used in docs
├── mmdc-urls-unified_15042026.xlsx       # Master URL list with WBM status
├── _spider-artifacts/                    # URL discovery (the spidering run)
│   ├── input/seed-urls.txt
│   ├── scripts/                          # spider.py, url_classifier.py, …
│   ├── docs/                             # PLAN-url-spider-mmdc.md, DISCOVERY-sru-api.md
│   └── runtime/                          # checkpoints, logs, storage
└── _archiving-artifacts/                 # WBM submission & local rendering
    ├── scripts/                          # Python archiving scripts
    ├── data/                             # JSON result files
    ├── docs/                             # Experiment reports, lessons learned
    ├── reports/                          # Run reports
    ├── screenshots/before|after/         # Comparison screenshots
    ├── local-archive/                    # Full local site copy
    └── warc/                             # WARC bundle (work in progress)
```

## Notes & known issues

- Two URLs have minor source-data issues: `…/AccessibilityStatement` (missing `.html`) and `…/index_Bifolium.pdx` (typo, should be `.pdf`).
- The large local artifacts (`_archiving-artifacts/local-archive/`, `warc/`, 11,738 rendered catalog pages) are kept outside GitHub because the total repo exceeds GitHub's 2 GB limit; long-term hosting via the Internet Archive is being arranged.