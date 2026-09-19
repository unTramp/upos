# Project Adapter Ontology

**ID:** UPOS-11-ONT-001  
**Type:** ONTOLOGY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Core concepts

### Project Manifest
Declarative configuration entry point for one project adopting U-POS.

### Project Adapter
Governed collection of project-specific bindings plus resolution/validation rules.

### Binding
Versioned mapping from an abstract U-POS requirement/reference to a concrete project/runtime/provider realization.

### Provider Adapter
Implementation interface to an external provider/system. Provider Adapter capability does not imply semantic permission.

### Resolved Adapter View
Immutable execution-time projection of effective bindings after scope, precedence, compatibility and availability validation.

### Binding Drift
Observed mismatch between configured binding assumptions and actual provider/project reality.

### Adapter Validation Result
Configuration/binding result with values:

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
INVALID
```

This is not a Quality Verdict.

## Stable identities

Module 11 adopts:

```text
project_id
binding_id
provider_adapter_ref + provider_adapter_version
```

For independently referenced executable command mappings:

```text
command_binding_id
```

`adapter_resolution_id` is adopted for immutable execution-time Resolved Adapter Views because it is referenced by execution/audit provenance and has an independent lifecycle.

No separate `project_manifest_id` is required in v1:

```text
project_id + manifest_version
```

is the manifest identity.

No global `project_adapter_id` is introduced; project adapter identity is represented by:

```text
project_id + project_adapter_version
```

## Binding classes

```text
REPOSITORY_BINDING
PATH_BINDING
COMMAND_BINDING
TOOL_BINDING
PROVIDER_BINDING
IDENTITY_BINDING
RESOURCE_BINDING
CAPABILITY_BINDING
ENVIRONMENT_BINDING
SECRET_BINDING
QUALITY_BINDING
OBSERVABILITY_BINDING
LEARNING_BINDING
APPROVAL_BINDING
```

Extensions require namespaced binding types.

## Critical separations

```text
Binding != Policy
Binding != Project Knowledge
Provider Adapter != Domain Owner
Resource Binding != Resource semantics
Capability Binding != Permission Decision
Resolved Adapter View != Source of Truth
Adapter Health != Product/System Quality
```
