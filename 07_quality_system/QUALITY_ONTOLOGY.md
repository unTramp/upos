# Quality Ontology

**ID:** UPOS-07-QON-001  
**Type:** ONTOLOGY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Entities

### QUALITY CRITERION

One evaluable requirement/condition sourced from governed authority or explicitly marked advisory guidance.

### QUALITY CRITERIA SET

A versioned evaluable projection that selects criteria for a bounded purpose/target class.

It references requirement truth; it does not replace it.

### EVIDENCE RECORD

An attributable record of observed/check/review/test/manual/external support tied to a target state.

### FINDING

An attributable quality observation representing nonconformance, defect, risk, missing evidence, ambiguity, or advisory improvement.

### QUALITY ASSESSMENT

A bounded evaluation snapshot tying:

```text
target
+ criteria
+ evidence
+ findings
+ criterion evaluations
+ independence
+ limitations
→ verdict
```

### QUALITY VERDICT

`PASS | FAIL | BLOCKED | INCONCLUSIVE`.

### QUALITY GATE

A reusable governed contract defining what Quality conditions must hold for a referenced orchestration checkpoint.

### QUALITY GATE RESULT

One attributable evaluation of one Gate/version against one exact target state.

### QUALITY READINESS

Quality-only readiness for a governed action such as merge/release.

### QUALITY EXCEPTION

A recorded externally authorized exception/waiver affecting a criterion/finding/gate for bounded scope.

## 2. Result specializations

Review Result and QA Result are not separate top-level identity entities.

```text
DIFF_REVIEW
ARCHITECTURE_REVIEW
QA_VALIDATION
DOCUMENTATION_CONFORMANCE
ACCEPTANCE_CRITERIA_EVALUATION
MERGE_QUALITY_READINESS
RELEASE_QUALITY_READINESS
```

are `assessment_type` values of `QualityAssessment`.

Security substantive evaluation/veto remains external to UPOS-007.

## 3. Criterion addressing

UPOS-007 avoids inventing a global duplicate `criterion_id`.

Each criterion entry is addressable by:

```text
quality_criteria_set_id
criteria_set_version
criterion_key
criterion_ref
```

`criterion_ref` points to authoritative requirement/policy/decision/acceptance-criterion identity where available.

## 4. Target descriptor

Every Quality entity that evaluates applicability MUST carry an exact target descriptor.

Minimum semantic fields:

```text
target_type
target_ref
target_state_ref

base_revision_ref        where applicable
head_revision_ref        where applicable
commit_ref               where applicable
diff_or_change_set_ref    where applicable
integration_request_ref   where applicable
artifact_version_ref      where applicable
```

Non-applicable fields are explicit `N/A`.

## 5. Engineering-target provenance resolution

For engineering targets:

```text
target_ref
```

MUST resolve to the applicable UPOS-006 engineering artifact identity appropriate to `target_type`, such as:

```text
engineering_change_id
repository_change_unit_id
integration_request_ref
commit_ref
revision_ref
```

where applicable.

Exact-state fields such as base/head/commit/change-set/revision references then bind the evaluated state.

This is resolution to upstream identities, not a second Quality-owned engineering identity model.

## 6. No identity explosion

No new global ID is created merely because a projection/view exists.

Examples:

- Review Result → `quality_assessment_id`
- QA Result → `quality_assessment_id`
- Quality readiness → Assessment/Gate result fields
- criterion → authoritative `criterion_ref` + set-local `criterion_key`

New identity requires independent lifecycle/provenance need.
