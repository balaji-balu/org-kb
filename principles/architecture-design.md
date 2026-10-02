---
type: Principle Set
title: "Principles — Architecture and design"
description: "6 org engineering principles for architecture and design, derived from SWEBOK v4.0 (Software Architecture, Software Design)."
tags: [principles, design]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: ARC-1
    title: "Let quality attributes drive the architecture"
    enforcement: wave-2
    enforced_by: "Design skill"
  - id: ARC-2
    title: "Record significant decisions"
    enforcement: wave-1
    enforced_by: "Design skill"
  - id: ARC-3
    title: "Describe architecture through multiple views"
    enforcement: guidance
  - id: DES-1
    title: "Separate concerns and hide information"
    enforcement: wave-2
    enforced_by: "Code review agent"
  - id: DES-2
    title: "Maximize cohesion, minimize coupling"
    enforcement: wave-2
    enforced_by: "Code review agent"
  - id: DES-3
    title: "Design for change and for failure"
    enforcement: guidance
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

# Principles — Architecture and design

Derived from SWEBOK v4.0 knowledge area(s): Software Architecture, Software Design. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## ARC-1 Let quality attributes drive the architecture

Choose structures by the qualities they must deliver (scalability, modifiability, security, availability), and evaluate candidates against scenarios for each.

- **Enforcement:** wave 2 — Design skill: Each quality attribute has a measurable scenario. See [enforcement map](/principles/enforcement.md).

## ARC-2 Record significant decisions

Capture each architectural decision with its context, options considered, rationale and consequences (e.g. an ADR).

- **Enforcement:** wave 1 — Design skill: Each significant decision has an ADR. See [enforcement map](/principles/enforcement.md).
- **Refined by:** [Software design guideline](/guidelines/software-design.md)

## ARC-3 Describe architecture through multiple views

Address each stakeholder concern with an appropriate view (context, component, deployment, data, runtime) rather than one diagram for all.

- **Enforcement:** guidance only; reviewed by humans.

## DES-1 Separate concerns and hide information

Each module owns one responsibility and exposes a stable interface; internals can change without rippling outward.

- **Enforcement:** wave 2 — Code review agent: Coupling and dependency metrics within thresholds. See [enforcement map](/principles/enforcement.md).
- **Refined by:** [Software design guideline](/guidelines/software-design.md)

## DES-2 Maximize cohesion, minimize coupling

Group what changes together; depend on abstractions, not concrete implementations.

- **Enforcement:** wave 2 — Code review agent: Coupling and dependency metrics within thresholds. See [enforcement map](/principles/enforcement.md).
- **Refined by:** [Software design guideline](/guidelines/software-design.md)

## DES-3 Design for change and for failure

Anticipate likely variations and isolate them; assume dependencies fail and define how the system degrades.

- **Enforcement:** guidance only; reviewed by humans.
- **Refined by:** [Software design guideline](/guidelines/software-design.md)
