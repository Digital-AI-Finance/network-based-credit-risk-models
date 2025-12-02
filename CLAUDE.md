# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Jekyll-based GitHub Pages site** for the SNSF research project "Network-Based Credit Risk Models in P2P Lending Markets". The site is hosted at https://digital-ai-finance.github.io/network-based-credit-risk-models/.

## Build and Development Commands

```bash
# Local Jekyll development (requires Ruby and bundler)
bundle install
bundle exec jekyll serve --livereload

# Fetch latest publications from OpenAlex API
python scripts/fetch_publications.py

# Verify site functionality (uses Playwright for browser testing)
python scripts/verify_site.py

# Debug navigation issues
python scripts/debug_navigation.py

# Clean HTML tags from publication abstracts
python scripts/fix_publications.py
```

## Architecture

### Jekyll Site Structure

- **`index.md`**: Single-page site with 11 sections (Home, Team, Research, Publications, Analytics, Resources, News, Events, Collaborations, Funding, Contact)
- **`_config.yml`**: Jekyll configuration using Cayman theme (`jekyll-theme-cayman`)
- **`_data/`**: JSON data files consumed by Liquid templates
  - `publications.json` - Auto-fetched from OpenAlex API
  - `team.json` - Team member profiles
  - `news.json` - News items
  - `snsf_project_complete.json` - Full SNSF grant data
- **`assets/css/style.scss`**: Custom SCSS overriding Cayman theme
- **`assets/js/main.js`**: Navigation, smooth scrolling, BibTeX generation
- **`assets/js/visualizations.js`**: Chart.js and D3.js visualizations

### Navigation System

Dual navigation with synchronized scroll highlighting:
- **Top nav bar** (`.nav-container` / `.nav-menu`): Horizontal menu, always visible
- **Left sidebar** (`.sidebar-nav`): Fixed 180px sidebar, desktop only (min-width: 64em)

### Automated Workflows

**`.github/workflows/update-publications.yml`**: Weekly GitHub Action that:
1. Fetches publications from OpenAlex API
2. Filters to finance-related keywords
3. Auto-commits changes to `_data/publications.json`

## Critical Gotchas

### Jekyll HTML/Markdown Rendering

**Jekyll does NOT render Markdown inside HTML tags.** When content is inside `<section>` tags:
- Use `<h2>`, `<h3>` instead of `##`, `###`
- Use `<strong>` instead of `**`
- Use `<ul><li>` instead of `-` lists

### Publication Data Cleaning

HTML/XML tags in `publications.json` (e.g., `<ns3:p>` from OpenAlex) break Jekyll rendering. Run `scripts/fix_publications.py` to clean abstracts.

### CSS Layout for Sidebar

When sidebar is visible (desktop), these elements need `margin-left: 180px`:
- `.page-header`
- `.nav-container`
- `.main-content`
- `.site-footer`

## Data Sources

- **Publications**: OpenAlex API (`https://api.openalex.org`) - fetched by author ID
- **SNSF Grant Data**: Official source at `https://data.snf.ch/grants/grant/205487`
- **Team Images**: Local in `/images/`
