# Resource & Action Model

**ID:** UPOS-10-RAM-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Permission tuple

Every request resolves over at least:

```text
subject
capability
action
resource_type
resource_ref
resource_scope
security/execution context
```

Role alone is never sufficient.

## 2. Resource types

Universal abstract resource classes:

```text
PROJECT
REPOSITORY
BRANCH_OR_PROTECTED_TARGET
PATH_SCOPE
DOCUMENTATION_SOURCE
CONTEXT_SOURCE
ENVIRONMENT
SECRET
SERVICE
DATABASE
DATA_SCOPE
ARTIFACT
DEPLOYMENT_TARGET
SECURITY_POLICY_TARGET
PROVIDER_RESOURCE
```

Concrete identifiers remain upstream/project/provider-owned.

## 3. Resource scope

Scope may express:

```text
whole resource
subresource/path
branch/target
record/data segment
environment
operation class
exact artifact/revision
```

Broad wildcard scope MUST be explicit, inspectable and policy-allowed.

## 4. Resource hierarchy

Permission inheritance is **not implicit**.

```text
repository permission
!= production permission
project access
!= all secrets
parent path access
!= all child paths unless policy says so
```

If inheritance exists, Security Policy must define it.

## 5. Action intent

Permission evaluation MAY use governed purpose/work references:

```text
task_id
workflow_instance_id
stage_id
engineering_change_id
protected_action_id
approved plan/decision ref
```

Arbitrary free-text intent from an Agent MUST NOT be treated as authoritative purpose by itself.

## 6. Exact-target preference

Protected/security-sensitive requests SHOULD bind to the most exact practical resource state/reference so an `ALLOW` cannot silently float to unrelated later targets.
