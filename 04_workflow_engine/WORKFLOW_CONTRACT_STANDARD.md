# Workflow Contract Standard

**ID:** UPOS-04-WCS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/WORKFLOW_CONTRACT_TEMPLATE.md


## 1. Requirement

Every production Base Workflow and Profile MUST have a versioned contract.

## 2. Base Workflow mandatory fields

```text
Identity
Purpose
Version
Lifecycle status

Applicability
Work Types
Allowed / required Change Classes
Concern compatibility

Entry Conditions
Required Source Classes
Context Interface Requirements

Roles
Role Participation
Separation-of-Duties Constraints

Skills
Skill Version / compatibility references

Stages
Stage dependencies
Stage entry conditions
Stage outputs
Stage exit conditions

Transitions
Transition conditions

Handoffs

External Gate References
Human Approval References
Security/Permission References

Reclassification Triggers
Rerouting Rules

Failure Modes
Retry Rules
Recovery Rules
Rework Loops

Pause / Block / Resume
Escalation

Cancellation
Completion Criteria
Terminal Outcomes

Observability Interface Requirements

Lifecycle
Version
Supersession
```

## 3. Roles

Workflow references canonical Role identities from UPOS-002.

It MUST NOT copy Agent Contracts.

## 4. Skills

Workflow references stable Skill IDs/versions from UPOS-003.

It MUST NOT copy Skill procedures.

## 5. Sources/context

Workflow may declare Required Source Classes and Context interface needs.

UPOS-005/01 resolve/assemble truth.

No physical project path belongs in the universal Workflow contract.

## 6. Gates

Workflow owns whether an external gate/result is required at a stage.

Workflow does not own the gate's internal evidence/verdict semantics.

## 7. Approvals

Workflow may require a Human/Security/Permission approval reference.

Authority/grant semantics remain external.

## 8. Stages

A Stage is a bounded orchestration phase.

A Stage contract MUST identify:

- stable `stage_id`;
- participating Roles;
- Skill references;
- dependencies;
- entry conditions;
- expected orchestration outputs;
- exit conditions;
- external gates;
- allowed rework/retry behavior.

A Stage display name MUST NOT be used as the Stage identity.

A canonical `stage_id` MUST remain stable within the Workflow/Profile lineage unless the Stage is semantically replaced.

Resolved Profile-added stages MUST also remain independently addressable and MUST NOT collide with Base Workflow stage identities.

## 9. Transitions

Only declared transitions are legal in automated/reference execution.

Every declared Transition MUST have a stable:

```text
transition_id
```

or an explicitly specified deterministic stable identifier equivalent.

`transition_id` identifies the transition rule, not a display phrase.

Transitions MUST be condition-driven, not implicit narrative jumps.

## 10. Terminal outcomes

Canonical terminal Workflow Result classes:

```text
COMPLETED
FAILED
CANCELLED
ESCALATED_TERMINAL
SUPERSEDED_BY_REROUTE
```

Project/runtime schemas may encode these later through the cross-cutting schemas layer.
