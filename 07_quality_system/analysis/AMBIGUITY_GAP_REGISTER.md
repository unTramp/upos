# UPOS-007 Ambiguity & Gap Register

**ID:** UPOS-07-AN-011  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-007 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 07 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-007 v1.0 decomposition/implementation/audit state at freeze time. It is not timeless normative truth. Current Quality semantics are owned by canonical Module 07 normative artifacts; `MODULE_07_TRACEABILITY.md` remains the canonical coverage artifact.


| ID | Issue | Module-07 resolution | Deferred owner | Severity | Status |
|---|---|---|---|---|---|
| G07-001 | Evidence vs Finding | Evidence supports evaluation; Finding is an attributable detected quality observation. | — | P0 | CLOSED |
| G07-002 | Evidence vs Verdict | Evidence is input; Verdict is Assessment conclusion. | — | P0 | CLOSED |
| G07-003 | Finding vs Verdict | Finding is issue/observation; Verdict integrates all required criterion evaluations. | — | P0 | CLOSED |
| G07-004 | Criterion vs Acceptance Criterion | Acceptance Criterion is an upstream governed criterion class; UPOS-007 evaluates it. | UPOS-01 | P1 | CLOSED |
| G07-005 | Criteria Set vs Source of Truth | Criteria Set is evaluable projection, never a second truth database. | UPOS-01 | P0 | CLOSED |
| G07-006 | Assessment vs Skill Invocation | Skill is procedure execution; Assessment is canonical quality evaluation artifact. | UPOS-003 | P0 | CLOSED |
| G07-007 | Assessment lifecycle vs Verdict | Lifecycle is OPEN/EVALUATING/COMPLETED/CANCELLED; Verdict separate. | — | P1 | CLOSED |
| G07-008 | Finding severity vs status | Severity consequence and lifecycle disposition are separate axes. | — | P1 | CLOSED |
| G07-009 | Finding severity vs confidence | No equivalence; confidence is not universal severity. | — | P1 | CLOSED |
| G07-010 | Review Result vs Assessment | Review Result = QualityAssessment with review assessment_type; no extra ID. | — | P0 | CLOSED |
| G07-011 | QA Result vs Assessment | QA Result = QualityAssessment with QA_VALIDATION; no extra ID. | — | P0 | CLOSED |
| G07-012 | Quality Gate vs Workflow gate placement | UPOS-007 owns semantics; UPOS-004 owns placement/timing. | UPOS-004 | P0 | CLOSED |
| G07-013 | Gate Result vs Workflow state | Gate result is quality evaluation, not Workflow state. | UPOS-004 | P0 | CLOSED |
| G07-014 | Quality PASS vs CI green | CI is evidence provider only; PASS requires criteria/sufficiency. | UPOS-006 | P0 | CLOSED |
| G07-015 | Quality PASS vs no findings | No findings does not prove criteria evaluated/satisfied. | — | P0 | CLOSED |
| G07-016 | Quality readiness vs mechanical mergeability | Separate owned states. | UPOS-006 | P0 | CLOSED |
| G07-017 | Quality readiness vs Merge Controller authority | Quality result does not grant authority. | UPOS-002 | P0 | CLOSED |
| G07-018 | Quality readiness vs permission | Quality result does not grant permission. | UPOS-010 | P0 | CLOSED |
| G07-019 | DoR vs Workflow entry condition | UPOS-007 evaluates quality readiness criteria; UPOS-004 owns entry orchestration. | UPOS-004 | P1 | CLOSED |
| G07-020 | DoD vs Workflow completion | Quality DoD result is not Workflow completion. | UPOS-004 | P0 | CLOSED |
| G07-021 | Security Review vs Security veto | Generic Quality can consume Security result; veto substance remains UPOS-010. | UPOS-010 | P0 | CLOSED |
| G07-022 | Waiver vs resolved Finding | WAIVED retains finding; RESOLVED requires correction + verification. | — | P0 | CLOSED |
| G07-023 | Waiver authority vs recording | UPOS-007 records; external authority authorizes. | UPOS-002/010 | P0 | CLOSED |
| G07-024 | Artifact staleness vs Evidence staleness | UPOS-006 emits artifact change; UPOS-007 assesses evidence applicability. | UPOS-006 | P1 | CLOSED |
| G07-025 | Context staleness vs Evidence staleness | UPOS-005 owns Context validity; UPOS-007 revalidates evidence assumptions. | UPOS-005 | P1 | CLOSED |
| G07-026 | Re-review vs rework | UPOS-004 routes rework; UPOS-007 creates a new review Assessment. | UPOS-004 | P1 | CLOSED |
| G07-027 | Delta review vs full re-review | Delta allowed only with exact change and preserved evidence applicability. | — | P1 | CLOSED |
| G07-028 | Self-check vs independent review | Self-check is evidence, not independent verification. | UPOS-002 | P0 | CLOSED |
| G07-029 | Quality provenance vs Observability trace | Quality owns semantic refs; UPOS-008 owns events/traces/metrics. | UPOS-008 | P1 | CLOSED |
| G07-030 | Quality failure vs Workflow failure | UPOS-007 returns quality condition; UPOS-004 chooses orchestration response. | UPOS-004 | P0 | CLOSED |

## Result

No unresolved P0/P1 Module-07 semantic gap remains at freeze.
