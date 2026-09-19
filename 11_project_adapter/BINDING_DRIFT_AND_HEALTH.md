# Binding Drift and Health

**ID:** UPOS-11-BDH-001  
**Type:** DRIFT/HEALTH STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Binding drift classes

```text
REFERENCE_DRIFT
CAPABILITY_DRIFT
PROVIDER_DRIFT
COMMAND_DRIFT
PATH_DRIFT
IDENTITY_DRIFT
RESOURCE_DRIFT
SECURITY_BINDING_DRIFT
OBSERVABILITY_BINDING_DRIFT
VERSION_COMPATIBILITY_DRIFT
```

## Health state

```text
VALID
DEGRADED
UNAVAILABLE
INVALID
UNKNOWN
```

Health is not Quality.

## Drift examples

```text
repository renamed
branch removed
CI job changed
provider permission changed
secret ref unavailable
environment ID changed
tool version incompatible
provider capability withdrawn
```

## Reaction boundary

UPOS-011 detects/reports drift and may refresh technical resolution caches when safe.

It MUST NOT auto-rewrite Security Policy, Workflow, Quality rules or canonical documentation to make a drift disappear.

UPOS-008 may observe drift events/health state through its own event semantics.
