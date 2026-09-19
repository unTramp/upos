# Observability Event Standard

**ID:** UPOS-08-EVT-001  
**Type:** EVENT CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0  
**Related:** `templates/OBSERVABILITY_EVENT_TEMPLATE.md`

## 1. Event identity

Every durable Observability Event MUST have stable:

```text
event_id
```

The same logical Event redelivered/reingested MUST reuse the same `event_id` when the producer/adapter can identify it.

A corrected observation is a **new Event with a new `event_id`** and an explicit correction relation.

## 2. Minimum Event envelope

Every durable Event MUST include or explicitly mark non-applicable where appropriate:

```text
event_id
event_type
event_class
event_schema_version

event_contract_ref
event_contract_version

occurred_at
recorded_at
ingested_at                         # optional before collector ingestion

time_source_ref                    # where externally available
timestamp_quality                   # EXACT / APPROXIMATE / UNKNOWN

producer_module
producer_component_ref
producer_contract_ref
producer_contract_version

domain_owner_module

initiator_type
initiator_ref
producer_role_ref                   # where applicable
producer_agent_run_ref              # where applicable
agent_instance_ref                  # where applicable

trace_id
span_id
parent_span_id                      # where applicable
correlation_id
causation_event_id                  # where explicitly known
causation_basis

project_id

task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id

skill_id
skill_version
skill_invocation_ref

context_request_id
context_bundle_id

engineering_change_id
repository_change_unit_id
workspace_id
commit_ref
integration_request_ref
revision_ref
check_ref
merge_operation_id

quality_assessment_id
evidence_record_id
finding_id
quality_gate_id
quality_gate_result_id
quality_exception_id

primary_domain_entity_type
primary_domain_entity_ref
primary_domain_state_ref
related_domain_refs

event_payload
owner_reason_code
owner_result_ref
owner_status_ref

failure_owner_module
failure_code
failure_ref

source_provenance_refs

telemetry_importance
capture_policy_ref
capture_policy_version
sampling_policy_ref
sampling_decision_ref

security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref

correction_of_event_id
correction_reason
```

The large envelope is a semantic superset. Non-applicable cross-module references MUST be `N/A`/omitted according to the future schema contract; they MUST NOT be fabricated.


## 2.1 Security handling metadata

Security/privacy handling constraints are consumed from UPOS-010 and governed project policy; UPOS-008 does not define their substantive meaning.

```text
security_policy_ref + security_policy_version
→ canonical policy basis

sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
→ optional policy-scoped handling references/directives
```

These references constrain telemetry capture, projection visibility and retention behavior. UPOS-008 owns observability mechanics; UPOS-010 owns security handling semantics; UPOS-011 binds concrete enforcement/storage/provider mechanisms.

## 3. Producer attribution

`producer_module` identifies the module/runtime boundary emitting the Observability Event.

It MUST NOT be interpreted as domain ownership.

`producer_component_ref` MAY identify an Agent runtime, adapter, CI collector, repository webhook adapter, Workflow runtime, or other emitting component.

## 4. Initiator attribution

`initiator_type` canonical v1 values:

```text
AGENT_RUN
HUMAN
SYSTEM_COMPONENT
EXTERNAL_PROVIDER
SCHEDULED_SYSTEM
UNKNOWN
N/A
```

`initiator_ref` MUST use an externally owned identity/reference where one exists.

The Event producer MUST NOT invent a Human/Agent identity when it is unknown.

## 5. Domain ownership attribution

`domain_owner_module` identifies the module whose semantics define the observed entity/result.

Examples:

```text
UPOS-004 → Workflow transition
UPOS-005 → Context Bundle invalidation
UPOS-006 → Merge Operation
UPOS-007 → Quality Assessment completion
```

## 6. Primary and related domain entities

Every domain Event SHOULD identify one primary domain entity when a meaningful owner entity exists.

Operations affecting several entities MAY also carry `related_domain_refs`.

Primary attribution MUST remain explicit; a bag of related IDs is not sufficient.

## 7. Owner result/status references

Observability MUST preserve owner-module status/result references rather than translate them into competing Observability states.

Example:

```text
owner_status_ref = UPOS-007 Quality Assessment COMPLETED
owner_result_ref = quality_verdict PASS
```

UPOS-008 does not redefine `COMPLETED` or `PASS`.

## 8. Event payload

`event_payload` contains only event-specific small structured attributes not already modeled in the envelope.

Prefer references over copies.

The payload MUST NOT be used to smuggle a second copy of full domain artifacts into the Event Store.

## 9. Event immutability

Once recorded as a durable Event, the Event payload/envelope is immutable while retained.

Corrections use:

```text
new event_id
correction_of_event_id = prior event_id
correction_reason
```

The original Event remains historical subject to externally governed retention policy.

## 10. Event correction != domain correction

Correcting a telemetry record does not correct owner-domain state.

If domain state is wrong, the owning module must perform its own governed correction/change.

## 11. Event contract/version

`event_schema_version` describes representation compatibility.

`event_contract_ref/version` points to the applicable UPOS-008 Event Standard/extension contract.

`producer_contract_ref/version` identifies the producer's semantic contract version when available.

UPOS-008 v1 does **not** introduce a separate universal `event_type_version`.

Material event semantic change should be represented through:

- updated producer/domain contract version;
- updated event contract/schema version where representation changes;
- a new namespaced `event_type` where the occurrence meaning itself is incompatible.

## 12. Actor privacy / sensitive identity

The existence/shape/access of sensitive actor references is subject to UPOS-010 reconciliation.

Until then, Module 08 requires references/minimization and MUST NOT prescribe identity exposure policy.
