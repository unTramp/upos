# UPOS-010 Interface Reconciliation Register

**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Result

```text
UPOS-008 ↔ UPOS-010 = RECONCILED
Material unresolved items = 0
```

| ID | Resolution | Status |
|---|---|---|
| `OBS-010-REC-001` | Event security basis uses `security_policy_ref/version` plus optional policy-scoped sensitivity/redaction/access/retention constraint refs. | RESOLVED |
| `OBS-010-REC-002` | Raw secrets/protected payloads are prohibited; UPOS-010 owns security handling constraints, UPOS-008 telemetry mechanics. | RESOLVED |
| `OBS-010-REC-003` | UPOS-010 may impose audit/security retention/access constraints; UPOS-008 owns Event Store retention/storage mechanics under them. | RESOLVED |
| `OBS-010-REC-004` | Observable security refs use `permission_request_id`, `permission_decision_id`, `grant_id`, `protected_action_id`, `security_exception_id` and owner result/reason refs. | RESOLVED |
| `OBS-010-REC-005` | Planned security-required Human action remains owner-attributed; Observability records owner category/ref rather than inventing Security semantics. | RESOLVED |
| `OBS-010-REC-006` | Permission-denied metrics derive only from UPOS-010 Permission Decision population/decision semantics. | RESOLVED |
| `OBS-010-REC-007` | Security projection visibility/redaction follows UPOS-010 handling constraints; no identity exposure is inferred by UPOS-008. | RESOLVED |
| `OBS-010-REC-008` | Event immutability applies while retained; policy-governed deletion/retention does not rewrite retained Event identity/history. | RESOLVED |
| `OBS-010-REC-009` | `SECURITY` read model is an UPOS-008 projection over UPOS-010 refs with security-controlled visibility. | RESOLVED |

No Permission, Grant, Security Policy, veto, exception or protected-action authority semantics are owned by UPOS-008.
