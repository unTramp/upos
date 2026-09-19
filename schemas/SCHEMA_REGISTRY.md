# Canonical Schema Registry

**ID:** UPOS-SCHEMA-REG-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0

## 1. Purpose

The Schema Registry is an index of machine-readable contracts.

~~~text
SCHEMA REGISTRY != GLOBAL DOMAIN MODEL != SOURCE OF TRUTH
~~~

Owner modules remain normative.

## 2. Registry entry contract

Every concrete entry contains:

~~~text
schema_key
schema_uri
schema_version
artifact_path
implementation_state
upos_baseline
semantic_owner_module
schema_steward
normative_source_refs
identity_model
reference_dependencies
instance_compatibility
semantic_compatibility
notes
~~~

semantic_owner_module is owner-domain attribution.

schema_steward is maintenance responsibility for the representation.

They MUST NOT be conflated.

## 3. Registration rule

A schema MUST NOT be registered as STABLE while semantic owner/infrastructure classification, governing source, identity semantics, baseline compatibility, canonical schema URI, reference dependencies, automated validation, or owner-contract conformance is unresolved.

## 4. Machine-readable registry

Current registry:

~~~text
schemas/registry/schema-registry.json
~~~

Registry schema:

~~~text
schemas/meta/schema-registry.schema.json
~~~

The machine-readable registry does not become semantic Source of Truth.

## 5. Planned schema families

~~~text
A. common representation primitives
B. UPOS-01 documentation authority / Source-of-Truth representation
C. UPOS-011 Project Manifest
D. UPOS-011 Project Adapter
E. execution backbone:
   UPOS-004 Task / Routing / Workflow / Stage
   UPOS-002 Agent Run
   UPOS-005 Context Bundle
F. engineering / quality / security
G. observability / learning
~~~

This is implementation sequencing only.

## 6. Cross-module references

Cross-module schema references MUST point to the owning schema family rather than copying upstream fields into a new pseudo-entity.

Canonical cross-file references use SCHEMA_URI_AND_REFERENCE_CONVENTIONS.md.

Transport projections/snapshots must remain explicitly non-canonical and retain upstream identity/provenance.

## 7. Frozen anti-duplication

Do not introduce:

~~~text
quality_readiness_id
global metric_observation_id
project_manifest_id
project_adapter_id
~~~

Representation schemas MAY exist for the underlying concepts where frozen owners permit them, while preserving upstream identity.

## 8. Dependency consistency

Every reference_dependencies key MUST resolve to a registered schema family.

Every schema_uri MUST match artifact $id.

The validator rejects unresolved source refs, unresolved schema dependencies, duplicate schema URIs, owner-prefix mismatch, unresolved canonical cross-schema references, and unsupported external reference forms.
