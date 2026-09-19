# Quality Gate Standard

**ID:** UPOS-07-QGS-001  
**Type:** QUALITY GATE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/QUALITY_GATE_TEMPLATE.md, templates/QUALITY_GATE_RESULT_TEMPLATE.md, EVIDENCE_SUFFICIENCY_AND_FRESHNESS.md


## 1. Gate definition

A Quality Gate is a reusable, governed, versioned Quality evaluation contract referenced by Workflow.

UPOS-004 owns placement/timing.

UPOS-007 owns what satisfies the Quality Gate.

## 2. Stable identities

Gate Definition:

```text
quality_gate_id
```

Gate evaluation:

```text
quality_gate_result_id
```

## 3. Gate Definition contract

```text
quality_gate_id
name
version
status
purpose

quality_policy_ref
quality_policy_version

applicability_conditions
target_types

required_criteria_set_refs
required_assessment_types
required_evidence_classes
required_independence_conditions

acceptable_assessment_verdicts
blocking_conditions
external_gate_refs

exception_policy_ref

supersedes
replacement
```

## 4. Gate Result contract

```text
quality_gate_result_id
quality_gate_id
quality_gate_version

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

quality_policy_ref
quality_policy_version

assessment_refs
evidence_record_refs
finding_refs
quality_exception_refs
external_gate_result_refs

sufficiency_result
gate_result
open_limitations
open_unknowns

evaluated_by_role_ref
evaluated_by_agent_run_ref
evaluated_at
```

The exact-target fields reuse the universal `QUALITY_ONTOLOGY.md` target descriptor.

Non-applicable exact-target fields are explicitly:

```text
N/A
```

For engineering targets, target/revision identities resolve to UPOS-006-owned engineering artifacts; UPOS-007 does not create a second engineering identity system.

## 5. Gate sufficiency result

`QualityGateResult.sufficiency_result` reuses the canonical UPOS-007 sufficiency vocabulary from `EVIDENCE_SUFFICIENCY_AND_FRESHNESS.md`:

```text
SUFFICIENT
INSUFFICIENT
NOT_APPLICABLE
UNKNOWN
```

```text
sufficiency_result
!=
gate_result
```

Meaning:

```text
sufficiency_result
= whether the applicable evidence/evaluations are sufficient
  to support the Gate conclusion

gate_result
= the actual result of evaluating the Quality Gate
```

`SUFFICIENT` does not itself mean `SATISFIED`.

`SATISFIED` does not replace the requirement to record sufficiency.

## 6. Gate Result values

```text
SATISFIED
NOT_SATISFIED
BLOCKED
INCONCLUSIVE
```

These are not Workflow states.

## 7. Meaning

### SATISFIED
All required Gate Quality conditions are currently satisfied for the exact target.

### NOT_SATISFIED
One or more required Quality conditions are demonstrably unsatisfied.

### BLOCKED
Gate cannot be evaluated/satisfied due to missing prerequisite/access/context/external result.

### INCONCLUSIVE
Evaluation exists but evidence is insufficient/ambiguous to support satisfied/not-satisfied.

## 8. External gates

Security approval, Human Governance approval, permission grants and other external decisions are references.

UPOS-007 may require them but MUST NOT redefine their substantive meaning.

## 9. Gate placement invariant

```text
QUALITY_GATE_PLACEMENT != QUALITY_GATE_SEMANTICS
```
