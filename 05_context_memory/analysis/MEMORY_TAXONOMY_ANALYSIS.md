# Memory Taxonomy Analysis

**ID:** UPOS-05-AN-006  
**Type:** ANALYSIS / MEMORY TAXONOMY  
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


## v1 taxonomy

### RUN_WORKING_MEMORY

Ephemeral noncanonical support for one Agent Run.

Examples:

- temporary notes;
- intermediate calculations;
- retrieval pointers;
- partial working artifacts.

Default: not persisted beyond Run without explicit policy.

### TASK_WORKING_MEMORY

Bounded noncanonical operational memory retained across Runs/Stages for one Task.

It MUST NOT duplicate UPOS-004 Workflow state.

### RETRIEVAL_CACHE

Performance optimization for previously resolved/retrieved material.

Invariant:

```text
CACHE HAS ZERO ADDITIONAL AUTHORITY
```

### GOVERNED_PROJECT_MEMORY_VIEW

Not a new semantic database.

```text
GOVERNED_PROJECT_MEMORY_VIEW
= Context/Retrieval view over knowledge governed by UPOS-01
```

## Rejected generic bucket

A single persistent `memory` bucket is rejected because it conflates:

- scratch state;
- task coordination;
- cached retrieval;
- canonical project knowledge.

## Cross-task rule

Task Working Memory is not automatically reusable by another Task.

Cross-task reuse must pass through governed knowledge/evidence/artifact references and current scope/freshness/permission checks.

## Provider/model memory

Provider private memory, latent model memory, personalization memory, and raw conversation history are not Project Memory and cannot be hidden dependencies.
