# Installation

## One-Line Install

### Unix

```bash
curl -fsSL https://raw.githubusercontent.com/Muhammad Usman Ali/antigravity-seo/v1.9.6-antigravity.5/install.sh | bash
```

### Windows

```powershell
irm https://raw.githubusercontent.com/Muhammad Usman Ali/antigravity-seo/v1.9.6-antigravity.5/install.ps1 | iex
```

## Manual Install From Local Checkout

```bash
git clone https://github.com/dotusmanali/antigravity-seo.git
cd antigravity-seo
bash install.sh
```

Windows:

```powershell
git clone https://github.com/dotusmanali/antigravity-seo.git
cd antigravity-seo
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

## What Gets Installed

- `~/.gemini/skills/seo`
- `~/.gemini/skills/seo-*`
- `~/.gemini/agents/seo-*.toml`
- Python runtime at `~/.gemini/skills/seo/.venv`
- Core Python dependencies, with optional visual/report/Google/OCR groups attempted best-effort

## Overrides

- `GEMINI_HOME`: alternate Antigravity home
- `GEMINI_SEO_REPO`: fork or local Git path
- `GEMINI_SEO_REF`: branch, tag, or commit; defaults to `v1.9.6-antigravity.5`
- `GEMINI_SEO_SKIP_PLAYWRIGHT_BROWSER=1`: skip Chromium install
- `GEMINI_SEO_PLAYWRIGHT_WITH_DEPS=1`: install Playwright system deps where supported

## Verify

```bash
~/.gemini/skills/seo/.venv/bin/python ~/.gemini/skills/seo/scripts/verify_environment.py
```

Windows:

```powershell
& "$HOME\.gemini\skills\seo\.venv\Scripts\python.exe" "$HOME\.gemini\skills\seo\scripts\verify_environment.py"
```

## Uninstall

```bash
bash uninstall.sh
```

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
