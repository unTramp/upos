# Input Baseline Resolution

## Purpose

Record which physical source files became the final U-POS v1 release baseline and why.

## Resolution

The initially uploaded 005/006 files were older frozen transports. Final UPOS-007 active traceability expects the later baselines:

```text
UPOS-005 186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528
UPOS-006 49301fa994e2d47c146f84260e4783585c950faf0c73dbe129767c2c2c95e45e
```

Those later frozen files were available in the working corpus and were selected. UPOS-007 was retained at:

`36c52764ccafdfef053d224ec1af5d297e3cd6eceacbc45d287d4bc96a1833b0`

This avoids regressing Module 07 to older upstream contracts.

## 008–011 input candidates

The original convergence candidates were audited, narrowly reconciled, and replaced by the final hashes listed in `UPOS_V1_FREEZE_MANIFEST.md`.

## Chat independence

No old conversation transcript is required to interpret the final package. Normative meaning comes from the master source, Module-001 documentation/governance corpus, and the embedded ACTIVE/NORMATIVE files inside Modules 002–011. Historical `analysis/` artifacts remain evidence, not Source of Truth.
