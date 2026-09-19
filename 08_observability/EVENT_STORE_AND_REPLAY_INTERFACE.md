# Event Store and Replay Interface

**ID:** UPOS-08-ESR-001  
**Type:** STORAGE / REPLAY SEMANTIC INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Scope

UPOS-008 defines semantic requirements for retained Event storage.

It does not select a database, message bus, trace backend, analytics engine or vendor.

## 2. Event Store requirements

A conforming implementation SHOULD be:

```text
append-oriented
immutable by event_id while retained
queryable by time and stable correlation/domain refs
idempotent/deduplicating by event_id
schema-version aware
late-event tolerant
retention-policy aware
capable of projection rebuild inputs
```

## 3. Delivery semantics

UPOS-008 does not require transport-level exactly-once delivery.

The semantic requirement is:

```text
at-least-once delivery is acceptable
if ingestion is idempotent by event_id
and duplicates do not double-count projections/metrics
```

Other transport guarantees may be used by UPOS-011 implementations.

## 4. Duplicate Event

Same `event_id` + semantically same Event:

```text
redelivery
→ one retained logical Event
```

Same `event_id` + conflicting immutable payload:

```text
EVENT_ID_COLLISION
→ telemetry integrity error
```

Do not choose one payload silently.

## 5. Late Event

A valid Event may arrive after projections/metrics were computed.

The Event retains original:

```text
event_id
occurred_at
recorded_at
```

and receives collector `ingested_at` where available.

Affected read models/Metric Observations MAY be recomputed with incremented `data_revision`.

## 6. Replay

Observability replay means:

```text
re-read retained observational records
→ rebuild Trace/Metric/Read Model projections
```

It MUST NOT mean:

```text
re-execute external side effects
re-run merge/deploy actions
reissue provider commands
```

Side-effect replay belongs to owner/runtime systems if supported.

## 7. Retention

Event immutability does not imply infinite retention.

Retention, deletion, legal/privacy constraints and access controls remain pending UPOS-010/011/project policy.

If retained history is incomplete due to governed retention, projections/metrics MUST expose resulting completeness limits.

## 8. Rebuildability

A read projection SHOULD be rebuildable from:

```text
retained Events
+ referenced owner snapshots/relations where required
+ projection definition/version
```

Projection storage corruption MUST NOT alter owner-domain state.
