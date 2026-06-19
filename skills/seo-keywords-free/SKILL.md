---
name: seo-keywords-free
description: >
  Free domain authority (Ahrefs Domain Rating) lookup for your own domains and competitors.
  No API key required. Pairs with seo-trends and seo-dataforseo.
  Use when user says "domain rating", "DR", "ahrefs DR", "competitor authority",
  "free keywords", "competitor DR", or "free backlink metrics".
user-invokable: true
argument-hint: "<domain>"
license: MIT
metadata:
  author: dotusmanali
  version: "1.0.0"
  category: seo
---

# seo-keywords-free

## Purpose
Free domain authority signal (Ahrefs Domain Rating) for your own sites and competitors, with no API key. Pairs with `seo-trends` for demand and `seo-dataforseo` (paid, optional) for real volume/difficulty when a client deliverable needs exact numbers.

## When to use
- Quick competitor authority comparison (e.g. ForexGuru.pk vs. babypips.com vs. a local competitor).
- Sanity-checking whether a target keyword's SERP is dominated by high-authority sites (low chance) or weak ones (opportunity).
- Tracking your own domains' DR trend over time by re-running monthly and diffing against `.seo-cache`.

## Tool
**Ahrefs Domain Rating (free, no key)**
- Endpoint: `GET https://api.ahrefs.com/v3/public/domain-rating-free?target=<domain-or-url>&output=json`
- No auth header needed.
- Returns: `{"domain_rating": {"domain_rating": <float 0-100>, "license": "<url>"}}`
- **Attribution required if shown to end users/clients**: "Domain Rating by Ahrefs" linking to ahrefs.com. Internal use (your own analysis, not published) doesn't require this, but add it anyway to reports you hand to clients to stay safe.
- No documented rate limit, but this is a goodwill free endpoint — don't loop it across hundreds of domains in a tight script. Cache results in `.seo-cache/dr/` and only re-check weekly/monthly.

## Workflow
1. Pull the target domain + up to 4 competitor domains (from `seo-research` or user input).
2. Call the DR endpoint for each (sequential, small delay between calls, not parallel).
3. Cross-reference with `seo-trends` output for the same keyword set — high DR + rising demand = harder opportunity; low DR + rising demand = easier opportunity.
4. Cache results: `.seo-cache/dr/<domain>.json` with timestamp, so repeated audits show DR movement over time (feeds into the existing drift-monitoring feature).

## Script wrapper (suggested location: ${ANTIGRAVITY_PLUGIN_ROOT}/scripts/ahrefs_dr_free.py)
See `${ANTIGRAVITY_PLUGIN_ROOT}/scripts/ahrefs_dr_free.py` wrapper which can be executed:
```python
import requests

def get_domain_rating(target: str) -> dict:
    resp = requests.get(
        "https://api.ahrefs.com/v3/public/domain-rating-free",
        params={"target": target, "output": "json"},
        headers={"Accept": "application/json"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["domain_rating"]
```

## What this does NOT give you
- No backlink count or referring domains list (that's the paid Ahrefs Site Explorer API, or the educational `dataseo-mcp` scraper — see notes below, not recommended for client-facing numbers since it scrapes and can be inaccurate).
- No keyword-level data at all — this is domain-level authority only.

## Honest limitation
This is a single Ahrefs-controlled free endpoint with no SLA. If usage patterns look automated/abusive from Ahrefs' side, they can throttle or pull it without notice. Don't build a public-facing product around it — fine for internal/agency use where you control the call volume.
