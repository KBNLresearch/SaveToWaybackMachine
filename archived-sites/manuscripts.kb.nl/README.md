# manuscripts.kb.nl - Wayback Machine archive

*Archived: December 2025*

## About

This folder documents the archiving of [manuscripts.kb.nl](https://manuscripts.kb.nl/) — the **Medieval Illuminated Manuscripts** (Middeleeuwse Verluchte Handschriften / MVH) database of the KB, National Library of the Netherlands — to [The Wayback Machine](https://web.archive.org/).

The site was scheduled to be shut down on **15 December 2025**. All discoverable URLs were spidered and submitted to the Wayback Machine between 10-14 December 2025.

## Statistics

| Category | Count | Status |
|----------|------:|--------|
| Manuscript detail pages | 2,371 | Archived to WBM |
| Image gallery pages | 2,322 | Archived to WBM |
| Text-only views | 1,520 | Archived to WBM |
| Extended search pages | 806 | Archived to WBM |
| Literature search pages | 397 | Archived to WBM |
| Index pages | 9 | Archived to WBM |
| Static pages | 8 | Archived to WBM |
| Wiki priority URLs | 27 | Archived to WBM (unique to wiki) |
| **Total archived** | **7,460** | **100% success rate** |
| Spider output (all discovered) | 12,550 | 5,117 not submitted (mostly image search pages) |

Full per-URL status lives in [`manuscripts-urls-wbm-archived.xlsx`](manuscripts-urls-wbm-archived.xlsx). Column schema documented in [`excel-details.md`](excel-details.md).

## How the site was spidered

1. **Seeds** — `_spider-artifacts/seed-urls.txt` (homepage, introduction, background, advanced search, and all 9 index pages).
2. **Crawler** — `_spider-artifacts/scripts/spider.py` (Python + requests/BeautifulSoup) crawls each page, extracts links, and classifies them into categories (manuscript detail, image galleries, search results, indexes, static pages).
3. **Configuration** — `_spider-artifacts/scripts/config.py` defines seed URLs, crawl settings, and category definitions.
4. **Output** — 12,550 unique URLs written to `manuscripts-urls-spider-output.xlsx`, with crawl state checkpointed in `_spider-artifacts/data/spider_state.json`.

Plan: [`_spider-artifacts/docs/PLAN-url-spider-manuscripts.kb.nl.md`](_spider-artifacts/docs/PLAN-url-spider-manuscripts.kb.nl.md).

## How the site was archived

Archiving was done in two phases:

1. **Wiki priority** (10-11 Dec 2025) — 61 URLs linked from Dutch Wikipedia and Wikimedia Commons were archived first using `_archiving-artifacts/scripts/SaveToWBM_manuscripts_wiki_priority.py`. All 61 completed successfully in ~23 minutes.

2. **Bulk archiving** (11-14 Dec 2025) — 7,433 URLs from the spider output were submitted sheet by sheet (smallest first) using `_archiving-artifacts/scripts/SaveToWBM_manuscripts_bulk.py`. The script uses the Internet Archive SPN2 API with authenticated rate limits (17s between requests). All sheets completed with <0.1% transient error rate (4 errors, all retried successfully).

Plan: [`_archiving-artifacts/docs/PLAN-wbm-archiving-manuscripts.kb.nl.md`](_archiving-artifacts/docs/PLAN-wbm-archiving-manuscripts.kb.nl.md).

## Folder structure

```
manuscripts.kb.nl/
├── README.md                                # This file
├── excel-details.md                         # Spreadsheet column documentation
├── manuscripts-urls-wbm-archived.xlsx       # Master URL list with WBM status (7,460 URLs)
├── manuscripts-urls-spider-output.xlsx      # Full spider output (12,550 URLs)
├── wiki-priority-urls-WBM.xlsx              # Original wiki priority list (merged into master)
├── images/                                  # Before/after screenshots
├── _spider-artifacts/                       # URL discovery
│   ├── seed-urls.txt                        # Spider seed URLs
│   ├── scripts/                             # spider.py, config.py, excel_writer.py
│   ├── data/spider_state.json               # Crawl checkpoint (resume state)
│   ├── docs/                                # Spider plan
│   └── logs/                                # Crawl log
└── _archiving-artifacts/                    # WBM submission
    ├── scripts/                             # SaveToWBM_*.py, lookup_wbm_captures.py
    ├── data/                                # Progress/checkpoint files (not on GitHub)
    ├── docs/                                # Archiving plan
    └── logs/                                # Archiving logs
```

## Notes

- The spider discovered 12,550 URLs; 7,433 were selected for archiving (excluding ~5,100 image search result pages in the `SEARCH_RESULTS` and `OTHER` categories).
- 61 URLs linked from Wikimedia projects were archived as a priority; 34 of these overlap with the main bulk run, 27 are unique (mostly `/zoom/` image viewer URLs).
- The site served both `http://` and `https://` URLs — wiki links often used `http://` while the spider used `https://`.
