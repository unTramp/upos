# Adapter Failure Model

**ID:** UPOS-11-AFM-001  
**Type:** FAILURE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Failure classes

```text
BINDING_NOT_FOUND
BINDING_AMBIGUOUS
BINDING_CONFLICT
PROVIDER_UNAVAILABLE
CAPABILITY_UNSUPPORTED
REFERENCE_NOT_FOUND
COMMAND_NOT_AVAILABLE
PATH_INVALID
IDENTITY_UNRESOLVED
RESOURCE_UNRESOLVED
SECRET_BINDING_UNAVAILABLE
SECURITY_BINDING_INVALID
OBSERVABILITY_BINDING_INVALID
VERSION_INCOMPATIBLE
PROVIDER_AUTH_FAILURE
CONFIGURATION_INVALID
BINDING_DRIFT_DETECTED
```

## Failure contract

```text
failure_code
binding_ref where applicable
provider_adapter_ref/version where applicable
abstract_requirement_ref
affected scope
safe provider error ref/details
retryability_hint where technically known
observability refs
```

`retryability_hint` is not Workflow orchestration.

UPOS-004 decides retry/reroute/wait/abort behavior.

Provider-native errors are preserved by reference when safe.
