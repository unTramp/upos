# Schema Governance

**ID:** UPOS-SCHEMA-GOV-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Last reviewed:** 2026-09-20

## 1. Mission

Define how U-POS normative contracts are represented as machine-readable validation contracts without changing owner-module semantics.

## 2. Authority hierarchy

For semantic questions:

```text
owner-module normative U-POS contract
>
schema representation
>
runtime implementation
>
provider-native object
```

This is an authority relationship, not a statement that implementation evidence is unimportant.

Implementation/runtime remains evidence of current behavior, consistent with UPOS-01.

## 3. Ownership rule

A schema has a `schema_owner_module`, but the schema layer does not acquire semantic ownership.

Examples:

```text
Task semantics                  → UPOS-004
Context Bundle semantics        → UPOS-005
Engineering Change semantics    → UPOS-006
Quality Assessment semantics    → UPOS-007
Observability Event semantics   → UPOS-008
Learning Candidate semantics    → UPOS-009
Permission Decision semantics   → UPOS-010
Project Manifest semantics      → UPOS-011
```

Cross-cutting primitives MAY live under `schemas/common/` only when they are representation primitives and do not create domain semantics.

## 4. Schema obligations

Every stable schema MUST:

1. identify the exact owner module;
2. identify the U-POS baseline it represents;
3. reference the normative Markdown source(s);
4. preserve canonical identity semantics;
5. preserve required/optional distinctions supported by the owner contract;
6. preserve fail-closed behavior where the owner contract requires it;
7. avoid provider-specific assumptions unless the schema is explicitly an adapter/provider schema;
8. declare schema version independently from owner-module version;
9. have automated validation;
10. be registered in `SCHEMA_REGISTRY.md` and, once introduced, its machine-readable registry.

## 5. Prohibited schema behavior

Schemas MUST NOT:

```text
invent a new domain entity only to obtain a convenient ID
collapse distinct U-POS concepts into one field
turn projections into canonical entities
turn evidence into verdicts
turn provider capability into U-POS permission
turn configuration into project truth
turn telemetry into workflow/domain state
weaken an owner-module invariant
silently choose a winner in an unresolved Source-of-Truth conflict
```

## 6. Semantic change gate

A proposed schema change is a **semantic change** when it would change the meaning, ownership, lifecycle, authority, required invariant, or allowed domain behavior defined by an owner module.

A semantic change MUST NOT be introduced only in `schemas/`.

Required path:

```text
evidence / proposal
→ owner-module governance
→ approved future owner contract version
→ schema update
```

For frozen v1.0.0 contracts, schema work is representational unless a separately governed future U-POS release changes the owner semantics.

## 7. Representational change

A representational change MAY occur inside the schema layer when meaning is preserved.

Examples:

- correcting a schema typo;
- adding schema descriptions/examples;
- changing file organization without changing `$id`;
- adding a validation assertion already required by the owner contract;
- improving reference resolution tooling.

Representational changes still require validation and compatibility classification.

## 8. No hidden defaults

A schema MUST NOT create material behavior through a default that the owner contract does not define.

Defaults MAY be used only for explicitly non-semantic serialization convenience and MUST be documented.

Absence of a required project binding MUST remain absence; it must not be replaced by convenience fallback when UPOS-011 requires fail-closed behavior.

## 9. Provider neutrality

Universal schemas MUST use provider-neutral concepts owned by U-POS.

Provider-specific identifiers belong in explicit provider/native reference fields or adapter schemas.

Example:

```text
Integration Request     = U-POS concept
GitHub Pull Request     = provider object
```

The adapter binds them; the schema layer does not equate them.

## 10. Validation is not authorization

```text
SCHEMA_VALID
!=
QUALITY_PASS
!=
AUTHORIZED
!=
PERMITTED
!=
READY_TO_MERGE
```

Schema validation proves structural contract conformance only.

## 11. Promotion states

Schema implementation states:

```text
DRAFT
→ CANDIDATE
→ STABLE
→ DEPRECATED
→ RETIRED
```

These states describe the machine-readable artifact, not the lifecycle state of the domain entity it represents.

Promotion to `STABLE` requires:

- owner traceability;
- automated validation;
- compatibility classification;
- reference resolution;
- no known contradiction with the bound U-POS baseline.

## 12. Baseline binding

Every schema family MUST bind to a U-POS baseline.

Initial baseline:

```text
upos_baseline = v1.0.0
```

Historical validated instances MUST remain interpretable under the schema/baseline versions recorded for that execution or artifact. Newer schemas must not silently reinterpret historical records.
