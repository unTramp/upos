# Module 04 Ownership Map

**ID:** UPOS-04-AN-002  
**Type:** ANALYSIS / BOUNDARY MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Owns

Workflow/classification/routing/stage/transition/state/rework/retry/recovery/reclassification/rerouting/completion semantics and Workflow/Profile lifecycle/versioning.

## Does not own

| Concern | Owner |
|---|---|
| canonical project truth | UPOS-01 |
| Roles/authority/SoD/handoffs | UPOS-002 |
| Skill procedure/registry/evaluation | UPOS-003 |
| Context retrieval/memory | UPOS-005 |
| Git/PR/merge/worktree mechanics | UPOS-006 |
| review/QA/evidence/verdict semantics | UPOS-007 |
| telemetry/traces/metrics | UPOS-008 |
| learning detection/promotion | UPOS-009 + UPOS-01 |
| permissions/protected actions/secrets | UPOS-010 |
| project/provider/command bindings | UPOS-011 |

## Boundary test

If the central question is:

```text
When/why does this stage occur?
Which Role/Skill/gate is required?
What transition/rework/reroute is legal?
How deep is process based on risk?
```

it is Workflow-owned.

If the question is:

```text
What may this Role decide?
How does this Skill perform its method?
How is context retrieved?
What does QA PASS mean?
Who may merge/deploy?
Which Git command/provider/path is used?
```

it is not Module 04 ownership.
