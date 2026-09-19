# Evidence Standard

**ID:** UPOS-07-EVS-001  
**Type:** EVIDENCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/EVIDENCE_RECORD_TEMPLATE.md


## 1. Evidence Record

Every durable evidence item used materially in Quality evaluation MUST be attributable through a stable:

```text
evidence_record_id
```

Minimum contract:

```text
evidence_record_id
evidence_type

producer_role_ref
producer_agent_run_ref
skill_invocation_ref

target_type
target_ref
target_state_ref
base_revision_ref
head_revision_ref
commit_ref
diff_or_change_set_ref
integration_request_ref
artifact_version_ref

source_artifact_ref
engineering_check_ref
external_result_ref

context_bundle_id

created_at
procedure_or_method_ref
observed_result

criterion_refs
applicability_scope
evidence_applicability_state
provenance

reliability_state
reliability_limitations
freshness_state
limitations
```

Non-applicable fields are explicit `N/A`.

## 2. Evidence types

Canonical v1 provider-neutral types:

```text
AUTOMATED_CHECK
TEST_RESULT
STATIC_ANALYSIS
MANUAL_REVIEW
QA_OBSERVATION
REPRODUCTION_RESULT
REGRESSION_TEST
DOCUMENTATION_CHECK
ARCHITECTURE_REVIEW_RESULT
SECURITY_RESULT_REFERENCE
HUMAN_DECISION_REFERENCE
```

Governed extensions are allowed.

Tool/vendor names are not evidence types.

## 3. Evidence is not truth

Evidence supports an evaluation.

It does not become Product/Domain/Architecture truth or a Verdict by itself.

## 4. Exact target binding

Evidence MUST identify the exact artifact state actually evaluated.

Evidence against revision A MUST NOT silently satisfy a criterion against revision B.

For engineering targets, `target_ref` MUST resolve to the applicable UPOS-006 engineering artifact identity appropriate to `target_type`, such as `engineering_change_id`, `repository_change_unit_id`, `integration_request_ref`, `commit_ref`, or revision identity as appropriate.

The explicit exact-state fields bind the Evidence Record to the evaluated engineering state.

UPOS-007 does not duplicate the UPOS-006 provenance model.

## 5. Automated check boundary

UPOS-006 owns execution/reference mechanics.

Example:

```text
UPOS-006:
check_ref X executed against commit abc, exit/result success

UPOS-007:
is check_ref X applicable, fresh and sufficient
for criterion Y on this Assessment target?
```

Configured checks passing proves only what those checks validly cover.

## 6. Manual evidence

Manual evidence is allowed when appropriate and MUST state:

```text
who
target
method/procedure/reference
observed result
when
limitations
```

`looks good` alone is insufficient for a material required criterion.

## 7. Reliability

Canonical evidence reliability states:

```text
RELIABLE_FOR_CLAIM
QUALIFIED
UNRELIABLE
UNKNOWN
```

A flaky/unreliable result may remain evidence but MUST NOT be counted as strong sufficient PASS evidence without qualification.

## 8. No hidden reasoning dependency

Evidence records preserve attributable observations/results/rationale.

They MUST NOT require storage of hidden chain-of-thought.

## 9. Evidence applicability states

For the current Assessment/criterion relation:

```text
APPLICABLE
NOT_APPLICABLE
UNRESOLVED
```

A captured Evidence Record may exist while being `NOT_APPLICABLE` to the current criterion/target.

Applicability is separate from freshness and sufficiency.
