# Metric Derivation Standard

**ID:** UPOS-08-MDR-001  
**Type:** DERIVATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Reproducibility

Given equivalent:

```text
Metric Definition/version
source Event/domain data revision
population/window
dimensions
projection version where used
```

a calculation SHOULD be reproducible.

Hidden formulas only inside a dashboard are prohibited for canonical metrics.

## 2. Metric Observation contract

A canonical Metric Observation SHOULD preserve:

```text
metric_definition_id
metric_definition_version

scope_ref / population_ref
window_start
window_end
window_kind

dimensions

observation_state
value
unit
sample_size

data_completeness_state
source_event_range_or_query_ref
source_domain_snapshot_refs
projection_definition_ref
projection_definition_version

data_revision
computed_at
recomputed_at

known_limitations
```

No global `metric_observation_id` is required in v1.

## 3. Observation states

```text
VALUE
NO_DATA
INCOMPLETE
UNKNOWN
```

`VALUE` may legitimately contain numeric zero.

## 4. Data completeness

Metric computation must propagate known telemetry gaps.

A numeric value MAY still be provided with `INCOMPLETE` only if the Metric Definition explicitly defines partial-data semantics; otherwise use `INCOMPLETE` without pretending full accuracy.

## 5. Late-arriving Events

Late Events may require recomputation.

Recomputation:

- does not mutate original Events;
- increments/changes `data_revision`;
- records `recomputed_at`;
- preserves Definition version.

## 6. Window kinds

Canonical supported semantic classes:

```text
POINT_IN_TIME
FIXED_INTERVAL
ROLLING_INTERVAL
TASK_LIFETIME
WORKFLOW_LIFETIME
RELEASE_OR_VERSION_COHORT
```

Concrete timezone/query execution belongs to adapter/runtime.

## 7. Cohorts

Cohort comparison MAY use:

```text
time
project
Change Class
Work Type
Concern
Workflow version
Skill version
Agent Definition version
Quality Policy version
Context Policy version
```

Correlation does not prove that the version caused the outcome difference.

## 8. Before/after analysis

Before/after comparison is an Observability projection over comparable cohorts.

It MUST preserve:

- cohort definition;
- sample sizes;
- data completeness;
- confounder/limitation notes where known.

It does not decide which version is “better”.

## 9. Currency aggregation

Monetary observations in different currencies MUST NOT be summed directly.

Conversion requires explicit:

```text
fx_basis_ref
fx_basis_version/effective_at
conversion method
```

Otherwise keep currency-separated observations.

## 10. Derived metric lineage

A derived metric must remain traceable to:

```text
Metric Definition/version
source data range/query
source Metric Observation refs where used
projection version
completeness state
```
