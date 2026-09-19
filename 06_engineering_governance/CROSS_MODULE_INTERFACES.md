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
