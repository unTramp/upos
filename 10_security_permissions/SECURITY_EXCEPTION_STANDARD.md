# Security Exception Standard

**ID:** UPOS-10-SES-001  
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

A Security Exception is a bounded externally authorized departure from an applicable Security Policy rule.

```text
SECURITY EXCEPTION != POLICY DELETION
SECURITY EXCEPTION != POLICY CHANGE
SECURITY EXCEPTION != HUMAN APPROVAL ALONE
```

## 2. Identity

```text
security_exception_id
```

## 3. Minimum contract

```text
security_exception_id
status
status_history

affected_security_policy_ref
affected_security_policy_version
affected_rule_ref

subject_ref
capability
action
resource_type
resource_ref
resource_scope
resource_state_ref
execution_scope_refs

reason
scope
compensating_controls

authorizing_authority_ref
decision_ref

created_at
approved_at
effective_from
expires_at
review_trigger
revoked_at

supersedes
replacement

audit_requirement_refs
```

## 4. Lifecycle

```text
DRAFT
APPROVED
ACTIVE
EXPIRED
REVOKED
SUPERSEDED
INVALID
```

Only `ACTIVE` may be used to relax an exception-eligible policy rule.

Approval authority is external; UPOS-010 validates/reference semantics only.

## 5. Exact scope

Exception applicability is exact and bounded by:

```text
policy/rule version
subject
capability/action
resource/scope/state
execution scope
time
compensating controls
```

An Exception MUST NOT silently float to broader resources, new policy versions or later unrelated actions.

## 6. Historical semantics

An Exception authorized after a historical Permission Decision cannot retroactively turn `DENY` into `ALLOW`.

A new Permission Request/Decision is required for current use.

## 7. Immutability

After `APPROVED`, substantive exception scope/reason/authority/compensating controls are immutable for that ID.

Material change requires a new/superseding `security_exception_id`.

Status transitions remain append-only history.

## 8. Invalid exception

Examples:

```text
expired
revoked
wrong subject/resource/scope
wrong policy version
missing external authority
compensating control not satisfied
policy marks rule non-exceptionable
```

Such an Exception contributes no permission.
