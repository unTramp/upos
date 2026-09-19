# Memory Lifecycle & Invalidation

**ID:** UPOS-05-MLI-001  
**Type:** MEMORY LIFECYCLE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Memory item states

Canonical execution-support states:

```text
ACTIVE
STALE
EXPIRED
INVALIDATED
ARCHIVED
```

These states are not UPOS-01 Knowledge Lifecycle states.

## 2. Lifetime classes

Canonical semantic lifetime classes:

```text
RUN
TASK
TTL_BOUND
UNTIL_INVALIDATED
GOVERNED_REFERENCE
```

Actual data retention/security deletion requirements remain external.

## 3. RUN lifetime

Valid only for the originating Agent Run unless explicitly captured/promoted through governed interfaces.

## 4. TASK lifetime

Valid only inside the originating Task subject to freshness/scope/permission rules.

At Task completion, active reuse ends. Retention may archive or expire according to policy.

## 5. TTL_BOUND

Validity expires at an externally configured time/condition.

Expiry is not proof the underlying project fact is false.

## 6. UNTIL_INVALIDATED

May remain active until a declared invalidation trigger occurs.

No indefinite authority is implied.

## 7. GOVERNED_REFERENCE

Pointer/view relationship to UPOS-01 governed knowledge.

The referenced source lifecycle governs knowledge validity; Module-05 memory state only governs the reference/view usability.

## 8. Invalidation triggers

Memory becomes stale/expired/invalidated where applicable when:

- underlying source is superseded/retired/revised;
- Task/Run scope ends;
- Task scope materially changes;
- assumption is invalidated;
- Workflow reroutes/reclassifies materially;
- permission eligibility changes;
- TTL expires;
- canonical conflict appears;
- project/baseline/version applicability changes.

## 9. Invalidated memory

May remain historically attributable when allowed, but MUST NOT silently feed active Context.

## 10. Retrieval Cache invalidation

Cache must invalidate/revalidate against source version, scope, freshness and permission changes.

A cached copy MUST NOT override current source resolution.
