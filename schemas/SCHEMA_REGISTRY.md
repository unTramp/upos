# Canonical Schema Registry

**ID:** UPOS-SCHEMA-REG-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0

## 1. Purpose

The Schema Registry is an index of machine-readable contracts.

It is NOT a semantic owner.

```text
SCHEMA REGISTRY
!=
GLOBAL DOMAIN MODEL
!=
SOURCE OF TRUTH
```

Owner modules remain normative.

## 2. Registry entry contract

Every concrete schema entry MUST contain:

```text
schema_key
schema_version
artifact_path
implementation_state

upos_baseline

schema_owner_module
normative_source_refs

identity_model
reference_dependencies

instance_compatibility
semantic_compatibility

notes
```

Additional implementation metadata MAY be added without changing owner semantics.

## 3. Registration rule

A schema MUST NOT be registered as `STABLE` when any of the following is unresolved:

```text
semantic owner
normative source
identity semantics
baseline compatibility
reference dependencies
automated validation
known contradiction with owner contract
```

## 4. Initial registry state

Phase 2A creates governance for the registry before introducing domain schemas.

No domain schema is considered stable merely because a planned family appears below.

## 5. Planned schema families

Implementation order:

```text
A. common representation primitives
B. UPOS-01 documentation authority / Source-of-Truth representation
C. UPOS-11 Project Manifest
D. UPOS-11 Project Adapter
E. execution backbone:
   UPOS-004 Task / Routing / Workflow / Stage
   UPOS-002 Agent Run
   UPOS-005 Context Bundle
F. engineering / quality / security
G. observability / learning
```

This order is implementation sequencing only and does not alter module authority.

## 6. Cross-module references

Cross-module schema references MUST point to the owning schema family rather than copying the upstream object's fields into a new locally-owned pseudo-entity.

Duplication for transport convenience MUST be explicitly marked as a projection/snapshot when required and MUST retain upstream identity/provenance.

## 7. Frozen anti-duplication examples

The registry MUST NOT introduce entries for invented entities such as:

```text
QualityReadinessEntity with quality_readiness_id
MetricObservationEntity with global metric_observation_id
ProjectManifestEntity with project_manifest_id
ProjectAdapterEntity with project_adapter_id
```

Representation schemas MAY exist for these concepts where the frozen owner permits the concept, but their identity must remain exactly as defined upstream.

## 8. Machine-readable registry

A machine-readable registry artifact will be introduced only after the registry metadata contract itself is validated.

Its addition must not make that registry the semantic source of truth.
