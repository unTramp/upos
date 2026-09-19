# Binding Standard

**ID:** UPOS-11-BND-001  
**Type:** BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/BINDING_TEMPLATE.md


## Generic Binding contract

```text
binding_id
binding_type
version
status

abstract_requirement_ref

scope.project_id
scope.repository_ref
scope.environment_ref
scope.operation_ref

concrete_target_ref

provider_adapter_ref
provider_adapter_version
configuration_ref

canonical_policy_ref where applicable
security_policy_ref where applicable

requiredness:
REQUIRED | OPTIONAL | CONDITIONAL

effective_from
expires_at where applicable

validation_state
compatibility_state
health_state

supersedes
replacement
```

## Semantics

A Binding says how an already-defined requirement is realized here.

It does not define why the requirement exists or what it means.

## Requiredness

```text
REQUIRED
→ missing/unresolved blocks affected capability

OPTIONAL
→ absence is valid and explicit

CONDITIONAL
→ required only when stated applicability conditions hold
```

## Status

Definition lifecycle:

```text
DRAFT
ACTIVE
DEPRECATED
RETIRED
SUPERSEDED
```

Runtime availability/health is separate.

## Binding provenance

A Binding SHOULD retain source/configuration provenance sufficient to explain who/what version introduced it, without duplicating repository history when a stable change ref is sufficient.
