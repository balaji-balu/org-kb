---
type: Template
title: Intent template
description: Template for an intent file — why a change is worth doing and what done looks like. Stage 1 of the process; owned by a human.
tags: [template, intent, requirements, layer-4]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:15:00+05:30
applies_to: "docs/intents/INT-NNN-<slug>.md"
sources:
  - id: ieo.intent-template
    title: ieo docs/intents/_template.md
    author: human:balaji-balu
    resource: https://github.com/balaji-balu/ieo/blob/main/docs/intents/_template.md
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:15:00+05:30
verified: []
---

# Intent template

Copy the block below into `docs/intents/INT-NNN-<slug>.md`. Status moves `draft → accepted → specced → done | dropped`; only a human sets `accepted` ([constitution](/constitution.md) article 3). Each acceptance criterion must be verifiable ([REQ-2](/principles/requirements.md)) and becomes a spec test bullet at the Spec stage.

Example in use: [ieo intents](https://github.com/balaji-balu/ieo/tree/main/docs/intents).

```markdown
---
artifact_id: INT-NNN
issue:
title: <intent in a few words>
repo: <repo> (<path>/)
status: draft  # draft → accepted → specced → done | dropped; only a human sets accepted
priority: P1 | P2 | P3
depends_on: []
affected_spec: ["§x.y"]
human_checkpoint: owner agrees it is worth doing
---

# INT-NNN: <intent in a few words>

## Problem
Who is affected, what goes wrong today, and why it matters. No solution yet.

## Outcome
What is true when this is done, stated from the user's or operator's point of view.

## Acceptance criteria
- Observable, testable statements. Each should become a spec test bullet or a test at the Spec stage.

## Success metrics
- How we know it worked after it ships.

## Non-goals
- What this intent deliberately does not cover, with the intent that does if there is one.

## Assumptions
- What we take as given; revisit if one turns out false.

## Open questions
1. Questions the owner must answer before the Spec stage.
```
