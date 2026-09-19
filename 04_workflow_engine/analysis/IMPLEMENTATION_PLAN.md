# UPOS-004 Implementation Plan

**ID:** UPOS-04-AN-008  
**Type:** IMPLEMENTATION PLAN / EVIDENCE  
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


## Sequence

1. freeze Module 04 scope/non-scope;
2. audit C0–C5 and routing semantics;
3. resolve three-axis Work Type/Concern/Class model;
4. define Workflow/Profile contracts;
5. define state/transition/reclassification/retry semantics;
6. define base Workflow catalog;
7. convert orthogonal frozen workflows to Concern Profiles;
8. define cross-module interfaces/templates;
9. complete source disposition/traceability;
10. validate zero ownership leakage.

## Recommended logical commits

```text
docs(upos-004): establish workflow engine boundary
docs(upos-004): define change classification and routing model
docs(upos-004): define workflow and profile contracts
docs(upos-004): define workflow state and reclassification semantics
docs(upos-004): define failure retry recovery and dependency orchestration
docs(upos-004): add canonical base workflows
docs(upos-004): add concern profiles
docs(upos-004): add templates and cross-module interfaces
docs(upos-004): complete source traceability audit
```

One commit = one coherent logical change.

## Non-scope

No runtime provider, Git engine, Quality engine, Security engine, Context engine, telemetry store/dashboard, schema implementation, or project adapter implementation.
