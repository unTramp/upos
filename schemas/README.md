# U-POS Machine-Readable Schema Layer

**Phase:** 2A — Schema Governance & Identity Foundation  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Last reviewed:** 2026-09-20

## Purpose

This directory is the machine-readable representation layer for U-POS.

It exists to make frozen U-POS contracts validatable and executable by software without creating a second semantic source of truth.

The governing relationship is:

```text
U-POS owner-module normative contract
        ↓
machine-readable schema
        ↓
validated instance
        ↓
runtime implementation
```

Never:

```text
schema convenience
        ↓
new domain meaning
```

## Authority

The frozen U-POS v1.0.0 owner modules remain authoritative for semantics.

```text
SCHEMA != DOMAIN TRUTH
SCHEMA REGISTRY != SEMANTIC OWNER
SERIALIZATION FIELD != NEW ENTITY
VALID INSTANCE != AUTHORIZED ACTION
```

If a schema and its owning normative contract disagree, the discrepancy is a schema defect unless the owner module has first been changed through governed U-POS evolution.

## Baseline protection

Files under `01_documentation_system/` through `11_project_adapter/` and `legacy_sources/` remain protected by the v1.0.0 frozen-baseline verifier.

The schema layer is additive and lives outside those scopes.

## Phase 2 sequence

```text
2A  Schema Governance + Identity/Reference Foundation
2B  Documentation Authority machine-readable contracts
2C  Project Manifest + Project Adapter schemas
2D  Execution Backbone schemas
    Task → Routing → Workflow → Agent Run → Context
```

Runtime, orchestrator, event-store, provider adapters, CLI and Control Plane are out of scope for Phase 2A.

## Governance documents

- `SCHEMA_GOVERNANCE.md`
- `IDENTITY_AND_REFERENCE_CONVENTIONS.md`
- `SCHEMA_VERSIONING_AND_COMPATIBILITY.md`
- `SCHEMA_REGISTRY.md`
- `PHASE_2A_ACCEPTANCE.md`

## Required traceability

Every concrete schema introduced after this foundation MUST identify:

```text
schema key
schema version
owner module
U-POS baseline
normative source(s)
artifact path
compatibility status
implementation status
```

A schema that cannot identify its semantic owner MUST NOT be promoted to stable use.
