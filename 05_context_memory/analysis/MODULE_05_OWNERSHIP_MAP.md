# Module 05 Ownership Map

**ID:** UPOS-05-AN-002  
**Type:** ANALYSIS / OWNERSHIP MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Module 05 owns

```text
Context Requirement / Context Request semantics
authority-aware retrieval orchestration
source eligibility for execution context
relevance selection after authority eligibility
Context assembly
required vs optional treatment
representation / summarization safety
context budget / prioritization / overflow
Context Bundle / Context Manifest
context freshness / validity / invalidation / reassembly
Role/Run/Skill/Stage Context Views and isolation
context reuse
Run Working Memory
Task Working Memory
Retrieval Cache semantics
Governed Project Memory View interface
memory read/write/lifetime/invalidation
memory-to-knowledge promotion interface
cross-task/cross-project isolation semantics
Context/Memory failure semantics
Module-05 lifecycle/versioning semantics
```

## Module 05 does not own

| Concern | Canonical owner |
|---|---|
| project truth, fact scopes, canonical owner/source, normative conflicts, promotion | UPOS-01 |
| Role authority, Agent identity, SoD, handoff authority, Human Governance | UPOS-002 |
| Skill procedure / Skill evaluation | UPOS-003 |
| Workflow routing/state/stage order/retry-rework orchestration | UPOS-004 |
| Git/branch/commit/PR/merge mechanics | UPOS-006 |
| Review/QA evidence/verdict/gates | UPOS-007 |
| event/trace/metrics/dashboard/telemetry retention | UPOS-008 |
| organizational learning detection/promotion | UPOS-009 + UPOS-01 |
| access grants/secrets/security/protected-data policy | UPOS-010 |
| physical paths/providers/search/storage/model bindings | UPOS-011 |

## Boundary test

A rule belongs here when the central question is:

```text
What valid information should this bounded execution receive?
How is eligible information found, selected, represented, budgeted,
freshness-checked, isolated, and retained temporarily?
```

It does not belong here when the central question is:

```text
Which claim is project truth?
Who may decide it?
When does the Workflow transition?
What does QA PASS mean?
Who may read a secret?
Which vector database/search provider/path is used?
```
