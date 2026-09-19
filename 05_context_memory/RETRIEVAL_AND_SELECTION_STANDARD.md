# Retrieval & Selection Standard

**ID:** UPOS-05-RSS-001  
**Type:** RETRIEVAL STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SOURCE_RESOLUTION_INTERFACE.md


## 1. Retrieval Candidate

A Retrieval Candidate is discovered information that has not yet been admitted to Context.

Candidate attributes SHOULD include:

```text
source_ref
source_class
canonical_owner_ref
normativity/status
source_version_or_revision
version_applicability
scope_applicability
project_applicability
freshness
permission_eligibility
epistemic_class_ref
relevance
representation_possibilities
provenance_sufficiency
```

## 2. Authority-aware order

Retrieval MUST NOT be pure semantic similarity search.

Conceptual order:

```text
1. bounded request and scope
2. UPOS-01 canonical owner/source resolution
3. UPOS-010 permission/security constraints
4. UPOS-011 physical retrieval/provider mapping
5. project/scope/version/lifecycle eligibility
6. freshness/applicability assessment
7. epistemic/normativity preservation
8. relevance ranking among eligible candidates
9. required/optional obligation handling
10. budget/representation optimization
```

Invariant:

```text
HIGH RELEVANCE
MUST NOT OVERRIDE
LOWER AUTHORITY
```

## 3. Source eligibility gate

Candidate may be ineligible due to:

```text
wrong project
wrong scope
wrong version/baseline
superseded/retired status
permission denied
stale beyond applicable policy
canonical conflict
not applicable to current Stage/Role/Skill
insufficient provenance
```

Ineligible material MUST NOT silently enter Context because search returned it.

## 4. Relevance ranking

Relevance is applied only inside an eligible authority envelope.

Relevance MAY consider:

- direct Task/Stage/Skill relation;
- affected domain/component;
- decision applicability;
- implementation surface;
- evidence recency where applicable;
- historical similarity when explicitly useful.

It MUST NOT convert a lower-authority candidate into normative truth.

## 5. Knowledge retrieval priority consumed from UPOS-01

Default background order:

```text
1. Active canonical sources
2. Accepted relevant decisions
3. Validated active learnings
4. Current plan
5. Recent relevant evidence
6. Historical material
7. Raw/unreviewed notes
```

This order is not a substitute for fact-scope ownership or Context requiredness.

## 6. Incremental / just-in-time retrieval

UPOS-005 supports:

```text
initial minimal Bundle
+
bounded follow-up Context Request
```

Do not front-load an entire repository merely because it is accessible.

## 7. Explainability

For a material inclusion/exclusion, the system SHOULD be able to explain:

- why source was eligible;
- why included;
- why excluded;
- why representation was summary/reference/excerpt;
- why historical material was used;
- why Bundle was rebuilt.

Opaque similarity rank alone is insufficient.

## 8. Provider retrieval failure

Provider/search failure MUST be surfaced as technical retrieval failure.

It MUST NOT be interpreted as proof that project knowledge does not exist.
