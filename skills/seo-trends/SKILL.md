---
name: seo-trends
description: >
  Analyze market trends and search interest using Google Trends (via pytrends MCP).
  Explore keyword popularity over time, regional interest, and seasonal patterns.
  Use when user says "google trends", "search trends", "trending topics",
  "seasonal interest", "compare interest", or "market trends".
user-invokable: true
argument-hint: "<query> [--geo <region>] [--time <timeframe>]"
license: MIT
metadata:
  author: dotusmanali
  version: "1.0.0"
  category: seo
---

# seo-trends

## Purpose
Free demand-signal research using Google Trends and Google Suggest/Autocomplete. No paid API required. Use this before reaching for any paid keyword tool — it tells you if interest is rising, falling, or seasonal, and surfaces real autocomplete phrases people type.

## When to use
- `/seo:research <topic>` calls this as the first step for demand validation.
- Any time you need a quick "is this worth writing about" check.
- Seasonal content planning (e.g. PipsJournal trading topics, ForexGuru signal pages).
- Comparing interest across competing terms or brands.

## Tools available
1. **google-trends MCP** (`mcp__google-trends__*`)
   - `compare_keywords(keywords[], timeframe, geo)` — compare search interest for up to 5 keywords over time (trend line, rising/falling).
   - `get_interest_by_region(keyword, timeframe, geo, resolution)` — see where a keyword is most popular geographically.
   - `get_related_queries(keyword, timeframe, geo)` — find related search queries for a keyword (top and rising).
   - `get_related_topics(keyword, timeframe, geo)` — find related topics for a keyword.
   - `get_trending_searches(country)` — get today's trending searches.
   - Rate limit: unofficial, ~60s cooldown if you hit a 429. Don't hammer it in a loop; batch keywords (max 5 per call).

2. **google-ads-research MCP** (`mcp__google-ads-research__*`)
   - `get_autocomplete_suggestions(seed_keywords[])` — real Google Suggest phrases.
   - `get_trend_index(keywords[], geo)` — lightweight trend score.
   - `get_keyword_clusters()` — only works if Search Console service account is configured; groups GSC queries + autocomplete into intent clusters with page recommendations.

## Workflow
1. Take the seed keyword/topic from the user or from `/seo:research`.
2. Call `google-ads-research` autocomplete first — cheap, fast, no rate limit risk. This gives real phrasing variants.
3. Call `google-trends` compare_keywords on the top 3-5 variants to see direction (rising/flat/declining) over the last 12 months.
4. If geo matters (Pakistan vs. global vs. US for ForexGuru's audience), pass `geo` param.
5. Write findings to `.seo-cache/trends/<keyword-slug>.json` so repeated runs don't re-hit the rate limit same-day.
6. Pass output into `seo-keywords-free` or `/seo:create` for brief generation.

## What this does NOT give you
- No search volume numbers (Trends is a relative index 0-100, not absolute searches).
- No keyword difficulty score.
- No CPC or competition level.

For those, see `seo-keywords-free` (Domain Rating proxy + DataForSEO fallback) or set up `google-keyword-planner` MCP if exact volume becomes a blocker for a client deliverable.

## Output format
```json
{
  "seed": "forex trading signals",
  "geo": "PK",
  "autocomplete": ["forex trading signals free", "forex trading signals telegram", "..."],
  "trend_direction": "rising",
  "trend_window": "12m",
  "related_rising": ["..."],
  "notes": "Spike in March, likely seasonal — cross-check before committing a content calendar slot."
}
```
