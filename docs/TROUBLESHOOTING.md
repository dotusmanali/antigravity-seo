# Troubleshooting

## Skill Not Loading

Verify the canonical skill exists:

```bash
ls ~/.gemini/skills/seo/SKILL.md
ls ~/.gemini/agents/seo-technical.toml
```

Restart Antigravity after reinstalling.

## Runtime Not Ready

```bash
~/.gemini/skills/seo/.venv/bin/python ~/.gemini/skills/seo/scripts/verify_environment.py
```

If Playwright Chromium fails, core workflows can still run. Visual and PDF workflows remain limited until browser installation succeeds.

On Python 3.14 macOS, some optional packages can lag wheel support. The installer should still complete when `requirements-core.txt` installs and `core_ready` is true; use the verifier notes to identify any optional visual, Google API, report, or OCR capability that needs a different Python/runtime.

## Credentials Missing

Use Antigravity paths for new setup:

- Google: `~/.config/antigravity-seo/google-api.json`
- Backlinks: `~/.config/antigravity-seo/backlinks-api.json`
- DataForSEO budgets: `~/.config/antigravity-seo/dataforseo-costs.json`

Legacy `~/.config/antigravity-seo/` files are read as fallback only.

## Headless Workflow Fails

Run a narrow workflow first:

```bash
python scripts/run_skill_workflow.py --skill seo-technical https://example.com --json
```

For optional MCP/API workflows, `setup_required` is a valid result when credentials or MCP servers are absent.

## Reinstall

```bash
GEMINI_SEO_REPO=https://github.com/dotusmanali/antigravity-seo GEMINI_SEO_REF=v1.9.6-antigravity.5 bash install.sh
```
