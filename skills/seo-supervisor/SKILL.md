---
name: seo-supervisor
description: >
  Master Supervisor orchestrator that bridges the SEO and Blog subsystems.
  Analyzes multi-system prompts, generates roadmaps, coordinates task handoffs via .seo-cache,
  and executes a lightweight structured review loop with safety caps.
user-invokable: true
argument-hint: "<goal> [--max-steps <int>] [--force-fresh]"
license: MIT
metadata:
  author: dotusmanali
  version: "1.0.0"
  category: seo
---

# Master Supervisor Orchestrator

## Purpose
Bridges the gap between the SEO analysis and Blog creation subsystems, coordinating complex multi-step user prompts that span both modules.

## When to use
- Anytime the user prompt requires a mix of keyword research/SEO audit and content creation (e.g. "find trends and write a draft").
- To plan and run multi-step sequential tasks interactively.

## Command Reference
`/seo:run <goal> [--max-steps <int>] [--force-fresh]`

## Workflow
1. **Plan Phase**: Parse the user's goal and generate an Execution Roadmap as a visible checklist before executing anything. It details the required skills, target agents, and MCPs/scripts. Wait for user confirmation unless `--yes` is set.
2. **Cache Check (Fix 3)**: Before invoking any skill, check `.seo-cache/` for existing files matching `{domain-or-topic-slug}__{task-type}__{YYYY-MM-DD}.json`. If a cache file is less than 7 days old, ask the user if they want to reuse it, unless `--force-fresh` is set.
3. **Execution Loop**:
   - Invoke the target subagent or script for the current step.
   - Cache results in `.seo-cache/`.
4. **Lightweight Structured Review (Fix 2)**: 
   - Verify if the expected cache file was written to `.seo-cache/` and is valid. Do not re-read full prior outputs.
   - If a step fails, retry it up to a maximum of **2 retries** (3 total attempts).
   - If it still fails:
     * If no downstream tasks depend on its output $\rightarrow$ log a *Partial Failure* and continue.
     * If downstream tasks depend on its output $\rightarrow$ halt and report error.
5. **Safety Cap**: Capped at `max_iterations = 5` total roadmap steps per run. Halt immediately and output partial cache if exceeded.
6. **Handoff Phase**: Render the final deliverables, highlighting which cached files were reused versus freshly generated.
