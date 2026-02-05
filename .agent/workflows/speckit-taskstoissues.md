---
description: Convert existing tasks into actionable, dependency-ordered GitHub issues for the feature based on available design artifacts.
---

1. **Initialize**
// turbo
   Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root.

2. **Verify Remote**
   Confirm the Git remote is a GitHub URL by running `git config --get remote.origin.url`.

3. **Create Issues**
   For each task in `tasks.md`, use the GitHub MCP server to create a corresponding issue in the repository.

4. **Safety Check**
// turbo
   Ensure issues are only created in the repository matching the remote URL.
