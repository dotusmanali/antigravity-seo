#!/usr/bin/env bash
set -euo pipefail

echo "Removing Firecrawl extension..."

ANTIGRAVITY_ROOT="${GEMINI_HOME:-${HOME}/.gemini}"
SKILLS_ROOT="${ANTIGRAVITY_ROOT}/skills"
AGENT_DIR="${ANTIGRAVITY_ROOT}/agents"
SETTINGS_FILE="${ANTIGRAVITY_ROOT}/settings.json"

# Remove skill directory
rm -rf "${SKILLS_ROOT}/seo-firecrawl"
echo "v Removed skill files"

rm -f "${AGENT_DIR}/seo-firecrawl.toml"
echo "v Removed agent profile"

# Remove MCP entry from settings.json
if [ -f "${SETTINGS_FILE}" ]; then
    python3 -c "
import json, os

settings_path = '${SETTINGS_FILE}'
with open(settings_path, 'r') as f:
    settings = json.load(f)

if 'mcpServers' in settings and 'firecrawl-mcp' in settings['mcpServers']:
    del settings['mcpServers']['firecrawl-mcp']
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print('v Removed MCP server from settings.json')
else:
    print('  MCP server not found in settings.json (already removed)')
" || echo "  Warning: Could not update settings.json automatically."
fi

echo ""
echo "v Firecrawl extension uninstalled."
echo "  Core Antigravity SEO skills are unchanged."
