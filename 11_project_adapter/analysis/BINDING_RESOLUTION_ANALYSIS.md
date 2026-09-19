# Binding Resolution Analysis

**ID:** UPOS-11-AN-007  
**Type:** RESOLUTION ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


The selected resolution model is deterministic specificity precedence:

```text
organization
< project
< repository
< environment
< operation
< execution override
```

Equal-specificity incompatible matches fail as ambiguous/conflicting.

This avoids hidden provider preference and “last config wins”.

Fallback is a separate explicit mechanism and is prohibited by default for protected operations unless policy allows it.
