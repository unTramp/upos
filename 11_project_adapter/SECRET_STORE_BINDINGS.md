# Secret Store Bindings

**ID:** UPOS-11-SSB-001  
**Type:** SECRET BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-010 Secret and Sensitive Data Standard


## Contract

```text
binding_id
secret_ref
secret_store_adapter_ref/version
provider_secret_identifier_ref
allowed_use_mode
injection_mechanism_ref
environment_scope
validation_state
```

## Allowed modes

Implementation MAY support:

```text
USE_WITHOUT_DISCLOSURE
REFERENCE_ONLY
DISCLOSE_TO_AUTHORIZED_TOOL
```

only as permitted by UPOS-010.

## Raw secret rule

```text
RAW SECRET VALUE
MUST NOT be stored in Project Manifest,
Binding artifacts,
Observability telemetry,
Learning artifacts,
or normal Context by default.
```

Validation may verify existence/accessibility without returning the value.
