# Protected Action Analysis

**ID:** UPOS-10-AN-PACT-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Decision

`protected_action_id` identifies a concrete action instance requiring elevated controls, not a definition/class.

Protection classification comes from Security Policy.

## Why a local lifecycle exists

Audit needs to distinguish:

```text
requested
authorized
executed/failed/cancelled/expired
```

This does not duplicate Workflow lifecycle because it tracks the security-sensitive action instance only.

## Change Class separation

Protected Action and UPOS-004 Change Class are orthogonal. Risk classification may influence controls, but neither determines the other universally.
