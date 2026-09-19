# Phase 2A Acceptance Criteria

**ID:** UPOS-SCHEMA-P2A-ACCEPT-001  
**Status:** ACTIVE WORKING CHECKLIST  
**Baseline:** U-POS v1.0.0

Phase 2A is complete only when all mandatory items pass.

## Governance

- [x] Schema layer explicitly subordinate to frozen owner-module semantics.
- [x] Semantic vs representational schema change boundary defined.
- [x] Schema validation explicitly separated from Quality, Authority and Permission.
- [x] Provider-neutrality rule preserved.
- [x] Fail-closed baseline/binding behavior preserved.

## Identity & references

- [x] Frozen Global Identity & Reference Registry adopted as upstream.
- [x] Synthetic IDs prohibited where v1.0.0 explicitly excludes them.
- [x] Composite Project Manifest and Project Adapter identities preserved.
- [x] Namespace collision rule defined.
- [x] Provider/native refs separated from U-POS semantic identity.

## Versioning & compatibility

- [x] Schema version separated from U-POS/module/project/adapter/runtime versions.
- [x] Instance compatibility defined without conflating semantic compatibility.
- [x] Historical reproducibility requirement preserved.
- [x] Silent coercion prohibited.

## Registry

- [x] Registry purpose and non-ownership boundary defined.
- [x] Registry entry metadata contract defined.
- [x] Machine-readable registry artifact created.
- [x] Registry artifact schema-validates.
- [x] Broken normative-source references are automatically detected.

## Validation tooling

- [x] JSON Schema dialect selected and pinned: Draft 2020-12.
- [x] Validator implementation selected and pinned: Python `jsonschema==4.26.0`.
- [x] Local validation command added: `python tools/validate_schemas.py`.
- [x] CI `schema-validation` check added.
- [x] Positive fixture test added.
- [x] Negative fixture test added.
- [x] Frozen baseline verification remains PASS.

## CI evidence

For PR #1 at commit `4ac38a55a3133d19a4d635e0e295b45fdeaa4ae7`:

```text
Baseline Integrity   PASS
Schema Validation   PASS
```

The dependency pin was selected against the current PyPI release of `jsonschema` at the time of Phase 2A implementation.

## Exit condition

The mechanical foundation required by Phase 2A is operational.

Phase 2A is not yet declared frozen/complete until an independent reconciliation pass confirms that:

- governance rules do not create semantic ownership leakage;
- registry metadata is sufficient for the first domain schema families;
- namespace rules do not collide with owner-module terminology;
- no frozen identity exclusion was weakened;
- Phase 2B can consume this foundation without introducing a second Source of Truth.

Phase 2B (Documentation Authority schemas) MAY now proceed as candidate work, but no schema family should be promoted to STABLE until this reconciliation is complete.
