# Engineering Check Integration

**ID:** UPOS-06-CHK-001  
**Type:** ENGINEERING CHECK REFERENCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Purpose

UPOS-006 owns mechanical attachment of engineering check executions/results to exact repository artifacts.

It does not own which checks are required or what counts as sufficient Quality evidence.

## 2. Check kinds

Provider-neutral examples:

```text
build
test
lint
type-check
static-analysis
format-validation
generated-code-consistency
migration-validation
```

The physical command/provider belongs to UPOS-011.

## 3. Engineering Check Reference

Minimal semantic contract:

```text
check_ref
artifact_ref / commit_ref / head_revision_ref
check_kind
execution_ref
result_ref
provider_binding_ref
```

`check_ref` identifies the attached check relationship/result reference.

## 4. Artifact binding

A check MUST be attributable to the exact artifact identity it evaluated.

If the artifact changes:

```text
old check
must not silently remain associated
with the new artifact state
```

UPOS-006 exposes `CHECK_ARTIFACT_MISMATCH` / stale-artifact condition.

UPOS-007 decides whether rerun/revalidation is required.

## 5. CI boundary

```text
CI/check execution/attachment mechanics → UPOS-006 + adapters
required checks / evidence sufficiency  → UPOS-007 / UPOS-004 / project policy
physical commands/provider             → UPOS-011
```

```text
CI green != Quality PASS
```

## 6. Review artifact change

If new commits/history rewrite/rebase changes the reviewed head/commit set:

```text
REVIEW_ARTIFACT_CHANGED
```

is emitted as an engineering condition.

Module 06 MUST NOT assert old review evidence remains valid.

## 7. Merge invalidation inputs

Mechanical readiness package may become stale when:

- head revision changes;
- base revision materially changes;
- unresolved conflict appears;
- required engineering reference disappears;
- selected strategy is no longer available.

External approval/Quality validity remains with their owners.


## 8. Context revalidation interface

Repository artifact change and Context freshness are distinct concerns.

When Module 06 detects:

```text
REVIEW_ARTIFACT_CHANGED
CHECK_ARTIFACT_MISMATCH
material head/base revision change
```

and a previously consumed Context Bundle is intended for continued review/rework/merge-related use, the engineering layer MUST expose the exact changed artifact/revision to UPOS-005 for Context revalidation.

UPOS-005 owns whether the prior Bundle remains `VALID`, becomes `STALE` / `INVALIDATED`, or requires reassembly.

If reassembly occurs, Module 06 records the new upstream `context_bundle_id` reference and preserves the prior Bundle reference as historical provenance where relevant.
