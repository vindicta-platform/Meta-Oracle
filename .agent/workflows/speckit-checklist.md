---
description: Generate a custom checklist for the current feature based on user requirements.
---

1. **Setup**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS.

2. **Clarify Intent**
   Ask up to three contextual clarifying questions to refine the checklist scope, risk prioritization, and depth.

3. **Understand Request**
   Combine user input and clarifying answers to derive the checklist theme and mapping.

4. **Load Feature Context**
   Read relevant portions of `spec.md`, `plan.md`, and `tasks.md`.

5. **Generate Checklist**
   Create a new checklist file in `FEATURE_DIR/checklists/` (e.g., `ux.md`, `api.md`).
   - Items must test the **requirements quality**, not the implementation.
   - Use dimensions: Completeness, Clarity, Consistency, Measurability, Coverage.
   - Format: `[ ] CHK### <Question> [Dimension, Reference]`.

6. **Report**
   Summarize focus areas and provide the path to the created checklist.
