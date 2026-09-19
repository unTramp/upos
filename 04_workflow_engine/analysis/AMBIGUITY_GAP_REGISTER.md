# UPOS-004 Ambiguity & Gap Register

**ID:** UPOS-04-AN-006  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


| ID | Issue | Module-04 resolution | Deferred owner | Status |
|---|---|---|---|---|
| G04-001 | UI/API/DB/Security workflow overlap | Normalize as Concern Profiles, not competing base workflows. | — | CLOSED |
| G04-002 | Micro change as work type vs class | Micro is C0 classification depth; primary Work Type defaults to GENERIC_CHANGE. | — | CLOSED |
| G04-003 | Architecture as workflow vs concern | Architecture becomes a Concern Profile; durable architecture change imposes C4 minimum. | UPOS-002/01 for authority/decision | CLOSED |
| G04-004 | Skill procedure duplication | Workflow references stable Skill IDs/versions only. | UPOS-003 | CLOSED |
| G04-005 | Gate semantics leakage | Workflow says when gate is required; UPOS-007 defines evidence/verdict meaning. | UPOS-007 | CLOSED |
| G04-006 | Human approval semantics | Workflow requires approval reference; authority/enforcement external. | UPOS-002/010 | CLOSED |
| G04-007 | Context ownership | Workflow declares Source Classes/context need; retrieval/budget/memory external. | UPOS-005/01 | CLOSED |
| G04-008 | Git/merge mechanics | Workflow may include readiness/merge/release stage references but Git mechanics remain external. | UPOS-006 | CLOSED |
| G04-009 | Retry threshold | Universal rule is bounded retry; exact numeric budgets project-specific. | UPOS-011/project policy | CLOSED |
| G04-010 | Task lifecycle source too code-centric | Normalize universal Task states; review/QA/readiness become stage projections. | — | CLOSED |
| G04-011 | Workflow Instance vs telemetry runtime | Module 04 owns semantic attribution/state; persistence/events external. | UPOS-008/runtime/schemas | CLOSED |
| G04-012 | Parallelism vs shared-file collisions | Workflow owns dependency/parallel orchestration; collision/worktree mechanics external. | UPOS-006 | CLOSED |
| G04-013 | Security classification meaning | UPOS-004 consumes Security sensitivity signal; does not redefine security truth. | UPOS-010 | CLOSED |
| G04-014 | Release deploy stage without deploy Skill | Workflow may orchestrate external protected operational action by interface; tool/permission binding external. | UPOS-010/011 | CLOSED |

## Result

No unresolved P0/P1 Module-04 semantic gap remains at v1.0 freeze.
