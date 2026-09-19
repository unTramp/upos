# Repository Binding Standard

**ID:** UPOS-11-RBS-001  
**Type:** REPOSITORY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/REPOSITORY_BINDING_TEMPLATE.md


## Contract

```text
binding_id
repository_ref
repository_role

provider_adapter_ref/version
provider_repository_ref
remote_ref

workspace_strategy_ref
path_binding_refs

integration_target_binding
protected_target_refs

ci_binding_refs
security_resource_refs

validation_state
health_state
```

## Multi-repository

No monorepo/polyrepo assumption is made.

One Engineering Change may resolve different repository bindings for separate Repository Change Units.

## Git / provider boundary

```text
Git semantics → UPOS-006
GitHub/GitLab/etc mapping → UPOS-011
```

## Credentials

Credentials are referenced through Security/Secret bindings only.
