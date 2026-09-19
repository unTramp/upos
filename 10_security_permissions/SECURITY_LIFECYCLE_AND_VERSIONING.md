# Security Lifecycle & Versioning

**ID:** UPOS-10-SLV-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity preservation

Historical security records are append-only/provenance-preserving.

Materially new semantic object/state creates a new identity where specified rather than rewriting history.

## 2. Permission Request

A materially different request creates a new `permission_request_id`.

## 3. Permission Decision

Each completed evaluation snapshot has a new `permission_decision_id`.

Historical Decision result remains interpreted as-of its evaluation time and basis state.

## 4. Grant

Lifecycle:

```text
PENDING → ACTIVE ↔ SUSPENDED
ACTIVE/SUSPENDED → EXPIRED / REVOKED / SUPERSEDED
```

Project policy may restrict transitions further. Terminal records remain historical.

## 5. Security Exception

Lifecycle:

```text
DRAFT → APPROVED → ACTIVE
ACTIVE → EXPIRED / REVOKED / SUPERSEDED / INVALID
```

Substantive authorized scope is immutable after approval.

## 6. Protected Action

Minimal action-local lifecycle:

```text
REQUESTED → AUTHORIZED → EXECUTED
                      ↘ FAILED
REQUESTED/AUTHORIZED → CANCELLED / EXPIRED
```

It is not a Workflow state machine.

## 7. Policy versioning

Permission decisions always record:

```text
security_policy_ref
security_policy_version
```

Policy change can invalidate reuse of earlier `ALLOW`/Grant unless compatibility/current-policy rules explicitly preserve it.

## 8. Expiry vs revocation

```text
EXPIRY
= validity ended because a declared time/end condition was reached

REVOCATION
= authorized action terminated validity before ordinary expiry
```

They are not interchangeable.

## 9. Historical non-retroactivity

Later:

```text
Grant revocation
Exception approval/revocation
Human approval
policy version change
subject/Role change
```

does not rewrite historical Permission Decisions. It affects current/future authorization and may require re-evaluation.
