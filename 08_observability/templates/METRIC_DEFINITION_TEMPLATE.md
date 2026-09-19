# Metric Definition Template

**Template owner:** UPOS-008 Observability  
**Conforms to:** `METRIC_DEFINITION_STANDARD.md`

```text
metric_definition_id:
name:
version:
status:
purpose:
metric_class:
measurement_type:
unit:

source_event_types: []
source_domain_refs: []
source_contract_refs: []

population:
scope:
window_semantics:
aggregation_rule:
formula:

inclusion_criteria: []
exclusion_criteria: []

numerator_definition: N/A
denominator_definition: N/A

allowed_dimensions: []
default_dimensions: []

unknown_no_data_handling:
late_event_recomputation_policy:
data_quality_requirements:

sample_size_semantics:
percentile_semantics: N/A

freshness_expectation:
known_limitations: []

supersedes: none
replacement: none
```
