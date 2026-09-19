# Identity and Subject Bindings

**ID:** UPOS-11-ISB-001  
**Type:** IDENTITY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Purpose

Resolve U-POS organizational/security identities to concrete runtime/provider principals.

Potential concrete subjects:

```text
GitHub App installation
service account
OIDC subject
cloud IAM principal
CI identity
local OS identity
human provider identity
```

## Contract

```text
binding_id
upos_subject_ref
role_or_agent_ref where applicable
provider_adapter_ref/version
provider_identity_ref
scope
environment_ref
validation_state
```

## Hard invariant

```text
IDENTITY BINDING != ORGANIZATIONAL AUTHORITY
```

Provider identity proves where an operation is executed/authenticated, not whether it is organizationally authorized.
