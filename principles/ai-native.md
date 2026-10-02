---
type: Principle Set
title: "Principles — AI-native extensions"
description: "7 org principles for agent-produced work that go beyond SWEBOK v4.0."
tags: [principles, ai-native]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:05:00+05:30
principles:
  - id: AIN-1
    title: "Evaluate agents, not just code"
    enforcement: wave-1
    enforced_by: "CI gate"
  - id: AIN-2
    title: "Gate on evidence at human checkpoints"
    enforcement: wave-1
    enforced_by: "Orchestrator"
  - id: AIN-3
    title: "Engineer context as an artifact"
    enforcement: wave-1
    enforced_by: "CI gate"
  - id: AIN-4
    title: "Record provenance for every generated artifact"
    enforcement: wave-1
    enforced_by: "All agents"
  - id: AIN-5
    title: "Give agents least privilege"
    enforcement: wave-2
    enforced_by: "Control plane"
  - id: AIN-6
    title: "Treat model choice and token cost as design decisions"
    enforcement: wave-2
    enforced_by: "LLM gateway"
  - id: AIN-7
    title: "Watch for drift continuously"
    enforcement: wave-2
    enforced_by: "Product loop"
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:05:00+05:30
verified: []
---

# Principles — AI-native extensions

These principles go beyond SWEBOK v4.0, which assumes deterministic tools and human authors. Each names the SWEBOK principle it extends. See the [principles index](/principles/index.md).

## AIN-1 Evaluate agents, not just code

Every skill and agent has an eval suite with pass thresholds, rerun whenever its prompt, skill, model or context changes. Extends TST-1.

- **Enforcement:** wave 1 — CI gate: Skill/agent eval suite meets pass threshold. See [enforcement map](/principles/enforcement.md).

## AIN-2 Gate on evidence at human checkpoints

Define where a human must approve before an agent proceeds, and what evidence the agent must present (trace links, eval results, diff). Extends MGT-2, QUA-1.

- **Enforcement:** wave 1 — Orchestrator: Checkpoint blocks until a human approves. See [enforcement map](/principles/enforcement.md).

## AIN-3 Engineer context as an artifact

Context packs, KB entries, memory and skill files are versioned, reviewed and tested like code. Extends SCM-1, MNT-2.

- **Enforcement:** wave 1 — CI gate: Context and skill files versioned; changes trigger evals. See [enforcement map](/principles/enforcement.md).

## AIN-4 Record provenance for every generated artifact

Capture the agent, skill version, model, inputs and human approver for each artifact. Extends SCM-2.

- **Enforcement:** wave 1 — All agents: Provenance frontmatter present on every output. See [enforcement map](/principles/enforcement.md).

## AIN-5 Give agents least privilege

Scope tools, MCP servers, file and network access per agent and per task; deny by default. Extends SEC-2.

- **Enforcement:** wave 2 — Control plane: Per-agent tool allowlist enforced. See [enforcement map](/principles/enforcement.md).

## AIN-6 Treat model choice and token cost as design decisions

Route tasks to models deliberately, set budgets, and record the choice in an ADR. Extends ECO-1, ARC-2.

- **Enforcement:** wave 2 — LLM gateway: Per-task budget and model routing logged. See [enforcement map](/principles/enforcement.md).

## AIN-7 Watch for drift continuously

Compare code against design, design against requirements, and requirements against intent; flag divergence to a human rather than silently fixing it. Extends MNT-2, QUA-2.

- **Enforcement:** wave 2 — Product loop: Drift report raised to a human. See [enforcement map](/principles/enforcement.md).
