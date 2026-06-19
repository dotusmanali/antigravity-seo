<p align="center">
  <img src="screenshots/cover-image.svg" alt="Antigravity SEO: SEO audit skill suite for Antigravity" width="100%">
</p>

# Antigravity SEO & Blog Suite — Complete SEO & Content Ecosystem for Antigravity

A complete, production-grade SEO analysis and blog creation ecosystem built for **Antigravity** (IDE, CLI, 2.0). Features 2 orchestrators, 60 specialist workflows, 32 AI agent profiles, 3 global rules, MCP integrations, shared cache artifacts, and deterministic headless runners.

[![GitHub license](https://img.shields.io/github/license/dotusmanali/antigravity-seo?style=flat-square&color=blue)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/dotusmanali/antigravity-seo?style=flat-square&color=orange)](https://github.com/dotusmanali/antigravity-seo/releases)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](pyproject.toml)
[![SEO Workflows](https://img.shields.io/badge/Workflows-60-emerald?style=flat-square)](docs/COMMANDS.md)
[![AI Agents](https://img.shields.io/badge/AI_Agents-32-blueviolet?style=flat-square)](agents/)

## Contents

- [Status](#status)
- [Install](#install)
- [Quick Start](#quick-start)
- [Visual Overview](#visual-overview)
- [Commands](#commands)
- [Features](#features)
- [Extensions](#extensions)
- [Headless/API Usage](#headlessapi-usage)
- [Architecture](#architecture)
- [Verification](#verification)
- [Requirements](#requirements)
- [Credentials And Cache](#credentials-and-cache)
- [Security](#security)
- [Uninstall](#uninstall)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [Credits](#credits)
- [Attribution](#attribution)

## Status

- Repository visibility: public.
- Current release: [`v1.9.6-antigravity.5`](https://github.com/dotusmanali/antigravity-seo/releases/tag/v1.9.6-antigravity.5).
- Installer default ref: `v1.9.6-antigravity.5`.
- Latest local validation: 52 tests passing, full installed smoke suite passing, demo readiness passing.
- Runtime credentials stay outside the repo under Antigravity/local config paths.
- Discovery topics: `antigravity`, `antigravity-cli`, `antigravity-skills`, `seo`, `ai-seo`, `ai-search`, `technical-seo`, `generative-engine-optimization`, `core-web-vitals`, `schema-markup`, `local-seo`, `ecommerce-seo`, `content-strategy`, `google-search-console`, `dataforseo`, `mcp`, `python`, `automation`, `marketing-automation`, `open-source`.

## Install

### Option 1: Via Antigravity CLI

```bash
agy plugin install /path/to/antigravity-seo
```

### Option 2: Manual Copy

```bash
# 1. Clone the repository
git clone https://github.com/dotusmanali/antigravity-seo.git

# 2. Link as plugin
# Linux/macOS
ln -s /path/to/antigravity-seo ~/.gemini/config/plugins/antigravity-seo

# Windows (PowerShell as Admin)
New-Item -ItemType Junction -Path "$env:USERPROFILE\.gemini\config\plugins\antigravity-seo" -Target "C:\path\to\antigravity-seo"
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

Restart Antigravity. All 60 skills and 32 agents are auto-discovered.

## Quick Start

Restart Antigravity after installation. Then ask naturally; a `/seo` command is not required:

```text
Do a full SEO check on https://example.com following best practices.
```

```text
Review this page for schema, Core Web Vitals, image SEO, and AI search readiness.
```

```text
Create an SEO strategy and content roadmap for a local dental clinic.
```

Command-style prompts also work:

```text
/seo audit https://example.com
/seo technical https://example.com
/seo schema https://example.com
/seo dataforseo serp "best seo tools"
```

## Visual Overview

Antigravity SEO is designed as a Antigravity-first routing layer: the user can ask naturally, the orchestrator selects the right specialist workflow, and deterministic runners write repeatable artifacts instead of relying on invisible chat-only output.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
  user["User prompt<br/>natural language or /seo"] --> orchestrator["skills/seo/SKILL.md<br/>main orchestrator"]
  orchestrator --> cache[".seo-cache<br/>shared evidence"]
  orchestrator --> skills["29 specialist<br/>SEO workflows"]
  skills --> agents["27 TOML agents<br/>parallel analysis slices"]
  skills --> scripts["scripts/<br/>deterministic runners"]
  scripts --> output["output/<br/>Markdown, JSON, HTML, PDF"]
  cache --> skills
  class user,orchestrator accent
  class cache,scripts data
  class output output
  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.4px
  classDef accent fill:#10151a,stroke:#ff9f1c,color:#fff7ed,stroke-width:2px
  classDef data fill:#06222a,stroke:#21e6c1,color:#ecfeff,stroke-width:1.5px
  classDef output fill:#15101a,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.8px
```

## Commands

The ecosystem features five one-shot mode commands under the **`/seo:`** namespace to orchestrate specific SEO and GEO intents:

| Command | Arguments | Purpose |
|---|---|---|
| `/seo:auto` | `<goal> [--deep]` | Infer SEO/GEO intent and run the smallest useful workflow. Add `--deep` for exhaustive, phase-gated execution. |
| `/seo:research` | `<domain-or-keyword>` | Analyze keyword demand, SERP intent, competitors, content gaps, and entity maps. |
| `/seo:create` | `<keyword> [--brief\|--series\|--refresh\|--publish\|--meta\|--schema]` | Generate content briefs, write/refresh posts, create series, and export CMS-neutral publish packages. |
| `/seo:audit` | `<target> [--full] [--tech\|--visibility\|--authority]` | Evaluate page SEO + CORE-EEAT quality, technical health (`--tech`), AI citation readiness (`--visibility`), and domain trust (`--authority`). |
| `/seo:track` | `<url> [--alert\|--report\|--remember]` | Track rank positions, trigger alerts (`--alert`), generate reports (`--report`), and update campaign memory (`--remember`). |

For individual workflow details and instructions, check the files directly under the `skills/` directory.

## Features

### Full Audit Pipeline

- Detects site/business type.
- Runs technical, content, schema, sitemap, performance, visual, GEO, image, and on-page analysis.
- Adds conditional specialists for local, maps, Google APIs, backlinks, clusters, SXO, drift, and e-commerce.
- Writes markdown reports, JSON summaries, cache artifacts, and optional premium HTML/PDF output.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TD
  request["Audit request"] --> detect["Detect site type<br/>business model and context"]
  detect --> core["Core audit specialists"]
  core --> technical["Technical"]
  core --> content["Content"]
  core --> schema["Schema"]
  core --> sitemap["Sitemap"]
  core --> geo["GEO / AI search"]
  core --> images["Images"]
  core --> performance["Performance"]
  core --> visual["Visual"]
  detect --> conditional["Conditional specialists"]
  conditional --> local["Local / Maps"]
  conditional --> backlinks["Backlinks"]
  conditional --> google["Google APIs"]
  conditional --> ecommerce["E-commerce"]
  conditional --> drift["Drift"]
  technical --> report["Unified SEO report"]
  content --> report
  schema --> report
  sitemap --> report
  geo --> report
  images --> report
  performance --> report
  visual --> report
  local --> report
  backlinks --> report
  google --> report
  ecommerce --> report
  drift --> report
  report --> artifacts["SUMMARY.json<br/>FULL-AUDIT-REPORT.md<br/>ACTION-PLAN.md<br/>optional HTML/PDF"]
  class request,detect accent
  class core,conditional data
  class report,artifacts output
  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.4px
  classDef accent fill:#10151a,stroke:#ff9f1c,color:#fff7ed,stroke-width:2px
  classDef data fill:#06222a,stroke:#21e6c1,color:#ecfeff,stroke-width:1.5px
  classDef output fill:#15101a,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.8px
```

### Technical SEO

- Robots.txt, sitemap discovery, canonical checks, indexability, URL hygiene.
- Security headers, JavaScript rendering risk, mobile basics, IndexNow.
- Core Web Vitals with INP, LCP, CLS, FCP, TTFB, and PageSpeed/CrUX integrations where available.

### Content, GEO, And SXO

- E-E-A-T and helpful content signals.
- AI citation readiness, answer-first formatting, entity clarity, llms.txt support.
- Search experience analysis: page type, user stories, persona fit, intent mismatch.

### Structured Data

- JSON-LD extraction and validation.
- Schema recommendations for Organization, LocalBusiness, Product, Article, FAQ, Breadcrumb, and related types.
- Generated schema artifacts for downstream use.

### Local, Maps, And E-Commerce SEO

- Local SEO signals, GBP readiness, citations, reviews, NAP consistency.
- Maps intelligence via free sources and DataForSEO when configured.
- Product schema, marketplace endpoints, merchant visibility, and e-commerce template checks.

### Drift Monitoring

- Capture SEO-critical baselines.
- Compare deployments or page changes.
- Track title, meta, headings, canonical, schema, robots, links, and content deltas.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","actorBkg":"#07131c","actorBorder":"#00d7e6","actorTextColor":"#f5fbff","actorLineColor":"#21e6c1","signalColor":"#21e6c1","signalTextColor":"#f5fbff","labelBoxBkgColor":"#10151a","labelTextColor":"#f5fbff","noteBkgColor":"#10151a","noteTextColor":"#f5fbff","activationBkgColor":"#06222a","activationBorderColor":"#ff9f1c","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
sequenceDiagram
  participant Before as Baseline
  participant Runner as Drift runner
  participant After as Current page
  participant Cache as .seo-cache
  participant Report as Drift report
  Before->>Runner: Capture titles, metas, canonicals, schema, headings
  Runner->>Cache: Store baseline snapshot
  After->>Runner: Re-check current SEO signals
  Cache->>Runner: Load prior snapshot
  Runner->>Report: Write changed, missing, and regressed signals
```

### Deterministic Runners

- `scripts/run_skill_workflow.py` standardizes output for every user-invokable workflow.
- `scripts/run_api_smoke_suite.py` runs all supported workflows in one pass.
- Setup-required workflows return structured fallback results instead of pretending live data exists.

## Extensions

| Extension | Skill | Setup | Notes |
|---|---|---|---|
| DataForSEO | `seo-dataforseo`, `seo-maps`, `seo-ecommerce`, `seo-cluster` | Set `DATAFORSEO_LOGIN`/`DATAFORSEO_PASSWORD` env vars (configured in `mcp_config.json`) | Live SERP, keyword, backlinks, on-page, content, business data, AI visibility |
| Google APIs | `seo-google`, `seo-performance` | `python scripts/google_auth.py --setup` | PageSpeed, CrUX, GSC, URL Inspection, Indexing API, GA4 |
| Firecrawl | `seo-firecrawl` | Set `FIRECRAWL_API_KEY` env var (configured in `mcp_config.json`) | JS-rendered crawl, scrape, site map |
| Banana / Gemini | `seo-image-gen` | Set `GOOGLE_AI_API_KEY` env var (configured in `mcp_config.json`) | AI image generation through `nanobanana-mcp` |

Optional integrations enrich the same workflow surface. If credentials or MCP servers are missing, wrappers return `setup_required` or `mcp_configured` states with no fabricated live data.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
  antigravity["Antigravity SEO workflows"] --> local["Local evidence<br/>HTML, robots, sitemaps, screenshots"]
  antigravity --> dfs["DataForSEO MCP<br/>SERP, keywords, backlinks, maps"]
  antigravity --> google["Google APIs<br/>GSC, PageSpeed, CrUX, GA4"]
  antigravity --> firecrawl["Firecrawl MCP<br/>JS crawl and site maps"]
  antigravity --> banana["Gemini / nanobanana<br/>SEO image assets"]
  local --> artifacts["Reports and .seo-cache"]
  dfs --> artifacts
  google --> artifacts
  firecrawl --> artifacts
  banana --> artifacts
  class antigravity accent
  class local,dfs,google,firecrawl,banana data
  class artifacts output
  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.4px
  classDef accent fill:#10151a,stroke:#ff9f1c,color:#fff7ed,stroke-width:2px
  classDef data fill:#06222a,stroke:#21e6c1,color:#ecfeff,stroke-width:1.5px
  classDef output fill:#15101a,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.8px
```

Demo readiness:

```bash
python scripts/demo_readiness.py --target https://example.com --live-apis --workflows --json
```

One low-depth DataForSEO proof:

```bash
python scripts/demo_readiness.py --target https://example.com --live-apis --live-serp --serp-keyword "seo tools" --json
```

## Headless/API Usage

Run a single workflow:

```bash
python scripts/run_skill_workflow.py --skill seo-technical https://example.com --json
python scripts/run_skill_workflow.py --skill seo-google https://example.com --json
python scripts/run_skill_workflow.py --skill seo-dataforseo https://example.com --json
```

Run the full smoke suite:

```bash
python scripts/run_api_smoke_suite.py https://example.com --json
```

Verify environment:

```bash
python scripts/verify_environment.py --target https://example.com --json
```

Bootstrap a clean runtime:

```bash
python scripts/bootstrap_environment.py --venv .venv --json
```

Artifacts are written to `output/`. Shared project cache is written to `.seo-cache/`. Both are ignored by git.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart LR
  cli["run_skill_workflow.py<br/>single workflow"] --> json["JSON result"]
  cli --> markdown["Markdown report"]
  cli --> cacheWrite[".seo-cache update"]
  suite["run_api_smoke_suite.py<br/>all workflows"] --> json
  suite --> outputRoot["output/api-smoke-*"]
  verify["verify_environment.py"] --> readiness["ready / setup_required<br/>capability status"]
  markdown --> outputRoot
  json --> outputRoot
  cacheWrite --> cache[".seo-cache"]
  class cli,suite,verify accent
  class cacheWrite,readiness data
  class json,markdown,outputRoot,cache output
  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.4px
  classDef accent fill:#10151a,stroke:#ff9f1c,color:#fff7ed,stroke-width:2px
  classDef data fill:#06222a,stroke:#21e6c1,color:#ecfeff,stroke-width:1.5px
  classDef output fill:#15101a,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.8px
```

## Architecture

The repository separates Antigravity-facing instructions, deterministic runtime code, optional provider setup, and validation contracts. That keeps the skill system usable in chat, installable as a suite, and testable from CI/API workflows.

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#05080d","primaryColor":"#07131c","primaryTextColor":"#f5fbff","primaryBorderColor":"#00d7e6","lineColor":"#00d7e6","secondaryColor":"#06222a","tertiaryColor":"#ff9f1c","edgeLabelBackground":"#05080d","fontFamily":"Inter, ui-sans-serif, system-ui, sans-serif"}}}%%
flowchart TB
  manifest["plugin.json"] --> skillsRoot["skills/"]
  skillsRoot --> orchestrator["seo/SKILL.md<br/>routing and orchestration"]
  skillsRoot --> specialists["seo-*/SKILL.md<br/>specialist workflows"]
  agentsDir["agents/seo-*.toml"] --> specialists
  scriptsDir["scripts/<br/>deterministic runners"] --> specialists
  mcpConfig["mcp_config.json<br/>MCP servers"] --> specialists
  references["skills/seo/references/<br/>thresholds and shared contracts"] --> specialists
  specialists --> cacheDir[".seo-cache/<br/>cross-skill memory"]
  specialists --> outputDir["output/<br/>reports and artifacts"]
  rulesDir["rules/<br/>global behavioral rules"] --> manifest
  testsDir["tests/<br/>contract and smoke coverage"] --> manifest
  testsDir --> skillsRoot
  testsDir --> scriptsDir
  class manifest,orchestrator accent
  class skillsRoot,specialists,agentsDir,scriptsDir,mcpConfig,references,testsDir,rulesDir data
  class cacheDir,outputDir output
  classDef default fill:#07131c,stroke:#00d7e6,color:#f5fbff,stroke-width:1.4px
  classDef accent fill:#10151a,stroke:#ff9f1c,color:#fff7ed,stroke-width:2px
  classDef data fill:#06222a,stroke:#21e6c1,color:#ecfeff,stroke-width:1.5px
  classDef output fill:#15101a,stroke:#ff9f1c,color:#fff7ed,stroke-width:1.8px
```

```text
antigravity-seo/
├── plugin.json                       # Antigravity plugin manifest
├── hooks.json                        # Event hooks (PostToolUse)
├── mcp_config.json                   # MCP server definitions
├── requirements.txt                  # Python dependencies
├── pyproject.toml                    # Python project configuration
├── skills/
│   ├── seo/SKILL.md                  # SEO orchestrator
│   ├── blog/SKILL.md                 # Blog orchestrator
│   ├── references/                   # Shared contracts and frameworks
│   ├── memory/                       # Local campaign memory and caches
│   └── ...                           # 75+ flat auto-discovered skills
├── agents/                           # 29 Antigravity TOML agent profiles
├── rules/                            # Global behavioral rules
├── scripts/                          # Python backend engines and connectors
├── hooks/                            # Hook script files
└── schema/                           # Schema.org templates
```

Design principles:

- `skills/` is the source of truth.
- `skills/seo/SKILL.md` routes natural-language SEO requests.
- TOML agents are Antigravity-native and mirror specialist workflows.
- Runtime credentials stay in `~/.config/antigravity-seo/` or `~/.gemini/settings.json`.
- Legacy `antigravity-seo` config/cache paths are read only as migration fallback.

More detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Verification

Local release gate:

```bash
python -m pytest tests/
python -m compileall -q scripts hooks
python scripts/run_api_smoke_suite.py https://example.com --json
```

PowerShell parse check:

```powershell
$files = Get-ChildItem -Recurse -Filter *.ps1
foreach ($f in $files) {
  $tokens = $null
  $errs = $null
  [System.Management.Automation.Language.Parser]::ParseFile($f.FullName, [ref]$tokens, [ref]$errs) > $null
  if ($errs.Count) { $errs; exit 1 }
}
```

Current GitHub CI runs:

- dependency install
- shell syntax checks
- Python compile checks
- `--help` checks for runner scripts
- `python -m pytest tests/`
- contract smoke checks for MCP-aware workflows

## Requirements

- Antigravity CLI with local skills support
- Python 3.10+
- Git
- Optional: Playwright Chromium for screenshots and PDF reports
- Optional: DataForSEO account for live SEO data
- Optional: Google API credentials for PageSpeed/CrUX/GSC/GA4
- Optional: Firecrawl API key for JS-rendered crawling
- Optional: Google AI API key for Gemini/nanobanana image generation

## Credentials And Cache

To secure your API keys and credentials, Antigravity SEO separates secret keys (environment variables) from dynamic credentials (isolated files). **Never commit secret keys, credentials files, `.env` files, or OAuth tokens to git.**

### 1. Environment Variables (Secret Keys)
Use environment variables to inject API keys for MCP servers (defined in `mcp_config.json`). 

- **`DATAFORSEO_LOGIN` & `DATAFORSEO_PASSWORD`**: Required for live SERP, keywords, backlinks, and local maps.
- **`FIRECRAWL_API_KEY`**: Required for JS-rendered crawling and sitemap parsing.
- **`GOOGLE_AI_API_KEY`**: Required for AI image generation (`nanobanana-mcp`).

#### Windows (PowerShell - Run once to set globally)
```powershell
[System.Environment]::SetEnvironmentVariable('FIRECRAWL_API_KEY', 'your_key_here', 'User')
[System.Environment]::SetEnvironmentVariable('DATAFORSEO_LOGIN', 'your_login_here', 'User')
[System.Environment]::SetEnvironmentVariable('DATAFORSEO_PASSWORD', 'your_password_here', 'User')
[System.Environment]::SetEnvironmentVariable('GOOGLE_AI_API_KEY', 'your_gemini_key_here', 'User')
```

#### macOS / Linux (Add to `~/.zshrc` or `~/.bashrc`)
```bash
export FIRECRAWL_API_KEY="your_key_here"
export DATAFORSEO_LOGIN="your_login_here"
export DATAFORSEO_PASSWORD="your_password_here"
export GOOGLE_AI_API_KEY="your_gemini_key_here"
```

*Note: Restart your terminal/IDE after setting these variables so they are successfully loaded.*

### 2. File-Based Credentials (Google APIs & Backlinks)
JSON configs and authentication credentials must be stored under your global user profile directory to keep them completely isolated from your project repositories.

- **Google Search Console, Indexing, GA4, PageSpeed**: Run the setup script to link your Google Cloud project and generate authentication tokens:
  ```bash
  python scripts/google_auth.py --setup
  ```
  This automatically saves files to `~/.config/antigravity-seo/google-api.json`.
- **Backlinks API (DataForSEO client fallback)**: Create `~/.config/antigravity-seo/backlinks-api.json` manually with the following shape:
  ```json
  {
    "login": "your_username",
    "password": "your_password"
  }
  ```

### 3. Caching & Directory Structure
- **Global Config Folder**: `~/.config/antigravity-seo/` (stores API configs, auth tokens, and cost ledgers).
- **Global Cache Folder**: `~/.cache/antigravity-seo/` (stores API responses and local cache artifacts).
- **Workspace Cache**: `.seo-cache/` is created inside the active project root for cross-skill metrics sharing (already gitignored).
- **Workspace Output**: `output/` is created inside the active project root for generated reports (already gitignored).

## Security

- URL-aware scripts block private, loopback, reserved, multicast, unspecified, and metadata hosts.
- Credential setup writes outside tracked repo files.
- Sensitive local settings are expected to use `0600` file permissions.
- DataForSEO calls use cost guardrails through `scripts/dataforseo_costs.py`.
- Report vulnerabilities through [SECURITY.md](SECURITY.md).

## Uninstall

Remove the plugin directory from your Antigravity config:

```bash
# Linux/macOS
rm -rf ~/.gemini/config/plugins/antigravity-seo

# Windows (PowerShell)
Remove-Item -Recurse "$env:USERPROFILE\.gemini\config\plugins\antigravity-seo"
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for local setup and validation, [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for project standards, and [SECURITY.md](SECURITY.md) for vulnerability reporting. Agent-facing project context is also available in [llms.txt](llms.txt).

## License

Antigravity SEO is released under the [MIT License](LICENSE).
