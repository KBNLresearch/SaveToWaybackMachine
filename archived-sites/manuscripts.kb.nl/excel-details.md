---
layout: default
title: manuscripts.kb.nl URL spreadsheet
breadcrumb:
  - title: Archived sites
    url: /archived-sites/
  - title: manuscripts.kb.nl
    url: /archived-sites/manuscripts.kb.nl/
  - title: URL spreadsheet
---

[← Back to manuscripts.kb.nl](./)

# URL spreadsheet: `manuscripts-urls-wbm-archived.xlsx`

The master spreadsheet [`manuscripts-urls-wbm-archived.xlsx`](manuscripts-urls-wbm-archived.xlsx) contains all URLs from manuscripts.kb.nl (Medieval Illuminated Manuscripts / Middeleeuwse Verluchte Handschriften) that were archived to the Wayback Machine in December 2025, before the site's shutdown on 15 December 2025.

A second file, [`manuscripts-urls-spider-output.xlsx`](manuscripts-urls-spider-output.xlsx), contains the full spider crawl output (12,550 URLs) but has no archiving data. It is kept as a reference for the complete URL inventory.

## Sheets overview

| Sheet | Rows | Purpose |
|-------|-----:|---------|
| [`ALL_URLS`](#sheet-all_urls) | 7,460 | Union of all sheets below — one row per unique archived URL |
| [`show_manuscript`](#sheet-show_manuscript) | 2,371 | Manuscript detail pages |
| [`show_images_text`](#sheet-show_images_text) | 2,322 | Image gallery pages with text descriptions |
| [`show_text`](#sheet-show_text) | 1,520 | Text-only manuscript views |
| [`search_extended`](#sheet-search_extended) | 806 | Extended search result pages |
| [`search_literature`](#sheet-search_literature) | 397 | Literature search result pages |
| [`indexes`](#sheet-indexes) | 9 | Browse index pages (shelfmark, author/title, place, language, etc.) |
| [`static_pages`](#sheet-static_pages) | 8 | Static pages (homepage, introduction, background, advanced search) |
| [`wiki_priority`](#sheet-wiki_priority) | 61 | All URLs linked from Dutch Wikipedia or Wikimedia Commons |

---

## Column schema

All sheets share the same column structure:

| Column | Description | Example |
|--------|-------------|---------|
| `URL` | Original manuscripts.kb.nl URL | `https://manuscripts.kb.nl/show/manuscript/10+A+11` |
| `Source` | Sheet/category this URL belongs to | `show_manuscript` |
| `Wiki_Source` | Wikipedia or Commons origin, if linked from Wikimedia | `Wikipedia NL`, `Commons` |
| `Wiki_Page_Title` | Title of the Wikipedia/Commons page that links to this URL | `Meester van het gebedenboek van Dresden` |
| `Wiki_Page_ID` | Page ID on the source wiki | `2810762` |
| `WBM_Status` | Archiving result status | `OK` |
| `WBM_Job_ID` | Save Page Now (SPN2) job identifier | `spn2-abf176e5dee7...` |
| `WBM_URL_submission` | WBM URL returned by the SPN2 API at submission time | `https://web.archive.org/web/20251211014959/https://manuscripts.kb.nl/indexes/authortitle` |
| `WBM_Timestamp_submission` | Timestamp of the SPN2 submission | `2025-12-11T01:49:59` |
| `WBM_URL_capture` | Actual capture URL found via CDX API lookup | `https://web.archive.org/web/20251211005650/https://manuscripts.kb.nl/indexes/authortitle` |
| `WBM_Timestamp_capture` | Timestamp of that CDX capture | `2025-12-11T00:56:50` |
| `Error` | Error message, if the submission failed | *(blank when OK)* |

---

## Sheet: `ALL_URLS`

Union of all per-type sheets, plus 27 URLs that appear only in `wiki_priority` (mostly `/zoom/` and `/search/` pages linked from Wikimedia but not covered by the main archiving run). This is the single sheet to query if you want to look up any manuscripts.kb.nl URL.

---

## Sheet: `show_manuscript`

2,371 manuscript detail pages. Each URL follows the pattern `/show/manuscript/{shelfmark}` or `/show/manuscript/{shelfmark}/page/{n}`.

Example: `https://manuscripts.kb.nl/show/manuscript/10+A+11/page/1`

---

## Sheet: `show_images_text`

2,322 image gallery pages with accompanying text. URL pattern: `/show/images_text/{shelfmark}` or `/show/images_text/{shelfmark}/page/{n}`.

Example: `https://manuscripts.kb.nl/show/images_text/10+A+11`

---

## Sheet: `show_text`

1,520 text-only views of manuscripts. URL pattern: `/show/text/{shelfmark}` or `/show/text/{shelfmark}/page/{n}`.

Example: `https://manuscripts.kb.nl/show/text/10+A+11`

---

## Sheet: `search_extended`

806 extended search result pages. URL pattern: `/search/manuscript/extended/page/{n}/shelfmark/{shelfmark}`.

Example: `https://manuscripts.kb.nl/search/manuscript/extended/page/1/shelfmark/10+A+11`

---

## Sheet: `search_literature`

397 literature search pages, one per shelfmark. URL pattern: `/search/literature/{shelfmark}`.

Example: `https://manuscripts.kb.nl/search/literature/10+A+11`

---

## Sheet: `indexes`

9 browse index pages covering all index types on the site.

| URL path | Index type |
|----------|-----------|
| `/indexes/authortitle` | Author / title |
| `/indexes/haspart` | Has part |
| `/indexes/iconclass` | Iconclass subject |
| `/indexes/imagetype` | Image type |
| `/indexes/language` | Language |
| `/indexes/miniaturist` | Miniaturist |
| `/indexes/place` | Place of origin |
| `/indexes/shelfmark` | Shelfmark |
| `/indexes/titleImage` | Title / image |

---

## Sheet: `static_pages`

8 static pages: the homepage, introduction, background, advanced search, and related entry points.

---

## Sheet: `wiki_priority`

All 61 URLs that are linked from Dutch Wikipedia (`nl.wikipedia.org`) or Wikimedia Commons. These were archived as a priority before the main bulk run. 34 of these URLs also appear in other sheets (with wiki metadata added there too); 27 are unique to this sheet (mostly `/zoom/` image viewer URLs and some `/search/` pages with specific query parameters).

The `Wiki_Source`, `Wiki_Page_Title`, and `Wiki_Page_ID` columns are populated for all 61 rows in this sheet, and for the 34 overlapping rows in their respective type sheets.

---

## Notes

- **`WBM_URL_capture` vs. `WBM_URL_submission`**: the **submission** URL is what the Save Page Now (SPN2) API returned at the moment of archiving; the **capture** URL is the nearest snapshot the CDX API reports for that URL and timestamp. They usually differ slightly in timestamp because the CDX index records the actual crawl time, not the API response time.
- **`Wiki_Source` / `Wiki_Page_Title` / `Wiki_Page_ID`** are only populated for the ~57 URLs that are linked from Wikimedia projects. All other rows have these columns blank.
- **Archiving period**: all submissions were made between 10-14 December 2025.
- **Success rate**: 100% of the 7,460 URLs have `WBM_Status = OK`.
