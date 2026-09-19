# Observability Event Template

**Template owner:** UPOS-008 Observability  
**Conforms to:** `EVENT_STANDARD.md`

```text
event_id:
event_type:
event_class:
event_schema_version:

event_contract_ref:
event_contract_version:

occurred_at:
recorded_at:
ingested_at: N/A

time_source_ref: N/A
timestamp_quality:

producer_module:
producer_component_ref:
producer_contract_ref:
producer_contract_version:

domain_owner_module:

initiator_type:
initiator_ref: N/A
producer_role_ref: N/A
producer_agent_run_ref: N/A
agent_instance_ref: N/A

trace_id:
span_id:
parent_span_id: N/A
correlation_id:
causation_event_id: N/A
causation_basis:

project_id:

task_id: N/A
routing_decision_id: N/A
workflow_instance_id: N/A
stage_id: N/A
transition_id: N/A

skill_id: N/A
skill_version: N/A
skill_invocation_ref: N/A

context_request_id: N/A
context_bundle_id: N/A

engineering_change_id: N/A
repository_change_unit_id: N/A
workspace_id: N/A
commit_ref: N/A
integration_request_ref: N/A
revision_ref: N/A
check_ref: N/A
merge_operation_id: N/A

quality_assessment_id: N/A
evidence_record_id: N/A
finding_id: N/A
quality_gate_id: N/A
quality_gate_result_id: N/A
quality_exception_id: N/A

primary_domain_entity_type:
primary_domain_entity_ref:
primary_domain_state_ref: N/A
related_domain_refs: []

event_payload: {}
owner_reason_code: N/A
owner_result_ref: N/A
owner_status_ref: N/A

failure_owner_module: N/A
failure_code: N/A
failure_ref: N/A

source_provenance_refs: []

telemetry_importance:
capture_policy_ref:
capture_policy_version:
sampling_policy_ref: N/A
sampling_decision_ref: N/A

security_policy_ref: N/A
security_policy_version: N/A
sensitivity_class_ref: N/A
redaction_directive_ref: N/A
access_constraint_ref: N/A
retention_constraint_ref: N/A

correction_of_event_id: N/A
correction_reason: N/A
```
