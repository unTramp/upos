# Commit Provenance Standard

**ID:** UPOS-06-CPR-001  
**Type:** PROVENANCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Goal

A governed Commit should be reconstructible as part of a specific engineering intention without storing private chain-of-thought.

## 2. Provenance fields

Where available/relevant, preserve or reference:

```text
commit_ref
repository_change_unit_id
engineering_change_id

task_id
routing_decision_id
workflow_instance_id
stage_id

Role reference
Agent Run reference
Skill Invocation reference

context_bundle_id reference(s)

parent/base reference
commit purpose
affected scope
related check_ref values
Integration Request reference
```

## 3. Context boundary

When Context materially informed the commit, provenance SHOULD reference the exact upstream `context_bundle_id` value(s) actually consumed.

A single Commit MAY have multiple Context Bundle references when it combines work from multiple governed execution slices, provided the Commit remains one coherent logical intent.

Module 06 does not copy the Context Manifest. Provenance continues through:

```text
commit_ref
→ context_bundle_id
→ context_request_id
→ Context Manifest / source refs
```

where Context-owned fields and validity remain UPOS-005 semantics.

Module 06 MUST NOT define:

- Context validity/freshness states;
- Context View semantics;
- Context isolation;
- retrieval/budget/memory semantics.


## 4. No hidden reasoning

Commit provenance MUST NOT require private chain-of-thought.

Store concise intent, decision refs, artifacts, evidence references, and attributable execution identities.

## 5. Rewrite preservation

If commit identity changes through history rewrite:

- previous `commit_ref` remains historical provenance;
- new `commit_ref` is associated with the rewrite/replacement operation;
- review/check references continue to identify the artifact they actually covered.

## 6. Squash preservation

When policy transforms a commit set into one integrated revision, provenance MUST retain discoverable links from resulting revision back to:

```text
Integration Request
original commit set
Task
Engineering Change
Repository Change Unit
```
