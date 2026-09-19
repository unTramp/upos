# Concurrency, Collision and Conflict

**ID:** UPOS-06-CCC-001  
**Type:** CONCURRENCY / COLLISION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 parallelism interface


## 1. Boundary

```text
Workflow logical parallelism
→ UPOS-004

Repository workspace / branch isolation
→ UPOS-006

runtime/model concurrency
→ runtime / UPOS-011
```

UPOS-004 decides whether work should proceed in parallel.
UPOS-006 reports whether repository mechanics make that parallelism safe.

## 2. Collision taxonomy

Canonical v1 engineering collision classes:

```text
FILE_OVERLAP
DIFF_OVERLAP
SHARED_CONTRACT_DEPENDENCY
GENERATED_ARTIFACT_COLLISION
MIGRATION_ORDER_COLLISION
BRANCH_BASE_DIVERGENCE
SEMANTIC_INTEGRATION_COLLISION
```

### FILE_OVERLAP
Concurrent units touch one or more same files.

### DIFF_OVERLAP
Concurrent edits affect overlapping hunks/lines/regions.

### SHARED_CONTRACT_DEPENDENCY
Two units depend on a shared contract whose unresolved state can cause incompatible implementation.

### GENERATED_ARTIFACT_COLLISION
Separate source changes regenerate/modify the same derived artifact.

### MIGRATION_ORDER_COLLISION
Repository migration artifacts require total/partial ordering that concurrent units violate.

### BRANCH_BASE_DIVERGENCE
Change units diverge materially from a common/required integration base.

### SEMANTIC_INTEGRATION_COLLISION
Changes may merge textually yet compose incorrectly at behavior/contract level.

File overlap is therefore neither necessary nor sufficient for semantic collision.

## 3. Engineering constraint results

UPOS-006 may report:

```text
SAFE_TO_PARALLELIZE
SERIALIZATION_REQUIRED
REBASE_REQUIRED
INTEGRATION_COORDINATION_REQUIRED
CONFLICT_PRESENT
```

These are engineering constraints, not Workflow transitions.

UPOS-004 owns the orchestration response.

## 4. Concurrent writer invariant

Two independent writers MUST NOT silently mutate one writable workspace.

Safe patterns include:

- separate workspace per Agent Run/RCU;
- explicit serialization;
- explicit ownership transfer;
- integration coordinator with separately attributable units.

## 5. Shared contract first

Before dependent surfaces are implemented concurrently, stable shared contracts SHOULD exist where required.

UPOS-006 consumes contract references and never creates Product/Domain/API truth.

## 6. Collision detection inputs

Detection may consider:

- repository/base revision;
- planned/touched paths;
- staged/uncommitted diff;
- branch/head revisions;
- generated artifact relationships;
- migration ordering;
- dependency graph references;
- shared contract references.

Concrete detection implementation belongs to runtime/UPOS-011.

## 7. Collision provenance

Collision reports SHOULD identify involved:

```text
engineering_change_id
repository_change_unit_id values
workspace_id values
branch_ref values
Agent Run references
base/head revision refs
collision class
affected artifacts
```

UPOS-008 later may observe these reports; Module 06 does not define event schemas.
