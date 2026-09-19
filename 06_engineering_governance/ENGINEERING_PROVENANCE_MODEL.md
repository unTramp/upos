# Engineering Provenance Model

**ID:** UPOS-06-PRV-001  
**Type:** PROVENANCE MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-008 future observability interface


## 1. Purpose

Engineering provenance makes repository work reconstructible without relying on chat history or private reasoning.

## 2. Canonical relationship chain

```text
Task
↓
Routing Decision
↓
Workflow Instance
↓
Stage
↓
Agent Run
↓
Skill Invocation
↓
Context Request (`context_request_id`)
↓
Context Bundle (`context_bundle_id`)
↓
Engineering Change
↓
Repository Change Unit
↓
Repository Workspace
↓
Change Branch
↓
Commit(s)
↓
Integration Request
↓
Review / QA / Security result references
↓
Merge Operation
↓
Integrated Revision
↓
possible Revert / Backout
```

This is a semantic relationship model, not an event/trace schema.

## 3. Stable identity/reference set

Owned semantic IDs:

```text
engineering_change_id
repository_change_unit_id
workspace_id
merge_operation_id
```

Upstream reused IDs:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

Native/external refs:

```text
Agent Run reference
Skill Invocation reference
repository_ref
branch_ref
commit_ref
integration_request_ref
revision_ref
check_ref
tag_ref / release_revision_ref where used
review/qa/security refs
context_request_id
context_bundle_id
```

## 4. Provenance != Observability

```text
artifact relationships / stable refs
→ UPOS-006

event_id / trace_id / span_id / metrics / dashboard
→ UPOS-008
```

## 5. Required reconstructibility

A future control plane SHOULD be able to answer from these relationships:

- Which Task caused this commit?
- Which Agent Run wrote it?
- Which Workflow Stage was active?
- Which `context_bundle_id` informed it?
- Which workspace/branch contained it?
- Why are these commits in one Integration Request?
- Which checks ran against exactly which revision?
- Did the artifact change after review/check?
- Who/which actor executed the Merge Operation?
- What integrated revision resulted?
- Was it later reverted/backed out?
- Which concurrent unit/Agent Run was involved in a collision?

## 6. Privacy of reasoning

Provenance MUST NOT store hidden chain-of-thought as a requirement.

Store attributable artifacts, references, concise rationale, decisions, evidence refs, and outcomes.

## 7. Context boundary

UPOS-006 consumes stable upstream Module-05 identities:

```text
context_request_id
context_bundle_id
```

for artifact provenance where applicable.

An Engineering Change may have multiple execution slices; therefore the provenance graph is many-to-one and MAY contain multiple Request/Bundle pairs.

Module 06 does not create `context_view_id`, does not duplicate Context Manifest/source provenance, and does not decide Context validity/freshness.

When a repository artifact changes, Module 06 exposes the exact artifact/revision change. UPOS-005 owns revalidation/reassembly and produces a new `context_bundle_id` when a new Bundle is assembled.
