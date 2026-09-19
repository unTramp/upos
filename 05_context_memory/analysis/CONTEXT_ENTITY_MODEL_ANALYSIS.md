# Context Entity Model Analysis

**ID:** UPOS-05-AN-004  
**Type:** ANALYSIS / ENTITY MODEL  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Recommended ontology

```text
KNOWLEDGE
= governed project truth/evidence/proposal/history
  owned by UPOS-01

CONTEXT REQUIREMENT
= reusable declaration of needed information characteristics

CONTEXT REQUEST
= concrete bounded request for execution context

SOURCE RESOLUTION
= canonical owner/source determination through UPOS-01

RETRIEVAL CANDIDATE
= discovered source/material candidate not yet included

CONTEXT ITEM
= attributable included information unit

CONTEXT BUNDLE
= immutable assembled execution snapshot

CONTEXT VIEW
= bounded projection for a Role/Run/Stage/Skill consumer

MEMORY ITEM
= retained noncanonical execution-support item

CACHE
= retrieval optimization with zero added authority
```

## Stable identity decision

Required Module-05 identities:

```text
context_request_id
context_bundle_id
memory_item_id
```

Not introduced in v1:

```text
context_resolution_id
retrieval_decision_id
```

Reason: source resolution remains an upstream/interface result and retrieval inclusion/exclusion decisions are sufficiently attributable through the Context Manifest. New global identity entities would add complexity without an independent lifecycle/ownership need.

## Provenance chain

```text
project reference
→ task_id
→ routing_decision_id
→ workflow_instance_id
→ stage_id
→ role_id
→ agent_definition/version
→ agent_run_id
→ skill_id/version + invocation reference where applicable
→ context_request_id
→ context_bundle_id
→ source references / memory references
```

## Immutability decision

Bundle payload is immutable once SEALED/consumed.

Late freshness/validity changes do not rewrite consumed content. They create a new validity assessment and, when required, a new Bundle:

```text
CB-102
→ stale / invalidated for active use
→ reassembly
→ CB-103
→ supersedes_context_bundle_id = CB-102
```
