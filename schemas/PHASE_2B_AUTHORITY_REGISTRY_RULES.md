# Phase 2B — Source-of-Truth Registry Rules

**ID:** UPOS-SCHEMA-P2B-SOTREG-001  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Semantic owner:** UPOS-01 Documentation  
**Date:** 2026-09-20

## 1. Upstream basis

UPOS-01 defines:

- scoped authority;
- canonical owner;
- canonical source;
- a recommended project SOURCE_OF_TRUTH map;
- an optional machine-readable Source-of-Truth Registry entry for larger projects;
- conflict taxonomy SOT-C1 through SOT-C7.

The schema layer represents those semantics. It does not resolve documentation disputes.

## 2. Base entry vs registry profile

The base entry schema remains conservative because UPOS-01 says a larger-project machine-readable record MAY include the listed fields.

~~~text
source-of-truth-entry.schema.json
= permissive representation of allowed record fields
~~~

The registry is a more specific operational profile:

~~~text
source-of-truth-registry.schema.json
= larger-project collection used for actual authority resolution
~~~

For a record to participate in the registry, the profile requires:

~~~text
scope
owner
canonicalSource
status
~~~

This does not convert every optional UPOS-01 metadata field into a universal MUST. It defines the minimum usable profile for a registry that claims to resolve scoped authority.

## 3. Structural invariants

The validator MUST reject:

1. exact duplicate registry objects;
2. duplicate authority keys:
   scope + owner + canonicalSource;
3. more than one ACTIVE canonical owner for the same exact scope;
4. unresolved schema references or invalid entry shapes.

The validator MUST NOT reject merely because one owner has multiple ACTIVE canonical sources for an exact scope.

UPOS-01 canonical resolution explicitly permits locating ACTIVE normative source(s), plural.

Multiple same-owner sources therefore require content-level reconciliation, not automatic structural failure.

## 4. Conflict boundary

~~~text
STRUCTURAL AUTHORITY AMBIGUITY
!=
SEMANTIC CLAIM CONFLICT
~~~

SOT-C4 requires active authoritative-looking sources that actually disagree.

JSON structure alone cannot prove that two documents disagree on a claim.

Therefore:

- different ACTIVE owners for one exact scope is a structural error;
- repeated same owner/source tuple is a structural error;
- multiple ACTIVE sources under the same owner produce a review warning, not an automatic conflict verdict;
- semantic disagreement must be registered/reviewed under UPOS-01 conflict governance.

## 5. High-risk rule

The schema/validator never silently resolves high-risk conflicts involving billing, authentication, authorization, privacy, retention, destructive actions, data ownership, domain lifecycle, compliance, production safety, or irreversible migration.

Those remain subject to explicit owner/human governance decision under UPOS-01.

## 6. Artist OS dogfooding

Artist OS is a representability case, not a source of universal semantics.

Expected mappings can include:

~~~text
MASTER v1.4 → ACTIVE canonical source
MASTER v1.3 → SUPERSEDED historical source
AR companion set → ACTIVE normative source(s) in their owned scope
temporary implementation plans → their execution scope only
completion reports → evidence/history, not timeless authority
~~~

The concrete project must choose exact scopes and owners during its adoption work.
