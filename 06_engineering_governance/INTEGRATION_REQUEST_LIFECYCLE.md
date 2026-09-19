# Integration Request Lifecycle

**ID:** UPOS-06-IRL-001  
**Type:** LIFECYCLE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Lifecycle

Canonical repository-mechanical lifecycle:

```text
DRAFT
→ OPEN
→ MERGED
```

Alternate:

```text
DRAFT / OPEN
→ CLOSED
```

Replacement:

```text
DRAFT / OPEN
→ SUPERSEDED
```

## 2. State meanings

- `DRAFT`: container exists but producer has not declared review-ready intent.
- `OPEN`: active review/integration container; may or may not currently be `ready_for_review`.
- `CLOSED`: ended without merge.
- `MERGED`: merge/integration operation produced a resulting integrated revision.
- `SUPERSEDED`: another Integration Request replaces it.

## 3. Forbidden Quality-state leakage

Module-06 lifecycle MUST NOT use:

```text
APPROVED
CHANGES_REQUESTED
QA_PASSED
SECURITY_PASSED
READY_TO_MERGE
```

as lifecycle states.

Those are external result/readiness concepts.

## 4. ready_for_review flag

`ready_for_review` is producer intent, not a verdict.

It may change within `OPEN`.

## 5. Lifecycle vs Workflow

Integration Request lifecycle is independent from:

- Task lifecycle;
- Workflow Instance state;
- Agent Run lifecycle;
- Quality gate state;
- release/deployment state.
