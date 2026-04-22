---
layout: default
title: mmdc.nl URL spreadsheet
breadcrumb:
  - title: Archived sites
    url: /archived-sites/
  - title: mmdc.nl
    url: /archived-sites/mmdc.nl/
  - title: URL spreadsheet
---

[← Back to mmdc.nl](./)

# URL spreadsheet: `mmdc-urls-unified_15042026.xlsx`

The master spreadsheet [`mmdc-urls-unified_15042026.xlsx`](mmdc-urls-unified_15042026.xlsx) is the single source of truth for everything archived from mmdc.nl. It contains three sheets, described below.

| Sheet | Rows | Purpose |
|-------|-----:|---------|
| [`catalog-pages`](#sheet-catalog-pages) | 11,738 | One row per manuscript catalog record |
| [`catalog-pages-full-metadata`](#sheet-catalog-pages-full-metadata) | 18,724 | One row per item/sub-item, with full descriptive metadata |
| [`non-catalog-pages`](#sheet-non-catalog-pages) | 466 | One row per static HTML page (homepage, section indexes, glossary, about, links, press, etc.) |

All WBM timestamps use the standard 14-digit Wayback Machine format `YYYYMMDDhhmmss`.

---

## Sheet: `catalog-pages`

One row per manuscript record (`recordId` 1…N). This is the primary index of the catalog.

| Column | Description | Example |
|--------|-------------|---------|
| `RecordID` | Human-readable record label | `Record 2` |
| `RecordID_Num` | Numeric record ID from the original catalog | `2` |
| `Parent_RecordID` | Label of the parent record, if this is a sub-item | `Record 7` |
| `Parent_RecordID_Num` | Numeric ID of the parent record | `7` |
| `Title` | Manuscript title | `Tongeren fragments / Usuard` |
| `Signature` | Shelfmark / call number | `The Hague, KB : ms. 70 E 4` |
| `Date` | Date of the manuscript | `13th-15th century` |
| `Author` | Author, if known | `Usuard (-c. 875)` |
| `WBM_URL_capture` | Latest WBM capture URL (most recent snapshot found via CDX) | `https://web.archive.org/web/20260402123710/https://mmdc.nl/wbm/site/search/catalog-page-2.html` |
| `WBM_Timestamp_capture` | Timestamp of that capture | `20260402123710` |
| `WBM_URL_submission` | WBM URL returned when the page was first submitted | `https://web.archive.org/web/20260402143653/https://mmdc.nl/wbm/site/search/catalog-page-2.html` |
| `WBM_Timestamp_submission` | Timestamp of that original submission | `20260402143653` |
| `URL_old_defunct` | Original (now defunct) live mmdc.nl URL | `https://mmdc.nl/static/site/search/detail.html?recordId=2#r2` |
| `Section` | Section bucket from the URL classifier | `CATALOG_RECORDS` |
| `CatalogPage_File` | Filename of the pre-rendered static HTML | `catalog-page-2.html` |
| `URL_new_temp` | Temporary stable URL used for WBM submission | `https://mmdc.nl/wbm/site/search/catalog-page-2.html` |
| *(unlabeled)* | Excel hyperlink helper cell (`Klik`) | `Klik` |
| `Local_Path_Absolute` | Absolute path to the pre-rendered HTML on disk | `D:\…\_archiving-artifacts\local-archive\catalog-pages\catalog-page-2.html` |
| `Local_Path_Relative` | Same path, repo-relative | `_archiving-artifacts/local-archive/catalog-pages/catalog-page-2.html` |
| `Status` | Processing status notes (blank when OK) | |

---

## Sheet: `catalog-pages-full-metadata`

Expanded view of the catalog: one row per **item or sub-item** (a multi-part manuscript produces several rows), with the full descriptive metadata harvested from each catalog page.

| Column | Description |
|--------|-------------|
| `RecordID`, `RecordID_Num` | Record identifiers (as in `catalog-pages`) |
| `Parent_RecordID`, `Parent_RecordID_Num` | Parent record, if this row is a sub-item |
| `CatalogPage_File` | Source HTML file |
| `WBM_URL_capture` | Latest WBM capture URL |
| *(unlabeled)* | Excel hyperlink helper cell |
| `Item_Index` | 1-based index of this item within its parent record |
| `Is_MultiItem` | `True` if the parent record has more than one item |
| `Is_SubItem` | `True` if this row is a sub-item (not the parent) |
| `Signature` | Shelfmark of this item |
| `Parent_Signature` | Shelfmark of the parent manuscript |
| `Title` | Item title |
| `Author` | Author of the item |
| `Date` | Date of the item |
| `Language` | Primary language |
| `Original language` | Language of the original work, if a translation |
| `Alternative title (Dutch)` | Dutch alternative title |
| `Alternative title (English)` | English alternative title |
| `Alternative title (other)` | Alternative title in another language (often Latin) |
| `Annotations on the text` | Text-level annotations (contents, notes on the text) |
| `Material and composition` | Support material, number of folios |
| `Dimensions` | Leaf size / written space |
| `Layout and script` | Layout and script description |
| `Illustration and decoration` | Miniatures, initials, border decoration |
| `Binding` | Binding description |
| `Region of origin` | Region of origin |
| `Place of origin` | Specific place of origin |
| `Provenance` | Ownership / location history |
| `Acquisition` | How the holding institution acquired it |
| `Former owner and collections` | Previous owners and collections |
| `Alternative shelfmark` | Other shelfmarks the item is known by |
| `Incipit/explicit` | Incipit and/or explicit text |
| `Category and keyword` | Subject categorisation / keywords |
| `Remarks` | Free-text remarks |
| `Literature` | Bibliographic references |
| `Links` | External links (e.g. institutional catalog, KB portal) |
| `Image_Count` | Number of digitised images attached |
| `Image_URLs` | Semicolon-separated list of image resolver URLs |

---

## Sheet: `non-catalog-pages`

All static HTML pages (homepage, section landings, glossary entries, about pages, links pages, press, accessibility, copyright, etc.) — everything that is **not** a catalog detail record.

| Column | Description | Example |
|--------|-------------|---------|
| `Title` | Page title (derived from URL or HTML `<title>`) | `Collections` |
| `WBM_URL_capture` | Latest WBM capture URL | `https://web.archive.org/web/20251214072708/https://mmdc.nl/static/site/collections/index.html` |
| `WBM_Timestamp_capture` | Timestamp of that capture | `20251214072708` |
| `WBM_URL_submission` | WBM URL from the original submission | |
| `WBM_Timestamp_submission` | Timestamp of the original submission | |
| `URL_old_defunct` | Original (now defunct) live mmdc.nl URL | `https://mmdc.nl/static/site/collections/index.html` |
| `Section` | URL-classifier section bucket | `COLLECTIONS`, `HIGHLIGHTS`, `LITERATURE`, `RESEARCH_EDUCATION`, `ABOUT`, `LINKS`, `HOMEPAGE`, `OTHER` |
| `Local_File` | Filename of the local copy | `static__site__collections__index.html` |
| `Local_Path_Absolute` | Absolute path on disk | |
| `Local_Path_Relative` | Repo-relative path | `_archiving-artifacts/local-archive/static-pages/static__site__collections__index.html` |

---

## Notes

- `WBM_URL_capture` vs. `WBM_URL_submission`: the **submission** URL is what the Save Page Now API returned at the moment of submission; the **capture** URL is the most recent snapshot the CDX API currently reports (they usually differ for URLs that the Wayback Machine has re-crawled).
- A small number of rows have blank `WBM_*` values where the submission failed or no capture has been indexed yet. See the `Status` column on `catalog-pages` for notes.
- Filename encoding: static-page filenames use `__` as a path separator (e.g. `static__site__collections__index.html` corresponds to the URL path `/static/site/collections/index.html`).
