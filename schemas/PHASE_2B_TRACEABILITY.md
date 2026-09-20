# Phase 2B Traceability — Documentation Authority

**ID:** UPOS-SCHEMA-P2B-TRACE-001  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Date:** 2026-09-20

## 1. Purpose

Trace Phase 2B machine-readable contracts to existing UPOS-01 semantics without creating a second Documentation ontology.

## 2. Document Manifest

Schema:

~~~text
schemas/01/documentation/document-manifest.schema.json
~~~

Upstream owner:

~~~text
UPOS-01 Documentation
~~~

Primary upstream:

~~~text
01_documentation_system/00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json
01_documentation_system/00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
~~~

Representation policy:

- preserve existing fields and enum sets;
- replace the placeholder example.invalid schema URI with canonical U-POS schema URI only in the new schema layer;
- do not modify the frozen upstream schema;
- do not reinterpret document lifecycle/status as product/domain lifecycle.

## 3. Source-of-Truth Entry

Schema:

~~~text
schemas/01/documentation/source-of-truth-entry.schema.json
~~~

Primary upstream:

~~~text
PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
~~~

UPOS-01 says larger projects MAY maintain a machine-readable record including fields conceptually equivalent to:

~~~text
scope
owner
canonicalSource
status
normativity
relatedDecisions
lastReviewed
~~~

Therefore the candidate schema:

- restricts field names/types;
- does not make those upstream MAY fields globally required;
- does not invent source_of_truth_entry_id;
- does not resolve conflicts;
- does not rank documents globally;
- does not promote evidence or freshness into authority.

## 4. Authority boundary

~~~text
Document metadata        → UPOS-01
Scoped canonicality      → UPOS-01 Source-of-Truth Model
Project path/provider binding → UPOS-011 where applicable
Context retrieval/selection   → UPOS-005
~~~

## 5. Artist OS dogfooding

The fixtures intentionally exercise real adoption concepts such as:

~~~text
MASTER v1.4 → ACTIVE / NORMATIVE
MASTER v1.3 → SUPERSEDED / HISTORICAL
~~~

These fixture values demonstrate representability only.

They do not make Artist OS project facts part of universal U-POS semantics.
