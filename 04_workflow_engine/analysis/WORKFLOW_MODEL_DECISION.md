# Workflow Model Decision — Three-Axis Resolution

**ID:** UPOS-04-AN-004  
**Type:** ARCHITECTURE ANALYSIS / MODEL DECISION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../WORK_TYPE_AND_CONCERN_MODEL.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Hypotheses considered

### A — One Workflow per named frozen-source change type

Rejected.

Reason: UI/API/DB/Security/Architecture overlap in the same task, creating ambiguous selection/combinatorial variants.

### B — One generic mega-workflow with conditional branches

Rejected as primary model.

Reason: hides Work Type intent and becomes difficult to reason/version/audit.

### C — Base Workflow + Concern Profiles + Change Class

Accepted.

```text
Primary intention → Base Workflow
Cross-cutting impacts → Profiles
Risk/impact depth → C0–C5
```

## Source preservation

Frozen named workflows are not discarded.

They are normalized:

- UI/Design System/Architecture/API/DB/Security → Concern Profiles;
- Micro → C0 depth on Generic Change;
- Bug/Feature/Refactor/Dependency Upgrade/Docs/Hotfix/Release → Base Workflows.

## Result

The selected model preserves semantics and allows multi-concern Tasks without multiplying Workflow Definitions.
