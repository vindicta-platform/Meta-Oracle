---
description: Identify underspecified areas in the current feature spec by asking up to 5 highly targeted clarification questions and encoding answers back into the spec.
---

1. **Initialize**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly` from repo root and parse FEATURE_DIR and FEATURE_SPEC.

2. **Analysis Pass**
   Perform a structured scan of the spec for ambiguity and coverage gaps across functional scope, data model, UX flow, and quality attributes.

3. **Prioritize Questions**
   Generate a prioritized queue of up to 5 (max 10 total) clarification questions that materially impact implementation.

4. **Interactive Questioning Loop**
   Present one question at a time with recommended options or suggested short answers.

5. **Incremental Integration**
   After each answer, update the `## Clarifications` section in the spec and apply the changes directly to the relevant sections.

6. **Validation & Completion**
   Verify the updated spec is consistent and testable. Report the number of questions resolved and sections updated.
