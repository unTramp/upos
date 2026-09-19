# Review Result Standard

**ID:** UPOS-07-RRS-001  
**Type:** REVIEW RESULT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_ASSESSMENT_STANDARD.md, INDEPENDENT_VERIFICATION.md


## 1. Review Result representation

A Review Result is a `QualityAssessment` with:

```text
assessment_type = DIFF_REVIEW
```

or, when applicable:

```text
assessment_type = ARCHITECTURE_REVIEW
```

It has no separate `review_result_id`.

## 2. Diff review expectations

Review evaluates the exact UPOS-006 target/diff state against applicable governed criteria.

It may address:

- correctness;
- requirement/scope conformance;
- architecture/domain constraints;
- testing/regression evidence;
- documentation;
- maintainability;
- UX/accessibility where criteria exist;
- external Security result references where required.

## 3. Independent review

A required Final Review MUST satisfy UPOS-002 independence rules and `INDEPENDENT_VERIFICATION.md`.

Implementer self-check cannot replace required independent Review.

## 4. Review findings

A Reviewer produces structured Findings with criterion/evidence references.

Vague preference is not a blocking Finding.

## 5. Re-review

Default semantic relationship:

```text
Finding
→ engineering rework
→ exact target changes
→ evidence applicability re-evaluated
→ new RE_REVIEW/DELTA_REVIEW Assessment
```

Old Review Assessment remains immutable.

## 6. Provider neutrality

Quality Review does not encode GitHub/GitLab provider approval states.

UPOS-011 adapters may map Quality results into provider mechanics without changing semantics.
