# Time and Duration Semantics

**ID:** UPOS-08-TIM-001  
**Type:** TIME MEASUREMENT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Event time dimensions

```text
occurred_at
= best available timestamp of the underlying observed occurrence

recorded_at
= timestamp the Event record was created/emitted by the producer

ingested_at
= timestamp the collector/Event Store accepted the Event, when available
```

Do not assume equality.

## 2. Timestamp quality

Canonical v1:

```text
EXACT
APPROXIMATE
UNKNOWN
```

Optional `time_source_ref` may identify provider/runtime clock source.

Clock synchronization/implementation belongs to UPOS-011.

## 3. Clock skew

Negative/impossible distributed elapsed intervals based only on wall clocks MUST NOT be silently clamped to zero.

They produce:

```text
CLOCK_SKEW_SUSPECTED
```

and affected derived duration becomes `UNKNOWN`/`INCOMPLETE` unless an explicit measured monotonic duration exists.

## 4. Measured duration

Where runtime directly measures a bounded operation duration using a monotonic source, that explicit measured duration is preferred over subtracting distributed wall-clock timestamps.

The chosen basis MUST be reproducible/documented by the Metric/Span contract.

## 5. Lead time != cycle time

```text
LEAD TIME
!=
CYCLE TIME
```

### Task lead time

Canonical v1 Task Lead Time:

```text
start = occurred_at of the owner-observed Task creation / entry into UPOS-004 NEW
end   = occurred_at of the owner-observed terminal Task state DONE or CANCELLED
```

If creation/NEW entry is not observed under the required capture contract, value is not derivable as zero.

`CANCELLED` SHOULD be dimensioned separately from successfully completed Tasks when aggregating.

### Workflow cycle time

Canonical v1 Workflow Cycle Time:

```text
start = occurred_at of first UPOS-004 Workflow Instance transition READY → RUNNING
end   = occurred_at of terminal Workflow Instance state
        COMPLETED / FAILED / CANCELLED / SUPERSEDED
```

This elapsed cycle includes pauses/blocks after execution started.

## 6. Active execution time

For Workflow-level active execution:

```text
active_execution_time
= wall-clock union of intervals where the Workflow Instance is in RUNNING
```

Use interval union, not naive sum of parallel Stage/Span durations.

## 7. Blocked time

```text
blocked_time
= wall-clock union of intervals where UPOS-004 Workflow Instance is in BLOCKED
```

Stage-specific blocked time may be measured separately.

## 8. Paused time

`PAUSED` and `BLOCKED` are distinct UPOS-004 states and MUST remain distinct metric dimensions when both are observed.

## 9. Queue/wait time

Universal UPOS-004 does not define a generic queue lifecycle.

Therefore canonical queue/wait metrics require explicit queue/wait boundary signals from a runtime/provider/owner interface.

Without them:

```text
queue_time = UNKNOWN / N/A
```

Do not infer queue time from inactivity.

## 10. Human wait vs human work

```text
human_wait_time
!=
human_active_work_time
```

Human active work duration requires explicit instrumentation or governed source evidence.

Elapsed time between two system Events MUST NOT automatically be labeled human work.

## 11. Rework time

UPOS-004 owns Rework semantics.

Robust universal metric:

```text
rework_count
= count of explicit owner-observed rework-entry occurrences/episodes
```

`rework_time` is canonical only when an owner/runtime interface supplies bounded rework episode boundaries or rerun-stage attribution sufficient to avoid mixing rework wait with execution.

Otherwise it remains conditional/UNKNOWN.

## 12. Retry time

Retry metrics use explicit owner/runtime retry relations.

Repeated tool calls or repeated similar Events MUST NOT be inferred as Retry without an explicit retry relation/reason.

## 13. Interval overlap

For parallel execution, metrics MUST specify whether they use:

```text
elapsed wall-clock union
sum of actor/resource durations
sum of provider billable durations
```

These are different measurements and MUST NOT be mixed.
