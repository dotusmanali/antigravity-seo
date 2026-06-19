---
name: run
description: "Master Supervisor orchestrator that bridges SEO, Blog, and memory systems using a structured, lightweight review loop."
argument-hint: "<complex-goal> [--max-steps <int>] [--force-fresh]"
parameters:
  - name: goal
    type: string
    required: true
    description: "Complex cross-system goal (e.g. research keyword and write blog brief)"
  - name: max-steps
    type: integer
    required: false
    description: "Maximum loop iterations before automatic termination (default: 5)"
  - name: force-fresh
    type: boolean
    required: false
    description: "Force execution and ignore cached results even if less than 7 days old"
---

# Run Command

Bridges the SEO and Blog subsystems to coordinate complex multi-system tasks with a safety-limited structured review loop.

## Route

- seo-supervisor

## Rules

- Parse the user's goal into a phased Execution Plan spanning both SEO and Blog systems.
- For each step, run the relevant specialist workflow, caching results in `.seo-cache/`.
- Perform a lightweight structured review (checklist/file checking) after each step. Do not re-read full prior outputs.
- Hard limit of loop iterations is 5 (or specified via `--max-steps`). Halt and return partial results if exceeded.

## Output

Return structured status and execution reports.
