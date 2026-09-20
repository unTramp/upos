# Phase 2C Reconciliation — Project Manifest / Adapter

**ID:** UPOS-SCHEMA-P2C-REC-001  
**Status:** P1 FIX APPLIED — PENDING CI  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20

## Scope

Narrow conformance reconciliation against frozen UPOS-011 specialized binding standards and real Artist OS dogfooding.

## P1-01 — Specialized binding semantics were flattened

The initial candidate represented Repository, Path and Environment bindings through the generic Binding shape.

CI was green, but the representation lost frozen type-specific fields.

Examples:

~~~text
Repository Binding:
binding_id
repository_ref
provider_repository_ref
path_binding_refs
...

Path Binding:
binding_id
abstract_path_ref
repository_ref
concrete_path
path_kind
validation_rule_ref

Environment Binding:
binding_id
abstract_environment_ref
project_environment_name
provider_environment_ref
resource_binding_refs
~~~

### Resolution

Added dedicated schemas:

~~~text
repository-binding.schema.json
path-binding.schema.json
environment-binding.schema.json
~~~

The generic Binding schema no longer accepts these specialized binding types.

## P1-02 — repository_ref was conflated with Repository Binding identity

Initial Artist OS dogfooding used:

~~~text
binding_id = artist-os-primary
~~~

and Path/Command bindings referenced that same token.

Frozen UPOS-011 distinguishes:

~~~text
Repository Binding identity = binding_id
Reusable repository identity/reference = repository_ref
~~~

### Resolution

Artist OS now uses:

~~~text
binding_id     = artist-os-repository-binding
repository_ref = artist-os-primary
~~~

Manifest repository declarations carry both:

~~~text
repository_ref
binding_id
~~~

Path and Command Bindings reference repository_ref.

## Validation strengthened

Semantic validation now checks:

- unique binding_id;
- unique repository_ref;
- Manifest repository declaration → Repository Binding resolution;
- declaration repository_ref equals Repository Binding repository_ref;
- Path Binding repository_ref resolves;
- Command Binding repository_ref resolves;
- Repository Binding path_binding_refs resolve to PATH_BINDINGs in the same repository namespace;
- required binding references are present only where frozen contracts define requiredness.

## Principle confirmed

~~~text
GREEN CI != CONTRACT CONFORMANCE
generic convenience != authority to erase specialized frozen semantics
binding_id != repository_ref
~~~

## Status

~~~text
P0 unresolved: 0
P1 fix applied: 2
CI revalidation: PENDING
Full Phase 2C reconciliation: IN PROGRESS
~~~
