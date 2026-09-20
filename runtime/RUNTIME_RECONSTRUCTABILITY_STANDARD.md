# Runtime Reconstructability Standard

**ID:** UPOS-RUNTIME-REC-001  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Baseline:** U-POS v1.0.0

## 1. Invariant

For every material governed execution, sufficient canonical references MUST be retained to reconstruct execution provenance without private chain-of-thought.

The reconstructable object is a reference graph, not necessarily one database row.

## 2. Slice-1 minimum graph

Where applicable, retain references to:

```text
Task
Routing Decision
Workflow Instance
Stage
Transition
Role
Agent Definition/version
Agent Instance
Agent Run
Skill/version
Skill Invocation
Skill Result
Context Request
Context Bundle
owner result
owner failure
Event
Trace/Span when externally available
runtime contract/schema versions needed for historical interpretation
```

Later Phase-3 slices extend this graph with Engineering, Quality, Security and Adapter Resolution references.

## 3. Prohibited reconstruction source

Private chain-of-thought MUST NOT be required or persisted as execution provenance.

Persist attributable identifiers, governed inputs/basis, outputs/results, evidence/artifact references and version information instead.

## 4. Non-scope

This standard does not define:

- dashboard read models;
- timeline UI;
- Control Plane API;
- projection store;
- Event Store.

UI-specific fields MUST NOT be added merely for reconstructability.

## 5. Normative sources

- `05_context_memory/CONTEXT_MEMORY_LIFECYCLE.md`
- `08_observability/EVENT_STANDARD.md`
- `00_system/GLOBAL_IDENTITY_REFERENCE_REGISTRY.md`
