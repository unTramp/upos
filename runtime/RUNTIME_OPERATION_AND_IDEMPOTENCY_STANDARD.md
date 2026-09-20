# Runtime Operation and Idempotency Standard

**ID:** UPOS-RUNTIME-OPS-001  
**Version:** 0.1.0  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Baseline:** U-POS v1.0.0

## 1. Separation

```text
OPERATION REQUEST
!=
OPERATION ATTEMPT
!=
OWNER RESULT
```

Owner result identifiers MUST NOT be assumed to exist before execution succeeds.

## 2. operation_request_key

`operation_request_key` is a technical request-control primitive.

It:

- is not a U-POS domain identity;
- MUST NOT enter the Global Identity & Reference Registry;
- MUST NOT replace an owner identity;
- MAY exist when no owner result exists;
- MAY survive technical failure;
- MUST be reused for technical redelivery of the same logical request;
- MUST change for a new logical operation/evaluation.

Its uses are limited to duplicate-delivery protection, ambiguous-outcome recovery, technical request correlation and idempotent replay.

## 3. Natural owner identity

Where a pre-existing owner identity safely names the bounded operation, that identity is the idempotency basis and no extra technical request key is required.

Slice-1 examples:

```text
Task registration            → task_id
Workflow Instance creation   → workflow_instance_id
Agent Run start              → agent_run_id
Skill Invocation start       → skill_invocation_ref
Context Request registration → context_request_id
Event emission               → event_id
```

Routing evaluation requires `operation_request_key` because a technical failure may occur before `routing_decision_id` exists.

## 3.1 Operations requiring a technical request key

Some bounded operations have no pre-existing owner identity that safely names the
attempt, because the owner identity is minted only on success. These require
`operation_request_key`.

```text
Routing evaluation   → TECHNICAL REQUEST KEY REQUIRED
                       a technical failure may occur before routing_decision_id exists

Adapter Resolution   → TECHNICAL REQUEST KEY REQUIRED
                       adapter_resolution_id identifies the successful immutable
                       Resolved Adapter View, not a failed resolver attempt
```

Slice-2 addition: `adapter_resolution_id` is adopted by UPOS-11 for immutable
execution-time Resolved Adapter Views only. A resolution that terminates in an
Adapter Failure produces no Resolved Adapter View and therefore no
`adapter_resolution_id`, so attempt correlation is carried solely by
`operation_request_key`.

When an Adapter Resolution terminates in a material Adapter Failure, the failure
MUST physically retain that same originating `operation_request_key`. Durable
failure correlation MUST NOT depend on `RUNTIME_WORKING_STATE` request data
remaining available.

Operations owned by later slices are not enumerated here; each slice states its
own per-operation basis when the operation enters scope.

## 4. Redelivery vs retry

```text
TRANSPORT REDELIVERY
!=
NESTED TECHNICAL RETRY
!=
UPOS-04 BOUNDED-OPERATION RETRY
```

Transport redelivery reuses the same logical request identity/key.

A UPOS-04 retry occurs only after a bounded execution failure and is governed by Workflow semantics.

## 5. Concurrency

Mutable state-changing operations SHOULD carry an expected-state/precondition sufficient to detect stale concurrent mutation.

This standard defines the contract requirement only. Locking, scheduling and transaction implementation are out of scope.

## 6. Normative sources

- `04_workflow_engine/FAILURE_RETRY_RECOVERY.md`
- `10_security_permissions/PERMISSION_REQUEST_STANDARD.md`
- `10_security_permissions/PERMISSION_DECISION_STANDARD.md`
- `11_project_adapter/BINDING_RESOLUTION_STANDARD.md`
- `08_observability/EVENT_STANDARD.md`
