# Trace / Correlation Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Resolution

```text
Trace = bounded causally coherent execution narrative
Correlation = broader grouping across one/many traces
Causation = explicit direct triggering relation
```

One Task/Workflow may contain multiple Traces.

Span parent relation is a single-parent acyclic hierarchy. Complex fan-in dependencies use Event causation/domain relations instead of multi-parent Span graphs.

Causation can cross Trace boundaries.

No global total order is introduced.
