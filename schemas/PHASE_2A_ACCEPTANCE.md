# Phase 2A Acceptance Criteria

**ID:** UPOS-SCHEMA-P2A-ACCEPT-001  
**Status:** COMPLETE  
**Baseline:** U-POS v1.0.0  
**Completed:** 2026-09-20

Phase 2A is complete because all mandatory foundation and reconciliation criteria pass.

## Governance

- [x] Schema layer explicitly subordinate to frozen owner-module semantics.
- [x] Semantic vs representational schema change boundary defined.
- [x] Schema validation explicitly separated from Quality, Authority and Permission.
- [x] Provider-neutrality rule preserved.
- [x] Fail-closed baseline/binding behavior preserved.
- [x] Semantic ownership separated from schema stewardship.
- [x] Scoped authority preserved; no false global precedence chain introduced.

## Identity & references

- [x] Frozen Global Identity & Reference Registry adopted as upstream.
- [x] Synthetic IDs prohibited where v1.0.0 explicitly excludes them.
- [x] Composite Project Manifest and Project Adapter identities preserved.
- [x] Namespace collision rule defined.
- [x] Provider/native refs separated from U-POS semantic identity.
- [x] Canonical versioned schema URI / cross-schema reference convention defined.
- [x] Offline schema reference resolution required.

## Versioning & compatibility

- [x] Schema version separated from U-POS/module/project/adapter/runtime versions.
- [x] Instance compatibility defined without conflating semantic compatibility.
- [x] Historical reproducibility preserved.
- [x] Silent coercion/substitution prohibited.

## Registry

- [x] Registry purpose and non-ownership boundary defined.
- [x] Registry entry metadata contract defined.
- [x] Machine-readable registry artifact created.
- [x] Registry artifact schema-validates.
- [x] Broken governing-source references are detected.
- [x] Registry/artifact URI mismatch is detected.
- [x] Duplicate schema URI is detected.
- [x] Registry dependency resolution is validated.
- [x] Owner namespace ↔ semantic owner consistency is validated.

## Validation tooling

- [x] JSON Schema dialect pinned: Draft 2020-12.
- [x] Validator pinned: Python jsonschema==4.26.0.
- [x] Local validation command: python tools/validate_schemas.py.
- [x] CI schema-validation check added.
- [x] Positive fixture test added.
- [x] Negative fixture test added.
- [x] Frozen baseline verification remains PASS.

## Final reconciliation evidence

Reconciliation commit:

~~~text
306666344de5e3f784996c6145a8bfd5ff6cea90
fix(schema): reconcile phase 2A ownership and references
~~~

CI on the exact reconciliation HEAD:

~~~text
Baseline Integrity   PASS
Schema Validation   PASS
~~~

Reconciliation status:

~~~text
P0 unresolved: 0
P1 unresolved: 0
P2 unresolved: 0

Frozen files modified: 0
Semantic ownership moved: 0
Synthetic frozen-excluded IDs introduced: 0
~~~

## Exit decision

~~~text
PHASE 2A
Schema Governance & Identity Foundation
COMPLETE
~~~

Phase 2B may proceed as candidate implementation work under schemas/PHASE_2B_SCOPE.md.

No Phase 2 schema family is promoted to STABLE merely because Phase 2A is complete; each family retains its own conformance, validation and compatibility obligations.
