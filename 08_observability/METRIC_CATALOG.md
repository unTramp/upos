# Metric Catalog

**ID:** UPOS-08-MCAT-001  
**Type:** METRIC DISCOVERY INDEX  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Purpose

The catalog indexes named reusable Metric Definitions without duplicating their full contracts.

Disposition:

```text
CANONICAL_V1
= formula/boundaries are supportable from frozen 01–07 or Module-08-owned telemetry semantics

CONDITIONAL_INTERFACE
= metric semantics are defined but require explicit runtime/provider/downstream signals before an observation can be valid

DEFERRED
= source owner/interface does not yet exist; do not fabricate observations
```

## 2. Inventory

| metric_definition_id | name | class | disposition | owner file |
|---|---|---|---|---|
| `OBS-MET-DEL-001` | `task_lead_time` | DURATION | CANONICAL_V1 | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-002` | `workflow_cycle_time` | DURATION | CANONICAL_V1 | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-003` | `workflow_active_execution_time` | DURATION | CANONICAL_V1 | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-004` | `workflow_blocked_time` | DURATION | CANONICAL_V1 | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-005` | `workflow_rework_entry_count` | COUNTER | CANONICAL_V1 | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-006` | `workflow_retry_count` | COUNTER | CONDITIONAL_INTERFACE | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-007` | `queue_wait_time` | DURATION | CONDITIONAL_INTERFACE | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-008` | `review_execution_duration` | DURATION | CONDITIONAL_INTERFACE | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-009` | `qa_execution_duration` | DURATION | CONDITIONAL_INTERFACE | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-DEL-010` | `merge_latency` | DURATION | CONDITIONAL_INTERFACE | `metrics/DELIVERY_METRICS.md` |
| `OBS-MET-QLT-001` | `first_pass_acceptance_rate` | RATE | CANONICAL_V1 | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-QLT-002` | `quality_assessment_cycle_count` | COUNTER | CANONICAL_V1 | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-QLT-003` | `quality_gate_not_satisfied_rate` | RATE | CANONICAL_V1 | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-QLT-004` | `blocking_finding_frequency` | RATE | CANONICAL_V1 | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-QLT-005` | `evidence_insufficient_rate` | RATE | CANONICAL_V1 | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-QLT-006` | `escaped_defect_rate` | RATE | DEFERRED | `metrics/QUALITY_METRICS.md` |
| `OBS-MET-CST-001` | `cost_per_task` | DERIVED | CONDITIONAL_INTERFACE | `metrics/COST_METRICS.md` |
| `OBS-MET-CST-002` | `cost_per_workflow_instance` | DERIVED | CONDITIONAL_INTERFACE | `metrics/COST_METRICS.md` |
| `OBS-MET-CST-003` | `cost_per_integrated_change` | DERIVED | CONDITIONAL_INTERFACE | `metrics/COST_METRICS.md` |
| `OBS-MET-CAP-001` | `running_agent_run_count` | GAUGE | CONDITIONAL_INTERFACE | `metrics/CAPACITY_METRICS.md` |
| `OBS-MET-CAP-002` | `blocked_workflow_ratio` | RATIO | CANONICAL_V1 | `metrics/CAPACITY_METRICS.md` |
| `OBS-MET-CAP-003` | `capacity_saturation` | RATIO | CONDITIONAL_INTERFACE | `metrics/CAPACITY_METRICS.md` |
| `OBS-MET-CAP-004` | `unplanned_human_intervention_rate` | RATE | CONDITIONAL_INTERFACE | `metrics/CAPACITY_METRICS.md` |
| `OBS-MET-GOV-001` | `reclassification_rate` | RATE | CANONICAL_V1 | `metrics/GOVERNANCE_METRICS.md` |
| `OBS-MET-GOV-002` | `scope_expansion_rate` | RATE | CONDITIONAL_INTERFACE | `metrics/GOVERNANCE_METRICS.md` |
| `OBS-MET-GOV-003` | `manual_override_rate` | RATE | CONDITIONAL_INTERFACE | `metrics/GOVERNANCE_METRICS.md` |
| `OBS-MET-GOV-004` | `permission_denied_rate` | RATE | CONDITIONAL_INTERFACE | `metrics/GOVERNANCE_METRICS.md` |

## 3. Non-canonical activity metrics

The following MUST NOT be treated as primary performance KPIs merely because they are easy to count:

```text
lines of code
number of commits
number of Integration Requests
number of messages
raw tool-call count
```

They may appear as diagnostic/contextual counts where a defined use case exists.
