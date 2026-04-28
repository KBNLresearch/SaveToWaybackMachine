---
layout: default
title: Accessibility, privacy & licensing
description: Accessibility statement, privacy compliance, and licensing documentation for the SaveToWaybackMachine website
breadcrumb:
  - title: Accessibility, privacy & licensing
---

[← Back to Home](./)

# Accessibility, privacy & licensing

This page documents the accessibility features, privacy compliance, and technical standards implemented on this website.

---

## GDPR/AVG compliance

This website is fully compliant with the **General Data Protection Regulation (GDPR)** and the Dutch **Algemene Verordening Gegevensbescherming (AVG)**.

### Data collection

| Aspect | Status |
|--------|--------|
| **Cookies** | No cookies used |
| **Analytics** | No tracking or analytics |
| **Personal data** | No personal data collected |
| **Contact forms** | None present |
| **Third-party services** | None embedded |
| **User accounts** | Not applicable |

### Privacy by design

- **Static site**: This is a static GitHub Pages site with no server-side processing
- **No databases**: No user data is stored in any database
- **No sessions**: No session tracking or user identification
- **External links**: Links to external sites (KB, Internet Archive) open in context with `rel="noopener"` for security

---

## WCAG 2.1 accessibility

This website strives to meet **WCAG 2.1 Level AA** compliance, the European standard for web accessibility.

### Implemented features

#### Perceivable (Principle 1)

| Guideline | Implementation |
|-----------|----------------|
| **1.1 Text alternatives** | All images have descriptive `alt` attributes |
| **1.3 Adaptable** | Semantic HTML5 structure (header, nav, main, footer) |
| **1.4 Distinguishable** | Minimum 4.5:1 color contrast ratio for text |

#### Operable (Principle 2)

| Guideline | Implementation |
|-----------|----------------|
| **2.1 Keyboard accessible** | All interactive elements keyboard-navigable |
| **2.4 Navigable** | Skip-to-content link, breadcrumb navigation |
| **2.4.7 Focus visible** | Clear focus indicators (3px blue outline) |

#### Understandable (Principle 3)

| Guideline | Implementation |
|-----------|----------------|
| **3.1 Readable** | Language declared (`lang="nl"`) |
| **3.2 Predictable** | Consistent navigation and layout |

#### Robust (Principle 4)

| Guideline | Implementation |
|-----------|----------------|
| **4.1 Compatible** | Valid HTML5, ARIA landmarks and labels |

### Accessibility features

- **Skip to main content** link for screen reader users
- **Keyboard navigation** throughout the site
- **Focus trapping** in modal dialogs (lightbox)
- **ARIA labels** on all interactive elements
- **Reduced motion** support via `prefers-reduced-motion`
- **High contrast mode** support via `prefers-contrast`
- **Screen reader announcements** (`aria-live` regions)

---

## Responsive design

The site is fully responsive across all device types and orientations.

### Breakpoints

| Device | Width | Optimizations |
|--------|-------|---------------|
| **Desktop** | > 768px | Full layout, 3-column grid |
| **Tablet** | 601-768px | Adapted spacing, 2-column grid |
| **Mobile** | 401-600px | Single column, larger touch targets |
| **Small mobile** | ≤ 400px | Compact layout, optimized typography |

### Orientation support

- **Portrait mode**: Optimized single-column layout
- **Landscape mode**: Adjusted lightbox sizing, compact captions

### Touch interactions

- **Swipe navigation** in image lightbox (left/right)
- **Touch-friendly** button sizes (minimum 44px)
- **Smooth scrolling** with `scroll-behavior: smooth`

---

## SEO optimization

### Meta tags

| Tag | Purpose |
|-----|---------|
| `<title>` | Page-specific titles |
| `meta description` | Page descriptions |
| `meta keywords` | Relevant keywords |
| `link canonical` | Canonical URLs |
| `meta robots` | Index, follow directive |

### Open graph

Full Open Graph support for social media sharing:
- `og:title`, `og:description`, `og:url`
- `og:type`, `og:site_name`, `og:locale`

### Twitter cards

Twitter Card meta tags for Twitter sharing.

### Schema.org structured data

JSON-LD structured data including:
- **Website** schema with publisher information
- **Breadcrumb list** schema for navigation
- **Organization** schema for KB

---

## Security

### Implemented measures

| Measure | Implementation |
|---------|----------------|
| **HTTPS** | Enforced via GitHub Pages |
| **External links** | `rel="noopener"` on all external links |
| **No inline scripts** | JavaScript in document body only |
| **No external scripts** | No third-party JavaScript |
| **Content security** | Static content only, no user input |

### GitHub Pages security

GitHub Pages provides:
- Automatic HTTPS with valid SSL certificates
- DDoS protection
- Regular security updates
- No server-side vulnerabilities (static hosting)

---

## Browser support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | Full support |
| Firefox | 88+ | Full support |
| Safari | 14+ | Full support |
| Edge | 90+ | Full support |
| Mobile Safari | iOS 14+ | Full support |
| Chrome Mobile | Android 10+ | Full support |

### Progressive enhancement

- Core content accessible without JavaScript
- Enhanced features (lightbox) require JavaScript
- CSS Grid with fallback for older browsers

---

## Dark mode

The site respects the user's system preference for dark mode:
- Automatic detection via `prefers-color-scheme: dark`
- Adjusted colors for readability
- Maintained contrast ratios

---

## Print styles

Optimized print stylesheet including:
- Visible URLs after links
- Removed lightbox and interactive elements
- Preserved KB logo colors
- Prevented page breaks within cards

---

## Validation & testing

### Tools used

| Tool | Purpose |
|------|---------|
| **W3C HTML validator** | HTML5 validation |
| **WAVE** | Accessibility testing |
| **Lighthouse** | Performance, accessibility, SEO audit |
| **axe DevTools** | Automated accessibility testing |
| **Color contrast analyzer** | WCAG contrast verification |

### Testing checklist

- [x] HTML5 validation passes
- [x] No WCAG 2.1 AA violations
- [x] Keyboard navigation complete
- [x] Screen reader compatible
- [x] Mobile responsive (320px - 1920px)
- [x] Touch interactions working
- [x] Dark mode rendering correct
- [x] Print preview acceptable

---

## Known limitations

Due to GitHub Pages static hosting:

1. **No custom HTTP headers**: Cannot set CSP, HSTS, or other security headers directly
2. **No server-side redirects**: Must rely on client-side or Jekyll redirects
3. **No dynamic content**: All content is pre-generated

These are acceptable trade-offs for a documentation and archive reference site.

---

## Compliance standards summary

| Standard | Level | Status |
|----------|-------|--------|
| **GDPR/AVG** | Full | Compliant |
| **WCAG 2.1** | AA | Compliant |
| **EU Web Accessibility Directive** | - | Compliant |
| **HTML5** | - | Valid |
| **Schema.org** | - | Implemented |

---

## Image credits & copyrights

This section clarifies the different licensing that applies to different types of content on this site.

### What is CC0 (public domain)

The following content is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/):

- **All source code** (Python scripts, HTML, CSS, JavaScript)
- **All text content** (documentation, README files, this compliance page)
- **Data files** (CSV, TXT files with URLs and metadata)

### What is NOT public domain

#### Wayback Machine screenshots

The screenshots displayed in the gallery sections are captures of archived websites. These websites may contain copyrighted content owned by third parties. The screenshots are displayed here for:

- **Documentary purposes** - Demonstrating the archiving work performed
- **Cultural heritage preservation** - Showcasing Dutch digital heritage
- **Educational purposes** - Illustrating web archiving practices

**Copyright notice:** If any rights holder believes their copyright is infringed by the display of these screenshots, please [file a GitHub Issue]({{ site.github.repository_url }}/issues) and the KB will remove the images as soon as possible.

#### KB logo

The KB (Koninklijke Bibliotheek) logo is licensed under [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

- **Source**: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Logo_koninklijke_bibliotheek.svg)
- **Attribution**: KB, national library of the Netherlands

#### Social media brand icons

The social media icons (Bluesky, Mastodon, LinkedIn, YouTube, Instagram, Facebook, GitHub) represent registered trademarks of their respective companies. They are used here solely to link to the KB's official social media presence.

### Summary

| Content type | License |
|--------------|---------|
| Source code | CC0 1.0 (Public Domain) |
| Text & documentation | CC0 1.0 (Public Domain) |
| Data files | CC0 1.0 (Public Domain) |
| Wayback Machine screenshots | Third-party copyrights might apply |
| [KB logo](https://nl.wikimedia.org/wiki/Bestand:Logo_koninklijke_bibliotheek.svg) | CC BY-SA 3.0 |
| Social media brand icons | Trademarks of respective companies |

---

## Contact

For accessibility issues, compliance questions, or **copyright concerns**, please contact:

- **Organization**: KB, national library of the Netherlands
- **Website**: [www.kb.nl](https://www.kb.nl)
- **GitHub Issues**: [Report an issue]({{ site.github.repository_url }}/issues)

---

*Last updated: April 2026*
