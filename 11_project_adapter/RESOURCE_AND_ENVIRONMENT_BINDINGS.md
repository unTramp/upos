# Resource and Environment Bindings

**ID:** UPOS-11-REB-001  
**Type:** RESOURCE/ENVIRONMENT BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Resource Binding

```text
binding_id
abstract_resource_ref
resource_type
provider_adapter_ref/version
provider_resource_ref
scope
environment_ref
security_resource_ref
validation_state
```

## Environment Binding

```text
binding_id
abstract_environment_ref
project_environment_name
provider_environment_ref
security_policy_ref
resource_binding_refs
```

Universal semantics do not require the literal names `dev`, `staging`, `prod`.

## Protected resources

A concrete resource may be marked as the implementation target of an abstract protected resource, but its protection/permission semantics remain UPOS-010.
