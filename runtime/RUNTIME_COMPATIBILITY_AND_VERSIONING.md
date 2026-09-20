# Runtime Compatibility and Versioning

**ID:** UPOS-RUNTIME-VER-001  
**Version:** 0.1.0  
**Phase:** 3  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER STANDARD  
**Semantic owner:** NONE_INFRASTRUCTURE  
**Baseline:** U-POS v1.0.0

## 1. Independent version axes

```text
owner semantic version
!= Phase-2 identity/reference schema version
!= Phase-3 runtime contract version
!= Phase-3 runtime schema version
!= Event contract/schema version
!= Phase-4 implementation version
!= persistence format version
```

A change to one axis does not automatically change the others.

## 2. Runtime contract SemVer

Phase-3 runtime contracts use `MAJOR.MINOR.PATCH`.

- MAJOR — breaking request/result/state/idempotency/persistence semantic change.
- MINOR — backward-compatible runtime expansion.
- PATCH — non-semantic/editorial correction.

Schema SemVer remains governed by `schemas/SCHEMA_VERSIONING_AND_COMPATIBILITY.md`.

## 3. Exact Phase-2 binding

Phase-3 schemas MUST reference exact versioned Phase-2 canonical URNs.

A compatibility resolver MAY substitute only after explicit compatibility evaluation.

Silent substitution is forbidden.

## 4. Historical interpretation

Durable runtime records MUST retain enough contract/schema version information to interpret them under the versions used when created.

Unsupported versions MUST fail closed rather than be silently interpreted as the newest version.

## 5. Owner semantic evolution

A new owner semantic version requires explicit review of whether:

- Phase-2 identity/reference representation changes;
- Phase-3 runtime behavior/contract changes;
- Event meaning/schema changes;
- migration is required.

No version axis is bumped merely because another axis changed.

## 6. Phase-4 consumer obligation

A future implementation MUST explicitly declare the runtime contracts and relevant schema/Event versions it supports.

Implementation version alone has no semantic authority.

## 7. Persistence version

A separate persistence format version is required only when physical storage representation has independent compatibility concerns.

Physical migration MUST NOT silently change owner meaning, identity or historical interpretation.

## 8. Normative sources

- `schemas/SCHEMA_VERSIONING_AND_COMPATIBILITY.md`
- `schemas/SCHEMA_URI_AND_REFERENCE_CONVENTIONS.md`
- `08_observability/OBSERVABILITY_LIFECYCLE_AND_VERSIONING.md`
