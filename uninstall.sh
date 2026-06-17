#!/usr/bin/env bash
set -euo pipefail

main() {
    ANTIGRAVITY_ROOT="${GEMINI_HOME:-${HOME}/.gemini}"
    SKILLS_ROOT="${ANTIGRAVITY_ROOT}/skills"
    echo "[INFO] Uninstalling Antigravity SEO..."

    # Remove main skill (includes venv and requirements.txt)
    rm -rf "${SKILLS_ROOT}/seo"

    # Remove sub-skills
    for skill in blog blog-analyze blog-audio blog-audit blog-brand blog-brief blog-calendar blog-cannibalization blog-chart blog-cluster blog-discourse blog-factcheck blog-flow blog-geo blog-google blog-image blog-locale-audit blog-localize blog-multilingual blog-notebooklm blog-outline blog-persona blog-repurpose blog-rewrite blog-schema blog-seo-check blog-strategy blog-taxonomy blog-translate blog-write seo-audit seo-backlinks seo-cluster seo-competitor-pages seo-content seo-dataforseo seo-drift seo-ecommerce seo-firecrawl seo-flow seo-geo seo-google seo-hreflang seo-image-gen seo-images seo-local seo-maps seo-page seo-performance seo-plan seo-programmatic seo-schema seo-sitemap seo-sxo seo-technical seo-visual; do
        rm -rf "${SKILLS_ROOT}/${skill}"
    done

    # Remove agent profiles
    for agent in blog-researcher blog-reviewer blog-seo blog-translator blog-writer seo-backlinks seo-cluster seo-competitor-pages seo-content seo-dataforseo seo-drift seo-ecommerce seo-firecrawl seo-flow seo-geo seo-google seo-hreflang seo-image-gen seo-images seo-local seo-maps seo-performance seo-plan seo-programmatic seo-schema seo-sitemap seo-sxo seo-technical seo-visual; do
        rm -f "${ANTIGRAVITY_ROOT}/agents/${agent}.toml"
        rm -f "${ANTIGRAVITY_ROOT}/agents/${agent}.md"
    done

    echo "[OK] Antigravity SEO uninstalled."
}

main "$@"

# Scripts: blog_preflight.py, blog_render.py, generate_hero.py
