# Security Entity Model Analysis

**ID:** UPOS-10-AN-ENT-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Accepted first-class identities

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
```

## Explicitly rejected duplicate identities

```text
security_approval_id
security_veto_id
security_review_result_id
security_policy_id
subject_id
resource_id
secret_id
```

Reasons:

- approval/veto authority already exists externally;
- Security review is not Permission Decision and uses external Skill/Quality artifacts;
- canonical Security Policy is a governed source reference/version;
- subject/resource/secret identities are project/provider/upstream-owned.

## Entity relationships

```text
Permission Request 1 → N Permission Decisions over time/re-evaluation
Permission Decision → 0..N applicable Grants
Permission Decision → 0..N approval/authority refs
Permission Decision → 0..N Security Exceptions
Protected Action → exact Request + current ALLOW Decision
Grant → bounded subject/capability/resource/lifetime
Security Exception → bounded policy departure
```
