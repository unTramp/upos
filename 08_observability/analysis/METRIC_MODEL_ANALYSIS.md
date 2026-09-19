# Metric Model Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Metric Definition

Receives stable ID/version/lifecycle because formula/population/window semantics are durable governance.

## Metric Observation

No global ID. Semantic tuple addressability avoids identity explosion.

## Metric dispositions

```text
CANONICAL_V1
CONDITIONAL_INTERFACE
DEFERRED
```

This prevents dashboard convenience from turning weak proxies into canonical KPIs.

## Key safeguards

- zero != unknown/no-data/incomplete;
- every rate has exact denominator/population/window;
- sample size preserved;
- percentiles versioned as part of Definition;
- late data creates new data revision/recompute time;
- current UI formula cannot be hidden;
- high-cardinality IDs remain trace refs by default rather than metric labels.

## Boundary metrics

Queue, review/QA execution and saturation require explicit runtime/Span/capacity signals. They are conditional rather than approximated from inactivity/comment timestamps.
