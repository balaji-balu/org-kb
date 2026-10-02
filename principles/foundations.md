---
type: Principle Set
title: "Principles — Foundations"
description: "4 org engineering principles for foundations, derived from SWEBOK v4.0 (Computing Foundations, Mathematical Foundations, Engineering Foundations)."
tags: [principles, foundations]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: FND-1
    title: "Engineer, don't just code"
    enforcement: guidance
  - id: FND-2
    title: "Measure before you claim"
    enforcement: guidance
  - id: FND-3
    title: "Respect computational limits"
    enforcement: guidance
  - id: FND-4
    title: "Use precise models where stakes are high"
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

# Principles — Foundations

Derived from SWEBOK v4.0 knowledge area(s): Computing Foundations, Mathematical Foundations, Engineering Foundations. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## FND-1 Engineer, don't just code

Treat software as an engineering artifact: define the problem, consider alternatives, make trade-offs explicit, and verify the result against criteria set beforehand.

- **Enforcement:** guidance only; reviewed by humans.

## FND-2 Measure before you claim

Back decisions about performance, reliability or effort with data and a stated method. An unmeasured claim is a hypothesis.

- **Enforcement:** guidance only; reviewed by humans.

## FND-3 Respect computational limits

Choose algorithms and data structures with known complexity; reason about concurrency, memory and failure before they show up in production.

- **Enforcement:** guidance only; reviewed by humans.

## FND-4 Use precise models where stakes are high

Apply formal reasoning (state machines, invariants, proofs, model checking) in proportion to the cost of being wrong.

- **Enforcement:** guidance only; reviewed by humans.
