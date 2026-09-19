# Observability Ontology

**ID:** UPOS-08-ONT-001  
**Type:** ONTOLOGY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Observability Event

```text
OBSERVABILITY EVENT
= immutable attributable observation that something occurred
```

An Event is not the underlying domain entity/state.

## 2. Trace

```text
TRACE
= causally coherent operational execution narrative identified by trace_id
```

A Trace is not a Task or Workflow Instance. One Task/Workflow may contain multiple Traces.

A materialized Trace view is a rebuildable projection over Span/Event records and may receive later data revisions without changing historical Event identity.

## 3. Span

```text
SPAN
= bounded timed operation/execution segment inside a Trace
```

A Span is not a Workflow Stage. A Stage may contain many Spans; one Span may observe work related to a Stage.

## 4. Correlation group

```text
correlation_id
= stable grouping key for occurrences belonging to one broader operational conversation
```

It is a key/relationship, not a separately governed domain entity.

## 5. Causation edge

```text
causation_event_id
= direct triggering/causal predecessor Event when explicitly known
```

Temporal adjacency alone is not causation.

## 6. Metric Definition

```text
METRIC DEFINITION
= versioned governed specification of how an operational measurement is derived
```

Every reusable canonical metric has stable `metric_definition_id`.

## 7. Metric Observation

```text
METRIC OBSERVATION
= measured/derived value for one Metric Definition/version + bounded scope/window/dimensions + data revision
```

No global `metric_observation_id` exists in v1.

A Metric Observation is addressable by its semantic tuple, for example:

```text
metric_definition_id + version
+ window/scope
+ normalized dimensions
+ data_revision
```

## 8. Audit Projection

```text
AUDIT PROJECTION
= governance/audit-oriented rebuildable view over attributable Event/domain references
```

It has no organizational authority.

## 9. Provenance Projection

```text
PROVENANCE PROJECTION
= navigable cross-module relation view over identities already owned by Modules 01–07 and later modules
```

It indexes provenance; it does not own it.

## 10. Read Model

```text
READ MODEL
= rebuildable query-oriented operational projection
```

Read Models are eventually consistent unless an external contract says otherwise.

## 11. Event Store

`Event Store` is an abstract storage/interface role for retained Observability Events.

UPOS-008 defines semantic requirements only. Concrete backend belongs to UPOS-011.

## 12. Resource Usage observation

Resource usage is normally represented as Event/Span attributes or source records referenced by metrics.

UPOS-008 v1 does not create a global `resource_usage_record_id`.

## 13. Stable identities

```text
event_id
trace_id
span_id
metric_definition_id
```

Relationships/keys:

```text
parent_span_id
correlation_id
causation_event_id
```

## 14. Upstream actor identity rule

UPOS-008 reuses:

```text
role_id
agent_definition_id + version
agent_run_id
```

from UPOS-002.

Frozen UPOS-002 describes Agent Instance as a configured runtime identity/reference but does not define a universal stable `agent_instance_id`.

Therefore Module 08 uses:

```text
agent_instance_ref
```

and MUST NOT silently mint an `agent_instance_id`.

Concrete instance binding is a UPOS-011 reconciliation point.

## 15. Anti-conflation invariants

```text
EVENT != DOMAIN ENTITY
EVENT != DOMAIN TRUTH
TRACE != WORKFLOW INSTANCE
SPAN != WORKFLOW STAGE
CORRELATION != CAUSATION
METRIC DEFINITION != METRIC OBSERVATION
METRIC != QUALITY VERDICT
AUDIT PROJECTION != AUTHORITY
READ MODEL != SOURCE OF TRUTH
PROVENANCE PROJECTION != PROVENANCE OWNERSHIP
TELEMETRY HEALTH != PRODUCT/CHANGE QUALITY
CAPACITY METRIC != PERSON PERFORMANCE SCORE
```
