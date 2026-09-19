# Human Approval & Security Veto

**ID:** UPOS-10-HAV-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Human approval boundary

```text
Human Governance / who may approve
→ UPOS-002

Security requirement that approval be present
→ UPOS-010
```

UPOS-010 references an external decision/approval artifact and validates its applicability to the security request.

No `security_approval_id` is introduced in v1.

## 2. Approval does not automatically grant permission

```text
Human approval present
!= ALLOW
```

Approval may satisfy one Security condition. All other current policy conditions must still be satisfied and a current applicable `ALLOW` Permission Decision must exist.

## 3. Approval applicability

A required approval must be:

```text
from externally authorized approver/authority
applicable to exact subject/action/resource/scope
applicable to required time/window
not revoked/superseded
compatible with applicable policy
```

## 4. Security veto

Security veto requires an external authority basis from UPOS-002/project governance and an applicable Security rule.

```text
Security authority basis
+ security condition prohibiting action
→ DENY Permission Decision
+ veto_basis_ref
```

UPOS-010 MUST NOT silently invent veto authority.

## 5. Override

Human or other override authority is externally governed.

An override can affect security only if applicable Security Policy explicitly permits an override/exception path.

Otherwise:

```text
Human Override request
+ non-overridable Security DENY
→ still DENY
```

## 6. SoD enforcement

UPOS-002 owns SoD rules. UPOS-010 may technically enforce them by consuming relationship/authority references.

Example:

```text
Implementer attempting own high-risk merge
+ applicable SoD rule
→ DENY / SOD_VIOLATION
```

The source SoD rule remains UPOS-002/project policy.
