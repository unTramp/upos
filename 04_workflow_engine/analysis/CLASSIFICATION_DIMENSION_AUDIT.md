# Classification Dimension Audit

**ID:** UPOS-04-AN-005  
**Type:** ANALYSIS / CLASSIFICATION AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../CHANGE_CLASSIFICATION_STANDARD.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


| Dimension | Provenance | Source support / rationale |
|---|---|---|
| product semantics impact | TASK_DIRECTIVE_REFINEMENT | C2 feature / Product routing implies relevance but source does not name dimension explicitly |
| domain semantics impact | TASK_DIRECTIVE_REFINEMENT | C3 multiple bounded contexts + Domain ownership |
| architecture impact | SOURCE_DERIVED | C4 definition/examples |
| cross-module breadth | SOURCE_DERIVED | C3 examples |
| data/model migration impact | SOURCE_DERIVED | DB migration + destructive/prod data C5 |
| security/privacy impact | SOURCE_DERIVED | C5 examples + Security workflow |
| authorization impact | SOURCE_DERIVED | auth/authz C5 examples |
| production blast radius | TASK_DIRECTIVE_REFINEMENT | production migration/hotfix/release source support |
| irreversibility | SOURCE_DERIVED | destructive data / irreversible AI action |
| external API compatibility | SOURCE_DERIVED | API workflow backward compatibility/versioning |
| user-facing behavior impact | TASK_DIRECTIVE_REFINEMENT | feature/UI workflows imply participation depth |
| operational impact | SOURCE_DERIVED | hotfix/release workflows |
| deployment complexity | TASK_DIRECTIVE_REFINEMENT | migration/release orchestration |
| uncertainty / missing truth | SOURCE_DERIVED | missing/stale Source-of-Truth + reclassification rules |

No `NEW_PROPOSAL` dimension was required for v1.
