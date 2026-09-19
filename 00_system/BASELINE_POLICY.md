# Frozen Baseline Policy

## Current baseline

- Module 01: stable Documentation System v1.2 baseline.
- Modules 02–11: FROZEN v1.0.
- Repository release tag: `v1.0.0`.

## Rule

A semantic change to a frozen module MUST NOT be made as an unversioned edit to the v1.0 baseline.

Any material change requires:

1. explicit owner/module impact analysis;
2. traceable change proposal;
3. review against cross-module ownership/interfaces;
4. new module version where semantics change;
5. refreshed release/freeze evidence and baseline hashes.

New runtime, schemas, adapters, tools, or Control Plane implementations MAY be added outside frozen module directories provided they conform to the frozen contracts and do not redefine them.
