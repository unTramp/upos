# Source Resolution Interface

**ID:** UPOS-05-SRI-001  
**Type:** UPSTREAM INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01 Source-of-Truth Model


## 1. Ownership boundary

UPOS-005 consumes UPOS-01 source resolution.

It MUST NOT decide by itself:

- who owns a fact;
- which source is canonical;
- which normative source wins;
- whether knowledge is promoted;
- whether a conflict is resolved.

## 2. Required conceptual flow

```text
Context Request
↓
resolve_scope(task / requested fact scope)
↓
resolve_canonical_owner(scope)
↓
resolve_active_canonical_sources(owner, request)
↓
resolve relevant accepted decisions/refinements
↓
check baseline/version applicability
↓
UPOS-005 retrieval/eligibility/assembly
```

## 3. UPOS-01 algorithm consumed

Module 05 must preserve the upstream logic:

```text
fact scope
→ canonical owner
→ ACTIVE normative sources
→ relevant accepted decisions
→ valid local refinement
→ version/baseline applicability
→ implementation evidence
→ conflict / UNKNOWN when unresolved
```

## 4. Source resolution output expectations

UPOS-005 expects resolution references sufficient to identify:

```text
fact_scope
canonical_owner_ref
canonical_source_refs
source status/normativity
decision/refinement refs
version/baseline applicability
known conflict status
known UNKNOWN / OWNER DECISION REQUIRED status
```

Exact machine structure is cross-cutting schemas/runtime.

## 5. Missing owner/source

If UPOS-01 reports no canonical owner/source:

```text
do not infer truth
do not promote nearest note
do not treat implementation as intended policy
```

Module 05 emits a Context failure/result that UPOS-004 can route.

## 6. Canonical conflict

If active normative sources conflict, Module 05 MUST NOT:

- average them;
- vote between them;
- pick newest blindly;
- choose highest embedding similarity;
- synthesize a compromise as truth.

Result is a Context conflict condition.

Truth resolution remains with UPOS-01/owner.

## 7. Implementation evidence

Implementation/code/tests/runtime artifacts may show what currently happens.

They remain implementation evidence and MUST NOT silently override confirmed normative sources.

Drift should remain visible.

## 8. Historical material

Historical/superseded/retired material MAY be included for explicit historical relevance only.

Its status MUST remain visible in Context.

## 9. Source not found vs source does not exist

```text
SOURCE_NOT_FOUND
= retrieval/resolution attempt did not locate expected material

SOURCE_DOES_NOT_EXIST
= absence has been established by canonical governance/owner resolution
```

Retrieval failure is not proof of nonexistence.
