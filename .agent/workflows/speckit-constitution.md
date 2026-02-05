---
description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.
---

1. **Load Template**
   Read the existing constitution template at `.specify/memory/constitution.md` and identify placeholder tokens (e.g., `[PROJECT_NAME]`).

2. **Collect Values**
   Derive concrete values for placeholders from user input, README, or repo context. Update dates and increment the `CONSTITUTION_VERSION` (MAJOR/MINOR/PATCH).

3. **Draft Updates**
   Replace all placeholders with concrete text. Ensure principles are declarative and testable.

4. **Propagate Consistency**
   Verify and update dependent templates:
   - `plan-template.md`
   - `spec-template.md`
   - `tasks-template.md`
   - Command files in `.specify/templates/commands/*.md`

5. **Finalize**
   Generate a Sync Impact Report (as an HTML comment), validate the final Markdown structure, and write to `.specify/memory/constitution.md`.

6. **Report**
   Summarize the new version, bump rationale, and suggested commit message.
