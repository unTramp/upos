# Phase 2C Traceability — Project Manifest & Project Adapter

**ID:** UPOS-SCHEMA-P2C-TRACE-001  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Semantic owner:** UPOS-011 Project Adapter  
**Date:** 2026-09-20

## Objective

Represent the frozen UPOS-011 Project Manifest, Generic Binding and Project Adapter aggregate in machine-readable form without changing ownership or inventing runtime semantics.

## Upstream

Primary frozen contracts:

- PROJECT_MANIFEST_STANDARD.md
- PROJECT_ADAPTER_ONTOLOGY.md
- PROJECT_ADAPTER_LIFECYCLE_AND_VERSIONING.md
- BINDING_STANDARD.md
- BINDING_RESOLUTION_STANDARD.md
- BINDING_VALIDATION_STANDARD.md
- templates/PROJECT_MANIFEST_TEMPLATE.md
- templates/BINDING_TEMPLATE.md

## Identity preservation

~~~text
Project Manifest identity
= project_id + manifest_version

Project Adapter identity
= project_id + project_adapter_version
~~~

Explicitly prohibited:

~~~text
project_manifest_id
project_adapter_id
~~~

## Manifest representation

All frozen top-level sections are required as keys.

Where UPOS-011 permits a capability to be not applicable, the section may be serialized as explicit `N/A` where the schema defines that representation.

Empty arrays mean the applicable binding family currently has no listed refs. They do not imply authorization, completeness or runtime readiness.

Project-specific operational detail belongs in explicit bindings or `extensions.<namespace>`; it does not become universal Manifest semantics.

## Binding representation

The Generic Binding schema follows the frozen contract/template.

Closed vocabularies are used only where UPOS-011 defines them:

- binding lifecycle status;
- requiredness;
- Adapter Validation Result.

UPOS-011 does not freeze closed vocabularies for `compatibility_state` or `health_state`; those remain non-empty strings.

## Project Adapter aggregate representation

Frozen UPOS-011 defines Project Adapter as a governed collection of bindings plus resolution/validation rules, but provides no standalone Project Adapter template.

The schema-layer aggregate therefore indexes:

- composite project/adapter identity;
- the bound Manifest composite reference;
- Binding refs;
- Command Binding refs;
- Provider Adapter ref/version pairs;
- frozen resolution/validation rule refs;
- Adapter Validation Result;
- configuration completeness;
- project extensions.

This is a serialization profile of the frozen ontology, not a new semantic entity.

## Cross-object invariant

The validator MUST reject silent cross-project composition:

~~~text
adapter.project_id
=
adapter.manifest_ref.project_id
=
manifest.project.project_id
~~~

It also checks:

~~~text
adapter.project_adapter_version
=
manifest.project_adapter_version

adapter.manifest_ref.manifest_version
=
manifest.manifest_version
~~~

## Artist OS dogfooding note

Artist OS human-readable adoption candidates contain more operational detail than the universal machine contract should require.

They also contain pre-Phase-2A conceptual namespace examples such as `upos.execution.AgentRun`.

The U-POS Core schema layer does not mutate Artist OS documents. This is recorded as adoption drift to reconcile in the project-side freeze pass.

The machine-readable 2C dogfooding instance will use owner-qualified U-POS namespaces and preserve unresolved production/quality/security bindings as incomplete rather than fabricating values.
