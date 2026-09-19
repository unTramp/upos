# Secret & Sensitive Data Standard

**ID:** UPOS-10-SSD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Secret semantic boundary

UPOS-010 defines access/use/disclosure/security handling requirements for Secrets.

UPOS-011/provider runtime owns concrete secret store, injection, retrieval and provider-native enforcement.

## 2. Secret capabilities

Keep separate:

```text
read-secret
use-secret
rotate-secret
manage-secret
```

```text
read-secret != use-secret
use-secret != disclose-secret
```

## 3. Prefer use without disclosure

Where supported:

```text
secure tool/provider binding receives secret
Agent/Context receives only secret_ref / capability
```

rather than exposing the raw value.

## 4. Raw secret logging prohibition

Hard invariant:

```text
RAW SECRET VALUE MUST NOT BE LOGGED
IN OBSERVABILITY / AUDIT / HANDOFF / FINDING / CONTEXT METADATA
```

Use safe metadata such as:

```text
secret_ref
secret_type/classification
access decision
operation type
subject ref
result
```

## 5. Sensitive Context access directive

For Context-source/data access UPOS-010 may return a representation constraint:

```text
ALLOW_FULL
ALLOW_REDACTED
REFERENCE_ONLY
DENY
```

This is a Security access/directive result, not a Context Bundle representation.

UPOS-005 consumes the directive and owns how the resulting Context is assembled/represented.

## 6. Data minimization

Only the minimum necessary sensitive information for the governed execution purpose may be exposed.

If a narrower representation can satisfy the purpose, prefer it.

## 7. Secret ownership

```text
SECRET ACCESS != SECRET OWNERSHIP
```

A subject allowed to use/read a secret does not become its policy owner or lifecycle owner.

## 8. Cross-project isolation

Secret/data/grant access for Project A must not automatically apply to Project B, even if resource names appear similar.

## 9. Copying and persistence

Security Policy may forbid raw sensitive material from entering:

```text
long-lived Context
project memory
logs
reports
commit messages
review text
telemetry
```

UPOS-010 declares restriction; owning modules enforce representation/storage within their domains.
