# Quality Readiness

**ID:** UPOS-07-QRY-001  
**Type:** QUALITY READINESS STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_ASSESSMENT_STANDARD.md, QUALITY_VERDICT_STANDARD.md


## 1. Definition

Quality Readiness means:

> sufficient applicable Quality evidence exists, required criteria are acceptably evaluated, and no unresolved Quality condition prevents the governed action from the Quality System perspective.

Canonical values:

```text
READY
NOT_READY
BLOCKED
INCONCLUSIVE
```

Quality Readiness is a scoped projection of a completed `QualityAssessment` verdict for a named governed action or transition.

It is not a separate top-level entity or independent lifecycle.

## 2. Verdict → Readiness projection

For Assessment types that normatively represent Quality Readiness, including at minimum:

```text
MERGE_QUALITY_READINESS
RELEASE_QUALITY_READINESS
```

and any other governed Assessment scope explicitly designated as a Quality Readiness assessment, a completed Assessment projects:

```text
PASS
→ READY

FAIL
→ NOT_READY

BLOCKED
→ BLOCKED

INCONCLUSIVE
→ INCONCLUSIVE
```

This projection reuses the Assessment's existing `quality_assessment_id`.

UPOS-007 v1 deliberately does **not** create:

```text
quality_readiness_id
QualityReadiness entity
second independent readiness lifecycle
```

The projection does not change the meaning of the underlying Quality Verdict.

## 3. Scoped readiness

Readiness MUST name its scope.

Examples:

```text
QUALITY_READY_FOR_MERGE
QUALITY_READY_FOR_RELEASE
QUALITY_READY_FOR_WORKFLOW_TRANSITION
```

In v1 this is represented by Assessment type/scope, not a new global `quality_readiness_id`.

## 4. Merge-quality readiness

`MERGE_QUALITY_READINESS` is a Quality Assessment type.

It may consume:

- required review Assessment results;
- required QA Assessment results;
- evidence sufficiency/freshness;
- open blocking Findings;
- documentation/architecture Quality results;
- external Security/Human references where policy requires them.

It does not inspect Git mechanics beyond UPOS-006-provided exact target/mechanical state references.

## 5. Merge ownership matrix

```text
Mechanical mergeability
→ UPOS-006

Quality readiness
→ UPOS-007

Merge Controller authority
→ UPOS-002

Workflow position
→ UPOS-004

Permission / protected action
→ UPOS-010
```

No single module owns the total merge decision.

## 6. Critical separations

```text
QUALITY_READY
!= MECHANICALLY_MERGEABLE
!= AUTHORIZED_TO_MERGE
!= PERMITTED_TO_MERGE
```

A `PASS` Quality Assessment or projected `READY` result does not by itself authorize, permit, mechanically enable, or schedule merge.

## 7. SKL-ASSESS-MERGE-READINESS boundary

```text
Skill procedure                     → UPOS-003
mechanical/artifact data            → UPOS-006
quality evidence/readiness meaning  → UPOS-007
Merge Controller authority          → UPOS-002
permission                          → UPOS-010
```

## 8. Release Quality readiness

`RELEASE_QUALITY_READINESS` evaluates Quality of the release candidate state.

Release orchestration remains UPOS-004; repository release artifacts remain UPOS-006; deployment/production authorization remains external.
