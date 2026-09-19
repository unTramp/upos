# Binding Validation Standard

**ID:** UPOS-11-BVS-001  
**Type:** VALIDATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Static validation

Checks:

```text
manifest/schema validity
required fields
binding uniqueness
reference graph
scope validity
canonical policy/source refs
version compatibility
forbidden invariant overrides
secret-value exclusion
```

## Runtime validation

Where required:

```text
provider available
provider adapter compatible
concrete resource resolves
capability supported
command available
path resolves
identity resolves
secret reference exists without disclosure
required event/trace endpoint reachable
required approval/security integration reachable
```

Runtime validation SHOULD prefer non-destructive probes.

## Result

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
INVALID
```

`VALID_WITH_WARNINGS` MUST NOT hide a missing REQUIRED binding.

## Configuration completeness

```text
COMPLETE
PARTIALLY_CONFIGURED
UNRESOLVED
INVALID
```

Completeness is separate from health.

## Semantic validation

Attempted configuration such as:

```text
disable reviewer independence
turn telemetry into Source of Truth
bypass UPOS-010 permission decision
allow Learning self-mutation
replace canonical source with convenience source
```

is `INVALID`, even if syntactically valid.
