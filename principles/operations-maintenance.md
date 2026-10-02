---
type: Principle Set
title: "Principles — Operations and maintenance"
description: "4 org engineering principles for operations and maintenance, derived from SWEBOK v4.0 (Software Engineering Operations, Software Maintenance)."
tags: [principles, operations]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: OPS-1
    title: "Design for operability"
    enforcement: guidance
  - id: OPS-2
    title: "Automate delivery and recovery"
    enforcement: guidance
  - id: MNT-1
    title: "Plan for the whole lifecycle"
    enforcement: guidance
  - id: MNT-2
    title: "Keep the system understandable"
    enforcement: wave-2
    enforced_by: "Product loop"
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

# Principles — Operations and maintenance

Derived from SWEBOK v4.0 knowledge area(s): Software Engineering Operations, Software Maintenance. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## OPS-1 Design for operability

Build in observability (logs, metrics, traces), health checks and runbooks before go-live, not after the first incident.

- **Enforcement:** guidance only; reviewed by humans.

## OPS-2 Automate delivery and recovery

Deploy through repeatable pipelines with rollback; define SLOs and respond to incidents with blameless post-incident reviews.

- **Enforcement:** guidance only; reviewed by humans.

## MNT-1 Plan for the whole lifecycle

Most cost comes after release; budget for corrective, adaptive, perfective and preventive maintenance from the start.

- **Enforcement:** guidance only; reviewed by humans.

## MNT-2 Keep the system understandable

Pay down technical debt deliberately, keep documentation current, and refactor before complexity makes change unsafe.

- **Enforcement:** wave 2 — Product loop: Drift report raised to a human. See [enforcement map](/principles/enforcement.md).
- **Refined by:** [Software design guideline](/guidelines/software-design.md)
