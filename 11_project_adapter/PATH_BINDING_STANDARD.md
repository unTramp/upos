# Path Binding Standard

**ID:** UPOS-11-PTH-001  
**Type:** PATH BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Contract

```text
binding_id
abstract_path_ref
repository_ref
environment_ref where applicable
concrete_path
path_kind
requiredness
validation_rule_ref
```

Universal modules MUST reference abstract path roles rather than embed project paths.

Path traversal outside the configured/project-authorized scope MUST NOT be inferred as allowed merely because the runtime filesystem permits it.
