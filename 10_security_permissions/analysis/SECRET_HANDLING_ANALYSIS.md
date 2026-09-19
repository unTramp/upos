# Secret Handling Analysis

**ID:** UPOS-10-AN-SEC-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Main decision

Separate secret **use** from secret **disclosure**.

Prefer secure binding/use without raw value exposure where available.

## Universal semantics

UPOS-010 may decide:

```text
may read raw secret?
may use secret via tool/provider binding?
may rotate/manage?
may raw value enter Context?
what redaction/minimization applies?
what audit metadata is required?
```

Concrete secret stores/injection remain UPOS-011/runtime.

## Telemetry safety

Raw secret values are forbidden from audit/observability payloads. Safe refs/metadata only.
