# Memory Read / Write Standard

**ID:** UPOS-05-MRW-001  
**Type:** MEMORY ACCESS STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/MEMORY_ITEM_TEMPLATE.md


## 1. Stable identity

Every persisted Module-05 memory item MUST have:

```text
memory_item_id
```

## 2. Persisted memory write contract

Every write MUST specify:

```text
memory_item_id
memory_class

project_id_ref
scope_refs
task_id and/or agent_run_id as applicable

producer_role_ref
producer_agent_run_ref

provenance
source_refs
created_from_refs

epistemic_class_ref
representation_content_type
content_or_artifact_ref

created_at
lifetime_class
expiration_or_review_trigger if applicable
invalidation_conditions

permission_security_constraint_refs where applicable

memory_state

canonicality = false
```

Exception: `GOVERNED_PROJECT_MEMORY_VIEW` is not written as a new canonical memory item; it references UPOS-01 governed knowledge.

## 3. Epistemic status

Memory SHOULD preserve UPOS-01 epistemic classes rather than invent a competing truth taxonomy.

Working status/lifetime is separate from epistemic class.

## 4. Read eligibility

Before a memory item can affect Context, check:

```text
project scope
Task/Run scope
provenance
source relationship
freshness/state
permission eligibility
current applicability
Role/independence constraints
```

## 5. Run Working Memory read/write

Run memory is private to the bounded Agent Run by default.

It MUST NOT automatically flow into another Role/Run.

## 6. Task Working Memory read/write

Task memory may be shared only inside the same Task according to Role/permission/independence constraints.

It MUST NOT become cross-task knowledge by persistence alone.

## 7. Cross-task reuse

Cross-task reuse requires governed reusable source/evidence or explicit authorized reference and a new applicability/freshness check.

## 8. Memory promotion boundary

Memory does not promote itself.

```text
Run/Task memory observation
→ candidate artifact/proposal/evidence
→ UPOS-01 Knowledge Lifecycle and/or UPOS-009
→ review/validation/promotion
→ new canonical source if approved
→ Module 05 may retrieve it later
```

`memory_item.status = permanent` would not create canonicality and is not a valid promotion mechanism.

## 9. Private reasoning

Module-05 workflows MUST NOT depend on storing hidden model chain-of-thought.

Store attributable artifacts, evidence, decisions, concise rationale, and explicit working notes where needed.
