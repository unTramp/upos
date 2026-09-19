# Quality Verdict Standard

**ID:** UPOS-07-QVS-001  
**Type:** VERDICT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Canonical verdicts

```text
PASS
FAIL
BLOCKED
INCONCLUSIVE
```

No `PASS_WITH_WARNINGS` in v1.

Non-blocking limitations/advisory Findings coexist with `PASS`.

## 2. PASS

`PASS` means:

- all REQUIRED applicable criteria in the Assessment scope are `SATISFIED`;
- required evidence is `SUFFICIENT` and acceptably fresh;
- required independence is satisfied;
- no unresolved `BLOCKING` Finding applies, unless a valid governed exception explicitly makes the affected requirement acceptable;
- required external quality-related references are satisfied as required by the criteria/gate;
- unknowns do not undermine required criteria.

```text
PASS = scoped PASS
```

It does not claim the whole system is bug-free.

## 3. FAIL

`FAIL` means one or more REQUIRED applicable criteria are demonstrably `UNSATISFIED`.

A valid open BLOCKING Finding normally implies FAIL for the affected required condition unless the Assessment itself cannot complete due to a more fundamental prerequisite problem.

## 4. BLOCKED

`BLOCKED` means the Assessment cannot validly proceed/complete because a required prerequisite is unavailable or prohibited, such as:

- authoritative criterion unresolved;
- required Context unavailable;
- required permission/evidence unavailable;
- external required gate/result unresolved;
- exact target unavailable.

`BLOCKED` is not evidence that the target is bad.

## 5. INCONCLUSIVE

`INCONCLUSIVE` means evaluation was materially attempted but available evidence is insufficient, unreliable, conflicting, stale, or ambiguous such that neither PASS nor FAIL is supported.

Unknown MUST NOT be converted into PASS.

## 6. CI green

```text
CI_GREEN != QUALITY_PASS
```

CI green means configured checks passed.

It proves only claims actually covered by applicable fresh evidence.

CI green does NOT by itself prove:

```text
requirements complete
architecture correct
no regression exists
UX correct
security safe
acceptance criteria satisfied
```

## 7. No-findings rule

```text
NO_FINDINGS != PROOF_OF_CORRECTNESS
```

An Assessment with no Findings may still be `INCONCLUSIVE` or `BLOCKED` if criteria/evidence were not sufficiently evaluated.
