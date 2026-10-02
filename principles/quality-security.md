---
type: Principle Set
title: "Principles — Quality and security"
description: "5 org engineering principles for quality and security, derived from SWEBOK v4.0 (Software Quality, Software Security)."
tags: [principles, quality]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: QUA-1
    title: "Build quality in; don't inspect it in"
    enforcement: guidance
  - id: QUA-2
    title: "Define quality in measurable terms"
    enforcement: wave-2
    enforced_by: "Product loop"
  - id: SEC-1
    title: "Treat security as a requirement from day one"
    enforcement: wave-1
    enforced_by: "Design skill"
  - id: SEC-2
    title: "Apply secure design principles"
    enforcement: guidance
  - id: SEC-3
    title: "Secure the supply chain and the lifecycle"
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

# Principles — Quality and security

Derived from SWEBOK v4.0 knowledge area(s): Software Quality, Software Security. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## QUA-1 Build quality in; don't inspect it in

Prevent defects through reviews, static analysis and clear definitions of done, rather than relying on late testing.

- **Enforcement:** guidance only; reviewed by humans.

## QUA-2 Define quality in measurable terms

Agree quality characteristics (e.g. ISO/IEC 25010) and target values per product, and verify and validate against them.

- **Enforcement:** wave 2 — Product loop: Drift report raised to a human. See [enforcement map](/principles/enforcement.md).

## SEC-1 Treat security as a requirement from day one

Threat-model during requirements and design; security is not a final-phase activity.

- **Enforcement:** wave 1 — Design skill: Threat model section present and non-empty. See [enforcement map](/principles/enforcement.md).

## SEC-2 Apply secure design principles

Least privilege, defense in depth, secure defaults, fail-safe behavior, and minimal attack surface.

- **Enforcement:** guidance only; reviewed by humans.

## SEC-3 Secure the supply chain and the lifecycle

Validate all inputs, manage secrets properly, scan dependencies, patch promptly, and plan for vulnerability disclosure and response.

- **Enforcement:** wave 1 — CI gate: Dependency and secret scans clean. See [enforcement map](/principles/enforcement.md).
