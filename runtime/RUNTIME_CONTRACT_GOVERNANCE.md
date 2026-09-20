# Runtime Contract Governance

**ID:** UPOS-RUNTIME-GOV-001  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Steward:** U-POS Runtime Contract Layer  
**Baseline:** U-POS v1.0.0

## 1. Purpose

Define governance for Phase-3 runtime contracts without creating a new U-POS domain owner.

```text
FROZEN OWNER SEMANTICS
→ PHASE-2 CANONICAL IDENTITY / REFERENCE
→ PHASE-3 RUNTIME REPRESENTATION
```

The runtime layer serializes, validates and transports owner semantics. It MUST NOT reinterpret them.

## 2. Ownership topology

```text
UPOS-02 → Agent Run identity / organizational attribution
UPOS-03 → Skill identity / Skill Contract / Skill Result semantics
UPOS-04 → Task/Workflow runtime semantics, execution-attempt state, retry/rework/recovery
UPOS-08 → Event/Trace/Span semantics and telemetry

cross-cutting runtime
→ representation, common envelopes, compatibility, persistence boundary, validation
```

Physical file placement MUST NOT change semantic ownership.

## 3. Identity rule

Phase-3 contracts MUST consume exact versioned Phase-2 canonical references.

They MUST NOT create a second domain identity for convenience.

Forbidden examples include:

```text
execution_attempt_id
run_attempt_id
invocation_attempt_id
runtime_error_id
generic workflow_id replacing workflow_instance_id
```

Infrastructure-only request correlation is governed separately and is not a domain identity.

## 4. Runtime-state rule

Agent Run and Skill Invocation technical execution state is owned by UPOS-04.

UPOS-02 and UPOS-03 attribution contracts MUST NOT privately own that state machine.

The narrow technical execution-attempt vocabulary is:

```text
CREATED
RUNNING
COMPLETED
FAILED
CANCELLED
```

It MUST NOT absorb Workflow, Quality, Security or Context lifecycle labels.

## 5. Result rule

```text
technical outcome
!=
owner result
```

Technical completion MUST NOT imply Quality PASS, Security ALLOW, Task DONE, Workflow COMPLETED or canonical truth.

## 6. Trace boundary

Phase 3 MAY carry canonical Trace/Span references when already available.

Phase 3 MUST NOT create or propagate trace context, manage spans, collect traces, store traces or derive trace projections.

## 7. Phase boundary

Out of scope:

```text
Phase 4: routing engine, scheduler, orchestrator, execution engine, automatic retry/rework/recovery
Phase 5: Event Store, trace runtime, collectors, projections, metric derivation
Phase 6: Git/provider/model/CI/IAM/secret-store implementations
Phase 7: Control Plane, dashboard, UI mutation APIs
```

## 8. Change governance

A Phase-3 contract change MUST identify:

- semantic owner;
- bound owner-contract version;
- bound Phase-2 schema versions;
- runtime-contract version;
- runtime-schema version where applicable;
- instance compatibility;
- semantic compatibility;
- migration requirement where applicable.

A semantic contradiction with a frozen owner contract is a planning blocker, not permission for the runtime layer to redefine the owner.

## 9. Normative sources

- `00_system/GLOBAL_OWNERSHIP_MATRIX.md`
- `00_system/GLOBAL_IDENTITY_REFERENCE_REGISTRY.md`
- frozen owner standards UPOS-02/03/04/08
- `schemas/SCHEMA_GOVERNANCE.md`
- `schemas/SCHEMA_VERSIONING_AND_COMPATIBILITY.md`
- `schemas/SCHEMA_URI_AND_REFERENCE_CONVENTIONS.md`
