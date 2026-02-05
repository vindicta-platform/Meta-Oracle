---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

1. **Setup**
// turbo
   Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse paths for spec, plan, and branch.

2. **Load Context**
   Read `spec.md`, `constitution.md`, and the `plan.md` template.

3. **Execute Planning Workflow**
   Follow the `plan.md` template structure:
   - Fill Technical Context (note unknowns as "NEEDS CLARIFICATION").
   - Fill Constitution Check.
   - **Phase 0: Research**: Resolve all unknowns and document in `research.md`.
   - **Phase 1: Design**: Generate `data-model.md`, `contracts/`, and `quickstart.md`.
   - **Phase 1: Agent Context**: Run script to update agent-specific context files.

4. **Final Check**
   Re-evaluate constitution alignment post-design.

5. **Report**
   End after Phase 2 planning and list all generated artifacts.
