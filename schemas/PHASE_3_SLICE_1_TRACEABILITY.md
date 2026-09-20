# Phase 3 / Slice 1 — Remediation Traceability

**ID:** UPOS-P3-S1-TRACE-001  
**Status:** REMEDIATED CANDIDATE — PENDING INDEPENDENT RE-AUDIT  
**Canonical baseline:** `338692cb3677bf395e9c5f17dc3e2a3ff9793960`  
**Audited candidate:** `2a291aa5d8e76198205efbfec075bb0755dd4bfc`

## 1. Evidence taxonomy

Negative evidence is classified explicitly:

- **SCHEMA REJECT** — JSON Schema validation rejects the instance.
- **CONFORMANCE REJECT** — deterministic cross-record/runtime rule rejects an otherwise structurally valid instance.
- **POSITIVE PASS** — schema and applicable conformance checks accept the valid case.

An illustrative bad fixture alone is not rejection evidence.

## 2. Contract traceability

| Contract / invariant | Positive evidence | Negative evidence |
|---|---|---|
| Runtime Operation Control | non-empty request key; distinct result reference | empty key — SCHEMA REJECT; permission/adapter request-key=result — CONFORMANCE REJECT |
| Routing Runtime | failed evaluation before decision; execution-spine request/result separation — POSITIVE PASS | missing request key — SCHEMA REJECT; request-key=decision/result — CONFORMANCE REJECT |
| Execution Attempt | COMPLETED, FAILED, CREATED, CANCELLED — POSITIVE PASS | BLOCKED state; synthetic attempt ID; unsupported contract version — SCHEMA REJECT |
| Retry Provenance | failed predecessor → RETRY_OF → distinct CREATED successor — POSITIVE PASS | missing predecessor/trigger — SCHEMA REJECT; reused bounded identity — CONFORMANCE REJECT |
| Technical redelivery | same request key + same owner subject without RETRY_OF — POSITIVE PASS | same bounded identity encoded as RETRY_OF — CONFORMANCE REJECT |
| Event correction | new Event ID + correction relation/reason — POSITIVE PASS | missing reason — SCHEMA REJECT; correction reuses own Event ID — CONFORMANCE REJECT |
| Reconstructability | execution-spine fixture validates and cross-references canonical refs — POSITIVE PASS | persisted private reasoning — recursive CONFORMANCE REJECT |
| Runtime contract resolution | known contract IDs and supported versions resolve — POSITIVE PASS | unknown/dangling or unsupported referenced contract version — fail-closed |
| Durable version carriage | supported Execution Attempt contract/schema version — POSITIVE PASS | unsupported runtime-contract version — SCHEMA REJECT |

## 3. Owner-bound runtime contract artifacts

```text
runtime/contracts/TASK_RUNTIME_CONTRACT.md
runtime/contracts/ROUTING_RUNTIME_CONTRACT.md
runtime/contracts/WORKFLOW_INSTANCE_RUNTIME_CONTRACT.md
runtime/contracts/EXECUTION_ATTEMPT_RUNTIME_CONTRACT.md
runtime/contracts/AGENT_RUN_ATTRIBUTION_CONTRACT.md
runtime/contracts/SKILL_INVOCATION_ATTRIBUTION_CONTRACT.md
runtime/contracts/EVENT_EMISSION_INTERFACE.md
runtime/contracts/RETRY_PROVENANCE_RUNTIME_CONTRACT.md
```

The extra Retry Provenance contract binds the already-authorized UPOS-04 retry-provenance durable schema to an explicit runtime contract/version; it does not create a new domain identity or semantic owner.

## 4. Version carriage

The six durable families called out by the blind audit can carry:

```text
runtime_contract_ref
runtime_contract_version
runtime_schema_version
```

Their values are constrained to the supported Slice-1 contract/schema version where present.

## 5. Phase boundary

Not implemented:

```text
orchestrator / scheduler / execution engine
automatic retry/rework/recovery
Event Store
trace creation/propagation/span runtime
provider adapters
database implementation
Control Plane/dashboard
Phase-3 Slice 2+
```

## 6. Re-audit handoff

This traceability document records remediation evidence only.

It does not substitute for independent closure of F-01…F-05, a stability decision, merge, or STABLE promotion.
