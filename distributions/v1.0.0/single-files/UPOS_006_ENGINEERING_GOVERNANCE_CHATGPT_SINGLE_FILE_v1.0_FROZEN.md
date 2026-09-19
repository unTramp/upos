# UPOS-006 Engineering Governance — ChatGPT Single-File Edition v1.0

**Module:** UPOS-006 — Engineering Governance  
**System:** Universal Project Operating System  
**Canonical baseline:** FROZEN v1.0  
**UPOS-005 reconciliation:** COMPLETE  
**FROZEN UPOS-005 SHA-256:** `186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528`  
**Embedded virtual files:** 42  
**Generated:** 2026-09-19

---

# 0. Interpretation rule

This is a transport bundle, not a replacement monolith.

Each virtual-file block represents one repository file under `06_engineering_governance/`.

Normative authority remains with the embedded normative Markdown documents.

`analysis/` is historical EVIDENCE only.

`MODULE_06_TRACEABILITY.md` is the canonical normative coverage artifact.

## Core Engineering model

```text
Task / Workflow / Stage
→ Context Request / Context Bundle
→ Engineering Change
→ Repository Change Unit(s)
→ isolated Repository Workspace
→ Change Branch / governed direct path
→ Atomic Commit(s)
→ Integration Request
→ Engineering Check references
→ Merge Operation
→ Integrated Revision
→ possible Revert / Backout
```

## Context reconciliation

```text
context_request_id
context_bundle_id
```

are reused from FROZEN UPOS-005.

`context_view_id` is NOT introduced.

Changed artifact/rework Context flow:

```text
UPOS-006 artifact change
→ UPOS-005 Bundle revalidation
→ new context_bundle_id if reassembled
→ old consumed Bundle remains immutable provenance
```

## Frozen validation

```text
UPOS-005 reconciliation items resolved = 9 / 9
Unresolved internal/interface P0/P1 gaps = 0
Active operational normative UPOS-005 pending markers = 0
Canonical operational template conformance = PASS
Hard-coded provider/project paths = 0

UNMAPPED MODULE-06 SOURCE REQUIREMENTS = 0

NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 04 / 05 / 07–11
```

# 1. Virtual repository tree

```text
06_engineering_governance/
├── README.md
├── ENGINEERING_GOVERNANCE_OPERATING_MODEL.md
├── ENGINEERING_CHANGE_MODEL.md
├── REPOSITORY_CHANGE_UNIT_STANDARD.md
├── REPOSITORY_WORKSPACE_AND_ISOLATION.md
├── BRANCH_GOVERNANCE.md
├── ATOMIC_COMMIT_STANDARD.md
├── COMMIT_PROVENANCE_STANDARD.md
├── INTEGRATION_REQUEST_STANDARD.md
├── INTEGRATION_REQUEST_LIFECYCLE.md
├── ENGINEERING_CHECK_INTEGRATION.md
├── CONCURRENCY_COLLISION_AND_CONFLICT.md
├── MULTI_REPOSITORY_CHANGE_MODEL.md
├── MERGE_GOVERNANCE.md
├── REVERT_BACKOUT_AND_RECOVERY.md
├── SPECIAL_REPOSITORY_ARTIFACTS.md
├── ENGINEERING_PROVENANCE_MODEL.md
├── ENGINEERING_FAILURE_MODEL.md
├── ENGINEERING_LIFECYCLE_AND_VERSIONING.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_06_DEFINITION_OF_DONE.md
├── MODULE_06_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── templates/COMMIT_PROVENANCE_TEMPLATE.md
├── templates/ENGINEERING_CHANGE_TEMPLATE.md
├── templates/INTEGRATION_REQUEST_TEMPLATE.md
├── templates/MERGE_OPERATION_TEMPLATE.md
├── templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md
├── analysis/COMMIT_ATOMICITY_ANALYSIS.md
├── analysis/CONCURRENCY_COLLISION_ANALYSIS.md
├── analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MERGE_BOUNDARY_ANALYSIS.md
├── analysis/MODULE_06_OWNERSHIP_MAP.md
├── analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md
```

# 2. Embedded files


---

## VIRTUAL FILE 1/42 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `b274bc1521eb`

===== BEGIN VIRTUAL FILE: README.md =====

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

===== END VIRTUAL FILE: README.md =====


---

## VIRTUAL FILE 2/42 — `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md`

**Virtual path:** `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md`  
**Content checksum:** `99fbb9f89dd3`

===== BEGIN VIRTUAL FILE: ENGINEERING_GOVERNANCE_OPERATING_MODEL.md =====

# Engineering Governance Operating Model

**ID:** UPOS-06-EGO-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Ownership

UPOS-006 is the canonical owner of repository engineering mechanics and artifact relationships.

It owns:

- Engineering Change and Repository Change Unit semantics;
- writable workspace isolation;
- Change Branch semantics;
- atomic commit policy and history-integrity rules;
- provider-neutral Integration Request mechanics;
- engineering check attachment/artifact-binding mechanics;
- collision/concurrency reporting;
- multi-repository engineering coordination mechanics;
- mechanical mergeability and Merge Operation mechanics;
- repository revert/backout mechanics;
- engineering provenance;
- engineering failure taxonomy;
- engineering object lifecycle/versioning.

## 2. Non-ownership

UPOS-006 MUST NOT redefine:

| Concern | Owner |
|---|---|
| canonical project truth / documentation authority | UPOS-01 |
| Roles, authority, delegation, SoD, Human Governance, Merge Controller authority | UPOS-002 |
| Skill procedures | UPOS-003 |
| Task, Change Class, Workflow, Stage, transition, retry/rework orchestration | UPOS-004 |
| Context retrieval/assembly/memory/freshness/isolation | UPOS-005 |
| Review findings, QA evidence, Quality verdicts, evidence sufficiency | UPOS-007 |
| events/traces/metrics/dashboard | UPOS-008 |
| organizational learning/promotion | UPOS-009 + UPOS-01 |
| permission grants, protected actions, secrets, production access | UPOS-010 |
| repository provider bindings, paths, branch names, CI commands/APIs | UPOS-011 |

## 3. Engineering chain

```text
Task / Routing / Workflow Stage      [UPOS-004]
        ↓
Role / Agent Run / Skills           [UPOS-002 / 003]
        ↓
Context Request / Context Bundle   [UPOS-005]
        ↓
ENGINEERING CHANGE                  [UPOS-006]
        ↓
REPOSITORY CHANGE UNIT(S)           [UPOS-006]
        ↓
isolated WORKSPACE(S)               [UPOS-006]
        ↓
CHANGE BRANCH / governed direct path[UPOS-006 mechanics]
        ↓
ATOMIC COMMITS                      [UPOS-006]
        ↓
INTEGRATION REQUEST(S)              [UPOS-006]
        ↓
Review / QA / Security refs         [external semantics]
        ↓
Merge readiness / authority / perm. [UPOS-007 / 002 / 010]
        ↓
MERGE OPERATION                     [UPOS-006 mechanics]
        ↓
INTEGRATED REVISION                 [UPOS-006 provenance]
```

## 4. Engineering Change is not a Task

Engineering Change is a repository realization of already governed work.

It never creates a second Task or Workflow state machine.

## 5. Engineering mechanics are not authority

A repository action being mechanically possible does not mean an Agent/Role is authorized to perform it.

```text
capability requirement → UPOS-006 declares
grant/deny            → UPOS-010
organizational authority → UPOS-002
workflow timing       → UPOS-004
provider invocation   → UPOS-011
```

## 6. Engineering mechanics are not Quality

Module 06 may bind checks/reviews to exact artifact identities and signal staleness.

It does not determine whether evidence is sufficient or whether the change passes Quality.

## 7. Engineering provenance is not observability

Engineering provenance describes durable semantic relationships among artifacts.

UPOS-008 later observes those entities with events/traces/metrics.

## 8. Project policy extension

Projects may be stricter:

- signed commits;
- branch naming rules;
- mandatory squash;
- green-history rules;
- multiple reviewers;
- force-update prohibition;
- target-specific protection.

Those concrete rules/bindings belong to UPOS-011 and/or their owning policy modules.

Universal Module 06 defines the invariant/interface, not project wiring.

===== END VIRTUAL FILE: ENGINEERING_GOVERNANCE_OPERATING_MODEL.md =====


---

## VIRTUAL FILE 3/42 — `ENGINEERING_CHANGE_MODEL.md`

**Virtual path:** `ENGINEERING_CHANGE_MODEL.md`  
**Content checksum:** `0640cf21b989`

===== BEGIN VIRTUAL FILE: ENGINEERING_CHANGE_MODEL.md =====

# Engineering Change Model

**ID:** UPOS-06-ECM-001  
**Type:** ENTITY / SCOPE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 Task/Workflow interfaces


## 1. Definition

```text
ENGINEERING CHANGE
= bounded engineering realization of approved/routed work
```

An Engineering Change is not a Task, Workflow, Feature, release, or Quality verdict.

## 2. Identity

Every Engineering Change MUST have stable:

```text
engineering_change_id
```

The identifier remains stable across its Repository Change Units, workspaces, branches, Integration Requests, merge operations, and repository recovery actions.

## 3. Upstream attribution

Where applicable, Engineering Change MUST reference:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
```

It MAY additionally reference:

```text
Role / Agent Run
Skill Invocation
Implementation Plan
canonical source / decision refs
Context Bundle ID reference(s) using upstream `context_bundle_id`
```

It MUST NOT create replacement identities for upstream entities.

## 4. Implementation Plan boundary

```text
Implementation Plan
→ UPOS-003 Skill output / governed knowledge artifact

Workflow execution
→ UPOS-004

Engineering Change / Repository Change Units
→ UPOS-006
```

UPOS-006 consumes the relevant plan reference where required; it does not own Product/Architecture intent.

## 5. Scope

An Engineering Change declares:

- purpose;
- approved/routed scope;
- non-scope;
- affected repository references;
- Repository Change Unit membership;
- dependency relationships;
- implementation-plan reference where applicable;
- discovered scope/architecture risks.

## 6. Scope expansion

No silent scope expansion.

When repository work reveals necessary out-of-scope work:

```text
UPOS-006 emits SCOPE_EXPANSION
→ UPOS-004 decides pause/reclassify/reroute/split
```

## 7. Architecture discovery

If implementation requires an unapproved architecture decision:

```text
Engineering Change
→ emit blocking discovery signal
→ Architecture / Workflow governance resolves
```

Repository implementation does not become architecture authority.

## 8. Multi-repository realization

One Engineering Change MAY contain one or many Repository Change Units.

It MUST NOT assume one Task = one repository.

## 9. Completion semantics

Engineering completion means its repository integration contract is satisfied for all required Repository Change Units.

It does NOT imply:

```text
Task DONE
Workflow COMPLETED
Quality PASS
release completed
deployment succeeded
```

## 10. Abandonment

An Engineering Change may be abandoned.

Abandonment MUST preserve enough provenance to explain:

- what existed;
- what was not integrated;
- workspace/branch/Integration Request disposition;
- why the change stopped;
- any superseding change.

## 11. Context interface

Engineering execution SHOULD be attributable to the governed Context actually supplied by UPOS-005.

Module 06 references the stable upstream identity:

```text
context_bundle_id
```

An Engineering Change MAY reference more than one `context_bundle_id` because one bounded change may span multiple Agent Runs, Stages, Skills, or rework cycles.

Where direct request-level provenance is materially useful, Module 06 MAY additionally reference the upstream:

```text
context_request_id
```

The authoritative Context provenance chain remains:

```text
context_request_id
→ context_bundle_id
→ Context Manifest / source refs / memory refs
```

owned by UPOS-005.

Module 06 does not define Context validity, freshness, View, isolation, budget, retrieval, or reassembly semantics.

===== END VIRTUAL FILE: ENGINEERING_CHANGE_MODEL.md =====


---

## VIRTUAL FILE 4/42 — `REPOSITORY_CHANGE_UNIT_STANDARD.md`

**Virtual path:** `REPOSITORY_CHANGE_UNIT_STANDARD.md`  
**Content checksum:** `d8fa8d9d3d53`

===== BEGIN VIRTUAL FILE: REPOSITORY_CHANGE_UNIT_STANDARD.md =====

# Repository Change Unit Standard

**ID:** UPOS-06-RCU-001  
**Type:** ENTITY / REPOSITORY-SCOPE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Definition

```text
REPOSITORY CHANGE UNIT
= one coherent repository-scoped portion of an Engineering Change
```

A Repository Change Unit (RCU) is the primary boundary for repository isolation, branch association, commit history, Integration Request mechanics, and repository integration.

## 2. Identity

Every RCU MUST have stable:

```text
repository_change_unit_id
```

## 3. Required attribution

An RCU MUST reference:

```text
repository_change_unit_id
engineering_change_id
repository_ref
task_id
workflow_instance_id
base_revision_ref
purpose
scope
non_scope
dependency_refs
```

Where applicable:

```text
stage_id
workspace_id
branch_ref
integration_request_ref
integrated_revision_ref
```

## 4. Base revision

Every RCU MUST know the repository state from which it began:

```text
base_revision_ref
```

This supports:

- diff reconstruction;
- review reproducibility;
- collision analysis;
- staleness detection;
- update-base/rebase decisions.

## 5. One repository

An RCU belongs to exactly one logical repository reference.

Cross-repository coordination belongs to the parent Engineering Change plus `MULTI_REPOSITORY_CHANGE_MODEL.md`.

## 6. Coherence

An RCU SHOULD represent one coherent repository intention.

Do not split by arbitrary file count.

Do not combine unrelated work merely because it touches the same repository.

## 7. Operational lifecycle

Canonical RCU lifecycle:

```text
PREPARED
→ ACTIVE
→ INTEGRATION_REQUEST_OPEN
→ INTEGRATED

alternate:
PREPARED / ACTIVE / INTEGRATION_REQUEST_OPEN
→ ABANDONED

replacement:
PREPARED / ACTIVE / INTEGRATION_REQUEST_OPEN
→ SUPERSEDED
```

These are repository-mechanical states, not Workflow or Quality states.

## 8. Integration order

An RCU MAY declare dependencies on other RCUs.

UPOS-006 exposes the engineering dependency; UPOS-004 owns overall orchestration.

## 9. Artifact staleness

An RCU may become mechanically stale when:

- integration base materially advances;
- required upstream RCU/revision changes;
- branch/history is rewritten;
- generated/migration artifacts diverge;
- reviewed/check artifact identity no longer matches current head.

Staleness here is engineering artifact staleness, not Context staleness.

===== END VIRTUAL FILE: REPOSITORY_CHANGE_UNIT_STANDARD.md =====


---

## VIRTUAL FILE 5/42 — `REPOSITORY_WORKSPACE_AND_ISOLATION.md`

**Virtual path:** `REPOSITORY_WORKSPACE_AND_ISOLATION.md`  
**Content checksum:** `f48b6300b8c0`

===== BEGIN VIRTUAL FILE: REPOSITORY_WORKSPACE_AND_ISOLATION.md =====

# Repository Workspace and Isolation

**ID:** UPOS-06-WSI-001  
**Type:** WORKSPACE / ISOLATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Definition

```text
REPOSITORY WORKSPACE
= isolated writable repository environment assigned to a bounded Repository Change Unit/execution
```

Possible realizations include separate working trees, clones, sandboxes, or remote isolated workspaces.

Concrete realization belongs to UPOS-011/runtime.

## 2. Identity

Every Workspace MUST have stable:

```text
workspace_id
```

## 3. Isolation invariant

```text
two independent concurrent writers
MUST NOT silently share
the same writable workspace
```

If multiple writers must touch one workspace, explicit coordination/serialization MUST make the ownership transition safe and attributable.

Conversational discipline is not sufficient isolation.

## 4. Attribution

Workspace SHOULD be attributable to:

```text
workspace_id
repository_ref
repository_change_unit_id
engineering_change_id
task_id
branch_ref
assigned Role reference
assigned Agent Run reference
lifecycle state
```

Where execution Context attribution is required, Workspace MAY reference the specific upstream:

```text
context_bundle_id
```

supplied to the assigned Role / Agent Run.

UPOS-005 v1.0 defines Context View as a bounded projection but does not introduce a separate global `context_view_id`. Module 06 therefore MUST NOT manufacture one.

Workspace attribution does not define or copy Context isolation/View semantics.

## 5. Lifecycle

```text
ALLOCATED
→ ACTIVE
→ READ_ONLY
→ RELEASED
```

Alternate terminal:

```text
ALLOCATED / ACTIVE / READ_ONLY
→ ABANDONED
```

Semantics:

- `ALLOCATED`: isolated environment reserved but not yet mutating.
- `ACTIVE`: currently writable under declared ownership.
- `READ_ONLY`: retained for inspection/provenance; mutation prohibited.
- `RELEASED`: no longer allocated for active work; retained references remain.
- `ABANDONED`: work stopped without successful integration; provenance retained.

Workspace lifecycle is distinct from Workflow, Agent Run, RCU, and Integration Request lifecycles.

## 6. Ownership transfer

Writable ownership transfer MUST be explicit.

Before transfer:

- current mutation stops;
- current repository state is attributable;
- new owner/Agent Run is declared;
- contamination risk is checked.

## 7. Contamination checks

Workspace validation SHOULD detect:

- unrelated untracked/staged/modified files;
- wrong RCU/Task changes;
- unexpected base/reference changes;
- branch mismatch;
- generated-artifact drift;
- residual state from another writer.

## 8. Completion/abandonment

Workspace cleanup MUST NOT silently delete provenance required to reconstruct commits, Integration Requests, or unresolved change state.

===== END VIRTUAL FILE: REPOSITORY_WORKSPACE_AND_ISOLATION.md =====


---

## VIRTUAL FILE 6/42 — `BRANCH_GOVERNANCE.md`

**Virtual path:** `BRANCH_GOVERNANCE.md`  
**Content checksum:** `1066be3e21fe`

===== BEGIN VIRTUAL FILE: BRANCH_GOVERNANCE.md =====

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

===== END VIRTUAL FILE: BRANCH_GOVERNANCE.md =====


---

## VIRTUAL FILE 7/42 — `ATOMIC_COMMIT_STANDARD.md`

**Virtual path:** `ATOMIC_COMMIT_STANDARD.md`  
**Content checksum:** `4ba715183587`

===== BEGIN VIRTUAL FILE: ATOMIC_COMMIT_STANDARD.md =====

# Atomic Commit Standard

**ID:** UPOS-06-COM-001  
**Type:** COMMIT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SKL-CREATE-ATOMIC-COMMIT


## 1. Definition

```text
COMMIT
= smallest coherent logical repository change
  that is understandable, reviewable, attributable,
  and revertable as a semantic unit where practical
```

Atomic means one coherent engineering intent.

It does NOT mean:

```text
one edited line
one tool action
one Agent turn
one file
```

## 2. Core invariants

A governed Commit SHOULD:

- have one logical purpose;
- exclude unrelated cleanup;
- preserve approved/routed scope;
- be understandable independently;
- be reviewable;
- be attributable;
- be revertable where practical;
- keep the repository coherent where practical;
- separate mechanical and semantic changes where safely possible;
- avoid unnecessary generated/noise changes.

```text
COMMIT SIZE != COMMIT QUALITY
```

No universal LOC threshold exists.

## 3. Small coherent commits

Prefer small coherent commits because they improve reviewability, blame, revert, provenance, and risk reasoning.

Reject the anti-pattern:

```text
commit after every action
```

Use semantic checkpoints:

```text
one coherent logical change
→ self-check
→ atomic commit
```

## 4. Unrelated cleanup

```text
No opportunistic unrelated cleanup inside a governed change.
```

Discovered unrelated improvement becomes a separate Task/Engineering Change unless required to safely complete current scope.

## 5. Mechanical vs semantic changes

Where practical separate:

```text
mechanical refactor / rename / formatting
```

from:

```text
behavioral or semantic change
```

Do not force separation if it creates unsafe or invalid intermediate states.

## 6. Regression protection

Regression protection SHOULD be created before or with a bug fix where practical.

Valid project-policy forms include:

```text
test + fix in one atomic green commit
```

or, when history policy permits:

```text
failing-test commit
→ fix commit
```

Module 06 does not require universally red intermediate history.

Quality sufficiency remains UPOS-007.

## 7. Review-fix commits

Do not create one commit per review comment.

Group corrections by coherent engineering intent.

## 8. Commit identity

Use:

```text
commit_ref
```

as the universal reference to the VCS-native immutable commit identity.

Do not invent a redundant universal commit ID.

## 9. Message semantics

A commit message SHOULD communicate:

- intent;
- affected scope where useful;
- reason/context where useful.

Universal Module 06 does not force a string syntax or commit taxonomy.

Project-specific syntax belongs to UPOS-011.

## 10. History integrity

If a commit set reviewed/checked earlier is rewritten, old associations remain attributable to the old artifact identity.

They MUST NOT silently attach to new commit identities.

===== END VIRTUAL FILE: ATOMIC_COMMIT_STANDARD.md =====


---

## VIRTUAL FILE 8/42 — `COMMIT_PROVENANCE_STANDARD.md`

**Virtual path:** `COMMIT_PROVENANCE_STANDARD.md`  
**Content checksum:** `02f3a25fce8a`

===== BEGIN VIRTUAL FILE: COMMIT_PROVENANCE_STANDARD.md =====

# Commit Provenance Standard

**ID:** UPOS-06-CPR-001  
**Type:** PROVENANCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Goal

A governed Commit should be reconstructible as part of a specific engineering intention without storing private chain-of-thought.

## 2. Provenance fields

Where available/relevant, preserve or reference:

```text
commit_ref
repository_change_unit_id
engineering_change_id

task_id
routing_decision_id
workflow_instance_id
stage_id

Role reference
Agent Run reference
Skill Invocation reference

context_bundle_id reference(s)

parent/base reference
commit purpose
affected scope
related check_ref values
Integration Request reference
```

## 3. Context boundary

When Context materially informed the commit, provenance SHOULD reference the exact upstream `context_bundle_id` value(s) actually consumed.

A single Commit MAY have multiple Context Bundle references when it combines work from multiple governed execution slices, provided the Commit remains one coherent logical intent.

Module 06 does not copy the Context Manifest. Provenance continues through:

```text
commit_ref
→ context_bundle_id
→ context_request_id
→ Context Manifest / source refs
```

where Context-owned fields and validity remain UPOS-005 semantics.

Module 06 MUST NOT define:

- Context validity/freshness states;
- Context View semantics;
- Context isolation;
- retrieval/budget/memory semantics.


## 4. No hidden reasoning

Commit provenance MUST NOT require private chain-of-thought.

Store concise intent, decision refs, artifacts, evidence references, and attributable execution identities.

## 5. Rewrite preservation

If commit identity changes through history rewrite:

- previous `commit_ref` remains historical provenance;
- new `commit_ref` is associated with the rewrite/replacement operation;
- review/check references continue to identify the artifact they actually covered.

## 6. Squash preservation

When policy transforms a commit set into one integrated revision, provenance MUST retain discoverable links from resulting revision back to:

```text
Integration Request
original commit set
Task
Engineering Change
Repository Change Unit
```

===== END VIRTUAL FILE: COMMIT_PROVENANCE_STANDARD.md =====


---

## VIRTUAL FILE 9/42 — `INTEGRATION_REQUEST_STANDARD.md`

**Virtual path:** `INTEGRATION_REQUEST_STANDARD.md`  
**Content checksum:** `ba44740a906e`

===== BEGIN VIRTUAL FILE: INTEGRATION_REQUEST_STANDARD.md =====

# Integration Request Standard

**ID:** UPOS-06-IRS-001  
**Type:** INTEGRATION REQUEST CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Definition

```text
INTEGRATION REQUEST
= provider-neutral coherent repository change container
  for review, checks, approvals, and integration references
```

It may contain multiple related atomic commits.

Provider-specific review-container names/APIs belong to UPOS-011.

## 2. Commit vs Integration Request

```text
Commit
= one coherent logical engineering change unit

Integration Request
= one coherent deliverable/intention
  that may contain multiple related Commits
```

No universal rule requires one Integration Request = one Commit.

One Integration Request MUST NOT mix unrelated feature/fix/refactor/cleanup/dependency work without one justified common intention.

## 3. Identity/reference

Use:

```text
integration_request_ref
```

as the universal reference.

Do not manufacture a duplicate Module-06 identifier unless the underlying provider/runtime cannot supply a stable reference.

## 4. Contract

A governed Integration Request SHOULD declare/reference:

```text
integration_request_ref
repository_change_unit_id
engineering_change_id

task_id
routing_decision_id
workflow_instance_id
stage_id

purpose
scope
non_scope

repository_ref
base_revision_ref
head_revision_ref
change_branch_ref
target/integration reference

commit_set

Change Class reference
Concern/Profile references
Implementation Plan reference where applicable

implementation Context Bundle ID reference(s) (`context_bundle_id`)
review Context Bundle ID reference(s) (`context_bundle_id`) when review has occurred

check_ref values

review_result_ref
qa_result_ref
security_ref
documentation_ref

rollback/revert considerations
known limitations

dependency/order constraints
superseded_integration_request_ref
```

Quality/Security semantics remain external.

## 5. Cohesion / size

One Integration Request = one reviewable intention.

Raw LOC is not the primary validity metric.

A large coherent migration or generated change may be valid; unrelated combined intentions are not.

If too broad:

```text
identify independent intentions
→ split safely
→ preserve dependency order
```

Do not split if doing so creates an unsafe/invalid intermediate state.

## 6. Review artifact

Module 06 provides a reconstructible review artifact consisting of at least:

```text
repository_ref
base_revision_ref
head_revision_ref
commit_set
diff/change reference where available
engineering provenance
```

This artifact is distinct from Reviewer Context.

UPOS-005 supplies Reviewer Context through a Reviewer-scoped Context Request / Context Bundle.

There is no Module-06 `context_view_id`.

Review execution provenance SHOULD reference the exact Reviewer `context_bundle_id` actually consumed where available.

Critical invariant consumed from UPOS-005:

```text
producer context
!= reviewer authoritative context
```

The producer's implementation Context Bundle MUST NOT automatically become the Reviewer Context Bundle.

Module 06 does not define Reviewer Context contents, independence policy, freshness, or validity; it records the upstream Bundle reference and exact repository artifact reviewed.


## 7. Context reuse / artifact-change interface

If an Integration Request's head/base revision or relevant repository artifact materially changes and a prior Context Bundle is intended for reuse:

```text
repository artifact changes
→ UPOS-006 reports exact artifact change
→ UPOS-005 revalidates the prior Context Bundle
→ reassembly, when required, produces a new context_bundle_id
```

The prior sealed/consumed Bundle remains immutable historical provenance.

Module 06 MUST NOT label the Bundle `STALE` or `INVALIDATED` itself.

## 8. Evidence container boundary

An Integration Request may contain references to:

```text
tests_ref
review_ref
qa_ref
security_ref
docs_ref
```

It does not define evidence sufficiency or verdict semantics.

## 9. ready_for_review

`ready_for_review` MAY be a producer-intent flag.

It means:

> producer asserts the repository artifact is ready to enter review.

It does NOT mean Quality approval.

## 10. Stacked/dependent requests

Dependent Integration Requests are allowed when safe decomposition exists.

Each MUST explicitly declare dependency/order relationships.

## 11. Documentation in same request

Documentation changes may share an Integration Request when they are part of the same coherent intention.

Canonical documentation ownership remains UPOS-01.

===== END VIRTUAL FILE: INTEGRATION_REQUEST_STANDARD.md =====


---

## VIRTUAL FILE 10/42 — `INTEGRATION_REQUEST_LIFECYCLE.md`

**Virtual path:** `INTEGRATION_REQUEST_LIFECYCLE.md`  
**Content checksum:** `40a71e25b825`

===== BEGIN VIRTUAL FILE: INTEGRATION_REQUEST_LIFECYCLE.md =====

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

===== END VIRTUAL FILE: INTEGRATION_REQUEST_LIFECYCLE.md =====


---

## VIRTUAL FILE 11/42 — `ENGINEERING_CHECK_INTEGRATION.md`

**Virtual path:** `ENGINEERING_CHECK_INTEGRATION.md`  
**Content checksum:** `f40b882ac746`

===== BEGIN VIRTUAL FILE: ENGINEERING_CHECK_INTEGRATION.md =====

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

===== END VIRTUAL FILE: ENGINEERING_CHECK_INTEGRATION.md =====


---

## VIRTUAL FILE 12/42 — `CONCURRENCY_COLLISION_AND_CONFLICT.md`

**Virtual path:** `CONCURRENCY_COLLISION_AND_CONFLICT.md`  
**Content checksum:** `a7caae132a46`

===== BEGIN VIRTUAL FILE: CONCURRENCY_COLLISION_AND_CONFLICT.md =====

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

===== END VIRTUAL FILE: CONCURRENCY_COLLISION_AND_CONFLICT.md =====


---

## VIRTUAL FILE 13/42 — `MULTI_REPOSITORY_CHANGE_MODEL.md`

**Virtual path:** `MULTI_REPOSITORY_CHANGE_MODEL.md`  
**Content checksum:** `136b640234de`

===== BEGIN VIRTUAL FILE: MULTI_REPOSITORY_CHANGE_MODEL.md =====

# Multi-Repository Change Model

**ID:** UPOS-06-MRC-001  
**Type:** MULTI-REPOSITORY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

```text
one Task
→ one Engineering Change
→ one or more Repository Change Units
```

One Task is not assumed to equal one repository.

## 2. Unit independence

Each RCU may have:

```text
separate repository_ref
separate workspace_id
separate branch_ref
separate commit history
separate integration_request_ref
separate merge_operation_id
separate integrated_revision_ref
```

They share the parent:

```text
engineering_change_id
task_id
workflow_instance_id
```

## 3. Engineering dependency constraints

Module 06 may declare relationships such as:

```text
RCU-B depends_on RCU-A integrated revision
RCU-C consumes package/revision produced by RCU-A
RCU-D cannot integrate before migration artifact RCU-B
```

These are repository integration constraints.

Overall Workflow ordering remains UPOS-004.

## 4. Merge/integration order

Integration order MUST be explicit when repository artifacts depend on each other.

Module 06 does not own deployment/release sequencing.

## 5. Partial integration

An Engineering Change may be mechanically `PARTIALLY_INTEGRATED` when some required RCUs are integrated and others are not.

This state MUST NOT be interpreted as Workflow completion or release success.

## 6. Cross-repository provenance

Future reconstruction should answer:

- which RCUs implement one Engineering Change;
- which revisions were integrated in each repository;
- their dependency/order relationships;
- whether a later revert/backout affected one or many RCUs.

===== END VIRTUAL FILE: MULTI_REPOSITORY_CHANGE_MODEL.md =====


---

## VIRTUAL FILE 14/42 — `MERGE_GOVERNANCE.md`

**Virtual path:** `MERGE_GOVERNANCE.md`  
**Content checksum:** `8ba6be65c204`

===== BEGIN VIRTUAL FILE: MERGE_GOVERNANCE.md =====

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

===== END VIRTUAL FILE: MERGE_GOVERNANCE.md =====


---

## VIRTUAL FILE 15/42 — `REVERT_BACKOUT_AND_RECOVERY.md`

**Virtual path:** `REVERT_BACKOUT_AND_RECOVERY.md`  
**Content checksum:** `943f317227b4`

===== BEGIN VIRTUAL FILE: REVERT_BACKOUT_AND_RECOVERY.md =====

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

===== END VIRTUAL FILE: REVERT_BACKOUT_AND_RECOVERY.md =====


---

## VIRTUAL FILE 16/42 — `SPECIAL_REPOSITORY_ARTIFACTS.md`

**Virtual path:** `SPECIAL_REPOSITORY_ARTIFACTS.md`  
**Content checksum:** `3cb7fb299485`

===== BEGIN VIRTUAL FILE: SPECIAL_REPOSITORY_ARTIFACTS.md =====

# Special Repository Artifacts

**ID:** UPOS-06-SRA-001  
**Type:** SPECIAL ARTIFACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Generated artifacts

Generated files are first-class repository artifacts when required by their source change.

Governance SHOULD ensure:

- source/generator relationship is attributable;
- generated output is reproducible where practical;
- unrelated generated noise is excluded;
- manual edits to generated output are prohibited unless the project explicitly permits them;
- generator/source mismatch is surfaced;
- generated artifacts are included in the same coherent Commit/Integration Request when they are required for the source change.

Generator commands/provider bindings belong to UPOS-011.

Quality verification belongs to UPOS-007.

## 2. Lockfiles / dependency manifests

Dependency-related lockfiles/manifests are first-class artifacts when required for a dependency change.

Avoid unrelated dependency churn.

Dependency classification/routing remains UPOS-004.

## 3. Database migration files

UPOS-006 governs repository mechanics:

- ordering references;
- file/sequence collision detection;
- change attribution;
- commit/branch/Integration Request handling.

Database/data migration safety semantics remain external to Module 06.

## 4. Documentation artifacts in engineering change

Documentation MAY live in the same Integration Request when it is part of the same coherent intention.

Canonical documentation truth/ownership remains UPOS-01.

Documentation Guardian authority remains UPOS-002.

Quality semantics remain UPOS-007.

===== END VIRTUAL FILE: SPECIAL_REPOSITORY_ARTIFACTS.md =====


---

## VIRTUAL FILE 17/42 — `ENGINEERING_PROVENANCE_MODEL.md`

**Virtual path:** `ENGINEERING_PROVENANCE_MODEL.md`  
**Content checksum:** `1b9186953e0b`

===== BEGIN VIRTUAL FILE: ENGINEERING_PROVENANCE_MODEL.md =====

# Engineering Provenance Model

**ID:** UPOS-06-PRV-001  
**Type:** PROVENANCE MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-008 future observability interface


## 1. Purpose

Engineering provenance makes repository work reconstructible without relying on chat history or private reasoning.

## 2. Canonical relationship chain

```text
Task
↓
Routing Decision
↓
Workflow Instance
↓
Stage
↓
Agent Run
↓
Skill Invocation
↓
Context Request (`context_request_id`)
↓
Context Bundle (`context_bundle_id`)
↓
Engineering Change
↓
Repository Change Unit
↓
Repository Workspace
↓
Change Branch
↓
Commit(s)
↓
Integration Request
↓
Review / QA / Security result references
↓
Merge Operation
↓
Integrated Revision
↓
possible Revert / Backout
```

This is a semantic relationship model, not an event/trace schema.

## 3. Stable identity/reference set

Owned semantic IDs:

```text
engineering_change_id
repository_change_unit_id
workspace_id
merge_operation_id
```

Upstream reused IDs:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

Native/external refs:

```text
Agent Run reference
Skill Invocation reference
repository_ref
branch_ref
commit_ref
integration_request_ref
revision_ref
check_ref
tag_ref / release_revision_ref where used
review/qa/security refs
context_request_id
context_bundle_id
```

## 4. Provenance != Observability

```text
artifact relationships / stable refs
→ UPOS-006

event_id / trace_id / span_id / metrics / dashboard
→ UPOS-008
```

## 5. Required reconstructibility

A future control plane SHOULD be able to answer from these relationships:

- Which Task caused this commit?
- Which Agent Run wrote it?
- Which Workflow Stage was active?
- Which `context_bundle_id` informed it?
- Which workspace/branch contained it?
- Why are these commits in one Integration Request?
- Which checks ran against exactly which revision?
- Did the artifact change after review/check?
- Who/which actor executed the Merge Operation?
- What integrated revision resulted?
- Was it later reverted/backed out?
- Which concurrent unit/Agent Run was involved in a collision?

## 6. Privacy of reasoning

Provenance MUST NOT store hidden chain-of-thought as a requirement.

Store attributable artifacts, references, concise rationale, decisions, evidence refs, and outcomes.

## 7. Context boundary

UPOS-006 consumes stable upstream Module-05 identities:

```text
context_request_id
context_bundle_id
```

for artifact provenance where applicable.

An Engineering Change may have multiple execution slices; therefore the provenance graph is many-to-one and MAY contain multiple Request/Bundle pairs.

Module 06 does not create `context_view_id`, does not duplicate Context Manifest/source provenance, and does not decide Context validity/freshness.

When a repository artifact changes, Module 06 exposes the exact artifact/revision change. UPOS-005 owns revalidation/reassembly and produces a new `context_bundle_id` when a new Bundle is assembled.

===== END VIRTUAL FILE: ENGINEERING_PROVENANCE_MODEL.md =====


---

## VIRTUAL FILE 18/42 — `ENGINEERING_FAILURE_MODEL.md`

**Virtual path:** `ENGINEERING_FAILURE_MODEL.md`  
**Content checksum:** `6f026a1e57f2`

===== BEGIN VIRTUAL FILE: ENGINEERING_FAILURE_MODEL.md =====

# Engineering Failure Model

**ID:** UPOS-06-EFM-001  
**Type:** ENGINEERING FAILURE TAXONOMY  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 failure/reclassification interfaces


## 1. Purpose

Module 06 classifies repository-engineering failure conditions and reports engineering constraints/signals.

It does NOT own Workflow retry/rework/recovery sequencing.

## 2. Taxonomy

| Failure | Engineering meaning | Detectability | Module-06 response / Workflow signal |
|---|---|---|---|
| `WORKSPACE_CONTAMINATION` | writable workspace contains state outside assigned RCU/owner scope | workspace/diff inspection | block mutation; isolate/clean/transfer; signal Workflow |
| `WRONG_BASE` | RCU/branch/workspace began from or points to unintended base | revision comparison | block integration; correct base/update; signal if scope/risk changes |
| `BRANCH_SCOPE_VIOLATION` | branch contains unrelated Task/RCU work | provenance/diff analysis | split/clean or block; emit scope signal |
| `UNRELATED_CHANGE_DETECTED` | Commit/IR contains opportunistic unrelated change | diff/provenance analysis | remove/split; emit scope expansion signal |
| `COMMIT_NON_ATOMIC` | Commit combines separable unrelated logical intents | commit/diff analysis | split/reconstruct where practical; block readiness mechanics if policy requires |
| `UNRESOLVED_VCS_CONFLICT` | version-control conflict unresolved | VCS state | `CONFLICT_PRESENT`; block merge mechanics |
| `CONCURRENT_WRITE_COLLISION` | independent writers mutate conflicting/shared state unsafely | workspace ownership/collision analysis | serialize/isolate/coordinate; signal UPOS-004 |
| `STALE_BASE` | base materially advanced beyond engineering policy | base/head comparison | `REBASE_REQUIRED` or coordination required |
| `CHECK_ARTIFACT_MISMATCH` | check result points to older/different artifact than current candidate | artifact ref comparison | mark stale association; expose to UPOS-007 |
| `REVIEW_ARTIFACT_CHANGED` | reviewed base/head/commit set changed | artifact ref comparison | expose artifact-change signal; do not preserve validity claim |
| `INTEGRATION_REQUEST_SCOPE_DRIFT` | IR purpose/scope no longer matches contained changes | scope/provenance analysis | block/split/update route as governed |
| `MERGE_CONFLICT` | integration operation cannot apply cleanly | VCS/provider mechanics | `MECHANICALLY_BLOCKED`; return conflict signal |
| `PROVENANCE_INCOMPLETE` | required artifact relationship cannot be reconstructed | provenance validation | block high-value integration mechanic per policy; request missing refs |
| `HISTORY_REWRITE_DETECTED` | commit/head identity changed by rebase/amend/force update | revision/ref comparison | preserve old refs; expose stale review/check associations |
| `GENERATED_ARTIFACT_MISMATCH` | generated artifact/source/generator relation is inconsistent | artifact consistency check | block or flag; invoke project generator/quality interfaces |

## 3. Workflow boundary

For failures requiring:

```text
retry
rework
replan
reclassification
rerouting
escalation
cancellation
```

Module 06 emits the condition; UPOS-004 owns orchestration.

## 4. Quality/Security boundary

Module 06 MUST NOT reinterpret external findings/vetoes.

It only binds their references to repository artifacts and exposes artifact changes.

## 5. Non-convergence

Repeated engineering conflicts or scope drift may be reported as evidence to Workflow/Learning systems.

Module 06 does not create its own infinite repair loop.

===== END VIRTUAL FILE: ENGINEERING_FAILURE_MODEL.md =====


---

## VIRTUAL FILE 19/42 — `ENGINEERING_LIFECYCLE_AND_VERSIONING.md`

**Virtual path:** `ENGINEERING_LIFECYCLE_AND_VERSIONING.md`  
**Content checksum:** `f6368fc342ef`

===== BEGIN VIRTUAL FILE: ENGINEERING_LIFECYCLE_AND_VERSIONING.md =====

# Engineering Lifecycle and Versioning

**ID:** UPOS-06-LCV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Distinct lifecycles

Module 06 maintains only repository-mechanical lifecycles.

They MUST remain distinct from Task, Workflow, Agent Run, Quality, release, deployment, and product lifecycles.

## 2. Engineering Change lifecycle

```text
ACTIVE
→ PARTIALLY_INTEGRATED   # only for multi-RCU changes where some required units are integrated
→ INTEGRATED

ACTIVE / PARTIALLY_INTEGRATED
→ ABANDONED

ACTIVE / PARTIALLY_INTEGRATED
→ SUPERSEDED
```

`INTEGRATED` means required repository integration contract is satisfied, not Workflow/Quality/release completion.

## 3. Repository Change Unit lifecycle

Defined in `REPOSITORY_CHANGE_UNIT_STANDARD.md`:

```text
PREPARED
ACTIVE
INTEGRATION_REQUEST_OPEN
INTEGRATED
ABANDONED
SUPERSEDED
```

## 4. Workspace lifecycle

```text
ALLOCATED
ACTIVE
READ_ONLY
RELEASED
ABANDONED
```

## 5. Integration Request lifecycle

```text
DRAFT
OPEN
CLOSED
MERGED
SUPERSEDED
```

No Quality verdict states are used.

## 6. Engineering Governance document versioning

Material changes to:

- entity identity semantics;
- atomic commit invariants;
- workspace isolation;
- Integration Request contract/lifecycle;
- collision/failure taxonomy semantics;
- merge/revert mechanics;
- provenance requirements;
- cross-module ownership boundaries

require version review.

## 7. Module status

UPOS-006 v1.0 completed its narrow reconciliation against FROZEN UPOS-005 Context & Memory v1.0.

```text
Status: ACTIVE
Canonical baseline: FROZEN v1.0
UPOS-005 interface reconciliation: COMPLETE
```

Future semantic changes require normal governed version review under UPOS-01.


## 8. Supersession

Future versions MUST preserve discoverability of superseded Module-06 standards and artifact semantics according to UPOS-01.

===== END VIRTUAL FILE: ENGINEERING_LIFECYCLE_AND_VERSIONING.md =====


---

## VIRTUAL FILE 20/42 — `CROSS_MODULE_INTERFACES.md`

**Virtual path:** `CROSS_MODULE_INTERFACES.md`  
**Content checksum:** `5c12b493d551`

===== BEGIN VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

# Module 06 Cross-Module Interfaces

**ID:** UPOS-06-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth / Knowledge

**UPOS-006 provides:** repository implementation/provenance evidence, docs artifact refs.  
**Consumes:** canonical owner/source resolution, decision records, normative conflict behavior, knowledge provenance.  
**MUST NOT redefine:** canonical truth, documentation ownership, promotion/supersession.

## UPOS-002 — Agent Organization

**Provides:** workspace/branch/commit/IR/merge mechanics usable by organizational Roles.  
**Consumes:** Role, Agent Run, authority, delegation, SoD, Merge Controller authority, Human Governance.  
**MUST NOT redefine:** who is allowed to implement/review/merge.

Required invariants:

```text
Implementer != Final Reviewer
high-risk:
Implementer != Reviewer != Merge Controller
```

## UPOS-003 — Skills System

**Provides:** engineering semantics consumed by `INTERFACE_SKILL` contracts such as `SKL-CREATE-ATOMIC-COMMIT`, `SKL-REVIEW-DIFF`, `SKL-ASSESS-MERGE-READINESS`.  
**Consumes:** Skill IDs/contracts/invocation references.  
**MUST NOT redefine:** Skill procedures.

## UPOS-004 — Workflow Engine

**Provides:** engineering constraints/signals: collision, stale base, scope drift, artifact change, mechanical integration state.  
**Consumes:** `task_id`, `routing_decision_id`, `workflow_instance_id`, `stage_id`, Change Class/Profiles, orchestration decisions.  
**MUST NOT redefine:** Task/Workflow state, routing, stage order, retry/rework/recovery, reclassification/rerouting.

### Rework mechanics

When UPOS-004 routes work back for rework, UPOS-006 supports:

```text
additional commits
branch/head update
Integration Request update
artifact identity change signal
new check associations
```

UPOS-006 does NOT create or bound the rework loop. Rework sequencing/bounds remain UPOS-004; finding semantics remain UPOS-007.

For rework/re-review, UPOS-005 requires the prior Context Bundle to be revalidated against the new finding and changed artifact. If reassembly is required, a new `context_bundle_id` is produced and the prior immutable Bundle remains provenance. Module 06 records the Bundle reference(s) but does not own Context validity.

### Hotfix mechanics

Hotfix repository mechanics may be expedited only where external policy permits.

```text
expedited != ungoverned
```

Attribution, scope, commit provenance, Integration Request/exception provenance, and Merge Operation provenance remain required. Workflow controls compressed stages; permissions/security remain external.

## UPOS-005 — Context & Memory

**UPOS-006 provides:**

- repository/diff/commit/Integration Request/revision references that may be used as Context candidates or revalidation inputs;
- exact artifact-change signals such as changed head/base/review artifact;
- engineering Context requirements at the interface level without defining retrieval semantics.

**UPOS-006 consumes:**

```text
context_request_id
context_bundle_id
Context Requirement / Context Request contract
Context Bundle / Context Manifest provenance
Role-/Run-/Reviewer-specific Context View semantics
Context validity / freshness / invalidation / reassembly results
Reviewer independence semantics
```

UPOS-005 v1.0 defines Context View as a bounded projection; it does not define a separate stable `context_view_id`. Module 06 MUST NOT invent one.

For repository provenance:

```text
artifact / commit / Integration Request
→ context_bundle_id
→ context_request_id
→ Context Manifest / source refs / memory refs
```

The authoritative Context provenance after `context_bundle_id` remains UPOS-005-owned.

For artifact change and rework:

```text
UPOS-006 exposes changed artifact/revision
→ UPOS-005 revalidates prior Bundle
→ if required: new context_bundle_id
→ prior consumed Bundle remains immutable provenance
```

**MUST NOT redefine:** Context identity semantics beyond reusing the frozen IDs, Context validity/freshness, isolation/View rules, retrieval, source resolution, budget, memory, Reviewer/Implementer Context contents, or reassembly behavior.

**Reconciled against:** FROZEN UPOS-005 Context & Memory v1.0  
**Source SHA-256:** `186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528`


## UPOS-007 — Quality System

**UPOS-006 provides:**

```text
stable review artifact
base/head revisions
commit set
diff/change refs
engineering check refs
artifact-changed/stale signals
mechanical mergeability
provenance
```

**Consumes:** Review Result, QA Result, Quality Gate Result, evidence sufficiency/readiness semantics.  
**MUST NOT redefine:** finding severity, PASS/FAIL, evidence sufficiency, DoD Quality meaning.

## UPOS-008 — Observability

**Provides stable entities/refs:**

```text
engineering_change_id
repository_change_unit_id
workspace_id
branch_ref
commit_ref
integration_request_ref
check_ref
merge_operation_id
integrated_revision_ref
```

**MUST NOT define:** `event_id`, `trace_id`, `span_id`, metrics, retention, dashboard.

## UPOS-009 — Learning

Engineering failures may become learning evidence:

- non-atomic commits;
- merge conflicts;
- workspace collisions;
- review-artifact invalidation;
- scope drift;
- revert/backout patterns.

UPOS-006 reports evidence/signals. It does not promote learning or mutate policy.

## UPOS-010 — Security & Permissions

Module 06 may declare capability requirements:

```text
repository-read
repository-write
branch-create
commit
push
integration-request-create
integration-request-update
merge
history-rewrite
protected-target-write
tag-create
```

UPOS-010 owns grant/deny, protected actions, approval, secrets, production authority.

## UPOS-011 — Project Adapter

UPOS-006 provides abstract requirements.

UPOS-011 resolves:

- repository provider and location;
- integration target;
- branch naming;
- workspace realization;
- VCS commands;
- review-container/provider API;
- CI provider and actual commands;
- merge strategy configuration;
- project-specific stricter engineering policy.

## Cross-cutting schemas/runtime

Future machine-readable forms may encode:

```text
EngineeringChange
RepositoryChangeUnit
Workspace
CommitProvenance
IntegrationRequest
EngineeringCheckReference
MergeOperation
```

Schemas MUST trace to normative Module-06 Markdown and MUST NOT become an independent semantic source.

===== END VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====


---

## VIRTUAL FILE 21/42 — `MODULE_06_DEFINITION_OF_DONE.md`

**Virtual path:** `MODULE_06_DEFINITION_OF_DONE.md`  
**Content checksum:** `9b71a294918f`

===== BEGIN VIRTUAL FILE: MODULE_06_DEFINITION_OF_DONE.md =====

# Module 06 Definition of Done

**ID:** UPOS-06-DOD-001  
**Type:** DEFINITION OF DONE / FREEZE GATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Final v1.0 Definition of Done

The following are satisfied:

```text
[x] Engineering Governance ownership boundary clear

[x] Engineering Change formally defined
[x] Repository Change Unit formally defined
[x] Workspace isolation model exists
[x] concurrent writers cannot silently share writable workspace
[x] branch governance model exists
[x] no GitFlow-specific universal assumption

[x] Atomic Commit Standard exists
[x] atomic != one action / one file / fixed LOC
[x] unrelated cleanup prohibited
[x] mechanical vs semantic change separation addressed
[x] regression-test/fix policy avoids mandatory red-history assumption
[x] Commit provenance exists

[x] provider-neutral Integration Request exists
[x] Commit vs Integration Request distinct
[x] Integration Request contract exists
[x] Integration Request lifecycle does not steal Quality verdict states

[x] CI/check integration exists
[x] check-artifact staleness exists

[x] concurrency/collision model exists
[x] semantic collision is not reduced to file overlap
[x] multi-repository changes supported
[x] base revision semantics exists
[x] artifact staleness exists
[x] history rewrite/rebase implications explicit

[x] merge mechanics separate from authority/readiness/permission
[x] mechanical mergeability != approved-to-merge
[x] Merge Operation contract exists
[x] merge strategy remains project configurable

[x] revert/backout semantics exist
[x] deployment/data rollback remain external

[x] engineering provenance model exists
[x] engineering failure taxonomy exists

[x] no hard-coded provider/project paths
[x] Quality semantics remain UPOS-007
[x] permissions remain UPOS-010
[x] project bindings remain UPOS-011
[x] telemetry remains UPOS-008
[x] Workflow orchestration remains UPOS-004

[x] context_request_id / context_bundle_id reused from frozen UPOS-005
[x] no context_view_id invented
[x] engineering provenance → Context interface reconciled
[x] Implementer/Workspace Context attribution reconciled
[x] Reviewer Context independence interface reconciled
[x] rework Context interface reconciled
[x] Context invalidation vs engineering artifact change reconciled
[x] old consumed Bundle remains immutable when reassembly creates a new Bundle
[x] UPOS-005 reconciliation register has zero unresolved material issues

[x] final cross-module validation rerun
[x] all five canonical operational templates conform to their owning normative contracts
[x] active operational normative UPOS-005 pending markers = 0
[x] no known ownership leakage against frozen UPOS-005
[x] no unresolved internal/interface P0/P1 Module-06 gaps
[x] UNMAPPED MODULE-06 SOURCE REQUIREMENTS = 0
```

## 2. Final completion status

```text
UPOS-006 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-005 INTERFACE RECONCILIATION:
COMPLETE

UPOS-006 FREEZE STATUS:
FROZEN v1.0
```

## 3. Freeze assertion

UPOS-006 v1.0 may be used as the canonical Engineering Governance baseline.

Future semantic changes require a new governed version; they MUST NOT silently mutate this frozen baseline.

===== END VIRTUAL FILE: MODULE_06_DEFINITION_OF_DONE.md =====


---

## VIRTUAL FILE 22/42 — `MODULE_06_TRACEABILITY.md`

**Virtual path:** `MODULE_06_TRACEABILITY.md`  
**Content checksum:** `d80432297bff`

===== BEGIN VIRTUAL FILE: MODULE_06_TRACEABILITY.md =====

# Module 06 Traceability

**ID:** UPOS-06-TRC-001  
**Type:** TRACEABILITY / NORMATIVE COVERAGE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analysis/SOURCE_SECTION_DISPOSITION.md


**Frozen master SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`  
**Module-06 directive SHA-256:** `eca639c6b344ad05b3159070b302d4ec612a492f3485bf637bdccab5a0a2dc2c`

**FROZEN UPOS-005 v1.0 SHA-256:** `186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528`

## 1. Rule

Traceability covers:

```text
frozen master design source
+
Module-06 implementation directive
+
later UPOS-005 reconciliation requirements
+
final conformance cleanup requirements
```

Final coverage maps every Module-06 directive section, every material frozen-master engineering requirement, all frozen UPOS-005 reconciliation requirements, and the final conformance cleanup requirements.

## 2. Requirement map

| Requirement | Source | Source topic | Disposition | Extracted requirement | Canonical target |
|---|---|---|---|---|---|
| `ENG-DIR-000` | Implementation directive §0 | SOURCE AUTHORITY | EXTRACTED_TO_MODULE_06 | Используй следующие источники. ## INPUT A — UPOS-01 Documentation System Используй: - `UNIVERSAL_PROJECT_DOCUMENTATION_SYSTEM_CHATGPT_SINGLE_FILE_v1.2.md` - `PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md` - `PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md` Это upstream governance. UPOS-006 потребляет: Но не… | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-001` | Implementation directive §1 | ЦЕЛЬ MODULE 06 | EXTRACTED_TO_MODULE_06 | Создать canonical ownership package: UPOS-006 должен отвечать: > Как U-POS безопасно и трассируемо превращает одобренную работу в реальные repository changes: изолирует рабочие пространства, управляет branches/change units, формирует маленькие atomic commits, связывает изменения с… | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-002` | Implementation directive §2 | FUNDAMENTAL MODEL | EXTRACTED_TO_MODULE_06 | Формализуй минимум следующие сущности: Do not use them interchangeably. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-003` | Implementation directive §3 | IMPORTANT TERMINOLOGY | EXTRACTED_TO_MODULE_06 | Do not make GitHub-specific `Pull Request` the universal ontology. Use a provider-neutral canonical concept such as: with mappings: You MAY use `PR/MR` conversationally in examples. Concrete provider mapping belongs UPOS-011. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-004` | Implementation directive §4 | MODULE 06 OWNS | EXTRACTED_TO_MODULE_06 | UPOS-006 is canonical owner for: --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-005` | Implementation directive §5 | MODULE 06 DOES NOT OWN | MIXED_EXTRACTED_AND_DEFERRED | Do not redefine: UPOS-006 may declare interfaces to those owners. It MUST NOT silently absorb them. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-006` | Implementation directive §6 | ENGINEERING CHANGE MODEL | EXTRACTED_TO_MODULE_06 | Define: as the engineering realization associated with already governed work. It MUST be attributable to upstream execution scope where applicable: and engineering participants/results. Do not create a competing Task. Recommended stable semantic identity to evaluate: If adopted, it must be… | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-DIR-007` | Implementation directive §7 | REPOSITORY CHANGE UNIT | EXTRACTED_TO_MODULE_06 | One Engineering Change MAY affect: Do not assume one Task = one repository. Formalize: with a stable identity candidate: It should represent one coherent repository-scoped realization. Example: UPOS-004 owns organizational sequencing. UPOS-006 owns engineering isolation/integration mechanics of… | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-DIR-008` | Implementation directive §8 | CHANGE PLAN BOUNDARY | EXTRACTED_TO_MODULE_06 | `SKL-CREATE-IMPLEMENTATION-PLAN` already exists. Do not create another competing planning system. Separate: UPOS-006 consumes an approved/relevant plan reference where required. It does not redefine Product/Architecture intent. --- | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-DIR-009` | Implementation directive §9 | REPOSITORY WORKSPACE | EXTRACTED_TO_MODULE_06 | Define a provider-neutral: as an isolated writable repository environment assigned to a bounded change unit/execution. Potential implementation: but concrete implementation belongs UPOS-011/runtime. UPOS-006 owns the isolation requirement. --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-010` | Implementation directive §10 | WORKSPACE ISOLATION INVARIANT | EXTRACTED_TO_MODULE_06 | Default invariant: unless explicit coordination/serialization rules make it safe. Especially for multiple Agents: when concurrent mutation occurs. Do not rely on conversational discipline. --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-011` | Implementation directive §11 | WORKSPACE ATTRIBUTION | EXTRACTED_TO_MODULE_06 | A Repository Workspace should be attributable to: Exact machine schema deferred. --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-012` | Implementation directive §12 | WORKSPACE LIFECYCLE | EXTRACTED_TO_MODULE_06 | Define a small semantic lifecycle. Candidate: or a better model. Do not create decorative states. Workspace lifecycle: --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-013` | Implementation directive §13 | BRANCH GOVERNANCE | EXTRACTED_TO_MODULE_06 | Define universal semantics for a bounded Change Branch. Do NOT hard-code: Those physical conventions belong Project Adapter. Instead define branch roles/relationships semantically. Examples: Avoid forcing GitFlow universally. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-014` | Implementation directive §14 | BRANCH INVARIANTS | EXTRACTED_TO_MODULE_06 | A Change Branch MUST be: Do not allow a shared branch to become a dumping ground for unrelated Tasks. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-015` | Implementation directive §15 | DIRECT-TO-INTEGRATION CHANGES | EXTRACTED_TO_MODULE_06 | Do not universally assume: because project/risk policies may permit exceptions. But direct integration branch mutation MUST be: and MUST NOT silently bypass required external Workflow/Quality/Security gates. Exact permission belongs UPOS-010/011. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-016` | Implementation directive §16 | ATOMIC COMMIT STANDARD | EXTRACTED_TO_MODULE_06 | This is a core Module-06 artifact. Define: Atomic does NOT mean: Atomic means: --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-017` | Implementation directive §17 | COMMIT QUALITY INVARIANTS | EXTRACTED_TO_MODULE_06 | A governed Commit SHOULD: Do not introduce arbitrary universal LOC limits. Explicit invariant: A 5-line commit may be bad. A 300-line generated migration may still be one coherent unit. --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-018` | Implementation directive §18 | SMALL COMMIT PRINCIPLE | EXTRACTED_TO_MODULE_06 | Preserve the design goal: But reject: The standard must favor semantic checkpoints. Example: Bad: Better: --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-019` | Implementation directive §19 | UNRELATED CLEANUP | EXTRACTED_TO_MODULE_06 | Explicit rule: If useful unrelated improvement is discovered: unless it is strictly required to safely complete the current scope. This improves: --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-020` | Implementation directive §20 | MECHANICAL VS SEMANTIC CHANGES | EXTRACTED_TO_MODULE_06 | Where practical separate: from: because mixed diffs reduce review quality. Do not force separation if it creates unsafe or invalid intermediate state. --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-021` | Implementation directive §21 | REGRESSION TEST + FIX | EXTRACTED_TO_MODULE_06 | Do not blindly require: because some projects require green history. Instead formalize: Possible valid forms: or, when policy permits: Exact policy may vary. Quality sufficiency remains UPOS-007. --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-022` | Implementation directive §22 | COMMIT PROVENANCE | EXTRACTED_TO_MODULE_06 | Each governed Commit should preserve/reference where available: Do not include private chain-of-thought. --- | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-DIR-023` | Implementation directive §23 | COMMIT IDENTITY | EXTRACTED_TO_MODULE_06 | Do not invent a replacement for the version-control system's immutable commit identity. Universal contract may use: Concrete SHA/object identifier is provider/VCS realization. If an additional U-POS semantic identifier is truly justified, document why. Prefer not to duplicate identity… | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-024` | Implementation directive §24 | COMMIT MESSAGE STANDARD | EXTRACTED_TO_MODULE_06 | Define required semantic information, not necessarily one universal string syntax. A commit message SHOULD convey: Do not universally force Conventional Commits unless source analysis proves it belongs in U-POS. Project-specific syntax belongs UPOS-011. --- | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-DIR-025` | Implementation directive §25 | HISTORY INTEGRITY | EXTRACTED_TO_MODULE_06 | Engineering history must remain auditable. Define rules around: Important principle: UPOS-006 emits the artifact-change condition. UPOS-007 decides quality/re-review semantics. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-026` | Implementation directive §26 | REVIEWED HISTORY REWRITE | EXTRACTED_TO_MODULE_06 | After an Integration Request has received external Review/QA evidence, history rewriting must not silently preserve stale evidence associations. Example: UPOS-006 must expose: It MUST NOT claim old review remains valid. Validity semantics remain UPOS-007. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-027` | Implementation directive §27 | INTEGRATION REQUEST | EXTRACTED_TO_MODULE_06 | Define provider-neutral: Purpose: Mapped externally to PR/MR/etc. It may contain multiple atomic commits. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-028` | Implementation directive §28 | COMMIT VS INTEGRATION REQUEST | EXTRACTED_TO_MODULE_06 | Explicit separation: Do not require: Do not permit: without justified common intent. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-029` | Implementation directive §29 | INTEGRATION REQUEST CONTRACT | EXTRACTED_TO_MODULE_06 | A governed Integration Request should declare/reference: Refine after source analysis. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-030` | Implementation directive §30 | PR AS EVIDENCE CONTAINER — BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | Integration Request may serve as a container of references to evidence. It MUST NOT define what evidence is sufficient. Separate: Thus Module 06 may require slots such as: but cannot decide their substantive PASS semantics. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-031` | Implementation directive §31 | INTEGRATION REQUEST LIFECYCLE | EXTRACTED_TO_MODULE_06 | Define repository-mechanical lifecycle only. Potential model: Refine if necessary. Do NOT encode Quality verdicts as lifecycle states. For example avoid making: Module-06-owned lifecycle states. Those are external results/references. --- | `INTEGRATION_REQUEST_LIFECYCLE.md` |
| `ENG-DIR-032` | Implementation directive §32 | READY FOR REVIEW | EXTRACTED_TO_MODULE_06 | `ready_for_review` may exist as an engineering/request state or flag indicating producer intent: > producer claims the change is ready to enter review. It MUST NOT mean: Review verdict remains UPOS-007. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-033` | Implementation directive §33 | REVIEW INTEGRATION | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 owns: UPOS-006 does not own: --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-034` | Implementation directive §34 | REVIEWER INDEPENDENCE + UPOS-005 PENDING INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 must support independent review by providing a stable review artifact: Reviewer Context itself belongs UPOS-005. Use only abstract: and mark: Do not define what Reviewer must or must not see. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-035` | Implementation directive §35 | CI / ENGINEERING CHECK INTEGRATION | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 should support references to execution such as: But distinguish: --- | `ENGINEERING_CHECK_INTEGRATION.md` |
| `ENG-DIR-036` | Implementation directive §36 | ENGINEERING CHECK REFERENCE | EXTRACTED_TO_MODULE_06 | Consider a minimal provider-neutral contract: UPOS-006 should not invent Quality scoring. --- | `ENGINEERING_CHECK_INTEGRATION.md` |
| `ENG-DIR-037` | Implementation directive §37 | CHECK RESULT STALENESS | MIXED_EXTRACTED_AND_DEFERRED | If the checked artifact changes: UPOS-006 should expose that the check was produced against an older artifact identity. UPOS-007 decides whether rerun is required. --- | `ENGINEERING_CHECK_INTEGRATION.md` |
| `ENG-DIR-038` | Implementation directive §38 | CHANGE ISOLATION | EXTRACTED_TO_MODULE_06 | Engineering Change isolation should protect against: Provide explicit validation. --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-039` | Implementation directive §39 | CONCURRENT AGENT WORK | MIXED_EXTRACTED_AND_DEFERRED | Parallel Agent implementation is allowed only when engineering isolation is safe. Distinguish: --- | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-DIR-040` | Implementation directive §40 | COLLISION MODEL | EXTRACTED_TO_MODULE_06 | A collision may be: Refine taxonomy after analysis. Do not assume file overlap is the only conflict. --- | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-DIR-041` | Implementation directive §41 | COLLISION RESPONSE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 may report engineering constraints such as: But Workflow orchestration response belongs UPOS-004. --- | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-DIR-042` | Implementation directive §42 | SHARED CONTRACT FIRST | MIXED_EXTRACTED_AND_DEFERRED | Preserve UPOS-004 principle: Before parallel implementation across dependent surfaces, stable shared contracts should exist where required. UPOS-006 consumes those references. It does not define Product/API/Domain contract truth. --- | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-DIR-043` | Implementation directive §43 | MULTI-REPOSITORY CHANGES | EXTRACTED_TO_MODULE_06 | Explicitly support: Each unit may have: but share: Integration order/dependency must remain explicit. --- | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-DIR-044` | Implementation directive §44 | MULTI-REPO MERGE ORDER | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 may declare engineering dependency constraints such as: But overall Workflow ordering remains UPOS-004. Deployment/release orchestration is not owned by Module 06. --- | `MULTI_REPOSITORY_CHANGE_MODEL.md` |
| `ENG-DIR-045` | Implementation directive §45 | BASE REVISION | EXTRACTED_TO_MODULE_06 | Every Repository Change Unit must know the repository state it started from. Define: This is needed for: --- | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-DIR-046` | Implementation directive §46 | ARTIFACT STALENESS | EXTRACTED_TO_MODULE_06 | Engineering artifacts can become stale when: Do not define Context staleness here. Engineering artifact staleness is Module-06 scope. Context staleness remains UPOS-005. --- | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-DIR-047` | Implementation directive §47 | REBASE GOVERNANCE | MIXED_EXTRACTED_AND_DEFERRED | Define semantic requirements for rebase/update-base operations. A rebase changes commit identity/history. Therefore it MUST preserve provenance and expose invalidation implications. Do not silently pretend: Quality decision external. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-048` | Implementation directive §48 | MERGE GOVERNANCE | MIXED_EXTRACTED_AND_DEFERRED | Separate: This boundary must be explicit everywhere. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-049` | Implementation directive §49 | MECHANICAL MERGEABILITY | EXTRACTED_TO_MODULE_06 | UPOS-006 MAY determine/report: Call this something like: It MUST NOT mean: --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-050` | Implementation directive §50 | MERGE OPERATION CONTRACT | EXTRACTED_TO_MODULE_06 | A Merge Operation should preserve/reference: Machine schema deferred. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-051` | Implementation directive §51 | MERGE STRATEGY | EXTRACTED_TO_MODULE_06 | Do not hard-code universally: UPOS-006 defines strategy semantics/integrity expectations. Project Adapter/policy selects allowed/default strategies. No strategy may silently destroy required provenance. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-052` | Implementation directive §52 | SQUASH | EXTRACTED_TO_MODULE_06 | If project policy uses squash: Ensure traceability from resulting integrated revision back to: Original logical commit history may be transformed, but provenance must remain discoverable. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-053` | Implementation directive §53 | FORCE PUSH / HISTORY REWRITE | EXTRACTED_TO_MODULE_06 | Do not define permission ownership here. UPOS-006 may classify operations as: and require permission/protected-action interfaces. UPOS-010 decides who may execute them. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-054` | Implementation directive §54 | PROTECTED BRANCH INTERFACE | EXTRACTED_TO_MODULE_06 | UPOS-006 may define engineering requirement: but: Do not bind GitHub branch-protection settings directly. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-055` | Implementation directive §55 | MERGE INVALIDATION | MIXED_EXTRACTED_AND_DEFERRED | A Merge readiness package may become stale when: UPOS-006 owns engineering artifact-change detection. Quality/security approval validity remains with their owners. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-056` | Implementation directive §56 | REVERT / BACKOUT | EXTRACTED_TO_MODULE_06 | Define repository-level: as controlled creation of a repository change intended to reverse previous integrated changes. Do not conflate with: Those belong elsewhere. --- | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-DIR-057` | Implementation directive §57 | REVERT TRACEABILITY | EXTRACTED_TO_MODULE_06 | A revert/backout must reference: Do not erase the original history. --- | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-DIR-058` | Implementation directive §58 | ROLLBACK BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 may require a rollback strategy reference. UPOS-006 owns only repository-level recovery mechanics. Examples outside scope: Do not absorb them. --- | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-DIR-059` | Implementation directive §59 | ABANDONED ENGINEERING CHANGE | EXTRACTED_TO_MODULE_06 | Support explicit abandonment. If work is abandoned: must have controlled lifecycle handling. Do not silently delete provenance required for audit. --- | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-DIR-060` | Implementation directive §60 | ENGINEERING PROVENANCE | MIXED_EXTRACTED_AND_DEFERRED | Create a normative engineering provenance model. It should support: Do NOT design event/trace schema. This is semantic artifact relationship/provenance. --- | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-DIR-061` | Implementation directive §61 | PROVENANCE != OBSERVABILITY | MIXED_EXTRACTED_AND_DEFERRED | Explicit separation: UPOS-008 later observes these stable entities. --- | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-DIR-062` | Implementation directive §62 | STABLE SEMANTIC IDENTITIES | EXTRACTED_TO_MODULE_06 | Evaluate and define only justified IDs. Likely: For VCS-native objects prefer external stable refs: Do not manufacture redundant IDs without purpose. --- | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-DIR-063` | Implementation directive §63 | FUTURE CONTROL PLANE SUPPORT | EXTRACTED_TO_MODULE_06 | Without designing Observability, Module 06 must make it possible to answer later: --- | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-DIR-064` | Implementation directive §64 | CHANGE SCOPE VALIDATION | MIXED_EXTRACTED_AND_DEFERRED | Engineering Change must remain within approved/routed scope. If implementation discovers out-of-scope work: UPOS-006 does not silently expand engineering scope. --- | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-DIR-065` | Implementation directive §65 | ARCHITECTURAL DISCOVERY | MIXED_EXTRACTED_AND_DEFERRED | If implementation discovers required architecture changes: Then Workflow/Architecture governs resolution. Do not let repository implementation become implicit architecture authority. --- | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-DIR-066` | Implementation directive §66 | GENERATED FILES | EXTRACTED_TO_MODULE_06 | Define handling for generated artifacts. Rules should address: Concrete generator command belongs UPOS-011. Quality verification belongs UPOS-007. --- | `SPECIAL_REPOSITORY_ARTIFACTS.md` |
| `ENG-DIR-067` | Implementation directive §67 | LOCKFILES / DEPENDENCY ARTIFACTS | EXTRACTED_TO_MODULE_06 | Dependency changes often modify lockfiles/generated manifests. Treat them as first-class engineering artifacts when required. Avoid unrelated dependency churn. Dependency risk/routing remains UPOS-004 profiles/work type. --- | `SPECIAL_REPOSITORY_ARTIFACTS.md` |
| `ENG-DIR-068` | Implementation directive §68 | DATABASE MIGRATION FILES | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 may govern repository mechanics for migration artifacts: But database/data migration safety semantics belong relevant Workflow/Quality/Security/project systems. Do not make Module 06 a database governance system. --- | `SPECIAL_REPOSITORY_ARTIFACTS.md` |
| `ENG-DIR-069` | Implementation directive §69 | DOCUMENTATION CHANGES IN ENGINEERING PR | MIXED_EXTRACTED_AND_DEFERRED | Documentation may live in same Integration Request when it is part of one coherent change. But canonical documentation truth/ownership remains UPOS-01. `Documentation Guardian` authority remains UPOS-002. Documentation Quality remains external. --- | `SPECIAL_REPOSITORY_ARTIFACTS.md` |
| `ENG-DIR-070` | Implementation directive §70 | SECURITY BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | Engineering operations may require capabilities such as: UPOS-006 declares required capabilities. UPOS-010 grants/denies/protects them. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-071` | Implementation directive §71 | TOOL / PROVIDER BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | Universal Engineering Governance MUST NOT hard-code: UPOS-011 owns binding. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-072` | Implementation directive §72 | GIT BOUNDARY | EXTRACTED_TO_MODULE_06 | Git-like concepts such as: may be normative if the operating model assumes Git-based source control. But repository provider remains abstract. Document this assumption explicitly. Do not accidentally conflate: --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-073` | Implementation directive §73 | QUALITY BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 MAY require references to: but not define: Those belong UPOS-007. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-074` | Implementation directive §74 | CONTEXT BOUNDARY — PROVISIONAL | MIXED_EXTRACTED_AND_DEFERRED | Until UPOS-005 is frozen, only state abstract requirements such as: Use: as placeholders. Every such interface must be recorded in: Do NOT freeze exact names/fields yet. --- | `CROSS_MODULE_INTERFACES.md; analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md` |
| `ENG-DIR-075` | Implementation directive §75 | REQUIRED UPOS-005 RECONCILIATION REGISTER | EXTRACTED_TO_MODULE_06 | Create: Status while UPOS-005 unfinished: For every dependency record: Example: --- | `analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md; MODULE_06_DEFINITION_OF_DONE.md` |
| `ENG-DIR-076` | Implementation directive §76 | UPOS-005 RECONCILIATION GATE | MIXED_EXTRACTED_AND_DEFERRED | Module 06 MUST NOT reach final: until: Final reconciliation must check at least: Do not change UPOS-005 ownership. --- | `analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md; MODULE_06_DEFINITION_OF_DONE.md` |
| `ENG-DIR-077` | Implementation directive §77 | ENGINEERING GOVERNANCE POLICY VS PROJECT POLICY | EXTRACTED_TO_MODULE_06 | Universal Module 06 defines semantic invariants. Projects may impose stricter engineering rules, for example: But project-specific rules/configuration belong UPOS-011 and/or relevant owner modules. Module 06 should define extension/interface points. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-078` | Implementation directive §78 | NO ARBITRARY UNIVERSAL NUMERIC LIMITS | EXTRACTED_TO_MODULE_06 | Do not hard-code: unless frozen source mandates it. Prefer semantic criteria: Metrics may later reveal project-appropriate thresholds. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-079` | Implementation directive §79 | PR SIZE | EXTRACTED_TO_MODULE_06 | Large Integration Request is a warning signal, not automatically invalid. Evaluate: differently from: Semantic cohesion dominates raw LOC. --- | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-DIR-080` | Implementation directive §80 | MERGE CONTROLLER INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 owns Merge Controller. UPOS-006 should expose to Merge Controller an engineering integration package such as: It does not grant merge authority. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-081` | Implementation directive §81 | MERGE READINESS SKILL INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | `SKL-ASSESS-MERGE-READINESS` exists in UPOS-003. Boundary: Keep all four distinct. --- | `MERGE_GOVERNANCE.md` |
| `ENG-DIR-082` | Implementation directive §82 | WORKFLOW INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 may say: UPOS-006 supplies engineering mechanics. It must not decide when those stages run. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-083` | Implementation directive §83 | REWORK INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | When UPOS-004 routes work back for rework: UPOS-006 must support: Do not create rework orchestration loops. UPOS-004 owns loop sequencing/bounds. UPOS-007 owns finding semantics. UPOS-005 owns rework Context. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-084` | Implementation directive §84 | HOTFIX INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | Hotfix may use expedited repository mechanics where project policy permits. But: Preserve: Workflow decides compressed stages. Security/permissions remain external. --- | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-DIR-085` | Implementation directive §85 | RELEASE BRANCH / TAG BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | Evaluate source-control release artifacts such as: Module 06 may own their repository mechanics. Release Workflow sequencing remains UPOS-004. Release Quality remains UPOS-007. Deployment remains elsewhere. Project naming/version conventions may belong UPOS-011/project docs. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-086` | Implementation directive §86 | TAG / RELEASE REVISION PROVENANCE | MIXED_EXTRACTED_AND_DEFERRED | If tags/releases are included in Module-06 scope, ensure they reference exact integrated revision and upstream engineering provenance. Do not silently retag different code under same governed release identity where policy forbids it. Avoid over-expanding into release management. --- | `BRANCH_GOVERNANCE.md` |
| `ENG-DIR-087` | Implementation directive §87 | ENGINEERING FAILURE CONDITIONS | EXTRACTED_TO_MODULE_06 | Create a Module-06 engineering failure/condition taxonomy distinct from Workflow failure taxonomy. Candidates: Refine after analysis. For each: Do not duplicate UPOS-004 failure orchestration. --- | `ENGINEERING_FAILURE_MODEL.md` |
| `ENG-DIR-088` | Implementation directive §88 | ENGINEERING RESULT STATES | EXTRACTED_TO_MODULE_06 | Evaluate whether Engineering Change / Repository Change Unit need small operational state models. Avoid duplicating Workflow state. Possible Repository Change Unit states: Only adopt if semantic value is real. Do not use Quality states. --- | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-DIR-089` | Implementation directive §89 | ENGINEERING CHANGE COMPLETION | EXTRACTED_TO_MODULE_06 | Engineering completion does not imply: It means its repository integration contract is satisfied. Keep terminal semantics separate. --- | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-DIR-090` | Implementation directive §90 | MACHINE-READABLE SCHEMA BOUNDARY | MIXED_EXTRACTED_AND_DEFERRED | Future schemas may encode: But schemas must trace back to normative Module-06 Markdown. Do not create an independent semantic source. --- | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-DIR-091` | Implementation directive §91 | CANDIDATE PACKAGE | IMPLEMENTATION_GOVERNANCE | Propose, validate, then implement approximately: Это architectural hypothesis. Refine package tree if analysis produces a cleaner decomposition. Do not create files only to satisfy this tree. Preserve semantics. --- | `analysis/*` |
| `ENG-DIR-092` | Implementation directive §92 | ANALYSIS FIRST | IMPLEMENTATION_GOVERNANCE | Before normative mass implementation create: Analysis files: Do not promote analysis conclusions into truth without normative artifact implementation. --- | `analysis/*` |
| `ENG-DIR-093` | Implementation directive §93 | SOURCE DISPOSITION | IMPLEMENTATION_GOVERNANCE | For each relevant frozen-source section use: Examples: --- | `analysis/*` |
| `ENG-DIR-094` | Implementation directive §94 | AMBIGUITY / GAP REGISTER | IMPLEMENTATION_GOVERNANCE | At minimum inspect: Each gap: No unresolved P0/P1 internal Module-06 gaps before provisional completion. UPOS-005-dependent items may remain explicitly pending reconciliation and MUST NOT be falsely marked resolved. --- | `analysis/*` |
| `ENG-DIR-095` | Implementation directive §95 | TRACEABILITY | IMPLEMENTATION_GOVERNANCE | Create: Mapping: Coverage should include: UPOS-005 reconciliation requirements should receive separate IDs when final reconciliation occurs. Internal completion may report: if genuinely true. But final freeze validation remains blocked by UPOS-005 reconciliation. --- | `MODULE_06_TRACEABILITY.md` |
| `ENG-DIR-096` | Implementation directive §96 | CROSS-MODULE INTERFACES | MIXED_EXTRACTED_AND_DEFERRED | Create `CROSS_MODULE_INTERFACES.md`. For each module define: Cover: --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-097` | Implementation directive §97 | MODULE-06 → UPOS-005 TEMPORARY INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | Until final Module 05 exists, only state: No stronger assumptions. --- | `CROSS_MODULE_INTERFACES.md; analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md` |
| `ENG-DIR-098` | Implementation directive §98 | MODULE-06 → UPOS-007 INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 provides: Consumes: Must not redefine Quality verdicts. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-099` | Implementation directive §99 | MODULE-06 → UPOS-008 INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | Expose stable references for future telemetry: Do not define: --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-100` | Implementation directive §100 | MODULE-06 → UPOS-009 INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | Engineering failures may later become learning evidence: UPOS-006 reports evidence/signals. It does not modify policy automatically. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-101` | Implementation directive §101 | MODULE-06 → UPOS-010 INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | Declare capability requirements such as: UPOS-010 owns: --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-102` | Implementation directive §102 | MODULE-06 → UPOS-011 INTERFACE | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 provides abstract engineering requirements. UPOS-011 resolves: Universal Module 06 contains no concrete project wiring. --- | `CROSS_MODULE_INTERFACES.md` |
| `ENG-DIR-103` | Implementation directive §103 | PROVISIONAL DEFINITION OF DONE | EXTRACTED_TO_MODULE_06 | Before UPOS-005 reconciliation, Module 06 may be declared: when: --- | `MODULE_06_DEFINITION_OF_DONE.md; README.md` |
| `ENG-DIR-104` | Implementation directive §104 | FINAL FREEZE DEFINITION OF DONE — NOT YET SATISFIABLE | MIXED_EXTRACTED_AND_DEFERRED | The following checks MUST remain unchecked/pending until FROZEN UPOS-005 exists: Do NOT check these prematurely. --- | `MODULE_06_DEFINITION_OF_DONE.md; README.md` |
| `ENG-DIR-105` | Implementation directive §105 | IMPLEMENTATION DISCIPLINE | IMPLEMENTATION_GOVERNANCE | Do not make one giant commit. Recommended sequence: After UPOS-005 freeze later: then final validation/freeze. Preserve: Ironically Module 06 itself should follow the standard it defines. --- | `analysis/IMPLEMENTATION_PLAN.md` |
| `ENG-DIR-106` | Implementation directive §106 | FIRST DELIVERABLE BEFORE NORMATIVE IMPLEMENTATION | IMPLEMENTATION_GOVERNANCE | First show/create: 1. Module 06 scope; 2. Module 06 non-scope; 3. fundamental engineering entity model; 4. Engineering Change vs Task/Workflow boundary; 5. Repository Change Unit model; 6. Workspace/isolation model; 7. branch governance model; 8. atomic commit model; 9. Commit vs Integration… | `analysis/*` |
| `ENG-DIR-107` | Implementation directive §107 | PROVISIONAL FINAL OUTPUT | IMPLEMENTATION_GOVERNANCE | At the end of this branch provide: 1. complete provisional `06_engineering_governance/` package; 2. virtual repository tree; 3. normative artifact inventory; 4. Engineering Change model; 5. Repository Change Unit model; 6. Workspace/branch isolation model; 7. Atomic Commit Standard summary; 8.… | `MODULE_06_DEFINITION_OF_DONE.md; README.md` |
| `ENG-DIR-108` | Implementation directive §108 | FINAL RECONCILIATION PROCEDURE — EXECUTE LATER | MIXED_EXTRACTED_AND_DEFERRED | Once the final frozen: is supplied, perform only a narrow interface reconciliation. Do not redesign Module 06. Check: Resolve every item in: Then rerun: Only then may Module 06 become: --- | `analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md; MODULE_06_DEFINITION_OF_DONE.md` |
| `ENG-DIR-109` | Implementation directive §109 | FINAL PRINCIPLES | EXTRACTED_TO_MODULE_06 | The goal is not maximum Git bureaucracy. The goal is: Do not confuse: Do not confuse: Do not confuse: Do not confuse: Do not confuse: Do not confuse: Do not confuse: Do not confuse: Do not allow: Do not allow: Do not allow: Do not invent final Context semantics while UPOS-005 is unfinished. The… | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md` |
| `ENG-FROZEN-001` | Frozen master §3.7 | Small coherent changes | EXTRACTED_OR_MIXED | Prefer reviewable coherent engineering changes. | `ATOMIC_COMMIT_STANDARD.md; INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-002` | Frozen master §3.8 | One PR, one intention | EXTRACTED_OR_MIXED | Normalize provider-specific PR concept into one coherent Integration Request intention. | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-003` | Frozen master §3.9 | One commit, one logical change | EXTRACTED_OR_MIXED | One Commit represents one coherent logical intent. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-004` | Frozen master §3.10 | No opportunistic refactoring by default | EXTRACTED_OR_MIXED | Unrelated cleanup is prohibited inside a governed change. | `ATOMIC_COMMIT_STANDARD.md; ENGINEERING_CHANGE_MODEL.md` |
| `ENG-FROZEN-005` | Frozen master §43 | Expected commits | EXTRACTED_OR_MIXED | Commit planning is indicative and organized by coherent intent. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-006` | Frozen master §44 | Git operating principles | EXTRACTED_OR_MIXED | Branch/change isolation is preferred; physical branch conventions remain project-specific. | `BRANCH_GOVERNANCE.md` |
| `ENG-FROZEN-007` | Frozen master §45 | Atomic logical commits | EXTRACTED_OR_MIXED | Commit atomicity is semantic, understandable, revertable where practical. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-008` | Frozen master §46 | Bad commit granularity | EXTRACTED_OR_MIXED | Do not turn history into one-commit-per-trivial-action. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-009` | Frozen master §47 | Bad oversized commit | EXTRACTED_OR_MIXED | Do not combine unrelated engineering intentions. | `ATOMIC_COMMIT_STANDARD.md; INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-010` | Frozen master §48 | Commit categories | EXTRACTED_OR_MIXED | Commit taxonomy is adaptable/project-specific, not universally hard-coded. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-011` | Frozen master §49 | Commit message contract | EXTRACTED_OR_MIXED | Commit message conveys intent/scope/reason without mandatory universal syntax. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-012` | Frozen master §50 | Bug-fix commit strategy | EXTRACTED_OR_MIXED | Regression protection and fix separation is preferred where practical but governed by project history policy. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-013` | Frozen master §51 | Review-fix commits | EXTRACTED_OR_MIXED | Group related review corrections; do not commit per comment. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-014` | Frozen master §52–56 | PR operating model / size / description | EXTRACTED_OR_MIXED | Integration Request is one coherent reviewable intention with scope/non-scope/evidence refs; no hard LOC limit. | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-015` | Frozen master §57 | Creation loop | EXTRACTED_OR_MIXED | Repository mechanics support implement/self-check/commit/update Integration Request while Workflow owns sequence. | `CROSS_MODULE_INTERFACES.md; ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-016` | Frozen master §59 | Self-check | EXTRACTED_OR_MIXED | Engineering checks can attach to exact artifacts; self-check does not equal independent approval. | `ENGINEERING_CHECK_INTEGRATION.md` |
| `ENG-FROZEN-017` | Frozen master §72 | Merge strategy | EXTRACTED_OR_MIXED | Merge strategy is project-configurable and must preserve meaningful provenance. | `MERGE_GOVERNANCE.md` |
| `ENG-FROZEN-018` | Frozen master §81 | Scope Guardian | EXTRACTED_OR_MIXED | Module 06 detects diff/scope drift and emits scope signals; authority/orchestration external. | `ENGINEERING_FAILURE_MODEL.md; ENGINEERING_CHANGE_MODEL.md` |
| `ENG-FROZEN-019` | Frozen master §82 | Concurrency model | EXTRACTED_OR_MIXED | Logical parallelism requires safe repository isolation and collision constraints. | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-FROZEN-020` | Frozen master §83 | Task isolation | EXTRACTED_OR_MIXED | Normalize one task/branch/worktree preference into RCU/workspace isolation that supports multi-repo tasks. | `REPOSITORY_WORKSPACE_AND_ISOLATION.md; BRANCH_GOVERNANCE.md` |
| `ENG-FROZEN-021` | Frozen master §84 | Shared file collision | EXTRACTED_OR_MIXED | Detect repository collision and expose serialization/coordination constraints. | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-FROZEN-022` | Frozen master §135 | Oversized PR handling | EXTRACTED_OR_MIXED | Split oversized Integration Requests by independent intention when safe. | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-023` | Frozen master §136 | Scope expansion handling | EXTRACTED_OR_MIXED | Repository scope expansion is signaled to UPOS-004; no silent expansion. | `ENGINEERING_CHANGE_MODEL.md; ENGINEERING_FAILURE_MODEL.md` |
| `ENG-FROZEN-024` | Frozen master §137 | Unplanned architecture discovery | EXTRACTED_OR_MIXED | Implementation must not create implicit architecture authority. | `ENGINEERING_CHANGE_MODEL.md` |
| `ENG-FROZEN-025` | Frozen master §141 | Agent sandbox hygiene | EXTRACTED_OR_MIXED | Allocate isolated workspace, record base, preserve clean attributable state. | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` |
| `ENG-FROZEN-026` | Frozen master §142 | Branch lifetime | EXTRACTED_OR_MIXED | Prefer short-lived branches without universal numeric limit. | `BRANCH_GOVERNANCE.md` |
| `ENG-FROZEN-027` | Frozen master §143 | Stacked PRs | EXTRACTED_OR_MIXED | Dependent Integration Requests may be stacked when dependency is explicit. | `INTEGRATION_REQUEST_STANDARD.md; MULTI_REPOSITORY_CHANGE_MODEL.md` |
| `ENG-FROZEN-028` | Frozen master §145 | Rollback thinking | EXTRACTED_OR_MIXED | Module 06 provides repository revert/backout mechanics while broader rollback remains external. | `REVERT_BACKOUT_AND_RECOVERY.md` |
| `ENG-FROZEN-029` | Frozen master §146 | Dependency graph awareness | EXTRACTED_OR_MIXED | Engineering dependency constraints support safe parallelism without owning Workflow sequencing. | `MULTI_REPOSITORY_CHANGE_MODEL.md; CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-FROZEN-030` | Frozen master §154 | Review freshness | EXTRACTED_OR_MIXED | Artifact identity changes are exposed; UPOS-007 decides review validity. | `ENGINEERING_CHECK_INTEGRATION.md; BRANCH_GOVERNANCE.md` |
| `ENG-FROZEN-031` | Frozen master §155 | Merge queue compatibility | EXTRACTED_OR_MIXED | Queue integration is an abstract mechanism; provider implementation remains UPOS-011. | `MERGE_GOVERNANCE.md` |
| `ENG-FROZEN-032` | Frozen master §156 | CI as evidence provider | EXTRACTED_OR_MIXED | Checks are bound to exact artifacts; CI success is not a Quality verdict. | `ENGINEERING_CHECK_INTEGRATION.md` |
| `ENG-FROZEN-033` | Frozen master §164 | Post-merge verification | EXTRACTED_OR_MIXED | Integrated revision is attributable for repository verification; deployment/Quality semantics external. | `ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-FROZEN-034` | Frozen master §189 | Auditability | EXTRACTED_OR_MIXED | Preserve actor/change/evidence refs/approval refs/integrated revision provenance. | `ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-FROZEN-035` | Frozen master §190 | Reproducibility | EXTRACTED_OR_MIXED | Reconstruct task/context/plan/commits/review/QA/merge references without hidden reasoning. | `ENGINEERING_PROVENANCE_MODEL.md; COMMIT_PROVENANCE_STANDARD.md` |
| `ENG-FROZEN-036` | Frozen master §197 | PR lifecycle | EXTRACTED_OR_MIXED | Normalize platform PR lifecycle into provider-neutral Integration Request lifecycle. | `INTEGRATION_REQUEST_LIFECYCLE.md` |
| `ENG-FROZEN-037` | Frozen master §205 | Change decomposition | EXTRACTED_OR_MIXED | Repository units split by coherent ownership/dependency, not arbitrary file count. | `REPOSITORY_CHANGE_UNIT_STANDARD.md` |
| `ENG-FROZEN-038` | Frozen master §206 | Multi-agent code ownership | EXTRACTED_OR_MIXED | Parallel implementers require explicit workspace/RCU ownership isolation. | `REPOSITORY_WORKSPACE_AND_ISOLATION.md; CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-FROZEN-039` | Frozen master §207 | Shared contract first | EXTRACTED_OR_MIXED | Module 06 consumes shared-contract refs before dependent parallel engineering. | `CONCURRENCY_COLLISION_AND_CONFLICT.md` |
| `ENG-FROZEN-040` | Frozen master §208 | Reviewer context independence | EXTRACTED_OR_MIXED | Stable review artifact is Module 06; Reviewer Context is an independent UPOS-005 Context Request/Bundle; Module 06 records the reviewed artifact and upstream Bundle reference. | `INTEGRATION_REQUEST_STANDARD.md; analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md` |
| `ENG-FROZEN-041` | Frozen master §218 | Change evidence bundle | EXTRACTED_OR_MIXED | Integration Request is a container of external result refs, not evidence-sufficiency owner. | `INTEGRATION_REQUEST_STANDARD.md` |
| `ENG-FROZEN-042` | Frozen master §219 | Artifact retention | EXTRACTED_OR_MIXED | Preserve required engineering provenance; retention policy remains external. | `ENGINEERING_PROVENANCE_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `ENG-FROZEN-043` | Frozen master §220 | Privacy of reasoning | EXTRACTED_OR_MIXED | Engineering provenance excludes hidden chain-of-thought. | `COMMIT_PROVENANCE_STANDARD.md; ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-FROZEN-044` | Frozen master §221.10 | Git history as keystroke log | EXTRACTED_OR_MIXED | One commit per trivial action is an anti-pattern. | `ATOMIC_COMMIT_STANDARD.md` |
| `ENG-FROZEN-045` | Frozen master Appendix L | Git Policy starter | EXTRACTED_OR_MIXED | Extract branch/commit/IR/merge mechanics; authority/quality/provider semantics remain deferred. | `BRANCH_GOVERNANCE.md; ATOMIC_COMMIT_STANDARD.md; INTEGRATION_REQUEST_STANDARD.md; MERGE_GOVERNANCE.md` |

## 3. FROZEN UPOS-005 reconciliation requirements

| Requirement | Source | Reconciled requirement | Canonical Module-06 artifact |
|---|---|---|---|
| `ENG-CTX-001` | UPOS-005 `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` §2–3; `CONTEXT_BUNDLE_STANDARD.md` §1–2 | Engineering provenance may reuse stable upstream `context_request_id` / `context_bundle_id`; Module 06 must not invent replacement Context identities. | `ENGINEERING_CHANGE_MODEL.md`; `ENGINEERING_PROVENANCE_MODEL.md`; templates |
| `ENG-CTX-002` | UPOS-005 `CONTEXT_ISOLATION_AND_VIEWS.md` §1–4 | Role-specific Context View is represented through Role/Run-scoped Context Request/Bundle; no global `context_view_id` is introduced. | `REPOSITORY_WORKSPACE_AND_ISOLATION.md`; `CROSS_MODULE_INTERFACES.md` |
| `ENG-CTX-003` | UPOS-005 `CONTEXT_BUNDLE_STANDARD.md` §5/8–9 | Commit/engineering Context provenance references immutable `context_bundle_id`; Bundle Manifest/source provenance remains Module 05-owned. | `COMMIT_PROVENANCE_STANDARD.md`; `ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-CTX-004` | UPOS-005 `CONTEXT_BUNDLE_STANDARD.md`; `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` | Integration Requests may reference implementation/review Context Bundles but do not decide Bundle validity; reassembly produces new Bundle identity. | `INTEGRATION_REQUEST_STANDARD.md`; template |
| `ENG-CTX-005` | UPOS-005 `CONTEXT_ISOLATION_AND_VIEWS.md` §3 | Reviewer Context must be independent from producer Context; review artifact remains separate from Reviewer Context. | `INTEGRATION_REQUEST_STANDARD.md`; `CROSS_MODULE_INTERFACES.md` |
| `ENG-CTX-006` | UPOS-005 `CONTEXT_MEMORY_LIFECYCLE.md` §7 | Engineering provenance chain supports Task/Workflow/Stage/Run/Skill → Context Request → Context Bundle → repository artifact reconstructibility. | `ENGINEERING_PROVENANCE_MODEL.md` |
| `ENG-CTX-007` | UPOS-005 `CROSS_MODULE_INTERFACES.md` — UPOS-006 | Module 06 provides repository/diff/commit/IR artifact interfaces and consumes Context requirements/references without redefining Git in Module 05 or Context in Module 06. | `CROSS_MODULE_INTERFACES.md` |
| `ENG-CTX-008` | UPOS-005 `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` §4/8–9 | Material artifact/head/base changes are exposed by Module 06; Module 05 determines Context revalidation/STALE/INVALIDATED/reassembly. | `ENGINEERING_CHECK_INTEGRATION.md`; `MERGE_GOVERNANCE.md` |
| `ENG-CTX-009` | UPOS-005 `CONTEXT_ASSEMBLY_STANDARD.md` §8 | Rework/re-review requires prior Context revalidation against findings/changed artifact; if rebuilt, new `context_bundle_id` supersedes prior Bundle. | `CROSS_MODULE_INTERFACES.md`; `INTEGRATION_REQUEST_STANDARD.md` |

## 4. Final conformance cleanup requirements

| Requirement | Source | Reconciled requirement | Canonical Module-06 artifact |
|---|---|---|---|
| `ENG-CONF-001` | Final conformance cleanup directive §1 | Remove stale operational `[UPOS-005 pending]` wording after completed reconciliation; historical/source quotations may remain explicitly historical. | `ENGINEERING_GOVERNANCE_OPERATING_MODEL.md`; `analysis/TRACEABILITY_VALIDATION.md` |
| `ENG-CONF-002` | Final conformance cleanup directive §2 | Commit Provenance operational template must represent `routing_decision_id` already present in the normative Commit Provenance Standard. | `COMMIT_PROVENANCE_STANDARD.md`; `templates/COMMIT_PROVENANCE_TEMPLATE.md` |
| `ENG-CONF-003` | Final conformance cleanup directive §3 | Engineering Change operational template must represent mandatory affected repository references from the Engineering Change contract. | `ENGINEERING_CHANGE_MODEL.md`; `templates/ENGINEERING_CHANGE_TEMPLATE.md` |
| `ENG-CONF-004` | Final conformance cleanup directive §3/7 | All five canonical operational templates must mechanically conform to their owning normative contracts without strengthening/weaking requiredness semantics. | `templates/*`; `analysis/TRACEABILITY_VALIDATION.md` |
| `ENG-CONF-005` | Final conformance cleanup directive §7 | Validation must distinguish active operational normative pending markers from historical source quotations/evidence. | `analysis/TRACEABILITY_VALIDATION.md` |

## 5. Coverage statement

```text
UNMAPPED MODULE-06 SOURCE REQUIREMENTS = 0
```

This means all Module-06 requirements identified from the frozen master, the Module-06 implementation directive, the final frozen UPOS-005 reconciliation, and the final conformance cleanup are mapped to canonical Module-06 artifacts or explicit historical evidence artifacts.

The UPOS-005 reconciliation gate is complete.

## 6. UPOS-005 reconciliation status

```text
ENG-CTX-001 … ENG-CTX-009 = MAPPED
UPOS-005 RECONCILIATION = COMPLETE
UNRESOLVED CONTEXT INTERFACE REQUIREMENTS = 0
```

All final Context-interface requirements are mapped to canonical Module-06 artifacts.

===== END VIRTUAL FILE: MODULE_06_TRACEABILITY.md =====


---

## VIRTUAL FILE 23/42 — `VIRTUAL_REPOSITORY_TREE.md`

**Virtual path:** `VIRTUAL_REPOSITORY_TREE.md`  
**Content checksum:** `33e9d69ab91a`

===== BEGIN VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

# UPOS-006 Virtual Repository Tree

**ID:** UPOS-06-TREE-001  
**Type:** REFERENCE / PACKAGE TREE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```text
06_engineering_governance/
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md
├── analysis/COMMIT_ATOMICITY_ANALYSIS.md
├── analysis/CONCURRENCY_COLLISION_ANALYSIS.md
├── analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MERGE_BOUNDARY_ANALYSIS.md
├── analysis/MODULE_06_OWNERSHIP_MAP.md
├── analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md
├── ATOMIC_COMMIT_STANDARD.md
├── BRANCH_GOVERNANCE.md
├── COMMIT_PROVENANCE_STANDARD.md
├── CONCURRENCY_COLLISION_AND_CONFLICT.md
├── CROSS_MODULE_INTERFACES.md
├── ENGINEERING_CHANGE_MODEL.md
├── ENGINEERING_CHECK_INTEGRATION.md
├── ENGINEERING_FAILURE_MODEL.md
├── ENGINEERING_GOVERNANCE_OPERATING_MODEL.md
├── ENGINEERING_LIFECYCLE_AND_VERSIONING.md
├── ENGINEERING_PROVENANCE_MODEL.md
├── INTEGRATION_REQUEST_LIFECYCLE.md
├── INTEGRATION_REQUEST_STANDARD.md
├── MERGE_GOVERNANCE.md
├── MODULE_06_DEFINITION_OF_DONE.md
├── MODULE_06_TRACEABILITY.md
├── MULTI_REPOSITORY_CHANGE_MODEL.md
├── README.md
├── REPOSITORY_CHANGE_UNIT_STANDARD.md
├── REPOSITORY_WORKSPACE_AND_ISOLATION.md
├── REVERT_BACKOUT_AND_RECOVERY.md
├── SPECIAL_REPOSITORY_ARTIFACTS.md
├── templates/COMMIT_PROVENANCE_TEMPLATE.md
├── templates/ENGINEERING_CHANGE_TEMPLATE.md
├── templates/INTEGRATION_REQUEST_TEMPLATE.md
├── templates/MERGE_OPERATION_TEMPLATE.md
├── templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md
├── VIRTUAL_REPOSITORY_TREE.md
```

===== END VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====


---

## VIRTUAL FILE 24/42 — `templates/COMMIT_PROVENANCE_TEMPLATE.md`

**Virtual path:** `templates/COMMIT_PROVENANCE_TEMPLATE.md`  
**Content checksum:** `28e6a172c54f`

===== BEGIN VIRTUAL FILE: templates/COMMIT_PROVENANCE_TEMPLATE.md =====

# Commit Provenance Template

**ID:** UPOS-06-TPL-003  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
Commit Reference:
Repository Change Unit ID:
Engineering Change ID:

Task ID:
Routing Decision ID:
Workflow Instance ID:
Stage ID:

Role Reference:
Agent Run Reference:
Skill Invocation Reference:

Context Bundle ID References (`context_bundle_id`):

Parent/Base Reference:
Purpose:
Affected Scope:
Check References:
Integration Request Reference:
```

===== END VIRTUAL FILE: templates/COMMIT_PROVENANCE_TEMPLATE.md =====


---

## VIRTUAL FILE 25/42 — `templates/ENGINEERING_CHANGE_TEMPLATE.md`

**Virtual path:** `templates/ENGINEERING_CHANGE_TEMPLATE.md`  
**Content checksum:** `537ca00db643`

===== BEGIN VIRTUAL FILE: templates/ENGINEERING_CHANGE_TEMPLATE.md =====

# Engineering Change Template

**ID:** UPOS-06-TPL-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Engineering Change — <title>

Engineering Change ID:
Task ID:
Routing Decision ID:
Workflow Instance ID:
Stage ID:

Purpose:
Scope:
Non-scope:
Affected Repository References:

Implementation Plan Reference:
Canonical/Decision References:

Context Bundle ID References (`context_bundle_id`):
Context Request ID References (`context_request_id`, optional):

Repository Change Units:
Dependencies:

Discovered scope/architecture risks:

Engineering state:
ACTIVE / PARTIALLY_INTEGRATED / INTEGRATED / ABANDONED / SUPERSEDED
```

===== END VIRTUAL FILE: templates/ENGINEERING_CHANGE_TEMPLATE.md =====


---

## VIRTUAL FILE 26/42 — `templates/INTEGRATION_REQUEST_TEMPLATE.md`

**Virtual path:** `templates/INTEGRATION_REQUEST_TEMPLATE.md`  
**Content checksum:** `9169295b5846`

===== BEGIN VIRTUAL FILE: templates/INTEGRATION_REQUEST_TEMPLATE.md =====

# Integration Request Template

**ID:** UPOS-06-TPL-004  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Integration Request — <title>

Integration Request Reference:
Repository Change Unit ID:
Engineering Change ID:

Task ID:
Routing Decision ID:
Workflow Instance ID:
Stage ID:

## Why

## What

## Scope

## Non-scope

Repository Reference:
Base Revision Reference:
Head Revision Reference:
Change Branch Reference:
Target/Integration Reference:

Commit Set:

Change Class Reference:
Concern/Profile References:
Implementation Plan Reference:

Implementation Context Bundle ID References (`context_bundle_id`):
Reviewer Context Bundle ID References (`context_bundle_id`, populated from review provenance when applicable):

Engineering Check References:

Review Result Reference:
QA Result Reference:
Security Reference:
Documentation Reference:

Rollback/Revert Considerations:
Known Limitations:
Dependency/Integration Order:
Supersedes:

ready_for_review: false
```

===== END VIRTUAL FILE: templates/INTEGRATION_REQUEST_TEMPLATE.md =====


---

## VIRTUAL FILE 27/42 — `templates/MERGE_OPERATION_TEMPLATE.md`

**Virtual path:** `templates/MERGE_OPERATION_TEMPLATE.md`  
**Content checksum:** `78fc239b9b55`

===== BEGIN VIRTUAL FILE: templates/MERGE_OPERATION_TEMPLATE.md =====

# Merge Operation Template

**ID:** UPOS-06-TPL-005  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
Merge Operation ID:
Integration Request Reference:
Engineering Change ID:
Repository Change Unit ID:

Target/Integration Reference:
Source/Head Reference:

Pre-merge Base Revision:
Pre-merge Head Revision:
Selected Merge Strategy Reference:

Actor / Merge Controller Reference:
Permission Reference:
Approval Reference:
Quality/Readiness References:

Mechanical Mergeability:
Operation Result:
Resulting Integrated Revision:
Timestamp/Provenance Reference:
```

===== END VIRTUAL FILE: templates/MERGE_OPERATION_TEMPLATE.md =====


---

## VIRTUAL FILE 28/42 — `templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md`

**Virtual path:** `templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md`  
**Content checksum:** `bc37a50345d8`

===== BEGIN VIRTUAL FILE: templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md =====

# Repository Change Unit Template

**ID:** UPOS-06-TPL-002  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Repository Change Unit — <title>

Repository Change Unit ID:
Engineering Change ID:
Repository Reference:

Task ID:
Workflow Instance ID:
Stage ID:

Purpose:
Scope:
Non-scope:

Base Revision Reference:
Workspace ID:
Branch Reference:
Integration Request Reference:

Dependency References:
Check References:
Integrated Revision Reference:

State:
PREPARED / ACTIVE / INTEGRATION_REQUEST_OPEN / INTEGRATED / ABANDONED / SUPERSEDED
```

===== END VIRTUAL FILE: templates/REPOSITORY_CHANGE_UNIT_TEMPLATE.md =====


---

## VIRTUAL FILE 29/42 — `analysis/AMBIGUITY_GAP_REGISTER.md`

**Virtual path:** `analysis/AMBIGUITY_GAP_REGISTER.md`  
**Content checksum:** `918b164c922a`

===== BEGIN VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

# Module 06 Ambiguity & Gap Register

**ID:** UPOS-06-AN-010  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time analysis is found factually incorrect  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


| ID | Issue | Module-06 resolution | Deferred owner | Severity | Status |
|---|---|---|---|---|---|
| ENG-GAP-001 | Task vs Engineering Change | Engineering Change is repository realization referencing Task, never a competing Task. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-002 | Workflow Stage vs Repository Change Unit | Stage is orchestration; RCU is repository-scoped engineering unit. | UPOS-004 | P1 | RESOLVED |
| ENG-GAP-003 | Implementation Plan vs Engineering Change | Plan is consumed by Engineering Change; planning semantics remain Skill/Workflow governance. | UPOS-003/004 | P1 | RESOLVED |
| ENG-GAP-004 | Engineering Change vs Branch | Engineering Change may span repositories/branches; branch belongs to one RCU realization. | — | P1 | RESOLVED |
| ENG-GAP-005 | RCU vs Workspace | RCU is durable repository-scoped unit; Workspace is isolated mutable environment. | — | P1 | RESOLVED |
| ENG-GAP-006 | Workspace vs Agent Run | Workspace references Agent Run but is not an execution lifecycle. | UPOS-002 | P1 | RESOLVED |
| ENG-GAP-007 | Branch vs Workspace | Branch is VCS history/ref; Workspace is writable environment. | UPOS-011 realization | P1 | RESOLVED |
| ENG-GAP-008 | Atomic Commit vs small commit | Atomicity is semantic cohesion, not size. | — | P1 | RESOLVED |
| ENG-GAP-009 | Commit vs Integration Request | Commit is logical unit; IR is coherent deliverable/container. | — | P1 | RESOLVED |
| ENG-GAP-010 | Integration Request vs Workflow | IR is repository artifact/container, not orchestration. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-011 | IR lifecycle vs Quality state | IR lifecycle is mechanical only; Quality states/results external. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-012 | Engineering check vs Quality evidence | Module 06 binds checks to artifacts; UPOS-007 decides evidence sufficiency. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-013 | Mechanical mergeability vs Merge readiness | Mechanical state != Quality readiness. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-014 | Merge mechanics vs Merge authority | Mechanics Module 06; authority Module 02. | UPOS-002 | P0 | RESOLVED |
| ENG-GAP-015 | Merge authority vs Merge permission | Authority Module 02; capability grant Module 10. | UPOS-002/010 | P0 | RESOLVED |
| ENG-GAP-016 | History rewrite vs review validity | Module 06 emits artifact-change; UPOS-007 decides validity/re-review. | UPOS-007 | P1 | RESOLVED |
| ENG-GAP-017 | Engineering revert vs deployment rollback | Repository revert/backout only; deployment/data/business rollback external. | UPOS-004/operations/data | P0 | RESOLVED |
| ENG-GAP-018 | Repository collision vs Workflow dependency | Module 06 detects/reports engineering constraints; UPOS-004 sequences. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-019 | File collision vs semantic collision | Separate taxonomy; semantic collision may exist without file overlap. | — | P1 | RESOLVED |
| ENG-GAP-020 | Multi-repository engineering vs Workflow orchestration | RCU mechanics Module 06; overall order Module 04. | UPOS-004 | P0 | RESOLVED |
| ENG-GAP-021 | IR evidence container vs Quality evidence ownership | IR holds refs; UPOS-007 owns evidence/verdict semantics. | UPOS-007 | P0 | RESOLVED |
| ENG-GAP-022 | Engineering provenance vs Observability trace | Artifact relationships Module 06; events/traces Module 08. | UPOS-008 | P0 | RESOLVED |
| ENG-GAP-023 | Context provenance vs engineering provenance | Engineering provenance reuses frozen `context_request_id` / `context_bundle_id`; Context Manifest/source provenance remains UPOS-005. | UPOS-005 | P1-INTERFACE | RESOLVED |
| ENG-GAP-024 | Reviewer Context vs review artifact | Review artifact remains Module 06; Reviewer Context is independent UPOS-005 Context Request/Bundle; no `context_view_id` added. | UPOS-005 | P1-INTERFACE | RESOLVED |
| ENG-GAP-025 | Protected branch policy vs permission grants | Engineering protection requirement Module 06; grants Module 10. | UPOS-010/011 | P0 | RESOLVED |
| ENG-GAP-026 | Git semantics vs provider | Git-like VCS semantics normative; provider/API/bindings abstract. | UPOS-011 | P1 | RESOLVED |

> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Result

```text
UNRESOLVED INTERNAL P0/P1 MODULE-06 GAPS = 0
```

The two prior UPOS-005 interface gaps are resolved against FROZEN UPOS-005 v1.0.

No unresolved P0/P1 internal or interface gap remains for Module 06 v1.0 freeze.

===== END VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====


---

## VIRTUAL FILE 30/42 — `analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md`

**Virtual path:** `analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md`  
**Content checksum:** `beaa48d734e0`

===== BEGIN VIRTUAL FILE: analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md =====

# Branch / Workspace Model Analysis

**ID:** UPOS-06-AN-004  
**Type:** ANALYSIS / ISOLATION MODEL  
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

Frozen source preferred one task → one branch/worktree/sandbox, but universal Module 06 must support:

- multi-repository Tasks;
- multiple Agent Runs;
- direct-to-integration exceptions;
- provider-neutral workspaces;
- explicit writable-state isolation.

## Decision

Isolation boundary is Repository Change Unit + Workspace.

Default:

```text
concurrent writer A → workspace A
concurrent writer B → workspace B
```

Branch is a VCS relationship, not the workspace itself.

## Rejected assumptions

- one Task = one branch;
- branch = workspace;
- every change requires a branch + Integration Request;
- universal GitFlow;
- fixed branch names/prefixes.

## Direct mutation exception

Allowed only via explicit external policy/permission while preserving attribution/gates.

## Lifecycle

Workspace uses:

```text
ALLOCATED → ACTIVE → READ_ONLY → RELEASED
                     ↘ ABANDONED
```

No Workflow/Quality states are reused.

===== END VIRTUAL FILE: analysis/BRANCH_WORKSPACE_MODEL_ANALYSIS.md =====


---

## VIRTUAL FILE 31/42 — `analysis/COMMIT_ATOMICITY_ANALYSIS.md`

**Virtual path:** `analysis/COMMIT_ATOMICITY_ANALYSIS.md`  
**Content checksum:** `7d266a47266d`

===== BEGIN VIRTUAL FILE: analysis/COMMIT_ATOMICITY_ANALYSIS.md =====

# Commit Atomicity Analysis

**ID:** UPOS-06-AN-005  
**Type:** ANALYSIS / COMMIT MODEL  
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

## Source tension

Frozen source simultaneously prefers:

```text
small coherent commits
one commit = one logical change
```

and warns against:

```text
Git history as keystroke log
```

## Resolution

Atomicity is semantic, not numerical.

```text
atomic = one coherent engineering intent
```

Rejected universal proxies:

```text
one file
one action
one AI turn
fixed LOC threshold
one review comment
```

## Regression test decision

Do not universally require a red failing-test commit because some projects require green history.

Canonical rule:

```text
regression protection SHOULD exist before or with fix where practical
```

Both green combined commit and test→fix sequence can be valid under project policy.

## Commit identity

Use native `commit_ref`; no duplicate U-POS commit identifier.

===== END VIRTUAL FILE: analysis/COMMIT_ATOMICITY_ANALYSIS.md =====


---

## VIRTUAL FILE 32/42 — `analysis/CONCURRENCY_COLLISION_ANALYSIS.md`

**Virtual path:** `analysis/CONCURRENCY_COLLISION_ANALYSIS.md`  
**Content checksum:** `12ce033ccb7a`

===== BEGIN VIRTUAL FILE: analysis/CONCURRENCY_COLLISION_ANALYSIS.md =====

# Concurrency / Collision Analysis

**ID:** UPOS-06-AN-007  
**Type:** ANALYSIS / COLLISION MODEL  
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

## Finding

File overlap alone is insufficient.

Concurrent changes can merge textually yet conflict semantically, or touch different files while depending on an unresolved shared contract.

## Accepted taxonomy

```text
FILE_OVERLAP
DIFF_OVERLAP
SHARED_CONTRACT_DEPENDENCY
GENERATED_ARTIFACT_COLLISION
MIGRATION_ORDER_COLLISION
BRANCH_BASE_DIVERGENCE
SEMANTIC_INTEGRATION_COLLISION
```

## Engineering outputs

```text
SAFE_TO_PARALLELIZE
SERIALIZATION_REQUIRED
REBASE_REQUIRED
INTEGRATION_COORDINATION_REQUIRED
CONFLICT_PRESENT
```

UPOS-004 consumes these signals and owns orchestration.

## Isolation

No uncontrolled shared writable workspace for independent concurrent writers.

===== END VIRTUAL FILE: analysis/CONCURRENCY_COLLISION_ANALYSIS.md =====


---

## VIRTUAL FILE 33/42 — `analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md`

**Virtual path:** `analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md`  
**Content checksum:** `6c3aed33c6bd`

===== BEGIN VIRTUAL FILE: analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md =====

# Engineering Entity Model Analysis

**ID:** UPOS-06-AN-003  
**Type:** ANALYSIS / ENTITY MODEL  
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

## Accepted model

```text
Task                     [UPOS-004]
└── Engineering Change   [UPOS-006]
    ├── Repository Change Unit A
    │   ├── Workspace
    │   ├── Branch
    │   ├── Commit(s)
    │   ├── Integration Request
    │   └── Merge Operation → Integrated Revision
    └── Repository Change Unit B
        └── ...
```

## Identity decisions

Accepted semantic IDs:

```text
engineering_change_id
repository_change_unit_id
workspace_id
merge_operation_id
```

Native references retained:

```text
repository_ref
branch_ref
commit_ref
integration_request_ref
revision_ref
check_ref
tag_ref where used
```

## Rejected identity duplication

No `commit_id` replacement, no `branch_id`, no mandatory synthetic `integration_request_id` where a stable provider/VCS ref exists.

## Task/Workflow boundary

Engineering Change references upstream execution; it does not become a second Task.

Repository unit lifecycle does not become Workflow state.

## Result

Model is sufficient for one-repository, multi-repository, concurrent Agent, review, merge, and revert provenance.

===== END VIRTUAL FILE: analysis/ENGINEERING_ENTITY_MODEL_ANALYSIS.md =====


---

## VIRTUAL FILE 34/42 — `analysis/IMPLEMENTATION_PLAN.md`

**Virtual path:** `analysis/IMPLEMENTATION_PLAN.md`  
**Content checksum:** `0cb12ced2624`

===== BEGIN VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

# UPOS-006 Implementation Plan

**ID:** UPOS-06-AN-013  
**Type:** IMPLEMENTATION PLAN / EVIDENCE  
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

## Sequence

1. establish Module-06 boundary and entity model;
2. define Engineering Change and Repository Change Unit;
3. define workspace isolation and branch governance;
4. define atomic commit/provenance;
5. define Integration Request contract/lifecycle;
6. define engineering checks and artifact staleness;
7. define collision/concurrency and multi-repository mechanics;
8. define merge mechanics and ownership boundary;
9. define revert/backout and special artifacts;
10. define engineering provenance/failure/lifecycle;
11. add templates/cross-module interfaces;
12. complete provisional source traceability/validation;
13. wait for FROZEN UPOS-005;
14. perform narrow Context-interface reconciliation;
15. rerun validation before any `FROZEN v1.0` promotion.

## Expected logical commits

```text
docs(upos-006): establish engineering governance boundary
docs(upos-006): define engineering change and repository units
docs(upos-006): define workspace isolation and branch governance
docs(upos-006): define atomic commit and provenance standards
docs(upos-006): define integration request governance
docs(upos-006): define engineering checks and artifact staleness
docs(upos-006): define concurrency collision and multi-repo mechanics
docs(upos-006): define merge governance and integration mechanics
docs(upos-006): define revert and repository recovery semantics
docs(upos-006): define engineering provenance and failure model
docs(upos-006): add templates and cross-module interfaces
docs(upos-006): complete provisional traceability audit
```

Later only:

```text
docs(upos-006): reconcile context interfaces with upos-005
```

## Commit discipline

```text
one commit = one coherent logical change
```

The sequence is an implementation plan, not a substitute for actual repository history in this chat-generated artifact package.

===== END VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====


---

## VIRTUAL FILE 35/42 — `analysis/MERGE_BOUNDARY_ANALYSIS.md`

**Virtual path:** `analysis/MERGE_BOUNDARY_ANALYSIS.md`  
**Content checksum:** `34c3e5f32883`

===== BEGIN VIRTUAL FILE: analysis/MERGE_BOUNDARY_ANALYSIS.md =====

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

===== END VIRTUAL FILE: analysis/MERGE_BOUNDARY_ANALYSIS.md =====


---

## VIRTUAL FILE 36/42 — `analysis/MODULE_06_OWNERSHIP_MAP.md`

**Virtual path:** `analysis/MODULE_06_OWNERSHIP_MAP.md`  
**Content checksum:** `cbbee96a7fe1`

===== BEGIN VIRTUAL FILE: analysis/MODULE_06_OWNERSHIP_MAP.md =====

# Module 06 Ownership Map

**ID:** UPOS-06-AN-002  
**Type:** ANALYSIS / OWNERSHIP MAP  
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

## Module 06 owns

```text
Engineering Change
Repository Change Unit
Workspace isolation/lifecycle
Change Branch semantics
atomic commit/history integrity
Commit provenance
Integration Request mechanics/lifecycle
engineering check artifact binding
collision/concurrency constraints
multi-repository engineering mechanics
mechanical mergeability
Merge Operation mechanics
repository Revert/Backout
engineering provenance
engineering failure conditions
engineering artifact staleness
```

## Module 06 consumes without owning

| Interface | Owner |
|---|---|
| project truth, canonical docs, decisions | UPOS-01 |
| Role, Agent Run, authority, SoD, Merge Controller | UPOS-002 |
| Skill procedure/Skill Invocation semantics | UPOS-003 |
| Task, Workflow Instance, Stage, routing, rework orchestration | UPOS-004 |
| Context Bundle/View/provenance/freshness | UPOS-005 — pending |
| review/QA findings, evidence sufficiency, readiness verdict | UPOS-007 |
| events/traces/metrics/dashboard | UPOS-008 |
| organizational learning/promotion | UPOS-009 |
| permissions/protected actions/secrets | UPOS-010 |
| providers, paths, commands, naming, concrete policies | UPOS-011 |

## Boundary test

If the question is:

> Which repository artifact changed, where, from what base, by which bounded engineering unit, in which workspace/branch/commit/Integration Request, and how was it mechanically integrated/reverted?

→ UPOS-006.

If the question is:

> Should the work run now, who is authorized, is it correct, which Context is valid, may it be merged, or which provider command performs it?

→ another owning module.

===== END VIRTUAL FILE: analysis/MODULE_06_OWNERSHIP_MAP.md =====


---

## VIRTUAL FILE 37/42 — `analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md`

**Virtual path:** `analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md`  
**Content checksum:** `d36549dde98b`

===== BEGIN VIRTUAL FILE: analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md =====

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

===== END VIRTUAL FILE: analysis/PR_INTEGRATION_REQUEST_ANALYSIS.md =====


---

## VIRTUAL FILE 38/42 — `analysis/PROPOSED_PACKAGE_TREE.md`

**Virtual path:** `analysis/PROPOSED_PACKAGE_TREE.md`  
**Content checksum:** `bf75547bbadf`

===== BEGIN VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

# Proposed Package Tree

**ID:** UPOS-06-AN-012  
**Type:** ANALYSIS / PACKAGE DESIGN  
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


```text
06_engineering_governance/
├── README.md
├── ENGINEERING_GOVERNANCE_OPERATING_MODEL.md
├── ENGINEERING_CHANGE_MODEL.md
├── REPOSITORY_CHANGE_UNIT_STANDARD.md
├── REPOSITORY_WORKSPACE_AND_ISOLATION.md
├── BRANCH_GOVERNANCE.md
├── ATOMIC_COMMIT_STANDARD.md
├── COMMIT_PROVENANCE_STANDARD.md
├── INTEGRATION_REQUEST_STANDARD.md
├── INTEGRATION_REQUEST_LIFECYCLE.md
├── ENGINEERING_CHECK_INTEGRATION.md
├── CONCURRENCY_COLLISION_AND_CONFLICT.md
├── MULTI_REPOSITORY_CHANGE_MODEL.md
├── MERGE_GOVERNANCE.md
├── REVERT_BACKOUT_AND_RECOVERY.md
├── SPECIAL_REPOSITORY_ARTIFACTS.md
├── ENGINEERING_PROVENANCE_MODEL.md
├── ENGINEERING_FAILURE_MODEL.md
├── ENGINEERING_LIFECYCLE_AND_VERSIONING.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_06_DEFINITION_OF_DONE.md
├── MODULE_06_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── templates/
│   ├── ENGINEERING_CHANGE_TEMPLATE.md
│   ├── REPOSITORY_CHANGE_UNIT_TEMPLATE.md
│   ├── COMMIT_PROVENANCE_TEMPLATE.md
│   ├── INTEGRATION_REQUEST_TEMPLATE.md
│   ├── MERGE_OPERATION_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_06_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── ENGINEERING_ENTITY_MODEL_ANALYSIS.md
    ├── BRANCH_WORKSPACE_MODEL_ANALYSIS.md
    ├── COMMIT_ATOMICITY_ANALYSIS.md
    ├── PR_INTEGRATION_REQUEST_ANALYSIS.md
    ├── CONCURRENCY_COLLISION_ANALYSIS.md
    ├── MERGE_BOUNDARY_ANALYSIS.md
    ├── UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── TRACEABILITY_VALIDATION.md
```

`SPECIAL_REPOSITORY_ARTIFACTS.md` is retained because generated files, lockfiles, migration artifacts, and documentation-in-engineering-change have distinct frozen/directive semantics that would otherwise be scattered across unrelated standards.

===== END VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====


---

## VIRTUAL FILE 39/42 — `analysis/SOURCE_ANALYSIS.md`

**Virtual path:** `analysis/SOURCE_ANALYSIS.md`  
**Content checksum:** `798a758938df`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

# UPOS-006 Source Analysis

**ID:** UPOS-06-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
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

## Sources and authority

1. UPOS-01 Documentation System / Source-of-Truth / Knowledge Lifecycle — ACTIVE upstream governance.
2. UPOS-002 Agent Organization v1.0 — FROZEN organizational authority/SoD.
3. UPOS-003 Skills System v1.0 — FROZEN Skill contracts and engineering `INTERFACE_SKILL` references.
4. UPOS-004 Workflow Engine v1.0 — FROZEN Task/Workflow/Stage/routing/rework semantics and stable IDs.
5. UPOS-005 Context & Memory — IN DEVELOPMENT; noncanonical design signal only.
6. `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.0` — frozen master design input.
7. UPOS-006 implementation directive — Module-06 design/implementation authority for this branch.

## Main extraction result

Frozen master Engineering/Git/PR semantics are concentrated around:

```text
§3.7–3.10
§43–56
§57–59 (mixed)
§72
§81–84
§135–146 (mixed)
§154–164 (mixed)
§189–190
§197
§205–208 (mixed)
§218–220 (mixed)
§221.10
Appendix L
```

The Module-06 directive then materially refines these semantics with:

- Engineering Change / Repository Change Unit identities;
- provider-neutral Integration Request;
- Workspace isolation;
- multi-repository coordination;
- artifact staleness;
- mechanical mergeability boundary;
- Merge Operation identity;
- repository Revert/Backout;
- engineering provenance/failure taxonomy;
- provisional UPOS-005 reconciliation gate.

## P0 governance conflicts

None found against FROZEN UPOS-01–04.

## Critical boundaries confirmed

```text
Task / Workflow / rework orchestration → UPOS-004
Role / authority / Merge Controller    → UPOS-002
Skill procedure                         → UPOS-003
Context semantics                       → UPOS-005 pending
Quality verdicts/evidence sufficiency   → UPOS-007
Telemetry                               → UPOS-008
Permissions/protected actions           → UPOS-010
Provider/project wiring                 → UPOS-011
```

## Architecture decisions

1. Adopt `engineering_change_id`, `repository_change_unit_id`, `workspace_id`, `merge_operation_id`.
2. Do NOT create duplicate IDs for VCS/provider-native objects; use `branch_ref`, `commit_ref`, `integration_request_ref`, `revision_ref`, `check_ref`.
3. Use provider-neutral `Integration Request`; no hosting-provider ontology.
4. Preserve Git-like source-control assumption while keeping provider binding abstract.
5. Maintain small repository-mechanical lifecycles separate from Workflow/Quality states.
6. Treat Context references as placeholders only until FROZEN UPOS-005 reconciliation.

===== END VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====


---

## VIRTUAL FILE 40/42 — `analysis/SOURCE_SECTION_DISPOSITION.md`

**Virtual path:** `analysis/SOURCE_SECTION_DISPOSITION.md`  
**Content checksum:** `320cb82ef2c4`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

# Frozen Source Section Disposition

**ID:** UPOS-06-AN-011  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** ../MODULE_06_TRACEABILITY.md

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Rule

```text
EXTRACTED_TO_MODULE_06
MIXED_EXTRACTED_AND_DEFERRED
DEFERRED_TO_MODULE
OUTSIDE_MODULE_06
```

The table records top-level frozen-master disposition plus key engineering subsections.

| Source section | Title | Disposition | Destination |
|---|---|---|---|
| §0 | Executive model | MIXED_EXTRACTED_AND_DEFERRED | OTHER / owning U-POS module |
| §1 | Relationship to the Documentation Operating Model | DEFERRED_TO_MODULE | UPOS-01/11 |
| §2 | Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-01/11 |
| §3 | Foundational principles | MIXED_EXTRACTED_AND_DEFERRED | OTHER / owning U-POS module |
| §4 | Core terminology | DEFERRED_TO_MODULE | UPOS-002 |
| §5 | Universal Agent Contract | DEFERRED_TO_MODULE | UPOS-002 |
| §6 | Agent identity is not enough | DEFERRED_TO_MODULE | UPOS-002 |
| §7 | Universal role families | DEFERRED_TO_MODULE | UPOS-002 |
| §8 | Orchestrator | DEFERRED_TO_MODULE | UPOS-002 |
| §9 | Product Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §10 | Domain / Architecture Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §11 | UX / Product Design Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §12 | Design System Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §13 | Implementer Agent | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-002 |
| §14 | Reviewer Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §15 | QA Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §16 | Security Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §17 | Documentation Guardian | DEFERRED_TO_MODULE | UPOS-002 |
| §18 | Merge Controller | DEFERRED_TO_MODULE | UPOS-002 |
| §19 | Skills model | DEFERRED_TO_MODULE | UPOS-003 |
| §20 | Skill contract | DEFERRED_TO_MODULE | UPOS-003 |
| §21 | Example universal skills | DEFERRED_TO_MODULE | UPOS-003 |
| §22 | Workflow contract | DEFERRED_TO_MODULE | UPOS-004 |
| §23 | Change classification | DEFERRED_TO_MODULE | UPOS-004 |
| §24 | C0 — Micro | DEFERRED_TO_MODULE | UPOS-004 |
| §25 | C1 — Small | DEFERRED_TO_MODULE | UPOS-004 |
| §26 | C2 — Standard Feature | DEFERRED_TO_MODULE | UPOS-004 |
| §27 | C3 — Cross-cutting | DEFERRED_TO_MODULE | UPOS-004 |
| §28 | C4 — Architectural | DEFERRED_TO_MODULE | UPOS-004 |
| §29 | C5 — High-risk | DEFERRED_TO_MODULE | UPOS-004 |
| §30 | Risk override rule | DEFERRED_TO_MODULE | UPOS-004 |
| §31 | Context assembly | DEFERRED_TO_MODULE | UPOS-005 |
| §32 | Context assembly order | DEFERRED_TO_MODULE | UPOS-005 |
| §33 | Context budget principle | DEFERRED_TO_MODULE | UPOS-005 |
| §34 | Memory model | DEFERRED_TO_MODULE | UPOS-005 |
| §35 | Project memory sources | DEFERRED_TO_MODULE | UPOS-005 |
| §36 | Learning is not hidden model training | DEFERRED_TO_MODULE | UPOS-009/01 |
| §37 | Learning promotion model | DEFERRED_TO_MODULE | UPOS-009/01 |
| §38 | Permissions model | DEFERRED_TO_MODULE | UPOS-010 |
| §39 | Default role permission philosophy | DEFERRED_TO_MODULE | UPOS-002 |
| §40 | Human approval model | DEFERRED_TO_MODULE | UPOS-002 |
| §41 | Recommended adoption mode | DEFERRED_TO_MODULE | UPOS-002 |
| §42 | Planning model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §43 | Expected commits | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §44 | Git operating principles | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §45 | Atomic logical commits | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §46 | Bad commit granularity | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §47 | Bad oversized commit | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §48 | Commit categories | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §49 | Commit message contract | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §50 | Bug-fix commit strategy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §51 | Review-fix commits | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §52 | PR operating model | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §53 | Good PR | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §54 | Bad PR | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §55 | PR size policy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §56 | PR description contract | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §57 | Creation loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §58 | Verification loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §59 | Self-check | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §60 | Independent review protocol | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §61 | Review finding severity | DEFERRED_TO_MODULE | UPOS-007 |
| §62 | Review output contract | DEFERRED_TO_MODULE | UPOS-007 |
| §63 | Reviewer independence | DEFERRED_TO_MODULE | UPOS-007 |
| §64 | QA protocol | DEFERRED_TO_MODULE | UPOS-007 |
| §65 | QA dimensions | DEFERRED_TO_MODULE | UPOS-007 |
| §66 | Documentation gate | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §67 | Architecture gate | DEFERRED_TO_MODULE | UPOS-007 |
| §68 | Security gate | DEFERRED_TO_MODULE | UPOS-007 |
| §69 | Database migration gate | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §70 | Merge readiness | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §71 | Merge authority | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §72 | Merge strategy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §73 | Handoff protocol | DEFERRED_TO_MODULE | UPOS-002 |
| §74 | Handoff context minimization | DEFERRED_TO_MODULE | UPOS-002 |
| §75 | Guardrails | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §76 | Guardrail types | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §77 | Escalation model | DEFERRED_TO_MODULE | UPOS-002 |
| §78 | Escalation targets | DEFERRED_TO_MODULE | UPOS-002 |
| §79 | Failure and recovery | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §80 | Retry policy | DEFERRED_TO_MODULE | UPOS-004 |
| §81 | Scope Guardian | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §82 | Concurrency model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §83 | Task isolation | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §84 | Shared file collision | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §85 | Workflow — Micro Change | DEFERRED_TO_MODULE | UPOS-004 |
| §86 | Workflow — Bug Fix | DEFERRED_TO_MODULE | UPOS-004 |
| §87 | Workflow — New Feature | DEFERRED_TO_MODULE | UPOS-004 |
| §88 | Workflow — UI Change | DEFERRED_TO_MODULE | UPOS-004 |
| §89 | Workflow — Design System Change | DEFERRED_TO_MODULE | UPOS-004 |
| §90 | Workflow — Architecture Change | DEFERRED_TO_MODULE | UPOS-004 |
| §91 | Workflow — API Change | DEFERRED_TO_MODULE | UPOS-004 |
| §92 | Workflow — Database Migration | DEFERRED_TO_MODULE | UPOS-004 |
| §93 | Workflow — Security Change | DEFERRED_TO_MODULE | UPOS-004 |
| §94 | Workflow — Refactor | DEFERRED_TO_MODULE | UPOS-004 |
| §95 | Workflow — Dependency Upgrade | DEFERRED_TO_MODULE | UPOS-004 |
| §96 | Workflow — Hotfix | DEFERRED_TO_MODULE | UPOS-004 |
| §97 | Workflow — Documentation Change | DEFERRED_TO_MODULE | UPOS-004 |
| §98 | Workflow — Release | DEFERRED_TO_MODULE | UPOS-004 |
| §99 | Observability model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-008 |
| §100 | Dashboard-ready metrics | DEFERRED_TO_MODULE | UPOS-008 |
| §101 | Do not optimize for activity | DEFERRED_TO_MODULE | UPOS-008 |
| §102 | Quality metrics | DEFERRED_TO_MODULE | UPOS-008 |
| §103 | Agent performance | DEFERRED_TO_MODULE | UPOS-008 |
| §104 | Agent learning record | DEFERRED_TO_MODULE | UPOS-003 |
| §105 | Skill evolution | DEFERRED_TO_MODULE | UPOS-003 |
| §106 | Workflow evolution | DEFERRED_TO_MODULE | UPOS-009/01 |
| §107 | Agent contract evolution | DEFERRED_TO_MODULE | UPOS-009/01 |
| §108 | Model/provider independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §109 | Tool independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §110 | Safety around secrets | DEFERRED_TO_MODULE | UPOS-010 |
| §111 | Production access | DEFERRED_TO_MODULE | UPOS-010 |
| §112 | Protected files | DEFERRED_TO_MODULE | UPOS-010 |
| §113 | Definition of Ready — task | DEFERRED_TO_MODULE | UPOS-007 |
| §114 | Definition of Ready — agent execution | DEFERRED_TO_MODULE | UPOS-007 |
| §115 | Definition of Done — implementation | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §116 | Definition of Done — PR | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §117 | Definition of Done — workflow | DEFERRED_TO_MODULE | UPOS-007 |
| §118 | Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §119 | Maturity model | DEFERRED_TO_MODULE | UPOS-011 |
| §120 | Recommended adoption sequence | DEFERRED_TO_MODULE | UPOS-011 |
| §121 | Recommended first implementation | DEFERRED_TO_MODULE | UPOS-011 |
| §122 | Universal Orchestrator algorithm | DEFERRED_TO_MODULE | UPOS-004 |
| §123 | Authority conflict resolution | DEFERRED_TO_MODULE | UPOS-002 |
| §124 | Security veto | DEFERRED_TO_MODULE | UPOS-002 |
| §125 | Architecture veto | DEFERRED_TO_MODULE | UPOS-002 |
| §126 | Reviewer veto | DEFERRED_TO_MODULE | UPOS-002 |
| §127 | Human override | DEFERRED_TO_MODULE | UPOS-002 |
| §128 | Agent output discipline | DEFERRED_TO_MODULE | UPOS-002 |
| §129 | Change Classification output | DEFERRED_TO_MODULE | UPOS-004 |
| §130 | Implementation Plan output | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §131 | Review Result output | DEFERRED_TO_MODULE | UPOS-004 |
| §132 | QA Result output | DEFERRED_TO_MODULE | UPOS-004 |
| §133 | Merge Readiness output | DEFERRED_TO_MODULE | UPOS-004 |
| §134 | Change review feedback loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §135 | Oversized PR handling | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §136 | Scope expansion handling | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §137 | Unplanned architecture discovery | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §138 | Unplanned product ambiguity | DEFERRED_TO_MODULE | UPOS-004 |
| §139 | Unplanned security concern | DEFERRED_TO_MODULE | UPOS-004 |
| §140 | Documentation drift detection | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §141 | Agent sandbox hygiene | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §142 | Branch lifetime | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §143 | Stacked PRs | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §144 | Feature flags | DEFERRED_TO_MODULE | UPOS-011 |
| §145 | Rollback thinking | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §146 | Dependency graph awareness | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §147 | Cost awareness | DEFERRED_TO_MODULE | UPOS-008 |
| §148 | Latency awareness | DEFERRED_TO_MODULE | UPOS-008 |
| §149 | Human attention as scarce resource | DEFERRED_TO_MODULE | UPOS-008 |
| §150 | Agent communication rule | DEFERRED_TO_MODULE | UPOS-002 |
| §151 | Decision preservation | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §152 | No circular authority | DEFERRED_TO_MODULE | UPOS-002 |
| §153 | Independent model diversity | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §154 | Review freshness | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §155 | Merge queue compatibility | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §156 | CI as evidence provider | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §157 | Agent-specific test ownership | DEFERRED_TO_MODULE | UPOS-007 |
| §158 | Test integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §159 | Snapshot integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §160 | Security scanner integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §161 | Linter suppression | DEFERRED_TO_MODULE | UPOS-007 |
| §162 | Technical debt creation | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §163 | Technical debt review | DEFERRED_TO_MODULE | UPOS-009/01 |
| §164 | Post-merge verification | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §165 | Post-merge learning trigger | DEFERRED_TO_MODULE | UPOS-009/01 |
| §166 | Incident integration | DEFERRED_TO_MODULE | UPOS-009/01 |
| §167 | Dashboard model | DEFERRED_TO_MODULE | UPOS-008 |
| §168 | Agent workload | DEFERRED_TO_MODULE | UPOS-008 |
| §169 | Workflow bottleneck analysis | DEFERRED_TO_MODULE | UPOS-008 |
| §170 | Maturity gates for autonomy | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §171 | Autonomy expansion | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §172 | Project-specific overrides | DEFERRED_TO_MODULE | UPOS-011 |
| §173 | Universal vs project-specific rules | DEFERRED_TO_MODULE | UPOS-011 |
| §174 | Agent manifests should be versioned | DEFERRED_TO_MODULE | UPOS-011 |
| §175 | Governance change workflow | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §176 | Universal starter agent set | DEFERRED_TO_MODULE | UPOS-002 |
| §177 | Universal full agent set | DEFERRED_TO_MODULE | UPOS-002 |
| §178 | Agent composition | DEFERRED_TO_MODULE | UPOS-002 |
| §179 | Universal policy files | DEFERRED_TO_MODULE | UPOS-011 |
| §180 | AI Agent README | DEFERRED_TO_MODULE | UPOS-011 |
| §181 | Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | UPOS-011 |
| §182 | Universal file naming | DEFERRED_TO_MODULE | UPOS-011 |
| §183 | Agent contract versioning | DEFERRED_TO_MODULE | UPOS-002 |
| §184 | Skill versioning | DEFERRED_TO_MODULE | UPOS-003 |
| §185 | Workflow versioning | DEFERRED_TO_MODULE | UPOS-004 |
| §186 | Telemetry retention | DEFERRED_TO_MODULE | UPOS-008 |
| §187 | Sensitive context policy | DEFERRED_TO_MODULE | UPOS-005 |
| §188 | Secret redaction | DEFERRED_TO_MODULE | UPOS-010 |
| §189 | Auditability | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §190 | Reproducibility | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §191 | Agent hallucination handling | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §192 | Missing Source of Truth | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §193 | Stale Source of Truth | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §194 | Feature lifecycle integration | DEFERRED_TO_MODULE | UPOS-004 |
| §195 | Agent lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| §196 | Task lifecycle | DEFERRED_TO_MODULE | UPOS-004 |
| §197 | PR lifecycle | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §198 | Agent run lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| §199 | Workflow state machine | DEFERRED_TO_MODULE | UPOS-004 |
| §200 | No hidden background authority | DEFERRED_TO_MODULE | UPOS-002 |
| §201 | Human pause points | DEFERRED_TO_MODULE | UPOS-002 |
| §202 | Plan change protocol | DEFERRED_TO_MODULE | UPOS-004 |
| §203 | Reclassification | DEFERRED_TO_MODULE | UPOS-004 |
| §204 | Risk inheritance | DEFERRED_TO_MODULE | UPOS-004 |
| §205 | Change decomposition | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §206 | Multi-agent code ownership | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §207 | Shared contract first | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §208 | Reviewer context independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-005 |
| §209 | QA context independence | DEFERRED_TO_MODULE | UPOS-005 |
| §210 | Merge Controller context | DEFERRED_TO_MODULE | UPOS-002 |
| §211 | Product Owner context | DEFERRED_TO_MODULE | UPOS-002 |
| §212 | Decision packet | DEFERRED_TO_MODULE | UPOS-002 |
| §213 | Do not fake consensus | DEFERRED_TO_MODULE | UPOS-002 |
| §214 | Conflict resolution by authority | DEFERRED_TO_MODULE | UPOS-002 |
| §215 | Majority voting | DEFERRED_TO_MODULE | UPOS-002 |
| §216 | Agent confidence | DEFERRED_TO_MODULE | UPOS-002 |
| §217 | Evidence hierarchy | DEFERRED_TO_MODULE | UPOS-007 |
| §218 | Change evidence bundle | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §219 | Artifact retention | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §220 | Privacy of reasoning | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §221 | Universal anti-patterns | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §222 | Governance health checks | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §223 | Quarterly / milestone review | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §224 | Universal adoption checklist | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §225 | Minimal viable agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §226 | Intermediate agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §227 | Advanced agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §228 | Final operating model | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §3.7 | Small coherent changes | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit / IR standards |
| §3.8 | One PR, one intention | EXTRACTED_TO_MODULE_06 | UPOS-006 Integration Request Standard |
| §3.9 | One commit, one logical change | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit Standard |
| §3.10 | No opportunistic refactoring by default | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit / Engineering Change scope |
| §44.1 | No direct push to protected main | MIXED_EXTRACTED_AND_DEFERRED | engineering invariant → UPOS-006; grants/provider → UPOS-010/011 |
| §44.2 | One branch per coherent task | MIXED_EXTRACTED_AND_DEFERRED | normalized to RCU/branch semantics → UPOS-006; naming → UPOS-011 |
| §221.10 | Git history as keystroke log | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit Standard |
| Appendix L | Git Policy starter | MIXED_EXTRACTED_AND_DEFERRED | engineering mechanics → UPOS-006; authority/quality/provider portions deferred |

## Note

Mixed sections contribute only repository engineering mechanics to UPOS-006.
Role authority, Workflow orchestration, Context, Quality, Observability, Learning, Permissions, and provider bindings remain with their owners.

===== END VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====


---

## VIRTUAL FILE 41/42 — `analysis/TRACEABILITY_VALIDATION.md`

**Virtual path:** `analysis/TRACEABILITY_VALIDATION.md`  
**Content checksum:** `80e8c80d067d`

===== BEGIN VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====

# UPOS-006 Final Traceability Validation

**ID:** UPOS-06-AN-014  
**Type:** VALIDATION REPORT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this final validation evidence is found factually incorrect.  
**Related:** ../MODULE_06_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-006 v1.0 freeze validation. Current normative Engineering Governance semantics are owned by canonical Module-06 artifacts.

## Results

| Check | Result |
|---|---|
| Module-06 implementation-directive sections mapped | 110 / 110 |
| Frozen-master engineering requirements mapped | 45 |
| Frozen UPOS-005 reconciliation requirements mapped | 9 / 9 |
| UPOS-005 reconciliation items resolved | 9 / 9 |
| Required normative metadata conformance | PASS |
| Engineering Change template conforms to `ENGINEERING_CHANGE_MODEL.md` | PASS |
| Repository Change Unit template conforms to `REPOSITORY_CHANGE_UNIT_STANDARD.md` | PASS |
| Commit Provenance template conforms to `COMMIT_PROVENANCE_STANDARD.md` | PASS |
| Integration Request template conforms to `INTEGRATION_REQUEST_STANDARD.md` | PASS |
| Merge Operation template conforms to `MERGE_GOVERNANCE.md` | PASS |
| Analysis artifacts historical EVIDENCE | PASS |
| Active operational normative UPOS-005 pending markers | 0 |
| Historical pending/provisional wording confined to source quotations / archived evidence | PASS |
| Provisional metadata in normative layer | 0 |
| Stable `engineering_change_id` | PASS |
| Stable `repository_change_unit_id` | PASS |
| Stable `workspace_id` | PASS |
| Stable `merge_operation_id` | PASS |
| Stable upstream `context_request_id` reused | PASS |
| Stable upstream `context_bundle_id` reused | PASS |
| New `context_view_id` introduced | NO |
| Reviewer Context independence preserved | PASS |
| Rework Context revalidation interface | PASS |
| Artifact-change → Context revalidation interface | PASS |
| Immutable prior Bundle preserved across reassembly | PASS |
| Unknown referenced UPOS-003 Skill IDs | 0 |
| Hard-coded repository/provider/project paths | 0 |
| Unresolved internal/interface P0/P1 Module-06 gaps | 0 |
| Mechanical mergeability separated from approval/readiness | PASS |
| CI/check result separated from Quality verdict | PASS |
| Workflow state/retry/rework semantics remain UPOS-004 | PASS |
| Context validity/freshness/retrieval semantics remain UPOS-005 | PASS |
| Quality verdict/evidence semantics remain UPOS-007 | PASS |
| Permission grants/protected actions remain UPOS-010 | PASS |
| Provider/project bindings remain UPOS-011 | PASS |

```text
UNMAPPED MODULE-06 SOURCE REQUIREMENTS = 0
```

## Operational template conformance proof

Canonical operational templates were checked against their owning normative contracts:

```text
ENGINEERING_CHANGE_TEMPLATE.md       → PASS
REPOSITORY_CHANGE_UNIT_TEMPLATE.md  → PASS
COMMIT_PROVENANCE_TEMPLATE.md       → PASS
INTEGRATION_REQUEST_TEMPLATE.md     → PASS
MERGE_OPERATION_TEMPLATE.md         → PASS
```

The final cleanup corrected two concrete drifts discovered during freeze audit:

```text
COMMIT_PROVENANCE_TEMPLATE: added Routing Decision ID
ENGINEERING_CHANGE_TEMPLATE: added Affected Repository References
```

Active operational normative artifacts contain no unresolved `UPOS-005 pending` marker. Historical analysis and traceability may preserve original directive wording as explicitly historical evidence/source quotation.


## UPOS-005 reconciliation proof

Reconciled against FROZEN UPOS-005 Context & Memory v1.0:

```text
SHA-256
186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528
```

Canonical upstream identities reused:

```text
context_request_id
context_bundle_id
```

No additional Context View identity was created.

Reviewer Context:

```text
producer context
!= reviewer authoritative context
```

Rework / changed artifact:

```text
UPOS-006 reports exact changed artifact/revision
→ UPOS-005 revalidates prior Context Bundle
→ if reassembly is required:
   new context_bundle_id
→ old consumed Bundle remains immutable provenance
```

## Ownership validation

```text
UPOS-01 truth / documentation ownership       PASS
UPOS-002 Role / authority / SoD              PASS
UPOS-003 Skill procedure                     PASS
UPOS-004 Task / Workflow orchestration       PASS
UPOS-005 Context / Memory semantics          PASS — reconciled interface only
UPOS-007 Quality / evidence / verdict        PASS
UPOS-008 observability / telemetry           PASS
UPOS-009 learning                            PASS
UPOS-010 permissions / protected actions     PASS
UPOS-011 provider / path / command bindings  PASS
```

```text
NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 04 / 05 / 07–11
```

## Final status

```text
UPOS-006 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-005 INTERFACE RECONCILIATION:
COMPLETE

UPOS-006 FREEZE STATUS:
FROZEN v1.0
```

## Verdict

PASS — UPOS-006 Engineering Governance v1.0 satisfies final UPOS-005 interface reconciliation, source traceability, operational-template conformance, ownership-boundary, and freeze gates.

UPOS-006 Engineering Governance v1.0 — FROZEN.

===== END VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====


---

## VIRTUAL FILE 42/42 — `analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md`

**Virtual path:** `analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md`  
**Content checksum:** `4b0de85bdac7`

===== BEGIN VIRTUAL FILE: analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md =====

# UPOS-005 Interface Reconciliation Register

**ID:** UPOS-06-AN-009  
**Type:** INTERFACE RECONCILIATION REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if the frozen UPOS-005 interface or this recorded reconciliation is found factually incorrect  
**Related:** ../CROSS_MODULE_INTERFACES.md

> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Reconciliation result

```text
FROZEN UPOS-005 v1.0 supplied.
9 / 9 interface items reconciled.
Unresolved material compatibility issues = 0.
```

**Reconciled source SHA-256:** `186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528`

This register is historical reconciliation evidence. Current normative interface semantics live in Module-06 canonical documents.

## Dependencies

| ID | Module-06 location | Frozen UPOS-005 interface used | Final reconciliation | Status |
|---|---|---|---|---|
| CTX-REC-001 | `ENGINEERING_CHANGE_MODEL.md`; `templates/ENGINEERING_CHANGE_TEMPLATE.md` | `context_bundle_id`; optional `context_request_id`; Bundle attribution | Engineering Change references the actual Bundle(s) consumed; no local Context identity invented. | RESOLVED |
| CTX-REC-002 | `REPOSITORY_WORKSPACE_AND_ISOLATION.md` | Context View + Bundle attribution by Role/Agent Run | Workspace references assigned writer's `context_bundle_id`; no `context_view_id` introduced. | RESOLVED |
| CTX-REC-003 | `COMMIT_PROVENANCE_STANDARD.md`; template | immutable Context Bundle + Manifest provenance | Commit provenance references one or more `context_bundle_id`; Context provenance continues through Bundle/Manifest. | RESOLVED |
| CTX-REC-004 | `INTEGRATION_REQUEST_STANDARD.md`; template | Context Bundle, Bundle immutability, freshness/reassembly | IR records implementation/review Bundle IDs; artifact change is sent to UPOS-005 for revalidation rather than assigning Context state locally. | RESOLVED |
| CTX-REC-005 | `INTEGRATION_REQUEST_STANDARD.md` | Reviewer independence + Role-specific Context View | Review artifact remains Module 06; Reviewer receives independent UPOS-005 Request/Bundle and review provenance records reviewer `context_bundle_id`. | RESOLVED |
| CTX-REC-006 | `ENGINEERING_PROVENANCE_MODEL.md` | replay chain `Context Request → Context Bundle → sources/memory` | Provenance chain explicitly consumes `context_request_id` and `context_bundle_id`; no duplicate Context provenance object. | RESOLVED |
| CTX-REC-007 | `CROSS_MODULE_INTERFACES.md` | Module-05 Cross-Module Interface contract | Provides/consumes/MUST-NOT-redefine updated to frozen UPOS-005 semantics. | RESOLVED |
| CTX-REC-008 | `ENGINEERING_CHECK_INTEGRATION.md`; `MERGE_GOVERNANCE.md` | freshness/invalidation/reassembly on changed artifact | Module 06 emits exact artifact change; UPOS-005 decides Bundle validity and reassembly; new assembly gets new `context_bundle_id`. | RESOLVED |
| CTX-REC-009 | Module-06 rework interface | UPOS-005 `Rework Context` | Rework/re-review requires Context revalidation; Module 06 records old/new Bundle references while UPOS-005 owns reassembly/validity. | RESOLVED |


## Preserved ownership boundaries

Module 06 now reuses the frozen upstream identities:

```text
context_request_id
context_bundle_id
```

but still does NOT define:

```text
Context validity / freshness semantics
Context budget
Context isolation / Context View semantics
memory semantics
Reviewer Context contents
Implementer Context contents
Context source resolution / retrieval / assembly
```

No `context_view_id` was invented.

## Completion condition

```text
CTX-REC-001 … CTX-REC-009 = RESOLVED
UNRESOLVED MATERIAL COMPATIBILITY ISSUES = 0
```

The reconciliation gate is complete.

===== END VIRTUAL FILE: analysis/UPOS_005_INTERFACE_RECONCILIATION_REGISTER.md =====
