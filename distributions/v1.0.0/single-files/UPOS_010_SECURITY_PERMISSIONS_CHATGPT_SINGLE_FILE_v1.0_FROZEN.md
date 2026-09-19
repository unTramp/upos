# UPOS-010 Security & Permissions — ChatGPT Single-File Edition v1.0 FROZEN

**Module:** UPOS-010 — Security & Permissions  
**System:** Universal Project Operating System  
**Status:** FROZEN v1.0  
**Freeze:** FROZEN v1.0  
**Reconciliation:** COMPLETE — UPOS-008, UPOS-009, UPOS-011  
**Embedded virtual files:** 44  
**Generated:** 2026-09-20

---

# 0. Interpretation rule

This is a transport bundle, not a replacement monolith.

Each `VIRTUAL FILE` block represents one repository file under `10_security_permissions/`.

Normative authority remains with embedded ACTIVE/NORMATIVE artifacts. `analysis/` is historical EVIDENCE only.

## Final validation

```text
UPOS-010 INTERNAL IMPLEMENTATION = COMPLETE
UNMAPPED MODULE-10 SOURCE REQUIREMENTS = 0
Unresolved internal P0/P1 gaps = 0
Template conformance = PASS
Hard-coded project/provider bindings = 0
UPOS-008 reconciliation = COMPLETE
UPOS-009 reconciliation = COMPLETE
UPOS-011 reconciliation = COMPLETE
UPOS-010 FREEZE = FROZEN v1.0
```

# 1. Virtual repository tree

```text
10_security_permissions/
├── CAPABILITY_MODEL.md
├── CROSS_MODULE_INTERFACES.md
├── GRANT_STANDARD.md
├── HUMAN_APPROVAL_AND_VETO.md
├── LEAST_PRIVILEGE_STANDARD.md
├── MODULE_10_DEFINITION_OF_DONE.md
├── MODULE_10_TRACEABILITY.md
├── PERMISSION_DECISION_STANDARD.md
├── PERMISSION_REQUEST_STANDARD.md
├── PRODUCTION_ACCESS_STANDARD.md
├── PROTECTED_ACTION_STANDARD.md
├── README.md
├── RESOURCE_AND_ACTION_MODEL.md
├── SECRET_AND_SENSITIVE_DATA_STANDARD.md
├── SECURITY_AUDIT_REQUIREMENTS.md
├── SECURITY_EXCEPTION_STANDARD.md
├── SECURITY_FAILURE_MODEL.md
├── SECURITY_LIFECYCLE_AND_VERSIONING.md
├── SECURITY_ONTOLOGY.md
├── SECURITY_PERMISSIONS_OPERATING_MODEL.md
├── SECURITY_POLICY_STANDARD.md
├── SUBJECT_AND_IDENTITY_INTERFACE.md
├── VIRTUAL_REPOSITORY_TREE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md
├── analysis/CAPABILITY_MODEL_ANALYSIS.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MODULE_10_OWNERSHIP_MAP.md
├── analysis/PRODUCTION_ACCESS_ANALYSIS.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/PROTECTED_ACTION_ANALYSIS.md
├── analysis/SECRET_HANDLING_ANALYSIS.md
├── analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md
├── analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md
├── analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md
├── templates/GRANT_TEMPLATE.md
├── templates/PERMISSION_DECISION_TEMPLATE.md
├── templates/PERMISSION_REQUEST_TEMPLATE.md
├── templates/PROTECTED_ACTION_TEMPLATE.md
├── templates/SECURITY_EXCEPTION_TEMPLATE.md
```

# 2. Embedded files


---

## VIRTUAL FILE 1/44 — `CAPABILITY_MODEL.md`

**Virtual path:** `CAPABILITY_MODEL.md`  
**Content checksum:** `deeeb35ab9ff`

===== BEGIN VIRTUAL FILE: CAPABILITY_MODEL.md =====

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
===== END VIRTUAL FILE: CAPABILITY_MODEL.md =====

---

## VIRTUAL FILE 2/44 — `CROSS_MODULE_INTERFACES.md`

**Virtual path:** `CROSS_MODULE_INTERFACES.md`  
**Content checksum:** `ec91fd6f8e2f`

===== BEGIN VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

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
===== END VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

---

## VIRTUAL FILE 3/44 — `GRANT_STANDARD.md`

**Virtual path:** `GRANT_STANDARD.md`  
**Content checksum:** `17b78fa98b42`

===== BEGIN VIRTUAL FILE: GRANT_STANDARD.md =====

# Grant Standard

**ID:** UPOS-10-GRT-001  
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

A Grant is a bounded technical allowance substrate.

```text
GRANT != ORGANIZATIONAL AUTHORITY
GRANT != ORGANIZATIONAL DELEGATION
GRANT != CURRENT PERMISSION DECISION
```

## 2. Identity

```text
grant_id
```

## 3. Minimum contract

```text
grant_id
status

subject_ref
role_ref
agent_run_scope_ref
task_scope_ref
workflow_scope_ref
stage_scope_ref

capability
allowed_actions
resource_type
resource_ref
resource_scope

conditions
security_policy_ref
security_policy_version
originating_permission_decision_ref
originating_authority_or_delegation_ref

created_at
effective_from
expires_at
revoked_at
revocation_reason
supersedes
replacement
status_history
```

## 4. Lifecycle

Canonical v1 states:

```text
PENDING
ACTIVE
SUSPENDED
EXPIRED
REVOKED
SUPERSEDED
```

Only `ACTIVE` may satisfy a current decision input.

## 5. Lifecycle semantics

- `PENDING` — grant record exists but is not effective.
- `ACTIVE` — effective within exact scope/conditions/time.
- `SUSPENDED` — temporarily unavailable; may later return to ACTIVE if policy allows.
- `EXPIRED` — terminal expiry due time/end condition.
- `REVOKED` — terminal administrative/security revocation.
- `SUPERSEDED` — replaced by another grant identity.

All status changes preserve append-only history.

## 6. Time-bounded access

Elevated/production/secret-admin grants SHOULD be temporary by default.

Indefinite standing privilege requires explicit project/security policy justification.

## 7. Invalidation/revocation triggers

Potential triggers include:

```text
Agent Run ended
Task completed/cancelled
Workflow rerouted materially
Role/authority changed
resource scope changed
policy version changed
approval revoked
risk/security context increased
security incident
manual authorized revocation
expiry
```

The exact trigger set is policy-specific.

## 8. Technical delegation

A technical Grant may be created from an externally governed organizational delegation only when:

```text
delegation/authority ref exists
+ Security Policy permits technical grant
```

The Grant does not expand the organizational delegation.

## 9. Supersession

Material scope/capability/subject/lifetime changes create a new `grant_id` and supersede the old Grant rather than silently rewriting historical authorization.
===== END VIRTUAL FILE: GRANT_STANDARD.md =====

---

## VIRTUAL FILE 4/44 — `HUMAN_APPROVAL_AND_VETO.md`

**Virtual path:** `HUMAN_APPROVAL_AND_VETO.md`  
**Content checksum:** `d119cac5c739`

===== BEGIN VIRTUAL FILE: HUMAN_APPROVAL_AND_VETO.md =====

# Human Approval & Security Veto

**ID:** UPOS-10-HAV-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Human approval boundary

```text
Human Governance / who may approve
→ UPOS-002

Security requirement that approval be present
→ UPOS-010
```

UPOS-010 references an external decision/approval artifact and validates its applicability to the security request.

No `security_approval_id` is introduced in v1.

## 2. Approval does not automatically grant permission

```text
Human approval present
!= ALLOW
```

Approval may satisfy one Security condition. All other current policy conditions must still be satisfied and a current applicable `ALLOW` Permission Decision must exist.

## 3. Approval applicability

A required approval must be:

```text
from externally authorized approver/authority
applicable to exact subject/action/resource/scope
applicable to required time/window
not revoked/superseded
compatible with applicable policy
```

## 4. Security veto

Security veto requires an external authority basis from UPOS-002/project governance and an applicable Security rule.

```text
Security authority basis
+ security condition prohibiting action
→ DENY Permission Decision
+ veto_basis_ref
```

UPOS-010 MUST NOT silently invent veto authority.

## 5. Override

Human or other override authority is externally governed.

An override can affect security only if applicable Security Policy explicitly permits an override/exception path.

Otherwise:

```text
Human Override request
+ non-overridable Security DENY
→ still DENY
```

## 6. SoD enforcement

UPOS-002 owns SoD rules. UPOS-010 may technically enforce them by consuming relationship/authority references.

Example:

```text
Implementer attempting own high-risk merge
+ applicable SoD rule
→ DENY / SOD_VIOLATION
```

The source SoD rule remains UPOS-002/project policy.
===== END VIRTUAL FILE: HUMAN_APPROVAL_AND_VETO.md =====

---

## VIRTUAL FILE 5/44 — `LEAST_PRIVILEGE_STANDARD.md`

**Virtual path:** `LEAST_PRIVILEGE_STANDARD.md`  
**Content checksum:** `6897cc9bc371`

===== BEGIN VIRTUAL FILE: LEAST_PRIVILEGE_STANDARD.md =====

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
===== END VIRTUAL FILE: LEAST_PRIVILEGE_STANDARD.md =====

---

## VIRTUAL FILE 6/44 — `MODULE_10_DEFINITION_OF_DONE.md`

**Virtual path:** `MODULE_10_DEFINITION_OF_DONE.md`  
**Content checksum:** `f478a8756212`

===== BEGIN VIRTUAL FILE: MODULE_10_DEFINITION_OF_DONE.md =====

# Module 10 Definition of Done

**ID:** UPOS-10-DOD-001  
**Type:** DEFINITION OF DONE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## v1 implementation DoD

```text
[x] Authority != Permission explicit
[x] Role != Permission explicit
[x] capability model exists
[x] resource/action model exists
[x] permission request stable identity exists
[x] permission decision stable identity exists
[x] grant model exists
[x] least privilege explicit
[x] default-deny/unknown behavior defined
[x] conditional permission exists
[x] permission freshness/revalidation exists
[x] protected action model exists
[x] Human Approval boundary correct
[x] security veto semantics defined
[x] security exception model exists
[x] secrets model exists
[x] secret disclosure minimized
[x] raw secrets prohibited in telemetry/audit payloads
[x] sensitive Context policy interface exists
[x] production access model exists
[x] break-glass analyzed
[x] temporary privilege elevation exists
[x] SoD enforcement consumes UPOS-002
[x] Workflow response remains UPOS-004
[x] Quality remains UPOS-007
[x] Context assembly remains UPOS-005
[x] provider IAM remains UPOS-011
[x] Security audit interface exists
[x] failure taxonomy exists
[x] policy versioning exists
[x] no hard-coded project/provider bindings
[x] templates conform
[x] no unresolved internal P0/P1 gaps
```

## Freeze validation

```text
[x] UPOS-008 reconciliation complete
[x] UPOS-009 reconciliation complete
[x] UPOS-011 reconciliation complete
[x] security handling constraints reconciled with Observability mechanics
[x] coordinated interface-stable convergence criterion satisfied
[x] final traceability/template validation rerun
[x] no known ownership leakage into UPOS-01–09 / 011
```

```text
UPOS-010 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-010 FREEZE:
FROZEN v1.0
```
===== END VIRTUAL FILE: MODULE_10_DEFINITION_OF_DONE.md =====

---

## VIRTUAL FILE 7/44 — `MODULE_10_TRACEABILITY.md`

**Virtual path:** `MODULE_10_TRACEABILITY.md`  
**Content checksum:** `33fe3d2d4144`

===== BEGIN VIRTUAL FILE: MODULE_10_TRACEABILITY.md =====

# Module 10 Traceability

**ID:** UPOS-10-TRACE-001  
**Type:** TRACEABILITY / COVERAGE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline



## 0.1 Final baseline fingerprints

```text
Frozen master SHA-256: f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699
UPOS-001 SHA-256: 0eed3f1319103b9fef7956519da9754986b7c512a05278c030c38edbaddcb3a1
UPOS-002 SHA-256: 34274f4f102150826e599def36b940d23c15a66a8b0be4b8f5e01964cc1dc043
UPOS-003 SHA-256: 94726e67917808cee0ca3a62d04ce22cdd9b3ad213ea69a93e630336159945ad
UPOS-004 SHA-256: abf2fbc069af77a70cf6ee2b1242435c6a510b7196b2cac92f03e91e5b09fae1
UPOS-005 SHA-256: 186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528
UPOS-006 SHA-256: 49301fa994e2d47c146f84260e4783585c950faf0c73dbe129767c2c2c95e45e
UPOS-007 SHA-256: 36c52764ccafdfef053d224ec1af5d297e3cd6eceacbc45d287d4bc96a1833b0
UPOS-008 final SHA-256: e6eed6e9d7e006a5bf3a3d9baa300d8917f6d9ccb3e76c6301a9fcef1b25a0ba
UPOS-009 final SHA-256: 76f8e1c43ae35890a63d527acdc285d25ea6c6494b2aa2af9839928dbb923fbb
```

## 1. Coverage contract

This is the canonical v1 coverage artifact for Module 10. All extracted Module-10 requirements from the directive, frozen master and upstream 01–07 interfaces are mapped below.

| Requirement | Source | Normalized requirement | Canonical target |
|---|---|---|---|
| `SEC-REQ-001` | Directive §0 | Module 10 answers concrete subject/capability/action/resource permission question | `README.md; SECURITY_PERMISSIONS_OPERATING_MODEL.md` |
| `SEC-REQ-002` | Directive §1 | Organizational authority != technical permission | `README.md; SECURITY_PERMISSIONS_OPERATING_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-003` | Directive §2 | ROLE != PERMISSION | `README.md` |
| `SEC-REQ-004` | Directive §2 | AUTHORITY != CAPABILITY GRANT | `README.md; GRANT_STANDARD.md` |
| `SEC-REQ-005` | Directive §2 | CAPABILITY != PERMISSION TO USE IT NOW | `README.md; CAPABILITY_MODEL.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-006` | Directive §2 | TOOL ACCESS != ACTION AUTHORIZATION | `README.md; CAPABILITY_MODEL.md` |
| `SEC-REQ-007` | Directive §2/§56 | QUALITY PASS != SECURITY APPROVAL | `README.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-008` | Directive §2/§55 | WORKFLOW STAGE != PERMISSION | `README.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-009` | Directive §2/§37 | SECRET ACCESS != SECRET OWNERSHIP | `README.md; SECRET_AND_SENSITIVE_DATA_STANDARD.md` |
| `SEC-REQ-010` | Directive §2/§33 | Human Approval is an external security condition, not automatic permission | `HUMAN_APPROVAL_AND_VETO.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-011` | Directive §3 | Core actor→capability→resource→policy→decision chain | `SECURITY_PERMISSIONS_OPERATING_MODEL.md` |
| `SEC-REQ-012` | Directive §§4–12 | Cross-module ownership boundaries explicit | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-013` | Directive §13 | Security ontology defined | `SECURITY_ONTOLOGY.md` |
| `SEC-REQ-014` | Directive §14 | permission_request_id stable | `PERMISSION_REQUEST_STANDARD.md` |
| `SEC-REQ-015` | Directive §14 | permission_decision_id stable | `PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-016` | Directive §14 | grant_id stable | `GRANT_STANDARD.md` |
| `SEC-REQ-017` | Directive §14/§32 | protected_action_id stable | `PROTECTED_ACTION_STANDARD.md` |
| `SEC-REQ-018` | Directive §14/§35 | security_exception_id stable | `SECURITY_EXCEPTION_STANDARD.md` |
| `SEC-REQ-019` | Directive §14/§33 | No duplicate security_approval_id | `SECURITY_ONTOLOGY.md; HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-020` | Directive §§15–16 | Security Subject reuses upstream/provider identities and narrow execution scope | `SUBJECT_AND_IDENTITY_INTERFACE.md` |
| `SEC-REQ-021` | Directive §§17–18 | Provider-neutral capability model | `CAPABILITY_MODEL.md` |
| `SEC-REQ-022` | Directive §§19–20 | Resource/action/scope/context tuple model | `RESOURCE_AND_ACTION_MODEL.md` |
| `SEC-REQ-023` | Directive §21 | Least privilege hard principle | `LEAST_PRIVILEGE_STANDARD.md` |
| `SEC-REQ-024` | Directive §22 | Protected capability defaults to non-executable absent current allow | `README.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-025` | Directive §23 | Decision vocabulary precise | `PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-026` | Directive §24 | Conditional permission is non-executable and externally conditionable | `PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-027` | Directive §25 | Permission Request contract | `PERMISSION_REQUEST_STANDARD.md; templates/PERMISSION_REQUEST_TEMPLATE.md` |
| `SEC-REQ-028` | Directive §26 | Permission Decision contract | `PERMISSION_DECISION_STANDARD.md; templates/PERMISSION_DECISION_TEMPLATE.md` |
| `SEC-REQ-029` | Directive §27 | Grant contract | `GRANT_STANDARD.md; templates/GRANT_TEMPLATE.md` |
| `SEC-REQ-030` | Directive §28 | Elevated access time-bounded by default | `LEAST_PRIVILEGE_STANDARD.md; PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-031` | Directive §29 | Grant invalidation/revocation preserves history | `GRANT_STANDARD.md; SECURITY_LIFECYCLE_AND_VERSIONING.md` |
| `SEC-REQ-032` | Directive §30 | Permission freshness/revalidation | `PERMISSION_DECISION_STANDARD.md; SECURITY_LIFECYCLE_AND_VERSIONING.md` |
| `SEC-REQ-033` | Directive §§31–32 | Protected action model/contract | `PROTECTED_ACTION_STANDARD.md; templates/PROTECTED_ACTION_TEMPLATE.md` |
| `SEC-REQ-034` | Directive §33 | Human Governance authority remains UPOS-002 | `HUMAN_APPROVAL_AND_VETO.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-035` | Directive §34 | Security veto requires external authority and maps to DENY | `HUMAN_APPROVAL_AND_VETO.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-036` | Directive §§35–36 | Security Exception contract preserves policy | `SECURITY_EXCEPTION_STANDARD.md; templates/SECURITY_EXCEPTION_TEMPLATE.md` |
| `SEC-REQ-037` | Directive §§37–39 | Secret semantics and raw telemetry prohibition | `SECRET_AND_SENSITIVE_DATA_STANDARD.md; SECURITY_AUDIT_REQUIREMENTS.md` |
| `SEC-REQ-038` | Directive §40 | Sensitive Context access directives | `SECRET_AND_SENSITIVE_DATA_STANDARD.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-039` | Directive §41 | Data minimization | `SECRET_AND_SENSITIVE_DATA_STANDARD.md; LEAST_PRIVILEGE_STANDARD.md` |
| `SEC-REQ-040` | Directive §42 | Cross-project isolation | `SUBJECT_AND_IDENTITY_INTERFACE.md; SECRET_AND_SENSITIVE_DATA_STANDARD.md` |
| `SEC-REQ-041` | Directive §43 | Environment semantics abstract/provider-neutral | `PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-042` | Directive §§44–45 | Production read/write/admin/deploy separated and elevated | `PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-043` | Directive §46 | Break-glass controlled and non-routine | `PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-044` | Directive §47 | Technical delegation requires external organizational delegation | `GRANT_STANDARD.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-045` | Directive §48 | SoD rule consumed from UPOS-002 and technically enforceable | `HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-046` | Directive §49 | Tool access does not imply all tool operations | `CAPABILITY_MODEL.md; README.md` |
| `SEC-REQ-047` | Directive §50 | Provider permission binding deferred to UPOS-011 | `CAPABILITY_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-048` | Directive §51 | Versioned Security Policy reference model | `SECURITY_POLICY_STANDARD.md` |
| `SEC-REQ-049` | Directive §52 | Policy conflict blocks; do not guess | `SECURITY_POLICY_STANDARD.md; SECURITY_FAILURE_MODEL.md` |
| `SEC-REQ-050` | Directive §53 | Material DENY explainable by reason code/policy ref | `PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-051` | Directive §54 | Security failure taxonomy | `SECURITY_FAILURE_MODEL.md` |
| `SEC-REQ-052` | Directive §55 | Workflow response remains UPOS-004 | `SECURITY_FAILURE_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-053` | Directive §56 | Security and Quality remain independent | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-054` | Directive §57 | Security access/redaction directive separate from Context representation | `SECRET_AND_SENSITIVE_DATA_STANDARD.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-055` | Directive §58 | Engineering action mechanics remain UPOS-006 | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-056` | Directive §§59,62–63,73 | Audit semantics defined; observability projection deferred; no raw secrets | `SECURITY_AUDIT_REQUIREMENTS.md; analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md` |
| `SEC-REQ-057` | Directive §60 | Learning receives security patterns but cannot mutate policy | `CROSS_MODULE_INTERFACES.md; analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md` |
| `SEC-REQ-058` | Directive §61 | Provider/project adapter bindings deferred | `CROSS_MODULE_INTERFACES.md; analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md` |
| `SEC-REQ-059` | Directive §64 | Decision explainability/reproducibility | `SECURITY_POLICY_STANDARD.md; SECURITY_AUDIT_REQUIREMENTS.md` |
| `SEC-REQ-060` | Directive §65 | Permission result does not mutate Workflow/Quality/Engineering state | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-061` | Directive §66 | Missing security information never defaults to ALLOW | `PERMISSION_DECISION_STANDARD.md; README.md` |
| `SEC-REQ-062` | Directive §67 | Read-only fallback only if policy-defined | `LEAST_PRIVILEGE_STANDARD.md` |
| `SEC-REQ-063` | Directive §68 | Action purpose uses governed refs | `RESOURCE_AND_ACTION_MODEL.md; PERMISSION_REQUEST_STANDARD.md` |
| `SEC-REQ-064` | Directive §69 | Explicit privilege elevation flow | `PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-065` | Directive §70 | Reauthentication is external condition, provider mechanics deferred | `PRODUCTION_ACCESS_STANDARD.md; SUBJECT_AND_IDENTITY_INTERFACE.md` |
| `SEC-REQ-066` | Directive §71 | Resource inheritance only if policy-defined | `RESOURCE_AND_ACTION_MODEL.md` |
| `SEC-REQ-067` | Directive §72 | Wildcards explicit/inspectable/minimized | `LEAST_PRIVILEGE_STANDARD.md; RESOURCE_AND_ACTION_MODEL.md` |
| `SEC-REQ-068` | Directive §74 | Security Review != Permission Decision | `README.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-069` | Directive §75 | Protected Action != high-risk Change Class | `PROTECTED_ACTION_STANDARD.md` |
| `SEC-REQ-070` | Directive §76 | Decision records policy ref/version | `PERMISSION_DECISION_STANDARD.md; SECURITY_POLICY_STANDARD.md` |
| `SEC-REQ-071` | Directive §77 | Grant lifecycle | `GRANT_STANDARD.md; SECURITY_LIFECYCLE_AND_VERSIONING.md` |
| `SEC-REQ-072` | Directive §78 | Exception lifecycle | `SECURITY_EXCEPTION_STANDARD.md; SECURITY_LIFECYCLE_AND_VERSIONING.md` |
| `SEC-REQ-073` | Directive §79 | Minimal Protected Action lifecycle without Workflow duplication | `PROTECTED_ACTION_STANDARD.md; SECURITY_LIFECYCLE_AND_VERSIONING.md` |
| `SEC-REQ-074` | Directive §§80–81 | Required package and analysis-first artifacts implemented | `VIRTUAL_REPOSITORY_TREE.md; analysis/*` |
| `SEC-REQ-075` | Directive §82 | Ambiguity register resolved | `analysis/AMBIGUITY_GAP_REGISTER.md` |
| `SEC-REQ-076` | Directive §83 | Canonical traceability with SEC-REQ IDs | `MODULE_10_TRACEABILITY.md` |
| `SEC-REQ-077` | Directive §84 | Five templates conform to Standards | `templates/*; analysis/TRACEABILITY_VALIDATION.md` |
| `SEC-REQ-078` | Directive §86 | Provisional DoD complete internally | `MODULE_10_DEFINITION_OF_DONE.md` |
| `SEC-REQ-079` | Directive §87 | 008/009/011 interfaces explicitly reconciled before coordinated freeze | `README.md; analysis/*_INTERFACE_RECONCILIATION_REGISTER.md` |
| `SEC-REQ-080` | Directive §88 | Final reconciliation/freeze status explicit | `README.md` |
| `SEC-REQ-081` | Directive §89 | Main protected-action acceptance criterion represented | `SECURITY_PERMISSIONS_OPERATING_MODEL.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-082` | Frozen master §3.6 | Least privilege preserved | `LEAST_PRIVILEGE_STANDARD.md` |
| `SEC-REQ-083` | Frozen master §16 | Security specialist conditional/scoped; authority not universal | `CROSS_MODULE_INTERFACES.md; HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-084` | Frozen master §38 | Permission model extracted into provider-neutral capabilities | `CAPABILITY_MODEL.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-085` | Frozen master §39 | Role permission philosophy normalized without making Role=Permission | `SUBJECT_AND_IDENTITY_INTERFACE.md; HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-086` | Frozen master §40 | Human approval preserved as governed condition | `HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-087` | Frozen master §68 | Security Gate semantics separated from Workflow placement | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-088` | Frozen master §75 | Permission/production guardrail intent preserved | `PROTECTED_ACTION_STANDARD.md; PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-089` | Frozen master §§77–78 | Security failures/escalation targets separated from Workflow handling | `SECURITY_FAILURE_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-090` | Frozen master §110 | Secrets least privilege / explicit modification policy preserved | `SECRET_AND_SENSITIVE_DATA_STANDARD.md` |
| `SEC-REQ-091` | Frozen master §111 | No unrestricted production mutation by default | `PRODUCTION_ACCESS_STANDARD.md` |
| `SEC-REQ-092` | Frozen master §112 | Protected resources supported without hard-coded paths | `RESOURCE_AND_ACTION_MODEL.md; PROTECTED_ACTION_STANDARD.md` |
| `SEC-REQ-093` | Frozen master §123 | Authority conflict resolution remains upstream; security consumes refs | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-094` | Frozen master §124 | Security veto normalized | `HUMAN_APPROVAL_AND_VETO.md; PERMISSION_DECISION_STANDARD.md` |
| `SEC-REQ-095` | Frozen master §127 | Human override cannot silently bypass non-overridable security rule | `HUMAN_APPROVAL_AND_VETO.md; SECURITY_EXCEPTION_STANDARD.md` |
| `SEC-REQ-096` | UPOS-01 governance | Permission/security policy canonical owner/source resolved by scope, not implementation evidence | `SECURITY_POLICY_STANDARD.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-097` | UPOS-002 frozen | Role/authority/delegation/SoD/Human Governance remain UPOS-002 | `CROSS_MODULE_INTERFACES.md; HUMAN_APPROVAL_AND_VETO.md` |
| `SEC-REQ-098` | UPOS-003 frozen | Skills declare requirements but grant nothing | `CAPABILITY_MODEL.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-099` | UPOS-004 frozen | Workflow protected checkpoint placement external; security result consumed | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-100` | UPOS-005 frozen | Security decides source access/redaction; Context assembly remains UPOS-005 | `SECRET_AND_SENSITIVE_DATA_STANDARD.md; CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-101` | UPOS-006 frozen | Engineering action/resource mechanics external; permission current-use owned by 010 | `CROSS_MODULE_INTERFACES.md` |
| `SEC-REQ-102` | UPOS-007 frozen | Quality result never substitutes Security approval/permission | `CROSS_MODULE_INTERFACES.md` |

## 2. Coverage assertion

```text
MODULE-10 REQUIREMENTS MAPPED = 102
UNMAPPED MODULE-10 SOURCE REQUIREMENTS = 0
```

## 3. Final reconciliation status

```text
UPOS-008 interface reconciliation = COMPLETE
UPOS-009 interface reconciliation = COMPLETE
UPOS-011 interface reconciliation = COMPLETE
UPOS-010 freeze = FROZEN v1.0

UNMAPPED MODULE-10 SOURCE REQUIREMENTS = 0
NO KNOWN OWNERSHIP LEAKAGE INTO UPOS-01–09 / 011
```

These reconciliations close interface dependencies without moving Security ownership.
===== END VIRTUAL FILE: MODULE_10_TRACEABILITY.md =====

---

## VIRTUAL FILE 8/44 — `PERMISSION_DECISION_STANDARD.md`

**Virtual path:** `PERMISSION_DECISION_STANDARD.md`  
**Content checksum:** `a84297393be0`

===== BEGIN VIRTUAL FILE: PERMISSION_DECISION_STANDARD.md =====

# Permission Decision Standard

**ID:** UPOS-10-PDS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity

Every completed security evaluation has stable:

```text
permission_decision_id
```

A Permission Decision is an immutable evaluation snapshot for one `permission_request_id` under one exact policy/context/basis state.

## 2. Decision vocabulary

```text
ALLOW
DENY
CONDITIONAL
BLOCKED
UNKNOWN
```

### ALLOW

All applicable Security conditions are satisfied now for the exact request, scope and validity window.

`ALLOW` is the only decision state that can authorize execution.

### DENY

At least one authoritative applicable Security rule definitively forbids the request or an unexcepted security veto applies.

### CONDITIONAL

The request could become allowable if one or more explicit conditions are satisfied, for example:

```text
Human Approval ref present
required organizational authority ref present
Quality readiness ref acceptable
stronger authentication/elevation satisfied
SoD condition satisfied
specific Grant activated
```

`CONDITIONAL` is not executable. When conditions change, produce a new Permission Decision unless an explicit policy-controlled activation mechanism is defined and attributable.

### BLOCKED

Evaluation cannot validly complete because a required authoritative prerequisite is missing/conflicted/unavailable.

Examples:

```text
security policy conflict
required subject identity unresolved
required resource identity unavailable
external approval state unavailable
provider enforcement state required but unavailable
```

### UNKNOWN

No authoritative applicable security rule/context can be resolved.

For protected capability use:

```text
UNKNOWN → not executable
```

Escalate to policy/owner resolution; do not default to ALLOW.

## 3. Minimum contract

```text
permission_decision_id
permission_request_id

decision
security_policy_ref
security_policy_version

subject_ref
capability
action
resource_ref
resource_scope
resource_state_ref

applicable_grant_refs
security_exception_refs
required_authority_refs
required_approval_refs
satisfied_condition_refs
unsatisfied_conditions

protected_action_id
denial_reason_code
reason_summary
veto_basis_ref

security_context_refs
basis_refs

effective_from
expires_at
revalidation_triggers

evaluated_by_ref
created_at
```

## 4. Grant relationship

`grant_ref`/`applicable_grant_refs` may contribute to `ALLOW`, but an active Grant does not force `ALLOW` if other current policy conditions fail.

## 5. Human approval relationship

Human Approval is an external condition ref. Approval does not mutate a historical `CONDITIONAL`/`DENY` decision to `ALLOW`; current execution requires a current applicable `ALLOW` decision.

## 6. Freshness / invalidation

A prior `ALLOW` becomes non-reusable when any material decision input changes, including:

```text
subject/Role/Run state
Task/Workflow/Stage scope
resource/scope/state
policy/version
grant status/expiry
approval status
SoD relationship
exception status
security context
protection classification
```

The old Decision remains historical provenance.

## 7. Denial explainability

Material `DENY` MUST include attributable:

```text
denial_reason_code
policy/basis ref
relevant missing/prohibited condition
```

Do not rely on opaque `permission denied` where the system can safely explain the security reason.

## 8. Security veto

A scoped Security veto is represented as `DENY` with:

```text
veto_basis_ref
required external authority source
policy ref/version
```

UPOS-010 does not create veto authority itself.
===== END VIRTUAL FILE: PERMISSION_DECISION_STANDARD.md =====

---

## VIRTUAL FILE 9/44 — `PERMISSION_REQUEST_STANDARD.md`

**Virtual path:** `PERMISSION_REQUEST_STANDARD.md`  
**Content checksum:** `6144c1fd5da5`

===== BEGIN VIRTUAL FILE: PERMISSION_REQUEST_STANDARD.md =====

# Permission Request Standard

**ID:** UPOS-10-PRS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity

Every independently evaluated permission request has stable:

```text
permission_request_id
```

A new materially different intended action/resource/security scope creates a new request identity.

## 2. Minimum contract

```text
permission_request_id

subject_type
subject_ref
role_ref
agent_run_id

task_id
workflow_instance_id
stage_id

capability
action
resource_type
resource_ref
resource_scope
resource_state_ref

security_context_refs
purpose_ref
requested_duration
requested_effective_from

candidate_grant_refs
required_policy_refs
protected_action_id

created_at
requesting_actor_ref
```

Non-applicable fields are explicit `N/A`.

## 3. Request semantics

A Permission Request asks for evaluation. It grants nothing.

```text
PERMISSION REQUEST != GRANT
PERMISSION REQUEST != PERMISSION DECISION
PERMISSION REQUEST != PROTECTED ACTION EXECUTION
```

## 4. Exactness

A request SHOULD identify the narrowest practical resource and execution scope.

Broad requests such as:

```text
subject X can write production forever
```

violate least-privilege expectations unless explicitly justified by policy.

## 5. Purpose provenance

`purpose_ref` SHOULD resolve to governed Task/Workflow/Plan/Decision scope where relevant. Free text may supplement but must not replace authoritative purpose.

## 6. Re-evaluation

When the intended capability/action/resource/scope changes materially, do not mutate the old request into a new meaning. Create a new Permission Request and retain linkage through external provenance if needed.
===== END VIRTUAL FILE: PERMISSION_REQUEST_STANDARD.md =====

---

## VIRTUAL FILE 10/44 — `PRODUCTION_ACCESS_STANDARD.md`

**Virtual path:** `PRODUCTION_ACCESS_STANDARD.md`  
**Content checksum:** `ae848874ac8e`

===== BEGIN VIRTUAL FILE: PRODUCTION_ACCESS_STANDARD.md =====

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
===== END VIRTUAL FILE: PRODUCTION_ACCESS_STANDARD.md =====

---

## VIRTUAL FILE 11/44 — `PROTECTED_ACTION_STANDARD.md`

**Virtual path:** `PROTECTED_ACTION_STANDARD.md`  
**Content checksum:** `feae63dc4064`

===== BEGIN VIRTUAL FILE: PROTECTED_ACTION_STANDARD.md =====

# Protected Action Standard

**ID:** UPOS-10-PAS-001  
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

A Protected Action is one concrete security-sensitive action instance requiring policy-defined controls beyond ordinary possession of a Capability.

```text
PROTECTED ACTION != WORKFLOW GATE
PROTECTED ACTION != CHANGE CLASS
PROTECTED ACTION != PERMISSION DECISION
```

## 2. Identity

```text
protected_action_id
```

The identity addresses the concrete protected action instance, not a universal action class.

## 3. Minimum contract

```text
protected_action_id
status

action_type
capability
resource_type
resource_ref
resource_scope
resource_state_ref

subject_ref
agent_run_id
task_id
workflow_instance_id
stage_id

change_class_ref
security_policy_ref
security_policy_version

required_capabilities
required_authority_refs
required_approval_refs
required_quality_or_external_gate_refs
required_grant_refs
required_security_context_conditions
security_exception_refs

permission_request_ref
permission_decision_ref

execution_constraints
audit_requirement_refs
execution_result_ref

created_at
authorized_at
executed_at
expires_at
```

## 4. Lifecycle

Minimal action-local lifecycle:

```text
REQUESTED
AUTHORIZED
EXECUTED
FAILED
CANCELLED
EXPIRED
```

`AUTHORIZED` requires a current applicable `ALLOW` Permission Decision.

This lifecycle tracks the protected action only and MUST NOT duplicate Workflow stage/state.

## 5. Typical protected classes

Examples, subject to project policy:

```text
merge/write protected target
history rewrite
production write/deploy/admin
secret rotation/administration
destructive data action
permission administration
security-policy change
break-glass elevation
```

## 6. Change Class boundary

UPOS-004 Change Class and UPOS-010 Protected Action are independent dimensions.

```text
C5 change may contain several protected actions.
Low-change-class work may still request one highly protected action.
```

## 7. Execution

UPOS-010 does not execute the operation. It records the security contract/authorization requirements and references external execution/outcome artifacts.
===== END VIRTUAL FILE: PROTECTED_ACTION_STANDARD.md =====

---

## VIRTUAL FILE 12/44 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `18ee2aa822ae`

===== BEGIN VIRTUAL FILE: README.md =====

# UPOS-010 — Security & Permissions

**ID:** UPOS-10-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 0. Module status

```text
UPOS-010 INTERNAL IMPLEMENTATION:
COMPLETE

UPOS-008 RECONCILIATION:
COMPLETE

UPOS-009 RECONCILIATION:
COMPLETE

UPOS-011 RECONCILIATION:
COMPLETE

UPOS-010 FREEZE:
FROZEN v1.0
```

The Security & Permissions semantic architecture is frozen as part of the coordinated UPOS-008–011 v1 interface-stable baseline. Further semantic change requires a new reviewed version.

## 1. Purpose

UPOS-010 is the canonical U-POS owner for deciding whether a specific security subject may exercise a specific capability/action against a specific resource, within a specific execution/security context, under an applicable versioned security policy and any required approval/protected-action conditions.

It answers:

> Who or what may perform this concrete action on this concrete protected resource now, under which scope, duration, conditions, approvals, exceptions and audit requirements?

It does not decide organizational responsibility, Workflow ordering, Quality correctness, Context assembly, repository mechanics, telemetry projection, learning promotion, or provider-native IAM bindings.

## 2. Fundamental separation

```text
ORGANIZATIONAL AUTHORITY
!=
TECHNICAL PERMISSION
```

```text
UPOS-002
= who is organizationally authorized / responsible

UPOS-010
= whether the requested protected capability/action/resource use
  is currently security-permitted
```

Both may be required.

## 3. Critical invariants

```text
ROLE != PERMISSION
AUTHORITY != CAPABILITY GRANT
CAPABILITY != PERMISSION TO USE IT NOW
TOOL ACCESS != ACTION AUTHORIZATION
QUALITY PASS != SECURITY APPROVAL
WORKFLOW STAGE != PERMISSION
SECRET ACCESS != SECRET OWNERSHIP
HUMAN APPROVAL != AUTOMATIC PERMISSION
GRANT != ORGANIZATIONAL DELEGATION
SECURITY REVIEW != PERMISSION DECISION
PROTECTED ACTION != WORKFLOW GATE
SECURITY AUDIT REQUIREMENT != OBSERVABILITY EVENT
```

Only a current applicable `ALLOW` Permission Decision authorizes execution of the exact request. `CONDITIONAL`, `BLOCKED`, `UNKNOWN`, and `DENY` are non-executable outcomes.

## 4. Core chain

```text
Actor / Execution Identity
↓
Permission Request
↓
Requested Capability + Action
↓
Resource + Scope
↓
Security Context / Execution Scope
↓
Applicable Security Policy
↓
Grant / authority / SoD / approval / exception inputs
↓
Permission Decision
↓
Protected Action conditions if applicable
↓
ALLOW only
↓
External execution
↓
Security audit reference requirements
```

## 5. Stable Module-10 identities

UPOS-010 owns:

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
```

UPOS-010 deliberately does **not** introduce:

```text
security_approval_id
security_veto_id
security_review_result_id
security_policy_id
secret_id as a competing provider/project identity
resource_id as a competing project/provider identity
subject_id as a competing identity-provider identity
```

Human/security approvals use externally governed decision/authority references. Security veto is represented by a `DENY` Permission Decision with attributable veto/authority basis where policy gives Security that veto. Security Policy uses `security_policy_ref + security_policy_version`.

## 6. Permission result vocabulary

```text
ALLOW
DENY
CONDITIONAL
BLOCKED
UNKNOWN
```

Only `ALLOW` authorizes the action.

- `ALLOW` — all security conditions are satisfied now for the exact request and validity window.
- `DENY` — an applicable rule definitively forbids the requested action.
- `CONDITIONAL` — the action could become allowable if explicit listed conditions become satisfied; execution is not yet authorized.
- `BLOCKED` — evaluation cannot validly complete because a required authoritative prerequisite is missing/conflicted/unavailable.
- `UNKNOWN` — no authoritative applicable security rule/context can be resolved; for protected capability use, default-deny behavior applies and execution is not authorized.

## 7. Default-deny rule

For a protected capability/action:

```text
not explicitly and currently permitted
→ not executable
```

This does not collapse `DENY`, `BLOCKED`, and `UNKNOWN` into one semantic state. They remain distinguishable for remediation and audit.

## 8. Ownership boundary

```text
canonical truth / policy source ownership       → UPOS-01
Role / authority / delegation / SoD             → UPOS-002
Skill procedure / capability requirement        → UPOS-003
Workflow ordering / wait / block / reroute      → UPOS-004
Context assembly / representation               → UPOS-005
repository / merge / engineering mechanics      → UPOS-006
Quality evidence / Verdict / readiness          → UPOS-007
events / traces / metrics / audit projection    → UPOS-008
learning candidates / promotion                 → UPOS-009 + UPOS-01
Security & Permission semantics                 → UPOS-010
provider IAM / secret stores / environment IDs  → UPOS-011
```

## 9. Read order

1. `SECURITY_PERMISSIONS_OPERATING_MODEL.md`
2. `SECURITY_ONTOLOGY.md`
3. `SUBJECT_AND_IDENTITY_INTERFACE.md`
4. `CAPABILITY_MODEL.md`
5. `RESOURCE_AND_ACTION_MODEL.md`
6. `SECURITY_POLICY_STANDARD.md`
7. `PERMISSION_REQUEST_STANDARD.md`
8. `PERMISSION_DECISION_STANDARD.md`
9. `GRANT_STANDARD.md`
10. `LEAST_PRIVILEGE_STANDARD.md`
11. `PROTECTED_ACTION_STANDARD.md`
12. `HUMAN_APPROVAL_AND_VETO.md`
13. `SECRET_AND_SENSITIVE_DATA_STANDARD.md`
14. `PRODUCTION_ACCESS_STANDARD.md`
15. `SECURITY_EXCEPTION_STANDARD.md`
16. `SECURITY_FAILURE_MODEL.md`
17. `SECURITY_AUDIT_REQUIREMENTS.md`
18. `SECURITY_LIFECYCLE_AND_VERSIONING.md`
19. `CROSS_MODULE_INTERFACES.md`
20. `MODULE_10_TRACEABILITY.md`
===== END VIRTUAL FILE: README.md =====

---

## VIRTUAL FILE 13/44 — `RESOURCE_AND_ACTION_MODEL.md`

**Virtual path:** `RESOURCE_AND_ACTION_MODEL.md`  
**Content checksum:** `c746e90dbc68`

===== BEGIN VIRTUAL FILE: RESOURCE_AND_ACTION_MODEL.md =====

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
===== END VIRTUAL FILE: RESOURCE_AND_ACTION_MODEL.md =====

---

## VIRTUAL FILE 14/44 — `SECRET_AND_SENSITIVE_DATA_STANDARD.md`

**Virtual path:** `SECRET_AND_SENSITIVE_DATA_STANDARD.md`  
**Content checksum:** `9dfb9e4993ee`

===== BEGIN VIRTUAL FILE: SECRET_AND_SENSITIVE_DATA_STANDARD.md =====

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
===== END VIRTUAL FILE: SECRET_AND_SENSITIVE_DATA_STANDARD.md =====

---

## VIRTUAL FILE 15/44 — `SECURITY_AUDIT_REQUIREMENTS.md`

**Virtual path:** `SECURITY_AUDIT_REQUIREMENTS.md`  
**Content checksum:** `0239876ddbce`

===== BEGIN VIRTUAL FILE: SECURITY_AUDIT_REQUIREMENTS.md =====

# Security Audit Requirements

**ID:** UPOS-10-AUD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Ownership boundary

UPOS-010 defines **which security facts/actions must be auditable and which metadata must be available**.

UPOS-008 owns event schemas, traces, storage, metrics, dashboards and audit projection mechanics after reconciliation.

## 2. Audit-relevant semantic records

At minimum:

```text
Permission Request
Permission Decision
Grant creation/activation/suspension/expiry/revocation/supersession
Protected Action authorization/execution outcome
Security Exception lifecycle/use
Security veto / DENY basis
Break-glass use
secret/sensitive-data access decision metadata
production privileged access
privilege elevation
```

## 3. Minimum attributable audit metadata

Where applicable:

```text
subject_ref
role_ref
agent_run_id
task_id
workflow_instance_id
stage_id

permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id

capability
action
resource_type
resource_ref
resource_scope

security_policy_ref
security_policy_version
approval/authority refs
exception refs

decision / lifecycle result
reason code
execution/outcome ref
occurred/evaluated timestamp
```

## 4. Secret minimization

Audit payload MUST NOT contain raw secret values.

Use:

```text
secret_ref
classification
operation type
decision/outcome
```

## 5. Sensitive-data minimization

Audit should be sufficient for attribution/reconstruction without copying protected payload content unnecessarily.

## 6. Reproducibility support

Audit/provenance should make it possible to answer:

```text
who/what requested this?
what exact protected capability/action/resource?
which policy version applied?
which approvals/grants/exceptions mattered?
why was it allowed/denied/blocked/conditional/unknown?
what was the execution result reference?
```

## 7. Reconciled UPOS-008 interface

The semantic field requirements above are normative UPOS-010 requirements.

For security-constrained telemetry/audit records, UPOS-010 may supply:

```text
security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

UPOS-008 owns concrete Event/audit schema, storage, projection and retention mechanics while honoring those constraints. UPOS-011 binds concrete enforcement/provider mechanisms.

```text
UPOS-010 security constraint semantics
!=
UPOS-008 retention/storage mechanics
```
===== END VIRTUAL FILE: SECURITY_AUDIT_REQUIREMENTS.md =====

---

## VIRTUAL FILE 16/44 — `SECURITY_EXCEPTION_STANDARD.md`

**Virtual path:** `SECURITY_EXCEPTION_STANDARD.md`  
**Content checksum:** `73c68461fdbb`

===== BEGIN VIRTUAL FILE: SECURITY_EXCEPTION_STANDARD.md =====

# Security Exception Standard

**ID:** UPOS-10-SES-001  
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

A Security Exception is a bounded externally authorized departure from an applicable Security Policy rule.

```text
SECURITY EXCEPTION != POLICY DELETION
SECURITY EXCEPTION != POLICY CHANGE
SECURITY EXCEPTION != HUMAN APPROVAL ALONE
```

## 2. Identity

```text
security_exception_id
```

## 3. Minimum contract

```text
security_exception_id
status
status_history

affected_security_policy_ref
affected_security_policy_version
affected_rule_ref

subject_ref
capability
action
resource_type
resource_ref
resource_scope
resource_state_ref
execution_scope_refs

reason
scope
compensating_controls

authorizing_authority_ref
decision_ref

created_at
approved_at
effective_from
expires_at
review_trigger
revoked_at

supersedes
replacement

audit_requirement_refs
```

## 4. Lifecycle

```text
DRAFT
APPROVED
ACTIVE
EXPIRED
REVOKED
SUPERSEDED
INVALID
```

Only `ACTIVE` may be used to relax an exception-eligible policy rule.

Approval authority is external; UPOS-010 validates/reference semantics only.

## 5. Exact scope

Exception applicability is exact and bounded by:

```text
policy/rule version
subject
capability/action
resource/scope/state
execution scope
time
compensating controls
```

An Exception MUST NOT silently float to broader resources, new policy versions or later unrelated actions.

## 6. Historical semantics

An Exception authorized after a historical Permission Decision cannot retroactively turn `DENY` into `ALLOW`.

A new Permission Request/Decision is required for current use.

## 7. Immutability

After `APPROVED`, substantive exception scope/reason/authority/compensating controls are immutable for that ID.

Material change requires a new/superseding `security_exception_id`.

Status transitions remain append-only history.

## 8. Invalid exception

Examples:

```text
expired
revoked
wrong subject/resource/scope
wrong policy version
missing external authority
compensating control not satisfied
policy marks rule non-exceptionable
```

Such an Exception contributes no permission.
===== END VIRTUAL FILE: SECURITY_EXCEPTION_STANDARD.md =====

---

## VIRTUAL FILE 17/44 — `SECURITY_FAILURE_MODEL.md`

**Virtual path:** `SECURITY_FAILURE_MODEL.md`  
**Content checksum:** `729d5a4bf7e1`

===== BEGIN VIRTUAL FILE: SECURITY_FAILURE_MODEL.md =====

# Security Failure Model

**ID:** UPOS-10-SFM-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Purpose

Security failures classify why permission evaluation/action protection cannot proceed. UPOS-010 owns the security meaning; UPOS-004 owns orchestration response.

## 2. Canonical failure taxonomy

| Code | Meaning | Security result tendency |
|---|---|---|
| `PERMISSION_DENIED` | applicable policy definitively forbids action | DENY |
| `MISSING_REQUIRED_GRANT` | required grant absent/inactive | CONDITIONAL or DENY per policy |
| `GRANT_EXPIRED` | needed grant expired | CONDITIONAL / DENY |
| `GRANT_REVOKED` | needed grant revoked | DENY |
| `POLICY_CONFLICT` | active applicable rules conflict without canonical resolution | BLOCKED |
| `POLICY_NOT_FOUND` | required policy/owner cannot be resolved | UNKNOWN/BLOCKED |
| `PROTECTED_ACTION_BLOCKED` | required protected-action condition not satisfied | CONDITIONAL/BLOCKED |
| `HUMAN_APPROVAL_REQUIRED` | policy requires external Human decision | CONDITIONAL |
| `HUMAN_APPROVAL_MISSING` | required approval absent/not current | CONDITIONAL |
| `SOD_VIOLATION` | external SoD rule would be violated | DENY |
| `AUTHORITY_REQUIRED` | required organizational authority ref absent | CONDITIONAL/BLOCKED |
| `SECRET_ACCESS_DENIED` | secret use/read prohibited | DENY |
| `SENSITIVE_CONTEXT_DENIED` | requested sensitive Context exposure prohibited | DENY or redacted alternative if policy defines |
| `PRODUCTION_ACCESS_DENIED` | protected production action forbidden | DENY |
| `INVALID_EXCEPTION` | exception cannot apply | no relaxation; evaluate base policy |
| `UNKNOWN_SECURITY_CONTEXT` | material security input unknown | UNKNOWN/BLOCKED |
| `RESOURCE_SCOPE_MISMATCH` | subject/grant/decision does not cover exact target | DENY |
| `PERMISSION_STALE` | prior decision no longer reusable | BLOCKED until re-evaluated |
| `BREAK_GLASS_CONDITION_MISSING` | emergency path incomplete | CONDITIONAL/BLOCKED |
| `PROVIDER_ENFORCEMENT_UNAVAILABLE` | required provider/IAM state cannot be verified/applied | BLOCKED |
| `AUDIT_REQUIREMENT_UNSATISFIABLE` | action requires audit controls unavailable | BLOCKED/DENY per policy |

## 3. Deterministic interpretation

```text
definitive applicable prohibition
→ DENY

potentially satisfiable missing condition
→ CONDITIONAL

required authoritative prerequisite unavailable/conflicted
→ BLOCKED

no authoritative coverage resolvable
→ UNKNOWN
```

Only `ALLOW` permits execution.

## 4. Workflow response boundary

UPOS-010 returns Security result/failure reason.

UPOS-004 decides whether to:

```text
wait
block
escalate
reroute
reclassify
cancel
```

UPOS-010 MUST NOT encode those Workflow transitions.
===== END VIRTUAL FILE: SECURITY_FAILURE_MODEL.md =====

---

## VIRTUAL FILE 18/44 — `SECURITY_LIFECYCLE_AND_VERSIONING.md`

**Virtual path:** `SECURITY_LIFECYCLE_AND_VERSIONING.md`  
**Content checksum:** `7944e87de8af`

===== BEGIN VIRTUAL FILE: SECURITY_LIFECYCLE_AND_VERSIONING.md =====

# Security Lifecycle & Versioning

**ID:** UPOS-10-SLV-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity preservation

Historical security records are append-only/provenance-preserving.

Materially new semantic object/state creates a new identity where specified rather than rewriting history.

## 2. Permission Request

A materially different request creates a new `permission_request_id`.

## 3. Permission Decision

Each completed evaluation snapshot has a new `permission_decision_id`.

Historical Decision result remains interpreted as-of its evaluation time and basis state.

## 4. Grant

Lifecycle:

```text
PENDING → ACTIVE ↔ SUSPENDED
ACTIVE/SUSPENDED → EXPIRED / REVOKED / SUPERSEDED
```

Project policy may restrict transitions further. Terminal records remain historical.

## 5. Security Exception

Lifecycle:

```text
DRAFT → APPROVED → ACTIVE
ACTIVE → EXPIRED / REVOKED / SUPERSEDED / INVALID
```

Substantive authorized scope is immutable after approval.

## 6. Protected Action

Minimal action-local lifecycle:

```text
REQUESTED → AUTHORIZED → EXECUTED
                      ↘ FAILED
REQUESTED/AUTHORIZED → CANCELLED / EXPIRED
```

It is not a Workflow state machine.

## 7. Policy versioning

Permission decisions always record:

```text
security_policy_ref
security_policy_version
```

Policy change can invalidate reuse of earlier `ALLOW`/Grant unless compatibility/current-policy rules explicitly preserve it.

## 8. Expiry vs revocation

```text
EXPIRY
= validity ended because a declared time/end condition was reached

REVOCATION
= authorized action terminated validity before ordinary expiry
```

They are not interchangeable.

## 9. Historical non-retroactivity

Later:

```text
Grant revocation
Exception approval/revocation
Human approval
policy version change
subject/Role change
```

does not rewrite historical Permission Decisions. It affects current/future authorization and may require re-evaluation.
===== END VIRTUAL FILE: SECURITY_LIFECYCLE_AND_VERSIONING.md =====

---

## VIRTUAL FILE 19/44 — `SECURITY_ONTOLOGY.md`

**Virtual path:** `SECURITY_ONTOLOGY.md`  
**Content checksum:** `90d0357e6a75`

===== BEGIN VIRTUAL FILE: SECURITY_ONTOLOGY.md =====

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
===== END VIRTUAL FILE: SECURITY_ONTOLOGY.md =====

---

## VIRTUAL FILE 20/44 — `SECURITY_PERMISSIONS_OPERATING_MODEL.md`

**Virtual path:** `SECURITY_PERMISSIONS_OPERATING_MODEL.md`  
**Content checksum:** `7e87ccbb2a74`

===== BEGIN VIRTUAL FILE: SECURITY_PERMISSIONS_OPERATING_MODEL.md =====

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
===== END VIRTUAL FILE: SECURITY_PERMISSIONS_OPERATING_MODEL.md =====

---

## VIRTUAL FILE 21/44 — `SECURITY_POLICY_STANDARD.md`

**Virtual path:** `SECURITY_POLICY_STANDARD.md`  
**Content checksum:** `33f53515f8e1`

===== BEGIN VIRTUAL FILE: SECURITY_POLICY_STANDARD.md =====

# Security Policy Standard

**ID:** UPOS-10-SPS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Policy reference model

UPOS-010 evaluates versioned Security Policy through:

```text
security_policy_ref
security_policy_version
```

`security_policy_ref` resolves to the governed canonical project/security source under UPOS-01 ownership rules.

UPOS-010 does not introduce a second global `security_policy_id` or independent policy database.

## 2. Policy content interface

A Security Policy may define:

```text
applicability
subject classes/attributes
resource classes/scopes
capability/action rules
default behavior
conditions
required authority refs
required approvals
SoD constraints
protected-action classifications
secret/sensitive-data controls
production/elevated access controls
exception eligibility
expiry/revalidation behavior
audit requirements
telemetry/audit sensitivity classifications where applicable
telemetry/audit redaction directives where applicable
telemetry/audit access constraints where applicable
telemetry/audit retention constraints where applicable
```


## 2.1 Observability security-handling interface

Where Security/Privacy policy constrains telemetry or audit material, UPOS-010 may expose policy-scoped handling references/directives without creating new global policy identities:

```text
security_policy_ref
security_policy_version
sensitivity_class_ref
redaction_directive_ref
access_constraint_ref
retention_constraint_ref
```

These values express security constraints only. UPOS-008 owns Event/Trace/storage/projection/retention mechanics under those constraints; UPOS-011 binds concrete storage/access/redaction/retention enforcement.

## 3. Canonicality

If applicable active normative Security sources conflict:

```text
DO NOT GUESS
→ BLOCKED / POLICY_CONFLICT
→ resolve canonical owner through UPOS-01 governance
```

## 4. Policy precedence

A more specific rule may refine a broader rule only where upstream security policy permits refinement and no stronger security rule is weakened.

UPOS-010 does not invent a universal numeric policy precedence system beyond canonical source resolution + explicit policy specificity/deny rules.

## 5. Deny-over-allow

Where the canonical policy defines explicit deny precedence for overlapping rules, that rule is honored.

Absent such a declared combination rule, conflicting applicable rules are `POLICY_CONFLICT`, not guessed.

## 6. Versioning

Every Permission Decision MUST record the exact `security_policy_ref` and `security_policy_version` used.

Material changes to authorization semantics require policy version change under the owning documentation/security governance.

## 7. Decision reproducibility

A decision should be explainable from:

```text
subject refs
execution scope
capability/action
resource/scope
policy ref/version
grant state
approval/authority refs
exception refs
security context refs
time
```

External provider state may prevent byte-identical replay, but the rule path and reason must remain attributable.
===== END VIRTUAL FILE: SECURITY_POLICY_STANDARD.md =====

---

## VIRTUAL FILE 22/44 — `SUBJECT_AND_IDENTITY_INTERFACE.md`

**Virtual path:** `SUBJECT_AND_IDENTITY_INTERFACE.md`  
**Content checksum:** `8add4aee4a6a`

===== BEGIN VIRTUAL FILE: SUBJECT_AND_IDENTITY_INTERFACE.md =====

# Subject & Identity Interface

**ID:** UPOS-10-SII-001  
**Type:** INTERFACE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity reuse

UPOS-010 consumes already-owned identities and references.

Agent execution:

```text
role_ref             → UPOS-002 role_id
agent_definition_ref → UPOS-002 agent_definition_id + version
agent_run_id          → UPOS-002 Agent Run identity
```

Workflow execution:

```text
task_id
workflow_instance_id
stage_id
```

Resource/provider/service identities are supplied by project/provider adapters and canonical resource owners.

## 2. Subject representation

A Permission Request MUST identify the subject using:

```text
subject_type
subject_ref
```

and where applicable the narrow execution identity:

```text
role_ref
agent_run_id
task_id
workflow_instance_id
stage_id
```

A Role alone is insufficient for execution-scoped authorization when a narrower Run/Task/Stage identity exists.

## 3. Subject types

Canonical abstract classes:

```text
HUMAN
AGENT_RUN
AGENT_INSTANCE
SERVICE
AUTOMATION
```

`ROLE` may appear as an organizational attribute/reference but is not treated as a standalone executing identity unless project policy explicitly uses a Role-bound service identity.

## 4. Identity proof / authentication boundary

UPOS-010 may require a security condition such as:

```text
subject authenticated
stronger authentication required
recent reauthentication required
identity assurance >= policy threshold
```

It does not define identity-provider mechanics, tokens, MFA implementation or credential issuance. UPOS-011 binds those conditions.

## 5. Execution scope

Permissions SHOULD be bound to the narrowest available governed scope:

```text
Agent Run
Task
Workflow Instance
Stage
Engineering Change / RCU
exact protected action
```

Standing actor-wide permission is exceptional, not default.

## 6. Cross-project isolation

A subject/grant/resource reference in Project A MUST NOT implicitly authorize equivalent-looking resources in Project B.

Project identity/scope must be explicit in binding or policy context where cross-project ambiguity is possible.
===== END VIRTUAL FILE: SUBJECT_AND_IDENTITY_INTERFACE.md =====

---

## VIRTUAL FILE 23/44 — `VIRTUAL_REPOSITORY_TREE.md`

**Virtual path:** `VIRTUAL_REPOSITORY_TREE.md`  
**Content checksum:** `0a21d45b5c8f`

===== BEGIN VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

# UPOS-010 Virtual Repository Tree

**ID:** UPOS-10-TREE-001  
**Type:** REFERENCE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```text
10_security_permissions/
├── CAPABILITY_MODEL.md
├── CROSS_MODULE_INTERFACES.md
├── GRANT_STANDARD.md
├── HUMAN_APPROVAL_AND_VETO.md
├── LEAST_PRIVILEGE_STANDARD.md
├── MODULE_10_DEFINITION_OF_DONE.md
├── MODULE_10_TRACEABILITY.md
├── PERMISSION_DECISION_STANDARD.md
├── PERMISSION_REQUEST_STANDARD.md
├── PRODUCTION_ACCESS_STANDARD.md
├── PROTECTED_ACTION_STANDARD.md
├── README.md
├── RESOURCE_AND_ACTION_MODEL.md
├── SECRET_AND_SENSITIVE_DATA_STANDARD.md
├── SECURITY_AUDIT_REQUIREMENTS.md
├── SECURITY_EXCEPTION_STANDARD.md
├── SECURITY_FAILURE_MODEL.md
├── SECURITY_LIFECYCLE_AND_VERSIONING.md
├── SECURITY_ONTOLOGY.md
├── SECURITY_PERMISSIONS_OPERATING_MODEL.md
├── SECURITY_POLICY_STANDARD.md
├── SUBJECT_AND_IDENTITY_INTERFACE.md
├── VIRTUAL_REPOSITORY_TREE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md
├── analysis/CAPABILITY_MODEL_ANALYSIS.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MODULE_10_OWNERSHIP_MAP.md
├── analysis/PRODUCTION_ACCESS_ANALYSIS.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/PROTECTED_ACTION_ANALYSIS.md
├── analysis/SECRET_HANDLING_ANALYSIS.md
├── analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md
├── analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md
├── analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md
├── templates/GRANT_TEMPLATE.md
├── templates/PERMISSION_DECISION_TEMPLATE.md
├── templates/PERMISSION_REQUEST_TEMPLATE.md
├── templates/PROTECTED_ACTION_TEMPLATE.md
├── templates/SECURITY_EXCEPTION_TEMPLATE.md
```
===== END VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

---

## VIRTUAL FILE 24/44 — `analysis/AMBIGUITY_GAP_REGISTER.md`

**Virtual path:** `analysis/AMBIGUITY_GAP_REGISTER.md`  
**Content checksum:** `210efb6ff3fe`

===== BEGIN VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

# Ambiguity & Gap Register

**ID:** UPOS-10-AN-AGR-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


| Topic | Resolution | Status |
|---|---|---|
| Authority vs Permission | UPOS-002 authority; UPOS-010 current technical permission | RESOLVED |
| Role vs Security Subject | Role is organizational attribute; executing subject is referenced identity, usually Agent Run/Human/Service | RESOLVED |
| Capability vs Tool | Capability is semantic power; Tool is technical mechanism | RESOLVED |
| Capability vs Permission | Capability availability does not authorize current use | RESOLVED |
| Permission Request vs Grant | Request asks for decision; Grant is bounded reusable allowance | RESOLVED |
| Permission Decision vs Grant | Decision is exact current evaluation; Grant is one decision input | RESOLVED |
| Grant vs delegation | Grant technical; delegation organizational UPOS-002 | RESOLVED |
| Grant vs authority | Grant cannot create authority | RESOLVED |
| Protected Action vs Workflow Gate | action security instance vs orchestration condition | RESOLVED |
| Human Approval vs Permission | approval is condition ref; current ALLOW still required | RESOLVED |
| Security Review vs Permission Decision | review assesses risk; decision authorizes/denies action | RESOLVED |
| Security Veto vs Quality Fail | independent owners/states | RESOLVED |
| Secret access vs Context inclusion | security access directive vs UPOS-005 representation | RESOLVED |
| Secret use vs disclosure | separate capabilities/effects | RESOLVED |
| Production access vs deployment Workflow | permission vs orchestration | RESOLVED |
| Break-glass vs exception | emergency route; exception only if policy departure | RESOLVED |
| Exception vs policy change | exception bounded; policy remains active | RESOLVED |
| Grant expiry vs revocation | natural end vs early authorized termination | RESOLVED |
| Technical permission vs provider IAM scope | universal semantics vs UPOS-011 mapping | RESOLVED/PENDING BINDING |
| Security Audit vs Observability Event | audit requirement semantics vs UPOS-008 projection | RESOLVED/PENDING INTERFACE |
| Learning signal contract | security outcome refs vs UPOS-009 semantics | PENDING RECONCILIATION |

```text
Unresolved internal P0/P1 Module-10 gaps = 0
External freeze blockers = UPOS-008 / UPOS-009 / UPOS-011 reconciliation only
```
===== END VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

---

## VIRTUAL FILE 25/44 — `analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md`

**Virtual path:** `analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md`  
**Content checksum:** `1d064a4f5f03`

===== BEGIN VIRTUAL FILE: analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md =====

# Authority vs Permission Boundary Analysis

**ID:** UPOS-10-AN-APB-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Core decision

```text
ORGANIZATIONAL AUTHORITY != TECHNICAL PERMISSION
```

UPOS-002 answers whether a Role/Human/Agent is authorized organizationally to decide/act in scope.

UPOS-010 answers whether the concrete protected use is security-permitted now.

A technical provider credential or Grant cannot create organizational authority.

A Role's organizational authority cannot bypass a technical Security DENY.

## Merge example

```text
Merge Controller authority                     → UPOS-002
mechanically mergeable repository state        → UPOS-006
Quality readiness                              → UPOS-007
permission to execute protected merge now      → UPOS-010
provider branch-protection/IAM mapping          → UPOS-011
```

## Human approval

Human approval is an external organizational decision ref. UPOS-010 may require it as a condition but does not own who may approve.
===== END VIRTUAL FILE: analysis/AUTHORITY_PERMISSION_BOUNDARY_ANALYSIS.md =====

---

## VIRTUAL FILE 26/44 — `analysis/CAPABILITY_MODEL_ANALYSIS.md`

**Virtual path:** `analysis/CAPABILITY_MODEL_ANALYSIS.md`  
**Content checksum:** `251a6f9e0d40`

===== BEGIN VIRTUAL FILE: analysis/CAPABILITY_MODEL_ANALYSIS.md =====

# Capability Model Analysis

**ID:** UPOS-10-AN-CAP-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Decision

Use provider-neutral capability taxonomy plus exact action/resource scope.

Do not model provider scopes as canonical capabilities.

## Why capability and action are separate

Capability gives reusable policy grouping; Action gives request precision.

Example:

```text
capability = production-write
action = update feature flag value
resource = exact production service/config scope
```

## Taxonomy principle

Use stable semantic names only where they carry cross-project meaning. Project-specific capabilities may extend the taxonomy through governed policy/adapter binding without changing universal core.

## Inheritance

No implicit capability implication. Any implication/aggregation must be policy-defined.
===== END VIRTUAL FILE: analysis/CAPABILITY_MODEL_ANALYSIS.md =====

---

## VIRTUAL FILE 27/44 — `analysis/IMPLEMENTATION_PLAN.md`

**Virtual path:** `analysis/IMPLEMENTATION_PLAN.md`  
**Content checksum:** `135e9a707fd2`

===== BEGIN VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

# Implementation Plan

**ID:** UPOS-10-AN-PLAN-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Logical implementation sequence

```text
1. ownership boundary + ontology
2. subject/capability/resource model
3. permission request/decision semantics
4. grant + least privilege
5. protected actions + Human Approval/veto
6. secret/sensitive data
7. production/elevation/break-glass
8. exceptions + policy
9. failures + lifecycle
10. audit requirements
11. templates + interfaces
12. traceability + validation
```

## Suggested commit decomposition

```text
docs(upos-010): establish security ownership boundary
docs(upos-010): define subjects capabilities resources and actions
docs(upos-010): define permission request and decision semantics
docs(upos-010): define grants and least privilege
docs(upos-010): define protected actions approvals and veto
docs(upos-010): define secrets and sensitive-data handling
docs(upos-010): define production and elevated access
docs(upos-010): define security exceptions and policy
docs(upos-010): define failure lifecycle and audit semantics
docs(upos-010): add templates and cross-module interfaces
docs(upos-010): complete provisional traceability audit
```

## Freeze strategy

Do not redesign the core after 008/009/011 stabilize. Perform a narrow interface reconciliation only unless a true ownership conflict is discovered.
===== END VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

---

## VIRTUAL FILE 28/44 — `analysis/MODULE_10_OWNERSHIP_MAP.md`

**Virtual path:** `analysis/MODULE_10_OWNERSHIP_MAP.md`  
**Content checksum:** `7963de9bf63d`

===== BEGIN VIRTUAL FILE: analysis/MODULE_10_OWNERSHIP_MAP.md =====

# Module 10 Ownership Map

**ID:** UPOS-10-AN-OWN-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


| Semantic area | Owner | UPOS-010 treatment |
|---|---|---|
| organizational Role / authority | UPOS-002 | consume refs only |
| delegation / SoD / Human Governance | UPOS-002 | consume/enforce refs only |
| Skill procedure | UPOS-003 | consume capability requirements |
| Workflow order/transition | UPOS-004 | emit Security result only |
| Context retrieval/assembly | UPOS-005 | emit access/redaction directive only |
| repository action mechanics | UPOS-006 | evaluate permission only |
| Quality evidence/verdict/readiness | UPOS-007 | consume external refs if policy requires |
| telemetry/events/metrics | UPOS-008 | declare audit semantics; reconciliation pending |
| learning/promotion | UPOS-009 + UPOS-01 | provide outcome refs; reconciliation pending |
| permission semantics | UPOS-010 | canonical |
| capability/resource/action security model | UPOS-010 | canonical |
| grant lifecycle | UPOS-010 | canonical |
| protected action security semantics | UPOS-010 | canonical |
| secret/sensitive access semantics | UPOS-010 | canonical |
| production permission/elevation | UPOS-010 | canonical |
| security exception semantics | UPOS-010 | canonical |
| provider IAM / physical resource binding | UPOS-011 | pending adapter reconciliation |
===== END VIRTUAL FILE: analysis/MODULE_10_OWNERSHIP_MAP.md =====

---

## VIRTUAL FILE 29/44 — `analysis/PRODUCTION_ACCESS_ANALYSIS.md`

**Virtual path:** `analysis/PRODUCTION_ACCESS_ANALYSIS.md`  
**Content checksum:** `156ce3289022`

===== BEGIN VIRTUAL FILE: analysis/PRODUCTION_ACCESS_ANALYSIS.md =====

# Production Access Analysis

**ID:** UPOS-10-AN-PROD-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Decision

Production access is decomposed into independent capabilities:

```text
production-read
production-write
production-admin
deploy
```

Elevated mutation uses time-bounded/access-minimized controls by default.

## Break-glass decision

Break-glass is a protected emergency access mode, not automatically a Security Exception.

```text
policy-defined emergency route
→ no exception required if all policy conditions satisfied

policy departure
→ valid Security Exception additionally required
```

This avoids conflating emergency operation with policy bypass.
===== END VIRTUAL FILE: analysis/PRODUCTION_ACCESS_ANALYSIS.md =====

---

## VIRTUAL FILE 30/44 — `analysis/PROPOSED_PACKAGE_TREE.md`

**Virtual path:** `analysis/PROPOSED_PACKAGE_TREE.md`  
**Content checksum:** `75efb97fb947`

===== BEGIN VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

# Proposed Package Tree

**ID:** UPOS-10-AN-TREE-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


The implemented package follows the directive's ownership decomposition without additional modules or provider-specific subpackages.

```text
10_security_permissions/
├── README.md
├── SECURITY_PERMISSIONS_OPERATING_MODEL.md
├── SECURITY_ONTOLOGY.md
├── SUBJECT_AND_IDENTITY_INTERFACE.md
├── CAPABILITY_MODEL.md
├── RESOURCE_AND_ACTION_MODEL.md
├── PERMISSION_REQUEST_STANDARD.md
├── PERMISSION_DECISION_STANDARD.md
├── GRANT_STANDARD.md
├── LEAST_PRIVILEGE_STANDARD.md
├── PROTECTED_ACTION_STANDARD.md
├── HUMAN_APPROVAL_AND_VETO.md
├── SECRET_AND_SENSITIVE_DATA_STANDARD.md
├── PRODUCTION_ACCESS_STANDARD.md
├── SECURITY_EXCEPTION_STANDARD.md
├── SECURITY_POLICY_STANDARD.md
├── SECURITY_FAILURE_MODEL.md
├── SECURITY_AUDIT_REQUIREMENTS.md
├── SECURITY_LIFECYCLE_AND_VERSIONING.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_10_DEFINITION_OF_DONE.md
├── MODULE_10_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── templates/ ...
└── analysis/ ...
```
===== END VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

---

## VIRTUAL FILE 31/44 — `analysis/PROTECTED_ACTION_ANALYSIS.md`

**Virtual path:** `analysis/PROTECTED_ACTION_ANALYSIS.md`  
**Content checksum:** `4cbb3475f28a`

===== BEGIN VIRTUAL FILE: analysis/PROTECTED_ACTION_ANALYSIS.md =====

# Protected Action Analysis

**ID:** UPOS-10-AN-PACT-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Decision

`protected_action_id` identifies a concrete action instance requiring elevated controls, not a definition/class.

Protection classification comes from Security Policy.

## Why a local lifecycle exists

Audit needs to distinguish:

```text
requested
authorized
executed/failed/cancelled/expired
```

This does not duplicate Workflow lifecycle because it tracks the security-sensitive action instance only.

## Change Class separation

Protected Action and UPOS-004 Change Class are orthogonal. Risk classification may influence controls, but neither determines the other universally.
===== END VIRTUAL FILE: analysis/PROTECTED_ACTION_ANALYSIS.md =====

---

## VIRTUAL FILE 32/44 — `analysis/SECRET_HANDLING_ANALYSIS.md`

**Virtual path:** `analysis/SECRET_HANDLING_ANALYSIS.md`  
**Content checksum:** `2e94cbd17867`

===== BEGIN VIRTUAL FILE: analysis/SECRET_HANDLING_ANALYSIS.md =====

# Secret Handling Analysis

**ID:** UPOS-10-AN-SEC-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Main decision

Separate secret **use** from secret **disclosure**.

Prefer secure binding/use without raw value exposure where available.

## Universal semantics

UPOS-010 may decide:

```text
may read raw secret?
may use secret via tool/provider binding?
may rotate/manage?
may raw value enter Context?
what redaction/minimization applies?
what audit metadata is required?
```

Concrete secret stores/injection remain UPOS-011/runtime.

## Telemetry safety

Raw secret values are forbidden from audit/observability payloads. Safe refs/metadata only.
===== END VIRTUAL FILE: analysis/SECRET_HANDLING_ANALYSIS.md =====

---

## VIRTUAL FILE 33/44 — `analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md`

**Virtual path:** `analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md`  
**Content checksum:** `5489b8790ef0`

===== BEGIN VIRTUAL FILE: analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md =====

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
===== END VIRTUAL FILE: analysis/SECURITY_ENTITY_MODEL_ANALYSIS.md =====

---

## VIRTUAL FILE 34/44 — `analysis/SOURCE_ANALYSIS.md`

**Virtual path:** `analysis/SOURCE_ANALYSIS.md`  
**Content checksum:** `157ce4751142`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

# UPOS-010 Source Analysis

**ID:** UPOS-10-AN-SA-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## 1. Source hierarchy

```text
UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle
→ upstream governance

UPOS-002…007 FROZEN v1.0
→ upstream module contracts/interfaces

Universal AI Agent Operating Model v1.0
→ frozen design source

UPOS-010 implementation directive §§0–89
→ task-specific implementation requirements

UPOS-008 / 009 / 011 drafts
→ NOT authoritative for Module-10 semantics until reconciliation
```

## 2. Frozen-master Security-relevant extraction

Material source sections include:

```text
3.1 Human governance
3.6 Least privilege
5 Agent Contract — Permissions interface
16 Security Agent
23–30 risk/high-risk/human approval relationships
38 Permissions model
39 Default role permission philosophy
40 Human approval model
68 Security gate
75 Guardrails
77–78 Escalation / Security Owner
93 Security Change workflow signal
98 Release security/ops gate signal
110 Safety around secrets
111 Production access
112 Protected files
114 permissions sufficient readiness signal
123 Authority conflict resolution
124 Security veto
127 Human override
```

Ownership extraction rule:

- Role authority / veto authority / Human Governance → UPOS-002.
- Workflow placement/order → UPOS-004.
- Skill procedure → UPOS-003.
- Engineering mechanics → UPOS-006.
- Quality verdict/gate → UPOS-007.
- Security permission/protected-action/secret/production semantics → UPOS-010.
- Provider bindings → UPOS-011.

## 3. Directive impact

The task directive materially extends the frozen-source Permission section into a normalized Security ontology with stable request/decision/grant/action/exception identities, explicit lifecycle, current-state revalidation, secrets/sensitive Context rules, protected actions and audit requirements.

These are accepted as `TASK_DIRECTIVE_REFINEMENT` of Module-10 ownership, not a redesign of upstream modules.

## 4. P0 conflict check

No P0 ownership conflict found.

The only deliberate freeze blockers are external interface reconciliations with UPOS-008, UPOS-009 and UPOS-011.
===== END VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

---

## VIRTUAL FILE 35/44 — `analysis/SOURCE_SECTION_DISPOSITION.md`

**Virtual path:** `analysis/SOURCE_SECTION_DISPOSITION.md`  
**Content checksum:** `66384fb2d679`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

# Source Section Disposition

**ID:** UPOS-10-AN-DISP-001  
**Type:** ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Frozen master disposition

| Frozen source area | Disposition |
|---|---|
| Human Governance / authority | DEFERRED_TO_UPOS_002, consumed by 010 |
| Least privilege | EXTRACTED_TO_MODULE_10 |
| Security Agent authority | MIXED: authority → 002; security permission semantics → 010 |
| Permissions model | EXTRACTED_TO_MODULE_10 |
| Role permission philosophy | MIXED: Role/authority → 002; capability/permission → 010 |
| Human approval model | MIXED: authority → 002; approval-condition semantics → 010 |
| Security gate | MIXED: placement → 004; security result → 010 |
| Guardrails / permission change / production deploy | MIXED: workflow/mechanics external; permission rule → 010 |
| Escalation | DEFERRED_TO_UPOS_004/002; 010 emits reason/result |
| Secrets safety | EXTRACTED_TO_MODULE_10; provider implementation → 011 |
| Production access | EXTRACTED_TO_MODULE_10; operation workflow/provider implementation external |
| Protected files | EXTRACTED as resource/protected-action semantics; concrete paths → 011 |
| Authority conflict resolution | DEFERRED_TO_UPOS_002/01; 010 consumes authority refs |
| Security veto | MIXED: veto authority → 002; DENY/veto enforcement semantics → 010 |
| Human override | MIXED: override authority → 002; policy exception/override applicability → 010 |
| Observability/metrics | DEFERRED_TO_UPOS_008 |
| Learning/evolution | DEFERRED_TO_UPOS_009 + 01 |
| Project manifest/provider scopes | DEFERRED_TO_UPOS_011 |

## Directive disposition

Sections `0–89` were reviewed. Requirements owned by Module 10 are implemented in normative artifacts. Cross-module mechanics are referenced/deferred to their declared owner. The only intentional provisional items are the explicit 008/009/011 interface reconciliations.
===== END VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

---

## VIRTUAL FILE 36/44 — `analysis/TRACEABILITY_VALIDATION.md`

**Virtual path:** `analysis/TRACEABILITY_VALIDATION.md`  
**Content checksum:** `8c17fbce09d0`

===== BEGIN VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====

# Traceability & Conformance Validation

**ID:** UPOS-10-AN-VAL-001  
**Type:** VALIDATION EVIDENCE  
**Status:** ARCHIVED / FINAL FREEZE VALIDATION  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01–07 frozen baselines; UPOS-008/009/011 pending reconciliation


## Results

```text
Required package files present = PASS
Normative core documents present = 22 / 22
Required templates present = 5 / 5
Required analysis/reconciliation artifacts present = 16 / 16

Permission Request template conforms = PASS
Permission Decision template conforms = PASS
Grant template conforms = PASS
Protected Action template conforms = PASS
Security Exception template conforms = PASS

Stable permission_request_id = PASS
Stable permission_decision_id = PASS
Stable grant_id = PASS
Stable protected_action_id = PASS
Stable security_exception_id = PASS
Duplicate security_approval_id introduced = NO
Duplicate security_veto_id introduced = NO
Duplicate security_policy_id introduced = NO

Decision vocabulary deterministic = PASS
Only ALLOW authorizes execution = PASS
Default-deny behavior for protected capability = PASS
Permission freshness/revalidation = PASS
Grant != current permission = PASS
Authority != permission = PASS
Role != permission = PASS
Protected Action != Workflow Gate = PASS
Security Review != Permission Decision = PASS
Quality PASS != Security approval = PASS

Raw secret logging prohibited = PASS
Sensitive Context directive boundary = PASS
Production/elevation/break-glass semantics = PASS
Security exception non-retroactivity = PASS

Hard-coded project/provider bindings = 0
Unresolved internal P0/P1 gaps = 0

SEC-REQ mappings = 102
UNMAPPED MODULE-10 SOURCE REQUIREMENTS = 0

UPOS-008 reconciliation = COMPLETE
UPOS-009 reconciliation = COMPLETE
UPOS-011 reconciliation = COMPLETE
UPOS-010 freeze = FROZEN v1.0
```

Security handling constraint interface = PASS
Observability retention/security boundary = PASS
Learning signal boundary = PASS
Project Adapter enforcement binding boundary = PASS

## Verdict

PASS for **FROZEN v1.0** coordinated baseline.

Core Module-10 semantics are internally complete and ownership-bounded. All registered external narrow reconciliations are closed.

## Final peer fingerprints

```text
UPOS-008 final SHA-256: e6eed6e9d7e006a5bf3a3d9baa300d8917f6d9ccb3e76c6301a9fcef1b25a0ba
UPOS-009 final SHA-256: 76f8e1c43ae35890a63d527acdc285d25ea6c6494b2aa2af9839928dbb923fbb
```
===== END VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====

---

## VIRTUAL FILE 37/44 — `analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md`

**Virtual path:** `analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md`  
**Content checksum:** `511c7e21ed2b`

===== BEGIN VIRTUAL FILE: analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md =====
# UPOS-008 Interface Reconciliation Register

**ID:** UPOS-10-AN-R008-001  
**Type:** RECONCILIATION REGISTER  
**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Reconciled baseline

```text
UPOS-008 final SHA-256: e6eed6e9d7e006a5bf3a3d9baa300d8917f6d9ccb3e76c6301a9fcef1b25a0ba
```

## Result

```text
UPOS-010 ↔ UPOS-008 = RECONCILED
Material unresolved items = 0
```

Observable UPOS-010 identities/results:

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
security_policy_ref/version
decision / reason code / owner result refs
break-glass/elevation refs
secret/sensitive-data access decision metadata
```

Security handling constraints may be represented by policy-scoped sensitivity/redaction/access/retention refs. UPOS-008 owns telemetry/storage mechanics. Raw secrets/protected payload values are prohibited.

No Event/Trace/Metric/Read Model semantics are owned by UPOS-010.
===== END VIRTUAL FILE: analysis/UPOS_008_INTERFACE_RECONCILIATION_REGISTER.md =====

---

## VIRTUAL FILE 38/44 — `analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md`

**Virtual path:** `analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md`  
**Content checksum:** `0a90e069fb2d`

===== BEGIN VIRTUAL FILE: analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md =====
# UPOS-009 Interface Reconciliation Register

**ID:** UPOS-10-AN-R009-001  
**Type:** RECONCILIATION REGISTER  
**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Reconciled baseline

```text
UPOS-009 final SHA-256: 76f8e1c43ae35890a63d527acdc285d25ea6c6494b2aa2af9839928dbb923fbb
```

## Result

```text
UPOS-010 ↔ UPOS-009 = RECONCILED
Material unresolved items = 0
```

Security evidence usable by Learning includes attributable repeated denials, exceptions, missing approvals, over-broad/long-lived Grants, break-glass use, protected-action failure and sensitive-data access pressure.

UPOS-009 may form Learning Candidates/Proposals but cannot change Security Policy, Grants, Exceptions or Permission Decisions directly. Promotion remains governed through the canonical owner and UPOS-01.
===== END VIRTUAL FILE: analysis/UPOS_009_INTERFACE_RECONCILIATION_REGISTER.md =====

---

## VIRTUAL FILE 39/44 — `analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md`

**Virtual path:** `analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md`  
**Content checksum:** `c4340569099b`

===== BEGIN VIRTUAL FILE: analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md =====
# UPOS-011 Interface Reconciliation Register

**ID:** UPOS-10-AN-R011-001  
**Type:** RECONCILIATION REGISTER  
**Status:** ARCHIVED / RECONCILED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Reconciled:** 2026-09-20

## Result

```text
UPOS-010 ↔ UPOS-011 = RECONCILED
Material unresolved items = 0
```

Resolved binding classes:

```text
subject refs → concrete identity/provider principals
universal capabilities → provider-native scopes/mechanisms
resource refs → physical provider/project resources
security_policy_ref → canonical project policy source binding
Grant enforcement → provider/runtime controls
environment refs → concrete environment IDs
secret refs → secret-store bindings
use-secret → secure injection mechanisms
protected targets → concrete branch/environment/resource protection
approval refs → external approval systems
reauthentication/elevation → provider identity mechanism
break-glass → concrete emergency mechanism
security handling constraints → concrete storage/access/redaction/retention enforcement
```

Provider credential breadth never substitutes for the scoped UPOS-010 Permission Decision.
===== END VIRTUAL FILE: analysis/UPOS_011_INTERFACE_RECONCILIATION_REGISTER.md =====

---

## VIRTUAL FILE 40/44 — `templates/GRANT_TEMPLATE.md`

**Virtual path:** `templates/GRANT_TEMPLATE.md`  
**Content checksum:** `20071b7c9024`

===== BEGIN VIRTUAL FILE: templates/GRANT_TEMPLATE.md =====

# Grant Template

**ID:** UPOS-10-TPL-GRT-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
grant_id:
status:  # PENDING | ACTIVE | SUSPENDED | EXPIRED | REVOKED | SUPERSEDED

subject_ref:
role_ref: N/A
agent_run_scope_ref: N/A
task_scope_ref: N/A
workflow_scope_ref: N/A
stage_scope_ref: N/A

capability:
allowed_actions: []
resource_type:
resource_ref:
resource_scope:

conditions: []
security_policy_ref:
security_policy_version:
originating_permission_decision_ref:
originating_authority_or_delegation_ref: N/A

created_at:
effective_from:
expires_at:
revoked_at: N/A
revocation_reason: N/A
supersedes: none
replacement: none
status_history: []
```
===== END VIRTUAL FILE: templates/GRANT_TEMPLATE.md =====

---

## VIRTUAL FILE 41/44 — `templates/PERMISSION_DECISION_TEMPLATE.md`

**Virtual path:** `templates/PERMISSION_DECISION_TEMPLATE.md`  
**Content checksum:** `37cda0b81646`

===== BEGIN VIRTUAL FILE: templates/PERMISSION_DECISION_TEMPLATE.md =====

# Permission Decision Template

**ID:** UPOS-10-TPL-PDS-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
permission_decision_id:
permission_request_id:

decision:  # ALLOW | DENY | CONDITIONAL | BLOCKED | UNKNOWN
security_policy_ref:
security_policy_version:

subject_ref:
capability:
action:
resource_ref:
resource_scope:
resource_state_ref: N/A

applicable_grant_refs: []
security_exception_refs: []
required_authority_refs: []
required_approval_refs: []
satisfied_condition_refs: []
unsatisfied_conditions: []

protected_action_id: N/A
denial_reason_code: N/A
reason_summary:
veto_basis_ref: N/A

security_context_refs: []
basis_refs: []

effective_from:
expires_at:
revalidation_triggers: []

evaluated_by_ref:
created_at:
```
===== END VIRTUAL FILE: templates/PERMISSION_DECISION_TEMPLATE.md =====

---

## VIRTUAL FILE 42/44 — `templates/PERMISSION_REQUEST_TEMPLATE.md`

**Virtual path:** `templates/PERMISSION_REQUEST_TEMPLATE.md`  
**Content checksum:** `a0bce597772a`

===== BEGIN VIRTUAL FILE: templates/PERMISSION_REQUEST_TEMPLATE.md =====

# Permission Request Template

**ID:** UPOS-10-TPL-PRQ-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
permission_request_id:

subject_type:
subject_ref:
role_ref: N/A
agent_run_id: N/A

task_id: N/A
workflow_instance_id: N/A
stage_id: N/A

capability:
action:
resource_type:
resource_ref:
resource_scope:
resource_state_ref: N/A

security_context_refs: []
purpose_ref:
requested_duration:
requested_effective_from:

candidate_grant_refs: []
required_policy_refs: []
protected_action_id: N/A

created_at:
requesting_actor_ref:
```
===== END VIRTUAL FILE: templates/PERMISSION_REQUEST_TEMPLATE.md =====

---

## VIRTUAL FILE 43/44 — `templates/PROTECTED_ACTION_TEMPLATE.md`

**Virtual path:** `templates/PROTECTED_ACTION_TEMPLATE.md`  
**Content checksum:** `12eae32846f2`

===== BEGIN VIRTUAL FILE: templates/PROTECTED_ACTION_TEMPLATE.md =====

# Protected Action Template

**ID:** UPOS-10-TPL-PACT-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
protected_action_id:
status:  # REQUESTED | AUTHORIZED | EXECUTED | FAILED | CANCELLED | EXPIRED

action_type:
capability:
resource_type:
resource_ref:
resource_scope:
resource_state_ref: N/A

subject_ref:
agent_run_id: N/A
task_id: N/A
workflow_instance_id: N/A
stage_id: N/A

change_class_ref: N/A
security_policy_ref:
security_policy_version:

required_capabilities: []
required_authority_refs: []
required_approval_refs: []
required_quality_or_external_gate_refs: []
required_grant_refs: []
required_security_context_conditions: []
security_exception_refs: []

permission_request_ref:
permission_decision_ref: N/A

execution_constraints: []
audit_requirement_refs: []
execution_result_ref: N/A

created_at:
authorized_at: N/A
executed_at: N/A
expires_at: N/A
```
===== END VIRTUAL FILE: templates/PROTECTED_ACTION_TEMPLATE.md =====

---

## VIRTUAL FILE 44/44 — `templates/SECURITY_EXCEPTION_TEMPLATE.md`

**Virtual path:** `templates/SECURITY_EXCEPTION_TEMPLATE.md`  
**Content checksum:** `260145dbe754`

===== BEGIN VIRTUAL FILE: templates/SECURITY_EXCEPTION_TEMPLATE.md =====

# Security Exception Template

**ID:** UPOS-10-TPL-SEX-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


```yaml
security_exception_id:
status:  # DRAFT | APPROVED | ACTIVE | EXPIRED | REVOKED | SUPERSEDED | INVALID
status_history: []

affected_security_policy_ref:
affected_security_policy_version:
affected_rule_ref:

subject_ref:
capability:
action:
resource_type:
resource_ref:
resource_scope:
resource_state_ref: N/A
execution_scope_refs: []

reason:
scope:
compensating_controls: []

authorizing_authority_ref:
decision_ref:

created_at:
approved_at: N/A
effective_from:
expires_at:
review_trigger: N/A
revoked_at: N/A

supersedes: none
replacement: none

audit_requirement_refs: []
```
===== END VIRTUAL FILE: templates/SECURITY_EXCEPTION_TEMPLATE.md =====
