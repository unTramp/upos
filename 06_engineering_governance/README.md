# UPOS-006 — Engineering Governance

**ID:** UPOS-06-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, UPOS-003, UPOS-004, UPOS-005 FROZEN v1.0 interface


## 0. Status

```text
UPOS-006 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-005 INTERFACE RECONCILIATION:
COMPLETE

UPOS-006 FREEZE STATUS:
FROZEN v1.0
```

**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

The UPOS-005 narrow reconciliation was completed against FROZEN UPOS-005 Context & Memory v1.0.


## 1. Purpose

UPOS-006 defines how already governed work becomes safe, bounded, attributable repository change.

It owns repository engineering mechanics:

```text
Engineering Change
→ Repository Change Unit(s)
→ isolated Repository Workspace
→ Change Branch / governed direct-integration path
→ Atomic Commit(s)
→ Integration Request
→ Engineering Check references
→ mechanically governed Merge Operation
→ Integrated Revision
→ possible repository Revert / Backout
```

It does not own Task/Workflow semantics, Role authority, Quality verdicts, Context semantics, permissions, telemetry, or provider/project bindings.

## 2. Fundamental entities

```text
ENGINEERING CHANGE
= bounded engineering realization of approved/routed work

REPOSITORY CHANGE UNIT
= one repository-scoped portion of an Engineering Change

REPOSITORY WORKSPACE
= isolated writable repository environment for one bounded change unit/execution

CHANGE BRANCH
= version-control branch associated with a bounded Repository Change Unit

COMMIT
= atomic version-control change representing one coherent logical intent

INTEGRATION REQUEST
= provider-neutral review/integration container for one coherent repository intention

ENGINEERING CHECK REFERENCE
= attributable reference to build/test/lint/static-analysis/etc execution against a specific artifact

MERGE OPERATION
= governed repository integration action

ENGINEERING PROVENANCE
= attributable relationships between upstream execution scope and repository artifacts/actions
```

These entities MUST NOT be used interchangeably.

## 3. Stable semantic identities

Module 06 owns:

```text
engineering_change_id
repository_change_unit_id
workspace_id
merge_operation_id
```

For native version-control/provider objects, Module 06 prefers stable references instead of duplicate U-POS IDs:

```text
repository_ref
branch_ref
commit_ref
integration_request_ref
revision_ref
check_ref
execution_ref
result_ref
```

Upstream identities are reused unchanged:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
Agent Run reference
Skill Invocation reference
```

## 4. Core invariants

```text
Implementer != Final Reviewer
```

For high-risk work:

```text
Implementer != Reviewer != Merge Controller
```

These are consumed from UPOS-002. Module 06 makes repository mechanics compatible with them but grants no authority.

```text
COMMIT SIZE != COMMIT QUALITY
```

```text
Commit = one coherent logical intent.
Integration Request = one coherent reviewable repository intention.
```

```text
two independent concurrent writers
MUST NOT silently share
the same writable workspace
```

```text
MECHANICALLY_MERGEABLE
!=
APPROVED_TO_MERGE
```

```text
CI/check success
!=
Quality PASS
```

```text
repository revert/backout
!=
deployment rollback
!=
database rollback
!=
business compensation
```

## 5. Provider-neutral terminology

`Integration Request` is the canonical Module-06 concept.

Provider-specific review-container names and APIs belong to UPOS-011.

Git-like version-control semantics (`branch`, `commit`, `revision`, `merge`) are assumed by v1, but no hosting/provider product is part of the universal ontology.

## 6. Context boundary — reconciled with FROZEN UPOS-005 v1.0

UPOS-006 reuses stable Module-05 identities when repository provenance must identify the execution Context that informed an engineering artifact:

```text
context_request_id
context_bundle_id
```

Module 06 does not create a `context_view_id`.

Role-/Run-/Reviewer-specific Context is supplied by UPOS-005 through its Context Request / Context Bundle model; the Bundle already carries Role, Agent Run, Task, Workflow Instance, Stage, Skill and policy attribution.

Engineering artifacts MAY reference one or more `context_bundle_id` values actually consumed during their creation/review.

Context provenance beyond that reference is followed through the UPOS-005 Context Bundle / Context Manifest rather than copied into Module 06.

When repository artifacts materially change and prior Context is intended for reuse:

```text
UPOS-006 emits artifact/base/head change
→ UPOS-005 revalidates the prior Bundle
→ if reassembly is required, a new context_bundle_id is created
→ old consumed Bundle remains immutable provenance
```

UPOS-006 MUST NOT redefine:

```text
Context Request/Bundle validity states
Context freshness / invalidation
Context isolation / Context View semantics
Context budget / retrieval / source selection
Memory semantics
Reviewer / Implementer Context contents
```

**Reconciled upstream source SHA-256:** `186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528`


## 7. Read order

1. `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md`
2. `ENGINEERING_CHANGE_MODEL.md`
3. `REPOSITORY_CHANGE_UNIT_STANDARD.md`
4. `REPOSITORY_WORKSPACE_AND_ISOLATION.md`
5. `BRANCH_GOVERNANCE.md`
6. `ATOMIC_COMMIT_STANDARD.md`
7. `COMMIT_PROVENANCE_STANDARD.md`
8. `INTEGRATION_REQUEST_STANDARD.md`
9. `INTEGRATION_REQUEST_LIFECYCLE.md`
10. `ENGINEERING_CHECK_INTEGRATION.md`
11. `CONCURRENCY_COLLISION_AND_CONFLICT.md`
12. `MULTI_REPOSITORY_CHANGE_MODEL.md`
13. `MERGE_GOVERNANCE.md`
14. `REVERT_BACKOUT_AND_RECOVERY.md`
15. `SPECIAL_REPOSITORY_ARTIFACTS.md`
16. `ENGINEERING_PROVENANCE_MODEL.md`
17. `ENGINEERING_FAILURE_MODEL.md`
18. `ENGINEERING_LIFECYCLE_AND_VERSIONING.md`
19. `CROSS_MODULE_INTERFACES.md`
20. `MODULE_06_DEFINITION_OF_DONE.md`
21. `MODULE_06_TRACEABILITY.md`
