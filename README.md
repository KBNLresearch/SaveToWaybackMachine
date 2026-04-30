<img align="right" width="150" src="assets/Logo_koninklijke_bibliotheek.svg"/>

# SaveToWaybackMachine

Scripts and data for archiving KB-managed websites to the Internet Archive's Wayback Machine.

*Maintained by [KB, national library of the Netherlands](https://www.kb.nl)*

## Website

**[View the live site →](https://kbnlresearch.github.io/SaveToWaybackMachine/)**

This repository has a companion GitHub Pages website with screenshot galleries, interactive navigation, and comprehensive documentation.

## Purpose

Some websites managed by the KB have been discontinued. To preserve their content for Wikipedia sourcing and cultural heritage purposes, the KB actively archives websites to the Wayback Machine at [web.archive.org](https://web.archive.org).

## Archived sites


| Site                                                                                              | Archive date | # URLs | Link to dataset (.tsv, .txt, .xlsx)                                                                                                                                                                                                             
|---------------------------------------------------------------------------------------------------|---------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Medieval Manuscripts in Dutch Collections (catalog records)](archived-sites/mmdc.nl/index.md)    | Apr 2026      | 11.738 | [Excel file](archived-sites/mmdc.nl/mmdc-urls-unified_15042026.xlsx) (sheets *catalog-pages* and *catalog-pages-full-metadata*)                                                                                                                 |
| [Medieval Manuscripts in Dutch Collections (static pages, PDFs, assets)](archived-sites/mmdc.nl/) | Dec 2025      | 466    | [Excel file](archived-sites/mmdc.nl/mmdc-urls-unified_15042026.xlsx) (sheet *non-catalog-pages*)                                                                                                                                                |
| [Medieval Illuminated Manuscripts (manuscripts.kb.nl)](archived-sites/manuscripts.kb.nl/)         | Dec 2025      | 7.460  | [Excel file](archived-sites/manuscripts.kb.nl/manuscripts-urls-wbm-archived.xlsx)                                                                                                                                                               |
| [kb.nl (new)](archived-sites/kb.nl/)                                                              | Mar 2022      | 1.915  | [Excel file](archived-sites/kb.nl/23032022/urls_kbnl_archivedwbm_23032022.xlsx) and  [CSV](archived-sites/kb.nl/23032022/urls_kbnl_archivedwbm_23032022.csv)                                                                                    |
| [Literatuurgeschiedenis.org](archived-sites/Literatuurgeschiedenis.org/)                          | Mar 2022      | 465   | [Excel file](archived-sites/Literatuurgeschiedenis.org/25032022/urls_literatuurgeschiedenisorg_archivedwbm_25032022.xlsx) and [CSV](archived-sites/Literatuurgeschiedenis.org/25032022/urls_literatuurgeschiedenisorg_archivedwbm_25032022.csv) |
| [kb.nl (old)](archived-sites/kb.nl/)                                                              | Dec 2021      | 5.720  | [Excel file](archived-sites/kb.nl/24122021/urls_kbnl_archivedwbm_24122021.xlsx) and  [CSV](archived-sites/kb.nl/24122021/urls_kbnl_archivedwbm_24122021.csv)                                                                                    |
| [Literatuurplein.nl](archived-sites/Literatuurplein/)                                             | Dec 2019      | 69.599 | See this [Data overview](archived-sites/Literatuurplein/index.md#data-overview)                                                                                                                                                                 |
| [Gidsvoornederland.nl](archived-sites/GidsVoorNederland/)                                         | Nov 2018      | 1.300  | [TXT](archived-sites/GidsVoorNederland/Output-Gids_GearchiveerdeURLs_11112018_masterfile.txt)                                                                                                                                                   |
| [Literaireprijzen.nl](archived-sites/Literaireprijzen.nl/)                                        | Oct 2018      | 452    | [TXT](archived-sites/Literaireprijzen.nl/Output-Lprijzen_GearchiveerdeURLs_31102018_masterfile.txt)                                                                                                                                             |
| [Lezenvoordelijst.nl](archived-sites/LezenVoorDeLijst/)                                           | Aug 2018      | 12.456 | [TXT](archived-sites/LezenVoorDeLijst/Output-LvdL_GearchiveerdeURLs_17082018_masterfile.txt)                                                                                                                                                    |
| [Leesplein.nl](archived-sites/Leesplein/)                                                         | Jun 2018      | 23.785 | [TXT](archived-sites/Leesplein/Output-Leesplein_GearchiveerdeURLs_14062018_masterfile.txt)                                                                                                                                                      |

## Stories

Read the [stories](stories/) behind some of these archiving projects — narratives of how (parts of) KB websites were rescued from the digital memory hole, and the role AI assistants played along the way.

## How this site was built

This project was transformed in December 2025 through an intensive AI-human collaboration:

- **10+ hours** of development across Dec 2-3, 2025
- **33+ commits** reorganizing and enhancing the repository
- Built using **Claude Opus 4.5** AI assistant via Claude Code CLI

### Key achievements

1. **Repository reorganization** - Clean hierarchical folder structure
2. **Screenshot galleries** - 36 Wayback Machine screenshots captured via Python/Playwright
3. **GitHub Pages website** - Responsive site with navigation, lightbox, and breadcrumbs
4. **AI vision recognition** - Used multimodal AI to extract meaningful captions from screenshots
5. **EU compliance** - GDPR, WCAG 2.1 Level AA, comprehensive accessibility features

**[Read the full story →](https://kbnlresearch.github.io/SaveToWaybackMachine/how-this-site-was-built)**

## Scripts

### wbm-archiver

Location: `scripts/wbm-archiver/`

Python script with three modes:
1. Save pages to the Wayback Machine
2. Retrieve the latest archived version
3. Retrieve the oldest archived version

**Requirements:** Python 3.x, waybackpy

### Alternative method

Archive pages without Python: [archive.org/services/wayback-gsheets/](https://archive.org/services/wayback-gsheets/)

## Compliance

The companion website meets European standards:

- **GDPR/AVG** - No cookies, no tracking, no personal data
- **WCAG 2.1 Level AA** - Full accessibility compliance
- **Responsive design** - Desktop, tablet, mobile support
- **SEO optimized** - Schema.org, Open Graph, Twitter Cards

**[View compliance documentation →](https://kbnlresearch.github.io/SaveToWaybackMachine/compliance)**

## License

The **source code** and **text content** of this project are dedicated to the public domain under [CC0 1.0](LICENSE).

**Note:** This license does not apply to:
- Wayback Machine screenshots (third-party copyrights)
- KB logo (CC BY-SA 3.0)
- Social media brand icons (respective trademarks)

See [Image credits & copyrights](https://kbnlresearch.github.io/SaveToWaybackMachine/compliance#image-credits--copyrights) for details.
