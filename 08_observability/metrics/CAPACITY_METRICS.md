# Capacity Metrics

**ID:** UPOS-08-CAP-SET-001  
**Type:** METRIC DEFINITIONS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability

## OBS-MET-CAP-001 — running_agent_run_count

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Concurrent Agent Runs observed as actively executing.
measurement_type: GAUGE
source: Agent Run execution Spans/runtime start/end telemetry
population: selected project/Role/Agent Definition/provider scope
window: POINT_IN_TIME
formula: count(active bounded Agent Run intervals at observation time)
dimensions: project, Role, Agent Definition/version, provider binding
unknown handling: incomplete run lifecycle telemetry → INCOMPLETE
limitations: Running != productive; Agent Instance binding remains an external runtime reference.
```

## OBS-MET-CAP-002 — blocked_workflow_ratio

**Disposition:** `CANONICAL_V1`

```text
definition: Current proportion of active non-terminal Workflow Instances in UPOS-004 BLOCKED.
measurement_type: RATIO
source: authoritative/current UPOS-004 state projection reconciled with Events
population: active non-terminal Workflow Instances in selected scope
window: POINT_IN_TIME
formula: BLOCKED active instances / all active non-terminal instances
dimensions: project, Change Class, Workflow Definition/version, Work Type
unknown handling: owner-state/projection disagreement → INCOMPLETE + PROJECTION_DRIFT; denominator 0 → NO_DATA
limitations: BLOCKED is not PAUSED; high ratio is a signal, not root-cause proof.
```

## OBS-MET-CAP-003 — capacity_saturation

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Used execution capacity divided by real configured/observable available capacity.
measurement_type: RATIO
source: runtime/provider active capacity + configured capacity denominator from UPOS-011/project binding
population: selected runtime/provider capacity pool
window: POINT_IN_TIME / FIXED_INTERVAL summary
formula: active capacity units / configured available capacity units
dimensions: project, provider binding, capacity pool, operation class
unknown handling: no real denominator → UNKNOWN
limitations: Historical observed max is not capacity.
```

## OBS-MET-CAP-004 — unplanned_human_intervention_rate

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Rate of Workflow Instances requiring at least one unplanned Human intervention.
measurement_type: RATE
source: Human-interaction Events classified against upstream Workflow/Human Governance plan
population: selected completed/terminal Workflow Instances
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: instances with >=1 unplanned Human intervention / population instances
dimensions: project, Change Class, Workflow, Work Type
unknown handling: Human classification unavailable → UNKNOWN/INCOMPLETE; denominator 0 → NO_DATA
limitations: Planned/required Human gates are excluded; metric does not measure Human work quality.
```
