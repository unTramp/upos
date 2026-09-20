# Schema Versioning & Compatibility

**ID:** UPOS-SCHEMA-VER-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0

## 1. Separate version axes

The following are distinct:

```text
U-POS baseline version
owner-module contract version
schema version
project manifest version
project adapter version
provider adapter version
runtime implementation version
```

A change to one does not automatically change all others.

## 2. Schema version

Schemas use semantic versioning for the machine-readable contract:

```text
MAJOR.MINOR.PATCH
```

Interpretation:

- **MAJOR** — validation/serialization compatibility break for declared consumers;
- **MINOR** — compatible extension under the declared compatibility model;
- **PATCH** — non-semantic correction that preserves accepted instance meaning.

Schema SemVer does not authorize a semantic change to the owning U-POS module.

## 3. Compatibility model

Let:

```text
Old = set of instances valid under the previous schema
New = set of instances valid under the proposed schema
```

Then:

```text
BACKWARD_INSTANCE_COMPATIBLE
Old ⊆ New

FORWARD_INSTANCE_COMPATIBLE
New ⊆ Old

FULL_INSTANCE_COMPATIBLE
Old = New

BREAKING_OR_MIXED
neither inclusion relationship is guaranteed
```

This definition concerns schema validation only.

It does NOT prove semantic compatibility.

## 4. Semantic compatibility

A schema change is semantically compatible only when every instance retains the same meaning under the bound owner-module contract.

Therefore:

```text
VALIDATION_COMPATIBLE
does not imply
SEMANTICALLY_COMPATIBLE
```

Adding a field that changes authority, ownership, lifecycle or permission meaning is semantic even if older instances still validate.

## 5. Required compatibility declaration

Every schema change after first stable publication MUST declare:

```text
previous_schema_version
new_schema_version
instance_compatibility
semantic_compatibility
migration_required
owner_contract_change_required
```

## 6. Baseline compatibility

A schema MUST declare which U-POS baseline it represents.

A validator/runtime MUST reject an unsupported baseline rather than silently reinterpret the artifact.

This preserves the UPOS-011 fail-closed compatibility rule.

## 7. Deprecation

Deprecation does not delete history.

A deprecated schema MUST retain:

- its version identity;
- its baseline binding;
- its replacement/supersession reference when one exists;
- migration guidance when required.

Historical artifacts remain attributable to the schema version used when created.

## 8. No convenience coercion

Validators MUST NOT silently coerce incompatible legacy instances into a newer meaning unless a separately defined migration explicitly performs that transformation and records provenance.
