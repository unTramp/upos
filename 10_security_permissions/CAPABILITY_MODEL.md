# Capability Model

**ID:** UPOS-10-CAP-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Definition

A Capability is a provider-neutral abstract action class used to state what security power is needed.

```text
CAPABILITY != TOOL
CAPABILITY != PROVIDER SCOPE
CAPABILITY != GRANT
CAPABILITY != CURRENT PERMISSION
```

## 2. Universal capability families

### Repository / engineering

```text
repository-read
repository-write
branch-create
commit
push
integration-request-create
integration-request-update
merge
history-rewrite
protected-target-write
tag-create
```

### Documentation / project knowledge access

```text
read-project-documentation
write-project-documentation
read-decision-records
write-governed-documentation
```

### Context / sensitive data

```text
read-sensitive-context
read-restricted-source
read-secret
use-secret
rotate-secret
manage-secret
```

### Execution

```text
execute-test
execute-build
execute-static-analysis
execute-migration
```

### Environment / operations

```text
deploy
production-read
production-write
production-admin
service-admin
database-read
database-write
```

### Security administration

```text
permission-admin
grant-admin
security-policy-change
approve-protected-action
```

## 3. Capability granularity

A capability SHOULD be broad enough to remain provider-independent but narrow enough to support least privilege.

Bad universal capability:

```text
do-anything
```

Overly provider-specific capability:

```text
vendor-specific-scope-string
```

Preferred:

```text
production-write
merge
use-secret
```

with resource/action scope providing precision.

## 4. Capability requirements from Skills/Engineering

UPOS-003 Skill contracts MAY declare required capability references. UPOS-006 Engineering actions MAY declare capability/action needs.

These declarations are requirements, not grants.

UPOS-010 evaluates whether use is permitted.

## 5. Capability composition

Possession of one Capability MUST NOT imply another unless Security Policy explicitly defines that relationship.

Examples:

```text
production-read != production-write
read-secret != use-secret
use-secret != disclose-secret
repository-write != history-rewrite
merge != permission-admin
```

## 6. Provider mapping

Concrete provider/native permissions are deferred to UPOS-011:

```text
universal capability
→ project/provider binding
→ technical enforcement mechanism
```
