# UPOS-008 Normative Artifact Inventory

**ID:** UPOS-08-INV-001  
**Type:** CANONICAL INVENTORY  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## Operating / ontology / event layer

| Artifact | Purpose |
|---|---|
| `README.md` | module entry point/status/invariants |
| `OBSERVABILITY_OPERATING_MODEL.md` | ownership and operating constitution |
| `OBSERVABILITY_ONTOLOGY.md` | core entities/identity model |
| `EVENT_STANDARD.md` | durable Event contract/envelope |
| `EVENT_TAXONOMY.md` | event classes/naming discipline |
| `CORRELATION_CAUSATION_AND_ORDERING.md` | correlation/causation/order semantics |
| `TRACE_AND_SPAN_STANDARD.md` | Trace/Span contracts/propagation |
| `TELEMETRY_CAPTURE_STANDARD.md` | capture importance/sampling/minimization |
| `EVENT_STORE_AND_REPLAY_INTERFACE.md` | abstract storage/idempotency/replay |
| `TELEMETRY_DATA_QUALITY.md` | telemetry quality/completeness taxonomy |
| `TIME_AND_DURATION_SEMANTICS.md` | exact time/duration boundaries |

## Metric / resource layer

| Artifact | Purpose |
|---|---|
| `METRIC_DEFINITION_STANDARD.md` | Metric Definition contract/lifecycle |
| `METRIC_DERIVATION_STANDARD.md` | Metric Observation/recompute/lineage |
| `METRIC_CATALOG.md` | canonical metric discovery/disposition |
| `COST_AND_USAGE_ATTRIBUTION.md` | usage/cost/pricing attribution |
| `CAPACITY_WORKLOAD_AND_HUMAN_ATTENTION.md` | capacity/workload/Human-attention semantics |
| `metrics/DELIVERY_METRICS.md` | delivery/time/retry/rework metrics |
| `metrics/QUALITY_METRICS.md` | UPOS-007-derived Quality metrics |
| `metrics/COST_METRICS.md` | cost metrics |
| `metrics/CAPACITY_METRICS.md` | capacity/workload metrics |
| `metrics/GOVERNANCE_METRICS.md` | governance metrics |

## Projection / interface layer

| Artifact | Purpose |
|---|---|
| `QUALITY_OBSERVABILITY.md` | Quality interface constraints |
| `GOVERNANCE_OBSERVABILITY.md` | governance measurement constraints |
| `AUDIT_AND_PROVENANCE_PROJECTIONS.md` | audit/provenance read projections |
| `CONTROL_PLANE_READ_MODELS.md` | Control Plane read-model semantics |
| `OBSERVABILITY_HEALTH.md` | self-observability health |
| `OBSERVABILITY_LIFECYCLE_AND_VERSIONING.md` | lifecycle/versioning |
| `CROSS_MODULE_INTERFACES.md` | interfaces with UPOS-01–11/runtime |
| `MODULE_08_DEFINITION_OF_DONE.md` | final freeze criteria |
| `MODULE_08_TRACEABILITY.md` | canonical source-to-artifact coverage |
| `VIRTUAL_REPOSITORY_TREE.md` | package structure |

## Operational authoring templates

```text
templates/OBSERVABILITY_EVENT_TEMPLATE.md
templates/TRACE_TEMPLATE.md
templates/SPAN_TEMPLATE.md
templates/METRIC_DEFINITION_TEMPLATE.md
```

## Evidence layer

All `analysis/*.md` files are historical evidence and are not normative contracts.
