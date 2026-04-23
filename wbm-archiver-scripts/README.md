---
layout: default
title: wbm-archiver
breadcrumb:
  - title: Scripts
    url: /scripts/
  - title: wbm-archiver
---

[← Back to Scripts](../)

# wbm-archiver

*Version 2.0 - 30 November 2021*

Python script to archive URLs to the Internet Archive's Wayback Machine, or retrieve existing archived versions.

## Features

This script has three modes:

1. **Save pages** - Submit URLs to the Wayback Machine for archiving
2. **Retrieve latest** - Get the most recent archived version of a page
3. **Retrieve oldest** - Get the earliest archived version of a page

## Requirements

- Python 3.x
- waybackpy library (`pip install waybackpy`)

## Files

| File | Description |
|------|-------------|
| [SaveToWaybackMachine_v2_30112021.py](SaveToWaybackMachine_v2_30112021.py) | Main script (v2) |
| [SaveToWaybackMachine_v2_30112021_improvedVeraDeKok.py](SaveToWaybackMachine_v2_30112021_improvedVeraDeKok.py) | Improved version by Vera de Kok |

## Usage

```bash
# Install dependencies
pip install waybackpy

# Run the script
python SaveToWaybackMachine_v2_30112021.py
```

The script will prompt you for:
1. Input file with URLs (one per line)
2. Operation mode (save/retrieve latest/retrieve oldest)
3. Output file for results

