---
type: Principle Set
title: "Principles — Testing"
description: "4 org engineering principles for testing, derived from SWEBOK v4.0 (Software Testing)."
tags: [principles, testing]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: TST-1
    title: "Testing shows the presence of defects, not their absence"
    enforcement: guidance
  - id: TST-2
    title: "Test at every level"
    enforcement: wave-1
    enforced_by: "CI gate"
  - id: TST-3
    title: "Design tests from requirements and from structure"
    enforcement: guidance
  - id: TST-4
    title: "Test early and keep tests trustworthy"
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

# Principles — Testing

Derived from SWEBOK v4.0 knowledge area(s): Software Testing. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## TST-1 Testing shows the presence of defects, not their absence

Choose tests by risk and coverage criteria, and state what remains untested.

- **Enforcement:** guidance only; reviewed by humans.

## TST-2 Test at every level

Unit, integration, system and acceptance tests each catch different faults; automate the ones that run repeatedly.

- **Enforcement:** wave 1 — CI gate: Unit and integration suites pass. See [enforcement map](/principles/enforcement.md).

## TST-3 Design tests from requirements and from structure

Combine black-box techniques (equivalence classes, boundary values, scenarios) with white-box coverage.

- **Enforcement:** guidance only; reviewed by humans.

## TST-4 Test early and keep tests trustworthy

Shift testing left into requirements and design reviews; treat flaky or slow tests as defects.

- **Enforcement:** guidance only; reviewed by humans.
