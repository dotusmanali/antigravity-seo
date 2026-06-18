# Ecosystem Conventions

These conventions apply to the entire Antigravity SEO & Blog ecosystem.

## Directory Structure

- `skills/` — Auto-discovered skill definitions (each has `SKILL.md`)
- `agents/` — Auto-discovered subagent templates (TOML format)
- `rules/` — Global behavioral rules (this directory)
- `scripts/` — Python backend scripts, referenced as `${ANTIGRAVITY_PLUGIN_ROOT}/scripts/`
- `hooks/` — Hook script files (validate-schema.py, pre-commit-seo-check.sh)
- `schema/` — Schema.org JSON-LD templates
- `docs/` — Documentation and command guides
- `tests/` — pytest test suite
- `pdf/` — PDF templates
- `output/` — Generated reports (gitignored)
- `.seo-cache/` — Cross-skill shared cache (gitignored)

## Script Path References

- Always use `${ANTIGRAVITY_PLUGIN_ROOT}/scripts/` for script paths in SKILL.md files
- Never use hardcoded home-directory paths (`~/.gemini/skills/`, `$HOME/.antigravity/`)
- Scripts resolve relative to the plugin root directory

## Cache & Output

- Cache artifacts: `.seo-cache/` at the active project root (gitignored)
- Output artifacts: `output/` at the plugin root (gitignored)
- Never commit cache, output, OAuth tokens, service accounts, or API keys

## Credentials

- Stored at `~/.config/antigravity-seo/` — never in the repository
- MCP server env vars defined in `mcp_config.json` at plugin root
- Google API credentials: `python scripts/google_auth.py --setup`

## Naming Conventions

- Skill directories: kebab-case (`seo-technical`, `blog-write`)
- Agent files: kebab-case with `.toml` extension (`seo-backlinks.toml`)
- Python scripts: snake_case (`analyze_blog.py`)
- Rule files: kebab-case with `.md` extension (`seo-quality-gates.md`)

## Development Rules

- SKILL.md files: under 500 lines / 5000 tokens
- Reference files: focused and under 200 lines (comprehensive refs exempt)
- Scripts: must have docstrings, CLI interface, and JSON output
- Agents: invoked via Task tool, never via Bash
- Python 3.10+ required
- Test with `python -m pytest tests/` after changes

## MCP Integration

- MCP servers configured centrally in `mcp_config.json` at plugin root
- If MCP server or credentials are missing, scripts return `setup_required` status
- Never fabricate live data when API is unavailable
