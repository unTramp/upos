# UPOS-005 — Context & Memory

**ID:** UPOS-05-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, UPOS-003, UPOS-004


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-005 defines how U-POS assembles the minimum sufficient, authoritative, fresh, relevant, permission-safe, role-appropriate and traceable execution context for a bounded consumer without creating a second Source of Truth.

It also defines bounded execution-support Memory and its strict separation from governed Project Knowledge.

## 1. Fundamental separation

```text
KNOWLEDGE
= governed project truth / evidence / proposal / historical knowledge
  owned by UPOS-01

CONTEXT
= execution-time selected information
  assembled for a bounded consumer and purpose

MEMORY
= retained execution-support information
  with explicit scope, provenance, lifetime and authority limits

RETRIEVAL
= process of locating eligible information

SOURCE RESOLUTION
= determination of canonical owner/source through UPOS-01

CONTEXT BUNDLE
= attributable assembled execution package

CACHE
= performance optimization
  with zero additional semantic authority
```

These terms MUST NOT be used interchangeably.

## 2. Critical invariants

```text
MEMORY != TRUTH
CONTEXT != TRUTH
CACHE != TRUTH
DERIVED_SUMMARY != CANONICAL_SOURCE
RAW_CHAT_HISTORY != PROJECT_MEMORY
PROVIDER_PRIVATE_MEMORY != PROJECT_KNOWLEDGE
```

Canonicality remains UPOS-01 ownership.

## 3. Context goal

Do not optimize for:

```text
maximum retrieved documents
maximum tokens
maximum remembered history
```

Optimize for:

```text
minimum sufficient
authoritative
fresh
relevant
permission-safe
role-appropriate
traceable
context
```

## 4. Core flow

```text
Task / Workflow / Stage / Role / Skill
↓
Context Requirements
↓
Context Request
↓
UPOS-01 canonical owner/source resolution
↓
UPOS-010 permission constraints
↓
UPOS-011 physical source/provider resolution
↓
UPOS-005 eligibility + retrieval
↓
authority-aware selection
↓
freshness validation
↓
budget / representation
↓
Context Bundle
↓
Agent Run / Skill Invocation
↓
output / temporary memory
↓
possible candidate
↓
UPOS-01 / UPOS-009 governance
```

## 5. Stable Module-05 identities

```text
context_request_id
context_bundle_id
memory_item_id
```

No additional global identity is introduced in v1 for source resolution or retrieval decisions. Their provenance is carried through upstream references and the Context Manifest.

## 6. Upstream execution identity references

Where applicable, a Context Request/Bundle references externally owned identities:

```text
project_id/reference
task_id
routing_decision_id
workflow_instance_id
stage_id
role_id
agent_definition_id/version
agent_run_id
skill_id/version
skill_invocation_ref
```

Module 05 consumes but does not own these identities.

## 7. Scope / non-scope

UPOS-005 owns retrieval/assembly/budget/freshness/isolation/memory semantics.

It MUST NOT redefine:

```text
project truth / canonical ownership             → UPOS-01
Role authority / Agent identity / SoD           → UPOS-002
Skill procedure                                 → UPOS-003
Workflow routing/state/stage order              → UPOS-004
Git/PR/merge mechanics                          → UPOS-006
Quality evidence/verdict/gates                  → UPOS-007
events/traces/metrics/dashboard                 → UPOS-008
organizational learning/promotion               → UPOS-009 + UPOS-01
access grants/secrets/security policy           → UPOS-010
paths/providers/search/storage/model bindings   → UPOS-011
```

## 8. Recommended read order

1. `CONTEXT_MEMORY_OPERATING_MODEL.md`
2. `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md`
3. `CONTEXT_BUNDLE_STANDARD.md`
4. `SOURCE_RESOLUTION_INTERFACE.md`
5. `RETRIEVAL_AND_SELECTION_STANDARD.md`
6. `CONTEXT_ASSEMBLY_STANDARD.md`
7. `CONTEXT_BUDGET_AND_REPRESENTATION.md`
8. `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md`
9. `CONTEXT_ISOLATION_AND_VIEWS.md`
10. `CONTEXT_FAILURE_MODEL.md`
11. `MEMORY_TAXONOMY.md`
12. `MEMORY_READ_WRITE_STANDARD.md`
13. `MEMORY_LIFECYCLE_AND_INVALIDATION.md`
14. `PROJECT_MEMORY_INTERFACE.md`
15. `CONTEXT_MEMORY_LIFECYCLE.md`
16. `CROSS_MODULE_INTERFACES.md`
17. `MODULE_05_TRACEABILITY.md`
