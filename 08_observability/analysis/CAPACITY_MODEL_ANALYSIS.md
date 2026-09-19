# Capacity Model Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Resolution

Capacity is system execution capacity, not human-style utilization.

Robust facts:

- currently running runs where lifecycle instrumentation exists;
- blocked Workflow state from UPOS-004;
- observed active durations;
- explicit queue occupancy/wait when runtime emits queue boundaries.

## Avoided false metrics

- observed maximum concurrency is not configured capacity;
- inactivity is not proof of queuing;
- busy ratio is not productivity;
- elapsed Human wait is not Human work effort.

Saturation therefore remains conditional on real capacity denominator from UPOS-011/runtime/project binding.
