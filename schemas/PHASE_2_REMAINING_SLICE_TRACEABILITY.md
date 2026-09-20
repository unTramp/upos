# Phase 2 Remaining Slice — Cross-Module Identity & Reference Traceability

**ID:** UPOS-SCHEMA-P2-REMAINING-TRACE-001  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20  
**Scope:** frozen identity/reference serialization only

## 1. Governing boundary

~~~text
PHASE 2
= canonical serialization of frozen identity/reference semantics

PHASE 3
= runtime behavior consuming those canonical references
~~~

This slice does not define lifecycle execution, state machines, persistence, runtime operations, error/result contracts, event emission, orchestration, retry/recovery, provider execution, Event Store, Quality evaluation, Permission evaluation or Adapter resolution behavior.

## 2. Traceability matrix

| Owner | Frozen identity/reference family | Schema | Positive fixture | Meaningful negative fixture | Phase-3 behavior excluded |
|---|---|---|---|---|---|
| UPOS-02 | role_id/ref; agent_definition_id + version; agent_instance_ref; agent_run_id/ref | `schemas/02/agent_organization/identity-references.schema.json` | `fixtures/identity_references/agent_organization/valid.json` | missing Agent Definition version; invented `agent_instance_id` | Agent Run lifecycle/execution/results/errors/persistence |
| UPOS-03 | skill_id + version; skill_invocation_ref; skill_result_ref | `schemas/03/skills/identity-references.schema.json` | `fixtures/identity_references/skills/valid.json` | versioned Skill ref missing version | Skill invocation/result runtime, failures/retries |
| UPOS-04 | task_id; routing_decision_id; workflow_instance_id; stage_id; transition_id | `schemas/04/workflow/identity-references.schema.json` | `fixtures/identity_references/workflow/valid.json` | generic/invented `workflow_id` instead of frozen instance identity | routing execution, state machine, transitions, retry/rework/recovery |
| UPOS-05 | context_request_id; context_bundle_id; memory_item_id | `schemas/05/context_memory/identity-references.schema.json` | `fixtures/identity_references/context_memory/valid.json` | invented `context_view_id` | retrieval, assembly, freshness runtime, invalidation/reassembly/cache |
| UPOS-06 | engineering_change_id; repository_change_unit_id; workspace_id; merge_operation_id; provider/native branch/commit/IR/check/revision refs | `schemas/06/engineering/identity-references.schema.json` | `fixtures/identity_references/engineering/valid.json` | invented global `integration_request_id` | Git/provider operations, workspace creation, merge execution |
| UPOS-07 | quality_criteria_set_id; quality_assessment_id; evidence_record_id; finding_id; quality_gate_id; quality_gate_result_id; quality_exception_id | `schemas/07/quality/identity-references.schema.json` | `fixtures/identity_references/quality/valid.json` | invented `quality_readiness_id` | evidence collection, assessment/verdict/gate/readiness execution |
| UPOS-08 | event_id; trace_id; span_id; metric_definition_id | `schemas/08/observability/identity-references.schema.json` | `fixtures/identity_references/observability/valid.json` | invented global `metric_observation_id` | event emission/ingestion, Event Store, trace runtime, metric derivation |
| UPOS-09 | pattern_candidate_id; learning_candidate_id; root_cause_assessment_id; improvement_proposal_id; validation_plan_id; learning_outcome_id | `schemas/09/learning/identity-references.schema.json` | `fixtures/identity_references/learning/valid.json` | invented `learning_evidence_set_id` | detection, root-cause execution, validation/promotion/runtime mutation |
| UPOS-10 | permission_request_id; permission_decision_id; grant_id; protected_action_id; security_exception_id; security_policy_ref + version | `schemas/10/security/identity-references.schema.json` | `fixtures/identity_references/security/valid.json` | incomplete versioned Security Policy ref | Permission engine, policy evaluation, ALLOW/DENY enforcement |
| UPOS-11 | adapter_resolution_id | `schemas/11/project_adapter/adapter-resolution-reference.schema.json` | `fixtures/project_adapter/adapter-resolution-reference.valid.json` | empty resolution identity | binding resolution/precedence/availability/runtime resolver |

All fixture paths above are relative to `schemas/`.

## 3. Canonical cross-schema reference proof

Infrastructure-only harness:

~~~text
schemas/meta/cross-module-reference-conformance.schema.json
~~~

It imports canonical owner definitions through exact versioned URNs for:

~~~text
UPOS-02 Agent Definition
UPOS-03 Skill
UPOS-04 Task
UPOS-05 Context Bundle
UPOS-06 Engineering Change
UPOS-07 Quality Assessment
UPOS-08 Event
UPOS-09 Learning Candidate
UPOS-10 Permission Decision
UPOS-11 Adapter Resolution
~~~

Fixtures:

~~~text
schemas/fixtures/cross_module_references/valid.json
schemas/fixtures/cross_module_references/invalid-imported-version-requirement.json
~~~

The negative fixture proves that imported owner constraints remain active across canonical `$ref`: an Agent Definition reference without its frozen required version fails.

The existing Schema Registry validator additionally requires:

~~~text
reference_dependencies
=
actual registered canonical cross-schema $ref dependencies
~~~

No stale or undeclared dependency is accepted.

## 4. Anti-identity preservation

Global semantic validation rejects schema property introduction of frozen-rejected synthetic identities including:

~~~text
agent_instance_id
context_view_id
integration_request_id
quality_readiness_id
metric_observation_id
learning_signal_id
learning_evidence_set_id
confirmed_pattern_id
root_cause_hypothesis_id
improvement_opportunity_id
promotion_recommendation_id
learning_backlog_item_id
project_manifest_id
project_adapter_id
security_approval_id
~~~

This supplements owner-specific negative fixtures.

## 5. Namespace / Artist OS compatibility

Real source:

~~~text
unTramp/artistos
branch: feat/upos-adoption
path: .upos/PROJECT_ADAPTER.md
~~~

The project declares an anti-corruption boundary:

~~~text
U-POS concept != Artist OS product concept merely because names match
No automatic conversion is authorized.
~~~

Phase-2-only dogfooding artifact:

~~~text
schemas/dogfooding/artist-os/identity-namespace-compatibility.json
~~~

It verifies:

~~~text
project namespace = artist.product
reserved U-POS schema-key prefix = upos.
project concepts remain project namespaced
automatic_mappings = []
~~~

No fake Task, Agent Run, Context Bundle, Quality Assessment, Permission Decision or other runtime instance is created.

## 6. Frozen sources

Primary global sources:

~~~text
ROADMAP.md
00_system/GLOBAL_IDENTITY_REFERENCE_REGISTRY.md
00_system/GLOBAL_OWNERSHIP_MATRIX.md
schemas/SCHEMA_GOVERNANCE.md
schemas/SCHEMA_URI_AND_REFERENCE_CONVENTIONS.md
~~~

Owner semantics trace to the corresponding frozen v1.0.0 ontology/standard and `CROSS_MODULE_INTERFACES.md` documents recorded by each Schema Registry entry.

## 7. Registry integration

Every identity/reference schema is registered with:

~~~text
schema_key
schema_uri
schema_version
artifact_path
implementation_state = CANDIDATE
upos_baseline = v1.0.0
semantic_owner_module
schema_steward
normative_source_refs
identity_model
reference_dependencies
compatibility metadata
~~~

The identity/reference slice deliberately remains CANDIDATE pending independent blind audit and the final Phase 2 exit/stability gate.

## 8. Non-claims

This traceability artifact does NOT claim:

~~~text
PHASE 2 COMPLETE
Phase 3 started
runtime contracts implemented
runtime dogfooding completed
CANDIDATE schemas promoted to STABLE
~~~
