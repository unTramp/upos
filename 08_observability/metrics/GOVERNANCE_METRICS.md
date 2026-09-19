# Governance Metrics

**ID:** UPOS-08-GOV-SET-001  
**Type:** METRIC DEFINITIONS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability

## OBS-MET-GOV-001 — reclassification_rate

**Disposition:** `CANONICAL_V1`

```text
definition: Rate of selected Task/Workflow units that undergo at least one explicit UPOS-004 reclassification after initial routing.
measurement_type: RATE
source: explicit UPOS-004 reclassification occurrences
population: Tasks or Workflow Instances in selected cohort
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: units with >=1 reclassification / all population units
dimensions: project, Change Class initial/final, Workflow, Work Type
unknown handling: missing required routing/reclassification telemetry → INCOMPLETE; denominator 0 → NO_DATA
limitations: Reclassification is not automatically process failure; new evidence may justify it.
```

## OBS-MET-GOV-002 — scope_expansion_rate

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Rate of selected Tasks/Engineering Changes with at least one governed scope-expansion occurrence.
measurement_type: RATE
source: explicit UPOS-004/006 SCOPE_EXPANSION owner signals
population: selected Tasks or Engineering Changes
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: units with >=1 scope-expansion occurrence / population units
dimensions: project, Change Class, Workflow, repository where applicable
unknown handling: no explicit scope-expansion capture → UNKNOWN; denominator 0 → NO_DATA
limitations: Do not infer scope expansion from diff size.
```

## OBS-MET-GOV-003 — manual_override_rate

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Rate of governed population units with an explicit exceptional Human Governance override.
measurement_type: RATE
source: UPOS-002 Human Governance override references/events
population: selected governed decisions/Workflow Instances
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: units with explicit exceptional override / defined population units
dimensions: project, Change Class, Workflow, override type where governed
unknown handling: owner semantics unavailable → UNKNOWN; denominator 0 → NO_DATA
limitations: Ordinary required approvals/reviews are excluded.
```

## OBS-MET-GOV-004 — permission_denied_rate

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Rate of permission-checked actions whose reconciled UPOS-010 Permission Decision is DENY.
measurement_type: RATE
source: UPOS-010 governed Permission Decision refs
population: protected/permission-checked actions in selected scope
window: FIXED_INTERVAL / ROLLING_INTERVAL / cohort
formula: denied actions / permission-checked actions
dimensions: project, protected action type, Role, Change Class where permitted
unknown handling: missing/incomplete Permission Decision population → UNKNOWN/INCOMPLETE; denominator 0 → NO_DATA
limitations: Module 08 does not define Permission Decision semantics and must not infer denials from provider/tool failures.
```
