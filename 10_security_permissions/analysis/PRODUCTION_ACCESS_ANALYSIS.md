# Production Access Analysis

**ID:** UPOS-10-AN-PROD-001  
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

Production access is decomposed into independent capabilities:

```text
production-read
production-write
production-admin
deploy
```

Elevated mutation uses time-bounded/access-minimized controls by default.

## Break-glass decision

Break-glass is a protected emergency access mode, not automatically a Security Exception.

```text
policy-defined emergency route
→ no exception required if all policy conditions satisfied

policy departure
→ valid Security Exception additionally required
```

This avoids conflating emergency operation with policy bypass.
