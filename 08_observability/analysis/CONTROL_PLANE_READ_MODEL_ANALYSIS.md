# Control Plane Read Model Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Model

Control Plane is a consumer of rebuildable projections, not a database of domain truth.

Every read model needs freshness/coverage metadata.

Actions must call owner-module interfaces.

## Core views

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
```

Learnings/Security views wait for UPOS-009/010.

## Projection drift

Current-state read models should reconcile with owner snapshots. Owner wins; `PROJECTION_DRIFT` is observable health evidence.
