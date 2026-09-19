# Retrieval Authority Analysis

**ID:** UPOS-05-AN-005  
**Type:** ANALYSIS / RETRIEVAL AUTHORITY  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Rejected model

```text
semantic similarity
→ highest score
→ treat as authoritative
```

Rejected because relevance is not authority.

## Adopted order

```text
1. bounded request/scope
2. UPOS-01 fact-scope + canonical-owner/source resolution
3. UPOS-010 permission/security constraints
4. UPOS-011 physical retrieval/provider mapping
5. project/scope/version/lifecycle eligibility
6. freshness/applicability assessment
7. epistemic/normativity preservation
8. relevance ranking within eligible candidates
9. required/optional obligation handling
10. budget/representation optimization
11. Context Manifest + Bundle
```

Invariant:

```text
HIGH RELEVANCE
MUST NOT OVERRIDE
LOWER AUTHORITY
```

## Required vs optional

`REQUIRED/OPTIONAL` is an obligation axis.

Context priority is a separate selection axis.

A required source cannot be removed simply because an optional item scores as more relevant.

## Source-not-found distinction

```text
SOURCE_NOT_FOUND
= retrieval/resolution attempt did not find the source

SOURCE_DOES_NOT_EXIST
= absence is established by canonical owner/source governance
```

The first MUST NOT be silently converted into the second.

## Retrieval technology

No vector database/search backend/model is canonicalized by Module 05.
