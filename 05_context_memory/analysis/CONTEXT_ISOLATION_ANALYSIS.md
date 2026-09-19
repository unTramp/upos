# Context Isolation Analysis

**ID:** UPOS-05-AN-007  
**Type:** ANALYSIS / CONTEXT ISOLATION  
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


## Context View

A Context View is a bounded projection of eligible information for a specific consumer.

Relevant dimensions:

```text
project
Task
Workflow Instance
Stage
Role
Agent Run
Skill Invocation
Change Class
permissions/security constraints
independence requirements
```

## Reviewer independence

```text
producer context
!= reviewer authoritative context
```

Reviewer MUST independently receive the authoritative sources needed to evaluate the change.

Reviewer context MUST NOT automatically inherit:

- Implementer scratch notes;
- private chain-of-thought/reasoning;
- unverified assumptions;
- self-approval claims;
- producer-only transient memory.

Producer notes MAY be included only as clearly labeled producer-provided material when relevant.

## QA independence

QA Context View should begin from expected behavior/contracts and risk, not only implementation narrative.

## Cross-project isolation

```text
Project A context
MUST NOT leak into
Project B context
```

unless an explicit shared/federated mechanism is authorized externally.

## Cross-task isolation

Task memory from Task A is not injected into Task B merely because a model/search engine can retrieve it.

## Authority boundary

Access to a source does not grant authority over that fact scope.
