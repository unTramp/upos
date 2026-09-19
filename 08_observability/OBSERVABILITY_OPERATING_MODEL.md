# Observability Operating Model

**ID:** UPOS-08-OOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Mission

UPOS-008 makes U-POS execution reconstructable, measurable and explainable without creating a second execution authority or Source of Truth.

Its responsibility is:

```text
OBSERVE
CORRELATE
MEASURE
EXPLAIN
PROJECT
```

not:

```text
OWN DOMAIN TRUTH
ORCHESTRATE
AUTHORIZE
GRANT PERMISSION
DECIDE QUALITY
PROMOTE LEARNING
BIND PROVIDERS
```

## 2. Ownership

UPOS-008 owns:

- Observability Event semantics and envelope;
- Event identity, timestamp, producer/initiator attribution and correction semantics;
- correlation, explicit causation and ordering semantics;
- Trace/Span semantics and propagation interface;
- telemetry capture classes, sampling constraints and payload minimization;
- Event Store semantic requirements and observational replay;
- telemetry data-quality and Observability-health semantics;
- Metric Definition, Metric Observation and metric derivation semantics;
- duration/latency/wait/block measurement semantics;
- cost/resource-usage attribution semantics;
- capacity/workload/human-attention observational semantics;
- audit/provenance projections;
- rebuildable Control Plane read-model semantics;
- Observability lifecycle/versioning;
- cross-module Observability interfaces and traceability.

## 3. Non-ownership

| Concern | Canonical owner |
|---|---|
| project truth, fact ownership, knowledge lifecycle | UPOS-01 |
| Roles, authority, SoD, Human Governance | UPOS-002 |
| Skill procedure/result semantics | UPOS-003 |
| Task/Workflow/Stage states, routing, retry/rework/recovery | UPOS-004 |
| Context/Memory validity, freshness, provenance | UPOS-005 |
| repository/Git/check/merge mechanics | UPOS-006 |
| Quality Evidence/Finding/Verdict/Gate/readiness semantics | UPOS-007 |
| Learning Candidate/pattern interpretation/promotion | UPOS-009 |
| permissions/security/sensitive-data/retention policy | UPOS-010 |
| concrete provider/storage/exporter/clock/pricing/project bindings | UPOS-011 |

## 4. Observation does not create truth

An Event may reliably say that a component observed or emitted a domain result reference.

It does not thereby become the owner of that result.

```text
quality.assessment.completed event
→ proves the event was observed/emitted
→ points to quality_assessment_id

quality_assessment_id semantics/current truth
→ remain UPOS-007
```

## 5. Event history is not canonical current state

```text
latest observed event
!= automatically canonical current domain state
```

Reasons include:

- dropped Events;
- late Events;
- retention;
- projection lag;
- externally changed owner state;
- corrected telemetry;
- instrumentation defects.

Current-state projections MUST expose freshness/completeness and reconcile to owner state where authoritative current state is required.

## 6. Producer, initiator and owner are distinct

```text
producer
= component that creates/emits the Observability Event

initiator
= actor/system occurrence that initiated the underlying action where known

domain owner
= UPOS module owning the underlying semantic fact/entity
```

They MAY be the same, but MUST NOT be assumed equal.

Example:

```text
Git provider webhook adapter (producer)
observes merge performed by Merge Controller run (initiator/actor)
for Merge Operation owned by UPOS-006 (domain owner)
```

## 7. Minimal telemetry principle

Capture enough to reconstruct governed execution and measurements, but prefer references over copied artifacts.

```text
IDs + versions + reason/result refs + small structured attributes
>
raw prompts / whole diffs / full Context Bundles / credentials / private reasoning
```

## 8. Hidden reasoning prohibition

```text
OBSERVABILITY MUST NOT REQUIRE HIDDEN CHAIN-OF-THOUGHT CAPTURE
```

Allowed alternatives:

- explicit decision/result reference;
- governed reason code;
- criterion/evidence reference;
- user-visible rationale where policy permits;
- output artifact reference.

## 9. Balanced system measurement

Operational evaluation SHOULD preserve multiple axes:

```text
SPEED
+
QUALITY
+
COST
+
HUMAN ATTENTION
+
GOVERNANCE
```

No single axis is a universal score.

## 10. No metric-driven self-modification

```text
metric changed
→ observation / evidence
→ possible UPOS-009 input
→ governed proposal
→ owner-module version change
```

A metric MUST NOT directly rewrite Workflow, Skill, Quality Policy, permission policy, or canonical knowledge.
