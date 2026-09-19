# Metric Definition Standard

**ID:** UPOS-08-MDS-001  
**Type:** METRIC CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0  
**Related:** `templates/METRIC_DEFINITION_TEMPLATE.md`

## 1. Identity

Every reusable canonical Metric Definition MUST have stable:

```text
metric_definition_id
```

Compatible versions retain the same semantic ID.

## 2. Minimum contract

```text
metric_definition_id
name
version
status
purpose
metric_class
measurement_type
unit

source_event_types
source_domain_refs
source_contract_refs

population
scope
window_semantics
aggregation_rule
formula

inclusion_criteria
exclusion_criteria

numerator_definition            # required for rate/ratio where applicable
denominator_definition          # required for rate/ratio where applicable

allowed_dimensions
default_dimensions

unknown_no_data_handling
late_event_recomputation_policy
data_quality_requirements

sample_size_semantics
percentile_semantics            # where distribution metric

freshness_expectation
known_limitations

supersedes
replacement
```

## 3. Metric classes

Canonical v1:

```text
COUNTER
GAUGE
DURATION
RATE
RATIO
DISTRIBUTION
DERIVED
```

## 4. Definition is not observation

The Metric Definition describes how to compute/interpret a measurement.

A Metric Observation is one output for one bounded scope/window/dimension set.

## 5. Rate/ratio discipline

Every rate/ratio MUST specify:

```text
numerator
denominator
population
window
exclusions
unknown handling
```

Names such as `success_rate` without these definitions are non-conformant.

## 6. Zero vs missing

A Metric Definition MUST define when numeric zero is a valid observed value.

It MUST NOT coerce:

```text
UNKNOWN
NO_DATA
INCOMPLETE
```

to `0`.

## 7. Dimensions

Dimensions are controlled by the Metric Definition.

Possible governed dimensions include:

```text
project
Change Class
Work Type
Concern
Workflow Definition/version
Stage
Role
Agent Definition/version
Skill/version
provider binding
Quality assessment type
```

High-cardinality identifiers SHOULD remain trace/query refs rather than metric dimensions unless explicitly justified.

## 8. Sample size

Rate/ratio/distribution observations MUST preserve applicable sample size/population count.

```text
100%, n=2
!=
100%, n=5000
```

## 9. Distribution summaries

Where useful, a Distribution Metric MAY define summaries such as:

```text
median
p75
p90
p95
```

The selected percentiles are part of the Metric Definition/version.

## 10. Versioning

Material formula/population/window/denominator/unknown-handling change requires a new Metric Definition version.

Do not silently redefine an established metric name.

## 11. Lifecycle

Metric Definition lifecycle:

```text
DRAFT
→ REVIEW
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

Historical Metric Observations retain the Definition version actually used.

## 12. Provider independence

A Metric Definition may require abstract source semantics.

Concrete query language/backend/analytics provider belongs to UPOS-011.
