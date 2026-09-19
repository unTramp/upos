# Grant Standard

**ID:** UPOS-10-GRT-001  
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

A Grant is a bounded technical allowance substrate.

```text
GRANT != ORGANIZATIONAL AUTHORITY
GRANT != ORGANIZATIONAL DELEGATION
GRANT != CURRENT PERMISSION DECISION
```

## 2. Identity

```text
grant_id
```

## 3. Minimum contract

```text
grant_id
status

subject_ref
role_ref
agent_run_scope_ref
task_scope_ref
workflow_scope_ref
stage_scope_ref

capability
allowed_actions
resource_type
resource_ref
resource_scope

conditions
security_policy_ref
security_policy_version
originating_permission_decision_ref
originating_authority_or_delegation_ref

created_at
effective_from
expires_at
revoked_at
revocation_reason
supersedes
replacement
status_history
```

## 4. Lifecycle

Canonical v1 states:

```text
PENDING
ACTIVE
SUSPENDED
EXPIRED
REVOKED
SUPERSEDED
```

Only `ACTIVE` may satisfy a current decision input.

## 5. Lifecycle semantics

- `PENDING` — grant record exists but is not effective.
- `ACTIVE` — effective within exact scope/conditions/time.
- `SUSPENDED` — temporarily unavailable; may later return to ACTIVE if policy allows.
- `EXPIRED` — terminal expiry due time/end condition.
- `REVOKED` — terminal administrative/security revocation.
- `SUPERSEDED` — replaced by another grant identity.

All status changes preserve append-only history.

## 6. Time-bounded access

Elevated/production/secret-admin grants SHOULD be temporary by default.

Indefinite standing privilege requires explicit project/security policy justification.

## 7. Invalidation/revocation triggers

Potential triggers include:

```text
Agent Run ended
Task completed/cancelled
Workflow rerouted materially
Role/authority changed
resource scope changed
policy version changed
approval revoked
risk/security context increased
security incident
manual authorized revocation
expiry
```

The exact trigger set is policy-specific.

## 8. Technical delegation

A technical Grant may be created from an externally governed organizational delegation only when:

```text
delegation/authority ref exists
+ Security Policy permits technical grant
```

The Grant does not expand the organizational delegation.

## 9. Supersession

Material scope/capability/subject/lifetime changes create a new `grant_id` and supersede the old Grant rather than silently rewriting historical authorization.
