# Least Privilege Standard

**ID:** UPOS-10-LPS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Hard principle

```text
grant minimum capabilities
for minimum resource scope
for minimum execution scope
for minimum duration
with minimum sensitive-data disclosure
needed for governed work
```

## 2. Evaluation dimensions

Least privilege is evaluated over:

```text
Capability breadth
Action breadth
Resource breadth
Execution scope breadth
Duration
Sensitive-data exposure
Provider credential breadth
Delegation breadth
```

## 3. Standing privilege

Broad standing privileges SHOULD be exceptional.

Prefer:

```text
base low-privilege access
→ explicit elevation request
→ bounded approval/decision
→ temporary elevated Grant
→ automatic expiry
```

## 4. Wildcards

Wildcard capabilities/resources must be explicit, justified and inspectable.

Do not infer wildcard inheritance from a parent resource.

## 5. Read-only fallback

If write is denied, read-only access MAY remain available only where policy explicitly allows it and a separate Permission Decision/Grant covers it.

Do not infer fallback automatically.

## 6. Secret minimization

Prefer:

```text
use-secret without raw disclosure
```

over:

```text
read-secret raw value into Agent Context
```

when runtime/provider can support secure binding.

## 7. Production minimization

Separate:

```text
production-read
production-write
production-admin
deploy
```

Do not collapse them into `production-access`.
