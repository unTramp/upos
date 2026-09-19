# Telemetry Data Quality

**ID:** UPOS-08-TDQ-001  
**Type:** DATA QUALITY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Purpose

Telemetry quality describes whether Observability records are sufficient and internally coherent for their declared observational purpose.

```text
TELEMETRY QUALITY != PRODUCT QUALITY
```

## 2. Canonical v1 issue taxonomy

```text
MISSING_REQUIRED_EVENT
DUPLICATE_EVENT
EVENT_ID_COLLISION
MALFORMED_EVENT
UNKNOWN_SCHEMA_VERSION
BROKEN_CAUSATION_REF
CAUSATION_CYCLE
BROKEN_SPAN_PARENT_REF
SPAN_PARENT_CYCLE
ORPHANED_DOMAIN_REF
CLOCK_SKEW_SUSPECTED
TIMESTAMP_QUALITY_UNKNOWN
INCOMPLETE_TRACE
LATE_EVENT
METRIC_SOURCE_GAP
PROJECTION_DRIFT
PROJECTION_SOURCE_GAP
UNRESOLVED_POLICY_REFERENCE
```

## 3. Missing Event rule

`MISSING_REQUIRED_EVENT` requires a known capture expectation.

Valid basis:

```text
capture_policy_ref/version
producer contract
owner-domain instrumentation contract
```

No expectation → absence is `UNKNOWN`, not automatically missing.

## 4. Completeness states

For a bounded trace/projection/metric source set:

```text
COMPLETE
PARTIAL
UNKNOWN
NO_DATA
```

Definitions:

- `COMPLETE` — all declared required source/capture expectations for that scope are satisfied;
- `PARTIAL` — known required source data is missing/late/invalid;
- `UNKNOWN` — completeness cannot be proven;
- `NO_DATA` — the defined source population yielded no data, without implying zero outcome.

## 5. Projection drift

```text
PROJECTION_DRIFT
= derived Observability current-state projection disagrees with authoritative owner state/reference for the same semantic scope
```

Resolution:

```text
owner state wins
→ retain drift evidence
→ rebuild/reconcile projection
```

Observability MUST NOT overwrite owner state to make the projection agree.

## 6. Data-quality issue lifecycle

Module 08 may observe data-quality issues, but v1 does not create a new global `telemetry_issue_id` unless future runtime needs justify it.

Issues may be represented as Events/health records with attributable scope.

## 7. Orphan references

An unresolvable domain ref is not automatically proof the domain entity never existed.

Possible causes:

- delayed source synchronization;
- retention;
- wrong project/version;
- malformed ref;
- owner data unavailable.

The condition remains an Observability integrity problem until resolved.

## 8. Metric impact

A Metric Observation affected by source gaps MUST propagate the appropriate observation/completeness state.

It MUST NOT silently convert missing source data to zero.

## 9. Trace impact

A Trace with known required missing Spans/Events is `INCOMPLETE`.

A Trace without a complete capture expectation is generally `UNKNOWN` completeness, not automatically complete.
