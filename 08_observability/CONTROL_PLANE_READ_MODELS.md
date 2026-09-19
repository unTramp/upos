# Control Plane Read Models

**ID:** UPOS-08-CPR-001  
**Type:** READ MODEL STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Fundamental rule

```text
CONTROL PLANE != SOURCE OF TRUTH
READ MODEL != CANONICAL STATE
```

Read Models are rebuildable operational projections.

## 2. Projection metadata

Every materialized operational Read Model SHOULD expose where applicable:

```text
projection_definition_ref
projection_definition_version
source_coverage_state
data_revision
projection_watermark
last_updated_at
projection_lag
known_limitations
```

No global `read_model_row_id` is required by v1.

## 3. Rebuildability

Read Models SHOULD be rebuildable from retained Events plus authoritative owner snapshots/refs required by the projection definition.

Deleting/corrupting projection storage MUST NOT mutate canonical owner state.

## 4. Eventual consistency

Read Models MAY be eventually consistent.

The UI must expose freshness/lag rather than imply instantaneous canonical consistency.

## 5. Owner reconciliation

If a current-state Read Model conflicts with authoritative owner state:

```text
owner state wins
projection marks PROJECTION_DRIFT
projection is recomputed/reconciled
```

## 6. Canonical v1 Read Model families

```text
SYSTEM_OVERVIEW
WORK_TASKS
TASK_TIMELINE
AGENTS
TRACES
QUALITY
GOVERNANCE
COSTS
AUDIT_PROVENANCE
SYSTEM_HEALTH
LEARNINGS
SECURITY
```

## 7. System Overview

May show factual projected counts/statuses such as:

```text
active work
running workflows/runs
blocked work
review/QA activity
human action pending
integration activity
```

Labels must be traceable to upstream owner states/events.

## 8. Task Timeline

Should correlate:

```text
Task creation/classification/routing
Workflow/Stage transitions
Context assembly
Agent Runs / Skills
Engineering artifacts
Review/QA/Findings/Rework
Gate Results
Merge Operations
```

Each item SHOULD retain timestamp, actor/initiator, causation and owner result refs.

## 9. Agent View

Must not conflate:

```text
Role
Agent Definition
Agent Instance reference
Agent Run
```

May show current/recent Runs, durations, waits, blocked states, cost/usage, retries and downstream Quality outcomes with scope/sample limitations.

## 10. Trace View

Supports Trace → Span tree/forest plus cross-trace/cause links, durations, errors, usage and domain refs.

## 11. Quality View

Uses UPOS-007 Assessments/Verdicts/Findings/Gate Results/Exceptions/readiness and cycle kinds.

It MUST NOT reduce Quality to CI/Git status.

## 12. Governance View

May project reclassification/rerouting/escalation/Human Governance/exception/conflict/protected-action references without owning them.

## 13. Costs View

May aggregate cost by Task, Workflow, Role, Agent Run, Skill, provider and integrated change when source data/price basis is complete.

## 14. Audit/Provenance View

Provides navigable identity/causal chain and source completeness.

## 15. System Health View

Shows Observability/runtime health signals such as ingestion lag, trace completeness, schema rejection, projection lag and metric freshness.

## 16. Explainability

A Control Plane indicator should have enough metadata to answer:

```text
why is this work blocked?
why is this run waiting?
why did this metric change?
why did this Gate fail?
why did cost increase?
```

Only through real references/formulas; not generated causal stories without evidence.

## 17. Control Plane actions

A future button/action MUST call the proper owner-domain interface.

Example:

```text
Approve action
→ UPOS-002/010 governed command/interface
```

It MUST NOT mutate projection storage as a substitute for domain action.

## 18. Dashboard metric transparency

Every canonical metric shown should expose:

```text
definition
formula
population
window
dimensions
sample size
data freshness/completeness
limitations
```

## 19. Learnings View

May project UPOS-009-owned references and statuses such as:

```text
pattern_candidate_id
learning_candidate_id
root_cause_assessment_id
improvement_proposal_id
validation_plan_id
learning_outcome_id
canonical owner / target refs
supporting event/metric/evidence refs
```

The projection MUST NOT promote Learning, decide root cause, mutate target artifacts, or become canonical Learning state. Owner state wins projection conflicts.

## 20. Security View

May project UPOS-010-owned references such as:

```text
permission_request_id
permission_decision_id
decision / reason code
grant_id + lifecycle state ref
protected_action_id + status/outcome ref
security_exception_id + lifecycle/use ref
security_policy_ref/version
subject/resource/capability/action refs
break-glass/elevation refs
```

Raw secrets and protected payload content MUST NOT be exposed. Visibility and redaction follow UPOS-010 constraints; concrete enforcement/query bindings belong UPOS-011.
