---
layout: default
title: "Lessons learned: archiving mmdc.nl"
breadcrumb:
  - title: Archived sites
    url: /archived-sites/
  - title: mmdc.nl
    url: /archived-sites/mmdc.nl/
  - title: Lessons learned
---

[← Back to mmdc.nl](./)

# Lessons learned: archiving mmdc.nl to the Wayback Machine

*Project: Medieval Manuscripts in Dutch Collections (mmdc.nl) preservation*
*Team: Olaf Janssen (KB, human curator) & Claude/Jantien (AI assistant)*
*Timeline: December 2025 - April 2026*

---

## 1. The challenge

mmdc.nl - a medieval manuscripts database and cultural heritage resource hosted by the KB, national library of the Netherlands - was scheduled for shutdown on 15 December 2025. The site contained 12.204 URLs: 466 static pages/PDFs/assets and 11.738 manuscript catalog records. All needed to be preserved before the site went offline.

## 2. The JavaScript problem

The 11.738 catalog pages were the core challenge. Each page was a JavaScript Single Page Application (SPA):

1. Browser loads an HTML shell with an empty `<div id="recordDetail"></div>`
2. JavaScript (`ptp_v3.js`) reads the `recordId` from the URL
3. AJAX call fetches XML data from KB's SRU API (`jsru.kb.nl`)
4. XSLT transformation renders the content client-side

**The Wayback Machine does NOT execute JavaScript.** When WBM archives such pages, it captures only the empty HTML shell - the actual manuscript data is lost.

## 3. What we tried (and what failed)

### Attempt 1: Standard WBM Save Page Now
Submit URLs directly to `web.archive.org/save`. **Result: empty pages.** WBM fetches raw HTML without executing JavaScript.

### Attempt 2: WBM SPN2 API with authentication
Use Internet Archive credentials with capture flags. **Result: still empty** (9.311 bytes captured vs 33.545 when rendered). Even the authenticated API does not render JavaScript.

### Attempt 3: Headless browser + WBM submit
Render the page locally with Playwright, then submit the URL to WBM. **Result: still empty.** WBM fetches fresh HTML from the server, ignoring any local rendering.

### Method comparison experiment

We ran a controlled experiment comparing Method 2 (pre-render + submit) vs Method 3 (direct submit) on 5 test records:

| Method | Avg time/URL | Success rate | Projected time for 11.738 pages |
|--------|-------------|-------------|--------------------------------|
| Pre-render + submit | 41,4 s | 80% | 135 hours (5,6 days) |
| Direct submit | 7,6 s | 100% | 25 hours (1 day) |

Direct submission was 5x faster - but **both methods captured empty shells**. Neither could solve the JavaScript rendering problem.

## 4. The solution: local rendering pipeline

### Attempt 4: Local rendering with Playwright (success)

The breakthrough was to stop trying to make WBM render the JavaScript, and instead:

1. **Render locally** with a headless browser (Playwright)
2. **Save as standalone HTML** with all CSS inlined and images embedded as base64
3. **Upload the pre-rendered files** to a temporary webserver under a clean URL path
4. **Submit those static URLs** to WBM

### Unexpected problems along the way

**The shutdown banner:** After rendering, the page still showed a red shutdown notice. Investigation revealed it wasn't in the rendered HTML - it was **dynamically injected** by an external script (`default.js`) that the saved HTML still referenced. Solution: strip all external `<script>` tags.

**The broken logo:** The logo used a path with `../..` segments (`/static/site/../../assets/images/logo_mmdc.gif`) that didn't resolve in the standalone file. Solution: embed all images as base64 data URIs, making the HTML completely self-contained.

### The final rendering pipeline

Implemented in [render_catalog_full.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/render_catalog_full.py):

1. Load page in Playwright, wait for `#recordDetail` to become non-empty
2. Extract rendered DOM with inlined CSS
3. Remove shutdown banner and external scripts
4. Convert relative URLs to absolute
5. Embed images as base64
6. Save as standalone HTML (~150-160 KB per page)

Result: 11.738 self-contained HTML files, each working completely offline.

## 5. The rate limiting disaster

### Static pages (Phase 1)

The first archiving run for the 429 static pages used 12 concurrent connections. **Result: 83% failure rate** due to WBM rate limiting.

> "Very many pages failed!! ... this is disappointing!" - Olaf

**Solution:** A sequential archiver with 5-second delays between requests and exponential backoff. The slower approach achieved **429/429 (100%) success**. PDFs needed an extra-slow retry (10-second delays).

**Key insight:** Patience over speed. Going slower (5-10s between requests) achieved 100% success vs 83% failure with concurrent requests.

### Catalog pages (Phase 2)

The 11.738 catalog pages were submitted sequentially over 6 calendar days (Apr 2-7, 2026) at ~2.000-3.000 submissions/day. After an initial pass (11.658 successful) and a 34-minute retry of the remaining 80 pages: **11.738/11.738 (100%) indexed in the Wayback Machine**.

## 6. Key lessons for web archivists

1. **JavaScript is the enemy of web archiving.** Modern SPAs require special handling. Standard crawlers capture empty shells.
2. **Always verify WBM captures.** Don't assume successful submission = successful capture. Open the archived page and check the content is actually there.
3. **Headless browsers are essential.** Playwright, Puppeteer, or Selenium are necessary for JavaScript-rendered content.
4. **Watch for dynamic injection.** External scripts can re-inject content (banners, tracking) even after removal. Strip all external script references.
5. **Base64 embedding = self-contained archives.** Embedding images as data URIs creates truly standalone HTML files with no external dependencies.
6. **Go slow with WBM submissions.** Sequential requests with delays beat concurrent requests. The WBM rate limiter is aggressive.
7. **Institutional relationships matter.** Contact the Internet Archive early. Libraries and cultural heritage institutions often get special consideration.

## 7. Human-AI collaboration

This project was a collaboration between Olaf Janssen (human curator at the KB) and Claude/Jantien (AI assistant). The AI was renamed "Jantien" early in the project.

> "no, you are called Jantien from now, Claude is your maiden name!" - Olaf

The collaboration pattern: human makes decisions and sets direction, AI executes technical tasks (writing scripts, debugging, documentation). Session logs served as shared memory between sessions. The iterative problem-solving - trying approaches, analyzing failures, pivoting - was genuinely collaborative.

## 8. Tools developed

| Script | Purpose |
|--------|---------|
| [render_catalog_full.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/render_catalog_full.py) | Render all 11.738 catalog pages to standalone HTML |
| [render_static_pages.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/render_static_pages.py) | Render static pages to standalone HTML |
| [SaveToWBM_mmdc_non-catalog-pages.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/SaveToWBM_mmdc_non-catalog-pages.py) | Submit static pages to WBM with rate limiting |
| [SaveToWBM_mmdc_catalog-pages.py]({{ site.github.repository_url }}/blob/main/archived-sites/mmdc.nl/_archiving-artifacts/scripts/SaveToWBM_mmdc_catalog-pages.py) | Submit catalog pages to WBM with rate limiting |

---

*Combined from experiment reports and lessons-learned documents, December 2025 - April 2026*
