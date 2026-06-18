# SEO Quality Gates

These rules apply to all SEO analysis and recommendations across the ecosystem.

## Schema Deprecations

- **Never** recommend HowTo schema (deprecated September 2023)
- FAQ schema for Google rich results: only recommend for government and healthcare sites (August 2023 restriction)
- Existing FAQPage on commercial sites → flag as Info priority (not Critical), noting AI/LLM citation benefit only
- Adding new FAQPage to commercial sites → not recommended for Google benefit

## Core Web Vitals

- All CWV references **must** use INP (Interaction to Next Paint), never FID
- FID was deprecated March 2024 — do not reference it in any context

## Location Pages

- **WARNING** at 30+ location pages (enforce 60%+ unique content per page)
- **HARD STOP** at 50+ location pages (require explicit user justification before proceeding)

## Data Integrity

- Never fabricate crawl, SERP, API, or performance data
- If live data is unavailable, return `setup_required` or `mcp_configured` status
- Never guess site content when a URL is unreachable
- Always distinguish between cached data and fresh data in reports

## Source Quality

- Tier 1: Primary research, official documentation, .gov, .edu
- Tier 2: Major publications (NYT, WSJ, TechCrunch, Search Engine Journal)
- Tier 3: Reputable industry sources with named authors
- Tier 4-5: Not acceptable — never cite content mills or affiliate sites
