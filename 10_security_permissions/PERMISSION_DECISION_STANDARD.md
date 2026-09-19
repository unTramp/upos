# Permission Decision Standard

**ID:** UPOS-10-PDS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity

Every completed security evaluation has stable:

```text
permission_decision_id
```

A Permission Decision is an immutable evaluation snapshot for one `permission_request_id` under one exact policy/context/basis state.

## 2. Decision vocabulary

```text
ALLOW
DENY
CONDITIONAL
BLOCKED
UNKNOWN
```

### ALLOW

All applicable Security conditions are satisfied now for the exact request, scope and validity window.

`ALLOW` is the only decision state that can authorize execution.

### DENY

At least one authoritative applicable Security rule definitively forbids the request or an unexcepted security veto applies.

### CONDITIONAL

The request could become allowable if one or more explicit conditions are satisfied, for example:

```text
Human Approval ref present
required organizational authority ref present
Quality readiness ref acceptable
stronger authentication/elevation satisfied
SoD condition satisfied
specific Grant activated
```

`CONDITIONAL` is not executable. When conditions change, produce a new Permission Decision unless an explicit policy-controlled activation mechanism is defined and attributable.

### BLOCKED

Evaluation cannot validly complete because a required authoritative prerequisite is missing/conflicted/unavailable.

Examples:

```text
security policy conflict
required subject identity unresolved
required resource identity unavailable
external approval state unavailable
provider enforcement state required but unavailable
```

### UNKNOWN

No authoritative applicable security rule/context can be resolved.

For protected capability use:

```text
UNKNOWN → not executable
```

Escalate to policy/owner resolution; do not default to ALLOW.

## 3. Minimum contract

```text
permission_decision_id
permission_request_id

decision
security_policy_ref
security_policy_version

subject_ref
capability
action
resource_ref
resource_scope
resource_state_ref

applicable_grant_refs
security_exception_refs
required_authority_refs
required_approval_refs
satisfied_condition_refs
unsatisfied_conditions

protected_action_id
denial_reason_code
reason_summary
veto_basis_ref

security_context_refs
basis_refs

effective_from
expires_at
revalidation_triggers

evaluated_by_ref
created_at
```

## 4. Grant relationship

`grant_ref`/`applicable_grant_refs` may contribute to `ALLOW`, but an active Grant does not force `ALLOW` if other current policy conditions fail.

## 5. Human approval relationship

Human Approval is an external condition ref. Approval does not mutate a historical `CONDITIONAL`/`DENY` decision to `ALLOW`; current execution requires a current applicable `ALLOW` decision.

## 6. Freshness / invalidation

A prior `ALLOW` becomes non-reusable when any material decision input changes, including:

```text
subject/Role/Run state
Task/Workflow/Stage scope
resource/scope/state
policy/version
grant status/expiry
approval status
SoD relationship
exception status
security context
protection classification
```

The old Decision remains historical provenance.

## 7. Denial explainability

Material `DENY` MUST include attributable:

```text
denial_reason_code
policy/basis ref
relevant missing/prohibited condition
```

Do not rely on opaque `permission denied` where the system can safely explain the security reason.

## 8. Security veto

A scoped Security veto is represented as `DENY` with:

```text
veto_basis_ref
required external authority source
policy ref/version
```

UPOS-010 does not create veto authority itself.
