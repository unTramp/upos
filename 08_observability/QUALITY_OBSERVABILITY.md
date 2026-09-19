# Quality Observability

**ID:** UPOS-08-QOB-001  
**Type:** QUALITY OBSERVABILITY INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Boundary

UPOS-007 owns:

```text
Quality Criteria
Evidence Record / Evidence Binding interpretation
Finding
Quality Assessment / Verdict
Quality Gate / Gate Result
Quality Exception
Quality Readiness
```

UPOS-008 owns measurements/projections over those governed semantics.

## 2. Quality references

Where applicable, Observability consumes:

```text
quality_assessment_id
assessment_type
assessment_cycle_kind
quality_verdict
assessed_at

evidence_record_id
finding_id
quality_gate_id
quality_gate_result_id
quality_exception_id
```

It MUST NOT invent alternate review/QA identities.

## 3. First-pass acceptance

`FIRST_PASS` comes from UPOS-007 `assessment_cycle_kind`.

Observability may define a rate over it; it does not infer first pass from comment count or chronology.

## 4. Review cycle count

Review-cycle metrics MUST use governed cycle kinds:

```text
FIRST_PASS
RE_REVIEW
DELTA_REVIEW
RE_VALIDATION
```

They MUST NOT use comment count, commit count, or arbitrary reviewer messages as cycle count.

## 5. Historical as-of semantics

Reconciled UPOS-007 completed Assessments are interpreted `as of assessed_at`.

Observability metrics over historical verdicts/findings/exceptions MUST respect that temporal snapshot and MUST NOT reinterpret an old Assessment using a later Finding/Exception current status.

## 6. Evidence stale/insufficient metrics

Where a metric counts stale/insufficient evidence, it MUST use UPOS-007 Assessment-local evidence interpretation/bindings and applicable sufficiency semantics.

It MUST NOT assign its own freshness or reliability judgement to an Evidence Record.

## 7. Gate metrics

Gate success/failure observations consume UPOS-007 Gate Result semantics.

```text
METRIC != GATE VERDICT
```

A dashboard color or ratio cannot redefine what `SATISFIED`, `NOT_SATISFIED`, `BLOCKED`, or `INCONCLUSIVE` means.

## 8. Quality timelines

Quality timelines MAY correlate:

```text
exact engineering target
→ independent Assessment start span
→ assessed_at
→ Findings
→ rework owner event
→ re-review Assessment
→ Gate Result
```

Causation links must be explicit/governed; chronological adjacency is insufficient.

## 9. Finding counts

Finding count by severity/category is descriptive.

It is NOT a universal measure of Agent quality because counts depend on:

- risk;
- scope;
- review depth;
- criteria;
- reviewer behavior;
- sample size.

## 10. Escaped defect dependency

A future escaped-defect metric requires an externally owned post-acceptance defect/incident attribution interface.

UPOS-008 MUST NOT create Incident/Defect ontology merely to compute this metric.

Until such source exists, escaped-defect metrics are `DEFERRED/CONDITIONAL`.
