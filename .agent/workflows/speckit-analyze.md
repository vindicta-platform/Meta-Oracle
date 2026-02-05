---
description: Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.
---

1. **Initialize Analysis Context**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root and parse FEATURE_DIR, SPEC, PLAN, and TASKS paths.

2. **Load Artifacts**
   Load minimal context from `spec.md`, `plan.md`, `tasks.md`, and `.specify/memory/constitution.md`.

3. **Build Semantic Models**
   Create internal representations for requirements, user stories, task coverage, and constitution rules.

4. **Detection Passes**
   Perform analysis for:
   - Duplication
   - Ambiguity
   - Underspecification
   - Constitution Alignment
   - Coverage Gaps
   - Inconsistency

5. **Severity Assignment**
   Prioritize findings as CRITICAL, HIGH, MEDIUM, or LOW.

6. **Produce Report**
   Output a Markdown report with a findings table, coverage summary, and constitution alignment.

7. **Next Actions & Remediation**
   Suggest follow-up commands and offer optional remediation edits.
