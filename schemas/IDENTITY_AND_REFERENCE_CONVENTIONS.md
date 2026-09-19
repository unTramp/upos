# Identity & Reference Conventions

**ID:** UPOS-SCHEMA-IDREF-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Normative upstream:** 00_system/GLOBAL_IDENTITY_REFERENCE_REGISTRY.md

## 1. Core rule

Machine-readable schemas reuse owner-module identities. They MUST NOT create a second entity merely because software prefers a standalone identifier.

## 2. Canonical identity families

The schema layer preserves the families registered by the frozen Global Identity & Reference Registry.

~~~text
UPOS-002: Role; Agent Definition/version; Agent Instance ref; Agent Run
UPOS-003: skill_id + version; invocation/result refs
UPOS-004: task_id, routing_decision_id, workflow_instance_id, stage_id, transition_id
UPOS-005: context_request_id, context_bundle_id, memory_item_id
UPOS-006: engineering_change_id, repository_change_unit_id, workspace_id, merge_operation_id, provider/native refs
UPOS-007: quality_criteria_set_id, quality_assessment_id, evidence_record_id, finding_id, quality_gate_id, quality_gate_result_id, quality_exception_id
UPOS-008: event_id, trace_id, span_id, metric_definition_id
UPOS-009: pattern_candidate_id, learning_candidate_id, root_cause_assessment_id, improvement_proposal_id, validation_plan_id, learning_outcome_id
UPOS-010: permission_request_id, permission_decision_id, grant_id, protected_action_id, security_exception_id
UPOS-011: project_id, binding_id, provider_adapter_ref + provider_adapter_version, command_binding_id, adapter_resolution_id
~~~

## 3. Identities explicitly NOT introduced

~~~text
no quality_readiness_id
no global metric_observation_id
no project_manifest_id
no project_adapter_id
~~~

Composite identities remain:

~~~text
Project Manifest = project_id + manifest_version
Project Adapter  = project_id + project_adapter_version
~~~

Review/QA results reuse quality_assessment_id with assessment semantics owned by UPOS-007.

## 4. Namespace rule

Lexically identical names from different semantic owners are not equivalent.

Reserved U-POS schema-key namespace:

~~~text
upos.*
~~~

Project/product schemas and semantic types MUST NOT claim upos.* for project-owned meanings.

~~~text
artist.product.agent_run != upos.02.agent_organization.agent_run
artist.product.learning  != upos.09.learning.*
artist.product.context   != upos.05.context_memory.context_bundle
~~~

A plain lexical name such as AgentRun is never sufficient evidence that two objects share identity or semantics.

## 5. Canonical schema-key prefixes

~~~text
upos.common
upos.01.documentation
upos.02.agent_organization
upos.03.skills
upos.04.workflow
upos.05.context_memory
upos.06.engineering
upos.07.quality
upos.08.observability
upos.09.learning
upos.10.security
upos.11.project_adapter
~~~

A schema key identifies a serialization contract, not a domain entity.

Canonical schema URI/reference rules are defined in SCHEMA_URI_AND_REFERENCE_CONVENTIONS.md.

## 6. Reference rule

A reference MUST preserve the identity semantics of the referenced owner.

References MUST NOT rename an upstream identity into a new entity, drop a required version component, convert provider-native identity into U-POS semantic identity without an adapter binding, or imply current validity merely because an object exists.

## 7. Versioned identities

Where a frozen owner defines identity as ID + version, both parts are material. Schema convenience MUST NOT erase the version component.

## 8. Provider/native references

~~~text
provider ref != U-POS semantic identity
~~~

Provider/native references remain opaque to universal domain semantics unless an explicit adapter contract resolves them.

## 9. Historical reproducibility

Serialized execution records SHOULD retain the identity/version references required to reconstruct the baseline used at execution time, including project_id, project manifest version, project adapter version, owner-definition versions, binding refs, and provider adapter ref/version.

Historical records are not silently re-bound to current configuration.
