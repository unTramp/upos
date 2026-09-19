# PR / Integration Request Analysis

**ID:** UPOS-06-AN-006  
**Type:** ANALYSIS / INTEGRATION CONTAINER  
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

## Problem

Frozen source uses `PR`, but universal ontology must not depend on one provider.

## Decision

```text
INTEGRATION REQUEST
= provider-neutral coherent repository review/integration container
```

Provider mapping belongs UPOS-011.

## Cohesion

```text
Commit = one logical change
Integration Request = one reviewable intention
```

An Integration Request may contain several atomic commits.

## Lifecycle decision

Adopt repository-mechanical states only:

```text
DRAFT
OPEN
CLOSED
MERGED
SUPERSEDED
```

Keep `ready_for_review` as producer intent flag.

Reject Quality states such as `APPROVED`, `QA_PASSED`, `CHANGES_REQUESTED`.

## Stable review artifact

Use reconstructible tuple/refs:

```text
repository
base revision
head revision
commit set
diff/change ref
engineering provenance
```

Reviewer Context remains UPOS-005 pending.
