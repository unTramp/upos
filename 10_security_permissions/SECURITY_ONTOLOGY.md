# Security Ontology

**ID:** UPOS-10-ONT-001  
**Type:** ONTOLOGY  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. SECURITY SUBJECT

A Security Subject is the already-identifiable actor/execution identity on whose behalf a capability is requested or held.

It may reference:

```text
human identity reference
role_id
agent_instance_ref
agent_run_id
service identity reference
automation identity reference
```

UPOS-010 does not create a universal identity provider or competing actor identity namespace.

## 2. CAPABILITY

A provider-neutral abstract action class that may be requested or granted, for example:

```text
repository-read
repository-write
commit
push
merge
history-rewrite
read-project-documentation
write-project-documentation
read-sensitive-context
read-secret
use-secret
execute-test
execute-build
deploy
production-read
production-write
production-admin
permission-admin
```

A Capability says what class of power is relevant, not whether the subject may use it now.

## 3. ACTION

The concrete intended operation inside a Capability class.

Example:

```text
capability = repository-write
action     = update file within exact RCU scope
```

## 4. RESOURCE

The protected target against which the action is evaluated. Resource identity is supplied by the canonical project/provider owner.

Abstract types include:

```text
repository
branch / protected target
file/path scope
documentation source
Context source
environment
secret
service
database
data set / record scope
production system
artifact
deployment target
permission policy target
```

## 5. PERMISSION REQUEST

A stable attributable request to evaluate one intended security use.

Identity:

```text
permission_request_id
```

## 6. PERMISSION DECISION

An immutable evaluation snapshot for one Permission Request under one applicable policy/basis state.

Identity:

```text
permission_decision_id
```

## 7. GRANT

A bounded governed allowance for a subject to hold/use a Capability within specified resource/execution scope, conditions and lifetime.

Identity:

```text
grant_id
```

Grant does not equal current permission.

## 8. PROTECTED ACTION

A concrete action instance that policy classifies as requiring elevated controls such as current permission decision, stronger authentication, Human Approval, SoD, exception, time-bound elevation, or enhanced audit.

Identity:

```text
protected_action_id
```

## 9. APPROVAL CONDITION

A requirement that a referenced externally governed decision/approval be present and valid before Permission Decision can become `ALLOW`.

UPOS-010 does not create `security_approval_id` in v1.

## 10. SECRET

Sensitive credential/key/token/material whose raw value requires protected handling. Secret identity/reference remains provider/project-owned.

UPOS-010 owns access/use/disclosure semantics, not secret storage implementation.

## 11. SECURITY EXCEPTION

A bounded externally authorized departure from an otherwise applicable Security Policy rule, preserving the original rule and compensating controls.

Identity:

```text
security_exception_id
```

## 12. SECURITY VETO

A security-policy consequence that prevents an action within a scope where external organizational/governance authority grants Security a veto.

Veto has no separate Module-10 ID. It is represented by an attributable `DENY` Permission Decision plus authority/policy basis refs.

## 13. SECURITY POLICY

A versioned governed source defining permission/security rules. UPOS-010 references:

```text
security_policy_ref
security_policy_version
```

It does not create a duplicate global `security_policy_id` database.

## 14. SECURITY AUDIT REQUIREMENT

A semantic requirement that a security-relevant action/decision must produce attributable, minimized audit metadata. UPOS-008 will own event/audit projection mechanics after reconciliation.
