# Validation and Baseline Standard

**ID:** UPOS-09-VBS-001  
**Type:** VALIDATION / BASELINE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/VALIDATION_PLAN_TEMPLATE.md



## 1. Validation Plan identity

Every independently referenced Validation Plan has stable:

```text
validation_plan_id
```

## 2. Contract

```text
validation_plan_id
improvement_proposal_ref
status

target_artifact_ref
target_version_before
candidate_version_or_change_ref

baseline_definition
baseline_period_or_cohort
comparison_definition
comparison_period_or_cohort

target_metric_or_observation_refs
quality_criteria_refs
minimum_evidence_requirements

expected_effects
guardrails
observation_window
stop_conditions
revert_or_owner_review_triggers

confounders_to_track
population_comparability_rules
analysis_method
limitations

created_by_ref
created_at
supersedes
replacement
```

## 3. Baseline

Where meaningful, establish a baseline before claiming improvement.

The baseline MAY include:

```text
first-pass acceptance
re-review/rework rate
escaped defect frequency
cycle time
latency
cost
human intervention/attention
waiver frequency
governance exceptions
```

Metric definition/calculation remains UPOS-008-owned once frozen.

## 4. No false precision

Insufficient samples or incomparable cohorts MUST be explicitly reported.

A numeric delta is not automatically meaningful evidence.

```text
METRIC CHANGE != PROOF OF IMPROVEMENT
```

## 5. Version comparison

Learning analysis SHOULD preserve exact compared versions/references where available, including:

```text
Skill version
Workflow version
Agent Definition version
Context policy version
Quality policy/version
Engineering standard version
project/provider binding version
```

## 6. Confounders

At minimum assess known plausible confounders such as:

```text
Change Class / Work Type mix
project/cohort change
model/provider/tool change
sample-size change
Quality policy change
human-involvement change
Context policy/source change
security policy change
seasonal/external factors
```

## 7. Success criteria are predeclared

A Validation Plan MUST define expected-effect and guardrail criteria before post-change interpretation when feasible.

Do not invent a success criterion after observing the result.

## 8. Validation vs Quality Gate

```text
VALIDATION PLAN
= how a proposed improvement's expected effect will be assessed

QUALITY GATE
= UPOS-007-owned reusable quality evaluation contract
```

A Validation Plan MAY reference Quality Gates/criteria but MUST NOT redefine their semantics.
