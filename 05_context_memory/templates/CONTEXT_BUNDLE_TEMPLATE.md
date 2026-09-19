# Context Bundle Template

**ID:** UPOS-05-TPL-003  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Context Bundle

context_bundle_id:
context_request_id:

project_id_ref:
task_id:
routing_decision_id:
workflow_instance_id:
stage_id:

role_id:
agent_definition_id:
agent_definition_version:
agent_run_id:

skill_id:
skill_version:
skill_invocation_ref:

purpose:

context_policy_ref:
context_policy_version:
assembly_policy_ref: N/A
assembly_policy_version: N/A
assembled_at:

validity_state:
required_sources_satisfied:

source_resolution_refs:

included_context_items:
- bundle_local_item_key:
  source_ref:
  source_class:
  source_version_or_revision:
  canonical_owner_ref:
  source_status:
  epistemic_class_ref:
  representation_type:
  derived_from:
  freshness_assessment:
  inclusion_reason:
  priority:
  required_or_optional:
  permission_transformation_ref: N/A

excluded_candidates:
- source_ref:
  exclusion_reason:
  materiality:

open_conflicts:
open_unknowns:

budget_accounting:
  budget_limit_or_reference:
  budget_consumed:
  required_material:
  optional_material:
  summarized_material:
  omitted_optional_material:

supersedes_context_bundle_id:
reassembly_reason:
```
