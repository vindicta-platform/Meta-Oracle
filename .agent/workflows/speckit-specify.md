---
description: Create or update the feature specification from a natural language feature description.
---

1. **Branch Preparation**
// turbo
   Generate a concise short name (2-4 words) for the feature.
   - Fetch remote branches (`git fetch --all --prune`).
   - Find the next available branch/feature number.
   - Run `.specify/scripts/powershell/create-new-feature.ps1` with the number and name.

2. **Load Spec Template**
   Read `.specify/templates/spec-template.md`.

3. **Draft Specification**
   - Extract actors, actions, data, and constraints from the description.
   - Use informed guesses for unclear aspects (max 3 `[NEEDS CLARIFICATION]` markers).
   - Define functional requirements, success criteria, and key entities.

4. **Quality Validation**
   - Create a `checklists/requirements.md` file.
   - Self-validate the spec against the checklist (max 3 iterations).
   - Address any failing items.

5. **User Clarification (if needed)**
   Present up to 3 critical questions with recommended options if markers remain. Update the spec based on responses.

6. **Report**
   Finalize the spec and provide the branch name and spec file path.
