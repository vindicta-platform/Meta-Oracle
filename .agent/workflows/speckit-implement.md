---
description: Execute the implementation plan by processing and executing all tasks defined in tasks.md
---

1. **Initialize**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root.

2. **Check Checklist Status**
   Scan files in `FEATURE_DIR/checklists/`. If any are incomplete, show a status table and ask the user if they want to proceed.

3. **Load Execution Context**
   Read `tasks.md`, `plan.md`, and any existing design docs (`data-model.md`, `contracts/`, etc.).

4. **Project Setup Verification**
   Create or verify ignore files (`.gitignore`, `.dockerignore`, etc.) based on the detected tech stack.

5. **Execute Tasks**
   Process `tasks.md` phase-by-phase (Setup, Tests, Core, Integration, Polish):
   - Respect dependencies and parallel markers [P].
   - Follow TDD: Execute test tasks before implementation tasks.
   - Halt on failure for sequential tasks.

6. **Progress Tracking**
   Mark completed tasks as [X] in `tasks.md` and report progress after each task.

7. **Validation**
   Verify all tasks are complete and the implementation matches the spec.
