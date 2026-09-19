# Global Identity & Reference Registry — U-POS v1

This is an audit/index artifact, not a new identity owner. Owner modules remain normative.

| Owner | Stable identity / reference family |
|---|---|
| 002 | Role ID; Agent Definition ID/version; Agent Instance identity/configuration ref; Agent Run identity |
| 003 | `skill_id` + version; Skill Invocation/Result references according to Skill contracts |
| 004 | `task_id`, `routing_decision_id`, `workflow_instance_id`, `stage_id`, `transition_id` |
| 005 | `context_request_id`, `context_bundle_id`, `memory_item_id` |
| 006 | `engineering_change_id`, `repository_change_unit_id`, `workspace_id`, `merge_operation_id`; provider/native artifact refs for branch/commit/IR/check/revision |
| 007 | `quality_criteria_set_id`, `quality_assessment_id`, `evidence_record_id`, `finding_id`, `quality_gate_id`, `quality_gate_result_id`, `quality_exception_id` |
| 008 | `event_id`, `trace_id`, `span_id`, `metric_definition_id`; Metric Observation is a derived/value record with no global ID |
| 009 | `pattern_candidate_id`, `learning_candidate_id`, `root_cause_assessment_id`, `improvement_proposal_id`, `validation_plan_id`, `learning_outcome_id` |
| 010 | `permission_request_id`, `permission_decision_id`, `grant_id`, `protected_action_id`, `security_exception_id` |
| 011 | `project_id`, `binding_id`, `provider_adapter_ref` + `provider_adapter_version`, `command_binding_id`, `adapter_resolution_id` |

## Anti-duplication rule for schemas/runtime

Machine-readable schemas may choose serialization field names for upstream semantic identities where a module intentionally defines identity conceptually rather than globally standardizing a field spelling. Schemas/runtime MUST NOT create a second domain entity merely to obtain a convenient identifier.

Examples:

```text
Review Result / QA Result → reuse quality_assessment_id via assessment_type
Quality Readiness → scoped projection of Quality Assessment; no quality_readiness_id
Metric Observation → no global metric_observation_id
Project Manifest identity → project_id + manifest_version; no project_manifest_id
Project Adapter identity → project_id + project_adapter_version; no project_adapter_id
```
