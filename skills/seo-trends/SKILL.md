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

# Google Trends Analysis
## Shared Data Cache

**Step 0 -- Check shared data cache:**

Before gathering, check `.seo-cache/` for reusable context.
Check `.seo-cache/site-meta.json` for industry and market context.

## Overview

This skill leverages the `google-trends` MCP server (based on `pytrends`) to
retrieve search interest data directly from Google Trends.

**Capabilities:**
- Interest over time (Last 5 years, last hour, etc.)
- Interest by region (Country, sub-region, city)
- Related queries (Top and Rising)
- Keyword comparison (Up to 5 terms)

## Commands & Tools

The agent should use the following tools provided by the `google-trends` MCP:

| Tool | Purpose |
|------|---------|
| `get_interest_over_time` | Fetch historical interest data for keywords |
| `get_interest_by_region` | Analyze where interest is highest geographically |
| `get_related_queries` | Find trending and top related search terms |
| `get_trending_searches` | Get currently trending searches for a region |
| `get_suggestions` | Get keyword suggestions from Google Trends |

## Workflows

### 1. Market Interest Analysis
Identify if a topic is growing, stable, or declining.

**Steps:**
1. Call `get_interest_over_time` with primary keywords.
2. Analyze the trend line: is there a consistent upward trajectory?
3. Identify seasonal peaks (e.g., "tax return" in April).

### 2. Regional Targeting
Find the best geographic locations for a campaign.

**Steps:**
1. Call `get_interest_by_region` for target keywords.
2. Rank sub-regions by interest index.
3. Suggest localized content or ad targeting based on high-interest areas.

### 3. Content Opportunity Discovery
Find "Rising" topics before they peak.

**Steps:**
1. Call `get_related_queries` for a niche.
2. Look for "Rising" keywords with "+500%" or "Breakout" status.
3. Propose blog post or landing page ideas for these emerging terms.

## Output Format

- **Trend Summary**: High-level description of interest (Growing / Stable / Seasonal).
- **Regional Heatmap**: List of top regions with interest index (0-100).
- **Related Topics**: Table of Top and Rising queries.
- **Actionable Insight**: One sentence on how to use this data for SEO.

## Error Handling

| Scenario | Action |
|----------|--------|
| Rate Limit (429) | Google Trends has aggressive rate limiting. Wait 60 seconds and retry. Inform the user of the wait. |
| No Data | If a query is too niche, Trends may return no data. Suggest broader terms. |
| Invalid Region | Ensure ISO country codes (e.g., "US", "GB") are used. |

## Write to shared data cache

After completing analysis, write a summary to `.seo-cache/trends.json`.
Include `top_regions`, `rising_queries`, and `trend_direction`.
