# UPOS-010 — Security & Permissions

**ID:** UPOS-10-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 0. Module status

```text
UPOS-010 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-008 RECONCILIATION:
COMPLETE

UPOS-009 RECONCILIATION:
COMPLETE

UPOS-011 RECONCILIATION:
COMPLETE

UPOS-010 FREEZE:
FROZEN v1.0
```

The Security & Permissions semantic architecture is frozen as part of the coordinated UPOS-008–011 v1 interface-stable baseline. Further semantic change requires a new reviewed version.

## 1. Purpose

UPOS-010 is the canonical U-POS owner for deciding whether a specific security subject may exercise a specific capability/action against a specific resource, within a specific execution/security context, under an applicable versioned security policy and any required approval/protected-action conditions.

It answers:

> Who or what may perform this concrete action on this concrete protected resource now, under which scope, duration, conditions, approvals, exceptions and audit requirements?

It does not decide organizational responsibility, Workflow ordering, Quality correctness, Context assembly, repository mechanics, telemetry projection, learning promotion, or provider-native IAM bindings.

## 2. Fundamental separation

```text
ORGANIZATIONAL AUTHORITY
!=
TECHNICAL PERMISSION
```

```text
UPOS-002
= who is organizationally authorized / responsible

UPOS-010
= whether the requested protected capability/action/resource use
  is currently security-permitted
```

Both may be required.

## 3. Critical invariants

```text
ROLE != PERMISSION
AUTHORITY != CAPABILITY GRANT
CAPABILITY != PERMISSION TO USE IT NOW
TOOL ACCESS != ACTION AUTHORIZATION
QUALITY PASS != SECURITY APPROVAL
WORKFLOW STAGE != PERMISSION
SECRET ACCESS != SECRET OWNERSHIP
HUMAN APPROVAL != AUTOMATIC PERMISSION
GRANT != ORGANIZATIONAL DELEGATION
SECURITY REVIEW != PERMISSION DECISION
PROTECTED ACTION != WORKFLOW GATE
SECURITY AUDIT REQUIREMENT != OBSERVABILITY EVENT
```

Only a current applicable `ALLOW` Permission Decision authorizes execution of the exact request. `CONDITIONAL`, `BLOCKED`, `UNKNOWN`, and `DENY` are non-executable outcomes.

## 4. Core chain

```text
Actor / Execution Identity
↓
Permission Request
↓
Requested Capability + Action
↓
Resource + Scope
↓
Security Context / Execution Scope
↓
Applicable Security Policy
↓
Grant / authority / SoD / approval / exception inputs
↓
Permission Decision
↓
Protected Action conditions if applicable
↓
ALLOW only
↓
External execution
↓
Security audit reference requirements
```

## 5. Stable Module-10 identities

UPOS-010 owns:

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
```

UPOS-010 deliberately does **not** introduce:

```text
security_approval_id
security_veto_id
security_review_result_id
security_policy_id
secret_id as a competing provider/project identity
resource_id as a competing project/provider identity
subject_id as a competing identity-provider identity
```

Human/security approvals use externally governed decision/authority references. Security veto is represented by a `DENY` Permission Decision with attributable veto/authority basis where policy gives Security that veto. Security Policy uses `security_policy_ref + security_policy_version`.

## 6. Permission result vocabulary

```text
ALLOW
DENY
CONDITIONAL
BLOCKED
UNKNOWN
```

Only `ALLOW` authorizes the action.

- `ALLOW` — all security conditions are satisfied now for the exact request and validity window.
- `DENY` — an applicable rule definitively forbids the requested action.
- `CONDITIONAL` — the action could become allowable if explicit listed conditions become satisfied; execution is not yet authorized.
- `BLOCKED` — evaluation cannot validly complete because a required authoritative prerequisite is missing/conflicted/unavailable.
- `UNKNOWN` — no authoritative applicable security rule/context can be resolved; for protected capability use, default-deny behavior applies and execution is not authorized.

## 7. Default-deny rule

For a protected capability/action:

```text
not explicitly and currently permitted
→ not executable
```

This does not collapse `DENY`, `BLOCKED`, and `UNKNOWN` into one semantic state. They remain distinguishable for remediation and audit.

## 8. Ownership boundary

```text
canonical truth / policy source ownership       → UPOS-01
Role / authority / delegation / SoD             → UPOS-002
Skill procedure / capability requirement        → UPOS-003
Workflow ordering / wait / block / reroute      → UPOS-004
Context assembly / representation               → UPOS-005
repository / merge / engineering mechanics      → UPOS-006
Quality evidence / Verdict / readiness          → UPOS-007
events / traces / metrics / audit projection    → UPOS-008
learning candidates / promotion                 → UPOS-009 + UPOS-01
Security & Permission semantics                 → UPOS-010
provider IAM / secret stores / environment IDs  → UPOS-011
```

## 9. Read order

1. `SECURITY_PERMISSIONS_OPERATING_MODEL.md`
2. `SECURITY_ONTOLOGY.md`
3. `SUBJECT_AND_IDENTITY_INTERFACE.md`
4. `CAPABILITY_MODEL.md`
5. `RESOURCE_AND_ACTION_MODEL.md`
6. `SECURITY_POLICY_STANDARD.md`
7. `PERMISSION_REQUEST_STANDARD.md`
8. `PERMISSION_DECISION_STANDARD.md`
9. `GRANT_STANDARD.md`
10. `LEAST_PRIVILEGE_STANDARD.md`
11. `PROTECTED_ACTION_STANDARD.md`
12. `HUMAN_APPROVAL_AND_VETO.md`
13. `SECRET_AND_SENSITIVE_DATA_STANDARD.md`
14. `PRODUCTION_ACCESS_STANDARD.md`
15. `SECURITY_EXCEPTION_STANDARD.md`
16. `SECURITY_FAILURE_MODEL.md`
17. `SECURITY_AUDIT_REQUIREMENTS.md`
18. `SECURITY_LIFECYCLE_AND_VERSIONING.md`
19. `CROSS_MODULE_INTERFACES.md`
20. `MODULE_10_TRACEABILITY.md`
