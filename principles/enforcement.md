---
type: Enforcement Map
title: Principle enforcement map
description: Which skill, gate or agent checks each enforceable principle, and in which rollout wave.
tags: [principles, enforcement, ai-native-sdlc]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:05:00+05:30
verified: []
---

# Principle enforcement map

Wave 1 is the 13 principles an agent can check automatically today; wire these into skills and gates first. Wave 2 needs metrics or tooling still to build. All other principles are guidance served from the KB, reviewed by humans.

Enforcer names are generic; rename them to match platform components.

| Wave | Principle | Enforced by | Automated check |
| --- | --- | --- | --- |
| 1 | [AIN-1](/principles/ai-native.md) | CI gate | Skill/agent eval suite meets pass threshold |
| 1 | [AIN-2](/principles/ai-native.md) | Orchestrator | Checkpoint blocks until a human approves |
| 1 | [AIN-3](/principles/ai-native.md) | CI gate | Context and skill files versioned; changes trigger evals |
| 1 | [AIN-4](/principles/ai-native.md) | All agents | Provenance frontmatter present on every output |
| 1 | [ARC-2](/principles/architecture-design.md) | Design skill | Each significant decision has an ADR |
| 1 | [CON-3](/principles/construction.md) | Code/QA loop | Tests generated alongside code; coverage above threshold |
| 1 | [REQ-1](/principles/requirements.md) | Intent skill | Every requirement links to an intent or stakeholder ID |
| 1 | [REQ-2](/principles/requirements.md) | Requirements skill | Each requirement has acceptance criteria in EARS or Gherkin |
| 1 | [REQ-4](/principles/requirements.md) | CI gate | Trace links resolve intent → requirement → design → code → test |
| 1 | [SCM-1](/principles/configuration-management.md) | CI gate | All artifacts in git with semver frontmatter |
| 1 | [SEC-1](/principles/quality-security.md) | Design skill | Threat model section present and non-empty |
| 1 | [SEC-3](/principles/quality-security.md) | CI gate | Dependency and secret scans clean |
| 1 | [TST-2](/principles/testing.md) | CI gate | Unit and integration suites pass |
| 2 | [AIN-5](/principles/ai-native.md) | Control plane | Per-agent tool allowlist enforced |
| 2 | [AIN-6](/principles/ai-native.md) | LLM gateway | Per-task budget and model routing logged |
| 2 | [AIN-7](/principles/ai-native.md) | Product loop | Drift report raised to a human |
| 2 | [ARC-1](/principles/architecture-design.md) | Design skill | Each quality attribute has a measurable scenario |
| 2 | [DES-1](/principles/architecture-design.md) | Code review agent | Coupling and dependency metrics within thresholds |
| 2 | [DES-2](/principles/architecture-design.md) | Code review agent | Coupling and dependency metrics within thresholds |
| 2 | [MNT-2](/principles/operations-maintenance.md) | Product loop | Drift report raised to a human |
| 2 | [QUA-2](/principles/quality-security.md) | Product loop | Drift report raised to a human |
| 2 | [REQ-3](/principles/requirements.md) | Requirements skill | NFR checklist complete (performance, security, availability, usability) |
