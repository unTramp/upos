# Context & Memory Lifecycle

**ID:** UPOS-05-CML-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Context Request lifecycle

Semantic request states:

```text
OPEN
RESOLVING
RETRIEVING
ASSEMBLING
FULFILLED
BLOCKED
FAILED
CANCELLED
```

These states describe Context assembly, not Workflow state.

## 2. Context Bundle lifecycle

Bundle content lifecycle:

```text
ASSEMBLING
→ SEALED
→ CONSUMED
→ HISTORICAL
```

This is distinct from validity:

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
STALE
INVALIDATED
```

## 3. Immutability

After `SEALED`, Bundle payload is immutable for provenance.

Validity assessments may evolve without rewriting the payload.

Reassembly produces a new Bundle identity.

## 4. Context Bundle identity vs version

A Context Bundle is not semver-versioned.

```text
new assembly/reassembly
→ new context_bundle_id
```

Normative Module-05 contracts themselves use governed document versions.

## 5. Context policy version

`context_policy_version` is recorded on Request/Bundle and may change independently from source versions.

A policy change MAY trigger reassembly where material.

## 6. Memory lifecycle

Memory item lifecycle is defined in `MEMORY_LIFECYCLE_AND_INVALIDATION.md`.

It MUST NOT be confused with UPOS-01 Knowledge Lifecycle.

## 7. Replay/audit support

The system must preserve enough semantic references to reconstruct:

```text
Task
Workflow Instance
Stage
Role / Agent Run
Skill Invocation
Context Request
Context Bundle
source versions
memory items that affected execution
output reference
```

Event Store/trace implementation remains UPOS-008/runtime.
