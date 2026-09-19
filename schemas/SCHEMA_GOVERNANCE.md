# Schema Governance

**ID:** UPOS-SCHEMA-GOV-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Last reviewed:** 2026-09-20

## 1. Mission

Define how U-POS normative contracts are represented as machine-readable validation contracts without changing owner-module semantics.

## 2. Scoped authority — no global total ordering

For semantic meaning, the owner-module normative U-POS contract governs.

For machine serialization conformance, the schema bound to that owner contract governs the representation.

Runtime/provider state remains evidence of current implementation or behavior as governed by UPOS-01.

~~~text
semantic truth        → owner module / UPOS-01 authority resolution
serialization shape   → registered schema representation
runtime behavior      → implementation evidence
provider object       → provider-native evidence/binding
~~~

A schema MUST NOT override owner semantics. A normative contract MUST NOT be inferred from provider convenience.

## 3. Semantic ownership vs schema stewardship

Every registered schema declares:

~~~text
semantic_owner_module
schema_steward
~~~

semantic_owner_module identifies the frozen U-POS module whose semantics are represented.

schema_steward identifies responsibility for maintaining the machine-readable artifact.

~~~text
SCHEMA STEWARDSHIP != SEMANTIC OWNERSHIP
~~~

Infrastructure/meta schemas that define only schema-layer mechanics use:

~~~text
semantic_owner_module = NONE_INFRASTRUCTURE
schema_steward         = UPOS_SCHEMA_LAYER
~~~

This does not create a new U-POS domain module.

Cross-cutting primitives MAY live under schemas/common only when they are representation primitives and do not create domain semantics.

## 4. Schema obligations

Every stable schema MUST:

1. identify the exact semantic owner module or explicitly declare infrastructure-only semantics;
2. identify the U-POS baseline it represents;
3. reference the governing/normative source(s);
4. preserve canonical identity semantics;
5. preserve required/optional distinctions supported by the owner contract;
6. preserve fail-closed behavior where the owner contract requires it;
7. avoid provider-specific assumptions unless explicitly an adapter/provider schema;
8. declare schema version independently from owner-module version;
9. have automated validation;
10. have a canonical schema URI and resolvable cross-schema references;
11. be registered in the machine-readable Schema Registry.

## 5. Prohibited schema behavior

Schemas MUST NOT invent a new domain entity only to obtain a convenient ID, collapse distinct U-POS concepts, turn projections into canonical entities, turn evidence into verdicts, turn provider capability into U-POS permission, turn configuration into project truth, turn telemetry into workflow/domain state, weaken an owner-module invariant, silently resolve Source-of-Truth conflict, or turn schema stewardship into semantic ownership.

## 6. Semantic change gate

A schema change is semantic when it changes meaning, ownership, lifecycle, authority, a required invariant, or allowed domain behavior defined by an owner module.

A semantic change MUST NOT be introduced only in schemas/.

Required path:

~~~text
evidence / proposal
→ owner-module governance
→ approved future owner contract version
→ schema update
~~~

For frozen v1.0.0 contracts, schema work is representational unless a separately governed future U-POS release changes owner semantics.

## 7. Representational change

A representational change MAY occur inside the schema layer when meaning is preserved, including descriptions, examples, repository file movement while preserving canonical schema URI, validation assertions already required by owner contracts, and reference-resolution tooling.

## 8. No hidden defaults

A schema MUST NOT create material behavior through a default that the owner contract does not define.

Absence of a required project binding remains absence. Convenience fallback is forbidden where UPOS-011 requires fail-closed behavior.

## 9. Provider neutrality

Universal schemas use provider-neutral U-POS concepts. Provider-native identifiers belong in explicit provider/native references or adapter schemas.

~~~text
Integration Request = U-POS concept
GitHub Pull Request = provider object
~~~

## 10. Validation is not authorization

~~~text
SCHEMA_VALID
!= QUALITY_PASS
!= AUTHORIZED
!= PERMITTED
!= READY_TO_MERGE
~~~

## 11. Promotion states

~~~text
DRAFT
→ CANDIDATE
→ STABLE
→ DEPRECATED
→ RETIRED
~~~

Promotion to STABLE requires semantic-owner traceability, automated validation, compatibility classification, canonical URI/reference resolution, and no known contradiction with the bound U-POS baseline.

## 12. Baseline binding

Every schema family binds to a U-POS baseline.

~~~text
upos_baseline = v1.0.0
~~~

Historical artifacts must remain interpretable under the schema/baseline versions recorded for them. Newer schemas must not silently reinterpret historical records.
