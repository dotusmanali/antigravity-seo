<p align="center">
  <img src="screenshots/cover-image.svg" alt="Antigravity SEO & Blog Suite Banner" width="100%">
</p>

# Antigravity SEO & Blog Suite — Complete SEO & Content Ecosystem

A production-grade, state-of-the-art SEO analysis and automated blog creation ecosystem built natively for the **Antigravity** developer platform. 

This suite bridges deep-dive search intelligence with automated editorial workflows. It combines determinism (via local Python runners) with real-time scraping and official APIs (via MCP) to deliver expert-level audits, keyword research, core visual charts, and publish-ready content.

[![Workflows Count](https://img.shields.io/badge/Workflows-60-emerald?style=flat-square)](skills/)
[![AI Agents Count](https://img.shields.io/badge/AI_Agents-32-blueviolet?style=flat-square)](agents/)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square)](pyproject.toml)
[![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)](LICENSE)

---

## 1. System Architecture & Subsystems

The suite is modular, dividing complexity across three key architectural layers:

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TD
  User["User Prompt"] --> Run["Master Supervisor (/seo:run)"]
  
  subgraph Routing ["Unified Routing Layer"]
    Run -->|"Coordinate Context"| Cache[".seo-cache/ (Shared Memory)"]
    Run -->|"SEO Tasks"| SEO["SEO Orchestrator<br/>(skills/seo/SKILL.md)"]
    Run -->|"Blog Tasks"| Blog["Blog Orchestrator<br/>(skills/blog/SKILL.md)"]
  end

  subgraph SEOSubsystem ["SEO Subsystem (29 Sub-skills & 27 Agents)"]
    SEO --> SEO_Audits["Audits & Technical:<br/>- seo-technical (Agent)<br/>- seo-audit (Skill)<br/>- seo-page (Skill)<br/>- seo-content (Agent)<br/>- seo-schema (Agent)<br/>- seo-images (Agent)<br/>- seo-performance (Agent)<br/>- seo-sitemap (Agent)<br/>- seo-visual (Agent)<br/>- seo-hreflang (Agent)"]
    SEO --> SEO_Intel["Search & Keyword Intel:<br/>- keyword-research (Skill)<br/>- seo-trends (Agent/Skill)<br/>- seo-keywords-free (Agent/Skill)<br/>- seo-backlinks (Agent)<br/>- competitor-analysis (Skill)<br/>- content-gap-analysis (Skill)<br/>- serp-analysis (Skill)"]
    SEO --> SEO_Advanced["Advanced & Local:<br/>- seo-geo (Agent)<br/>- seo-local (Agent)<br/>- seo-maps (Agent)<br/>- seo-programmatic (Agent)<br/>- seo-ecommerce (Agent)<br/>- seo-drift (Agent)"]
  end

  subgraph BlogSubsystem ["Blog Subsystem (30 Sub-skills & 5 Agents)"]
    Blog --> Blog_Plan["Planning & Strategy:<br/>- blog-strategy (Skill)<br/>- blog-calendar (Skill)<br/>- blog-cluster (Skill)<br/>- blog-discourse (Skill)"]
    Blog --> Blog_Create["Content Creation:<br/>- blog-brief (Skill)<br/>- blog-outline (Skill)<br/>- blog-write (Agent/Skill)<br/>- blog-rewrite (Skill)"]
    Blog --> Blog_Opt["Optimization & QA:<br/>- blog-seo-check (Skill)<br/>- blog-schema (Skill)<br/>- blog-factcheck (Skill)<br/>- blog-geo (Skill)"]
    Blog --> Blog_Assets["Media & Localization:<br/>- blog-chart (SVG Visuals)<br/>- blog-image (Gemini Gen)<br/>- blog-audio (TTS Narration)<br/>- blog-multilingual (Skill)<br/>- blog-translate (Agent)<br/>- blog-localize (Skill)"]
  end

  subgraph ToolsLayer ["MCP Servers & Data Layer"]
    SEO_Audits -.-> MCP_Gate["mcp_config.json"]
    SEO_Intel -.-> MCP_Gate
    SEO_Advanced -.-> MCP_Gate
    Blog_Create -.-> MCP_Gate
    Blog_Assets -.-> MCP_Gate
    
    MCP_Gate --> MCP_Trends["google-trends (Pytrends)"]
    MCP_Gate --> MCP_Ads["google-ads-research"]
    MCP_Gate --> MCP_Planner["google-keyword-planner"]
    MCP_Gate --> MCP_DFS["dataforseo"]
    MCP_Gate --> MCP_Crawl["firecrawl"]
    MCP_Gate --> MCP_Screen["nanobanana"]
  end
  
  Cache -.->|"Read/Write Context"| SEOSubsystem
  Cache -.->|"Read/Write Context"| BlogSubsystem

  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.2px
  classDef supervisor fill:#1b1525,stroke:#a78bfa,color:#fff7ed,stroke-width:2px
  classDef cache fill:#0c2220,stroke:#22c55e,color:#ecfeff,stroke-width:1.5px
  classDef mcp fill:#1a1a0c,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.5px
  
  class Run supervisor
  class Cache cache
  class MCP_Trends,MCP_Ads,MCP_Planner,MCP_DFS,MCP_Crawl,MCP_Screen mcp
```

### The Three Core Engines:
1. **SEO Router (`skills/seo/SKILL.md`)**:
   * Coordinates 29 sub-skills and 27 agent profiles. Performs single-page or site-wide analysis including Core Web Vitals (INP-focused), schema verification, authority audits, competitor gap analyses, and local map-pack checks.
2. **Blog Router (`skills/blog/SKILL.md`)**:
   * Coordinates 30 sub-skills, 12 content templates, and 5 specialized agents. Handles editorial calendars, outlines, EEAT assessments, translation/localization, and article drafts.
3. **Master Supervisor (`/seo:run`)**:
   * The top-level coordinator that bridges the SEO and Blog repositories. It reads multi-step prompts (e.g., *"Find trends and write a draft"*), plans the roadmap, verifies cache validation (Fix 3), evaluates outputs via a lightweight check (Fix 2), and executes loop logic safely (cap: 5 iterations).

---

## 2. Command Namespace Reference

All capabilities are exposed via the `/seo:` namespace to keep prompts simple and structured:

| Command | Arguments | Purpose / Workflow |
|---|---|---|
| `/seo:run` | `<complex-goal> [--max-steps <int>] [--force-fresh]` | **Master Supervisor**: Bridges SEO and Blog systems. Generates an Execution Roadmap, runs structural reviews, checks cache TTL, and halts on safety limits. |
| `/seo:auto` | `<goal> [--deep]` | **Intent Inference**: Runs local routing to check standard SEO scenario families (Audit, Research, Write, Track) and triggers standard gates. |
| `/seo:research`| `<domain-or-topic> [--competitors <domains>] [--map]` | **Market Intel**: Identifies search queries, competitor ratings, SERP intent, content gaps, and semantic architectures. |
| `/seo:audit` | `<target> [--full] [--tech\|--visibility\|--authority]` | **Deep Audit**: Analyzes Core Web Vitals, Schema.org health, E-E-A-T score, and AI visibility (GEO) rankings. |
| `/seo:create` | `<keyword> [--brief\|--series\|--refresh\|--meta\|--schema]` | **Content Engine**: Generates briefs, writes posts, applies HTML schema structures, and designs meta tags. |
| `/seo:track` | `<url> [--alert\|--report\|--remember]` | **Metrics Tracking**: Monitors SERP shifts, alerts on performance baseline drifts, and updates campaign memories. |

---

## 3. Visual Charts Engine (`blog-chart`)

The suite features a built-in SVG Data Visualization Engine (`skills/blog-chart`) that automatically designs dark-mode-compatible inline charts for blog posts and audit reports.

### Supported Visualization Types:
* **Horizontal Bar Chart**: Percentage changes and direct factor comparisons.
* **Grouped Bar Chart**: Before/after comparisons and dual-series metrics.
* **Donut Chart**: Share of voice, market share, and parts-of-a-whole.
* **Line Chart**: Keyword popularity and search trend lines over time.
* **Lollipop Chart**: Ranked opportunities and correlation values.
* **Area Chart**: Cumulative data distributions and ranges.
* **Radar Chart**: Multi-dimensional parameter scores (e.g. Core E-E-A-T categories).

### Strict Styling Constraints:
To ensure accessibility and contrast compatibility across both dark and light reader modes, the visual charts conform to the following strict rules:
1. **Background**: Always transparent (no root SVG fill).
2. **Colors**: Approved color palette tokens only:
   * 🟠 Primary: `#f97316` (Orange)
   * 🔵 Secondary: `#38bdf8` (Sky Blue)
   * 🟣 Tertiary: `#a78bfa` (Purple)
   * 🟢 Indicator: `#22c55e` (Green)
3. **Accessibility**: All charts output accessible markup using `role="img"`, descriptive `aria-label`, `<title>`, and `<desc>` fields, and attribute sources at the bottom center.
4. **CurrentColor**: Text, grid lines, and labels use `currentColor` to dynamically adapt to the user's theme.

---

## 4. Shared Data Cache (`.seo-cache/`)

The `.seo-cache/` folder functions as the local memory of your assistant, avoiding repetitive paid API requests and token wastage.

### Key Naming Convention:
All cached files are structured as follows:
```text
{domain-or-topic-slug}__{task-type}__{YYYY-MM-DD}.json
```
* *Example*: `forexguru-pk__dr__2026-06-19.json` (Stores competitor Domain Rating)
* *Example*: `forex-trading-signals__trends__2026-06-19.json` (Stores Google Trends)

### 7-Day TTL Staleness Rule:
* Before running any keyword or authority fetch, the Supervisor checks if a cache key exists for the target.
* If a file exists and is **less than 7 days old**, the Supervisor reuses the cached file to save API quotas and token volume.
* You can bypass this check and force a fresh run by passing the `--force-fresh` flag (e.g. `/seo:run "..." --force-fresh`).

---

## 5. MCP Configurations and Setup

To enrich audits with real-world live data, configure your extensions inside `mcp_config.json`. The following 7 servers are natively supported:

| MCP Server Name | Source / Command | Purpose | Required Env Variables |
|---|---|---|---|
| `google-trends` | `python` (Local Clone: `GoogleTrendsMCP`) | Free historical and regional search trend metrics without API keys. | *None* |
| `google-ads-research` | `npx -y google-ads-mcp` | Fast Google autocomplete suggest phrases and lightweight trend indexes. | *None* |
| `google-keyword-planner` | `npx -y google-keyword-planner-mcp` | Search volume, advertiser competition levels, and average CPC. | `GOOGLE_ADS_DEVELOPER_TOKEN`, `GOOGLE_ADS_CLIENT_ID`, `GOOGLE_ADS_CLIENT_SECRET`, `GOOGLE_ADS_REFRESH_TOKEN`, `GOOGLE_ADS_LOGIN_CUSTOMER_ID` |
| `dataforseo` | `npx -y dataforseo-mcp-server` | Professional live SERPs, organic difficulty scores, and merchant product indexes. | `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD` |
| `firecrawl` | `npx -y firecrawl-mcp-server` | Site-wide JS-rendered crawling and automated XML sitemap mappings. | `FIRECRAWL_API_KEY` |
| `nanobanana` | `npx -y nanobanana-mcp` | Capturing above-the-fold visual layouts, mobile testing, and screenshot analysis. | `GOOGLE_AI_API_KEY` |

### Setting Up Local Google Trends MCP:
```bash
# 1. Clone the repository
git clone https://github.com/cryptoken/GoogleTrendsMCP.git G:\skills\GoogleTrendsMCP

# 2. Create virtual environment
cd G:\skills\GoogleTrendsMCP
python -m venv venv

# 3. Install requirements
venv\Scripts\pip install -r requirements.txt
```
The workspace `mcp_config.json` is pre-configured to execute this server via your local clone.

---

## 6. Premium Reports & PDFs

When executing audits or visual analysis, you can generate client-ready PDF deliverables containing Lighthouse graphs, Core Web Vitals gauges, and visual checklist charts:

1. Execute the audit:
   ```bash
   /seo:audit https://example.com --full
   ```
2. Request a premium document:
   ```text
   Generate a client-ready report for this run
   ```
   *The system invokes `scripts/google_report.py` and creates a styled HTML baseline report, compiles the visual SVG charts, and compiles the final PDF deliverable under the `pdf/` or `output/` directory.*

---

## 7. Development & Verification

### Initializing the Plugin:
To link and register this suite inside the Antigravity ecosystem:
```bash
# Register the local directory as an active plugin
agy plugin install /path/to/antigravity-seo
```

### Validation Check:
Always run the validation tool after editing skills or agent profiles to verify schema compliance:
```bash
agy plugin validate /path/to/antigravity-seo
```

### Authorship Rules (Workspace Compliance):
All contributions, wrappers, configurations, and document edits MUST obey the Personal Ownership Mapping rules:
* **Owner/Author**: `dotusmanali`
* **Email**: `dotusmanali@gmail.com`
* **Repository**: `https://github.com/dotusmanali/antigravity-seo`
* **Command Namespace**: Explicitly scoped inside the `/seo:` namespace.
