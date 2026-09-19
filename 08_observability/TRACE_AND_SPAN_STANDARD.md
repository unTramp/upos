# Trace and Span Standard

**ID:** UPOS-08-TRC-001  
**Type:** TRACE / SPAN STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0  
**Related:** `templates/TRACE_TEMPLATE.md`, `templates/SPAN_TEMPLATE.md`

## 1. Trace identity

Every Trace has stable:

```text
trace_id
```

A Trace ID is a propagation/correlation identity, not a Workflow identity.

## 2. Trace scope

A Trace SHOULD represent one causally coherent technical/operational execution boundary.

Possible boundaries:

- one Agent Run;
- one Stage execution segment;
- one multi-tool Skill Invocation;
- one cross-service operation;
- a larger execution segment where propagation remains coherent.

Universal rules MUST NOT assume:

```text
1 Task = 1 Trace
1 Workflow Instance = 1 Trace
```

## 3. Trace projection minimum contract

A materialized Trace representation SHOULD support:

```text
trace_id
trace_contract_ref
trace_contract_version
correlation_id
project_id
root_span_id where known
related_trace_refs

task_id
workflow_instance_id
stage_id
agent_run_id
skill_invocation_ref

started_at
ended_at
observed_duration

span_refs
completeness_state
completeness_basis_ref

data_revision
last_recomputed_at
known_limitations
```

The materialized Trace is a rebuildable projection; late Events/Spans may increase `data_revision` without mutating historical Events.

## 4. Span identity

Every Span has stable:

```text
span_id
```

and belongs to one:

```text
trace_id
```

## 5. Span contract

A Span SHOULD support:

```text
span_id
trace_id
parent_span_id

span_type
operation_name

started_at
ended_at
measured_duration

producer_component_ref
role_id
agent_run_id
agent_instance_ref
skill_invocation_ref

task_id
workflow_instance_id
stage_id

primary_domain_entity_type
primary_domain_entity_ref
related_domain_refs

span_status
owner_result_ref
failure_owner_module
failure_code
failure_ref

resource_usage_refs
source_event_refs
known_limitations
```

## 6. Span types

Representative provider-neutral types:

```text
AGENT_RUN
SKILL_INVOCATION
CONTEXT_ASSEMBLY
TOOL_CALL
EXTERNAL_PROVIDER_CALL
ENGINEERING_OPERATION
CHECK_EXECUTION
REVIEW_EXECUTION
QA_EXECUTION
MERGE_OPERATION
GENERIC_OPERATION
```

This is not an owner-domain lifecycle taxonomy.

## 7. Span status

Canonical Observability-local status:

```text
OK
ERROR
CANCELLED
UNKNOWN
```

```text
span_status
!= Workflow Stage state
!= Skill Result class
!= Quality Verdict
!= owner failure taxonomy
```

`ERROR` means the bounded observed operation reported/experienced an execution error; owner failure details remain referenced externally.

## 8. Trace completeness

Canonical v1 projection values:

```text
COMPLETE
INCOMPLETE
UNKNOWN
```

Completeness MUST be evaluated against capture/producer expectations where available.

A Trace is not `COMPLETE` merely because it has a root Span and no obvious gaps.

## 9. Trace propagation contract

Provider-neutral propagation SHOULD carry where supported:

```text
trace_id
span_id
correlation_id
causation reference
```

Concrete headers, SDK APIs and propagation carriers belong to UPOS-011/runtime.

## 10. Unsupported propagation

If an external tool/provider cannot preserve Trace context:

- keep the known correlation/domain references;
- create a new Trace if necessary;
- link through explicit provider/job/domain refs;
- do not fabricate parentage.

## 11. Tool-call observability

Tool calls MAY be Span/Event records with:

```text
tool_class
tool_operation
provider_binding_ref
start/end/duration
result class
failure refs
usage refs
```

Do not persist unrestricted request/response bodies by default.
