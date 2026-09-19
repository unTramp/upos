# Observability Entity Model Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Decision

Top-level Module-08 semantic identities:

```text
event_id
trace_id
span_id
metric_definition_id
```

No additional global ID is justified for Metric Observation, Audit Projection row, Read Model row, Resource Usage record or correlation group.

## Why Metric Definition receives identity

Metric Definitions have independent lifecycle/version/supersession and are referenced historically by observations/dashboard definitions.

## Why Metric Observation does not

Observation is naturally addressable by Definition/version + scope/window/dimensions + data revision. No independent governance lifecycle was found.

## Why no agent_instance_id

Frozen UPOS-002 owns Agent Instance semantics but only guarantees configured runtime identity/reference. Inventing `agent_instance_id` in Module 08 would invert ownership. Use `agent_instance_ref`; reconcile concrete bindings with UPOS-011.

## Read projections

Trace materialization, Audit Projection and Read Models are derived projections and receive definition/version metadata, not new row identities by default.
