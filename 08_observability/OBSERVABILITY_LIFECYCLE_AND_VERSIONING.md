# Observability Lifecycle and Versioning

**ID:** UPOS-08-LCV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Event lifecycle

A durable Event is append-only/immutable while retained.

There is no mutable Event lifecycle state machine.

Correction uses a new Event and relation to the prior Event.

Retention/archive/deletion mechanics are owned by UPOS-008 and constrained by reconciled UPOS-010/project security policy; UPOS-011 binds concrete storage/enforcement.

## 2. Trace/Read Model lifecycle

Trace materializations and Read Models are projections, not immutable domain truth.

They may be recomputed as source data changes/arrives.

Projection revisions MUST preserve:

```text
projection_definition_ref/version
data_revision
recomputed_at / last_updated_at
source watermark/coverage
```

## 3. Metric Definition lifecycle

```text
DRAFT
→ REVIEW
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

A materially changed formula/population/window/unknown-handling rule requires a new Metric Definition version.

## 4. Semantic versioning

For Module-08 Definitions/Standards:

```text
MAJOR = breaking semantic contract change
MINOR = backward-compatible semantic expansion
PATCH = editorial/nonsemantic correction
```

UPOS-008 v1.0 is frozen in the coordinated interface-stable baseline; material semantic change requires a new reviewed version.

## 5. Event schema versioning

Every Event carries `event_schema_version`.

Old retained Events MUST remain interpretable by version-aware consumers for as long as they are retained under policy.

## 6. Unknown schema

An unsupported schema version yields:

```text
UNKNOWN_SCHEMA_VERSION
```

The Event MUST NOT be silently parsed as the newest schema.

## 7. Projection versioning

Material projection logic change requires a new `projection_definition_ref/version`.

The same historical Event stream may produce a new projection version without changing source Events.

## 8. Historical metrics

Historical Metric Observations retain the Metric Definition version actually used.

A new Definition version does not silently rewrite old observations.

Recomputation under a newer definition is a distinct observation cohort/version.

## 9. Reconciliation lifecycle

The v1 reconciliation registers for UPOS-009/010/011 are closed.

Future interface changes require explicit versioned reconciliation and MUST NOT silently reinterpret the frozen v1 Event/Trace/Metric contracts.
