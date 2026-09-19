# Cross-Module Security Interfaces

**ID:** UPOS-10-XMI-001  
**Type:** INTERFACE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## UPOS-01 — Documentation / Source of Truth / Knowledge

UPOS-010 consumes:

```text
canonical Security Policy source resolution
active normative conflict handling
Decision/approval provenance
knowledge promotion governance
```

It does not redefine project truth. Policy conflict resolves through UPOS-01 governance.

## UPOS-002 — Agent Organization

Consumes:

```text
role_id
agent_definition_id/version
agent_run_id
organizational authority refs
delegation refs
SoD relationships
Human Governance / veto / override authority refs
```

Boundary:

```text
ORGANIZATIONAL AUTHORITY → UPOS-002
TECHNICAL PERMISSION     → UPOS-010
```

## UPOS-003 — Skills

Consumes Capability requirements declared by Skills.

```text
Skill requires capability
!= capability granted
```

Skill procedures remain UPOS-003.

## UPOS-004 — Workflow Engine

Workflow may place Security Gate / Human Approval / Protected Action checkpoints.

UPOS-010 emits substantive results:

```text
ALLOW / DENY / CONDITIONAL / BLOCKED / UNKNOWN
approval required
security veto basis
protected-action authorization status
```

UPOS-004 owns what the Workflow does next.

## UPOS-005 — Context & Memory

UPOS-010 determines whether a source/sensitive data may be accessed and may return:

```text
ALLOW_FULL
ALLOW_REDACTED
REFERENCE_ONLY
DENY
```

UPOS-005 owns retrieval, assembly, Context Bundle representation and memory semantics.

## UPOS-006 — Engineering Governance

UPOS-006 declares/attempts engineering actions and exact engineering resources.

UPOS-010 decides whether the subject may use required capabilities now.

```text
repository/Git mechanics → UPOS-006
permission to perform action → UPOS-010
```

## UPOS-007 — Quality System

```text
Quality PASS != Security approval
Security approval != Quality PASS
```

UPOS-010 may consume Quality readiness/Assessment/Gate refs as Security Policy conditions without redefining their meaning.

Security review is distinct from Permission Decision.

## UPOS-008 — Observability

Observable Security refs:

```text
permission_request_id
permission_decision_id
grant_id + lifecycle refs
protected_action_id + status/outcome refs
security_exception_id + lifecycle/use refs
security_policy_ref/version
security reason/result refs
break-glass/elevation refs
secret/sensitive-data access decision metadata
```

Policy-scoped handling constraints may include:

```text
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

UPOS-008 owns Event/Trace/storage/metric/read-model mechanics. Raw secrets/protected payload values MUST NOT be emitted.

Status: `RECONCILED`.

## UPOS-009 — Learning

Security outcomes may become Learning evidence through attributable refs, including repeated denials/exceptions, repeated missing approvals, over-broad/long-lived Grants, frequent break-glass use and protected-action failures.

UPOS-009 may detect/generalize Learning Candidates. It MUST NOT change Security Policy, create/revoke Grants, approve Exceptions, convert Learning into permission or override Security decisions.

Status: `RECONCILED`.

## UPOS-011 — Project Adapter

UPOS-011 binds:

```text
Security Subject → provider/runtime identity
universal Capability → provider-native mechanism/scope
Security Resource → physical provider/project resource
Grant enforcement → runtime/provider controls
secret_ref → secret-store binding / secure injection
Protected Action target → concrete protected resource
approval requirement → external approval system
elevation / reauthentication → provider mechanism
break-glass requirement → concrete emergency mechanism
security handling constraints → concrete storage/access/redaction/retention enforcement
```

```text
provider credential/scope != UPOS-010 Permission Decision
```

UPOS-010 owns semantics; UPOS-011 owns physical binding/enforcement adapters.

Status: `RECONCILED`.
