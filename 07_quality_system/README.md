# UPOS-007 — Quality System

**ID:** UPOS-07-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01–06 frozen baselines, frozen master design source


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-007 is the canonical U-POS owner for independently evaluating the quality of an exact artifact/change state against applicable governed criteria using attributable evidence.

It answers:

> Does this exact target state satisfy the applicable governed quality criteria, with sufficient fresh evidence and required independence, and what does the resulting quality verdict/gate/readiness mean?

It does **not** answer what the product should mean, when a Workflow stage occurs, who has authority to approve/merge, how Git/CI executes, how Context is retrieved, or whether Security grants/vetoes an action.

## 1. Fundamental ontology

```text
QUALITY CRITERION
= one evaluable governed requirement/condition

QUALITY CRITERIA SET
= versioned evaluable projection of applicable criteria

EVIDENCE RECORD
= attributable support captured for evaluation

FINDING
= attributable quality observation/nonconformance/risk/gap/advice

QUALITY ASSESSMENT
= bounded immutable evaluation snapshot of one exact target state

QUALITY VERDICT
= scoped result of a completed Assessment

QUALITY GATE
= reusable versioned quality evaluation contract

QUALITY GATE RESULT
= attributable evaluation of one Gate for one exact target state

QUALITY READINESS
= quality-only readiness judgment for a governed action/transition

QUALITY EXCEPTION
= attributable externally authorized exception/waiver reference
```

These concepts MUST NOT be used interchangeably.

## 2. Stable semantic identities

UPOS-007 owns:

```text
quality_criteria_set_id
quality_assessment_id
evidence_record_id
finding_id
quality_gate_id
quality_gate_result_id
quality_exception_id
```

UPOS-007 deliberately does **not** introduce:

```text
review_result_id
qa_result_id
quality_readiness_id
criterion_id as a duplicate global requirement identity
```

Review/QA/readiness are specialized Assessment semantics.

A criterion is addressed through:

```text
authoritative criterion_ref
+
quality_criteria_set_id
+
criterion_key
```

This preserves upstream requirement identity and avoids a second requirements database.

## 3. Critical invariants

```text
EVIDENCE != VERDICT
FINDING != VERDICT
CI_GREEN != QUALITY_PASS
NO_FINDINGS != PROOF_OF_CORRECTNESS
REVIEW_PASS != MERGE_AUTHORITY
QUALITY_READY != MECHANICALLY_MERGEABLE
QUALITY_READY != PERMISSION_TO_MERGE
QUALITY_GATE_PLACEMENT != QUALITY_GATE_SEMANTICS
```

Also:

```text
PASS
= PASS only for the exact Assessment target, scope, criteria and policy version.
```

## 4. Exact target rule

Every Assessment, Evidence applicability decision, and Gate Result MUST identify an exact target state.

For engineering targets, ambiguous labels such as:

```text
current branch
latest PR
the change
```

are insufficient without stable repository/revision references from UPOS-006.

## 5. Quality flow

```text
UPOS-01 authoritative requirements/decisions
↓
Quality Policy + Criteria Set
↓
exact target state
↓
independent Context refs from UPOS-005
↓
Evidence Records
↓
criterion applicability/evaluation
↓
Findings
↓
Quality Assessment
↓
Quality Verdict
↓
Quality Gate Result
↓
UPOS-004 orchestration consumes result
↓
Quality readiness reference
↓
UPOS-002 / 006 / 010 merge boundary
```

## 6. Ownership boundary

```text
canonical truth / requirement meaning      → UPOS-01
Role/Reviewer/QA/Merge authority           → UPOS-002
verification Skill procedure               → UPOS-003
gate placement / rework routing            → UPOS-004
Reviewer/QA Context                         → UPOS-005
Git/CI execution / artifact mechanics      → UPOS-006
Quality criteria/evidence/finding/verdict  → UPOS-007
events/metrics/traces/dashboard            → UPOS-008
learning/policy improvement promotion      → UPOS-009 + UPOS-01
Security authority/permissions/veto        → UPOS-010
provider/project commands/thresholds       → UPOS-011 + governed project docs
```

## 7. Read order

1. `QUALITY_OPERATING_MODEL.md`
2. `QUALITY_ONTOLOGY.md`
3. `QUALITY_POLICY_STANDARD.md`
4. `QUALITY_CRITERIA_STANDARD.md`
5. `EVIDENCE_STANDARD.md`
6. `EVIDENCE_SUFFICIENCY_AND_FRESHNESS.md`
7. `FINDING_STANDARD.md`
8. `QUALITY_ASSESSMENT_STANDARD.md`
9. `QUALITY_VERDICT_STANDARD.md`
10. `REVIEW_RESULT_STANDARD.md`
11. `QA_RESULT_STANDARD.md`
12. `ACCEPTANCE_CRITERIA_EVALUATION.md`
13. `QUALITY_GATE_STANDARD.md`
14. `DEFINITION_OF_READY_AND_DONE.md`
15. `QUALITY_READINESS.md`
16. `QUALITY_EXCEPTION_AND_WAIVER.md`
17. `INDEPENDENT_VERIFICATION.md`
18. `QUALITY_FAILURE_MODEL.md`
19. `QUALITY_LIFECYCLE_AND_VERSIONING.md`
20. `CROSS_MODULE_INTERFACES.md`
21. `MODULE_07_TRACEABILITY.md`
