---
type: Principle Set
title: "Principles — Requirements"
description: "4 org engineering principles for requirements, derived from SWEBOK v4.0 (Software Requirements)."
tags: [principles, requirements]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: REQ-1
    title: "Start from stakeholder needs, not solutions"
    enforcement: wave-1
    enforced_by: "Intent skill"
  - id: REQ-2
    title: "Make every requirement verifiable"
    enforcement: wave-1
    enforced_by: "Requirements skill"
  - id: REQ-3
    title: "Specify non-functional requirements explicitly"
    enforcement: wave-2
    enforced_by: "Requirements skill"
  - id: REQ-4
    title: "Manage requirements as a living, traced baseline"
    enforcement: wave-1
    enforced_by: "CI gate"
sources:
  - id: swebok.v4
    title: SWEBOK Guide v4.0
    author: IEEE Computer Society
    resource: https://www.computer.org/education/bodies-of-knowledge/software-engineering
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:05:00+05:30
verified: []
---

# Principles — Requirements

Derived from SWEBOK v4.0 knowledge area(s): Software Requirements. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## REQ-1 Start from stakeholder needs, not solutions

Elicit the problem, users and context before proposing features. Record who asked for each requirement and why.

- **Enforcement:** wave 1 — Intent skill: Every requirement links to an intent or stakeholder ID. See [enforcement map](/principles/enforcement.md).

## REQ-2 Make every requirement verifiable

State it so a test, inspection or measurement can prove it met. Replace "fast" or "user-friendly" with numbers and conditions.

- **Enforcement:** wave 1 — Requirements skill: Each requirement has acceptance criteria in EARS or Gherkin. See [enforcement map](/principles/enforcement.md).

## REQ-3 Specify non-functional requirements explicitly

Performance, security, availability, usability and compliance get the same rigor as features; they drive the architecture.

- **Enforcement:** wave 2 — Requirements skill: NFR checklist complete (performance, security, availability, usability). See [enforcement map](/principles/enforcement.md).

## REQ-4 Manage requirements as a living, traced baseline

Version them, control changes, and keep traceability from requirement to design, code and test.

- **Enforcement:** wave 1 — CI gate: Trace links resolve intent → requirement → design → code → test. See [enforcement map](/principles/enforcement.md).
