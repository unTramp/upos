# Cost Metrics

**ID:** UPOS-08-COS-SET-001  
**Type:** METRIC DEFINITIONS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability

Valid monetary observations require provider usage/pricing or equivalent governed source data.

## OBS-MET-CST-001 — cost_per_task

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Attributed monetary cost allocated to one Task.
measurement_type: DERIVED
source: deduplicated usage/cost source records attributable to task_id with price basis
population: Tasks with sufficiently complete cost attribution
window: TASK_LIFETIME
formula: sum(allocated cost) per task_id under one currency or explicit FX basis
dimensions: project, Change Class, Work Type, provider binding, currency
unknown handling: missing pricing/usage/allocation basis → INCOMPLETE/UNKNOWN
limitations: Shared-cost allocation must be explicit; lower cost != better result.
```

## OBS-MET-CST-002 — cost_per_workflow_instance

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Attributed monetary cost allocated to one Workflow Instance.
measurement_type: DERIVED
source: usage/cost source records attributable to workflow_instance_id
population: Workflow Instances with sufficiently complete cost attribution
window: WORKFLOW_LIFETIME
formula: sum(allocated cost) per workflow_instance_id under explicit price/currency basis
dimensions: project, Workflow Definition/version, Change Class, provider binding, currency
unknown handling: incomplete nested/provider usage → INCOMPLETE
limitations: Avoid double-counting parent and child billed operations.
```

## OBS-MET-CST-003 — cost_per_integrated_change

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Attributed monetary cost for one integrated Engineering Change/revision boundary.
measurement_type: DERIVED
source: usage/cost attributable through Task/Workflow/Engineering provenance to integrated change
population: successfully integrated changes with defined attribution boundary
window: bounded Engineering Change lifetime/cohort
formula: sum(allocated cost for bounded change) per integrated change unit
dimensions: project, Change Class, repository, provider binding, currency
unknown handling: missing cross-run attribution or price basis → INCOMPLETE/UNKNOWN
limitations: Does not imply business value or profitability.
```
