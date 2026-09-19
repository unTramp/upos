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
- [ ] Machine-readable registry artifact created.
- [ ] Registry artifact schema-validates.
- [ ] Broken normative-source references are automatically detected.

## Validation tooling

- [ ] JSON Schema dialect selected and pinned.
- [ ] Validator implementation selected and pinned.
- [ ] Local validation command added.
- [ ] CI `schema-validation` check added.
- [ ] Positive fixture test added.
- [ ] Negative fixture test added.
- [ ] Frozen baseline verification remains PASS.

## Exit condition

Phase 2A MUST NOT be declared complete until machine-readable registry + automated validation exist.

Phase 2B (Documentation Authority schemas) MAY be designed in parallel, but MUST NOT be promoted as stable before the 2A validation foundation is operational.
