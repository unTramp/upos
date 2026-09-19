# Correlation, Causation and Ordering

**ID:** UPOS-08-CCO-001  
**Type:** RELATION / ORDERING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Correlation

```text
CORRELATION
= membership in the same broader operational conversation/group
```

`correlation_id` may connect multiple Traces associated with one Task/Workflow/change or cross-provider execution.

Correlation does not prove causation.

## 2. Causation

```text
CAUSATION
= explicit direct triggering relationship between observed occurrences
```

`causation_event_id` points to the direct predecessor Event when known.

## 3. Causation basis

Canonical v1:

```text
EXPLICIT_PRODUCER_LINK
EXPLICIT_DOMAIN_RELATION
RECONSTRUCTED_FROM_GOVERNED_RELATION
UNKNOWN
N/A
```

`RECONSTRUCTED_FROM_GOVERNED_RELATION` is allowed only when an upstream owner relation deterministically establishes the dependency.

Temporal proximity, correlation membership or statistical association alone MUST NOT be labeled direct causation.

## 4. Unknown causation

If direct cause cannot be established:

```text
causation_event_id = UNKNOWN / N/A
causation_basis = UNKNOWN
```

Do not invent a causal chain to make the timeline look complete.

## 5. Causation graph

Direct causal Event edges MUST be acyclic.

A detected cycle is telemetry-integrity failure:

```text
CAUSATION_CYCLE
```

and MUST NOT be silently broken by arbitrary timestamp order.

## 6. Trace-local parent relation

A Span has at most one `parent_span_id` in the v1 trace-parent model.

Parent relations MUST be acyclic.

Fan-in / multi-dependency semantics should be represented through Event causation/related domain refs rather than multiple span parents.

## 7. No global total order

U-POS Observability does not define a single global sequence across distributed producers.

Preferred ordering sources:

```text
1. explicit causation
2. span parent/child ordering
3. trace-local sequence where emitted
4. owner-domain transition/version/sequence refs
5. occurred_at as temporal evidence
6. recorded_at / ingested_at as collection evidence
```

Wall-clock timestamps alone are insufficient to prove semantic order.

## 8. Same timestamp

Equal timestamps do not imply simultaneity or order.

Ordering must remain partial unless stronger evidence exists.

## 9. Correlation scope

`correlation_id` SHOULD be stable for the intended grouping scope but SHOULD NOT become an unbounded project-wide bucket.

A Task may have one or multiple correlation groups depending on runtime boundaries.

## 10. Cross-trace causation

Causation MAY cross Trace boundaries.

A cross-trace causal edge does not require merging both Traces into one.
