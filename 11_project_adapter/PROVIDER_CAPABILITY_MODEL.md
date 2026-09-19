# Provider Capability Model

**ID:** UPOS-11-PCM-001  
**Type:** CAPABILITY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Purpose

Maps abstract required capabilities to concrete provider mechanisms.

Example:

```text
UPOS capability: repository-write
→ provider scope/mechanism: contents:write
```

The provider-native scope is implementation metadata, not a UPOS Permission Decision.

## Capability matrix fields

```text
abstract_capability_ref
provider_adapter_ref/version
support_state
provider_native_capability_ref
constraints
required_provider_auth_ref
known_limitations
```

## Constraint

Credential breadth may exceed the semantic capability needed for one execution.

Runtime enforcement MUST still honor the narrower UPOS-010 decision.
