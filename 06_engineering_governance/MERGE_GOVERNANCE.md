# Merge Governance

**ID:** UPOS-06-MRG-001  
**Type:** MERGE MECHANICS STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-002, UPOS-004, UPOS-007, UPOS-010, UPOS-011


## 1. Ownership matrix

| Concern | Canonical owner |
|---|---|
| Merge authority | UPOS-002 / Human Governance |
| Merge orchestration position | UPOS-004 |
| Merge readiness Quality | UPOS-007 |
| Merge permission/protected action | UPOS-010 |
| Merge mechanics / artifact integration | UPOS-006 |
| Provider/API/target binding | UPOS-011 |
| Context used for readiness/actor views | UPOS-005 |

Module 06 MUST NOT collapse these concerns.

## 2. Mechanical mergeability

UPOS-006 MAY report:

```text
MECHANICALLY_MERGEABLE
MECHANICALLY_BLOCKED
STALE_BASE_UPDATE_REQUIRED
CONFLICT_PRESENT
```

Mechanical mergeability may check:

- source/head and target/base references exist;
- no unresolved VCS conflict;
- required engineering references are present;
- target is current enough under engineering policy;
- an allowed integration strategy is available.

```text
MECHANICALLY_MERGEABLE
!=
APPROVED_TO_MERGE
```

## 3. Merge Operation

```text
MERGE OPERATION
= governed repository integration action producing or attempting to produce an integrated revision
```

Every Merge Operation MUST have:

```text
merge_operation_id
```

and SHOULD preserve/reference:

```text
integration_request_ref
engineering_change_id
repository_change_unit_id

target/integration reference
source/head reference

pre_merge_base_revision_ref
pre_merge_head_revision_ref
selected_merge_strategy_ref

Merge Controller / actor reference
permission_ref
approval_ref
quality/readiness refs

resulting_integrated_revision_ref
timestamp/provenance interface
operation_result
```

Machine schema is deferred.

## 4. Strategy

Universal Module 06 does not force:

- merge commit;
- squash;
- rebase integration;
- fast-forward.

UPOS-011/project policy selects allowed/default strategies.

No allowed strategy may silently destroy required provenance.

## 5. Squash integrity

If integration transforms a commit set, resulting revision MUST remain traceable to:

```text
Integration Request
original commit set
Task
Engineering Change
Repository Change Unit
```

## 6. History rewrite

Rebase/amend/force update before integration may invalidate artifact identity.

Module 06 exposes the artifact change.

UPOS-007 determines whether Quality evidence/review remains valid.

## 7. Merge invalidation

A previously assembled integration package can become stale when:

- head revision changes;
- base revision changes materially;
- VCS conflict appears;
- required engineering reference changes;
- external approval/result changes.

UPOS-006 owns only engineering artifact-change detection.

External result validity belongs to its owner.

## 8. Context revalidation interface

A material head/base/artifact change detected by Module 06 may invalidate assumptions of a Context Bundle intended for continued Merge Controller/readiness use.

Module 06 reports the exact repository artifact/revision change.

UPOS-005 revalidates the applicable Context Bundle and, if required, assembles a new immutable Bundle with a new `context_bundle_id`.

Module 06 MUST NOT assign Context validity/freshness states.

## 9. Merge Controller interface

Module 06 exposes:

```text
integration_request_ref
base_revision_ref
head_revision_ref
commit_set
mechanical conflict state
artifact-change/staleness status
engineering check refs
required external-result refs
allowed merge-strategy refs
engineering provenance
```

UPOS-002 owns whether the Merge Controller may act.

## 10. Queue/provider interfaces

A project/provider may integrate through a merge/integration queue.

Universal Module 06 models this only as an integration mechanism reference.
Concrete queue/API belongs to UPOS-011.

## 11. Protected target

Protected-target write capability is declared by Module 06 when required.

Grant/approval belongs to UPOS-010.
