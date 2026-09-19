# Delivery Metrics

**ID:** UPOS-08-DEL-SET-001  
**Type:** METRIC DEFINITIONS  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability

## OBS-MET-DEL-001 — task_lead_time

**Disposition:** `CANONICAL_V1`

```text
definition: Elapsed time from owner-observed Task creation/entry into UPOS-004 NEW to terminal Task state.
measurement_type: DURATION
source: owner-observed UPOS-004 Task lifecycle Events/state refs
population: Tasks with observed start and terminal boundary
window: TASK_LIFETIME
formula: terminal occurred_at - Task NEW/create occurred_at
dimensions: project, Change Class, Work Type, Workflow, terminal outcome
unknown handling: missing boundary → INCOMPLETE/UNKNOWN; never zero
limitations: Includes queue/wait/block after Task arrival; does not measure active work.
```

## OBS-MET-DEL-002 — workflow_cycle_time

**Disposition:** `CANONICAL_V1`

```text
definition: Elapsed execution-cycle time from first READY→RUNNING to terminal Workflow Instance state.
measurement_type: DURATION
source: UPOS-004 Workflow Instance state-transition Events/refs
population: Workflow Instances with observed start and terminal boundary
window: WORKFLOW_LIFETIME
formula: terminal occurred_at - first READY→RUNNING occurred_at
dimensions: project, Change Class, Work Type, Workflow Definition/version, terminal outcome
unknown handling: missing boundary → INCOMPLETE/UNKNOWN
limitations: Includes pauses/blocks after execution begins; not active execution time.
```

## OBS-MET-DEL-003 — workflow_active_execution_time

**Disposition:** `CANONICAL_V1`

```text
definition: Wall-clock union of intervals where the Workflow Instance is in UPOS-004 RUNNING.
measurement_type: DURATION
source: UPOS-004 Workflow Instance state-transition Events/refs
population: Workflow Instances with sufficient RUNNING transition telemetry
window: WORKFLOW_LIFETIME
formula: union(duration of RUNNING state intervals)
dimensions: project, Change Class, Workflow Definition/version
unknown handling: missing state transitions → INCOMPLETE
limitations: Uses interval union to avoid double-counting parallel Stages; not resource-seconds.
```

## OBS-MET-DEL-004 — workflow_blocked_time

**Disposition:** `CANONICAL_V1`

```text
definition: Wall-clock union of intervals where the Workflow Instance is in UPOS-004 BLOCKED.
measurement_type: DURATION
source: UPOS-004 Workflow Instance state-transition Events/refs
population: Workflow Instances with sufficient BLOCKED transition telemetry
window: WORKFLOW_LIFETIME
formula: union(duration of BLOCKED state intervals)
dimensions: project, Change Class, Workflow Definition/version, blocker owner/category where governed
unknown handling: incomplete transition sequence → INCOMPLETE
limitations: PAUSED is not BLOCKED and must not be included.
```

## OBS-MET-DEL-005 — workflow_rework_entry_count

**Disposition:** `CANONICAL_V1`

```text
definition: Count explicit UPOS-004 rework-entry occurrences for a Workflow Instance/cohort.
measurement_type: COUNTER
source: transitions into REWORK_REQUIRED or governed rework occurrence refs
population: Workflow Instances in selected cohort
window: WORKFLOW_LIFETIME or FIXED_INTERVAL cohort
formula: count(explicit rework-entry occurrences)
dimensions: project, Change Class, Workflow Definition/version
unknown handling: missing required rework transition telemetry → INCOMPLETE
limitations: Does not equal reviewer comments, commits, or repeated tool calls.
```

## OBS-MET-DEL-006 — workflow_retry_count

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Count explicit retry attempts/relations declared by UPOS-004/runtime.
measurement_type: COUNTER
source: explicit owner/runtime retry relation/Event
population: bounded operation or Workflow cohort with retry instrumentation
window: WORKFLOW_LIFETIME or FIXED_INTERVAL
formula: count(explicit retry occurrences)
dimensions: project, Workflow, failure class, operation type
unknown handling: no retry instrumentation → UNKNOWN
limitations: Retry != rework; repeated calls are not inferred as Retry.
```

## OBS-MET-DEL-007 — queue_wait_time

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Elapsed time in an explicitly modeled runtime/provider queue.
measurement_type: DURATION
source: explicit queue-entry and queue-exit/start signals from UPOS-011/runtime/provider
population: queued work items with both boundaries
window: bounded queue episode
formula: queue_exit_or_execution_start - queue_entry
dimensions: project, provider binding, queue class, Role/operation where governed
unknown handling: no explicit queue lifecycle → N/A/UNKNOWN
limitations: Inactivity is not evidence of queuing.
```

## OBS-MET-DEL-008 — review_execution_duration

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Active execution duration of one independent Review Assessment cycle.
measurement_type: DURATION
source: Review execution Span correlated to UPOS-007 review quality_assessment_id
population: DIFF_REVIEW / ARCHITECTURE_REVIEW cycles with explicit execution start/end
window: bounded review Span
formula: measured review Span duration, otherwise valid bounded start/end duration
dimensions: project, Change Class, assessment_type, assessment_cycle_kind, Role, Agent Definition/version
unknown handling: no Review execution Span/boundaries → UNKNOWN
limitations: Execution duration != waiting-for-review time; comments do not define review boundaries.
```

## OBS-MET-DEL-009 — qa_execution_duration

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Active execution duration of one QA validation cycle.
measurement_type: DURATION
source: QA execution Span correlated to UPOS-007 QA_VALIDATION quality_assessment_id
population: QA validation cycles with explicit execution start/end
window: bounded QA Span
formula: measured QA Span duration
dimensions: project, Change Class, assessment_cycle_kind, Role, Agent Definition/version
unknown handling: no QA execution Span → UNKNOWN
limitations: Excludes queue/wait unless separately instrumented.
```

## OBS-MET-DEL-010 — merge_latency

**Disposition:** `CONDITIONAL_INTERFACE`

```text
definition: Elapsed time from current applicable merge-quality readiness for the exact engineering target to UPOS-006 Merge Operation occurrence.
measurement_type: DURATION
source: UPOS-007 MERGE_QUALITY_READINESS/Gate refs + exact UPOS-006 target/head + Merge Operation Event
population: integrated changes with current readiness result matching the exact integrated target state
window: bounded readiness-to-merge interval
formula: merge_operation.occurred_at - applicable readiness.assessed_at/evaluated_at
dimensions: project, Change Class, repository, Workflow, readiness result type
unknown handling: no matching exact-target readiness boundary or changed head → UNKNOWN/N/A
limitations: Includes downstream authority/permission/Human/provider wait; not pure mechanical merge execution.
```
