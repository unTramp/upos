# Context Bundle Standard

**ID:** UPOS-05-CBS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/CONTEXT_BUNDLE_TEMPLATE.md


## 1. Definition

A Context Bundle is an attributable, immutable assembled execution snapshot satisfying a concrete Context Request to the extent reported by its validity state.

Every production Bundle MUST have stable:

```text
context_bundle_id
```

## 2. Minimum contract

A production Bundle MUST include or explicitly mark non-applicable:

```text
context_bundle_id
context_request_id

project_id_ref
task_id
routing_decision_id
workflow_instance_id
stage_id

role_id
agent_definition_id
agent_definition_version
agent_run_id

skill_id
skill_version
skill_invocation_ref

purpose

context_policy_ref
context_policy_version
assembly_policy_ref where separately configured
assembly_policy_version where separately configured

assembled_at

source_resolution_refs

validity_state
required_sources_satisfied

context_items
context_manifest

open_conflicts
open_unknowns

budget_accounting

supersedes_context_bundle_id if rebuilt
reassembly_reason if rebuilt
```

## 3. Context Item

Each meaningful Context Item MUST preserve:

```text
bundle_local_item_key
source_ref
source_class
source_version_or_revision
canonical_owner_ref where applicable
source_status/lifecycle reference
epistemic_class_ref
representation_type
derived_from if derived
freshness_assessment
inclusion_reason
priority
required_or_optional
permission_transformation_ref where applicable
```

`bundle_local_item_key` is addressable inside the Bundle but is not a new global identity.

## 4. Representation types

Canonical v1 representation types:

```text
EXACT
EXCERPT
DERIVED_SUMMARY
REFERENCE_ONLY
```

Their safety rules are defined in `CONTEXT_BUDGET_AND_REPRESENTATION.md`.

## 5. Context Manifest

Every production Bundle MUST include a Manifest sufficient to answer:

```text
what was required?
what was found?
what was included?
what was excluded?
why?
what was summarized?
from which source/version?
were all required sources satisfied?
what conflicts/unknowns remain?
what budget was available/consumed?
```

## 6. Required-source satisfaction

Bundle MUST explicitly report:

```text
required_sources_satisfied = true / false
```

Consumers MUST NOT infer completeness from item count.

## 7. Exclusion reasons

Canonical v1 exclusion vocabulary:

```text
OUT_OF_SCOPE
SUPERSEDED
RETIRED
STALE
PERMISSION_DENIED
BUDGET_OMITTED_OPTIONAL
LOW_RELEVANCE_OPTIONAL
WRONG_VERSION
WRONG_PROJECT
CONFLICTING_SOURCE
DUPLICATE
NOT_APPLICABLE_TO_STAGE
PROVENANCE_INSUFFICIENT
```

An exclusion reason does not redefine upstream source lifecycle or permission semantics.

## 8. Bundle immutability

Once a production Bundle is SEALED/consumed, its content MUST NOT be silently mutated.

If material source/context conditions change:

```text
CB-102
→ stale / invalidated for active use
→ reassembly
→ CB-103
→ supersedes_context_bundle_id = CB-102
```

The original consumed snapshot remains auditable.

## 9. Validity is separate from identity

Bundle identity does not change when a later assessment marks the immutable snapshot stale or invalidated.

Validity semantics are defined separately.

## 10. Context Bundle != prompt

A provider-specific prompt may be generated from a Bundle.

Prompt construction/formatting is runtime/adapter behavior and MUST NOT redefine Bundle semantics.
