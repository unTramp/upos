# Evidence Sufficiency & Freshness

**ID:** UPOS-07-ESF-001  
**Type:** EVIDENCE SUFFICIENCY / FRESHNESS STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Existence != sufficiency

```text
evidence exists
!=
evidence is sufficient
```

Criterion-level sufficiency states:

```text
SUFFICIENT
INSUFFICIENT
NOT_APPLICABLE
UNKNOWN
```

## 2. Sufficiency dimensions

Sufficiency MUST consider, as applicable:

```text
criterion
exact target state
scope/coverage
freshness
independence requirement
producer/provenance
reliability
method applicability
required evidence classes
relevant limitations
```

Evidence quantity alone is not a sufficiency measure.

## 3. Freshness states

Evidence applicability/freshness state:

```text
CURRENT
STALE
INVALIDATED
UNKNOWN
```

The captured Evidence Record content remains historically attributable even if later freshness state changes.

## 4. Staleness triggers

Evidence must be revalidated when relevant:

- target revision/head/base changes;
- rebase changes commit identities/content;
- diff/change set materially changes;
- criteria/source/policy version changes;
- UPOS-005 Context invalidation changes evaluation assumptions;
- test environment becomes invalid for the claim;
- external dependency/contract changes materially;
- required independence becomes invalid.

UPOS-006 reports engineering artifact changes.

UPOS-005 reports Context validity changes.

UPOS-007 determines Quality evidence applicability/staleness consequences.

## 5. Reuse test

Before reuse:

```text
same criterion?
same or demonstrably equivalent target?
same relevant assumptions?
fresh?
required independence preserved?
provenance valid?
coverage still sufficient?
```

If not, rerun/review/revalidate.

`it passed earlier` is not a reuse rule.

## 6. Delta review

`DELTA_REVIEW` is a bounded Assessment cycle kind.

Delta review is permitted only when:

- changed target can be precisely identified;
- prior evidence remains applicable for unchanged portions;
- all criteria affected by the delta are re-evaluated;
- independence requirements remain satisfied;
- limitations are recorded.

Diff size alone is not sufficient justification.

## 7. Target change consequence

When target changes:

```text
old Evidence/Assessment remains historical
→ applicability is re-evaluated
→ stale/invalidated elements identified
→ new/revalidated Assessment created as needed
```

No historical result is silently overwritten.

## 8. Evidence-class neutrality

No evidence class universally dominates all others.

```text
code review alone
!= proof of runtime behavior

runtime test alone
!= proof of architecture conformance
```

The applicable Criterion determines which evidence class or combination is sufficient.
