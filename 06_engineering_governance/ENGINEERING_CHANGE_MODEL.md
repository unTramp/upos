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
