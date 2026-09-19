# Security Binding Analysis

**ID:** UPOS-11-AN-009  
**Type:** SECURITY BINDING ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-011 Implementation  
**Version:** 1.0.0-rc.1  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


UPOS-010 requires mappings for:
- subject identities;
- capabilities to provider enforcement;
- resources/environments;
- Grant enforcement;
- secrets/secure injection;
- protected targets;
- approvals/elevation/break-glass.

No conflict exists with Module-11 ownership because UPOS-010 owns the semantic Permission Decision and Module 11 owns only physical realization.

Key invariant:

```text
provider scope != U-POS permission
```
