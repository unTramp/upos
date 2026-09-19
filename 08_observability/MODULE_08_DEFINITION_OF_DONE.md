# Module 08 Definition of Done

**ID:** UPOS-08-DOD-001  
**Type:** DEFINITION OF DONE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## v1 completion checklist

- [x] Observability ownership/non-ownership explicit.
- [x] `EVENT != DOMAIN TRUTH` explicit.
- [x] `TRACE != WORKFLOW` explicit.
- [x] `SPAN != WORKFLOW STAGE` explicit.
- [x] `READ MODEL != SOURCE OF TRUTH` explicit.
- [x] stable `event_id`, `trace_id`, `span_id`, `metric_definition_id`.
- [x] no unnecessary `metric_observation_id`, `audit_record_id`, `read_model_row_id`.
- [x] Agent Instance uses upstream/runtime `agent_instance_ref`, not invented ID.
- [x] Event envelope defined.
- [x] producer vs initiator vs domain owner distinguished.
- [x] Event immutability and correction relation defined.
- [x] occurred/recorded/ingested time separated.
- [x] clock skew/quality handled.
- [x] global total order rejected.
- [x] correlation != causation.
- [x] causal/span parent cycles forbidden.
- [x] Trace/Span models exist.
- [x] trace propagation interface exists.
- [x] no hidden chain-of-thought telemetry.
- [x] payload minimization defined.
- [x] capture expectations/policy basis defined.
- [x] required telemetry sampling prohibition defined.
- [x] Event Store semantic requirements defined.
- [x] idempotent ingestion/dedup semantics defined.
- [x] replay cannot re-execute side effects.
- [x] telemetry data-quality taxonomy exists.
- [x] projection drift rule defined.
- [x] Observability health defined.
- [x] Metric Definition/Observation semantics exist.
- [x] metric unknown/no-data/incomplete semantics exist.
- [x] late-event recomputation/data revision defined.
- [x] Task lead time / Workflow cycle time / active / blocked differentiated.
- [x] queue time conditional on explicit queue signals.
- [x] retry metrics != rework metrics.
- [x] Quality metrics consume reconciled UPOS-007 temporal semantics.
- [x] cost/usage attribution and price-basis provenance exist.
- [x] currency/FX provenance rule exists.
- [x] capacity != productivity explicit.
- [x] saturation requires real capacity denominator.
- [x] planned Human gate != unplanned intervention.
- [x] Control Plane/read-model semantics defined.
- [x] owner state wins projection conflicts.
- [x] audit/provenance projection semantics defined.
- [x] dashboard metric transparency defined.
- [x] template conformance validated.
- [x] no hard-coded provider/backend technology.
- [x] no unresolved internal P0/P1 Module-08 semantic gaps.
- [x] current frozen-source requirements mapped.
- [x] UPOS-009 dependencies registered.
- [x] UPOS-010 dependencies registered.
- [x] UPOS-011 dependencies registered.

## Final freeze validation

- [x] UPOS-009 reconciliation complete.
- [x] UPOS-010 reconciliation complete.
- [x] UPOS-011 reconciliation complete.
- [x] all material reconciliation-register items resolved.
- [x] final traceability audit rerun.
- [x] final ownership audit rerun.
- [x] final template conformance rerun.
- [x] `UNMAPPED MODULE-08 SOURCE REQUIREMENTS = 0`.
- [x] no known ownership leakage into UPOS-01–07 / 09–11.

```text
UPOS-008 FREEZE = FROZEN v1.0
```
