# Governed Project Memory Interface

**ID:** UPOS-05-PMI-001  
**Type:** PROJECT MEMORY INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01 Knowledge Lifecycle


## 1. Architectural rule

UPOS-005 MUST NOT create:

```text
project_memory_database
```

as an independent semantic Source of Truth.

Instead:

```text
GOVERNED_PROJECT_MEMORY_VIEW
= retrieval/context interface over UPOS-01 governed knowledge
```

## 2. Preferred durable project memory inputs

Consumed from UPOS-01 governed knowledge:

- Product Principles / Product contracts;
- Domain Model / invariants;
- Architecture contracts;
- Feature Specs;
- accepted ADR/PDR/DDR/etc.;
- Engineering Standards;
- Design System contracts;
- validated tests/evidence where appropriate;
- Runbooks;
- promoted Learnings;
- Postmortems/historical knowledge.

Their canonicality/lifecycle remains upstream.

## 3. Low-authority/history inputs

Raw brainstorming, unreviewed AI notes, old chats, rejected proposals, scratch plans may be retrieved only for explicit relevance and MUST remain clearly noncanonical/historical/proposal-class material.

## 4. Promotion

Module 05 may surface a candidate from Memory.

It cannot promote it.

Promotion remains:

```text
candidate
→ UPOS-01 / UPOS-009
→ review / validation
→ canonical owner/source update if approved
```

## 5. Knowledge change propagation

When upstream governed knowledge changes, Module 05 must invalidate/revalidate affected Context Bundles, Context Views, Memory references, and Retrieval Cache entries according to policy.

## 6. No hidden conversation dependency

A project is not considered to "know" something merely because an Agent/provider remembers a past conversation.

A durable fact must resolve to governed project knowledge or be treated as an unverified candidate.
