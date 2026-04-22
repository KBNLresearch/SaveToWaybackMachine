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
*Latest update: 22-04-2026*

## About

[mmdc.nl](https://mmdc.nl/) — the **Medieval Manuscripts in Dutch Collections** website of the KB, national library of the Netherlands — was scheduled to be phased out on **15 December 2025**.

<img src="images/homepage.png" width="500"/><br clear="all"/>

To preserve its content, URLs were archived to [The Wayback Machine](https://web.archive.org/) (WBM) of The Internet Archive in two phases. 

* First, its static pages, PDFs and images were archived during **December 2025**.
* In a second phase, the 11.738 manuscript catalog records were archived during **April 2026**, once their pre-rendered HTML form was ready (see below).

## Results & URL spreadsheet

* [mmdc-urls-unified_15042026.xlsx](mmdc-urls-unified_15042026.xlsx) is the master spreadsheet and the single source of truth for everything archived from mmdc.nl. It gives a detailed overview of all mmdc.nl URLs captured in the WBM. These include per-URL status, WBM capture URLs and timestamps, and local file paths for every individual item. 

* The [Excel detail page](excel-details.md) gives the full column-by-column breakdown of all three sheets in the Excel: 
  1. `non-catalog-pages` (466 rows - Phase 1, Dec 2025)
  2. `catalog-pages` (11.738 rows - Phase 2, April 2026)
  3. `catalog-pages-full-metadata` (18.724 rows) 


## Screenshots

### Before / after: static pages

Each pair shows the live mmdc.nl page (left) and the same URL as captured in the Wayback Machine (right, with the WBM toolbar visible at the top).

#### Homepage

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/homepage.png" width="380"/></td><td><img src="images/wbm_homepage.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/`](https://mmdc.nl/)
- WBM: [`…20251214093310/https://mmdc.nl/`](https://web.archive.org/web/20251214093310/https://mmdc.nl/)

#### Collections

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/collections-index.png" width="380"/></td><td><img src="images/wbm_collections-index.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/static/site/collections/index.html`](https://mmdc.nl/static/site/collections/index.html)
- WBM: [`…20251214072708/…/collections/index.html`](https://web.archive.org/web/20251214072708/https://mmdc.nl/static/site/collections/index.html)

#### Highlights

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/highlights-index.png" width="380"/></td><td><img src="images/wbm_highlights-index.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/static/site/highlights/index.html`](https://mmdc.nl/static/site/highlights/index.html)
- WBM: [`…20251214074859/…/highlights/index.html`](https://web.archive.org/web/20251214074859/https://mmdc.nl/static/site/highlights/index.html)

#### Literature

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/literature-index.png" width="380"/></td><td><img src="images/wbm_literature-index.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/static/site/literature/index.html`](https://mmdc.nl/static/site/literature/index.html)
- WBM: [`…20251214080033/…/literature/index.html`](https://web.archive.org/web/20251214080033/https://mmdc.nl/static/site/literature/index.html)

#### Research & Education (Palaeography)

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/research-education-index.png" width="380"/></td><td><img src="images/wbm_research-education-index.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/static/site/research_and_education/palaeography/index.html`](https://mmdc.nl/static/site/research_and_education/palaeography/index.html)
- WBM: [`…20251214082705/…/palaeography/index.html`](https://web.archive.org/web/20251214082705/https://mmdc.nl/static/site/research_and_education/palaeography/index.html)

#### About

<table>
<tr><th width="50%">Original (defunct)</th><th width="50%">Wayback Machine</th></tr>
<tr><td><img src="images/about.png" width="380"/></td><td><img src="images/wbm_about.png" width="380"/></td></tr>
</table>

- Original: [`https://mmdc.nl/static/site/about/index.html`](https://mmdc.nl/static/site/about/index.html)
- WBM: [`…20251214063529/…/about/index.html`](https://web.archive.org/web/20251214063529/https://mmdc.nl/static/site/about/index.html)

### Catalog pages in the Wayback Machine

The 11.738 catalog (manuscript detail) records were JavaScript-rendered on the live site, so they were pre-rendered to static HTML and submitted to the Wayback Machine under the `/wbm/site/search/catalog-page-N.html` path. No comparable "before" WBM screenshot could be captured, because the JS-based catalog pages were not suitable to be captured by the WBM — only the archived version of the pre-rendered HTML is shown below.

<table>
<tr>
  <th width="33%">catalog-page-2 — <em>Tongeren fragments / Usuard</em></th>
  <th width="33%">catalog-page-500 — <em>Book of hours</em></th>
  <th width="33%">catalog-page-5000 — <em>Lectionary</em></th>
</tr>
<tr>
  <td><img src="images/wbm_catalog-page-2.png" width="280"/></td>
  <td><img src="images/wbm_catalog-page-500.png" width="280"/></td>
  <td><img src="images/wbm_catalog-page-5000.png" width="280"/></td>
</tr>
</table>

**catalog-page-2** — Original (defunct): [`…detail.html?recordId=2`](https://mmdc.nl/static/site/search/detail.html?recordId=2#r2) · WBM: [`…20260402123710/…/catalog-page-2.html`](https://web.archive.org/web/20260402123710/https://mmdc.nl/wbm/site/search/catalog-page-2.html)

**catalog-page-500** — Original (defunct): [`…detail.html?recordId=500`](https://mmdc.nl/static/site/search/detail.html?recordId=500#r500) · WBM: [`…20260402222805/…/catalog-page-500.html`](https://web.archive.org/web/20260402222805/https://mmdc.nl/wbm/site/search/catalog-page-500.html)

**catalog-page-5000** — Original (defunct): [`…detail.html?recordId=5000`](https://mmdc.nl/static/site/search/detail.html?recordId=5000#r5000) · WBM: [`…20260403213400/…/catalog-page-5000.html`](https://web.archive.org/web/20260403213400/https://mmdc.nl/wbm/site/search/catalog-page-5000.html)

## How it was done

### Spidering the site

Because mmdc.nl is a JavaScript-rendered single-page application, a simple HTTP crawler could not discover all URLs. A custom spider was built in the `_spider-artifacts/` folder:

1. **Seed URLs** (`_spider-artifacts/input/seed-urls.txt`) — a handful of top-level section pages (homepage, `/collections/`, `/highlights/`, `/literature/`, `/research_and_education/`, `/about/`, `/links/`).
2. **Crawler** (`_spider-artifacts/scripts/spider.py`, Python + Crawlee with a headless browser) — renders each page, extracts internal links, and classifies them by URL pattern (`SEARCH_CATALOG`, `HIGHLIGHTS`, `LITERATURE`, `COLLECTIONS`, `STATIC_ASSETS`, …) via `url_classifier.py`.
3. **Catalog expansion** — search results were paginated and catalog IDs extracted (`extract_catalog_ids.py`, `generate_catalog_urls.py`) to enumerate all **11.738** manuscript records. PDF links were harvested separately (`extract_pdfs.py`).
4. **Consolidation** — all discovered URLs were deduplicated and written to a single spreadsheet (`combine_all_urls.py`, `create_unified_excel.py`), producing `mmdc-urls-unified_15042026.xlsx`.

Full planning notes are in [`_spider-artifacts/docs/PLAN-url-spider-mmdc.md`](_spider-artifacts/docs/PLAN-url-spider-mmdc.md).

### Rendering the catalog pages

On the (by now defunct) live mmdc.nl site, every manuscript record lived behind a single URL of the form `https://mmdc.nl/static/site/search/detail.html?recordId={N}#r{N}`. The HTML at that URL contained almost no content: an empty `<div id="recordDetail">` shell plus a block of JavaScript that fetched the record data client-side and injected it into the DOM. As a result, a conventional crawler — and the Wayback Machine's Save Page Now robot — captured only the empty shell, not the manuscript description.

To work around this, a headless-browser rendering pipeline was built using Python and Playwright:

1. **Load each record in a real browser.** For every `recordId` in the unified URL list, Playwright opened the live page with `wait_until="networkidle"` and then explicitly waited for `#recordDetail` to become non-empty (up to 30 s), so that the client-side JavaScript had fully populated the record.
2. **Inline all CSS.** External stylesheets were walked via `document.styleSheets`, their rules serialised, and fetched `<link rel="stylesheet">` files downloaded over HTTP and concatenated. The resulting CSS was embedded in a single `<style>` block in the rendered file, so each page is a self-contained standalone HTML file with no external dependencies.
3. **Write a stable, flat filename.** Each page was saved as `catalog-page-{N}.html` under `_archiving-artifacts/local-archive/catalog-pages/`, replacing the query-string URL (`/static/site/search/detail.html?recordId=N`) with a clean path-based one (`/wbm/site/search/catalog-page-N.html`) that the Wayback Machine could index cleanly.
4. **Resume, retry, log.** The pipeline checkpoints progress to a JSON file, retries transient failures up to three times, and logs any unrecoverable errors to another JSON file. This means the full 11.738-page run could be executed over several sessions without data loss.

The 11.738 rendered HTML files were then uploaded to a temporary KB hosted webserver at `https://mmdc.nl/wbm/site/search/catalog-page-{N}.html` and submitted to the Wayback Machine in April 2026. This is why the catalog pages in the WBM captures above show the full record content instead of an empty shell.

The same rendered files are kept locally under `_archiving-artifacts/local-archive/catalog-pages/` as a second, independent preservation copy.

### Submitting to the Wayback Machine

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

## Timeline

Dates reconstructed from the `WBM_Timestamp_submission` columns of the spreadsheet and from the surrounding session logs (all times UTC).

| Date | Activity | Output |
|------|----------|--------|
| 2025 (sporadic) | A handful of early WBM captures of individual pages (one each on 2025-01-20, 2025-04-29, 2025-05-14, 2025-09-17/18/19) | 7 static pages opportunistically in the Wayback Machine |
| Nov–early Dec 2025 | Site spidering with Python + Crawlee (headless browser), URL classification, catalog-ID enumeration, PDF harvesting | `mmdc-urls-UNIFIED.xlsx` — 317 static pages, 112 PDFs, 38 assets, 11.738 catalog record IDs |
| **2025-12-14** | Mass WBM submission of all static HTML pages via Save Page Now | 459 static-page submissions indexed same day |
| **2025-12-15** | mmdc.nl officially phased out; domain starts redirecting to the KB manuscripts landing page | Live site no longer available |
| Dec 2025 | PDFs and static asset images downloaded locally; 26 PDFs freshly indexed in WBM, 40 already had older captures | 112 PDFs + 38 images preserved locally |
| Late Dec 2025 – Mar 2026 | Headless-browser rendering of the 11.738 catalog records to self-contained HTML (`render_catalog_full.py`), with resume + retry across multiple sessions | `_archiving-artifacts/local-archive/catalog-pages/catalog-page-{N}.html` |
| **2026-04-02 → 2026-04-07** | Sequential WBM submission of all 11.738 pre-rendered catalog pages under `/wbm/site/search/catalog-page-{N}.html` | ≈ 2.000–3.000 submissions/day, 11.658 successful on first pass |
| 2026-04-08 → 2026-04-10 | CDX-API verification of indexed captures; identification of 80 URLs that needed retry | Retry list compiled |
| **2026-04-11** | 34-minute retry pass for the remaining 80 catalog pages | 11.738 / 11.738 catalog pages indexed in the Wayback Machine |
| **2026-04-15** | Unified spreadsheet exported with final WBM capture URLs and timestamps | [`mmdc-urls-unified_15042026.xlsx`](mmdc-urls-unified_15042026.xlsx) |

See also the [broader development timeline](../../how-this-site-was-built.md#april-2026-mmdcnl-catalog-pages-submitted-to-wbm) for day-by-day submission counts.

## Notes & known issues

- Two URLs have minor source-data issues: `…/AccessibilityStatement` (missing `.html`) and `…/index_Bifolium.pdx` (typo, should be `.pdf`).
- The large local artifacts (`_archiving-artifacts/local-archive/`, `warc/`, 11.738 rendered catalog pages) are kept outside GitHub because the total repo exceeds GitHub's 2 GB limit; long-term hosting via the Internet Archive is being arranged.
