---
type: Template
title: ADR template
description: Template for an architecture decision record — a decision the spec leaves open, written as rules an agent can follow.
tags: [template, adr, architecture, layer-4]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:15:00+05:30
applies_to: "docs/adr/NNNN-<slug>.md"
sources:
  - id: ieo.adr-template
    title: ieo docs/adr/README.md (template section)
    author: human:balaji-balu
    resource: https://github.com/balaji-balu/ieo/blob/main/docs/adr/README.md
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:15:00+05:30
verified: []
---

# ADR template

Copy the block below into `docs/adr/NNNN-<slug>.md` and add a row to the project's ADR index. Agents follow an **Accepted** ADR without re-asking; to change one, write a new ADR that supersedes it. List at least two options ([G-A7](/guidelines/software-design.md)) and state the decision as rules an agent can follow ([ARC-2](/principles/architecture-design.md)).

Example in use: [ieo ADRs](https://github.com/balaji-balu/ieo/tree/main/docs/adr).

```markdown
# NNNN. <Decision in a few words>

Status: Proposed | Accepted | Superseded by NNNN · Date: YYYY-MM-DD · Spec: §x.y

## Context
What forces the decision. Cite spec sections.

## Decision
What we do, stated as rules an agent can follow.

## Consequences
What gets easier, what gets harder, what to watch.

## Options considered
- Option — why not.
```
