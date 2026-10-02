---
type: Principle Set
title: "Principles — Configuration management"
description: "3 org engineering principles for configuration management, derived from SWEBOK v4.0 (Software Configuration Management)."
tags: [principles, scm]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: SCM-1
    title: "Version everything that defines the system"
    enforcement: wave-1
    enforced_by: "CI gate"
  - id: SCM-2
    title: "Control and audit change"
    enforcement: guidance
  - id: SCM-3
    title: "Know what is deployed"
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

# Principles — Configuration management

Derived from SWEBOK v4.0 knowledge area(s): Software Configuration Management. Wording paraphrases SWEBOK; see the [principles index](/principles/index.md) for the full set.

## SCM-1 Version everything that defines the system

Code, configuration, infrastructure, schemas, requirements and build scripts all live under version control.

- **Enforcement:** wave 1 — CI gate: All artifacts in git with semver frontmatter. See [enforcement map](/principles/enforcement.md).

## SCM-2 Control and audit change

Every change is identified, reviewed and traceable to a reason; releases are baselined and reproducible from source.

- **Enforcement:** guidance only; reviewed by humans.

## SCM-3 Know what is deployed

Maintain an accurate record of which versions and dependencies run in each environment, including a software bill of materials.

- **Enforcement:** guidance only; reviewed by humans.
