# Task and Workflow Instance Model

**ID:** UPOS-04-TWI-001  
**Type:** STATE / INSTANCE MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Task

Task / Change Request is the work entering U-POS.

Task lifecycle is orchestration-facing and distinct from product feature lifecycle, Agent Run lifecycle, PR lifecycle, and Skill Invocation state.

Normalized Task states:

```text
NEW
CLASSIFIED
ROUTED
IN_PROGRESS
BLOCKED
DONE
CANCELLED
```

`IN_REVIEW`, `IN_QA`, and `READY_TO_MERGE` from the frozen-source suggested lifecycle are treated as stage-specific projections for applicable code workflows, not universal Task states for documentation/release workflows.

## 2. Stable Task identity

Every Task / Change Request MUST have a stable:

```text
task_id
```

`task_id` identifies the Task across classification, routing, Workflow Instances, reroutes, rework, and later provenance.

It is not a display title and MUST NOT change merely because the Task title/description changes.

This is a semantic identity requirement only; machine representation belongs to the cross-cutting schemas/runtime layer.

## 3. Workflow Definition vs Instance

```text
WORKFLOW DEFINITION
= durable versioned orchestration contract

WORKFLOW INSTANCE
= one execution of one Workflow Definition/version
  for one Task/Change
```

## 4. Stable Workflow Instance identity and attribution

Every Workflow Instance MUST have a stable:

```text
workflow_instance_id
```

A Workflow Instance MUST be attributable to:

```text
workflow_instance_id
workflow_definition_id
workflow_version
task_id
routing_decision_id
change_class
work_type
concerns / profile refs
current workflow state
current stage(s)
required roles
required skill refs
external gate refs
approval refs
```

## 5. Workflow Instance is not project truth

Workflow Instance state is operational orchestration state.

It MUST NOT be interpreted as canonical Product/Domain/Architecture truth.

## 6. Runtime representation

Exact persistence/event/schema implementation is outside Module 04.

Module 04 owns the semantic fields/states; runtime/observability encode them later.
