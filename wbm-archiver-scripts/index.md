---
layout: default
title: WBM archiver scripts
breadcrumb:
  - title: WBM archiver scripts
---

[← Back to Home](../)

# wbm-archiver

Python scripts to archive URLs to the Internet Archive's Wayback Machine, or retrieve existing archived versions.

---

## 1. General-purpose scripts

These scripts work with any website. They read a list of URLs from a text file and submit them to the Wayback Machine using the [waybackpy](https://pypi.org/project/waybackpy/) library.

| Script | Description |
|--------|-------------|
| [SaveToWaybackMachine_v2_30112021.py](SaveToWaybackMachine_v2_30112021.py) | Main script (v2, Nov 2021). Interactive: prompts for input file, operation mode, and output file. |
| [SaveToWaybackMachine_v2_30112021_improvedVeraDeKok.py](SaveToWaybackMachine_v2_30112021_improvedVeraDeKok.py) | Improved version by Vera de Kok, with better error handling. |

### Features

Three modes of operation:

1. **Save pages** — submit URLs to the Wayback Machine for archiving
2. **Retrieve latest** — get the most recent archived version of a page
3. **Retrieve oldest** — get the earliest archived version of a page

### Requirements

```bash
pip install waybackpy
```

### Usage

```bash
python SaveToWaybackMachine_v2_30112021.py
```

The script will prompt you for:
1. Input file with URLs (one per line)
2. Operation mode (save / retrieve latest / retrieve oldest)
3. Output file for results

---

## 2. mmdc.nl-specific scripts

These scripts were developed for the [mmdc.nl archiving project](../archived-sites/mmdc.nl/) and are located in the [`_archiving-artifacts/scripts/`]({{ site.github.repository_url }}/tree/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts) folder. They use the Internet Archive's [Save Page Now 2 (SPN2) API](https://web.archive.org/save) with authenticated access.

| Script | Description |
|--------|-------------|
| [SaveToWBM_mmdc_non-catalog-pages.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/SaveToWBM_mmdc_non-catalog-pages.py) | Submits non-catalog URLs (317 static HTML pages, 112 PDFs, 38 images) to the WBM. Used in Dec 2025: **466/466 (100%) archived**. |
| [SaveToWBM_mmdc_catalog-pages.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/SaveToWBM_mmdc_catalog-pages.py) | Submits pre-rendered catalog pages to the WBM. Used in Apr 2026: **11.738/11.738 (100%) archived**. |

### Features

Both scripts share the same robustness features, designed for long-running submissions (the catalog script ran for ~55 hours):

* **Resume capability** — progress saved after every URL; picks up exactly where it left off after a crash or interruption
* **Graceful shutdown** — Ctrl+C saves Excel + progress state before exit
* **Automatic retry** — exponential backoff on transient failures (timeouts, connection errors)
* **Rate-limit handling** — detects HTTP 429, pauses for 5 minutes + jitter
* **Offline detection** — after 3 consecutive failures, enters wait-for-connectivity mode with increasing delays (30s → 1m → 2m → 5m → 10m)
* **Excel locking detection** — retries if the Excel file is open in another application
* **Pause file** — create a `PAUSE.flag` file next to the script to pause after the current URL

### Requirements

```bash
pip install requests openpyxl python-dotenv
```

### Configuration

Both scripts require Internet Archive API credentials in a `.env` file:

```
IA_ACCESS_KEY=your_access_key
IA_SECRET_KEY=your_secret_key
```

Get your credentials at <https://archive.org/account/s3.php>.

### Usage

```bash
# Navigate to the scripts folder
cd archived-sites/mmdc.nl/_archiving-artifacts/scripts

# Submit non-catalog pages (static HTML, PDFs, images)
python SaveToWBM_mmdc_non-catalog-pages.py

# Submit catalog pages (pre-rendered HTML)
python SaveToWBM_mmdc_catalog-pages.py
```

Both scripts read URLs from `mmdc-urls-unified_15042026.xlsx` and write results back to the same Excel (WBM URL, timestamp, HTTP status). To reset and start fresh, delete the corresponding progress JSON file in `_archiving-artifacts/data/`.

### Adapting for other projects

These scripts can be adapted for other websites by:

1. Changing the Excel file path and sheet name
2. Adjusting the column mapping (which columns to read URLs from, which to write results to)
3. Updating the `.env` credentials

The core submission logic (SPN2 API calls, retry handling, progress tracking) is reusable as-is.

---

For more context on how these scripts were used, see the [mmdc.nl archiving documentation](../archived-sites/mmdc.nl/) and the [lessons learned](../archived-sites/mmdc.nl/lessons-learned.md).
