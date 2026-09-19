# Quality Assessment Standard

**ID:** UPOS-07-QAS-001  
**Type:** ASSESSMENT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/QUALITY_ASSESSMENT_TEMPLATE.md


## 1. Definition

A Quality Assessment is a bounded, attributable, immutable-on-completion evaluation of one exact target state against one Criteria Set/version using Evidence and Findings.

Every Assessment MUST have stable:

```text
quality_assessment_id
```

## 2. Assessment types

Canonical v1:

```text
DIFF_REVIEW
ARCHITECTURE_REVIEW
QA_VALIDATION
DOCUMENTATION_CONFORMANCE
ACCEPTANCE_CRITERIA_EVALUATION
MERGE_QUALITY_READINESS
RELEASE_QUALITY_READINESS
```

Security substantive assessment is not generic UPOS-007 ownership; external Security results may be referenced as evidence/gate inputs.

## 3. Assessment cycle kind

For future provenance/observability:

```text
FIRST_PASS
RE_REVIEW
RE_VALIDATION
DELTA_REVIEW
```

This is semantic metadata, not a KPI.

## 4. Minimum contract

```text
quality_assessment_id
assessment_contract_ref
assessment_contract_version
assessment_type
assessment_cycle_kind
assessment_state

task_id
workflow_instance_id
stage_id

target_type
target_ref
target_state_ref
base_revision_ref
head_revision_ref
commit_ref
diff_or_change_set_ref
integration_request_ref
artifact_version_ref

producer_role_ref
producer_agent_run_ref
skill_invocation_refs

context_bundle_id

quality_policy_ref
quality_policy_version
quality_criteria_set_id
criteria_set_version

criterion_evaluations
evidence_record_refs
finding_refs

independence_state
independence_basis_refs

evidence_sufficiency_summary

quality_verdict
known_limitations
open_unknowns

related_prior_assessment_id
relationship_to_prior

assessed_at
```

For engineering targets, `target_ref` MUST resolve to the applicable UPOS-006 engineering artifact identity appropriate to `target_type`, such as `engineering_change_id`, `repository_change_unit_id`, `integration_request_ref`, `commit_ref`, or revision identity as appropriate.

The exact-state fields bind the Assessment to the evaluated engineering state.

This resolution reuses UPOS-006 identities and does not add mandatory engineering fields to non-engineering targets.

## 5. Assessment operational state

```text
OPEN
EVALUATING
COMPLETED
CANCELLED
```

Verdict MUST NOT be encoded as lifecycle state.

A completed Assessment may have verdict `PASS`, `FAIL`, `BLOCKED`, or `INCONCLUSIVE`.

## 6. Criterion evaluation entry

Each criterion evaluation records:

```text
criterion_key
criterion_ref
applicability
applicability_rationale
evaluation_state
evidence_record_refs
sufficiency
finding_refs
exception_ref
limitations
```

## 7. Quality provenance chain

Assessment semantics support reconstructing:

```text
Task
→ Workflow Instance / Stage
→ Role / Agent Run
→ Skill Invocation
→ Context Bundle
→ exact engineering/artifact target
→ Criteria Set / Policy versions
→ Evidence Records
→ Findings
→ Quality Assessment / Verdict
→ Quality Gate Result
```

This is semantic provenance, not UPOS-008 event/trace semantics.

## 8. Future audit/control-plane questions

The semantic model MUST retain enough references to answer later, without defining UPOS-008 UI/metrics:

```text
Why did this exact target fail review?
Which criterion was violated?
What evidence supported PASS?
What exact revision/change set was reviewed?
Was required independence satisfied?
Which Context Bundle informed the verifier?
Which Findings were blocking?
Which Findings were waived and under what authority?
Why was QA inconclusive?
Did evidence become stale after target change/rebase?
Which Quality Gate prevented progression?
What changed between first review and re-review?
Which Quality Policy / Criteria Set versions applied?
```

## 9. Immutability

A `COMPLETED` Assessment is a historical snapshot.

Target/criteria/context changes produce a new Assessment or explicit revalidation relationship.

Do not mutate an old Assessment to make it appear it evaluated a later target.

## 10. Assessment relationship

Re-review/re-validation/delta review references the prior Assessment.

Typical:

```text
related_prior_assessment_id
relationship_to_prior =
  RE_REVIEW_OF
  RE_VALIDATION_OF
  DELTA_REVIEW_OF
  SUPERSEDES_FOR_CURRENT_TARGET
```

Historical prior Assessments remain auditable.

## 11. First-pass semantics

`FIRST_PASS` identifies the first required independent Assessment of the relevant assessment type for the target lineage before producer rework caused by that Assessment's findings.

UPOS-008 may later compute first-pass acceptance; UPOS-007 does not calculate the metric.

## 12. Quality Assessment != Skill Invocation

A Skill Invocation is procedure execution.

A Quality Assessment is the canonical evaluation artifact/result semantics.

A Skill may produce or contribute to an Assessment; the entities remain distinct.
