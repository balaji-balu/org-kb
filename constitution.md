---
type: Constitution
title: Organization constitution
description: The 8 non-negotiable articles every project, agent and person follows. Loaded into every agent's context; nothing else in the KB or a project may contradict it.
tags: [org-kb, constitution, layer-1]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:15:00+05:30
sources:
  - id: ieo.constitution.v1
    title: Constitution — Intelligent Edge Orchestrator (v1)
    author: human:balaji-balu
    resource: https://github.com/balaji-balu/ieo/blob/main/constitution.md
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:15:00+05:30
verified: []
---

# Organization constitution

These 8 articles are non-negotiable. Every other document in this KB and in each project works out the details; none may contradict them. Generalised from the [ieo constitution](https://github.com/balaji-balu/ieo/blob/main/constitution.md); each article cites the [principles](/principles/index.md) it rests on.

## Articles

1. **The spec is the contract.** Behaviour is defined in the project spec, not in code. A behaviour change updates the spec in the same change. Where the spec is silent, the answer goes into the spec or an ADR, not into code alone. *([REQ-4](/principles/requirements.md), [MOD-1](/principles/management-process.md))*
2. **Adopted standards come first.** Where a project adopts an external standard, that standard is authoritative for the rules it covers; where the project disagrees with it, the project has a bug. Each project names its standards and pins their versions. *([CON-4](/principles/construction.md))*
3. **Humans own intent; agents own execution.** Humans decide what to build, approve specs, plans and tests, make architecture decisions and merge. Agents plan, test, implement and respond to review inside the approved scope. *([AIN-2](/principles/ai-native.md))*
4. **Tests are the executable spec.** No behaviour without a test that was seen failing first. *([CON-3](/principles/construction.md), [TST-2](/principles/testing.md))*
5. **Every change is small, traceable and machine-verified.** One slice per pull request, spec references everywhere, CI green before review. *([REQ-4](/principles/requirements.md), [SCM-2](/principles/configuration-management.md), [AIN-4](/principles/ai-native.md))*
6. **Complexity is the enemy.** Code follows the [software design guideline](/guidelines/software-design.md): deep modules, hidden information, errors defined out of existence, obvious code. *([CON-1](/principles/construction.md))*
7. **Safety before autonomy.** The deterministic core decides; intelligent features only advise and always have a baseline fallback. Security-sensitive areas named in the project spec always get human review. No secrets anywhere in a repository. *([SEC-1](/principles/quality-security.md), [SEC-3](/principles/quality-security.md), [AIN-5](/principles/ai-native.md))*
8. **The process learns.** Repeated mistakes become rules in agent instructions, guidelines or lint rules. *([PRC-2](/principles/management-process.md))*

## Order of authority

Within a project: adopted external standard → project spec → project ADRs → code. Code is never the source of truth. This constitution sits above all of them; the org [principles](/principles/index.md) and [guidelines](/guidelines/index.md) apply unless a project ADR records a reasoned exception.

## What each project provides

A project inherits this KB and adds only what is specific to it.

| Document | Purpose | Template |
| --- | --- | --- |
| Project constitution (optional) | Extra articles, e.g. naming the adopted standard; may add, never contradict | — |
| Spec | Behaviour as MUST/SHOULD rules, domain terms, security areas, test matrix | — |
| Intents | Why each change exists and what done looks like | [intent](/standards/templates/intent.md) |
| ADRs | Decisions the spec leaves open | [ADR](/standards/templates/adr.md) |
| Agent rules (`CLAUDE.md` / `AGENTS.md`) | Repo map, commands, project guardrails | — |
| Language conventions and review checklist | Rules specific to the stack | — |
| Pull request template | Definition of done as checkboxes | [pull request](/standards/templates/pull-request.md) |

Reference implementation: the [ieo repository](https://github.com/balaji-balu/ieo).

## Amendments

The constitution changes only by a pull request that a human approves and whose description explains why. Documents that conflict with the amended version are updated in the same pull request.
