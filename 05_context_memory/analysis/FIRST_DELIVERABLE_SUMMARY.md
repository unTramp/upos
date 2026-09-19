# UPOS-005 First Deliverable Summary

**ID:** UPOS-05-AN-011  
**Type:** ANALYSIS / FIRST DELIVERABLE  
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


## 1. Scope
Execution-time Context & Memory semantics: requirements/requests, retrieval eligibility, assembly, budget, views, freshness, failures, temporary memory and governed project-memory access.

## 2. Non-scope
Truth/authority/workflow/Git/quality/telemetry/learning/security grants/provider bindings remain UPOS-01/02/04/06–11.

## 3. Ontology
`Knowledge != Context != Memory != Retrieval != Source Resolution != Context Bundle != Cache`.

## 4. Request → Bundle
`Requirements → Context Request → UPOS-01 resolution → permission/provider interfaces → eligible candidates → selection/representation/budget → immutable Context Bundle`.

## 5. Stable identity
`context_request_id`, `context_bundle_id`, `memory_item_id`; upstream identities are referenced, not re-owned.

## 6. Source resolution vs retrieval
UPOS-01 decides canonical owner/source universe; UPOS-005 retrieves/selects within that authority envelope.

## 7. Authority-aware retrieval
Authority/scope/version/permission/freshness eligibility precedes relevance and budget.

## 8. Bundle contract
Immutable, attributable, policy-versioned snapshot with Context Manifest, provenance, validity, budget accounting, exclusions, conflicts/unknowns and supersession link.

## 9. Budget
Optimize for minimum sufficient authoritative context; required material cannot be silently budget-dropped.

## 10. Compression
`EXACT / EXCERPT / DERIVED_SUMMARY / REFERENCE_ONLY`; summaries remain derived and provenance-linked.

## 11. Freshness
Freshness separate from authority/canonicality; material source/route changes trigger revalidation and possibly a new Bundle.

## 12. Context View
Role/Run/Stage/Skill projection over eligible material, with permissions and independence constraints.

## 13. Reviewer independence
Reviewer independently receives authoritative requirements and does not inherit Implementer scratch/private reasoning automatically.

## 14. Memory taxonomy
`RUN_WORKING_MEMORY`, `TASK_WORKING_MEMORY`, `RETRIEVAL_CACHE`, `GOVERNED_PROJECT_MEMORY_VIEW`.

## 15. Project-memory boundary
Governed Project Memory View is a retrieval/view interface over UPOS-01, not a new database of truth.

## 16. Memory write/promotion
Persisted items remain noncanonical unless they are references into governed knowledge. Promotion is UPOS-01/009.

## 17. Failure taxonomy
Explicit Context failures with degraded/blocked semantics; Workflow response remains UPOS-004.

## 18. Cross-module interfaces
Explicit provides/consumes/MUST NOT redefine for UPOS-01–04 and 06–11.

## 19. Ambiguity/gaps
28 boundary/gap items resolved; no open P0/P1.

## 20. Package tree
See `PROPOSED_PACKAGE_TREE.md`.

## 21. Implementation plan
See `IMPLEMENTATION_PLAN.md`.

## 22. Expected commits
11 coherent documentation commits are proposed; no giant commit is assumed.

## 23. Definition of Done
The directive's Module-05 DoD will be encoded canonically in `MODULE_05_DEFINITION_OF_DONE.md`.
