#!/usr/bin/env bash
set -euo pipefail

main() {
    ANTIGRAVITY_ROOT="${GEMINI_HOME:-${HOME}/.gemini}"
    SKILLS_ROOT="${ANTIGRAVITY_ROOT}/skills"
    AGENT_DIR="${ANTIGRAVITY_ROOT}/agents"
    SETTINGS_FILE="${ANTIGRAVITY_ROOT}/settings.json"

    echo "→ Uninstalling DataForSEO extension..."

    # Remove skill
    rm -rf "${SKILLS_ROOT}/seo-dataforseo"

    # Remove agent
    rm -f "${AGENT_DIR}/seo-dataforseo.toml"

    # Remove field config
    rm -f "${SKILLS_ROOT}/seo/dataforseo-field-config.json"

    # Remove MCP server entry from settings.json
    if [ -f "${SETTINGS_FILE}" ]; then
        python3 -c "
import json, os
settings_path = '${SETTINGS_FILE}'
with open(settings_path, 'r') as f:
    settings = json.load(f)
if 'mcpServers' in settings and 'dataforseo' in settings['mcpServers']:
    del settings['mcpServers']['dataforseo']
    if not settings['mcpServers']:
        del settings['mcpServers']
    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    print('  ✓ Removed dataforseo from settings.json')
else:
    print('  ✓ No dataforseo entry in settings.json')
" 2>/dev/null || echo "  ⚠  Could not auto-remove MCP config. Remove 'dataforseo' from ~/.gemini/settings.json manually."
    fi

    echo "✓ DataForSEO extension uninstalled."
}

main "$@"
