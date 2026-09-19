# Quality Lifecycle & Versioning

**ID:** UPOS-07-QLV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Criteria Set / Gate Definition lifecycle

```text
DRAFT
REVIEW
APPROVED
ACTIVE
DEPRECATED
RETIRED
```

Definition lifecycle is distinct from Assessment/Gate Result.

## 2. Definition versioning

Material semantic change to:

- criterion applicability;
- required evidence;
- acceptable verdict;
- independence requirement;
- gate blocking condition;
- exception eligibility;
- source/policy mapping

requires a new version.

Editorial change may use patch-level versioning without changing meaning.

## 3. Assessment lifecycle

```text
OPEN
EVALUATING
COMPLETED
CANCELLED
```

Verdict is separate.

Completed Assessment payload is immutable.

## 4. Gate Result lifecycle

A Gate Result is an immutable completed evaluation snapshot for an exact target state.

A target/policy/criteria change produces a new result.

## 5. Evidence lifecycle

Evidence capture content remains immutable.

Its Quality applicability/freshness can later become:

```text
CURRENT
STALE
INVALIDATED
UNKNOWN
```

Historical record is preserved.

## 6. Finding lifecycle

Defined in `FINDING_STANDARD.md`.

A Finding may change disposition through a verified later Assessment/exception link without rewriting the historical Assessment that created it.

## 7. Exception lifecycle

Defined in `QUALITY_EXCEPTION_AND_WAIVER.md`.

## 8. Historical policy

Historical Assessment is not silently reevaluated under today's policy.

Its original verdict remains a statement of what the then-applicable evidence supported within its scope.

## 9. Escaped defects

A post-acceptance defect/regression MAY be linked to historical Quality artifacts.

It MUST NOT retroactively rewrite a historical PASS into a different past verdict.

Historical PASS means the evidence available at that time supported PASS for that exact target/scope/criteria/policy.

The escaped defect becomes new evidence for UPOS-008/009 and possible revalidation/learning.
