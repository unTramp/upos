# Project Manifest Standard

**ID:** UPOS-11-PMS-001  
**Type:** MANIFEST STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/PROJECT_MANIFEST_TEMPLATE.md


## Required top-level contract

```text
project
upos_baseline
manifest_version
project_adapter_version

repositories
paths
commands
providers
runtime
environments

identity_bindings
resource_bindings
capability_bindings
security_bindings
secret_bindings

quality_bindings
observability_bindings
learning_bindings

extensions
```

A section MAY be explicitly `N/A` only when the project does not require that capability.

## Project block

```text
project_id
name
canonical_project_source_ref
```

`canonical_project_source_ref` points to UPOS-01-governed project truth; the Manifest does not own those facts.

## Baseline compatibility

```text
upos_baseline.version
upos_baseline.module_interface_requirements where material
```

The template serialization MUST represent these as the nested `upos_baseline.version` and `upos_baseline.module_interface_requirements` fields.

The adapter MUST reject an incompatible baseline rather than silently reinterpret fields.

## Repository declarations

Each repository declaration references a `repository_ref` and its binding. One project may have one or many repositories.

## Policy references

Project-specific values that derive from policy MUST retain source:

```text
canonical_policy_ref
canonical_policy_version/revision
```

Examples include coverage thresholds, protected environments, learning thresholds and security constraints.

## Secrets

Raw secret values are forbidden.

Allowed:

```text
secret_ref
secret_store_binding_ref
secure_injection_ref
```

## Extensions

Extensions use explicit namespaces:

```text
extensions.<organization_or_project_namespace>
```

An extension MUST NOT override canonical core fields/invariants.

## Declarative constraint

The Manifest is configuration, not a scripting language.

Executable logic lives in referenced provider/runtime adapters.
