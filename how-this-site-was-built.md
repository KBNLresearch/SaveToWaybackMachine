---
layout: default
title: How this site was built
---

[← Back to Home](./)

# How this site was built

**An AI-human collaboration journey**

This GitHub Pages site was created in multiple intensive sessions on December 2-3, 2025, through collaboration between a human curator at the KB (National Library of the Netherlands) and Claude Opus 4.5, an AI assistant by Anthropic.
yes,
## Table of contents

- [Timeline overview](#timeline-overview)
- [Development phases](#development-phases)
- [April 2026: mmdc.nl catalog pages submitted to WBM](#april-2026-mmdcnl-catalog-pages-submitted-to-wbm)
- [April 2026: manuscripts.kb.nl documentation](#april-2026-manuscriptskbnl-documentation)
- [Major achievement: AI vision recognition](#major-achievement-ai-vision-recognition)
- [KB huisstijl implementation](#kb-huisstijl-implementation)
- [Accessibility, privacy & licensing](#compliance--accessibility)
- [Why frequent commits matter](#why-frequent-commits-matter)

---

## Timeline overview

| Phase | Date | Time | Duration | Commits |
|-------|------|------|----------|---------|
| [Repository reorganization](#phase-1-repository-reorganization-dec-2-session-1) | Dec 2 | 17:02 - 19:52 | 2h 50m | 3 |
| [Screenshot galleries](#phase-2-screenshot-galleries-dec-2-session-1) | Dec 2 | (session 1) | 2h 06m | 5 |
| [GitHub Pages setup](#phase-3-github-pages-setup-dec-2-session-1) | Dec 2 | (session 1) | 40m | 4 |
| [UI refinements](#phase-4-ui-refinements-dec-2-session-1) | Dec 2 | (session 1) | 46m | 6 |
| [Bug fixes & polish](#phase-5-bug-fixes--polish-dec-2-session-1) | Dec 2 | (session 1) | 48m | 5 |
| [KB huisstijl & compliance](#phase-6-kb-huisstijl--compliance-dec-3-session-2) | Dec 3 | (session 2) | ~2h | 6 |
| [Code organization & footer redesign](#phase-7-code-organization--footer-redesign-dec-3-session-2) | Dec 3 | (session 2) | ~1h | 4 |
| [mmdc.nl catalog WBM submissions](#april-2026-mmdcnl-catalog-pages-submitted-to-wbm) | Apr 2–11, 2026 | (7 active days) | ~6 calendar days of wall-clock submission time | — |
| [manuscripts.kb.nl documentation](#april-2026-manuscriptskbnl-documentation) | Apr 24, 2026 | 1 session | ~3h | — |
| **Total** | | | **~10 hours** (+ catalog run + manuscripts docs) | **33+ commits** |

---

## Development phases

### Phase 1: Repository reorganization (Dec 2, session 1)

**Goal:** Transform a flat, disorganized folder structure into a clean, navigable repository.

**Actions:**
- Created hierarchical folder structure (`archived-sites/`, `scripts/`)
- Added `.gitignore` for IDE and system files
- Added CC0 1.0 LICENSE for public domain dedication
- Updated README.md with comprehensive documentation
- Added internal links and accurate URL counts to all site READMEs

**Commits:**
1. `70d72a3` - Reorganize repository structure
2. `a0c030f` - Update READMEs with internal links, image galleries, and accurate URL counts
3. `1cf205e` - Remove .claude and .prompt-page from gitignore and update session log

---

### Phase 2: Screenshot galleries (Dec 2, session 1)

**Goal:** Add visual screenshots from the Wayback Machine to showcase each archived site.

**Actions:**
- Created Python scripts using Selenium to capture Wayback Machine pages
- Captured 36 screenshots (6 per site) at deep-level URLs
- Trimmed donation banners (210px from top) for cleaner presentation
- Added responsive image galleries to all README files
- Iterated through multiple screenshot captures to fix errors

**Commits:**
4. `acbaea3` - Add Wayback Machine screenshot galleries to all archived site READMEs
5. `4537732` - Fix Wayback Machine screenshots - remove erroneous captures
6. `533e61b` - Add Wayback Machine screenshots with trimmed donation banners
7. `d77396a` - Replace screenshots with comprehensive deep-level captures
8. `7aebfca` - Update session log with final screenshot improvements

---

### Phase 3: GitHub Pages setup (Dec 2, session 1)

**Goal:** Create a browsable website from the repository documentation.

**Actions:**
- Created `_config.yml` with Jekyll configuration
- Built custom `_layouts/default.html` with:
  - Responsive CSS styling
  - Navigation breadcrumbs
  - Card-based navigation
  - Lightbox for image galleries
- Created landing pages for all sections
- Enabled GitHub Pages via API
- Added repository topics for discoverability

**Commits:**
9. `4e39f33` - Add GitHub Pages site with navigation and breadcrumbs
10. `80ff275` - Add screenshot gallery to kb.nl overview page
11. `1f5ffec` - Fix GitHub Pages layout and add index.md files
12. `55e3bfe` - Fix homepage text and sort table by date descending

---

### Phase 4: UI refinements (Dec 2, session 1)

**Goal:** Polish the user interface and fix visual issues.

**Actions:**
- Added screenshot thumbnails to homepage navigation cards
- Implemented lightbox with keyboard navigation (← → Esc)
- Fixed table formatting issues
- Extended lightbox to work on all content images
- Reordered tiles by date (descending)

**Commits:**
13. `6e20fbc` - Add screenshots to archived site cards on homepage
14. `ced0b2b` - Fix table formatting, add lightbox for gallery images
15. `1c7cc4e` - Reorder Browse Archived Sites tiles by date (descending)
16. `47f2d4e` - Fix dead links: remove images/ directory links
17. `94eddc9` - Fix pipe character causing table rendering issue
18. `5856154` - Add missing Literatuurplein screenshots

---

### Phase 5: Bug fixes & polish (Dec 2, session 1)

**Goal:** Fix remaining issues and improve content quality.

**Actions:**
- Fixed GidsVoorNederland error screenshots
- Added lightbox navigation arrows
- Fixed LezenVoorDeLijst error screenshot
- **Used AI vision to extract meaningful captions from screenshots**
- Changed "Dutch website" to "former Dutch website"
- Added subfolder links
- Reorganized kb.nl galleries by site version

**Commits:**
19. `8f3256a` - Fix GidsVoorNederland screenshots and add lightbox navigation
20. `a599157` - Extend lightbox to all content images
21. `8c4ce2b` - Fix LezenVoorDeLijst error screenshot
22. `7294044` - Fix LezenVoorDeLijst screenshot with blog post page
23. `6f14a67` - Update gallery captions and improve documentation

---

### Phase 6: KB huisstijl & compliance (Dec 3, session 2)

**Goal:** Apply official KB brand colors and add comprehensive compliance documentation.

**Actions:**
- Implemented KB huisstijl color palette as CSS variables
- Updated all design elements (header, links, footer, cards)
- Created full WCAG 2.1 AA accessibility compliance
- Added GDPR/AVG compliance documentation
- Implemented dark mode with KB colors
- Added comprehensive compliance.md page

**Commits:**
24-29. Various commits for KB huisstijl colors, compliance page, accessibility features

---

### Phase 7: Code organization & footer redesign (Dec 3, session 2)

**Goal:** Improve code maintainability and refine footer design.

**Actions:**
- Split inline CSS (~760 lines) into `assets/css/main.css`
- Split inline JavaScript (~200 lines) into `assets/js/lightbox.js`
- Redesigned footer: black background, white text, white KB logo
- Removed gold circles from social media icons

**Commits:**
30. `e49f31f` - Split CSS and JS into separate files
31. `7536c28` - Fix footer styling: all white text, no gold circles, white logo
32-33. Documentation updates

---

## April 2026: mmdc.nl catalog pages submitted to WBM

After the initial December 2025 WBM submissions covered the 466 non-catalog URLs (317 static HTML pages, 112 PDFs and 38 images) of [mmdc.nl](archived-sites/mmdc.nl/), the remaining 11.738 JavaScript-rendered **catalog pages** still could not be captured by the Wayback Machine directly — the live URLs returned an empty `<div id="recordDetail">` shell. Once each record had been rendered into a self-contained static HTML file (see [the catalog rendering write-up](archived-sites/mmdc.nl/#2-rendering-the-catalog-pages)), the pre-rendered files were uploaded to a temporary public path `https://mmdc.nl/wbm/site/search/catalog-page-{N}.html` and submitted to the WBM's Save Page Now API in a sequential run.

### Submission timeline (from `WBM_Timestamp_submission` in the Excel)

All 11.738 `catalog-pages` rows in [`mmdc-urls-unified_15042026.xlsx`](archived-sites/mmdc.nl/mmdc-urls-unified_15042026.xlsx) carry a WBM submission timestamp. Aggregated by day:

| Date (UTC) | Catalog pages submitted | First submission | Last submission |
|------------|------------------------:|:----------------:|:---------------:|
| 2026-04-02 | 361 | 14:36:53 | 23:59:41 |
| 2026-04-03 | 2.911 | 00:00:04 | 23:59:52 |
| 2026-04-04 | 2.921 | 00:00:23 | 23:59:26 |
| 2026-04-05 | 2.453 | 00:00:02 | 23:03:37 |
| 2026-04-06 | 1.083 | 11:09:14 | 23:59:47 |
| 2026-04-07 | 1.929 | 00:00:22 | 13:50:53 |
| 2026-04-11 | 80 (retry) | 17:10:07 | 17:44:21 |
| **Total** | **11.738** | **2026-04-02 14:36:53** | **2026-04-11 17:44:21** |

### What the timestamps tell us

- **Overall window:** submissions ran almost non-stop from the afternoon of April 2 until midday April 7, with the retry pass on April 11 picking up the 80 records that had failed on the first pass.
- **Steady throughput:** on the four full days (Apr 3–6) the pipeline averaged roughly **2.000–3.000 submissions/day**, or one submission every ~30–40 seconds — the pacing imposed by Save Page Now to avoid being rate-limited. The shorter ramps on April 2 (started 14:36) and April 7 (stopped 13:50) are consistent with a multi-session manual-kickoff operation rather than a single cron run.
- **April 8–10 gap:** no catalog submissions happened on April 8, 9, or 10. These days were used to run WBM CDX queries to verify that the first 11.658 submissions had been indexed, and to identify the 80 URLs that needed a retry.
- **April 11 cleanup pass:** a tight 34-minute run (17:10 → 17:44, 80 submissions) finished the last batch — exactly the pattern expected when a small list of failures is re-submitted one-by-one with no pacing issues.

The matching `WBM_Timestamp_capture` column in the same sheet (which holds the *latest* snapshot the CDX API reports for each URL) shows that in every case the Wayback Machine subsequently indexed the submission successfully — see the [catalog-page-2 / 500 / 5000 examples](archived-sites/mmdc.nl/#catalog-pages-in-the-wayback-machine) on the mmdc.nl page.

Scripts that drove the run: [`SaveToWBM_mmdc_catalog-pages.py`](archived-sites/mmdc.nl/_archiving-artifacts/scripts/SaveToWBM_mmdc_catalog-pages.py) (initial submission + April 11 retry). See the [mmdc.nl lessons learned](archived-sites/mmdc.nl/lessons-learned.md) for the full story.

---

## April 2026: manuscripts.kb.nl documentation

The [manuscripts.kb.nl](archived-sites/manuscripts.kb.nl/) site (Medieval Illuminated Manuscripts / MVH) was spidered and archived to the Wayback Machine in **December 2025** (10-14 Dec), before the site's shutdown on 15 December 2025. The archiving itself was done using custom Python scripts and the SPN2 API, resulting in **7,460 URLs archived with a 100% success rate**.

In **April 2026**, the documentation for this archival run was consolidated:

- Created `index.md`, `README.md`, and `excel-details.md` following the mmdc.nl documentation template
- Restructured the master spreadsheet (`manuscripts-urls-wbm-archived.xlsx`) to distinguish between WBM submission and capture URLs/timestamps
- Merged wiki-priority URLs (61 URLs linked from Dutch Wikipedia and Wikimedia Commons) into the master spreadsheet
- Ran CDX API lookups to populate the `WBM_URL_capture` and `WBM_Timestamp_capture` columns
- Took before/after screenshots for the documentation gallery
- Improved internal documentation (docstrings) of all spider and archiving scripts

For full details, see the [manuscripts.kb.nl archiving documentation](archived-sites/manuscripts.kb.nl/).

---

## Major achievement: AI vision recognition

### The breakthrough

One of the most significant achievements of this project was using **AI multimodal vision** to automatically extract meaningful captions from screenshot images.

### The problem

Gallery captions were generic and meaningless:
- "Pagina 104937"
- "Boek 277"
- "Boek 287"

### The solution

Claude Opus 4.5 used its native vision capabilities to:
1. **Read each PNG screenshot directly** (not just filenames)
2. **Extract page titles** from Wayback Machine banners
3. **Identify content** - author names, article titles, section headers
4. **Generate meaningful captions** in Dutch and Frisian

### Results

![Annotated LezenVoorDeLijst screenshot: the generic gallery caption "Pagina 104937" at the bottom of the image is circled in red, and the actual page title "Training verplaatst, nog plaatsen vrij" at the top is also circled — showing what the vision model read to replace the meaningless caption.](assets/images/ai-vision-example-annotated.png)
*Example: the AI read the page title "Training verplaatst" directly from the screenshot to replace the generic "Pagina 104937" caption — the first row in the table below.*

| Site | Old caption | New caption (from vision) |
|------|-------------|---------------------------|
| LezenVoorDeLijst | Pagina 104937 | Training verplaatst |
| LezenVoorDeLijst | Pagina 154224 | De man die alles achterliet |
| Leesplein | Boek 277 | Annemarie Bon |
| Leesplein | Boek 287 | Nanda Roep |
| Leesplein | Boek 342 | Ron Langenus |
| Literatuurplein | Prijzen Overzicht | Literaire prijzen |
| Literatuurplein | Canon Overzicht | Canon van de Nederlandse geschiedenis |

### Why this matters

This demonstrates AI can:
- **Replace manual data entry** for image cataloging
- **Extract structured metadata** from screenshot archives
- **Improve accessibility** through automatic alt-text generation
- **Scale to large archives** without human review of each image

---

## KB huisstijl implementation

On December 3, 2025, the site design was updated to align with the official KB (Koninklijke Bibliotheek) house style guidelines. This ensures visual consistency with other KB digital properties.

### Key changes

- Implemented official KB color palette (gold, blue, beige, pink, teal)
- Updated header, footer, links, and navigation with brand colors
- Redesigned footer: black background, white text, white logo
- Added CSS custom properties for easy maintenance
- Ensured WCAG 2.1 AA compliance for all color combinations

📄 **[Full KB huisstijl documentation →](kb-huisstijl.md)**

---

## Compliance & accessibility

As a final phase, comprehensive compliance testing and improvements were implemented to ensure the site meets European standards.

### GDPR/AVG compliance

| Aspect | Status |
|--------|--------|
| **Cookies** | None used |
| **Analytics** | No tracking |
| **Personal data** | None collected |
| **Third-party services** | None embedded |

### WCAG 2.1 Level AA

| Feature | Implementation |
|---------|----------------|
| **Skip link** | "Skip to main content" for screen readers |
| **Keyboard navigation** | Full keyboard support throughout |
| **Focus indicators** | 3px blue outline on all focusable elements |
| **Color contrast** | Minimum 4.5:1 ratio (WCAG AA) |
| **ARIA labels** | All interactive elements labeled |
| **Focus trapping** | Modal dialogs trap focus correctly |
| **Reduced motion** | Respects `prefers-reduced-motion` |

### Responsive design

| Breakpoint | Target |
|------------|--------|
| > 768px | Desktop |
| 601-768px | Tablet |
| 401-600px | Mobile |
| ≤ 400px | Small mobile |

Additional features:
- **Landscape orientation** optimization for lightbox
- **Touch swipe** navigation in image galleries
- **Dark mode** support via `prefers-color-scheme`
- **High contrast** mode support via `prefers-contrast`
- **Print styles** for clean printed output

### SEO optimization

| Feature | Implementation |
|---------|----------------|
| **Meta tags** | Title, description, keywords, canonical |
| **Open Graph** | Full social media sharing support |
| **Twitter cards** | Twitter sharing optimization |
| **Schema.org** | JSON-LD structured data (Website, Breadcrumb list, Organization) |

### Security

- **HTTPS enforced** via GitHub Pages
- **`rel="noopener"`** on all external links
- **No external scripts** - all JavaScript inline
- **Static content only** - no server-side processing

📄 **[Full Accessibility, Privacy & Licensing Documentation →](compliance.md)**

---

## Why frequent commits matter

One unexpected benefit of working with Claude Code is how it transforms version control from a chore into a natural part of the workflow.

### Before AI assistance

- Writing commit messages was manual and time-consuming
- Developers often batched many changes into single commits
- Git commands required memorization or documentation lookup
- Version control felt like overhead rather than a tool

### With AI assistance

- Commits happen in natural language: "commit and push"
- Each small change gets its own descriptive commit
- Complex Git operations become accessible to all skill levels
- Version control becomes an integral part of the conversation

### Benefits of frequent commits

| Benefit | Description |
|---------|-------------|
| **Detailed history** | Every change is documented with context |
| **Time tracking** | Commit timestamps enable accurate time expenditure analysis |
| **Easy rollback** | Small commits make it simple to undo specific changes |
| **Better collaboration** | Clear history helps others understand the evolution |
| **Learning record** | The commit log becomes a tutorial of the development process |
| **Accountability** | Each decision is recorded with its rationale |

### This project as example

This project has **40+ commits** over two sessions. Each commit represents a logical unit of work:
- Bug fixes get their own commits
- Style changes are separate from structural changes
- Documentation updates are tracked independently

The result is a complete, searchable history that serves as both documentation and a learning resource.

---

## Tools used

- **AI assistant:** Claude Opus 4.5 (claude-opus-4-5-20251101) via Claude Code CLI
- **Screenshot capture:** Python + Playwright + Pillow
- **Static site generator:** Jekyll (GitHub Pages)
- **Version control:** Git + GitHub
- **Browser automation:** Playwright (Chromium)

---

## License

The source code and text content of this project are dedicated to the public domain under [CC0 1.0](LICENSE). For image credits and copyright information, see [Accessibility, privacy & licensing](compliance#image-credits--copyrights).
