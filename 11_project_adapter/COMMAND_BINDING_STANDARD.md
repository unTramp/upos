# Command Binding Standard

**ID:** UPOS-11-CMD-001  
**Type:** COMMAND BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/COMMAND_BINDING_TEMPLATE.md


## Stable identity

```text
command_binding_id
```

is justified because command mappings are independently referenced by Skills, Quality checks, Engineering checks and audit records.

## Contract

```text
command_binding_id
version
abstract_operation_ref

repository_ref
working_directory_ref

executable
arguments

environment_binding_refs
secret_binding_refs

timeout_policy_ref
expected_result_interface_ref
produced_artifact_or_check_type

required_capability_refs

provider_or_runtime_binding_ref
platform_constraints

requiredness
validation_state
```

## Separation

```text
command result
!= Quality Verdict
```

A Quality criterion may require evidence from a command, but the command string never defines the criterion.
