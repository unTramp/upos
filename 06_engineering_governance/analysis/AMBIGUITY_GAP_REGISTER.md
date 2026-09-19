# Module 06 Ambiguity & Gap Register

**ID:** UPOS-06-AN-010  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time analysis is found factually incorrect  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


| ID | Issue | Module-06 resolution | Deferred owner | Severity | Status |
|---|---|---|---|---|---|
| ENG-GAP-001 | Task vs Engineering Change | Engineering Change is repository realization referencing Task, never a competing Task. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-002 | Workflow Stage vs Repository Change Unit | Stage is orchestration; RCU is repository-scoped engineering unit. | UPOS-004 | P1 | RESOLVED |
| ENG-GAP-003 | Implementation Plan vs Engineering Change | Plan is consumed by Engineering Change; planning semantics remain Skill/Workflow governance. | UPOS-003/004 | P1 | RESOLVED |
| ENG-GAP-004 | Engineering Change vs Branch | Engineering Change may span repositories/branches; branch belongs to one RCU realization. | — | P1 | RESOLVED |
| ENG-GAP-005 | RCU vs Workspace | RCU is durable repository-scoped unit; Workspace is isolated mutable environment. | — | P1 | RESOLVED |
| ENG-GAP-006 | Workspace vs Agent Run | Workspace references Agent Run but is not an execution lifecycle. | UPOS-002 | P1 | RESOLVED |
| ENG-GAP-007 | Branch vs Workspace | Branch is VCS history/ref; Workspace is writable environment. | UPOS-011 realization | P1 | RESOLVED |
| ENG-GAP-008 | Atomic Commit vs small commit | Atomicity is semantic cohesion, not size. | — | P1 | RESOLVED |
| ENG-GAP-009 | Commit vs Integration Request | Commit is logical unit; IR is coherent deliverable/container. | — | P1 | RESOLVED |
| ENG-GAP-010 | Integration Request vs Workflow | IR is repository artifact/container, not orchestration. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-011 | IR lifecycle vs Quality state | IR lifecycle is mechanical only; Quality states/results external. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-012 | Engineering check vs Quality evidence | Module 06 binds checks to artifacts; UPOS-007 decides evidence sufficiency. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-013 | Mechanical mergeability vs Merge readiness | Mechanical state != Quality readiness. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-014 | Merge mechanics vs Merge authority | Mechanics Module 06; authority Module 02. | UPOS-002 | P0 | RESOLVED |
| ENG-GAP-015 | Merge authority vs Merge permission | Authority Module 02; capability grant Module 10. | UPOS-002/010 | P0 | RESOLVED |
| ENG-GAP-016 | History rewrite vs review validity | Module 06 emits artifact-change; UPOS-007 decides validity/re-review. | UPOS-007 | P1 | RESOLVED |
| ENG-GAP-017 | Engineering revert vs deployment rollback | Repository revert/backout only; deployment/data/business rollback external. | UPOS-004/operations/data | P0 | RESOLVED |
| ENG-GAP-018 | Repository collision vs Workflow dependency | Module 06 detects/reports engineering constraints; UPOS-004 sequences. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-019 | File collision vs semantic collision | Separate taxonomy; semantic collision may exist without file overlap. | — | P1 | RESOLVED |
| ENG-GAP-020 | Multi-repository engineering vs Workflow orchestration | RCU mechanics Module 06; overall order Module 04. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-021 | IR evidence container vs Quality evidence ownership | IR holds refs; UPOS-007 owns evidence/verdict semantics. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-022 | Engineering provenance vs Observability trace | Artifact relationships Module 06; events/traces Module 08. | UPOS-008 | P0 | RESOLVED |
| ENG-GAP-023 | Context provenance vs engineering provenance | Engineering provenance reuses frozen `context_request_id` / `context_bundle_id`; Context Manifest/source provenance remains UPOS-005. | UPOS-005 | P1-INTERFACE | RESOLVED |
| ENG-GAP-024 | Reviewer Context vs review artifact | Review artifact remains Module 06; Reviewer Context is independent UPOS-005 Context Request/Bundle; no `context_view_id` added. | UPOS-005 | P1-INTERFACE | RESOLVED |
| ENG-GAP-025 | Protected branch policy vs permission grants | Engineering protection requirement Module 06; grants Module 10. | UPOS-010/011 | P0 | RESOLVED |
| ENG-GAP-026 | Git semantics vs provider | Git-like VCS semantics normative; provider/API/bindings abstract. | UPOS-011 | P1 | RESOLVED |

> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Result

```text
UNRESOLVED INTERNAL P0/P1 MODULE-06 GAPS = 0
```

The two prior UPOS-005 interface gaps are resolved against FROZEN UPOS-005 v1.0.

No unresolved P0/P1 internal or interface gap remains for Module 06 v1.0 freeze.
