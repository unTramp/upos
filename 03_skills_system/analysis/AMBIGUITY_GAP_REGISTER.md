# UPOS-003 Ambiguity & Gap Register

**ID:** UPOS-03-AN-005  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


| ID | Issue | Module-03 resolution | Deferred owner | Status |
|---|---|---|---|---|
| G03-001 | Skill vs Workflow | Bounded reusable procedure remains Skill; cross-role order/gates/routing remain UPOS-004. | UPOS-004 | CLOSED |
| G03-002 | Skill vs Agent Process | Reusable procedure is extracted from old Agent `Process`; Agent keeps organizational invariants/interfaces. | UPOS-002 | CLOSED |
| G03-003 | Skill vs Context Assembly | Skill may request/organize context but retrieval/freshness/budget/memory remain UPOS-005. | UPOS-005 | CLOSED |
| G03-004 | Skill vs Quality Procedure | Skill-level procedure/criteria are allowed; evidence/verdict/gate semantics remain UPOS-007. | UPOS-007 | CLOSED |
| G03-005 | Skill vs Tool | Skill may require abstract capabilities; concrete tools/providers remain adapters. | UPOS-011 | CLOSED |
| G03-006 | Skill vs Permission | Skill declares capability requirement but cannot grant permission. | UPOS-010 | CLOSED |
| G03-007 | Skill vs Policy | Skill consumes policy and cannot redefine allowed/required/forbidden organization-wide behavior. | UPOS-004/06/07/10 | CLOSED |
| G03-008 | Skill vs Learning | Skill can create Learning Candidate or be evolution target; detection/promotion remain UPOS-009/01. | UPOS-009 + UPOS-01 | CLOSED |
| G03-009 | Skill vs project adapter | Universal Skill Contract uses abstract sources/tools and no project paths/providers. | UPOS-011 | CLOSED |
| G03-010 | Definition vs Invocation | Definition lifecycle/version is Module 03; invocation runtime state/event is deferred. | UPOS-004/08/schemas | CLOSED |
| G03-011 | Dependency vs sequencing | Dependency expresses capability relationship, not Workflow order. | UPOS-004 | CLOSED |
| G03-012 | prepare-release breadth | Bounded to preparation/readiness artifacts; deploy/release sequencing excluded. | UPOS-004/06/10 | CLOSED |
| G03-013 | implement-change breadth | Bounded to one approved Change Plan segment; feature lifecycle remains Workflow. | UPOS-004/06 | CLOSED |
| G03-014 | Schema/runtime representation | Machine form deferred to cross-cutting schemas/runtime; Markdown remains normative. | cross-cutting schemas/runtime | CLOSED |

## Result

No unresolved P0/P1 Module-03 semantic gap remains at v1.0 freeze.
