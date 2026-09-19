# Capacity, Workload and Human Attention

**ID:** UPOS-08-CAP-001  
**Type:** CAPACITY / HUMAN ATTENTION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Capacity principle

Agent/system capacity is engineering execution capacity, not employee productivity.

```text
CAPACITY METRIC != PERSON PERFORMANCE SCORE
```

## 2. Observable workload candidates

When instrumentation supports them:

```text
running runs
queued runs
blocked runs
waiting runs
work in progress
active execution time
queue time
blocked time
concurrency
provider/tool wait time
```

## 3. Queue boundary requirement

Universal U-POS does not define one queue lifecycle.

A `queued` count or `queue_time` requires an explicit queue signal from runtime/provider/owner interface.

No explicit queue signal → `UNKNOWN/N/A`, not inferred from “not running”.

## 4. Capacity limit requirement

A saturation metric requires a configured/observable capacity denominator, for example provider concurrency/rate limit/runtime worker capacity.

Observed historical maximum is NOT automatically the capacity limit.

Without a real denominator:

```text
saturation = UNKNOWN
```

## 5. Active execution ratio

Where a meaningful bounded availability interval exists:

```text
active_execution_ratio
= active execution duration / eligible availability duration
```

The denominator MUST be defined.

This is not a productivity score.

## 6. Agent-level analytics

Allowed factual views include:

```text
runs
run duration
wait/block duration
usage/cost
failure/retry observations
rework incidence
first-pass downstream Quality outcomes
```

Do not create a universal composite “Agent Score”.

## 7. Human attention

Where attributable source data exists, Module 08 may measure:

```text
human_interaction_count
human_decision_count
human_wait_time
human_active_review_time
human_minutes_per_change
```

## 8. Planned vs unplanned Human interaction

Canonical v1 observational categories:

```text
PLANNED_APPROVAL
PLANNED_REVIEW
MANUAL_DECISION
ERROR_RECOVERY
POLICY_OVERRIDE
MISSING_CONTEXT_RESOLUTION
QUALITY_ESCALATION
SECURITY_REQUIRED_REFERENCE
OTHER
```

Security-specific classification consumes reconciled UPOS-010 owner semantics.

A Human interaction is `PLANNED` only when the upstream Workflow/Human Governance/policy reference establishes it as planned.

## 9. Autonomy metric

A possible bounded metric:

```text
workflow_without_unplanned_human_intervention_rate
```

Required/planned Human Governance gates MUST NOT be counted as autonomy defects.

The denominator/population must be defined by Change Class/Workflow cohort.

## 10. Human wait != human work

A Task waiting for a Human action may measure `human_wait_time` from explicit waiting boundary to response.

It MUST NOT infer that the Human worked continuously during that interval.
