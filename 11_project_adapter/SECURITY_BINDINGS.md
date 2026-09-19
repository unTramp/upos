# Security Bindings

**ID:** UPOS-11-SECB-001  
**Type:** SECURITY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-010 Security & Permissions


## Mappings

UPOS-011 binds:

```text
Security Subject → concrete provider identity
universal Capability → provider-native mechanism/scope
Security Resource → physical provider/project resource
Grant enforcement requirement → runtime/provider control
Protected Action target → concrete protected resource
Approval requirement → external approval system
elevation requirement → provider authentication/elevation mechanism
break-glass requirement → concrete emergency mechanism
telemetry/audit handling constraints → concrete storage/access/redaction/retention enforcement
```

## Non-negotiable boundary

```text
provider credential/scope
!= UPOS-010 Permission Decision
```

Even if a token has broad native rights, runtime execution MUST honor the scoped UPOS-010 decision.

## Fail closed

Missing/invalid REQUIRED security binding makes the affected protected action unavailable.

UPOS-011 reports the binding failure; UPOS-004 decides orchestration response.
