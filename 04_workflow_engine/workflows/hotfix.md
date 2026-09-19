# Workflow — hotfix

**ID:** WFL-HOTFIX  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-HOTFIX`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `HOTFIX`

## Purpose

Orchestrate expedited recovery without treating urgency as permission to skip safety.

## Applicability

**Allowed / required Change Classes:** C1–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- active incident/urgent regression established
- minimal recovery intention defined
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Merge Controller
- Human approval reference as externally required

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

- `SKL-ANALYZE-INCIDENT`
- `SKL-REPRODUCE-BUG (where possible)`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-PREPARE-RELEASE`
- `SKL-ASSESS-MERGE-READINESS`
- `SKL-CAPTURE-LEARNING (follow-up candidate)`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-HOTFIX:INCIDENT_CONTEXT` | relevant incident Role | `SKL-ANALYZE-INCIDENT` | incident scope/evidence established |
| `WFL-HOTFIX:MINIMAL_PLAN` | Implementer | `SKL-CREATE-IMPLEMENTATION-PLAN` | minimal safe fix plan exists |
| `WFL-HOTFIX:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | minimal fix produced |
| `WFL-HOTFIX:EXPEDITED_REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | independent review result available |
| `WFL-HOTFIX:FOCUSED_QA` | QA | `SKL-QA-VALIDATION` | focused validation available |
| `WFL-HOTFIX:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | required approval/readiness references resolved |
| `WFL-HOTFIX:RELEASE_PREP` | DevOps/SRE or release role | `SKL-PREPARE-RELEASE` | release preparation complete if applicable |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-HOTFIX:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-HOTFIX:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-HOTFIX:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-HOTFIX:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-HOTFIX:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-HOTFIX:TR-COMPLETE` | successful final required stage → `COMPLETED` |

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

Recovery change is safely ready/released according to external policy; follow-up debt/learning may be emitted separately.

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
