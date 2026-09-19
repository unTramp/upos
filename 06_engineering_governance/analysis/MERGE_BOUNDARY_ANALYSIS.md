# Merge Boundary Analysis

**ID:** UPOS-06-AN-008  
**Type:** ANALYSIS / MERGE OWNERSHIP  
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

## Ownership split

```text
MERGE AUTHORITY
→ UPOS-002

MERGE ORCHESTRATION POSITION
→ UPOS-004

MERGE READINESS QUALITY
→ UPOS-007

MERGE PERMISSION
→ UPOS-010

MERGE MECHANICS
→ UPOS-006

PROVIDER/API/TARGET
→ UPOS-011
```

## Mechanical result

Module 06 may report:

```text
MECHANICALLY_MERGEABLE
```

but never:

```text
APPROVED_TO_MERGE
```

as an authority/quality conclusion.

## Merge Operation identity

`merge_operation_id` is justified because a merge attempt/action is a U-POS engineering operation, not merely a revision object, and must correlate actor/permission/readiness/source/target/resulting revision.

## Strategy

Strategy stays abstract/configurable. Provenance must survive squash/rewrite transformations.
