# Workflow — release

**ID:** WFL-RELEASE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-RELEASE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `RELEASE`

## Purpose

Orchestrate release of a selected release candidate through required external operational/security/human checkpoints.

## Applicability

**Allowed / required Change Classes:** C2–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- release candidate identified
- required release/operations sources resolvable
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- DevOps / SRE or project release specialist
- QA
- Security when relevant
- Human approval reference
- Documentation Guardian as relevant

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-PREPARE-RELEASE`
- `SKL-QA-VALIDATION`
- `SKL-REVIEW-SECURITY (conditional)`
- `SKL-RECONCILE-DOCUMENTATION (conditional)`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-RELEASE:PREPARE` | release specialist | `SKL-PREPARE-RELEASE` | release package/readiness gaps identified |
| `WFL-RELEASE:EXTERNAL_GATES` | relevant Roles | `referenced external quality/security/operations interfaces` | required external gate results available |
| `WFL-RELEASE:HUMAN_CHECKPOINT` | Human authority by reference | `no Skill; approval interface` | required human approval exists |
| `WFL-RELEASE:DEPLOYMENT` | authorized operational Role | `external protected-action/tool interface` | deployment outcome available |
| `WFL-RELEASE:VERIFY` | QA/operations | `SKL-QA-VALIDATION` | post-release verification available |
| `WFL-RELEASE:ROLLBACK_OR_COMPLETE` | operations/orchestrator | `external rollback/recovery interface if needed` | terminal release result reached |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-RELEASE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-RELEASE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-RELEASE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-RELEASE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-RELEASE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-RELEASE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Release candidate reaches completed/rolled-back terminal outcome with required verification and approvals.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.
