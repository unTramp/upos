# Repository Change Unit Standard

**ID:** UPOS-06-RCU-001  
**Type:** ENTITY / REPOSITORY-SCOPE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Definition

```text
REPOSITORY CHANGE UNIT
= one coherent repository-scoped portion of an Engineering Change
```

A Repository Change Unit (RCU) is the primary boundary for repository isolation, branch association, commit history, Integration Request mechanics, and repository integration.

## 2. Identity

Every RCU MUST have stable:

```text
repository_change_unit_id
```

## 3. Required attribution

An RCU MUST reference:

```text
repository_change_unit_id
engineering_change_id
repository_ref
task_id
workflow_instance_id
base_revision_ref
purpose
scope
non_scope
dependency_refs
```

Where applicable:

```text
stage_id
workspace_id
branch_ref
integration_request_ref
integrated_revision_ref
```

## 4. Base revision

Every RCU MUST know the repository state from which it began:

```text
base_revision_ref
```

This supports:

- diff reconstruction;
- review reproducibility;
- collision analysis;
- staleness detection;
- update-base/rebase decisions.

## 5. One repository

An RCU belongs to exactly one logical repository reference.

Cross-repository coordination belongs to the parent Engineering Change plus `MULTI_REPOSITORY_CHANGE_MODEL.md`.

## 6. Coherence

An RCU SHOULD represent one coherent repository intention.

Do not split by arbitrary file count.

Do not combine unrelated work merely because it touches the same repository.

## 7. Operational lifecycle

Canonical RCU lifecycle:

```text
PREPARED
→ ACTIVE
→ INTEGRATION_REQUEST_OPEN
→ INTEGRATED

alternate:
PREPARED / ACTIVE / INTEGRATION_REQUEST_OPEN
→ ABANDONED

replacement:
PREPARED / ACTIVE / INTEGRATION_REQUEST_OPEN
→ SUPERSEDED
```

These are repository-mechanical states, not Workflow or Quality states.

## 8. Integration order

An RCU MAY declare dependencies on other RCUs.

UPOS-006 exposes the engineering dependency; UPOS-004 owns overall orchestration.

## 9. Artifact staleness

An RCU may become mechanically stale when:

- integration base materially advances;
- required upstream RCU/revision changes;
- branch/history is rewritten;
- generated/migration artifacts diverge;
- reviewed/check artifact identity no longer matches current head.

Staleness here is engineering artifact staleness, not Context staleness.
