# Antigravity SEO Uninstaller for Windows

$ErrorActionPreference = "Stop"

$antigravityRoot = if ($env:GEMINI_HOME) { $env:GEMINI_HOME } else { Join-Path $HOME ".gemini" }
$skillsRoot = Join-Path $antigravityRoot "skills"
$agentDir = Join-Path $antigravityRoot "agents"

$skillNames = @(
    "blog",
    "blog-analyze",
    "blog-audio",
    "blog-audit",
    "blog-brand",
    "blog-brief",
    "blog-calendar",
    "blog-cannibalization",
    "blog-chart",
    "blog-cluster",
    "blog-discourse",
    "blog-factcheck",
    "blog-flow",
    "blog-geo",
    "blog-google",
    "blog-image",
    "blog-locale-audit",
    "blog-localize",
    "blog-multilingual",
    "blog-notebooklm",
    "blog-outline",
    "blog-persona",
    "blog-repurpose",
    "blog-rewrite",
    "blog-schema",
    "blog-seo-check",
    "blog-strategy",
    "blog-taxonomy",
    "blog-translate",
    "blog-write",
    "seo",
    "seo-audit",
    "seo-backlinks",
    "seo-cluster",
    "seo-competitor-pages",
    "seo-content",
    "seo-dataforseo",
    "seo-drift",
    "seo-ecommerce",
    "seo-firecrawl",
    "seo-flow",
    "seo-geo",
    "seo-google",
    "seo-hreflang",
    "seo-image-gen",
    "seo-images",
    "seo-local",
    "seo-maps",
    "seo-page",
    "seo-performance",
    "seo-plan",
    "seo-programmatic",
    "seo-schema",
    "seo-sitemap",
    "seo-sxo",
    "seo-technical",
    "seo-visual"
)

$agentNames = @(
    "blog-researcher",
    "blog-reviewer",
    "blog-seo",
    "blog-translator",
    "blog-writer",
    "seo-backlinks",
    "seo-cluster",
    "seo-competitor-pages",
    "seo-content",
    "seo-dataforseo",
    "seo-drift",
    "seo-ecommerce",
    "seo-firecrawl",
    "seo-flow",
    "seo-geo",
    "seo-google",
    "seo-hreflang",
    "seo-image-gen",
    "seo-images",
    "seo-local",
    "seo-maps",
    "seo-performance",
    "seo-plan",
    "seo-programmatic",
    "seo-schema",
    "seo-sitemap",
    "seo-sxo",
    "seo-technical",
    "seo-visual"
)

Write-Host "[INFO] Uninstalling Antigravity SEO..." -ForegroundColor Yellow

foreach ($skill in $skillNames) {
    $path = Join-Path $skillsRoot $skill
    if (Test-Path $path) {
        Remove-Item -Path $path -Recurse -Force
    }
}

foreach ($agent in $agentNames) {
    foreach ($extension in @(".toml", ".md")) {
        $path = Join-Path $agentDir "$agent$extension"
        if (Test-Path $path) {
            Remove-Item -Path $path -Force
        }
    }
}

Write-Host "[OK] Antigravity SEO uninstalled." -ForegroundColor Green

# Scripts: blog_preflight.py, blog_render.py, generate_hero.py
