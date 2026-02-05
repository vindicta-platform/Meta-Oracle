---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
---

1. **Setup**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root.

2. **Load Design Docs**
   Read `plan.md` (tech stack), `spec.md` (user stories), and any optional docs like `data-model.md` or `contracts/`.

3. **Task Generation**
   Generate `tasks.md` using the template at `.specify/templates/tasks-template.md`.
   - Organize tasks by **user story** phase.
   - Phase 1: Setup, Phase 2: Foundational, Phase 3+: User Stories (in priority order).
   - Strictly follow the checklist format: `- [ ] [TaskID] [P?] [Story?] Description with file path`.

4. **Validation**
   Ensure all tasks are independently testable and specific enough for an LLM to execute.

5. **Report**
   Summarize total task count, parallel opportunities, and suggested MVP scope.
