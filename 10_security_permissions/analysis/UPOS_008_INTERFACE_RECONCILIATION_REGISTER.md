# UPOS-008 Interface Reconciliation Register

**ID:** UPOS-10-AN-R008-001  
**Type:** RECONCILIATION REGISTER  
**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Reconciled baseline

```text
UPOS-008 final SHA-256: e6eed6e9d7e006a5bf3a3d9baa300d8917f6d9ccb3e76c6301a9fcef1b25a0ba
```

## Result

```text
UPOS-010 ↔ UPOS-008 = RECONCILED
Material unresolved items = 0
```

Observable UPOS-010 identities/results:

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
security_policy_ref/version
decision / reason code / owner result refs
break-glass/elevation refs
secret/sensitive-data access decision metadata
```

Security handling constraints may be represented by policy-scoped sensitivity/redaction/access/retention refs. UPOS-008 owns telemetry/storage mechanics. Raw secrets/protected payload values are prohibited.

No Event/Trace/Metric/Read Model semantics are owned by UPOS-010.
