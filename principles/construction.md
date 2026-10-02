---
type: Principle Set
title: "Principles — Construction"
description: "4 org engineering principles for construction, derived from SWEBOK v4.0 (Software Construction)."
tags: [principles, construction]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: CON-1
    title: "Minimize complexity"
    enforcement: guidance
  - id: CON-2
    title: "Anticipate change"
    enforcement: guidance
  - id: CON-3
    title: "Construct for verification"
    enforcement: wave-1
    enforced_by: "Code/QA loop"
  - id: CON-4
    title: "Reuse and follow standards"
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

# Principles — Construction

Derived from SWEBOK v4.0 knowledge area(s): Software Construction. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## CON-1 Minimize complexity

Prefer the simplest code that meets the requirement; readable code beats clever code.

- **Enforcement:** guidance only; reviewed by humans.
- **Refined by:** [Software design guideline](/guidelines/software-design.md)

## CON-2 Anticipate change

Write code that is easy to modify: prefer deep modules with simple interfaces, split only when it reduces complexity, use clear names, and avoid duplicating knowledge.

- **Enforcement:** guidance only; reviewed by humans.
- **Refined by:** [Software design guideline](/guidelines/software-design.md)

## CON-3 Construct for verification

Make code testable by design (dependency injection, pure functions, observable outputs) and verify continuously as you build.

- **Enforcement:** wave 1 — Code/QA loop: Tests generated alongside code; coverage above threshold. See [enforcement map](/principles/enforcement.md).

## CON-4 Reuse and follow standards

Use proven libraries and agreed coding standards; vet third-party components for licence, maintenance and security before adopting them.

- **Enforcement:** guidance only; reviewed by humans.
