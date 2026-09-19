# Observability Health

**ID:** UPOS-08-OHL-001  
**Type:** SELF-OBSERVABILITY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Principle

Observability must make its own data health visible.

```text
OBSERVABILITY HEALTH != PRODUCT QUALITY
```

Telemetry can be healthy while a change fails Quality, and telemetry can be degraded while the underlying operation succeeded.

## 2. Canonical health signals

Where measurable:

```text
ingestion_lag
required_event_gap_count/estimate
schema_rejection_count
unknown_schema_count
event_id_collision_count
orphan_reference_rate
broken_causation_rate
trace_completeness_rate
late_event_rate
metric_source_gap_count
metric_freshness
projection_lag
projection_drift_count
```

## 3. Event loss estimate

Event loss MUST NOT be presented as a precise percentage unless the system has an independent expected-event/capture basis sufficient to calculate it.

Otherwise expose known required gaps or `UNKNOWN` loss estimate.

## 4. Trace completeness rate

Denominator includes only traces/scopes whose capture expectations allow a meaningful completeness determination.

Unknown-completeness traces should be reported separately.

## 5. Projection lag

Projection lag SHOULD distinguish:

```text
latest source Event ingestion watermark
vs
projection processed watermark
```

Concrete watermark implementation belongs to UPOS-011/runtime.

## 6. Health signals are not automatic policy changes

High rework, telemetry lag, repeated provider failure or high stale-context rate may trigger alerts/candidates.

They MUST NOT automatically change Workflow, Skills, Quality policy or permissions.

## 7. Alert candidates

UPOS-008 MAY define observable alert candidates/conditions.

Alert routing, incident authority and remediation orchestration remain outside Module 08.

## 8. Module health wording

A Control Plane MUST NOT label a U-POS module semantically “healthy” based only on telemetry uptime.

If displaying module health, criteria must be explicit, e.g.:

- event interface availability;
- capture completeness;
- projection integrity;
- queue/block anomalies;
- validation failures.
