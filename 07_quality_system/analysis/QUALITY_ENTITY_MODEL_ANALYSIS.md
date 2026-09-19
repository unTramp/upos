# Quality Entity Model Analysis

**ID:** UPOS-07-AN-004  
**Type:** ANALYSIS / ENTITY MODEL  
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


## Adopted entities

```text
QualityCriteriaSet
EvidenceRecord
Finding
QualityAssessment
QualityGate
QualityGateResult
QualityException
```

## Stable identities

```text
quality_criteria_set_id
evidence_record_id
finding_id
quality_assessment_id
quality_gate_id
quality_gate_result_id
quality_exception_id
```

## Deliberately not introduced

```text
review_result_id
qa_result_id
quality_readiness_id
global duplicated criterion_id
```

## Rationale

Review/QA/readiness are projections of a common Assessment lifecycle/provenance.

Criterion truth already has upstream requirement identity; Criteria Set adds bounded evaluable projection and `criterion_key`.

This is sufficient for provenance without identity explosion.
