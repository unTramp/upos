# UPOS-005 Ambiguity & Gap Register

**ID:** UPOS-05-AN-008  
**Type:** ANALYSIS / GAP REGISTER  
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


| ID | Issue | Module-05 resolution | Deferred owner | Severity | Status |
|---|---|---|---|---|---|
| G05-001 | Context vs Knowledge | Knowledge remains UPOS-01; Context is execution-time selection. | UPOS-01 | P0 | CLOSED |
| G05-002 | Context vs Memory | Context is assembled per execution; Memory is retained execution support with explicit scope/lifetime. | — | P1 | CLOSED |
| G05-003 | Memory vs Project Knowledge | Governed Project Memory is a view over UPOS-01, not a second store. | UPOS-01 | P0 | CLOSED |
| G05-004 | Task Memory vs Workflow State | Task memory stores support material; Workflow state remains UPOS-004. | UPOS-004 | P0 | CLOSED |
| G05-005 | Context Requirement vs Skill Contract | Skill declares Source/Context needs; Module 05 resolves them. | UPOS-003 | P1 | CLOSED |
| G05-006 | Context Requirement vs Workflow Stage Contract | Stage declares need/timing; Module 05 assembles valid context. | UPOS-004 | P1 | CLOSED |
| G05-007 | Context Bundle vs Prompt | Bundle is provider-independent semantic package; prompt formatting is adapter/runtime concern. | UPOS-011/runtime | P1 | CLOSED |
| G05-008 | Context Bundle vs Source of Truth | Bundle snapshots sources; canonicality remains UPOS-01. | UPOS-01 | P0 | CLOSED |
| G05-009 | Retrieval vs Source Resolution | Source Resolution determines owner/canonical universe; retrieval locates eligible material. | UPOS-01 | P0 | CLOSED |
| G05-010 | Authority ranking vs relevance ranking | Authority eligibility precedes relevance; relevance cannot override authority. | UPOS-01 | P0 | CLOSED |
| G05-011 | Freshness vs canonicality | Freshness is execution applicability; canonicality/owner status remains upstream. | UPOS-01 | P1 | CLOSED |
| G05-012 | Stale vs superseded | STALE is Context freshness assessment; SUPERSEDED is consumed source lifecycle/status. | UPOS-01 | P1 | CLOSED |
| G05-013 | Summary vs canonical source | Summary is DERIVED_SUMMARY with provenance and never canonical by itself. | UPOS-01 | P0 | CLOSED |
| G05-014 | Cache vs Memory | Cache is retrieval optimization; working memory supports execution. | — | P1 | CLOSED |
| G05-015 | Cache vs Source | Cache preserves source identity/version and adds zero authority. | UPOS-01 | P0 | CLOSED |
| G05-016 | Context reuse vs stale reuse | Reuse requires revalidation of scope/source version/freshness/permissions. | — | P1 | CLOSED |
| G05-017 | Run memory vs Task memory | Run memory is ephemeral single-run; Task memory spans bounded Task execution. | — | P1 | CLOSED |
| G05-018 | Task memory vs cross-task knowledge | Task memory does not cross task boundary without governed reusable reference/promotion. | UPOS-01 | P0 | CLOSED |
| G05-019 | Context isolation vs Security permissions | Module 05 performs isolation/minimization using constraints returned by UPOS-010; it does not grant access. | UPOS-010 | P0 | CLOSED |
| G05-020 | Reviewer independence vs Implementer context | Reviewer gets independent authoritative Context View; producer notes are separately labeled. | UPOS-002/007 | P0 | CLOSED |
| G05-021 | Context invalidation vs Workflow reroute | UPOS-004 reroute/reclassify triggers Module-05 revalidation/reassembly; Module 05 does not route. | UPOS-004 | P1 | CLOSED |
| G05-022 | Context failure vs Workflow failure | Module 05 emits Context result/failure; UPOS-004 selects orchestration response. | UPOS-004 | P0 | CLOSED |
| G05-023 | Memory evolution vs Learning System | Memory observations become candidates; promotion/evolution remains UPOS-009/01. | UPOS-009/01 | P0 | CLOSED |
| G05-024 | Project Memory vs provider/model memory | Private provider/model memory is never canonical U-POS knowledge. | UPOS-01/011 | P0 | CLOSED |
| G05-025 | Bundle immutable vs validity changes | Bundle payload is immutable; later validity assessments do not mutate consumed content. | — | P1 | CLOSED |
| G05-026 | Required source exceeds budget | Cannot silently omit; use safe summarization/staged retrieval/split/block/escalate. | UPOS-004/011 | P0 | CLOSED |
| G05-027 | Source not found vs absence | Technical retrieval failure is not proof source does not exist. | UPOS-01/011 | P1 | CLOSED |
| G05-028 | Context policy version | Bundle records context policy/version for reproducibility; source versions remain separate. | — | P1 | CLOSED |

## Result

No unresolved P0/P1 Module-05 semantic gap remains before normative implementation.
