# Protected Action Template

**ID:** UPOS-10-TPL-PACT-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
protected_action_id:
status:  # REQUESTED | AUTHORIZED | EXECUTED | FAILED | CANCELLED | EXPIRED

action_type:
capability:
resource_type:
resource_ref:
resource_scope:
resource_state_ref: N/A

subject_ref:
agent_run_id: N/A
task_id: N/A
workflow_instance_id: N/A
stage_id: N/A

change_class_ref: N/A
security_policy_ref:
security_policy_version:

required_capabilities: []
required_authority_refs: []
required_approval_refs: []
required_quality_or_external_gate_refs: []
required_grant_refs: []
required_security_context_conditions: []
security_exception_refs: []

permission_request_ref:
permission_decision_ref: N/A

execution_constraints: []
audit_requirement_refs: []
execution_result_ref: N/A

created_at:
authorized_at: N/A
executed_at: N/A
expires_at: N/A
```
