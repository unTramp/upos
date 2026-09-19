# Upstream Identity Audit

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Stable upstream identities safe for direct reuse

```text
UPOS-002: role_id, agent_definition_id + version, agent_run_id
UPOS-003: skill_id + version; skill_invocation_ref (reference semantics)
UPOS-004: task_id, routing_decision_id, workflow_instance_id, stage_id, transition_id
UPOS-005: context_request_id, context_bundle_id, memory_item_id
UPOS-006: engineering_change_id, repository_change_unit_id, workspace_id, merge_operation_id + native refs
UPOS-007: quality_criteria_set_id, quality_assessment_id, evidence_record_id, finding_id,
          quality_gate_id, quality_gate_result_id, quality_exception_id
```

## Agent Instance finding

Frozen reconciled UPOS-002 intentionally states:

```text
Agent Instance → configured runtime identity/reference
```

but does not define stable universal `agent_instance_id`.

Resolution:

```text
UPOS-008 consumes agent_instance_ref
UPOS-008 does not mint agent_instance_id
UPOS-011 later binds concrete runtime/project identity
```

This avoids downstream identity inversion.
