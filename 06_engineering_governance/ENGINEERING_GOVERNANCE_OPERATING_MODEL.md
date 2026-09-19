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
