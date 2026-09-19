# Branch Governance

**ID:** UPOS-06-BRG-001  
**Type:** BRANCH / HISTORY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Change Branch

```text
CHANGE BRANCH
= version-control branch associated with one bounded Repository Change Unit
```

Module 06 does not prescribe physical names or a universal branching model.

## 2. Branch roles

Semantic references MAY include:

```text
integration_branch_ref
change_branch_ref
release_branch_ref       # only where project policy uses one
hotfix_branch_ref        # only where project policy uses one
```

Concrete names/patterns belong to UPOS-011.

## 3. Invariants

A Change Branch MUST be:

- attributable;
- bounded in purpose;
- associated with an RCU;
- traceable to upstream Task/Workflow;
- protected from unrelated work;
- based on an explicit base revision/target reference.

## 4. Shared branch rule

A shared branch MUST NOT become an ungoverned dumping ground for unrelated Tasks/Engineering Changes.

If multiple RCUs intentionally share a branch, project policy MUST explicitly permit it and Module-06 provenance MUST preserve unit boundaries.

Default preference remains one coherent RCU per Change Branch.

## 5. Direct-to-integration mutation

Module 06 does not universally require branch + Integration Request for every change.

Direct integration-target mutation is allowed only when it is:

```text
explicitly permitted
attributable
policy-governed
traceable
compatible with required Workflow/Quality/Security gates
```

Permission belongs to UPOS-010; concrete policy/provider implementation belongs to UPOS-011.

## 6. Branch lifetime

Change branches SHOULD be short-lived where practical because long-lived divergence raises integration risk.

No universal duration threshold is defined.

## 7. Base update / rebase governance

Updating a branch base or rebasing may change commit identities and reviewed artifact identity.

Such operations MUST:

- preserve engineering provenance;
- expose changed commit/head identity;
- mark prior check/review associations as referring to the previous artifact;
- never claim prior Quality evidence remains valid for the new artifact.

Quality validity/re-review decisions belong to UPOS-007.

## 8. Amend / force update / history rewrite

History-rewriting operations are classified as:

```text
history-rewriting
shared-history-impacting when applicable
```

Module 06 declares the engineering condition/capability need.

Permission/grants belong to UPOS-010.

## 9. Protected target interface

Integration branches/targets MAY require protection policy.

Module 06 consumes protection constraints but does not define provider settings or grants.

## 10. Release source-control artifacts

Where project policy uses source-control release artifacts, Module 06 may govern their repository mechanics through abstract refs such as:

```text
release_branch_ref
tag_ref
release_revision_ref
```

They MUST reference exact repository revisions/provenance.

Release Workflow sequencing remains UPOS-004.
Release Quality remains UPOS-007.
Deployment/release execution remains outside Module 06.
Naming/version/provider rules belong to UPOS-011/project policy.

Module 06 MUST NOT silently retarget a governed tag/release reference to different code when project policy forbids mutation.
