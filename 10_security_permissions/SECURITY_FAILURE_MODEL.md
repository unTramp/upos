# Security Failure Model

**ID:** UPOS-10-SFM-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Purpose

Security failures classify why permission evaluation/action protection cannot proceed. UPOS-010 owns the security meaning; UPOS-004 owns orchestration response.

## 2. Canonical failure taxonomy

| Code | Meaning | Security result tendency |
|---|---|---|
| `PERMISSION_DENIED` | applicable policy definitively forbids action | DENY |
| `MISSING_REQUIRED_GRANT` | required grant absent/inactive | CONDITIONAL or DENY per policy |
| `GRANT_EXPIRED` | needed grant expired | CONDITIONAL / DENY |
| `GRANT_REVOKED` | needed grant revoked | DENY |
| `POLICY_CONFLICT` | active applicable rules conflict without canonical resolution | BLOCKED |
| `POLICY_NOT_FOUND` | required policy/owner cannot be resolved | UNKNOWN/BLOCKED |
| `PROTECTED_ACTION_BLOCKED` | required protected-action condition not satisfied | CONDITIONAL/BLOCKED |
| `HUMAN_APPROVAL_REQUIRED` | policy requires external Human decision | CONDITIONAL |
| `HUMAN_APPROVAL_MISSING` | required approval absent/not current | CONDITIONAL |
| `SOD_VIOLATION` | external SoD rule would be violated | DENY |
| `AUTHORITY_REQUIRED` | required organizational authority ref absent | CONDITIONAL/BLOCKED |
| `SECRET_ACCESS_DENIED` | secret use/read prohibited | DENY |
| `SENSITIVE_CONTEXT_DENIED` | requested sensitive Context exposure prohibited | DENY or redacted alternative if policy defines |
| `PRODUCTION_ACCESS_DENIED` | protected production action forbidden | DENY |
| `INVALID_EXCEPTION` | exception cannot apply | no relaxation; evaluate base policy |
| `UNKNOWN_SECURITY_CONTEXT` | material security input unknown | UNKNOWN/BLOCKED |
| `RESOURCE_SCOPE_MISMATCH` | subject/grant/decision does not cover exact target | DENY |
| `PERMISSION_STALE` | prior decision no longer reusable | BLOCKED until re-evaluated |
| `BREAK_GLASS_CONDITION_MISSING` | emergency path incomplete | CONDITIONAL/BLOCKED |
| `PROVIDER_ENFORCEMENT_UNAVAILABLE` | required provider/IAM state cannot be verified/applied | BLOCKED |
| `AUDIT_REQUIREMENT_UNSATISFIABLE` | action requires audit controls unavailable | BLOCKED/DENY per policy |

## 3. Deterministic interpretation

```text
definitive applicable prohibition
→ DENY

potentially satisfiable missing condition
→ CONDITIONAL

required authoritative prerequisite unavailable/conflicted
→ BLOCKED

no authoritative coverage resolvable
→ UNKNOWN
```

Only `ALLOW` permits execution.

## 4. Workflow response boundary

UPOS-010 returns Security result/failure reason.

UPOS-004 decides whether to:

```text
wait
block
escalate
reroute
reclassify
cancel
```

UPOS-010 MUST NOT encode those Workflow transitions.
