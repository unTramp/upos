# UPOS-010 Interface Reconciliation Register

**ID:** UPOS-11-AN-R010-001  
**Type:** INTERFACE RECONCILIATION REGISTER  
**Status:** ACTIVE  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** TEMPORARY  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Baseline

```text
UPOS-010 SHA-256: c751ee3d3c44b14c84bb14378f04453fbcda38cad13b7a937239f214324d814f
UPOS-011 side: RESOLVED
```

| UPOS-010 requirement | Module-11 binding | Status |
|---|---|---|
| subject → provider identity | Identity Binding | RESOLVED |
| capability → provider mechanism/scope | Capability Binding | RESOLVED |
| resource → concrete resource | Resource Binding | RESOLVED |
| Security Policy ref | canonical policy/source binding | RESOLVED |
| Grant enforcement | Security/Provider Binding | RESOLVED |
| environment refs | Environment Binding | RESOLVED |
| secret refs/store | Secret Binding | RESOLVED |
| secure injection | Secret Binding use mechanism | RESOLVED |
| protected targets | Resource/Security Binding | RESOLVED |
| approval refs | Approval Binding | RESOLVED |
| elevation/reauth | Security Provider Binding | RESOLVED |
| break-glass | explicit Security Binding | RESOLVED |
| audit binding | Observability + Security Binding refs | RESOLVED |

## Critical invariant

```text
provider-native permission/scope
!= UPOS-010 Permission Decision
```

## Closure

```text
MATERIAL UPOS-010 ↔ UPOS-011 CONFLICTS = 0
UPOS-011-SIDE RECONCILIATION = COMPLETE
```
