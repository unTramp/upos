# Memory Taxonomy

**ID:** UPOS-05-MTX-001  
**Type:** MEMORY TAXONOMY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Critical invariant

```text
MEMORY != TRUTH
```

Persistence, retrieval frequency, model confidence, or embedding similarity do not create canonicality.

## 2. RUN_WORKING_MEMORY

```text
RUN_WORKING_MEMORY
= ephemeral noncanonical execution support
  scoped to one Agent Run
```

May include:

- temporary notes;
- intermediate calculations;
- retrieval pointers;
- partial working artifacts.

Default: not persisted after the Run unless explicit policy requires retention.

## 3. TASK_WORKING_MEMORY

```text
TASK_WORKING_MEMORY
= bounded noncanonical operational memory
  retained across multiple Runs/Stages
  for one Task
```

May include:

- unresolved working questions;
- temporary artifact references;
- coordination notes;
- temporary mappings.

It MUST NOT duplicate UPOS-004 Workflow state.

## 4. RETRIEVAL_CACHE

```text
RETRIEVAL_CACHE
= optimization for previously retrieved/resolved information
```

Invariant:

```text
CACHE HAS ZERO ADDITIONAL AUTHORITY
```

Cache entries remain tied to source identity/version/scope/freshness and permission eligibility.

## 5. GOVERNED_PROJECT_MEMORY_VIEW

```text
GOVERNED_PROJECT_MEMORY_VIEW
= Context/Retrieval interface over knowledge governed by UPOS-01
```

It is not an independent Module-05 truth database.

Durable project truth remains in UPOS-01 governed sources.

## 6. Raw conversation history

```text
raw chat history != Project Memory
```

Conversation can contain Signal/Observation/Evidence/Hypothesis/Proposal candidates.

Durable truth requires governed capture/resolution/promotion.

## 7. Provider/model memory

```text
provider private memory
model latent memory
conversation personalization memory
```

MUST NOT be treated as canonical U-POS project knowledge.

If useful information exists only there:

```text
surface as candidate
→ verify
→ resolve canonical owner
→ govern through UPOS-01
```

## 8. No generic permanent memory bucket

UPOS-005 v1 intentionally rejects an undifferentiated persistent `memory` bucket.
