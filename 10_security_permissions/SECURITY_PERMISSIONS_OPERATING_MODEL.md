# Security & Permissions Operating Model

**ID:** UPOS-10-SPOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Operating question

UPOS-010 determines whether a concrete protected use is permitted now. It evaluates a bounded security request, not a role title in the abstract.

```text
subject
+ execution scope
+ capability/action
+ resource/scope
+ current policy version
+ current grants
+ authority/SoD references
+ required approval state
+ applicable exception state
+ time/security context
=
Permission Decision
```

## 2. Organizational authority and technical permission

Organizational authority comes from UPOS-002. Technical permission comes from UPOS-010.

Examples:

```text
Merge Controller organizational authority
→ UPOS-002

permission to execute merge against protected target now
→ UPOS-010
```

```text
Security Role may have scoped veto authority
→ UPOS-002 / project governance

current technical enforcement result preventing protected action
→ UPOS-010 DENY + veto basis
```

UPOS-010 MUST NOT infer organizational authority from a provider token, active Grant, tool access, or successful execution.

## 3. Authorization model

A permission decision is exact enough to explain:

```text
who/what
wanted to do what
using which abstract capability
to which resource/scope
for which governed work/purpose
under which policy version
with which grants/approvals/exceptions
at what time
and why the result was ALLOW/DENY/CONDITIONAL/BLOCKED/UNKNOWN
```

## 4. Current-state rule

Authorization is time/context sensitive.

A historical `ALLOW` MUST NOT be reused blindly after material change to:

```text
subject identity or role binding
Agent Run / Task / Workflow / Stage
resource or resource scope
resource protection state
security policy/version
grant status or expiry
approval state
SoD relationship
security exception status
risk/security context
project/environment binding
```

A materially changed request requires re-evaluation and a new `permission_decision_id`.

## 5. Capability grant vs permission decision

```text
CAPABILITY
= abstract action class

GRANT
= bounded allowance substrate for subject + capability + scope + lifetime

PERMISSION DECISION
= current evaluation of one exact request
```

An active Grant can satisfy part of an authorization decision but cannot bypass current policy, SoD, protected-action, approval, expiry or resource constraints.

## 6. Protected action model

A Protected Action is a concrete security-sensitive action instance requiring controls beyond ordinary capability possession.

Typical universal categories include:

```text
protected-target merge/write
history rewrite
production write/deploy/admin
secret read/rotation/administration
destructive data operation
permission/security administration
security-policy modification
break-glass/elevated access
```

Project-specific protected action classification belongs in project security policy/UPOS-011 bindings.

## 7. Decision effect

```text
ALLOW       → may proceed if still current at execution time
DENY        → must not proceed
CONDITIONAL → must not proceed; satisfy conditions then re-evaluate
BLOCKED     → must not proceed; repair prerequisite/conflict then re-evaluate
UNKNOWN     → must not proceed for protected capability; resolve owner/policy/context
```

UPOS-004 consumes these results for orchestration. UPOS-010 does not decide whether Workflow should wait, reroute, escalate, cancel, or retry.

## 8. Least privilege

The system prefers:

```text
minimum capability
× minimum resource scope
× minimum execution scope
× minimum duration
× minimum data disclosure
```

over standing broad access.

## 9. Security enforcement is not provider IAM

UPOS-010 defines universal semantics. UPOS-011 later binds those semantics to concrete identities, provider permissions, secret stores, environment IDs, repository protections and external approval systems.

A provider-native credential may be broader than a U-POS Permission Decision. U-POS authorization MUST still enforce its own semantic scope.

## 10. Non-bypass invariants

```text
Quality PASS cannot override Security DENY.
Human approval cannot override Security policy unless policy explicitly permits that approval/override route.
Security Exception cannot silently delete or mutate the underlying policy.
Break-glass cannot become standing ordinary access.
Tool capability cannot bypass permission evaluation.
```
