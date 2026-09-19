# Protected Action Standard

**ID:** UPOS-10-PAS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Definition

A Protected Action is one concrete security-sensitive action instance requiring policy-defined controls beyond ordinary possession of a Capability.

```text
PROTECTED ACTION != WORKFLOW GATE
PROTECTED ACTION != CHANGE CLASS
PROTECTED ACTION != PERMISSION DECISION
```

## 2. Identity

```text
protected_action_id
```

The identity addresses the concrete protected action instance, not a universal action class.

## 3. Minimum contract

```text
protected_action_id
status

action_type
capability
resource_type
resource_ref
resource_scope
resource_state_ref

subject_ref
agent_run_id
task_id
workflow_instance_id
stage_id

change_class_ref
security_policy_ref
security_policy_version

required_capabilities
required_authority_refs
required_approval_refs
required_quality_or_external_gate_refs
required_grant_refs
required_security_context_conditions
security_exception_refs

permission_request_ref
permission_decision_ref

execution_constraints
audit_requirement_refs
execution_result_ref

created_at
authorized_at
executed_at
expires_at
```

## 4. Lifecycle

Minimal action-local lifecycle:

```text
REQUESTED
AUTHORIZED
EXECUTED
FAILED
CANCELLED
EXPIRED
```

`AUTHORIZED` requires a current applicable `ALLOW` Permission Decision.

This lifecycle tracks the protected action only and MUST NOT duplicate Workflow stage/state.

## 5. Typical protected classes

Examples, subject to project policy:

```text
merge/write protected target
history rewrite
production write/deploy/admin
secret rotation/administration
destructive data action
permission administration
security-policy change
break-glass elevation
```

## 6. Change Class boundary

UPOS-004 Change Class and UPOS-010 Protected Action are independent dimensions.

```text
C5 change may contain several protected actions.
Low-change-class work may still request one highly protected action.
```

## 7. Execution

UPOS-010 does not execute the operation. It records the security contract/authorization requirements and references external execution/outcome artifacts.
