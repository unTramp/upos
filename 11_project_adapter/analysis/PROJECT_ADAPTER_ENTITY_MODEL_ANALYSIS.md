# Project Adapter Entity Model Analysis

**ID:** UPOS-11-AN-004  
**Type:** ENTITY MODEL ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Adopted stable identities

```text
project_id
binding_id
provider_adapter_ref + version
command_binding_id
adapter_resolution_id
```

## Deliberately not introduced

```text
project_manifest_id
project_adapter_id
repository_binding_id separate from binding_id
quality_binding_id separate from binding_id
security_binding_id separate from binding_id
```

Reason: `binding_id + binding_type` provides one consistent addressable lifecycle.

Manifest identity is `project_id + manifest_version`; adapter identity is `project_id + project_adapter_version`.

`adapter_resolution_id` is justified because the immutable resolved configuration snapshot is independently referenced by execution/audit records.
