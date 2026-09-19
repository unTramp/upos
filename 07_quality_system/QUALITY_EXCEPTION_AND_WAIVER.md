# Quality Exception & Waiver Standard

**ID:** UPOS-07-QEW-001  
**Type:** QUALITY EXCEPTION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/QUALITY_EXCEPTION_TEMPLATE.md


## 1. Definition

A Quality Exception records an externally authorized bounded exception to a Quality criterion/finding/gate requirement.

Every exception has stable:

```text
quality_exception_id
```

UPOS-007 records/consumes it.

UPOS-002/UPOS-010/Human Governance or other canonical authority owns authorization.

## 2. Contract

```text
quality_exception_id
status

target_ref
target_state_ref

criterion_ref
criterion_key
finding_id
quality_gate_id

reason
scope
effective_from
expiry_or_review_trigger

authorizing_authority_ref
decision_ref
policy_ref

created_at
supersedes
replacement
```

Non-applicable links are explicit `N/A`.

## 3. Exception status

```text
ACTIVE
EXPIRED
REVOKED
SUPERSEDED
INVALID
```

## 4. Waiver does not erase history

```text
WAIVED != NEVER EXISTED
```

Preserve:

- original Finding;
- affected criterion;
- decision/authority;
- scope;
- expiry/review trigger.

## 5. Scope

Exceptions may be:

- one-target;
- one-release;
- time-limited;
- scope-limited.

No permanent silent waiver by default.

## 6. Invalid exception

An expired/revoked/out-of-scope/unverifiable exception MUST NOT satisfy the affected criterion/gate.

## 7. Authority boundary

Recording an exception does not grant authority to create it.
