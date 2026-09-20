# Runtime Persistence Boundary

**ID:** UPOS-RUNTIME-PER-001  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Baseline:** U-POS v1.0.0

## 1. Principle

```text
DATABASE
!=
SEMANTIC OWNER
```

Phase 3 defines durability obligations and persistence boundaries. It does not select storage technology or define tables.

## 2. Persistence classes

```text
DURABLE_OWNER_RECORD
IMMUTABLE_SNAPSHOT
RUNTIME_WORKING_STATE
CACHE_ONLY
EXTERNAL_PROVIDER_STATE
EVENT_HISTORY
DERIVED_PROJECTION
```

`EVENT_HISTORY` and `DERIVED_PROJECTION` identify Phase-5 storage concerns.

## 3. Slice-1 guidance

- Task runtime — durable owner state and attributable transition provenance.
- Routing Decision — immutable durable snapshot.
- Workflow Instance / Stage — durable owner state where execution must survive process restart.
- Agent Run attribution — durable governed attribution.
- Execution Attempt — durable terminal execution record; mutable only while non-terminal.
- Skill Invocation attribution/result refs — durable attribution metadata as required for audit.
- Runtime Outcome/Failure — durable where required to reconstruct a governed operation.
- Event — Phase 3 defines emission; durable Event Store belongs to Phase 5.

## 4. Cache rule

Cache is never canonical truth.

A cache entry MUST remain replaceable/rebuildable and MUST NOT become the semantic source of owner state.

## 5. Provider state

Provider-native state may be referenced as `EXTERNAL_PROVIDER_STATE`.

Provider storage semantics do not redefine U-POS owner semantics.

## 6. Non-scope

No Phase-3 persistence standard may introduce:

- SQL tables;
- ORM models;
- database migrations;
- queue implementation;
- Event Store implementation;
- projection database.

## 7. Normative sources

- `00_system/GLOBAL_OWNERSHIP_MATRIX.md`
- `05_context_memory/CONTEXT_MEMORY_LIFECYCLE.md`
- `06_engineering_governance/ENGINEERING_LIFECYCLE_AND_VERSIONING.md`
- `08_observability/OBSERVABILITY_LIFECYCLE_AND_VERSIONING.md`
