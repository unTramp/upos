# Module 09 Cross-Module Interfaces

**ID:** UPOS-09-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-009 provides**
- validated Learning Candidates;
- Improvement Proposals;
- evidence/root-cause/validation/outcome refs;
- promotion recommendations.

**Consumes**
- canonical owner/source resolution;
- knowledge classes/lifecycle;
- proposal/review/decision/promotion/supersession semantics.

**MUST NOT redefine**
- canonical truth, promotion, source authority, knowledge activation/supersession.

## UPOS-002 — Agent Organization

**Provides**
- evidence-backed organizational/Agent Contract improvement candidates.

**Consumes**
- Role/Agent Definition/Agent Run identities;
- authority/delegation/Human Governance;
- owner/reviewer authority references.

**MUST NOT redefine**
- Role authority, approval, veto, human governance.

## UPOS-003 — Skills System

**Provides**
- Skill improvement proposals;
- Skill-effectiveness evidence/outcomes.

**Consumes**
- Skill IDs/versions;
- Skill invocation/result refs;
- Skill evolution interface.

**MUST NOT redefine**
- Skill procedure/lifecycle/version semantics.

## UPOS-004 — Workflow Engine

**Provides**
- Workflow/routing/rework/retry improvement proposals/pattern evidence.

**Consumes**
- Workflow IDs/versions/instances;
- Stage/transition refs;
- retry/rework/reclassification/rerouting refs.

**MUST NOT redefine**
- Workflow state/routing/retry/rework semantics.

## UPOS-005 — Context & Memory

**Provides**
- Context policy/selection/memory improvement candidates.

**Consumes**
- Context Bundle IDs/policy versions;
- Context failure/invalidation refs.

**MUST NOT redefine**
- retrieval, Context freshness, Memory semantics.

## UPOS-006 — Engineering Governance

**Provides**
- engineering-governance improvement candidates.

**Consumes**
- engineering change/RCU/commit/IR/revert/collision/merge-conflict refs.

**MUST NOT redefine**
- branch/commit/merge/collision mechanics.

## UPOS-007 — Quality System

**Provides**
- Quality-policy/criterion/gate improvement proposals as noncanonical owner-routed proposals.

**Consumes**
- Findings;
- Quality Assessments;
- Gate Results;
- exceptions/waivers;
- first-pass/re-review Quality semantics.

**MUST NOT redefine**
- Finding severity/status, Evidence/Assessment/Verdict/Gate/Readiness semantics.

## UPOS-008 — Observability

**Provides**
- attributable `event_id` and `trace_id` references;
- Metric Observation value records linked to stable `metric_definition_id`;
- version/cohort comparison inputs;
- retry/rework/recurrence observations;
- cost/time/quality/human-attention measurements;
- data completeness/coverage metadata.

Metric Observation has no global `metric_observation_id`.

**UPOS-009 consumes**
- those Observability records as Learning evidence only.

**UPOS-009 provides**
- `pattern_candidate_id`;
- `learning_candidate_id`;
- `root_cause_assessment_id`;
- `improvement_proposal_id`;
- `validation_plan_id`;
- `learning_outcome_id`;

which UPOS-008 may observe/correlate by reference.

**MUST NOT define**
- Event/Trace/Span identity or schema;
- metric formulas;
- telemetry storage/retention;
- Control Plane projection semantics.

Status: `RECONCILED`.

## UPOS-010 — Security & Permissions

UPOS-009 may consume, as attributable Learning evidence:

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
security_policy_ref/version
owner reason/result refs
break-glass/elevation outcome refs
```

Examples of signals include repeated denials/exceptions, repeated missing approvals, frequent break-glass use, over-broad or long-lived Grants and protected-action failures.

UPOS-009 MUST NOT define Security severity, Permission Decision, Grant, secrets policy, veto, exception or protected-action authority and MUST NOT mutate Security Policy directly.

Sensitive Learning artifacts consume UPOS-010 access/minimization constraints.

Status: `RECONCILED`.

## UPOS-011 — Project Adapter

UPOS-011 may bind:

```text
learning evidence source refs
project learning policy refs
project-specific threshold values backed by governed source refs
artifact locations
validation environments
canonical owner routing refs
optional project backlog mapping
security/access refs for Learning artifacts
```

UPOS-009 remains owner of Pattern, Root Cause, Learning Candidate, Proposal, Validation and Outcome semantics.

Status: `RECONCILED`.

## Cross-cutting schemas layer

Future machine-readable schemas MAY encode Module-09 records.

Schemas MUST trace to these normative Markdown semantics and MUST NOT create an independent Learning truth model.
