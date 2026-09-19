# Revert, Backout and Repository Recovery

**ID:** UPOS-06-RBR-001  
**Type:** REPOSITORY RECOVERY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 recovery orchestration interface


## 1. Definitions

```text
REVERT
= repository change that semantically reverses effects of prior integrated repository change(s)

BACKOUT
= controlled repository integration action that removes/reverses a prior integrated change from the target history/state
```

Projects/providers may realize these differently.

## 2. Boundary

Repository Revert/Backout is not:

```text
deployment rollback
traffic shift
database restore
data rollback
payment compensation
business compensation
```

Those belong to operations/data/domain systems.

## 3. Traceability

A revert/backout MUST reference:

```text
original_integrated_revision_ref
original_engineering_change_id
original_repository_change_unit_id where known
reason
new task/workflow reference where applicable
new engineering_change_id / repository_change_unit_id
new commit_ref / integration_request_ref
resulting revision
```

Original history/provenance MUST NOT be erased.

## 4. Workflow boundary

UPOS-004 may require a rollback/recovery strategy and decides orchestration.

UPOS-006 executes/governs only repository-level mechanics.

## 5. Revert as new governed change

Unless provider mechanics produce an immediate protected emergency backout under explicit policy, a revert SHOULD itself be modeled as a new attributable Engineering Change/RCU so its intent, reviewability, checks, and merge provenance are explicit.

## 6. Abandoned work

When work is abandoned:

- workspace transitions to `ABANDONED` or `RELEASED` as appropriate;
- branch disposition is recorded;
- open Integration Request is closed/superseded as appropriate;
- temporary artifacts may be cleaned;
- audit-relevant provenance remains.

## 7. Recovery does not rewrite history silently

Recovery actions MUST preserve references explaining what was integrated, what was reversed, and what replaced it.
