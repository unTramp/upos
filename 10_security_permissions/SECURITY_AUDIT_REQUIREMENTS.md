# Security Audit Requirements

**ID:** UPOS-10-AUD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Ownership boundary

UPOS-010 defines **which security facts/actions must be auditable and which metadata must be available**.

UPOS-008 owns event schemas, traces, storage, metrics, dashboards and audit projection mechanics after reconciliation.

## 2. Audit-relevant semantic records

At minimum:

```text
Permission Request
Permission Decision
Grant creation/activation/suspension/expiry/revocation/supersession
Protected Action authorization/execution outcome
Security Exception lifecycle/use
Security veto / DENY basis
Break-glass use
secret/sensitive-data access decision metadata
production privileged access
privilege elevation
```

## 3. Minimum attributable audit metadata

Where applicable:

```text
subject_ref
role_ref
agent_run_id
task_id
workflow_instance_id
stage_id

permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id

capability
action
resource_type
resource_ref
resource_scope

security_policy_ref
security_policy_version
approval/authority refs
exception refs

decision / lifecycle result
reason code
execution/outcome ref
occurred/evaluated timestamp
```

## 4. Secret minimization

Audit payload MUST NOT contain raw secret values.

Use:

```text
secret_ref
classification
operation type
decision/outcome
```

## 5. Sensitive-data minimization

Audit should be sufficient for attribution/reconstruction without copying protected payload content unnecessarily.

## 6. Reproducibility support

Audit/provenance should make it possible to answer:

```text
who/what requested this?
what exact protected capability/action/resource?
which policy version applied?
which approvals/grants/exceptions mattered?
why was it allowed/denied/blocked/conditional/unknown?
what was the execution result reference?
```

## 7. Reconciled UPOS-008 interface

The semantic field requirements above are normative UPOS-010 requirements.

For security-constrained telemetry/audit records, UPOS-010 may supply:

```text
security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

UPOS-008 owns concrete Event/audit schema, storage, projection and retention mechanics while honoring those constraints. UPOS-011 binds concrete enforcement/provider mechanisms.

```text
UPOS-010 security constraint semantics
!=
UPOS-008 retention/storage mechanics
```
