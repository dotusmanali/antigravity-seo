# Firecrawl Extension Uninstaller for Antigravity SEO (Windows)
$ErrorActionPreference = 'Stop'

Write-Host "Removing Firecrawl extension..." -ForegroundColor Yellow

$AntigravityRoot = if ($env:GEMINI_HOME) { $env:GEMINI_HOME } else { Join-Path $HOME ".gemini" }
$SkillsRoot = Join-Path $AntigravityRoot "skills"
$AgentDir = Join-Path $AntigravityRoot "agents"
$SkillDir = Join-Path $SkillsRoot "seo-firecrawl"
$SettingsFile = Join-Path $AntigravityRoot "settings.json"

if (Test-Path $SkillDir) {
    Remove-Item -Recurse -Force $SkillDir
    Write-Host "v Removed skill files" -ForegroundColor Green
}

$AgentFile = Join-Path $AgentDir "seo-firecrawl.toml"
if (Test-Path $AgentFile) {
    Remove-Item -Force $AgentFile
    Write-Host "v Removed agent profile" -ForegroundColor Green
}

if (Test-Path $SettingsFile) {
    $settings = Get-Content $SettingsFile -Raw | ConvertFrom-Json
    if (($settings.PSObject.Properties.Name -contains "mcpServers") -and ($settings.mcpServers.PSObject.Properties.Name -contains "firecrawl-mcp")) {
        $settings.mcpServers.PSObject.Properties.Remove('firecrawl-mcp')
        $settings | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile -Encoding UTF8
        Write-Host "v Removed MCP server from settings.json" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "v Firecrawl extension uninstalled." -ForegroundColor Green
Write-Host "  Core Antigravity SEO skills are unchanged."
