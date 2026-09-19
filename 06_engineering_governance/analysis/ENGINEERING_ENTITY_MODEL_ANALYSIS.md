# Engineering Entity Model Analysis

**ID:** UPOS-06-AN-003  
**Type:** ANALYSIS / ENTITY MODEL  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Accepted model

```text
Task                     [UPOS-004]
└── Engineering Change   [UPOS-006]
    ├── Repository Change Unit A
    │   ├── Workspace
    │   ├── Branch
    │   ├── Commit(s)
    │   ├── Integration Request
    │   └── Merge Operation → Integrated Revision
    └── Repository Change Unit B
        └── ...
```

## Identity decisions

Accepted semantic IDs:

```text
engineering_change_id
repository_change_unit_id
workspace_id
merge_operation_id
```

Native references retained:

```text
repository_ref
branch_ref
commit_ref
integration_request_ref
revision_ref
check_ref
tag_ref where used
```

## Rejected identity duplication

No `commit_id` replacement, no `branch_id`, no mandatory synthetic `integration_request_id` where a stable provider/VCS ref exists.

## Task/Workflow boundary

Engineering Change references upstream execution; it does not become a second Task.

Repository unit lifecycle does not become Workflow state.

## Result

Model is sufficient for one-repository, multi-repository, concurrent Agent, review, merge, and revert provenance.
