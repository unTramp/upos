# Permission Decision Template

**ID:** UPOS-10-TPL-PDS-001  
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
permission_decision_id:
permission_request_id:

decision:  # ALLOW | DENY | CONDITIONAL | BLOCKED | UNKNOWN
security_policy_ref:
security_policy_version:

subject_ref:
capability:
action:
resource_ref:
resource_scope:
resource_state_ref: N/A

applicable_grant_refs: []
security_exception_refs: []
required_authority_refs: []
required_approval_refs: []
satisfied_condition_refs: []
unsatisfied_conditions: []

protected_action_id: N/A
denial_reason_code: N/A
reason_summary:
veto_basis_ref: N/A

security_context_refs: []
basis_refs: []

effective_from:
expires_at:
revalidation_triggers: []

evaluated_by_ref:
created_at:
```
