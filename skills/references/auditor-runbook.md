# Auditor Runbook — ownership & changelog

> **Runbook version**: 1.2 · **Release**: v10.0.x · **Last updated**: 2026-05-06

The authoritative auditor runbook — §1 Handoff Schema, §2 Critical Fail Cap, §3 Guardrail Negatives, §4 Artifact Gate, §5 User-Facing Translation Layer — is **inlined directly in the two auditor skills**, because markdown-linked references do not load reliably at skill-activation time. The runbook therefore lives where it executes:

- [cross-cutting/content-quality-auditor/SKILL.md](https://github.com/dotusmanali/antigravity-seo/blob/main/skills/content-quality-auditor/SKILL.md) — §1–§5 inline
- [cross-cutting/domain-authority-auditor/SKILL.md](https://github.com/dotusmanali/antigravity-seo/blob/main/skills/domain-authority-auditor/SKILL.md) — §1–§5 inline

Those two inlined copies **are** the runbook and are co-equal homes. When auditor behavior changes, edit the §1–§5 blocks in BOTH skill bodies and keep them consistent with each other. This file no longer duplicates the procedure — it records only ownership and version history, so there is no third faithful copy to maintain.

## Ownership routing

- **Auditor item / veto definitions** (IDs, dimension structure) → [core-eeat-benchmark.md](https://github.com/dotusmanali/antigravity-seo/blob/main/skills/references/core-eeat-benchmark.md) (CORE-EEAT) and [cite-domain-rating.md](https://github.com/dotusmanali/antigravity-seo/blob/main/skills/references/cite-domain-rating.md) (CITE)
- **General handoff format for all skills** → [skill-contract.md](https://github.com/dotusmanali/antigravity-seo/blob/main/skills/references/skill-contract.md)
- **Cap policy, cap arithmetic, handoff schema, translation rules** → the §1–§5 blocks inlined in the two auditor skills above

## Changelog

- **1.2** (v10.0.x): severity-tier routing (P0/P1/P2) added to §5 Translation Layer.
- **1.1**: Example 1 arithmetic corrected to integer; cross-version rerun rule (§5); BLOCKED-path escape hatch (§5); `open_loops` scope clarified (§5).
- **1.0**: initial runbook.
