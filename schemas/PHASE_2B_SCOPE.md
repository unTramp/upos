# Phase 2B Scope — Documentation Authority Machine-Readable Contracts

**ID:** UPOS-SCHEMA-P2B-SCOPE-001  
**Status:** CANDIDATE SCOPE  
**Baseline:** U-POS v1.0.0  
**Owner semantics:** UPOS-01 Documentation

## Objective

Represent existing UPOS-01 documentation authority and Source-of-Truth semantics in machine-readable contracts without redesigning UPOS-01.

## Canonical upstream

Primary normative sources:

~~~text
PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md
~~~

Supporting informative taxonomy:

~~~text
PROJECT_DOCUMENTATION_CATALOG_v1.0.md
~~~

Important:

~~~text
PROJECT_DOCUMENTATION_CATALOG_v1.0
!= project instance authority registry
~~~

## Candidate representation families

Subject to exact source extraction/reconciliation:

~~~text
Document metadata representation
Source-of-Truth entry representation
Source-of-Truth registry representation
Document lifecycle/status enums
Normativity/lifetime/freshness representation
Supersession/reference representation
~~~

Do not introduce document_registry_id or source_of_truth_entry_id merely for convenience unless upstream semantics establish such identity or a later governed decision does so.

## Source-of-Truth entry basis

UPOS-01 already permits a machine-readable larger-project record conceptually including:

~~~text
scope
owner
canonicalSource
status
normativity
relatedDecisions
lastReviewed
~~~

Phase 2B must preserve scoped authority and conflict behavior.

## Non-scope

Phase 2B does not own Context Bundle retrieval/assembly (UPOS-005), provider/path resolution (UPOS-011), Quality verdicts (UPOS-007), Security decisions (UPOS-010), or runtime orchestration.

## Exit requirement

Before any 2B schema becomes STABLE:

- exact upstream fields/enums/optionality must be traced;
- identity must be reconciled without synthetic owner-domain entities;
- positive and negative fixtures must exist;
- Source-of-Truth conflicts must not be auto-resolved by schema validation;
- Artist OS authority metadata must be expressible without changing Artist OS product semantics.
