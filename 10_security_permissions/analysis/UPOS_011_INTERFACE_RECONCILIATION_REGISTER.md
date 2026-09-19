# UPOS-011 Interface Reconciliation Register

**ID:** UPOS-10-AN-R011-001  
**Type:** RECONCILIATION REGISTER  
**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Result

```text
UPOS-010 ↔ UPOS-011 = RECONCILED
Material unresolved items = 0
```

Resolved binding classes:

```text
subject refs → concrete identity/provider principals
universal capabilities → provider-native scopes/mechanisms
resource refs → physical provider/project resources
security_policy_ref → canonical project policy source binding
Grant enforcement → provider/runtime controls
environment refs → concrete environment IDs
secret refs → secret-store bindings
use-secret → secure injection mechanisms
protected targets → concrete branch/environment/resource protection
approval refs → external approval systems
reauthentication/elevation → provider identity mechanism
break-glass → concrete emergency mechanism
security handling constraints → concrete storage/access/redaction/retention enforcement
```

Provider credential breadth never substitutes for the scoped UPOS-010 Permission Decision.
