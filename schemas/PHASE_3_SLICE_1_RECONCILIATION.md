# Phase 3 / Slice 1 — Remediation Reconciliation

**ID:** UPOS-P3-S1-REC-001  
**Status:** REMEDIATED CANDIDATE — PENDING INDEPENDENT RE-AUDIT  
**Canonical baseline:** `338692cb3677bf395e9c5f17dc3e2a3ff9793960`  
**Audited candidate:** `2a291aa5d8e76198205efbfec075bb0755dd4bfc`
**F-03 validated checkpoint:** `ac887a16848a5c34d9af5caec29214fe9e3ff89c`

## 1. Ownership remains unchanged

```text
UPOS-02 → Agent Run identity / organizational attribution
UPOS-03 → Skill identity / Skill Result / Invocation attribution
UPOS-04 → Task/Workflow runtime, Execution Attempt, Retry provenance
UPOS-08 → Event / Trace / Span semantics
cross-cutting runtime → representation / compatibility / validation only
```

No new semantic owner is introduced.

## 2. F-01 correction to prior evidence claim

The pre-audit candidate stated that cross-record inequalities were "validated by deterministic conformance logic". At audited HEAD that statement was false: several checks only asserted that the negative fixture contained the violation.

The repaired validator now rejects the violation itself and separately proves valid cases.

Current deterministic checks include:

```text
operation_request_key != routing_decision_ref
operation_request_key != runtime_outcome.owner_result_ref
operation_request_key != owner_result_ref
successor_ref != predecessor_ref
event_id != correction_of_event_id
private reasoning fields absent recursively
technical redelivery != RETRY_OF
```

This is conformance validation only; it does not execute routing, retry policy, Event storage, or orchestration.

## 3. F-02 retry/lifecycle reconciliation

The previous retry fixtures proved only the relation shape. The repaired evidence now ties the relation to actual attempt state:

```text
failed predecessor attempt
+ failure_ref
+ RETRY_OF trigger_ref matching that failure_ref
+ distinct successor bounded identity
+ successor CREATED attempt
```

CREATED, FAILED, CANCELLED and COMPLETED positive attempt states are all instantiated.

## 4. F-04 contract-reference reconciliation

Previously used owner-bound references such as:

```text
UPOS-04-ROUTING-RUNTIME
UPOS-04-EXECUTION-ATTEMPT
```

now resolve to repository contract artifacts. The same resolution rule applies to all runtime/Event/producer contract references exercised by Slice-1 runtime fixtures.

Resolution is fail-closed.

## 5. F-03 versioning reconciliation

Durable records identified by the audit now expose separate runtime-contract and runtime-schema version carriage.

Unsupported declared versions are rejected rather than silently interpreted as the newest supported version.

This preserves:

```text
owner semantic version
!= Phase-2 schema version
!= Phase-3 runtime contract version
!= Phase-3 runtime schema version
!= Event contract/schema version
!= implementation version
!= persistence format version
```

## 6. Registry and phase boundaries

Remediation is additive and remains inside Slice 1.

No remediation change is authorized to:

- edit frozen UPOS-001—011 sources;
- start Slice 2;
- implement Phase 4/5/6/7 runtime;
- merge PR #6;
- promote Slice-1 schemas to STABLE.

## 7. Finding status semantics

The implementation contains remediation for F-01 through F-05.

This document deliberately does **not** declare those findings independently closed and does not state an acceptance P0/P1 verdict. Closure belongs to the independent re-audit.

## 8. Required next action

After exact-HEAD validators are green:

```text
REMEDIATED CANDIDATE
→ STOP
→ independent re-audit
```
