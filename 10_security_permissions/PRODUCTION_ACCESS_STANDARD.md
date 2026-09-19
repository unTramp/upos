# Production Access Standard

**ID:** UPOS-10-PROD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Production is elevated by default

Production mutation is treated as elevated/protected unless project Security Policy explicitly defines otherwise.

UPOS-010 distinguishes at least:

```text
production-read
production-write
production-admin
deploy
```

## 2. Production write baseline

Production write SHOULD normally require:

```text
exact resource scope
explicit purpose/work ref
current Permission Decision
time-bounded Grant/elevation where reusable access is needed
audit requirement
protected-action treatment
risk/Workflow condition refs as applicable
Human Approval where project policy requires
```

## 3. Deployment boundary

```text
Deployment Workflow ordering/execution orchestration → UPOS-004
Production/deploy permission semantics             → UPOS-010
Provider deployment mechanism                      → UPOS-011/runtime
```

## 4. Privilege elevation flow

```text
base low privilege
↓
elevation Permission Request
↓
policy / authority / approval evaluation
↓
ALLOW Permission Decision
↓
temporary elevated Grant where needed
↓
Protected Action execution externally
↓
automatic expiry / revocation
```

## 5. Break-glass

Break-glass is an exceptional emergency access mode.

It MUST require at least:

```text
explicit emergency reason/purpose ref
strong subject attribution
narrow resource/action scope
limited duration
elevated audit requirement
automatic expiry
post-action review requirement
```

### Break-glass vs Security Exception

```text
BREAK_GLASS != SECURITY_EXCEPTION
```

If policy already defines an emergency path, break-glass may operate within policy and need no Exception.

If it departs from an otherwise applicable rule, it additionally requires a valid `security_exception_id`.

Break-glass MUST NOT become ordinary standing access.

## 6. Reauthentication / assurance

Security Policy may require stronger/recent authentication as a condition. Identity-provider mechanics remain UPOS-011/provider-owned.

## 7. Environment abstraction

UPOS-010 uses abstract environment/protection semantics. It does not universally require names such as development/test/staging/production. UPOS-011 maps concrete environments.
