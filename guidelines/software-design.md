---
type: Guideline
title: Software design guideline
description: 23 language-neutral design and coding rules (G-A1 to G-D4) based on Ousterhout's "A Philosophy of Software Design", each with its red flag, the process stage it applies at, and who enforces it. Cited by ID in plans and reviews.
tags: [design, construction, complexity, code-review, layer-3-guideline]
version: 0.1.0
status: draft
timestamp: 2026-10-02T07:15:00+05:30
refines: [CON-1, CON-2, DES-1, DES-2, DES-3, ARC-2, MNT-2]
sources:
  - id: ieo.coding-guidelines.v1
    title: Coding Guidelines — Intelligent Edge Orchestrator (v1), sections A–D
    author: human:balaji-balu
    resource: https://github.com/balaji-balu/ieo/blob/main/docs/coding-guidelines.md
  - id: ousterhout.posd.2e
    title: A Philosophy of Software Design (2nd ed.)
    author: John Ousterhout
    resource: https://web.stanford.edu/~ouster/cgi-bin/book.php
generated:
  by: claude/claude-opus-5-5
  at: 2026-10-02T07:15:00+05:30
verified: []
---

# Software design guideline

**The goal is to reduce complexity.** Complexity shows up as *change amplification* (one change touches many places), *cognitive load* (too much to know before making a change) and *unknown unknowns* (it is not obvious what must change). It comes from **dependencies** and **obscurity**; every rule below targets one of the two.

Each rule has an ID for plans and review comments ("violates G-A2"), the **red flag** that shows it is broken, and the process stage where it applies. Rules are generalised from sections A–D of the [ieo coding guidelines](https://github.com/balaji-balu/ieo/blob/main/docs/coding-guidelines.md) and keep the same IDs, so ieo's existing citations stay valid. Projects add their own language and repository rules (ieo's sections E and F) and concrete examples on top.

Refines the principles [CON-1, CON-2](/principles/construction.md), [DES-1, DES-2, DES-3, ARC-2](/principles/architecture-design.md) and [MNT-2](/principles/operations-maintenance.md); required by [constitution](/constitution.md) article 6.

## A. Module design

Applied at **Plan**; checked at human **Review**.

| ID | Rule | Red flag |
| --- | --- | --- |
| G-A1 | **Deep modules.** A module's interface should be much simpler than its implementation. Prefer few, powerful operations over many thin ones. | *Shallow module*: the interface is about as complex as what it does. |
| G-A2 | **Information hiding.** Each design decision (a wire format, a storage layout, a state encoding) lives in exactly one module. | *Information leakage*: the same knowledge coded in two places, e.g. two services both parsing one file layout. |
| G-A3 | **Split by knowledge, not by order of execution.** | *Temporal decomposition*: `fetch` / `parse` / `apply` modules that all have to know the same format. |
| G-A4 | **Different layer, different abstraction.** Each layer adds meaning to what it wraps. | *Pass-through method or variable*: a function that only forwards its arguments, or a parameter threaded through layers that don't use it. |
| G-A5 | **Pull complexity downward.** The module deals with the complexity so its callers don't have to. Give sensible defaults. | *Overexposure*: callers must set knobs they don't understand to do the common thing. |
| G-A6 | **Somewhat general-purpose interfaces.** Keep business policy out of generic mechanisms (schedulers, messaging wrappers, stores). | *Special-general mixture*: business-specific cases in a general utility. |
| G-A7 | **Design it twice.** Every plan that adds or changes a module names at least two options and why one was chosen. | The plan shows only one design. |
| G-A8 | **Keep together what belongs together, and apart what doesn't.** Merge code that shares information or is always used together; separate general code from special-purpose code. | *Conjoined methods*: one function can't be understood without reading another. *Repetition*: the same code pattern in several places. |

## B. Errors and special cases

Applied at **Implement**.

| ID | Rule | Red flag |
| --- | --- | --- |
| G-B1 | **Define errors out of existence.** Make operations idempotent: removing something already gone succeeds; applying the same input twice is a no-op. | Callers each handle "already exists" / "not found" in their own way. |
| G-B2 | **Mask or aggregate errors at one level.** Retries, backoff and reconnects live in one place (e.g. the client library), not in every caller. | The same retry block copied across modules. |
| G-B3 | **Wrap with context; never swallow.** Errors carry the identifiers of what failed and keep the cause. A deliberately ignored error has a comment saying why. | Discarded errors, log-and-continue, or error messages with no identifiers. |
| G-B4 | **Crash only on programmer errors.** Abort only at startup or on broken invariants; runtime failures follow the spec's recovery behaviour. | A crash or process exit in a request, sync or reconcile path. |
| G-B5 | **Few special cases.** Let the normal path handle edge cases (an empty list, a zero value) without extra branches. | Stacked "if empty" / "if first" branches. |

## C. Comments, names and obviousness

Applied at **Implement**; checked at AI **Review**.

| ID | Rule | Red flag |
| --- | --- | --- |
| G-C1 | **Write the interface comment first.** Every public type and function says what it does, its invariants, units and error behaviour, before the body is written. If the comment is hard to write, the design is wrong. | *Hard to describe*: the comment needs "and also…" or lists special cases. |
| G-C2 | **Comments say what the code can't:** why, invariants, units, references. Code that implements a spec rule cites it (e.g. `SPEC §8.5`). | *Comment repeats code*: `// increment i`. |
| G-C3 | **Interface comments describe use, not implementation.** | *Implementation contaminates interface*: a doc comment explaining internal data structures or threads. |
| G-C4 | **Precise, consistent names.** A concept has one name everywhere, matching the project glossary (the spec's domain terms). | *Vague name* (`data`, `info`, `mgr`, `handle`); *hard to pick a name* (usually a muddled design). |
| G-C5 | **Obvious code.** A reader understands a function without tracing other files. Avoid hidden control flow (callbacks registered far away, work started from getters). | *Nonobvious code*: the reviewer has to ask "what does this do?". |
| G-C6 | **Be consistent.** Follow the existing pattern in the module, even when you'd do it differently. Change a convention everywhere or nowhere. | Two styles of doing the same thing in one module. |

## D. Strategic programming

Applied throughout.

| ID | Rule |
| --- | --- |
| G-D1 | **Working code isn't enough.** Code that passes tests but makes the next change harder should not merge (the "tactical tornado" warning). Agents generating code quickly are tactical by default, so this applies to every generated change. |
| G-D2 | **Invest about 10–20% of each slice in design**, but only within the slice's scope. |
| G-D3 | **Design problems outside the slice** become an issue or an ADR draft, not a wider pull request. |
| G-D4 | **Leave code better than you found it**, in the files you are already changing. |

## Who enforces what

| Enforcer | Rules | When |
| --- | --- | --- |
| Machine (formatter, linter, tests) | Project language rules; parts of G-B3 and G-C2 where a lint rule exists | Locally before push; CI |
| AI reviewer | B, C, and A red flags visible in the diff | Review |
| Human reviewer | A (depth, boundaries, design it twice), D, spec fidelity | Plan and review |

When the same finding shows up in two reviews, the process's Learn stage turns it into an agent rule, or a lint rule if it can be automated ([constitution](/constitution.md) article 8).
