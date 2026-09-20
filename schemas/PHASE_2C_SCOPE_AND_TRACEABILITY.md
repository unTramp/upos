# Phase 2C — Project Manifest & Project Adapter Schemas

**ID:** UPOS-SCHEMA-P2C-TRACE-001  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Semantic owner:** UPOS-011 Project Adapter  
**Date:** 2026-09-20

## Objective

Represent the frozen UPOS-011 project binding model in machine-readable contracts without turning project configuration into project truth.

## Upstream

- PROJECT_MANIFEST_STANDARD.md
- PROJECT_ADAPTER_ONTOLOGY.md
- PROJECT_ADAPTER_OPERATING_MODEL.md
- BINDING_STANDARD.md
- BINDING_RESOLUTION_STANDARD.md
- BINDING_VALIDATION_STANDARD.md
- COMMAND_BINDING_STANDARD.md

## Schema families

- project-manifest.schema.json
- project-adapter.schema.json
- binding.schema.json
- command-binding.schema.json

## Identity preservation

~~~text
Project Manifest identity = project_id + manifest_version
Project Adapter identity  = project_id + project_adapter_version
Binding identity          = binding_id
Command Binding identity  = command_binding_id
~~~

No project_manifest_id or project_adapter_id is introduced.

COMMAND_BINDING is represented separately because its independently referenced frozen identity is command_binding_id.

## Manifest normalization

The frozen Manifest template defines top-level binding/declaration sections but does not prescribe one machine shape for each declaration.

Phase 2C normalizes those sections into binding-reference lists:

~~~text
Manifest → declares which binding identities configure the project
Adapter  → contains concrete versioned Binding records
~~~

This is representation only.

## Fail closed

Unresolved provider/resource/production capability is not represented by an invented concrete Binding.

Absence remains absence, while adapter validation_result and configuration_completeness expose incompleteness.

A REQUIRED referenced binding that is missing fails static validation.

## Boundaries

~~~text
Manifest value != canonical project fact
Binding != Policy
Capability Binding != Permission Decision
Command result != Quality Verdict
Resolved Adapter View != Source of Truth
~~~

Runtime resolution/provider integrations/orchestration remain out of scope.
