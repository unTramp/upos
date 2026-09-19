# Quality Metrics

**ID:** UPOS-08-QUA-SET-001  
**Type:** METRIC DEFINITIONS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability

All Quality states/semantics are consumed from UPOS-007.

## OBS-MET-QLT-001 — first_pass_acceptance_rate

**Disposition:** `CANONICAL_V1`

```text
definition: Rate of completed required FIRST_PASS Quality Assessments that PASS.
measurement_type: RATE
source: UPOS-007 completed Quality Assessments
population: completed applicable Assessments in selected assessment_type/cohort with assessment_cycle_kind=FIRST_PASS
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: numerator PASS FIRST_PASS Assessments / denominator terminal evaluative FIRST_PASS Assessments
dimensions: project, Change Class, Workflow, assessment_type, Role, Agent Definition/version, Skill/version
unknown handling: source gap → INCOMPLETE; denominator 0 → NO_DATA
limitations: Not an Agent score; depends on risk, criteria and review scope.
```

## OBS-MET-QLT-002 — quality_assessment_cycle_count

**Disposition:** `CANONICAL_V1`

```text
definition: Count governed Quality Assessment cycles for one target lineage/change cohort.
measurement_type: COUNTER
source: UPOS-007 assessment_cycle_kind and prior/supporting relations
population: selected exact target lineage/change cohort
window: TARGET_LINEAGE / cohort
formula: count(FIRST_PASS, RE_REVIEW, DELTA_REVIEW, RE_VALIDATION Assessments in scope)
dimensions: project, assessment_type, Change Class, Workflow, cycle kind
unknown handling: broken lineage refs → INCOMPLETE
limitations: Comment count and commit count are not review cycles.
```

## OBS-MET-QLT-003 — quality_gate_not_satisfied_rate

**Disposition:** `CANONICAL_V1`

```text
definition: Rate of evaluated Quality Gate Results whose governed result is NOT_SATISFIED.
measurement_type: RATE
source: UPOS-007 quality_gate_result_id results
population: evaluated Gate Results in selected gate/version/cohort
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: NOT_SATISFIED / all evaluated SATISFIED+NOT_SATISFIED+BLOCKED+INCONCLUSIVE results
dimensions: project, quality_gate_id/version, Change Class, Workflow
unknown handling: denominator 0 → NO_DATA; source gap → INCOMPLETE
limitations: BLOCKED/INCONCLUSIVE remain distinct outcomes; they are not rewritten as NOT_SATISFIED.
```

## OBS-MET-QLT-004 — blocking_finding_frequency

**Disposition:** `CANONICAL_V1`

```text
definition: Frequency of UPOS-007 Findings whose governed consequence makes them blocking for the selected Quality scope.
measurement_type: RATE
source: UPOS-007 Findings plus applicable Assessment/criteria/policy semantics
population: completed Assessments by default; alternate population requires new/versioned definition
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: blocking Findings / completed Assessments in population
dimensions: project, Change Class, assessment_type, finding category/severity where governed
unknown handling: unresolved blocking consequence or source gaps → UNKNOWN/INCOMPLETE
limitations: Finding volume depends on risk/review depth and is not a universal Agent quality score.
```

## OBS-MET-QLT-005 — evidence_insufficient_rate

**Disposition:** `CANONICAL_V1`

```text
definition: Rate of applicable REQUIRED criterion evaluations with UPOS-007 evidence sufficiency INSUFFICIENT.
measurement_type: RATE
source: UPOS-007 completed criterion evaluations / Evidence Bindings
population: applicable REQUIRED criterion evaluations in completed Assessments
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: INSUFFICIENT evaluations / applicable REQUIRED evaluations with governed sufficiency state
dimensions: project, Change Class, assessment_type, Criteria Set/version
unknown handling: unresolved/unknown sufficiency → separate/INCOMPLETE; never assumed sufficient
limitations: Observability does not assess Evidence freshness/reliability itself.
```

## OBS-MET-QLT-006 — escaped_defect_rate

**Disposition:** `DEFERRED`

```text
definition: Rate of post-acceptance defects/regressions attributable to previously accepted changes.
measurement_type: RATE
source: future owner-defined defect/incident identity and change-attribution relation
population: not available in current frozen 01–07
window: future cohort/window
formula: deferred until owner interface exists
dimensions: future project/change/incident dimensions
unknown handling: NO_DATA/UNKNOWN until source owner exists
limitations: UPOS-008 must not invent Incident/Defect ontology.
```
