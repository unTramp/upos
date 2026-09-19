# Quality Policy Standard

**ID:** UPOS-07-QPS-001  
**Type:** POLICY INTERFACE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_CRITERIA_STANDARD.md


## 1. Purpose

A Quality Policy defines reusable Quality expectations without becoming Workflow orchestration.

It may specify by Change Class, Work Type, Concern, target class, or governed project scope:

- required Criteria Sets;
- required evidence classes;
- independence requirements;
- assessment-type requirements;
- evidence freshness expectations;
- specialist/external result references;
- allowed exception policy references;
- readiness/gate constraints.

## 2. Identity/version reference

Assessments and Gate Results MUST record:

```text
quality_policy_ref
quality_policy_version
```

If no separate project Quality Policy exists, the operational record MUST reference the applicable UPOS-007/default governed policy source rather than leave the semantic basis implicit.

## 3. Ownership

Universal Quality semantics are UPOS-007-owned.

Concrete project-specific thresholds and matrices remain governed project knowledge under UPOS-01 and are bound by UPOS-011.

## 4. Quality Policy != Workflow Profile

```text
Quality Policy
= criteria/evidence/independence expectations

Workflow Profile
= orchestration stages/roles/gates/timing
```

A Quality Policy MUST NOT schedule a Stage or assign Role authority.

## 5. Version changes

Material change to required criteria/evidence/independence requires a new governed policy version.

Historical Assessments remain linked to the version actually used.

## 6. No silent tightening/loosening

Runtime/adapters MUST NOT silently alter Quality Policy semantics.

Provider capability limits must be surfaced as inability/blocked evidence, not hidden policy change.
