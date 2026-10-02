---
type: Template
title: Pull request template
description: Pull request template carrying the definition of done as checkboxes; projects add their own language and CI items.
tags: [template, pull-request, definition-of-done, layer-4]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:15:00+05:30
applies_to: ".github/pull_request_template.md"
sources:
  - id: ieo.pr-template
    title: ieo .github/pull_request_template.md
    author: human:balaji-balu
    resource: https://github.com/balaji-balu/ieo/blob/main/.github/pull_request_template.md
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:15:00+05:30
verified: []
---

# Pull request template

Copy the block below into `.github/pull_request_template.md`. It enforces [constitution](/constitution.md) articles 1, 4 and 5: spec updated with behaviour, tests seen failing first, one small traced slice. Add project-specific checks (language tooling, generated code, compliance) under "Project checks".

Example in use: [ieo PR template](https://github.com/balaji-balu/ieo/blob/main/.github/pull_request_template.md).

```markdown
## Summary

<!-- What changes and why. Link the issue. -->

Closes #

Intent: INT-NNN <!-- "n/a" for tooling or docs-only PRs -->

## Spec sections affected

<!-- e.g. §8.5, §17.4. Write "None — no behaviour change" for docs/tooling-only PRs. -->

- §

## Slice

<!-- The roadmap step (or smaller) this PR implements, and what is explicitly out of scope. -->

- Step:
- Out of scope:

## Design

<!-- For new or changed modules: the options considered and why this one (G-A7).
     Cite guideline IDs (G-A1…) where relevant. -->

## Tests

<!-- Spec tests added or updated, named after the bullet they cover.
     Confirm each new test was seen failing for the right reason first. -->

-

## Definition of done

- [ ] Spec sections affected are listed above
- [ ] Spec (and system overview, if the design changed) updated in this PR
- [ ] Spec tests added or updated, named after the bullets they cover
- [ ] Local checks pass; CI green on the latest commit
- [ ] AI code review run; every finding resolved or answered
- [ ] Security review run, if this touches security-sensitive areas named in the spec
- [ ] ADR added for any implementation-defined choice
- [ ] Intent ID cited; its status updated if this PR completes a stage

## Project checks

<!-- Project-specific items, e.g. generated code regenerated, no package added to a known-broken list. -->
```
