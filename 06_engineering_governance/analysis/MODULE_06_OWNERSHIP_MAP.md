# Module 06 Ownership Map

**ID:** UPOS-06-AN-002  
**Type:** ANALYSIS / OWNERSHIP MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Module 06 owns

```text
Engineering Change
Repository Change Unit
Workspace isolation/lifecycle
Change Branch semantics
atomic commit/history integrity
Commit provenance
Integration Request mechanics/lifecycle
engineering check artifact binding
collision/concurrency constraints
multi-repository engineering mechanics
mechanical mergeability
Merge Operation mechanics
repository Revert/Backout
engineering provenance
engineering failure conditions
engineering artifact staleness
```

## Module 06 consumes without owning

| Interface | Owner |
|---|---|
| project truth, canonical docs, decisions | UPOS-01 |
| Role, Agent Run, authority, SoD, Merge Controller | UPOS-002 |
| Skill procedure/Skill Invocation semantics | UPOS-003 |
| Task, Workflow Instance, Stage, routing, rework orchestration | UPOS-004 |
| Context Bundle/View/provenance/freshness | UPOS-005 — pending |
| review/QA findings, evidence sufficiency, readiness verdict | UPOS-007 |
| events/traces/metrics/dashboard | UPOS-008 |
| organizational learning/promotion | UPOS-009 |
| permissions/protected actions/secrets | UPOS-010 |
| providers, paths, commands, naming, concrete policies | UPOS-011 |

## Boundary test

If the question is:

> Which repository artifact changed, where, from what base, by which bounded engineering unit, in which workspace/branch/commit/Integration Request, and how was it mechanically integrated/reverted?

→ UPOS-006.

If the question is:

> Should the work run now, who is authorized, is it correct, which Context is valid, may it be merged, or which provider command performs it?

→ another owning module.
