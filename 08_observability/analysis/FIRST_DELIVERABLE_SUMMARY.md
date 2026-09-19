# UPOS-008 First Deliverable Summary

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL  
**Date:** 2026-09-19

## 1. Scope

UPOS-008 owns execution observation, correlation/causation, traces/spans, telemetry data quality, metric semantics, cost/usage attribution, audit/provenance projections, Observability health and Control Plane read models.

## 2. Non-scope

It does not own truth, authority, Skill procedure, Workflow state, Context semantics, Engineering mechanics, Quality verdicts, Learning interpretation, Security/permission policy or provider/project bindings.

## 3. Ontology

```text
Event
Trace
Span
Metric Definition
Metric Observation
Audit Projection
Provenance Projection
Read Model
```

## 4. Stable identities

```text
event_id
trace_id
span_id
metric_definition_id
```

Deliberately not created:

```text
metric_observation_id
audit_record_id
read_model_row_id
agent_instance_id
```

## 5. Key reconciliations/additions beyond the implementation directive

1. `producer != initiator != domain owner`.
2. Use `agent_instance_ref`; frozen UPOS-002 does not own a universal `agent_instance_id`.
3. Telemetry completeness is defined only against explicit capture expectations/policy.
4. Event/Span causal graphs are acyclic; temporal adjacency is not causation.
5. Event Store is at-least-once tolerant through semantic idempotency by `event_id`; exactly-once transport is not required.
6. Current-state projection conflicts produce `PROJECTION_DRIFT`; owner state wins.
7. Task lead time and Workflow cycle time receive exact UPOS-004 boundaries.
8. Queue/wait/saturation metrics are conditional unless runtime/provider exposes real queue/capacity boundaries.
9. Rework/Retry are measured only from explicit UPOS-004/runtime semantics; repeated actions are not inferred as either.
10. Quality metrics honor reconciled UPOS-007 assessment cycle, evidence-binding and historical `as of assessed_at` semantics.
11. Monetary aggregation across currencies requires explicit FX basis.
12. Human wait time is not inferred Human work time.
13. Metric observations have semantic tuple addressability; no observation ID explosion.
14. Canonical metric inventory distinguishes `CANONICAL_V1`, `CONDITIONAL_INTERFACE`, and `DEFERRED` metrics.

## 6. Event envelope

Includes identity/type/schema, occurrence/record/ingest time, producer, initiator, domain owner, trace/correlation/causation, upstream semantic spine refs, primary/related domain refs, owner result/failure refs, provenance refs, capture/sampling refs and pending security policy refs.

## 7. Event taxonomy

High-level classes only; namespaced event types remain controlled. Owner-domain result/status stays in owner refs rather than exploding event types.

## 8. Time/order model

No global total order. Prefer causation, span hierarchy, owner version/transition refs and only then timestamps.

## 9. Trace/Span

One Task/Workflow may have multiple Traces. Trace materializations are rebuildable projections; Events stay immutable. Span status is Observability-local and does not duplicate Workflow/Quality state.

## 10. Telemetry quality

Explicit taxonomy covers missing required events, duplicates, ID collision, malformed/unknown schema, causal/span cycles, orphan refs, clock skew, incomplete traces, late events, metric source gaps and projection drift.

## 11. Metrics

Metric Definition has stable identity/version/lifecycle. Metric Observation has no global ID and preserves source lineage, completeness, data revision and sample size.

## 12. Cost/usage

Provider-neutral raw usage + pricing basis + currency + calculation method. No hidden pricing. No direct summation across currencies without FX basis.

## 13. Capacity/human attention

Capacity is system execution capacity, not HR utilization. Saturation needs a real denominator. Planned Human gates and unplanned intervention are different.

## 14. Audit/provenance

Projections index owner-module relationships and support navigation/reconstruction but never become provenance owners.

## 15. Control Plane

Read Models are rebuildable, eventually consistent and freshness-aware. Actions route to owner-domain interfaces.

## 16. Pending reconciliation

```text
UPOS-009 → learning interpretation/promotion interface
UPOS-010 → sensitivity/access/redaction/retention/protected-action audit interface
UPOS-011 → concrete storage/exporter/provider/clock/pricing/project/queue/capacity bindings
```

## 17. P0 result

No P0 conflict with frozen UPOS-01–07 was identified.

Normative implementation proceeded automatically as directed.
