# Capability Model Analysis

**ID:** UPOS-10-AN-CAP-001  
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

Use provider-neutral capability taxonomy plus exact action/resource scope.

Do not model provider scopes as canonical capabilities.

## Why capability and action are separate

Capability gives reusable policy grouping; Action gives request precision.

Example:

```text
capability = production-write
action = update feature flag value
resource = exact production service/config scope
```

## Taxonomy principle

Use stable semantic names only where they carry cross-project meaning. Project-specific capabilities may extend the taxonomy through governed policy/adapter binding without changing universal core.

## Inheritance

No implicit capability implication. Any implication/aggregation must be policy-defined.
