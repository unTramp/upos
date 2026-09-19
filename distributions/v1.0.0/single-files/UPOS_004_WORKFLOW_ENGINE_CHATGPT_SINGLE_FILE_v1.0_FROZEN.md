# UPOS-004 Workflow Engine — ChatGPT Single-File Edition v1.0

**Module:** UPOS-004 — Workflow Engine  
**System:** Universal Project Operating System  
**Canonical baseline:** FROZEN v1.0  
**Embedded virtual files:** 44  
**Generated:** 2026-09-19

---

# 0. Interpretation rule

This is a transport bundle, not a replacement monolith.

Each virtual-file block represents one repository file under `04_workflow_engine/`.

Normative authority remains with the embedded normative Markdown documents.

`analysis/` is historical EVIDENCE only.

`MODULE_04_TRACEABILITY.md` is the canonical normative coverage artifact.

## Accepted architecture — unchanged

```text
Change Class
+
Work Type
+
Concern Profiles
```

```text
Base Workflow
+
Concern Profiles
+
Change Class
=
Resolved Workflow Configuration
```

## Stable semantic identities

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

## Non-convergence invariant

```text
No infinite retry loops.
No infinite rework loops.
```

## Frozen validation

```text
Profile contracts missing required sections = 0
Workflow contracts missing required sections = 0
Unknown UPOS-003 Skill IDs referenced = 0
Hard-coded provider/project-path leakage = 0
Unresolved P0/P1 Module-04 gaps = 0

UNMAPPED MODULE-04 SOURCE REQUIREMENTS = 0

NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 05–11
```

# 1. Virtual repository tree

```text
04_workflow_engine/
├── README.md
├── WORKFLOW_OPERATING_MODEL.md
├── CHANGE_CLASSIFICATION_STANDARD.md
├── WORK_TYPE_AND_CONCERN_MODEL.md
├── WORKFLOW_PROFILE_STANDARD.md
├── WORKFLOW_CONTRACT_STANDARD.md
├── ROUTING_STANDARD.md
├── TASK_AND_WORKFLOW_INSTANCE_MODEL.md
├── WORKFLOW_STATE_MODEL.md
├── RECLASSIFICATION_AND_REROUTING.md
├── FAILURE_RETRY_RECOVERY.md
├── PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md
├── WORKFLOW_LIFECYCLE_AND_VERSIONING.md
├── WORKFLOW_CATALOG.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_04_DEFINITION_OF_DONE.md
├── MODULE_04_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── workflows/bug-fix.md
├── workflows/dependency-upgrade.md
├── workflows/documentation-change.md
├── workflows/feature.md
├── workflows/generic-change.md
├── workflows/hotfix.md
├── workflows/refactor.md
├── workflows/release.md
├── profiles/api.md
├── profiles/architecture.md
├── profiles/database-migration.md
├── profiles/design-system.md
├── profiles/documentation-impact.md
├── profiles/security.md
├── profiles/ui.md
├── templates/ROUTING_DECISION_TEMPLATE.md
├── templates/WORKFLOW_CONTRACT_TEMPLATE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/CLASSIFICATION_DIMENSION_AUDIT.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MODULE_04_OWNERSHIP_MAP.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── analysis/WORKFLOW_MODEL_DECISION.md
```

# 2. Embedded files


---

## VIRTUAL FILE 1/44 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `6347ffd9ef31`

===== BEGIN VIRTUAL FILE: README.md =====

# UPOS-004 — Workflow Engine

**ID:** UPOS-04-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, UPOS-003, frozen master design source


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-004 defines how U-POS classifies work, selects a Workflow, composes concern-specific orchestration requirements, sequences Roles/Skills/stages, handles transitions/rework/retry/recovery/reclassification, and reaches a terminal orchestration result.

It does this without taking ownership from Agent Organization, Skills, Context & Memory, Engineering Governance, Quality, Security, Observability, Learning, or Project Adapter.

## 1. Fundamental model

```text
TASK / CHANGE REQUEST
= work entering the operating system

CHANGE CLASS
= canonical impact/risk classification

WORK TYPE
= primary nature/intention of the work

CONCERN
= cross-cutting impact affecting orchestration

WORKFLOW DEFINITION
= versioned canonical base orchestration contract

WORKFLOW PROFILE
= reusable concern-specific orchestration overlay

RESOLVED WORKFLOW CONFIGURATION
= Base Workflow + Profiles + Change Class + external policy references

WORKFLOW INSTANCE
= one concrete execution of one resolved Workflow configuration

WORKFLOW STAGE
= bounded orchestration phase

TRANSITION
= allowed movement between stages/states

GATE REFERENCE
= reference to an externally owned condition/result

ROUTING DECISION
= attributable selection of the resolved configuration

WORKFLOW RESULT
= terminal orchestration outcome
```

These concepts MUST NOT be used interchangeably.

## 2. Three-axis routing model

UPOS-004 adopts the following normalized model:

```text
1. CHANGE CLASS
   C0–C5
   = impact / risk depth

2. WORK TYPE
   = primary intention

3. CONCERNS / PROFILES
   = cross-cutting orchestration impacts
```

Resolution:

```text
Base Workflow
+
Concern Profiles
+
Change Class
+
External policy/gate references
=
Resolved Workflow Configuration
```

This model preserves frozen-source workflows while avoiding combinatorial explosion.

## 3. Critical boundaries

```text
Role / authority / SoD / handoff contract → UPOS-002
Skill procedure / registry / evaluation   → UPOS-003
Context retrieval / memory / budgets      → UPOS-005
Git / commit / PR / merge mechanics       → UPOS-006
Quality evidence / verdict / gate meaning → UPOS-007
Telemetry / traces / dashboard            → UPOS-008
Learning detection / promotion            → UPOS-009 + UPOS-01
Permissions / protected actions           → UPOS-010
Project/provider/runtime bindings          → UPOS-011
Canonical project truth                    → UPOS-01
```

Workflow definitions reference those interfaces; they do not redefine them.

## 4. Organizational invariants consumed from UPOS-002

```text
Implementer != Final Reviewer
```

For high-risk work:

```text
Implementer != Reviewer != Merge Controller
```

The Workflow Engine MUST route/compose stages so these constraints can be satisfied.

## 5. Skill boundary consumed from UPOS-003

```text
ROLE / AGENT
= WHO

SKILL
= reusable bounded HOW

WORKFLOW
= WHEN, WHY, UNDER WHAT CONDITIONS,
  and IN WHAT ORDER
```

Workflow definitions reference stable Skill IDs/versions. They MUST NOT copy Skill procedures.

## 6. Read order

1. `WORKFLOW_OPERATING_MODEL.md`
2. `CHANGE_CLASSIFICATION_STANDARD.md`
3. `WORK_TYPE_AND_CONCERN_MODEL.md`
4. `WORKFLOW_PROFILE_STANDARD.md`
5. `WORKFLOW_CONTRACT_STANDARD.md`
6. `ROUTING_STANDARD.md`
7. `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`
8. `WORKFLOW_STATE_MODEL.md`
9. `RECLASSIFICATION_AND_REROUTING.md`
10. `FAILURE_RETRY_RECOVERY.md`
11. `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md`
12. `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`
13. `WORKFLOW_CATALOG.md`
14. `CROSS_MODULE_INTERFACES.md`
15. relevant `workflows/*.md`
16. relevant `profiles/*.md`
17. `MODULE_04_TRACEABILITY.md`

===== END VIRTUAL FILE: README.md =====


---

## VIRTUAL FILE 2/44 — `WORKFLOW_OPERATING_MODEL.md`

**Virtual path:** `WORKFLOW_OPERATING_MODEL.md`  
**Content checksum:** `f5790cb4f222`

===== BEGIN VIRTUAL FILE: WORKFLOW_OPERATING_MODEL.md =====

# Workflow Operating Model

**ID:** UPOS-04-WOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CHANGE_CLASSIFICATION_STANDARD.md, ROUTING_STANDARD.md


## 1. Definition

A Workflow Definition is a versioned canonical orchestration contract describing when, why, under what conditions, and in what order organizational Roles and Skill references participate in a class of work.

A Workflow owns orchestration.

It does not own the detailed procedure of a Skill, organizational authority of a Role, or semantics of external gates.

## 2. Why three axes are required

The frozen source contains dedicated examples for:

```text
UI Change
Design System Change
Architecture Change
API Change
Database Migration
Security Change
```

Those concerns are not mutually exclusive.

One feature may be simultaneously:

```text
Feature
+ UI
+ API
+ Database
+ Security
```

Treating each combination as a separate Workflow Definition creates combinatorial explosion and ambiguous routing.

Therefore UPOS-004 normalizes them as:

```text
Primary Work Type → Base Workflow
Cross-cutting impact → Concern Profiles
Risk/impact depth → Change Class
```

## 3. Base Workflow

A Base Workflow expresses the primary intention.

v1 base Work Types:

```text
GENERIC_CHANGE
BUG_FIX
FEATURE
REFACTOR
DEPENDENCY_UPGRADE
DOCUMENTATION_CHANGE
HOTFIX
RELEASE
```

`MICRO` is not a Work Type. It is Change Class C0 and normally resolves through `GENERIC_CHANGE`.

## 4. Concern Profile

A Concern Profile modifies orchestration without replacing the Base Workflow.

v1 profiles:

```text
UI
DESIGN_SYSTEM
ARCHITECTURE
API
DATABASE_MIGRATION
SECURITY
DOCUMENTATION_IMPACT
```

Profiles may:

- add required Role participation references;
- add Skill references;
- add stages/checkpoints;
- add external gate references;
- add reclassification triggers;
- impose conditional risk floors where normative criteria justify them.

Profiles MUST NOT redefine external owners' semantics.

## 5. Resolved Workflow Configuration

A Routing Decision resolves:

```text
task
→ work type
→ concerns
→ change class
→ base workflow
→ compatible profiles
→ required organizational constraints
→ external gates/approvals by reference
```

The result is attributable and reproducible.

## 6. Risk determines process depth

Frozen-source principle:

```text
Risk / impact
!=
diff size
```

Process depth is adjusted by classification/profile/policy.

## 7. No every-agent swarm

Workflow routing MUST choose only Roles/Skills justified by the resolved configuration.

The existence of a Role or Skill in the U-POS catalog is not a reason to run it for every Task.

## 8. No hidden workflow in Skills

Workflow stages reference Skill IDs.

They do not embed Skill procedures.

## 9. No hidden authority in Workflow

Workflow may require participation or approval references.

It cannot create authority a Role does not possess.

## 10. No hidden canonical truth

Workflow status/results do not automatically become canonical project knowledge.

Project truth remains governed by UPOS-01.

===== END VIRTUAL FILE: WORKFLOW_OPERATING_MODEL.md =====


---

## VIRTUAL FILE 3/44 — `CHANGE_CLASSIFICATION_STANDARD.md`

**Virtual path:** `CHANGE_CLASSIFICATION_STANDARD.md`  
**Content checksum:** `b11a7cc737a8`

===== BEGIN VIRTUAL FILE: CHANGE_CLASSIFICATION_STANDARD.md =====

# Change Classification Standard — C0–C5

**ID:** UPOS-04-CLS-001  
**Type:** CLASSIFICATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** ROUTING_STANDARD.md, analysis/CLASSIFICATION_DIMENSION_AUDIT.md


## 1. Principle

Classification is based on impact/risk, not line count or diff size.

```text
RISK / IMPACT != DIFF SIZE
```

A one-line authorization change may be C5.

A large generated-documentation change may be low-risk.

## 2. Canonical classes

### C0 — MICRO

Typical intent:

- typo/copy correction;
- small spacing correction;
- simple documentation fix;
- trivial isolated null guard.

Characteristics:

- no durable Product/Domain/Architecture semantics change;
- no protected/high-risk concern;
- isolated and reversible;
- minimal orchestration depth.

### C1 — SMALL

Typical intent:

- isolated bug;
- small component behavior adjustment;
- minor API validation fix inside existing contract.

Characteristics:

- bounded impact;
- existing architecture/domain boundaries preserved;
- independent review normally required;
- validation may be lightweight.

### C2 — STANDARD

Typical intent:

- ordinary capability;
- feature/change inside existing architecture;
- UI behavior backed by existing domain.

Characteristics:

- normal product/implementation change;
- review + QA/validation expectations;
- documentation reconciliation when contract changes.

### C3 — CROSS_CUTTING

Typical intent:

- frontend + backend + data persistence;
- multiple bounded contexts;
- large shared component migration;
- integration-heavy change.

Characteristics:

- multiple ownership/dependency surfaces;
- integration risk;
- architecture impact check normally required;
- safe parallelization may be possible after shared contracts exist.

### C4 — ARCHITECTURAL

Typical intent:

- new service;
- new canonical storage owner;
- major routing architecture;
- multi-tenancy model;
- eventing model;
- durable structural ownership/boundary change.

Expected orchestration references include:

- RFC;
- Architecture review;
- human decision/approval reference;
- ADR;
- implementation/migration planning;
- independent review;
- QA;
- documentation reconciliation.

### C5 — HIGH_RISK

Typical intent:

- authentication/authorization;
- billing/money movement;
- destructive data change;
- privacy/retention;
- secrets;
- production migration;
- security boundary;
- irreversible AI action.

Expected orchestration references include:

- relevant specialist review;
- human approval;
- rollback/recovery strategy;
- strong external evidence;
- enhanced QA/verification.

AI-only merge/release SHOULD be prohibited by default through external Human/Security policy.

## 3. Risk override

Any high-risk signal may override low apparent size.

Classification MUST consider the highest material impact.

## 4. Classification dimensions

UPOS-004 v1 recognizes dimensions from the source audit:

| Dimension | Provenance | Workflow interpretation |
|---|---|---|
| Product semantics impact | TASK_DIRECTIVE_REFINEMENT supported by source | may increase process depth / Product participation |
| Domain semantics impact | TASK_DIRECTIVE_REFINEMENT supported by C3 bounded-context source | may require Domain participation and higher class |
| Architecture impact | SOURCE_DERIVED | durable architecture change drives C4 |
| Cross-module breadth | SOURCE_DERIVED | broad multi-surface change drives C3+ |
| Data/model migration impact | SOURCE_DERIVED | migration/destructive/prod data signals may drive C3–C5 |
| Security/privacy impact | SOURCE_DERIVED | security boundary/privacy/secrets signals may drive C5 |
| Authorization impact | SOURCE_DERIVED | auth/authz is C5 signal |
| Production blast radius | TASK_DIRECTIVE_REFINEMENT supported by prod migration/hotfix/release | increases risk depth |
| Irreversibility | SOURCE_DERIVED | destructive/irreversible behavior is high-risk |
| External API compatibility | SOURCE_DERIVED from API workflow | backward compatibility/versioning affects routing/risk |
| User-facing behavior impact | TASK_DIRECTIVE_REFINEMENT supported by feature/UI source | affects Product/UX/QA participation |
| Operational impact | SOURCE_DERIVED | hotfix/release/production change affects route |
| Deployment complexity | TASK_DIRECTIVE_REFINEMENT supported by migration/release source | affects release/migration checkpoints |
| Uncertainty / missing truth | SOURCE_DERIVED from missing/stale Source-of-Truth and reclassification rules | blocks or raises classification until resolved |

## 5. Consuming external signals

If a dimension's substantive meaning belongs elsewhere, Workflow classification consumes the signal rather than redefining it.

Example:

```text
Security owner determines security sensitivity
→ UPOS-004 consumes signal
→ routing/classification depth changes
```

## 6. Change-class monotonic safety

During execution:

- upward reclassification is always allowed when material new risk is discovered;
- downward reclassification requires explicit evidence;
- stale classification MUST NOT be silently retained.

## 7. Risk inheritance

If an inseparable critical sub-change is C5, the resolved Workflow configuration MUST treat the containing change as C5 for protected orchestration.

If sub-changes can be safely decomposed, they MAY be routed separately by coherent ownership/dependency.

===== END VIRTUAL FILE: CHANGE_CLASSIFICATION_STANDARD.md =====


---

## VIRTUAL FILE 4/44 — `WORK_TYPE_AND_CONCERN_MODEL.md`

**Virtual path:** `WORK_TYPE_AND_CONCERN_MODEL.md`  
**Content checksum:** `2d95cfde8782`

===== BEGIN VIRTUAL FILE: WORK_TYPE_AND_CONCERN_MODEL.md =====

# Work Type and Concern Model

**ID:** UPOS-04-WTC-001  
**Type:** TAXONOMY / ROUTING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Work Type

Work Type represents the primary intention.

Canonical v1 Work Types:

| Work Type | Meaning | Base Workflow |
|---|---|---|
| `GENERIC_CHANGE` | bounded change not better classified below | `WFL-GENERIC-CHANGE` |
| `BUG_FIX` | correct observed behavior defect | `WFL-BUG-FIX` |
| `FEATURE` | add/change intended capability | `WFL-FEATURE` |
| `REFACTOR` | change internal structure while preserving intended behavior | `WFL-REFACTOR` |
| `DEPENDENCY_UPGRADE` | update external/internal dependency version/interface | `WFL-DEPENDENCY-UPGRADE` |
| `DOCUMENTATION_CHANGE` | documentation is the primary deliverable | `WFL-DOCUMENTATION-CHANGE` |
| `HOTFIX` | expedited recovery-oriented change | `WFL-HOTFIX` |
| `RELEASE` | orchestrate release of an already selected release candidate | `WFL-RELEASE` |

## 2. Concern

Concern is orthogonal to primary intention.

Canonical v1 concerns:

| Concern | Profile |
|---|---|
| `UI` | `WFP-UI` |
| `DESIGN_SYSTEM` | `WFP-DESIGN-SYSTEM` |
| `ARCHITECTURE` | `WFP-ARCHITECTURE` |
| `API` | `WFP-API` |
| `DATABASE_MIGRATION` | `WFP-DATABASE-MIGRATION` |
| `SECURITY` | `WFP-SECURITY` |
| `DOCUMENTATION_IMPACT` | `WFP-DOCUMENTATION-IMPACT` |

## 3. Why UI/API/DB/Security are concerns

They frequently coexist.

Example:

```text
Work Type: FEATURE
Concerns:
- UI
- API
- DATABASE_MIGRATION
- SECURITY
Change Class: C5
```

The resolved configuration is one Feature Workflow plus four compatible concern profiles, not four competing workflows.

## 4. Source-workflow normalization

Frozen examples are preserved as follows:

```text
Micro Change         → GENERIC_CHANGE + C0
Bug Fix              → BUG_FIX
New Feature          → FEATURE
UI Change            → base work type + UI profile
Design System Change → base work type + DESIGN_SYSTEM profile
Architecture Change  → base work type + ARCHITECTURE profile; durable architecture change => C4
API Change           → base work type + API profile
Database Migration   → base work type + DATABASE_MIGRATION profile
Security Change      → base work type + SECURITY profile
Refactor             → REFACTOR
Dependency Upgrade   → DEPENDENCY_UPGRADE
Hotfix               → HOTFIX
Documentation Change → DOCUMENTATION_CHANGE
Release              → RELEASE
```

## 5. Primary-intention rule

A Task MUST have one primary Work Type for routing.

A Task MAY have multiple Concerns.

If two independent primary intentions exist, the Task SHOULD be decomposed unless doing so would create an invalid intermediate system.

## 6. Concern detection

Concern detection is an orchestration classification.

It does not transfer authority to UPOS-004.

Concern-specific meaning remains with the relevant owner module/Role.

===== END VIRTUAL FILE: WORK_TYPE_AND_CONCERN_MODEL.md =====


---

## VIRTUAL FILE 5/44 — `WORKFLOW_PROFILE_STANDARD.md`

**Virtual path:** `WORKFLOW_PROFILE_STANDARD.md`  
**Content checksum:** `451abed29d7b`

===== BEGIN VIRTUAL FILE: WORKFLOW_PROFILE_STANDARD.md =====

# Workflow Profile / Overlay Standard

**ID:** UPOS-04-PRF-001  
**Type:** PROFILE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** profiles/*.md


## 1. Definition

A Workflow Profile is a reusable orchestration modifier applied to a compatible Base Workflow.

It represents a cross-cutting concern, not a competing primary Workflow.

## 2. A Profile may add

- Role participation references;
- Skill references;
- stages/checkpoints;
- stage dependencies;
- external gate references;
- approval references;
- handoff references;
- reclassification triggers;
- conditional minimum Change Class rules;
- completion requirements attributable to the concern.

## 3. A Profile may not

- redefine Role authority;
- copy Skill procedures;
- define Context retrieval;
- define Git mechanics;
- define Quality verdict/evidence semantics;
- grant permissions;
- bind concrete providers/commands/paths.

## 4. Profile compatibility

A Profile MUST declare:

```text
profile_id
version
compatible_work_types
conflicts
dependencies
risk implications
added roles
added skill references
added/modified stages
external gate references
reclassification triggers
```

## 5. Composition

Multiple Profiles MAY compose if:

- their stage dependencies are non-contradictory;
- Role/SoD constraints remain satisfiable;
- no profile conflicts are declared;
- required gates/approvals can all be represented;
- resulting workflow remains bounded and understandable.

## 6. Precedence

Profiles can only tighten the Base Workflow.

They MUST NOT remove a mandatory base requirement unless the base contract explicitly declares that requirement conditional and the profile resolves it safely.

Higher Change Class requirements override weaker profile/base defaults.

## 7. Conflict handling

Profile conflict:

```text
pause routing
→ identify conflicting orchestration requirements
→ reclassify / choose compatible base / decompose / escalate
```

No silent precedence guessing.

===== END VIRTUAL FILE: WORKFLOW_PROFILE_STANDARD.md =====


---

## VIRTUAL FILE 6/44 — `WORKFLOW_CONTRACT_STANDARD.md`

**Virtual path:** `WORKFLOW_CONTRACT_STANDARD.md`  
**Content checksum:** `7d0a3e04cca6`

===== BEGIN VIRTUAL FILE: WORKFLOW_CONTRACT_STANDARD.md =====

# Workflow Contract Standard

**ID:** UPOS-04-WCS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/WORKFLOW_CONTRACT_TEMPLATE.md


## 1. Requirement

Every production Base Workflow and Profile MUST have a versioned contract.

## 2. Base Workflow mandatory fields

```text
Identity
Purpose
Version
Lifecycle status

Applicability
Work Types
Allowed / required Change Classes
Concern compatibility

Entry Conditions
Required Source Classes
Context Interface Requirements

Roles
Role Participation
Separation-of-Duties Constraints

Skills
Skill Version / compatibility references

Stages
Stage dependencies
Stage entry conditions
Stage outputs
Stage exit conditions

Transitions
Transition conditions

Handoffs

External Gate References
Human Approval References
Security/Permission References

Reclassification Triggers
Rerouting Rules

Failure Modes
Retry Rules
Recovery Rules
Rework Loops

Pause / Block / Resume
Escalation

Cancellation
Completion Criteria
Terminal Outcomes

Observability Interface Requirements

Lifecycle
Version
Supersession
```

## 3. Roles

Workflow references canonical Role identities from UPOS-002.

It MUST NOT copy Agent Contracts.

## 4. Skills

Workflow references stable Skill IDs/versions from UPOS-003.

It MUST NOT copy Skill procedures.

## 5. Sources/context

Workflow may declare Required Source Classes and Context interface needs.

UPOS-005/01 resolve/assemble truth.

No physical project path belongs in the universal Workflow contract.

## 6. Gates

Workflow owns whether an external gate/result is required at a stage.

Workflow does not own the gate's internal evidence/verdict semantics.

## 7. Approvals

Workflow may require a Human/Security/Permission approval reference.

Authority/grant semantics remain external.

## 8. Stages

A Stage is a bounded orchestration phase.

A Stage contract MUST identify:

- stable `stage_id`;
- participating Roles;
- Skill references;
- dependencies;
- entry conditions;
- expected orchestration outputs;
- exit conditions;
- external gates;
- allowed rework/retry behavior.

A Stage display name MUST NOT be used as the Stage identity.

A canonical `stage_id` MUST remain stable within the Workflow/Profile lineage unless the Stage is semantically replaced.

Resolved Profile-added stages MUST also remain independently addressable and MUST NOT collide with Base Workflow stage identities.

## 9. Transitions

Only declared transitions are legal in automated/reference execution.

Every declared Transition MUST have a stable:

```text
transition_id
```

or an explicitly specified deterministic stable identifier equivalent.

`transition_id` identifies the transition rule, not a display phrase.

Transitions MUST be condition-driven, not implicit narrative jumps.

## 10. Terminal outcomes

Canonical terminal Workflow Result classes:

```text
COMPLETED
FAILED
CANCELLED
ESCALATED_TERMINAL
SUPERSEDED_BY_REROUTE
```

Project/runtime schemas may encode these later through the cross-cutting schemas layer.

===== END VIRTUAL FILE: WORKFLOW_CONTRACT_STANDARD.md =====


---

## VIRTUAL FILE 7/44 — `ROUTING_STANDARD.md`

**Virtual path:** `ROUTING_STANDARD.md`  
**Content checksum:** `80055639850e`

===== BEGIN VIRTUAL FILE: ROUTING_STANDARD.md =====

# Workflow Routing Standard

**ID:** UPOS-04-ROU-001  
**Type:** ROUTING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/ROUTING_DECISION_TEMPLATE.md


## 1. Routing inputs

Routing consumes:

- Task/Change Request;
- Source-of-Truth/context availability;
- Work Type recommendation;
- Concern signals;
- C0–C5 classification recommendation;
- relevant external policy signals;
- Role/Skill availability compatibility;
- unresolved governance conflicts.

## 2. Classification is not routing

```text
SKL-CLASSIFY-CHANGE
→ classification recommendation

UPOS-004 Change Classification Standard
→ canonical C0–C5 semantics

Routing
→ base workflow + profiles + class + external references

Orchestrator
→ coordinates route under UPOS-002 authority
```

## 3. Routing algorithm

Conceptual deterministic order:

```text
1. Accept Task / Change Request.
2. Resolve canonical Source-of-Truth prerequisites by interface.
3. Determine one primary Work Type.
4. Detect zero or more Concerns.
5. Classify C0–C5 against canonical criteria.
6. Apply risk overrides / inheritance.
7. Select Base Workflow by Work Type.
8. Compose compatible Concern Profiles.
9. Apply Change-Class process depth.
10. Enforce UPOS-002 SoD/role constraints.
11. Bind required Skill references by stable ID/version compatibility.
12. Add required external gate/approval references.
13. Validate dependencies/parallelism.
14. Produce attributable Routing Decision.
15. If unresolved conflict remains → BLOCK / ESCALATE, not guess.
```

## 4. Routing Decision identity

Every Routing Decision MUST have a stable, independently addressable:

```text
routing_decision_id
```

`routing_decision_id` identifies the decision artifact itself, not merely the Task or Workflow Instance.

It MUST:

- remain immutable for that Routing Decision record;
- be independently referenceable by provenance, Workflow Instances, approvals, and later observability;
- not be inferred from a display label;
- not be silently reused for a materially changed rerouting decision.

A materially changed reroute creates a new `routing_decision_id` and SHOULD preserve a reference to the superseded/prior Routing Decision.

This section defines semantic identity only. Machine encoding belongs to the cross-cutting schemas/runtime layer.

## 5. Routing Decision contract

A Routing Decision MUST include:

```text
routing_decision_id
task_id
work_type
change_class
classification_rationale
concerns
base_workflow_id
base_workflow_version
profiles
role_requirements
skill_references
sod_constraints
external_gate_references
approval_references
reclassification_triggers
source/context references
open conflicts / unknowns
```

## 6. No every-agent routing

Only required Roles/Skills participate.

## 7. Project stricter rules

Projects MAY impose stricter routing/classification via UPOS-011 bindings/policies.

Project overrides MUST NOT weaken non-overridable universal invariants.

## 8. Routing failure

Routing fails safely when:

- no authoritative classification basis exists;
- required Source-of-Truth is in active normative conflict;
- selected profiles conflict;
- required SoD cannot be satisfied;
- mandatory external policy cannot be resolved.

Outcome:

```text
BLOCKED_ROUTING
→ escalation / owner decision
```

===== END VIRTUAL FILE: ROUTING_STANDARD.md =====


---

## VIRTUAL FILE 8/44 — `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`

**Virtual path:** `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`  
**Content checksum:** `2c19f97d568b`

===== BEGIN VIRTUAL FILE: TASK_AND_WORKFLOW_INSTANCE_MODEL.md =====

# Task and Workflow Instance Model

**ID:** UPOS-04-TWI-001  
**Type:** STATE / INSTANCE MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Task

Task / Change Request is the work entering U-POS.

Task lifecycle is orchestration-facing and distinct from product feature lifecycle, Agent Run lifecycle, PR lifecycle, and Skill Invocation state.

Normalized Task states:

```text
NEW
CLASSIFIED
ROUTED
IN_PROGRESS
BLOCKED
DONE
CANCELLED
```

`IN_REVIEW`, `IN_QA`, and `READY_TO_MERGE` from the frozen-source suggested lifecycle are treated as stage-specific projections for applicable code workflows, not universal Task states for documentation/release workflows.

## 2. Stable Task identity

Every Task / Change Request MUST have a stable:

```text
task_id
```

`task_id` identifies the Task across classification, routing, Workflow Instances, reroutes, rework, and later provenance.

It is not a display title and MUST NOT change merely because the Task title/description changes.

This is a semantic identity requirement only; machine representation belongs to the cross-cutting schemas/runtime layer.

## 3. Workflow Definition vs Instance

```text
WORKFLOW DEFINITION
= durable versioned orchestration contract

WORKFLOW INSTANCE
= one execution of one Workflow Definition/version
  for one Task/Change
```

## 4. Stable Workflow Instance identity and attribution

Every Workflow Instance MUST have a stable:

```text
workflow_instance_id
```

A Workflow Instance MUST be attributable to:

```text
workflow_instance_id
workflow_definition_id
workflow_version
task_id
routing_decision_id
change_class
work_type
concerns / profile refs
current workflow state
current stage(s)
required roles
required skill refs
external gate refs
approval refs
```

## 5. Workflow Instance is not project truth

Workflow Instance state is operational orchestration state.

It MUST NOT be interpreted as canonical Product/Domain/Architecture truth.

## 6. Runtime representation

Exact persistence/event/schema implementation is outside Module 04.

Module 04 owns the semantic fields/states; runtime/observability encode them later.

===== END VIRTUAL FILE: TASK_AND_WORKFLOW_INSTANCE_MODEL.md =====


---

## VIRTUAL FILE 9/44 — `WORKFLOW_STATE_MODEL.md`

**Virtual path:** `WORKFLOW_STATE_MODEL.md`  
**Content checksum:** `a55643b58053`

===== BEGIN VIRTUAL FILE: WORKFLOW_STATE_MODEL.md =====

# Workflow State Model

**ID:** UPOS-04-STM-001  
**Type:** STATE MACHINE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Workflow Instance states

Canonical orchestration states:

```text
READY
RUNNING
PAUSED
BLOCKED
REWORK_REQUIRED
ESCALATED
COMPLETED
FAILED
CANCELLED
SUPERSEDED
```

## 2. Stage states

```text
PENDING
READY
RUNNING
BLOCKED
COMPLETED
SKIPPED
FAILED
CANCELLED
```

## 3. Stage identity

Every canonical or resolved Stage MUST be independently addressable by a stable:

```text
stage_id
```

The `stage_id` is semantic identity, not a display name.

For Base Workflow stages, v1 uses namespaced identifiers such as:

```text
WFL-FEATURE:SPEC
WFL-BUG-FIX:REVIEW
```

Profile-added checkpoints/stages use their Profile namespace, for example:

```text
WFP-UI:UI-VALIDATION
```

A resolved Workflow configuration MUST preserve the originating stable `stage_id` values so a later consumer can identify exactly which Stage produced/consumed an artifact.

## 4. Transition identity

Every declared transition rule MUST be independently addressable by a stable:

```text
transition_id
```

For Workflow-specific rules, v1 uses namespaced identifiers such as:

```text
WFL-FEATURE:TR-NORMAL-NEXT
WFL-FEATURE:TR-GATE-REWORK
```

Global Workflow-state transitions defined in this standard use stable identifiers listed below.

A `transition_id` MUST NOT be inferred from a human-readable display label.

## 5. Legal-transition principle

Automated/reference execution MUST only use transitions declared by the Workflow Definition/Profile resolution.

Typical instance transition rules:

| transition_id | From | To / condition |
|---|---|---|
| `WST-READY-RUNNING` | READY | RUNNING |
| `WST-RUNNING-PAUSED` | RUNNING | PAUSED |
| `WST-RUNNING-BLOCKED` | RUNNING | BLOCKED |
| `WST-RUNNING-REWORK` | RUNNING | REWORK_REQUIRED |
| `WST-RUNNING-ESCALATED` | RUNNING | ESCALATED |
| `WST-RUNNING-COMPLETED` | RUNNING | COMPLETED |
| `WST-RUNNING-FAILED` | RUNNING | FAILED |
| `WST-PAUSED-RUNNING` | PAUSED | RUNNING |
| `WST-BLOCKED-RUNNING` | BLOCKED | RUNNING |
| `WST-REWORK-RUNNING` | REWORK_REQUIRED | RUNNING |
| `WST-ESCALATED-RUNNING` | ESCALATED | RUNNING when authority/condition is resolved |
| `WST-ESCALATED-CANCELLED` | ESCALATED | CANCELLED |
| `WST-ESCALATED-FAILED` | ESCALATED | FAILED |
| `WST-ANY-CANCELLED` | any non-terminal state | CANCELLED when cancellation is authorized |
| `WST-ROUTE-SUPERSEDED` | current route | SUPERSEDED when rerouted |

## 6. Pause vs Block

`PAUSED`:
- deliberate checkpoint;
- may await human decision, scheduled action, or external condition.

`BLOCKED`:
- required condition/input/gate cannot currently be satisfied.

## 7. Rework

`REWORK_REQUIRED` means an existing stage/result must be revisited due to a failed external gate/finding or changed requirement.

Quality verdict meaning remains UPOS-007.

## 8. Escalated

`ESCALATED` means orchestration cannot proceed within currently delegated authority/routing.

Authority resolution remains UPOS-002/10/01.

## 9. Terminal semantics

`COMPLETED`, `FAILED`, `CANCELLED`, and `SUPERSEDED` are terminal for that Workflow Instance version/route.

A reroute creates/continues a new resolved configuration while preserving provenance to the superseded route.

===== END VIRTUAL FILE: WORKFLOW_STATE_MODEL.md =====


---

## VIRTUAL FILE 10/44 — `RECLASSIFICATION_AND_REROUTING.md`

**Virtual path:** `RECLASSIFICATION_AND_REROUTING.md`  
**Content checksum:** `ee4945086c62`

===== BEGIN VIRTUAL FILE: RECLASSIFICATION_AND_REROUTING.md =====

# Reclassification and Rerouting

**ID:** UPOS-04-RCR-001  
**Type:** RECLASSIFICATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Mandatory reclassification rule

A Workflow MUST NOT silently continue under stale classification after material new risk/impact is discovered.

## 2. Reclassification triggers

Triggers include:

- new architecture decision required;
- previously unknown database/data migration;
- security/auth/privacy/protected-action impact;
- expanded Product/Domain semantics;
- new external API compatibility impact;
- discovered cross-module breadth;
- production blast radius materially higher than known;
- irreversibility/destructive action discovered;
- missing/conflicting canonical truth affecting risk;
- scope expansion beyond current route;
- plan material change.

## 3. Upward reclassification

Always permitted when justified by new evidence.

Current Workflow Instance MUST pause or block before executing stages invalid under the higher class.

## 4. Downward reclassification

Requires explicit evidence that the higher-risk signal no longer applies.

Downward reclassification MUST NOT be used to bypass required gates/approvals already materially triggered.

## 5. What remains valid

After reclassification, completed outputs may be reused only if:

- their producing contract/version is still compatible;
- required sources remain valid;
- stronger SoD/gates do not invalidate independence;
- no changed assumption affects correctness.

Otherwise they MUST be rechecked/reworked.

## 6. Rerouting

Reclassification may cause:

```text
same base workflow + deeper class
same base workflow + added profiles
different base workflow
task decomposition
terminal escalation
```

Old routing provenance remains preserved.

## 7. Scope expansion

When execution discovers extra work:

```text
pause
→ classify discovered work
→ decide:
   required for current task?
   separate follow-up?
   new concern?
   higher change class?
   different base work type?
```

No silent scope expansion.

## 8. Risk inheritance

If an inseparable sub-change is C5, the containing route inherits C5 protected orchestration.

If it can be safely separated, split by coherent ownership/dependency rather than arbitrary file count.

===== END VIRTUAL FILE: RECLASSIFICATION_AND_REROUTING.md =====


---

## VIRTUAL FILE 11/44 — `FAILURE_RETRY_RECOVERY.md`

**Virtual path:** `FAILURE_RETRY_RECOVERY.md`  
**Content checksum:** `44ed8c8c82ff`

===== BEGIN VIRTUAL FILE: FAILURE_RETRY_RECOVERY.md =====

# Failure, Retry and Recovery

**ID:** UPOS-04-FRR-001  
**Type:** FAILURE / RECOVERY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** RECLASSIFICATION_AND_REROUTING.md, WORKFLOW_STATE_MODEL.md

## 1. Concept separation

UPOS-004 distinguishes:

```text
RETRY
= repeat the same bounded operation/stage after a transient or repeatable failure
  without semantic rejection of the produced result

REWORK
= return to the producer stage because the produced output was rejected,
  insufficient, or non-conformant

RECOVERY
= controlled alternate orchestration path after failure

RECLASSIFICATION
= reassessment of impact/risk because material facts changed

REROUTING
= creation/resolution of a changed Workflow configuration

ESCALATION
= transition to different/higher authority because current delegated
  authority/routing cannot resolve the condition
```

Invariant:

```text
RETRY
!= REWORK
!= RECOVERY
!= RECLASSIFICATION
!= REROUTING
!= ESCALATION
```

## 2. Universal non-convergence invariant

```text
No infinite retry loops.
No infinite rework loops.
```

Retry and rework MUST both be bounded before autonomous/reference execution relies on them.

The exact numeric threshold MAY be supplied by:

```text
Workflow policy
Project policy
UPOS-011 binding
```

Threshold exhaustion MUST cause a controlled transition appropriate to the cause, such as:

```text
ESCALATE
REPLAN
RECLASSIFY
REROUTE
REQUEST_OWNER_DECISION
CANCEL
FAIL
```

Frozen-source examples such as `2 failed implementation attempts` or `3 review rejection cycles` remain illustrative and are not universal mandatory thresholds.

## 3. Workflow failure taxonomy

This taxonomy classifies orchestration response. It does not take substantive ownership from Security, Quality, Permissions, Source-of-Truth, or provider adapters.

| Failure class | Workflow meaning | Permitted orchestration responses |
|---|---|---|
| `TRANSIENT_EXECUTION_FAILURE` | Same bounded operation may succeed later without semantic change | retry; block; escalate/fail when retry budget is exhausted |
| `CONTRACT_FAILURE` | Produced/required artifact is non-conformant with an applicable contract | rework; replan; block; escalate; fail |
| `MISSING_REQUIRED_TRUTH` | Required canonical/source truth cannot be resolved | block; escalate; request owner decision; cancel/fail if unresolved |
| `CANONICAL_CONFLICT` | Active authoritative sources conflict | block; escalate; request owner decision; replan after resolution |
| `AUTHORITY_CONFLICT` | Current route/Role cannot resolve required authority | block; escalate; reroute/reassign through external authority rules; cancel |
| `SCOPE_EXPANSION` | Required work exceeds classified/routed scope | replan; reclassify; reroute; split task; cancel |
| `RISK_DISCOVERY` | New facts materially change impact/risk | pause/block; reclassify; reroute; escalate |
| `GATE_REJECTION` | An externally owned gate rejects/does not accept an artifact/result | rework; replan; block; escalate; fail according to external gate semantics |
| `SECURITY_VETO` | UPOS-010/Security authority reports a blocking veto | block; escalate; cancel/fail; rework only when the external remediation contract permits it |
| `HUMAN_DECISION_REQUIRED` | Current route requires a human/owner decision | pause/block; escalate; request owner decision; cancel |
| `DEPENDENCY_FAILURE` | Required upstream stage/service/artifact/dependency is unavailable or failed | retry if transient; block; replan; reroute; fail |
| `PERSISTENT_TOOL_PROVIDER_FAILURE` | Tool/provider failure persists beyond retry budget | block; replan; reroute through a valid external adapter/policy; escalate; fail |
| `NON_CONVERGENT_REWORK` | Repeated rework does not converge within declared bound | escalate; replan; reclassify; reroute; request owner decision; cancel/fail |

### Ownership boundary

- `GATE_REJECTION` does not define Quality PASS/FAIL; UPOS-007 owns that.
- `SECURITY_VETO` does not define Security veto substance; UPOS-010 owns that.
- `AUTHORITY_CONFLICT` does not redefine Role authority; UPOS-002 owns that.
- `MISSING_REQUIRED_TRUTH` / `CANONICAL_CONFLICT` do not redefine canonicality; UPOS-01/05 own source resolution.
- provider/tool semantics remain UPOS-011/runtime adapters.

## 4. Retry

Retry is appropriate only when the same bounded operation remains semantically valid, the failure is transient/repeatable, required truth/authority/policy did not change, and retry budget remains.

Do not retry unchanged for canonical conflict, authority conflict, scope expansion, changed risk, persistent gate rejection, or exhausted provider/tool failure.

## 5. Rework

Rework returns responsibility to the producer stage because an output is rejected, insufficient, or non-conformant.

A rework loop MUST:

- identify the producer stage/result being corrected;
- preserve independent Reviewer/QA roles where required;
- consume the externally owned finding/rejection without redefining it;
- have an explicit bounded rework policy;
- transition to controlled escalation/replan/reclassification/rerouting/owner decision/cancel/fail when the bound is exhausted.

Rework MUST NOT silently become an infinite review-fix-review cycle.

## 6. Recovery

Recovery is a controlled alternate orchestration path after failure.

Recovery may include replan, reassign/reroute, split task, rollback request/reference, pause/block, human/owner escalation, cancel, or fail.

Recovery MUST preserve Role authority, SoD, source validity, stronger Change-Class requirements, and external approval/gate constraints.

## 7. Reclassification / rerouting relationship

Reclassification is used when impact/risk facts changed.

Rerouting is used when the resolved Workflow configuration must change.

They are governed by `RECLASSIFICATION_AND_REROUTING.md`.

Retry or rework MUST NOT be used to avoid required reclassification/rerouting.

## 8. Rollback

UPOS-004 may require a rollback/recovery strategy reference at C3+ and especially C4/C5.

Actual Git/data/deployment rollback mechanics remain external.

## 9. Terminal failure

A Workflow may terminate `FAILED` when safe controlled recovery is unavailable, exhausted, explicitly rejected, or no longer justified.

Failure does not silently canonize partial outputs.

===== END VIRTUAL FILE: FAILURE_RETRY_RECOVERY.md =====


---

## VIRTUAL FILE 12/44 — `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md`

**Virtual path:** `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md`  
**Content checksum:** `bb6c64be5046`

===== BEGIN VIRTUAL FILE: PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md =====

# Parallelism and Dependency Orchestration

**ID:** UPOS-04-PAR-001  
**Type:** DEPENDENCY ORCHESTRATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

Parallelize only independent nodes whose shared contracts are already defined sufficiently for safe execution.

## 2. Dependency graph

Workflow may model stage/task dependencies such as:

```text
Domain contract
→ API contract
→ Backend
→ Frontend
→ Integration QA
```

This is orchestration dependency, not Git/file ownership policy.

## 3. Shared contract first

Before parallel execution across boundaries, establish relevant shared contract(s), e.g.:

```text
API contract
event contract
domain interface
design component contract
```

Their semantic ownership remains with their canonical owners.

## 4. Parallel-stage conditions

Parallelization is allowed when:

- dependencies are satisfied;
- Role authority is clear;
- shared contracts are stable enough;
- profiles do not impose serial ordering;
- external gates do not require prior completion;
- Engineering Governance reports no unresolved collision constraint.

## 5. Shared-file/collision boundary

UPOS-004 may pause/serialize orchestration when UPOS-006 reports a collision.

It does not own worktree/branch/file-lock mechanics.

## 6. Change decomposition

Split work by coherent ownership and dependency, not arbitrary file count.

Do not split when doing so creates invalid intermediate system state.

===== END VIRTUAL FILE: PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md =====


---

## VIRTUAL FILE 13/44 — `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`

**Virtual path:** `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`  
**Content checksum:** `8b6dc49b4f2c`

===== BEGIN VIRTUAL FILE: WORKFLOW_LIFECYCLE_AND_VERSIONING.md =====

# Workflow Lifecycle and Versioning

**ID:** UPOS-04-LFV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Workflow Definition lifecycle

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

This lifecycle is separate from Workflow Instance execution state.

## 2. Deprecation

Deprecated Definitions SHOULD NOT be selected for new routing when a supported replacement exists.

Historical executions remain attributable to their original Workflow version.

## 3. Versioning principle

Workflow Definition version MUST change when required gates, required stage sequence, routing applicability, mandatory profiles/roles/skills, terminal semantics, or failure/reclassification behavior changes materially.

## 4. Semantic versioning convention

### MAJOR
Breaking orchestration compatibility:

- removed/reordered mandatory stage in a way that changes consumers;
- incompatible entry/exit conditions;
- new mandatory gate/approval invalidating old assumptions;
- changed routing/work-type semantics;
- incompatible terminal result meaning.

### MINOR
Backward-compatible orchestration expansion:

- optional concern support;
- optional stage;
- compatible new Skill/Role reference;
- additional non-breaking validation/checkpoint.

### PATCH
Editorial/non-semantic correction only.

## 5. Supersession

Registry/catalog MUST point from deprecated Workflow/Profile to its replacement when one exists.

## 6. Instance pinning

A Workflow Instance is pinned to a resolved Workflow/Profile version set.

A material Definition change does not mutate an in-flight instance silently.

Migration/rerouting requires an explicit decision with provenance.

===== END VIRTUAL FILE: WORKFLOW_LIFECYCLE_AND_VERSIONING.md =====


---

## VIRTUAL FILE 14/44 — `WORKFLOW_CATALOG.md`

**Virtual path:** `WORKFLOW_CATALOG.md`  
**Content checksum:** `786fd01dba70`

===== BEGIN VIRTUAL FILE: WORKFLOW_CATALOG.md =====

# Workflow Catalog

**ID:** UPOS-04-CAT-001  
**Type:** CATALOG / DISCOVERY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** workflows/*.md, profiles/*.md

## 1. Catalog contract

The Catalog is the canonical discovery/index layer for active and historical Workflow Definitions and Workflow Profiles.

It MUST NOT duplicate full Workflow/Profile contracts.

Explicit `none` means the field is applicable and currently has no value.

`—` means not applicable for that registry entry.

## 2. Base Workflow registry

| workflow_id | name | version | status | purpose | work_type | supported_change_classes | compatible_profiles | required_roles | required_skills | supersedes | replacement | contract_ref |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| `WFL-BUG-FIX` | bug-fix | 1.0.0 | ACTIVE | Orchestrate diagnosis and correction of an observed behavior defect. | `BUG_FIX` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller | SKL-CLASSIFY-CHANGE, SKL-REPRODUCE-BUG, SKL-WRITE-REGRESSION-TEST, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/bug-fix.md` |
| `WFL-DEPENDENCY-UPGRADE` | dependency-upgrade | 1.0.0 | ACTIVE | Orchestrate dependency version/interface change with explicit compatibility and regression consideration. | `DEPENDENCY_UPGRADE` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY | Orchestrator, Implementer, Reviewer, QA, Security when relevant, Merge Controller | SKL-ANALYZE-IMPACT, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-REVIEW-SECURITY (conditional), SKL-ASSESS-MERGE-READINESS | none | none | `workflows/dependency-upgrade.md` |
| `WFL-DOCUMENTATION-CHANGE` | documentation-change | 1.0.0 | ACTIVE | Orchestrate a documentation-primary change against canonical ownership without unnecessary code gates. | `DOCUMENTATION_CHANGE` | C0–C5 | WFP-DOCUMENTATION-IMPACT | Orchestrator, Documentation Guardian, Reviewer as required | SKL-CLASSIFY-CHANGE, SKL-RECONCILE-DOCUMENTATION, SKL-REVIEW-DIFF (when review required) | none | none | `workflows/documentation-change.md` |
| `WFL-FEATURE` | feature | 1.0.0 | ACTIVE | Orchestrate delivery of a new or materially changed capability. | `FEATURE` | C2–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Product, Implementer, Reviewer, QA, Documentation Guardian, Merge Controller | SKL-CREATE-FEATURE-SPEC, SKL-ANALYZE-IMPACT, SKL-CLASSIFY-CHANGE, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-RECONCILE-DOCUMENTATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/feature.md` |
| `WFL-GENERIC-CHANGE` | generic-change | 1.0.0 | ACTIVE | Orchestrate a bounded change that is not better represented by another primary Work Type. | `GENERIC_CHANGE` | C0–C3 by default; C4/C5 only when routing/profile/policy proves compatibility | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, Merge Controller | SKL-CLASSIFY-CHANGE, SKL-CREATE-IMPLEMENTATION-PLAN (C1+ or when needed), SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/generic-change.md` |
| `WFL-HOTFIX` | hotfix | 1.0.0 | ACTIVE | Orchestrate expedited recovery without treating urgency as permission to skip safety. | `HOTFIX` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller, Human approval reference as externally required | SKL-ANALYZE-INCIDENT, SKL-REPRODUCE-BUG (where possible), SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-PREPARE-RELEASE, SKL-ASSESS-MERGE-READINESS, SKL-CAPTURE-LEARNING (follow-up candidate) | none | none | `workflows/hotfix.md` |
| `WFL-REFACTOR` | refactor | 1.0.0 | ACTIVE | Orchestrate structural implementation change intended to preserve externally intended behavior. | `REFACTOR` | C1–C5 | WFP-API, WFP-ARCHITECTURE, WFP-DATABASE-MIGRATION, WFP-DESIGN-SYSTEM, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY, WFP-UI | Orchestrator, Implementer, Reviewer, QA, Merge Controller | SKL-ANALYZE-IMPACT, SKL-CREATE-IMPLEMENTATION-PLAN, SKL-IMPLEMENT-CHANGE, SKL-REVIEW-DIFF, SKL-QA-VALIDATION, SKL-ASSESS-MERGE-READINESS | none | none | `workflows/refactor.md` |
| `WFL-RELEASE` | release | 1.0.0 | ACTIVE | Orchestrate release of a selected release candidate through required external operational/security/human checkpoints. | `RELEASE` | C2–C5 | WFP-API, WFP-DATABASE-MIGRATION, WFP-DOCUMENTATION-IMPACT, WFP-SECURITY | Orchestrator, DevOps / SRE or project release specialist, QA, Security when relevant, Human approval reference, Documentation Guardian as relevant | SKL-PREPARE-RELEASE, SKL-QA-VALIDATION, SKL-REVIEW-SECURITY (conditional), SKL-RECONCILE-DOCUMENTATION (conditional) | none | none | `workflows/release.md` |

## 3. Profile registry

| profile_id | concern | version | status | purpose | compatible_work_types | dependencies | conflicts | supersedes | replacement | contract_ref |
|---|---|---:|---|---|---|---|---|---|---|---|
| `WFP-API` | API | 1.0.0 | ACTIVE | Apply `API`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/api.md` |
| `WFP-ARCHITECTURE` | ARCHITECTURE | 1.0.0 | ACTIVE | Apply `ARCHITECTURE`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX | none | none | none | none | `profiles/architecture.md` |
| `WFP-DATABASE-MIGRATION` | DATABASE_MIGRATION | 1.0.0 | ACTIVE | Apply `DATABASE_MIGRATION`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/database-migration.md` |
| `WFP-DESIGN-SYSTEM` | DESIGN_SYSTEM | 1.0.0 | ACTIVE | Apply `DESIGN_SYSTEM`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR | none | none | none | none | `profiles/design-system.md` |
| `WFP-DOCUMENTATION-IMPACT` | DOCUMENTATION_IMPACT | 1.0.0 | ACTIVE | Apply `DOCUMENTATION_IMPACT`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | all base workflows | none | none | none | none | `profiles/documentation-impact.md` |
| `WFP-SECURITY` | SECURITY | 1.0.0 | ACTIVE | Apply `SECURITY`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE | none | none | none | none | `profiles/security.md` |
| `WFP-UI` | UI | 1.0.0 | ACTIVE | Apply `UI`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow. | GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, HOTFIX | none | none | none | none | `profiles/ui.md` |

## 4. Discovery semantics

Registry entries support stable identity lookup, lifecycle/status discovery, compatibility discovery, required Role/Skill reference discovery, supersession/replacement discovery, and canonical contract resolution.

Full orchestration semantics remain in the referenced canonical contracts.

## 5. Supersession / replacement

When a Workflow/Profile is deprecated or superseded, the Catalog MUST explicitly identify:

```text
supersedes
replacement
```

Historical entries remain discoverable for provenance.

A blank/missing supersession field is not equivalent to `none`; the registry uses explicit values.

===== END VIRTUAL FILE: WORKFLOW_CATALOG.md =====


---

## VIRTUAL FILE 15/44 — `CROSS_MODULE_INTERFACES.md`

**Virtual path:** `CROSS_MODULE_INTERFACES.md`  
**Content checksum:** `1e09480f2db8`

===== BEGIN VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

# Module 04 Cross-Module Interfaces

**ID:** UPOS-04-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth

**Provides:** Workflow-required Source Class declarations and orchestration references.  
**Consumes:** canonical owner/source resolution, normative conflict behavior, knowledge lifecycle.  
**Must not redefine:** project truth/canonical promotion.

## UPOS-002 — Agent Organization

**Provides:** Role participation/routing requirements and stage responsibility references.  
**Consumes:** Role identity, authority, delegation, SoD, handoff contract, human governance.  
**Must not redefine:** Role authority or handoff semantics.

Required invariants:

```text
Implementer != Final Reviewer
high-risk: Implementer != Reviewer != Merge Controller
```

## UPOS-003 — Skills System

**Provides:** when/where Skill invocation is required by reference.  
**Consumes:** stable Skill IDs/versions/contracts.  
**Must not redefine:** Skill procedure/evaluation.

## UPOS-005 — Context & Memory

**Provides:** source/context requirements per Workflow/Stage.  
**Consumes:** retrieval, assembly, memory, budget/freshness semantics.  
**Must not redefine:** how context is retrieved/ranked.

## UPOS-006 — Engineering Governance

**Provides:** orchestration points requiring engineering actions/results.  
**Consumes:** branch/commit/PR/merge/worktree/collision mechanics.  
**Must not redefine:** Git policy.

## UPOS-007 — Quality System

**Provides:** which external review/QA/evidence/readiness gates are required and where.  
**Consumes:** gate/evidence/finding/verdict semantics.  
**Must not redefine:** what PASS/FAIL/BLOCKED means.

## UPOS-008 — Observability

**Provides:** stable semantic identity references suitable for future provenance/telemetry correlation:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

**Consumes:** event/trace/metric/retention semantics.  
**Must not redefine:** telemetry/event/trace model, occurrence/event identity, retention, metrics, or dashboard semantics.

Stable identity belongs to UPOS-004; observability semantics remain UPOS-008.

## UPOS-009 — Learning

**Provides:** orchestration completion/failure/rework signals that may become learning inputs.  
**Consumes:** learning detection/evolution proposals.  
**Must not redefine:** learning promotion.

## UPOS-010 — Security & Permissions

**Provides:** protected checkpoint/approval references required by classification/profiles.  
**Consumes:** permissions, protected actions, secrets, human/security approval semantics.  
**Must not redefine:** grants/veto/security truth.

## UPOS-011 — Project Adapter

**Provides:** abstract requirements for commands/providers/project-specific stricter policies.  
**Consumes:** concrete bindings, commands, paths, provider/runtime adapters.  
**Must not redefine:** universal Workflow semantics.

## Cross-cutting schemas/runtime

Future machine-readable WorkflowDefinition/Task/RoutingDecision/WorkflowInstance representations must trace to this normative Markdown and must not create independent semantics.

===== END VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====


---

## VIRTUAL FILE 16/44 — `MODULE_04_DEFINITION_OF_DONE.md`

**Virtual path:** `MODULE_04_DEFINITION_OF_DONE.md`  
**Content checksum:** `1fc5ccfb1516`

===== BEGIN VIRTUAL FILE: MODULE_04_DEFINITION_OF_DONE.md =====

# Module 04 Definition of Done

**ID:** UPOS-04-DOD-001  
**Type:** DEFINITION OF DONE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


UPOS-004 v1.0 is complete when:

- [x] Workflow Engine has one clear ownership boundary.
- [x] Task, Change Class, Work Type, Concern, Workflow Definition, Profile, Instance, Stage, Transition, Gate Reference, Routing Decision, Workflow Result are distinct.
- [x] three-axis model is resolved without combinatorial explosion.
- [x] C0–C5 classification exists and is impact/risk-based.
- [x] classification dimensions have provenance.
- [x] classification is separate from routing.
- [x] reclassification/rerouting is explicit.
- [x] Workflow Contract Standard exists.
- [x] Workflow Definition lifecycle/versioning exists.
- [x] Workflow Instance state model exists.
- [x] stable Task/Routing/Workflow Instance/Stage/Transition identities exist.
- [x] bounded retry/rework/recovery and non-convergence handling exist.
- [x] Workflow failure taxonomy exists.
- [x] pause/block/rework/escalation/cancellation/completion semantics exist.
- [x] Base Workflow catalog exists and supports lifecycle/supersession/discovery fields.
- [x] Concern Profile catalog exists.
- [x] frozen UI/DS/Architecture/API/DB/Security workflows are preserved as profiles.
- [x] Micro is represented as C0 routing depth, not a competing work type.
- [x] UPOS-002 SoD constraints are enforceable by routing.
- [x] Skill procedures are referenced, not copied.
- [x] Context retrieval remains UPOS-005.
- [x] Git mechanics remain UPOS-006.
- [x] Quality verdict semantics remain UPOS-007.
- [x] Security/permission grants remain UPOS-010.
- [x] project/provider bindings remain UPOS-011.
- [x] cross-module interfaces are explicit.
- [x] no unresolved P0/P1 Module-04 semantic gaps remain.
- [x] `UNMAPPED MODULE-04 SOURCE REQUIREMENTS = 0`.

===== END VIRTUAL FILE: MODULE_04_DEFINITION_OF_DONE.md =====


---

## VIRTUAL FILE 17/44 — `MODULE_04_TRACEABILITY.md`

**Virtual path:** `MODULE_04_TRACEABILITY.md`  
**Content checksum:** `9792ec8dcc81`

===== BEGIN VIRTUAL FILE: MODULE_04_TRACEABILITY.md =====

# Module 04 Traceability

**ID:** UPOS-04-TRC-001  
**Type:** TRACEABILITY / NORMATIVE COVERAGE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analysis/SOURCE_SECTION_DISPOSITION.md, analysis/TRACEABILITY_VALIDATION.md


**Frozen source SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`  
**Implementation directive SHA-256:** `7c8465f949ef875e88c98044f051cb5a49f52e332e626316c91f35486536685b`

## Traceability rule

Each Module-04 requirement maps:

```text
stable requirement ID
→ frozen source / implementation directive section
→ extracted semantic requirement
→ canonical Module 04 artifact
```

Mixed source sections extract only Workflow-owned semantics; remaining semantics are deferred.

## Requirements

| Requirement | Source | Extracted requirement | Canonical artifact |
|---|---|---|---|
| `WFL-REQ-001` | §3.11 | Process depth must be risk-based; trivial and high-risk changes must not use identical orchestration depth. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-002` | §22, Appendix D | Every production Workflow must define trigger/applicability, entry/exit conditions, risk classes, Roles, Skills, sources, steps/stages, parallelism, external gates, human approvals, failure handling, completion and observability interfaces. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-003` | §23 | Canonical Change Classes are C0 Micro, C1 Small, C2 Standard, C3 Cross-cutting, C4 Architectural, C5 High-risk. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-004` | §24 | C0 represents micro/isolated low-risk work and normally uses minimal orchestration depth. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-005` | §25 | C1 represents small bounded work with independent review and lightweight validation. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-006` | §26 | C2 represents standard feature/change work inside existing architecture with normal review/QA/docs orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-007` | §27 | C3 represents cross-cutting work spanning multiple layers/contexts and requires integration-aware orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-008` | §28 | C4 represents durable architectural change and requires architecture decision orchestration including RFC/review/human/ADR references. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-009` | §29 | C5 represents high-risk change such as auth/authz/billing/destructive data/privacy/secrets/production migration/security boundary/irreversible AI action and requires enhanced protected orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-010` | §30 | Classification is based on impact, not line count; small diffs may be high-risk. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-011` | §79 | Workflow failure handling must support explicit recovery options such as retry, re-plan, reassign, split, rollback reference, abort or human escalation. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-012` | §80 | Retries must be bounded; exact thresholds may be project-specific and repeated failure should trigger re-plan/escalation rather than indefinite loops. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-013` | §85 | Frozen Micro Change semantics are preserved as GENERIC_CHANGE routed at C0 with lightweight implementation/review/readiness depth. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-014` | §86, Appendix P | Bug Fix orchestration includes reproduction, regression test where practical, plan/fix, independent review, QA, conditional docs and readiness. | `workflows/bug-fix.md` |
| `WFL-REQ-015` | §87, Appendix O | Feature orchestration includes Product/spec, impact analysis, classification, plan, implementation, independent review, QA, conditional Security/docs and readiness/human references. | `workflows/feature.md` |
| `WFL-REQ-016` | §88 | UI Change semantics are modeled as a UI Concern Profile applied to the selected base Work Type rather than a competing Workflow. | `profiles/ui.md` |
| `WFL-REQ-017` | §89 | Design System Change semantics are modeled as a Design System Concern Profile with registry/reuse decision, DS review, spec/implementation, visual QA and migration/deprecation references. | `profiles/design-system.md` |
| `WFL-REQ-018` | §90, Appendix Q | Architecture Change semantics are modeled as an Architecture Profile; durable architecture changes require C4 and RFC/review/human/ADR/migration planning orchestration. | `profiles/architecture.md` |
| `WFL-REQ-019` | §91 | API Change semantics are modeled as an API Profile with contract impact, backward compatibility/versioning, tests/consumer/docs checkpoints. | `profiles/api.md` |
| `WFL-REQ-020` | §92 | Database Migration semantics are modeled as a Database Migration Profile with data impact, migration/compatibility, backup/recovery, verification and rollback/forward-fix references. | `profiles/database-migration.md` |
| `WFL-REQ-021` | §93 | Security Change semantics are modeled as a Security Profile with threat/security design, approval, security review, QA and audit/evidence references. | `profiles/security.md` |
| `WFL-REQ-022` | §94 | Refactor Work Type must state behavior-preservation intent/reason/scope and must not silently mix unrelated feature change. | `workflows/refactor.md` |
| `WFL-REQ-023` | §95 | Dependency Upgrade Work Type must analyze breaking/security implications and include build/test/regression orchestration references. | `workflows/dependency-upgrade.md` |
| `WFL-REQ-024` | §96 | Hotfix is recovery-optimized but must not skip safety; it uses expedited independent review/validation/human/release follow-up as required. | `workflows/hotfix.md` |
| `WFL-REQ-025` | §97 | Documentation Change Work Type checks canonical ownership, updates documentation, validates links/contradictions/review, and avoids code gates unless behavior/generated docs require them. | `workflows/documentation-change.md` |
| `WFL-REQ-026` | §98 | Release Work Type orchestrates release candidate checks, migration/release notes/security/ops/human checkpoints, deployment reference, verification and rollback if needed. | `workflows/release.md` |
| `WFL-REQ-027` | §122 | Routing conceptually resolves project sources/outcome/classification/affected domains/workflow/roles/human gates/context before execution and handles conflict/gate failure explicitly. | `ROUTING_STANDARD.md` |
| `WFL-REQ-028` | §129 | Change Classification output/routing decision must be structured and attributable, including class, rationale, affected concerns/specialists and gate implications. | `ROUTING_STANDARD.md` |
| `WFL-REQ-029` | §136 | Material scope expansion requires pause and classification of discovered work; no silent expansion. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-030` | §146 | Workflow orchestration must model dependencies and parallelize only independent nodes. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-031` | §185 | Workflow Definition version must change when required gates or sequence materially changes. | `WORKFLOW_LIFECYCLE_AND_VERSIONING.md` |
| `WFL-REQ-032` | §194 | Workflow/task status is distinct from Product feature lifecycle and must not reuse feature enums. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-033` | §196 | Task lifecycle must be explicit and distinct from Workflow Instance/Agent Run/PR/product lifecycles. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-034` | §199 | Workflow automation requires an explicit legal state-transition model. | `WORKFLOW_STATE_MODEL.md` |
| `WFL-REQ-035` | §202 | Material implementation-plan change requires reason/update and reclassification if risk/impact changes. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-036` | §203 | Upward reclassification must be supported; downward reclassification requires evidence. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-037` | §204 | Risk inheritance applies to inseparable critical sub-changes; C5 may elevate the containing route. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-038` | §205 | Change decomposition is by coherent ownership/dependency, not arbitrary file count. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-039` | §207 | Cross-boundary parallel implementation should establish shared contracts before dependent parallel stages execute. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-040` | §221.3 | Workflow routing must not run every agent for every task; only justified Roles/Skills participate. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-041` | Appendix D | Workflow template semantics are normalized into the canonical Workflow Contract Standard. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-042` | Appendix J | Risk matrix intent is consumed for orchestration depth, while Review/QA/Human semantics remain owned by external modules. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-043` | Appendix O | Example New Feature route is preserved by the Feature base workflow plus applied concerns/classification. | `workflows/feature.md` |
| `WFL-REQ-044` | Appendix P | Example Bug Fix route is preserved by the Bug Fix base workflow. | `workflows/bug-fix.md` |
| `WFL-REQ-045` | Appendix Q | Example Architecture Change route is preserved by Base Workflow + Architecture Profile + C4 classification. | `profiles/architecture.md` |
| `WFL-REQ-046` | Final principle 4 | Risk determines process depth. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-047` | Implementation directive §2–3 | Task, Change Class, Work Type, Concern, Workflow Definition, Profile, Instance, Stage, Transition, Gate Reference, Routing Decision and Workflow Result are distinct concepts. | `README.md` |
| `WFL-REQ-048` | Implementation directive §3 | Routing uses three independent axes: Change Class, Work Type, and Concerns, composed as Base Workflow + Profiles + Class. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-049` | Implementation directive §3 | UI, Design System, Architecture, API, Database and Security are Concern Profiles rather than mutually exclusive primary Workflows in v1. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-050` | Implementation directive §7 | Classification dimensions must carry provenance SOURCE_DERIVED / TASK_DIRECTIVE_REFINEMENT / NEW_PROPOSAL. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-051` | Implementation directive §8 | classify-change Skill produces a recommendation; UPOS-004 owns canonical class semantics and routing. | `ROUTING_STANDARD.md` |
| `WFL-REQ-052` | Implementation directive §9 | Material new facts invalidate stale classification and trigger pause/reclassification/rerouting checks. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-053` | Implementation directive §10 | Workflow contracts reference Roles/Skills/gates/approvals without copying their owned semantics. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-054` | Implementation directive §11 | Workflow Definition and Workflow Instance are distinct; each Instance is attributable to Definition/version, Task, routing/classification/work type/concerns/stages/roles/skills/gates. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-055` | Implementation directive §12 | Workflow Definition lifecycle is distinct from Workflow Instance execution state. | `WORKFLOW_LIFECYCLE_AND_VERSIONING.md` |

| `WFL-REQ-056` | Final reconciliation directive §2 | Every Routing Decision has stable `routing_decision_id` independent from Task/Workflow Instance and suitable for provenance. | `ROUTING_STANDARD.md`, `templates/ROUTING_DECISION_TEMPLATE.md` |
| `WFL-REQ-057` | Final reconciliation directive §2 | Every Task and Workflow Instance has stable semantic identity: `task_id` and `workflow_instance_id`. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-058` | Final reconciliation directive §2 | Every canonical/resolved Stage and every declared Transition is independently addressable by stable `stage_id` / `transition_id` (or explicitly deterministic equivalent). | `WORKFLOW_CONTRACT_STANDARD.md`, `WORKFLOW_STATE_MODEL.md`, `workflows/*.md`, `profiles/*.md` |
| `WFL-REQ-059` | Final reconciliation directive §3 | Retry, Rework, Recovery, Reclassification, Rerouting and Escalation are distinct orchestration concepts and MUST NOT be conflated. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-060` | Final reconciliation directive §4 | Retry and rework are both bounded; non-convergence/exhaustion requires a controlled transition rather than an infinite loop. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-061` | Final reconciliation directive §5 | Workflow failure taxonomy includes transient execution, contract, missing truth, canonical conflict, authority conflict, scope expansion, risk discovery, gate rejection, security veto, human decision, dependency, persistent provider/tool, and non-convergent rework categories with allowed orchestration responses. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-062` | Final reconciliation directive §6 | Workflow Catalog is a conformance/discovery index with stable identity, purpose, lifecycle, compatibility, required Role/Skill refs, dependencies/conflicts, supersession/replacement and contract references. | `WORKFLOW_CATALOG.md` |
| `WFL-REQ-063` | Final reconciliation directive §1 | Every canonical Workflow Profile explicitly declares all required Profile Standard fields, including `Dependencies` and `Conflicts`; absence is not equivalent to `none`. | `WORKFLOW_PROFILE_STANDARD.md`, `profiles/*.md` |
| `WFL-REQ-064` | Final reconciliation directive §2/8 | Workflow semantic identities are exposed for future observability/provenance without defining UPOS-008 event/trace semantics. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`, `WORKFLOW_STATE_MODEL.md`, `CROSS_MODULE_INTERFACES.md` |

## Coverage statement

`UNMAPPED MODULE-04 SOURCE REQUIREMENTS = 0` means all Workflow-owned requirements identified from the frozen source, implementation directive, and final reconciliation directive are mapped or explicitly deferred.

It does not claim downstream modules are already implemented.

===== END VIRTUAL FILE: MODULE_04_TRACEABILITY.md =====


---

## VIRTUAL FILE 18/44 — `VIRTUAL_REPOSITORY_TREE.md`

**Virtual path:** `VIRTUAL_REPOSITORY_TREE.md`  
**Content checksum:** `253f4601e9be`

===== BEGIN VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

# UPOS-004 Virtual Repository Tree

```text
04_workflow_engine/
├── README.md
├── WORKFLOW_OPERATING_MODEL.md
├── CHANGE_CLASSIFICATION_STANDARD.md
├── WORK_TYPE_AND_CONCERN_MODEL.md
├── WORKFLOW_PROFILE_STANDARD.md
├── WORKFLOW_CONTRACT_STANDARD.md
├── ROUTING_STANDARD.md
├── TASK_AND_WORKFLOW_INSTANCE_MODEL.md
├── WORKFLOW_STATE_MODEL.md
├── RECLASSIFICATION_AND_REROUTING.md
├── FAILURE_RETRY_RECOVERY.md
├── PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md
├── WORKFLOW_LIFECYCLE_AND_VERSIONING.md
├── WORKFLOW_CATALOG.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_04_DEFINITION_OF_DONE.md
├── MODULE_04_TRACEABILITY.md
├── workflows/
│   ├── generic-change.md
│   ├── bug-fix.md
│   ├── feature.md
│   ├── refactor.md
│   ├── dependency-upgrade.md
│   ├── documentation-change.md
│   ├── hotfix.md
│   ├── release.md
├── profiles/
│   ├── ui.md
│   ├── design-system.md
│   ├── architecture.md
│   ├── api.md
│   ├── database-migration.md
│   ├── security.md
│   ├── documentation-impact.md
├── templates/
│   ├── WORKFLOW_CONTRACT_TEMPLATE.md
│   └── ROUTING_DECISION_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_04_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── WORKFLOW_MODEL_DECISION.md
    ├── CLASSIFICATION_DIMENSION_AUDIT.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── TRACEABILITY_VALIDATION.md
```

===== END VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====


---

## VIRTUAL FILE 19/44 — `workflows/bug-fix.md`

**Virtual path:** `workflows/bug-fix.md`  
**Content checksum:** `163dcfcf8320`

===== BEGIN VIRTUAL FILE: workflows/bug-fix.md =====

# Workflow — bug-fix

**ID:** WFL-BUG-FIX  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-BUG-FIX`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `BUG_FIX`

## Purpose

Orchestrate diagnosis and correction of an observed behavior defect.

## Applicability

**Allowed / required Change Classes:** C1–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- bug/symptom described
- expected behavior source can be resolved or gap is escalated
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Merge Controller

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-CLASSIFY-CHANGE`
- `SKL-REPRODUCE-BUG`
- `SKL-WRITE-REGRESSION-TEST`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-ASSESS-MERGE-READINESS`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-BUG-FIX:REPRODUCE` | Implementer or QA | `SKL-REPRODUCE-BUG` | reproduction/non-reproduction evidence exists |
| `WFL-BUG-FIX:REGRESSION_TEST` | Implementer | `SKL-WRITE-REGRESSION-TEST` | focused test exists or omission is justified |
| `WFL-BUG-FIX:PLAN` | Implementer | `SKL-CREATE-IMPLEMENTATION-PLAN` | bounded fix plan exists |
| `WFL-BUG-FIX:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | fix produced |
| `WFL-BUG-FIX:REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | external review result available |
| `WFL-BUG-FIX:QA` | QA | `SKL-QA-VALIDATION` | external QA result available |
| `WFL-BUG-FIX:DOCS` | Documentation Guardian if behavior contract changed | `SKL-RECONCILE-DOCUMENTATION` | docs reconciled or N/A |
| `WFL-BUG-FIX:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | readiness assessment available |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-BUG-FIX:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-BUG-FIX:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-BUG-FIX:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-BUG-FIX:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-BUG-FIX:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-BUG-FIX:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Defect correction satisfies required external gates and readiness.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/bug-fix.md =====


---

## VIRTUAL FILE 20/44 — `workflows/dependency-upgrade.md`

**Virtual path:** `workflows/dependency-upgrade.md`  
**Content checksum:** `d9b876a8d804`

===== BEGIN VIRTUAL FILE: workflows/dependency-upgrade.md =====

# Workflow — dependency-upgrade

**ID:** WFL-DEPENDENCY-UPGRADE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-DEPENDENCY-UPGRADE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `DEPENDENCY_UPGRADE`

## Purpose

Orchestrate dependency version/interface change with explicit compatibility and regression consideration.

## Applicability

**Allowed / required Change Classes:** C1–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- dependency/current-target version identified
- change source/changelog or equivalent evidence available where possible
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Security when relevant
- Merge Controller

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-ANALYZE-IMPACT`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-REVIEW-SECURITY (conditional)`
- `SKL-ASSESS-MERGE-READINESS`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-DEPENDENCY-UPGRADE:ANALYZE` | Implementer/Architecture/Security as relevant | `SKL-ANALYZE-IMPACT` | breaking/security implications identified |
| `WFL-DEPENDENCY-UPGRADE:PLAN` | Implementer | `SKL-CREATE-IMPLEMENTATION-PLAN` | upgrade plan exists |
| `WFL-DEPENDENCY-UPGRADE:UPGRADE` | Implementer | `SKL-IMPLEMENT-CHANGE` | upgrade produced |
| `WFL-DEPENDENCY-UPGRADE:REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | review result available |
| `WFL-DEPENDENCY-UPGRADE:QA` | QA | `SKL-QA-VALIDATION` | regression validation available |
| `WFL-DEPENDENCY-UPGRADE:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | readiness assessment available |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-DEPENDENCY-UPGRADE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-DEPENDENCY-UPGRADE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-DEPENDENCY-UPGRADE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-DEPENDENCY-UPGRADE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-DEPENDENCY-UPGRADE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-DEPENDENCY-UPGRADE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Upgrade compatibility, required regression/security concerns, and readiness are resolved.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/dependency-upgrade.md =====


---

## VIRTUAL FILE 21/44 — `workflows/documentation-change.md`

**Virtual path:** `workflows/documentation-change.md`  
**Content checksum:** `fb318526b027`

===== BEGIN VIRTUAL FILE: workflows/documentation-change.md =====

# Workflow — documentation-change

**ID:** WFL-DOCUMENTATION-CHANGE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-DOCUMENTATION-CHANGE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `DOCUMENTATION_CHANGE`

## Purpose

Orchestrate a documentation-primary change against canonical ownership without unnecessary code gates.

## Applicability

**Allowed / required Change Classes:** C0–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- documentation fact scope identified
- canonical documentation owner/source can be resolved
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Documentation Guardian
- Reviewer as required

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-CLASSIFY-CHANGE`
- `SKL-RECONCILE-DOCUMENTATION`
- `SKL-REVIEW-DIFF (when review required)`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-DOCUMENTATION-CHANGE:OWNERSHIP` | Documentation Guardian | `SKL-RECONCILE-DOCUMENTATION` | canonical owner/source confirmed or conflict escalated |
| `WFL-DOCUMENTATION-CHANGE:UPDATE` | Documentation Guardian or authorized Role | `SKL-RECONCILE-DOCUMENTATION` | documentation change produced |
| `WFL-DOCUMENTATION-CHANGE:VALIDATE` | Reviewer/Documentation Guardian | `SKL-REVIEW-DIFF` | link/contradiction/review result available as required |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-DOCUMENTATION-CHANGE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-DOCUMENTATION-CHANGE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-DOCUMENTATION-CHANGE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-DOCUMENTATION-CHANGE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-DOCUMENTATION-CHANGE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-DOCUMENTATION-CHANGE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Canonical documentation update is consistent; code/behavior gates are only added when generated docs or behavior is involved.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/documentation-change.md =====


---

## VIRTUAL FILE 22/44 — `workflows/feature.md`

**Virtual path:** `workflows/feature.md`  
**Content checksum:** `ef4d0abe6b32`

===== BEGIN VIRTUAL FILE: workflows/feature.md =====

# Workflow — feature

**ID:** WFL-FEATURE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-FEATURE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `FEATURE`

## Purpose

Orchestrate delivery of a new or materially changed capability.

## Applicability

**Allowed / required Change Classes:** C2–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- feature intent/scope resolvable
- relevant Product owner/source exists
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Product
- Implementer
- Reviewer
- QA
- Documentation Guardian
- Merge Controller

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-CREATE-FEATURE-SPEC`
- `SKL-ANALYZE-IMPACT`
- `SKL-CLASSIFY-CHANGE`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-RECONCILE-DOCUMENTATION`
- `SKL-ASSESS-MERGE-READINESS`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-FEATURE:SPEC` | Product | `SKL-CREATE-FEATURE-SPEC` | feature spec candidate/approved source exists as required by governance |
| `WFL-FEATURE:IMPACT` | relevant Product/Domain/Architecture/UX/Security Roles | `SKL-ANALYZE-IMPACT` | impact analysis complete |
| `WFL-FEATURE:CLASSIFY` | Orchestrator | `SKL-CLASSIFY-CHANGE` | classification/routing confirmed |
| `WFL-FEATURE:PLAN` | Implementer/Architecture as routed | `SKL-CREATE-IMPLEMENTATION-PLAN` | plan exists |
| `WFL-FEATURE:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | implementation produced |
| `WFL-FEATURE:REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | external review result available |
| `WFL-FEATURE:QA` | QA | `SKL-QA-VALIDATION` | external QA result available |
| `WFL-FEATURE:DOCS` | Documentation Guardian | `SKL-RECONCILE-DOCUMENTATION` | docs reconciled |
| `WFL-FEATURE:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | readiness assessment available |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-FEATURE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-FEATURE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-FEATURE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-FEATURE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-FEATURE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-FEATURE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Capability implementation and all applied profiles/gates meet completion criteria.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/feature.md =====


---

## VIRTUAL FILE 23/44 — `workflows/generic-change.md`

**Virtual path:** `workflows/generic-change.md`  
**Content checksum:** `2554fe029a8e`

===== BEGIN VIRTUAL FILE: workflows/generic-change.md =====

# Workflow — generic-change

**ID:** WFL-GENERIC-CHANGE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-GENERIC-CHANGE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `GENERIC_CHANGE`

## Purpose

Orchestrate a bounded change that is not better represented by another primary Work Type.

## Applicability

**Allowed / required Change Classes:** C0–C3 by default; C4/C5 only when routing/profile/policy proves compatibility

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- Task intention is coherent
- canonical sources required for the change can be resolved or missing truth is explicitly blocked
- classification/work type/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- Merge Controller

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-CLASSIFY-CHANGE`
- `SKL-CREATE-IMPLEMENTATION-PLAN (C1+ or when needed)`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-ASSESS-MERGE-READINESS`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-GENERIC-CHANGE:ROUTE` | Orchestrator | `SKL-CLASSIFY-CHANGE` | Routing Decision exists |
| `WFL-GENERIC-CHANGE:PLAN` | Implementer or Architecture as routed | `SKL-CREATE-IMPLEMENTATION-PLAN` | Plan exists or stage skipped by C0 policy |
| `WFL-GENERIC-CHANGE:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | bounded change produced |
| `WFL-GENERIC-CHANGE:REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | external review result available |
| `WFL-GENERIC-CHANGE:VALIDATE` | QA if required by class/profile | `SKL-QA-VALIDATION` | external QA result available or stage not required |
| `WFL-GENERIC-CHANGE:DOCS` | Documentation Guardian if contract changed | `SKL-RECONCILE-DOCUMENTATION` | docs reconciled or N/A |
| `WFL-GENERIC-CHANGE:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | readiness assessment available |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-GENERIC-CHANGE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-GENERIC-CHANGE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-GENERIC-CHANGE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-GENERIC-CHANGE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-GENERIC-CHANGE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-GENERIC-CHANGE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

All required stages/profiles/external gates satisfied and Workflow Result can be COMPLETED.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/generic-change.md =====


---

## VIRTUAL FILE 24/44 — `workflows/hotfix.md`

**Virtual path:** `workflows/hotfix.md`  
**Content checksum:** `7210d3f70961`

===== BEGIN VIRTUAL FILE: workflows/hotfix.md =====

# Workflow — hotfix

**ID:** WFL-HOTFIX  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-HOTFIX`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `HOTFIX`

## Purpose

Orchestrate expedited recovery without treating urgency as permission to skip safety.

## Applicability

**Allowed / required Change Classes:** C1–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- active incident/urgent regression established
- minimal recovery intention defined
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Merge Controller
- Human approval reference as externally required

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-ANALYZE-INCIDENT`
- `SKL-REPRODUCE-BUG (where possible)`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-PREPARE-RELEASE`
- `SKL-ASSESS-MERGE-READINESS`
- `SKL-CAPTURE-LEARNING (follow-up candidate)`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-HOTFIX:INCIDENT_CONTEXT` | relevant incident Role | `SKL-ANALYZE-INCIDENT` | incident scope/evidence established |
| `WFL-HOTFIX:MINIMAL_PLAN` | Implementer | `SKL-CREATE-IMPLEMENTATION-PLAN` | minimal safe fix plan exists |
| `WFL-HOTFIX:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | minimal fix produced |
| `WFL-HOTFIX:EXPEDITED_REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | independent review result available |
| `WFL-HOTFIX:FOCUSED_QA` | QA | `SKL-QA-VALIDATION` | focused validation available |
| `WFL-HOTFIX:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | required approval/readiness references resolved |
| `WFL-HOTFIX:RELEASE_PREP` | DevOps/SRE or release role | `SKL-PREPARE-RELEASE` | release preparation complete if applicable |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-HOTFIX:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-HOTFIX:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-HOTFIX:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-HOTFIX:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-HOTFIX:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-HOTFIX:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Recovery change is safely ready/released according to external policy; follow-up debt/learning may be emitted separately.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/hotfix.md =====


---

## VIRTUAL FILE 25/44 — `workflows/refactor.md`

**Virtual path:** `workflows/refactor.md`  
**Content checksum:** `79148e1c4686`

===== BEGIN VIRTUAL FILE: workflows/refactor.md =====

# Workflow — refactor

**ID:** WFL-REFACTOR  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-REFACTOR`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `REFACTOR`

## Purpose

Orchestrate structural implementation change intended to preserve externally intended behavior.

## Applicability

**Allowed / required Change Classes:** C1–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- refactor reason/scope explicit
- preserved behavior contract identifiable
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Merge Controller

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-ANALYZE-IMPACT`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-IMPLEMENT-CHANGE`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-ASSESS-MERGE-READINESS`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-REFACTOR:PRESERVATION_BASELINE` | Implementer/Reviewer | `SKL-ANALYZE-IMPACT` | behavior/contracts to preserve explicit |
| `WFL-REFACTOR:PLAN` | Implementer | `SKL-CREATE-IMPLEMENTATION-PLAN` | refactor plan exists |
| `WFL-REFACTOR:IMPLEMENT` | Implementer | `SKL-IMPLEMENT-CHANGE` | refactor produced |
| `WFL-REFACTOR:REVIEW` | Reviewer | `SKL-REVIEW-DIFF` | external review result available |
| `WFL-REFACTOR:QA` | QA when required | `SKL-QA-VALIDATION` | preservation validation available |
| `WFL-REFACTOR:READINESS` | Merge Controller | `SKL-ASSESS-MERGE-READINESS` | readiness assessment available |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-REFACTOR:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-REFACTOR:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-REFACTOR:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-REFACTOR:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-REFACTOR:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-REFACTOR:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Preserved behavior is externally validated as required and no unapproved feature scope was introduced.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/refactor.md =====


---

## VIRTUAL FILE 26/44 — `workflows/release.md`

**Virtual path:** `workflows/release.md`  
**Content checksum:** `888cb8bd7472`

===== BEGIN VIRTUAL FILE: workflows/release.md =====

# Workflow — release

**ID:** WFL-RELEASE  
**Type:** WORKFLOW DEFINITION  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_CONTRACT_STANDARD.md


**workflow_id:** `WFL-RELEASE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**work_type:** `RELEASE`

## Purpose

Orchestrate release of a selected release candidate through required external operational/security/human checkpoints.

## Applicability

**Allowed / required Change Classes:** C2–C5

Compatible Concern Profiles are resolved by routing. No concern profile is implied merely by this base Workflow.

## Entry Conditions

- release candidate identified
- required release/operations sources resolvable
- classification/concerns resolved

## Required Source Classes

Resolved by the task's affected scopes through UPOS-01/05 interfaces. This Workflow does not hard-code physical paths.

## Context Interface Requirements

Each stage receives minimal sufficient authoritative context appropriate to its Role/Skill references. Retrieval semantics remain UPOS-005.

## Roles

- Orchestrator
- DevOps / SRE or project release specialist
- QA
- Security when relevant
- Human approval reference
- Documentation Guardian as relevant

Role authority/SoD remain UPOS-002.

## Separation-of-Duties Constraints

```text
Implementer != Final Reviewer
```

For high-risk routes:

```text
Implementer != Reviewer != Merge Controller
```

Additional profile/policy constraints may tighten these.

## Skills

- `SKL-PREPARE-RELEASE`
- `SKL-QA-VALIDATION`
- `SKL-REVIEW-SECURITY (conditional)`
- `SKL-RECONCILE-DOCUMENTATION (conditional)`

Skill procedures remain UPOS-003.

## Stages

| stage_id | Primary Role reference | Skill / external interface reference | Stage exit condition |
|---|---|---|---|
| `WFL-RELEASE:PREPARE` | release specialist | `SKL-PREPARE-RELEASE` | release package/readiness gaps identified |
| `WFL-RELEASE:EXTERNAL_GATES` | relevant Roles | `referenced external quality/security/operations interfaces` | required external gate results available |
| `WFL-RELEASE:HUMAN_CHECKPOINT` | Human authority by reference | `no Skill; approval interface` | required human approval exists |
| `WFL-RELEASE:DEPLOYMENT` | authorized operational Role | `external protected-action/tool interface` | deployment outcome available |
| `WFL-RELEASE:VERIFY` | QA/operations | `SKL-QA-VALIDATION` | post-release verification available |
| `WFL-RELEASE:ROLLBACK_OR_COMPLETE` | operations/orchestrator | `external rollback/recovery interface if needed` | terminal release result reached |

## Stage Dependencies

Stages are serial in listed order unless a resolved profile/dependency graph explicitly marks independent stages parallelizable.

## Transitions

| transition_id | Rule |
|---|---|
| `WFL-RELEASE:TR-NORMAL-NEXT` | normal stage completion → next READY stage |
| `WFL-RELEASE:TR-GATE-REWORK` | external gate rejection/failure → `REWORK_REQUIRED` or `BLOCKED` according to resolved policy |
| `WFL-RELEASE:TR-RISK-RECLASSIFY` | material new risk → `PAUSED`/`BLOCKED` → reclassification |
| `WFL-RELEASE:TR-FAIL` | unrecoverable failure → `FAILED` |
| `WFL-RELEASE:TR-CANCEL` | authorized cancellation → `CANCELLED` |
| `WFL-RELEASE:TR-COMPLETE` | successful final required stage → `COMPLETED` |

These are stable transition-rule identities. Concrete transition occurrence/event identity is outside Module 04.

## Handoffs

Handoff references use UPOS-002 Handoff semantics. This contract does not duplicate handoff payload/authority rules.

## External Gate References

Review, QA, architecture, security, documentation, readiness, CI, release, or other gates are included only when required by Change Class/profiles/external policy. Their verdict semantics remain external.

## Human Approval References

Required according to resolved Change Class/profile and external Human/Security policy.

## Security / Permission References

Protected actions require UPOS-010 permission/approval interfaces. This Workflow grants nothing.

## Reclassification Triggers

Any trigger defined by `RECLASSIFICATION_AND_REROUTING.md` plus profile-specific triggers.

## Rerouting Rules

A material Work Type/Concern/Class change requires an updated Routing Decision. Old route provenance is retained.

## Failure Modes

- required source unavailable/conflicted;
- required Role/Skill/gate unavailable;
- stage output incompatible with downstream entry condition;
- classification/profile becomes stale;
- SoD cannot be satisfied.

## Retry Rules

Bounded only. Exact retry budgets are resolved by Workflow/project policy. No infinite loops.

## Recovery Rules

Use `FAILURE_RETRY_RECOVERY.md`: rework, re-plan, reclassify, reroute, split, rollback reference, pause, escalation, abort.

## Rework Loops

Gate/findings may route back only to a stage responsible for producing the affected artifact. Reviewer/QA independence must remain intact.

## Pause / Block / Resume

Defined by `WORKFLOW_STATE_MODEL.md`.

## Escalation

Escalate unresolved authority/source/profile/risk conflicts. Workflow does not invent specialist truth.

## Cancellation

Cancellation must preserve partial-output provenance and avoid treating unfinished artifacts as canonical.

## Completion Criteria

Release candidate reaches completed/rolled-back terminal outcome with required verification and approvals.

## Terminal Outcomes

`COMPLETED | FAILED | CANCELLED | ESCALATED_TERMINAL | SUPERSEDED_BY_REROUTE`

## Observability Interface Requirements

Future observability should correlate Workflow ID/version, Task, Routing Decision, profiles, stages, Role Runs, Skill invocations, gates and terminal result. Event semantics remain UPOS-008.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

## Version

`1.0.0`

## Supersession

None in v1.0.

===== END VIRTUAL FILE: workflows/release.md =====


---

## VIRTUAL FILE 27/44 — `profiles/api.md`

**Virtual path:** `profiles/api.md`  
**Content checksum:** `0ab9c769f354`

===== BEGIN VIRTUAL FILE: profiles/api.md =====

# Workflow Profile — API

**ID:** WFP-API  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-API`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `API`

## Purpose

Apply `API`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

No universal class floor. Breaking external compatibility materially increases risk and may require C3/C4+ depending breadth/ownership.

## Added / Required Role references

- Architecture
- Domain when semantics affected
- Implementer
- Reviewer
- QA
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-ARCHITECTURE (conditional)`
- `SKL-QA-VALIDATION`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-API:CONTRACT-IMPACT-CHECKPOINT` — contract impact checkpoint
- `stage_id: WFP-API:BACKWARD-COMPATIBILITY-VERSIONING-CHECKPOINT` — backward-compatibility/versioning checkpoint
- `stage_id: WFP-API:CONTRACT-INTEGRATION-VALIDATION-CHECKPOINT` — contract/integration validation checkpoint
- `stage_id: WFP-API:CONSUMER-DOCUMENTATION-CHECKPOINT` — consumer/documentation checkpoint

## External gate references

- contract-test/integration evidence reference where defined externally

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- breaking consumer contract discovered
- versioning/compatibility assumption invalidated

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/api.md =====


---

## VIRTUAL FILE 28/44 — `profiles/architecture.md`

**Virtual path:** `profiles/architecture.md`  
**Content checksum:** `ff505b917e17`

===== BEGIN VIRTUAL FILE: profiles/architecture.md =====

# Workflow Profile — ARCHITECTURE

**ID:** WFP-ARCHITECTURE  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-ARCHITECTURE`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `ARCHITECTURE`

## Purpose

Apply `ARCHITECTURE`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX

## Dependencies

none

## Conflicts

none

## Risk implications

Durable architecture boundary/ownership/topology change requires C4 minimum. High-risk security/production effects may drive C5.

## Added / Required Role references

- Architecture
- relevant Product/Domain/Security Roles
- Reviewer
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-CREATE-RFC`
- `SKL-REVIEW-ARCHITECTURE`
- `SKL-CREATE-ADR`
- `SKL-ANALYZE-IMPACT`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-ARCHITECTURE:RFC-ALTERNATIVES-CHECKPOINT-FOR-DURABLE` — RFC/alternatives checkpoint for durable architectural decision
- `stage_id: WFP-ARCHITECTURE:ARCHITECTURE-REVIEW` — Architecture review
- `stage_id: WFP-ARCHITECTURE:HUMAN-DECISION-APPROVAL-REFERENCE-WHERE` — human decision/approval reference where required
- `stage_id: WFP-ARCHITECTURE:ADR-AFTER-VALID-DECISION-AUTHORITY` — ADR after valid decision authority
- `stage_id: WFP-ARCHITECTURE:MIGRATION-IMPLEMENTATION-PLANNING-CHECKPOINT` — migration/implementation planning checkpoint

## External gate references

- Architecture review reference
- human approval reference for C4+ according to policy
- documentation reconciliation

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- new service/storage owner/routing/multitenancy/eventing boundary
- hidden durable decision found during implementation

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/architecture.md =====


---

## VIRTUAL FILE 29/44 — `profiles/database-migration.md`

**Virtual path:** `profiles/database-migration.md`  
**Content checksum:** `0ea2ced46a43`

===== BEGIN VIRTUAL FILE: profiles/database-migration.md =====

# Workflow Profile — DATABASE_MIGRATION

**ID:** WFP-DATABASE-MIGRATION  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DATABASE-MIGRATION`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DATABASE_MIGRATION`

## Purpose

Apply `DATABASE_MIGRATION`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

Migration concern normally increases process depth. Destructive/production/irreversible data migration is C5.

## Added / Required Role references

- Architecture
- Domain
- Database/DevOps specialist where project defines it
- Implementer
- QA
- Security when relevant

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-CREATE-IMPLEMENTATION-PLAN`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DATABASE-MIGRATION:DATA-IMPACT-CHECKPOINT` — data-impact checkpoint
- `stage_id: WFP-DATABASE-MIGRATION:MIGRATION-COMPATIBILITY-PLAN` — migration/compatibility plan
- `stage_id: WFP-DATABASE-MIGRATION:BACKUP-RECOVERY-STRATEGY-REFERENCE` — backup/recovery strategy reference
- `stage_id: WFP-DATABASE-MIGRATION:MIGRATION-IMPLEMENTATION-STAGE-BY-EXTERNAL` — migration implementation stage by external engineering mechanics
- `stage_id: WFP-DATABASE-MIGRATION:VERIFICATION` — verification
- `stage_id: WFP-DATABASE-MIGRATION:ROLLBACK-FORWARD-FIX-CHECKPOINT` — rollback/forward-fix checkpoint

## External gate references

- backup/recovery evidence reference
- migration verification reference
- human approval reference according to class

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- destructive data operation
- production migration
- irreversible transformation
- unexpected compatibility/data-loss risk

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/database-migration.md =====


---

## VIRTUAL FILE 30/44 — `profiles/design-system.md`

**Virtual path:** `profiles/design-system.md`  
**Content checksum:** `7e2b670b1c06`

===== BEGIN VIRTUAL FILE: profiles/design-system.md =====

# Workflow Profile — DESIGN_SYSTEM

**ID:** WFP-DESIGN-SYSTEM  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DESIGN-SYSTEM`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DESIGN_SYSTEM`

## Purpose

Apply `DESIGN_SYSTEM`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR

## Dependencies

none

## Conflicts

none

## Risk implications

No automatic class floor. Large shared migration may drive C3; durable architecture/security impacts classify separately.

## Added / Required Role references

- Design System
- UX
- Reviewer
- QA
- Documentation Guardian

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`
- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DESIGN-SYSTEM:REGISTRY-REUSE-EXTEND-CREATE-DECISION` — registry/reuse-extend-create decision checkpoint by Design System owner
- `stage_id: WFP-DESIGN-SYSTEM:COMPONENT-PATTERN-CONTRACT-CHECKPOINT` — component/pattern contract checkpoint
- `stage_id: WFP-DESIGN-SYSTEM:VISUAL-QA-DOCUMENTATION-DEPRECATION-CHECKPOINT` — visual QA/documentation/deprecation checkpoint

## External gate references

- Design System review reference
- visual/accessibility evidence reference where required

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- shared component migration expands breadth
- new reusable primitive/pattern affects multiple surfaces

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/design-system.md =====


---

## VIRTUAL FILE 31/44 — `profiles/documentation-impact.md`

**Virtual path:** `profiles/documentation-impact.md`  
**Content checksum:** `f04f067045c6`

===== BEGIN VIRTUAL FILE: profiles/documentation-impact.md =====

# Workflow Profile — DOCUMENTATION_IMPACT

**ID:** WFP-DOCUMENTATION-IMPACT  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-DOCUMENTATION-IMPACT`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `DOCUMENTATION_IMPACT`

## Purpose

Apply `DOCUMENTATION_IMPACT`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

all base workflows

## Dependencies

none

## Conflicts

none

## Risk implications

Does not independently raise Change Class; documents the fact that durable contract/documentation reconciliation is required.

## Added / Required Role references

- Documentation Guardian
- affected canonical owner Role

Role authority remains UPOS-002.

## Skill references

- `SKL-RECONCILE-DOCUMENTATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-DOCUMENTATION-IMPACT:DOCUMENTATION-IMPACT-CHECKPOINT` — documentation impact checkpoint
- `stage_id: WFP-DOCUMENTATION-IMPACT:CANONICAL-OWNER-SOURCE-RECONCILIATION` — canonical owner/source reconciliation
- `stage_id: WFP-DOCUMENTATION-IMPACT:DOCUMENTATION-UPDATE-REVIEW-BEFORE-COMPLETION` — documentation update/review before completion as required

## External gate references

- documentation consistency/reference gate as defined by UPOS-01/07

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- implementation changes a documented contract
- decision/spec/source is superseded or becomes stale

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/documentation-impact.md =====


---

## VIRTUAL FILE 32/44 — `profiles/security.md`

**Virtual path:** `profiles/security.md`  
**Content checksum:** `bcd6cad07374`

===== BEGIN VIRTUAL FILE: profiles/security.md =====

# Workflow Profile — SECURITY

**ID:** WFP-SECURITY  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-SECURITY`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `SECURITY`

## Purpose

Apply `SECURITY`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, DEPENDENCY_UPGRADE, HOTFIX, RELEASE

## Dependencies

none

## Conflicts

none

## Risk implications

Auth/authz/security-boundary/privacy/secrets/protected-action changes are C5 signals. Other security-relevant changes are classified by actual impact.

## Added / Required Role references

- Security
- relevant Architecture/Domain/Product Roles
- Reviewer
- QA

Role authority remains UPOS-002.

## Skill references

- `SKL-REVIEW-SECURITY`
- `SKL-ANALYZE-IMPACT`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-SECURITY:SECURITY-THREAT-IMPACT-CHECKPOINT` — security/threat-impact checkpoint
- `stage_id: WFP-SECURITY:SECURITY-DESIGN-CONSTRAINT-CHECKPOINT-IF` — security design/constraint checkpoint if needed
- `stage_id: WFP-SECURITY:SECURITY-REVIEW-STAGE` — security review stage
- `stage_id: WFP-SECURITY:HUMAN-SECURITY-APPROVAL-REFERENCE-WHERE` — human/security approval reference where required
- `stage_id: WFP-SECURITY:AUDIT-EVIDENCE-REFERENCE-CHECKPOINT` — audit/evidence reference checkpoint

## External gate references

- Security review/veto interface reference
- human approval reference for protected/high-risk action

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- new auth/authz path
- security boundary change
- secret/privacy/retention impact
- protected action discovered

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/security.md =====


---

## VIRTUAL FILE 33/44 — `profiles/ui.md`

**Virtual path:** `profiles/ui.md`  
**Content checksum:** `f67b184fbeb5`

===== BEGIN VIRTUAL FILE: profiles/ui.md =====

# Workflow Profile — UI

**ID:** WFP-UI  
**Type:** WORKFLOW PROFILE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** WORKFLOW_PROFILE_STANDARD.md


**profile_id:** `WFP-UI`  
**version:** `1.0.0`  
**status:** `ACTIVE`  
**concern:** `UI`

## Purpose

Apply `UI`-specific orchestration requirements to a compatible Base Workflow without creating a competing primary Workflow.

## Compatible Work Types

GENERIC_CHANGE, BUG_FIX, FEATURE, REFACTOR, HOTFIX

## Dependencies

none

## Conflicts

none

## Risk implications

No automatic class floor. Material user-facing/Product/Accessibility impact may raise classification.

## Added / Required Role references

- UX
- Design System when reusable components/patterns affected
- QA
- Reviewer

Role authority remains UPOS-002.

## Skill references

- `SKL-ANALYZE-IMPACT`
- `SKL-REVIEW-DIFF`
- `SKL-QA-VALIDATION`

Skill procedures remain UPOS-003.

## Added / Modified orchestration checkpoints

- `stage_id: WFP-UI:UX-INTENT-IMPACT-CHECKPOINT-BEFORE` — UX intent/impact checkpoint before implementation when behavior/flow changes
- `stage_id: WFP-UI:VISUAL-ACCESSIBILITY-EXTERNAL-EVIDENCE-CHECKPOINT` — visual/accessibility external evidence checkpoint after implementation
- `stage_id: WFP-UI:UI-FOCUSED-QA-PARTICIPATION` — UI-focused QA participation

## External gate references

- visual evidence reference as defined by Quality/Design tooling
- accessibility gate when externally required

Gate/verdict semantics remain with their external owners.

## Reclassification triggers

- unexpected domain/product behavior change
- Design System primitive/pattern change discovered

## Composition

This Profile may compose with other profiles when `WORKFLOW_PROFILE_STANDARD.md` compatibility rules are satisfied.

## Prohibited behavior

- redefining base Work Type;
- lowering mandatory Change Class protections;
- granting authority/permissions;
- copying Skill procedure;
- redefining external gate semantics;
- hard-coding provider/project paths.

## Lifecycle / Version

`ACTIVE / 1.0.0`

Definition lifecycle follows `WORKFLOW_LIFECYCLE_AND_VERSIONING.md`.

## Supersession

None in v1.0.

===== END VIRTUAL FILE: profiles/ui.md =====


---

## VIRTUAL FILE 34/44 — `templates/ROUTING_DECISION_TEMPLATE.md`

**Virtual path:** `templates/ROUTING_DECISION_TEMPLATE.md`  
**Content checksum:** `6c2095ff6738`

===== BEGIN VIRTUAL FILE: templates/ROUTING_DECISION_TEMPLATE.md =====

# Routing Decision Template

**ID:** UPOS-04-TPL-002  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Routing Decision

Routing Decision ID:
Task ID:
Work Type:
Change Class:
Classification rationale:

Concerns:
Base Workflow:
Base Workflow Version:
Profiles:

Required Roles:
Required Skills:
SoD Constraints:

External Gates:
Approval References:

Source / Context References:
Reclassification Triggers:

Open Conflicts / Unknowns:

Routing Result:
ROUTED / BLOCKED_ROUTING / RECLASSIFICATION_REQUIRED
```

===== END VIRTUAL FILE: templates/ROUTING_DECISION_TEMPLATE.md =====


---

## VIRTUAL FILE 35/44 — `templates/WORKFLOW_CONTRACT_TEMPLATE.md`

**Virtual path:** `templates/WORKFLOW_CONTRACT_TEMPLATE.md`  
**Content checksum:** `fdd2555a2402`

===== BEGIN VIRTUAL FILE: templates/WORKFLOW_CONTRACT_TEMPLATE.md =====

# Workflow Contract Template

**ID:** UPOS-04-TPL-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Workflow — <name>

**ID:** <workflow id>
**Type:** WORKFLOW DEFINITION
**Status:** <DRAFT|REVIEW|APPROVED|ACTIVE|DEPRECATED|RETIRED>
**Normativity:** NORMATIVE
**Owner:** UPOS-004 Workflow Engine
**Version:** <semver>

## Purpose
## Applicability
## Work Types
## Allowed / Required Change Classes
## Concern Compatibility
## Entry Conditions
## Required Source Classes
## Context Interface Requirements
## Roles
## Role Participation
## Separation-of-Duties Constraints
## Skills
## Stages
## Stage Dependencies
## Transitions
## Handoffs
## External Gate References
## Human Approval References
## Security / Permission References
## Reclassification Triggers
## Rerouting Rules
## Failure Modes
## Retry Rules
## Recovery Rules
## Rework Loops
## Pause / Block / Resume
## Escalation
## Cancellation
## Completion Criteria
## Terminal Outcomes
## Observability Interface Requirements
## Lifecycle
## Version
## Supersession
```

===== END VIRTUAL FILE: templates/WORKFLOW_CONTRACT_TEMPLATE.md =====


---

## VIRTUAL FILE 36/44 — `analysis/AMBIGUITY_GAP_REGISTER.md`

**Virtual path:** `analysis/AMBIGUITY_GAP_REGISTER.md`  
**Content checksum:** `5bae68dc0c22`

===== BEGIN VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

# UPOS-004 Ambiguity & Gap Register

**ID:** UPOS-04-AN-006  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


| ID | Issue | Module-04 resolution | Deferred owner | Status |
|---|---|---|---|---|
| G04-001 | UI/API/DB/Security workflow overlap | Normalize as Concern Profiles, not competing base workflows. | — | CLOSED |
| G04-002 | Micro change as work type vs class | Micro is C0 classification depth; primary Work Type defaults to GENERIC_CHANGE. | — | CLOSED |
| G04-003 | Architecture as workflow vs concern | Architecture becomes a Concern Profile; durable architecture change imposes C4 minimum. | UPOS-002/01 for authority/decision | CLOSED |
| G04-004 | Skill procedure duplication | Workflow references stable Skill IDs/versions only. | UPOS-003 | CLOSED |
| G04-005 | Gate semantics leakage | Workflow says when gate is required; UPOS-007 defines evidence/verdict meaning. | UPOS-007 | CLOSED |
| G04-006 | Human approval semantics | Workflow requires approval reference; authority/enforcement external. | UPOS-002/010 | CLOSED |
| G04-007 | Context ownership | Workflow declares Source Classes/context need; retrieval/budget/memory external. | UPOS-005/01 | CLOSED |
| G04-008 | Git/merge mechanics | Workflow may include readiness/merge/release stage references but Git mechanics remain external. | UPOS-006 | CLOSED |
| G04-009 | Retry threshold | Universal rule is bounded retry; exact numeric budgets project-specific. | UPOS-011/project policy | CLOSED |
| G04-010 | Task lifecycle source too code-centric | Normalize universal Task states; review/QA/readiness become stage projections. | — | CLOSED |
| G04-011 | Workflow Instance vs telemetry runtime | Module 04 owns semantic attribution/state; persistence/events external. | UPOS-008/runtime/schemas | CLOSED |
| G04-012 | Parallelism vs shared-file collisions | Workflow owns dependency/parallel orchestration; collision/worktree mechanics external. | UPOS-006 | CLOSED |
| G04-013 | Security classification meaning | UPOS-004 consumes Security sensitivity signal; does not redefine security truth. | UPOS-010 | CLOSED |
| G04-014 | Release deploy stage without deploy Skill | Workflow may orchestrate external protected operational action by interface; tool/permission binding external. | UPOS-010/011 | CLOSED |

## Result

No unresolved P0/P1 Module-04 semantic gap remains at v1.0 freeze.

===== END VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====


---

## VIRTUAL FILE 37/44 — `analysis/CLASSIFICATION_DIMENSION_AUDIT.md`

**Virtual path:** `analysis/CLASSIFICATION_DIMENSION_AUDIT.md`  
**Content checksum:** `242f2ad6d813`

===== BEGIN VIRTUAL FILE: analysis/CLASSIFICATION_DIMENSION_AUDIT.md =====

# Classification Dimension Audit

**ID:** UPOS-04-AN-005  
**Type:** ANALYSIS / CLASSIFICATION AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../CHANGE_CLASSIFICATION_STANDARD.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


| Dimension | Provenance | Source support / rationale |
|---|---|---|
| product semantics impact | TASK_DIRECTIVE_REFINEMENT | C2 feature / Product routing implies relevance but source does not name dimension explicitly |
| domain semantics impact | TASK_DIRECTIVE_REFINEMENT | C3 multiple bounded contexts + Domain ownership |
| architecture impact | SOURCE_DERIVED | C4 definition/examples |
| cross-module breadth | SOURCE_DERIVED | C3 examples |
| data/model migration impact | SOURCE_DERIVED | DB migration + destructive/prod data C5 |
| security/privacy impact | SOURCE_DERIVED | C5 examples + Security workflow |
| authorization impact | SOURCE_DERIVED | auth/authz C5 examples |
| production blast radius | TASK_DIRECTIVE_REFINEMENT | production migration/hotfix/release source support |
| irreversibility | SOURCE_DERIVED | destructive data / irreversible AI action |
| external API compatibility | SOURCE_DERIVED | API workflow backward compatibility/versioning |
| user-facing behavior impact | TASK_DIRECTIVE_REFINEMENT | feature/UI workflows imply participation depth |
| operational impact | SOURCE_DERIVED | hotfix/release workflows |
| deployment complexity | TASK_DIRECTIVE_REFINEMENT | migration/release orchestration |
| uncertainty / missing truth | SOURCE_DERIVED | missing/stale Source-of-Truth + reclassification rules |

No `NEW_PROPOSAL` dimension was required for v1.

===== END VIRTUAL FILE: analysis/CLASSIFICATION_DIMENSION_AUDIT.md =====


---

## VIRTUAL FILE 38/44 — `analysis/IMPLEMENTATION_PLAN.md`

**Virtual path:** `analysis/IMPLEMENTATION_PLAN.md`  
**Content checksum:** `ec6fe650f9ad`

===== BEGIN VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

# UPOS-004 Implementation Plan

**ID:** UPOS-04-AN-008  
**Type:** IMPLEMENTATION PLAN / EVIDENCE  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Sequence

1. freeze Module 04 scope/non-scope;
2. audit C0–C5 and routing semantics;
3. resolve three-axis Work Type/Concern/Class model;
4. define Workflow/Profile contracts;
5. define state/transition/reclassification/retry semantics;
6. define base Workflow catalog;
7. convert orthogonal frozen workflows to Concern Profiles;
8. define cross-module interfaces/templates;
9. complete source disposition/traceability;
10. validate zero ownership leakage.

## Recommended logical commits

```text
docs(upos-004): establish workflow engine boundary
docs(upos-004): define change classification and routing model
docs(upos-004): define workflow and profile contracts
docs(upos-004): define workflow state and reclassification semantics
docs(upos-004): define failure retry recovery and dependency orchestration
docs(upos-004): add canonical base workflows
docs(upos-004): add concern profiles
docs(upos-004): add templates and cross-module interfaces
docs(upos-004): complete source traceability audit
```

One commit = one coherent logical change.

## Non-scope

No runtime provider, Git engine, Quality engine, Security engine, Context engine, telemetry store/dashboard, schema implementation, or project adapter implementation.

===== END VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====


---

## VIRTUAL FILE 39/44 — `analysis/MODULE_04_OWNERSHIP_MAP.md`

**Virtual path:** `analysis/MODULE_04_OWNERSHIP_MAP.md`  
**Content checksum:** `16025e8606b8`

===== BEGIN VIRTUAL FILE: analysis/MODULE_04_OWNERSHIP_MAP.md =====

# Module 04 Ownership Map

**ID:** UPOS-04-AN-002  
**Type:** ANALYSIS / BOUNDARY MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Owns

Workflow/classification/routing/stage/transition/state/rework/retry/recovery/reclassification/rerouting/completion semantics and Workflow/Profile lifecycle/versioning.

## Does not own

| Concern | Owner |
|---|---|
| canonical project truth | UPOS-01 |
| Roles/authority/SoD/handoffs | UPOS-002 |
| Skill procedure/registry/evaluation | UPOS-003 |
| Context retrieval/memory | UPOS-005 |
| Git/PR/merge/worktree mechanics | UPOS-006 |
| review/QA/evidence/verdict semantics | UPOS-007 |
| telemetry/traces/metrics | UPOS-008 |
| learning detection/promotion | UPOS-009 + UPOS-01 |
| permissions/protected actions/secrets | UPOS-010 |
| project/provider/command bindings | UPOS-011 |

## Boundary test

If the central question is:

```text
When/why does this stage occur?
Which Role/Skill/gate is required?
What transition/rework/reroute is legal?
How deep is process based on risk?
```

it is Workflow-owned.

If the question is:

```text
What may this Role decide?
How does this Skill perform its method?
How is context retrieved?
What does QA PASS mean?
Who may merge/deploy?
Which Git command/provider/path is used?
```

it is not Module 04 ownership.

===== END VIRTUAL FILE: analysis/MODULE_04_OWNERSHIP_MAP.md =====


---

## VIRTUAL FILE 40/44 — `analysis/PROPOSED_PACKAGE_TREE.md`

**Virtual path:** `analysis/PROPOSED_PACKAGE_TREE.md`  
**Content checksum:** `b858a94f3367`

===== BEGIN VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

# Proposed Package Tree

**ID:** UPOS-04-AN-007  
**Type:** ANALYSIS / PACKAGE DESIGN  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


```text
04_workflow_engine/
├── README.md
├── WORKFLOW_OPERATING_MODEL.md
├── CHANGE_CLASSIFICATION_STANDARD.md
├── WORK_TYPE_AND_CONCERN_MODEL.md
├── WORKFLOW_PROFILE_STANDARD.md
├── WORKFLOW_CONTRACT_STANDARD.md
├── ROUTING_STANDARD.md
├── TASK_AND_WORKFLOW_INSTANCE_MODEL.md
├── WORKFLOW_STATE_MODEL.md
├── RECLASSIFICATION_AND_REROUTING.md
├── FAILURE_RETRY_RECOVERY.md
├── PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md
├── WORKFLOW_LIFECYCLE_AND_VERSIONING.md
├── WORKFLOW_CATALOG.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_04_DEFINITION_OF_DONE.md
├── MODULE_04_TRACEABILITY.md
├── workflows/
│   ├── generic-change.md
│   ├── bug-fix.md
│   ├── feature.md
│   ├── refactor.md
│   ├── dependency-upgrade.md
│   ├── documentation-change.md
│   ├── hotfix.md
│   ├── release.md
├── profiles/
│   ├── ui.md
│   ├── design-system.md
│   ├── architecture.md
│   ├── api.md
│   ├── database-migration.md
│   ├── security.md
│   ├── documentation-impact.md
├── templates/
│   ├── WORKFLOW_CONTRACT_TEMPLATE.md
│   └── ROUTING_DECISION_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_04_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── WORKFLOW_MODEL_DECISION.md
    ├── CLASSIFICATION_DIMENSION_AUDIT.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── TRACEABILITY_VALIDATION.md
```

===== END VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====


---

## VIRTUAL FILE 41/44 — `analysis/SOURCE_ANALYSIS.md`

**Virtual path:** `analysis/SOURCE_ANALYSIS.md`  
**Content checksum:** `8c7179ccd79b`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

# UPOS-004 Source Analysis

**ID:** UPOS-04-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../MODULE_04_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Sources

- UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle — active upstream governance.
- UPOS-002 Agent Organization v1.0 — frozen organizational contract.
- UPOS-003 Skills System v1.0 — frozen Skill contract/library.
- `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md` — frozen master design input.
- UPOS-004 implementation directive — task refinement.

## Direct Workflow-owned frozen sections

Architecture traceability assigns 46 structural units to Module 04, including:

- §3.11;
- §22–30;
- §79–80;
- §85–98;
- §122;
- §129;
- §136;
- §146;
- §185;
- §194;
- §196;
- §199;
- §202–205;
- §207;
- §221.3;
- Appendix D/J/O/P/Q;
- Final Principle 4.

## Main normalization

Frozen source models UI/DS/Architecture/API/DB/Security as named workflows.

Source analysis shows they are orthogonal concerns and can coexist.

Decision:

```text
Base Work Type Workflow
+
Concern Profiles
+
Change Class
=
Resolved Workflow Configuration
```

This preserves source intent while avoiding combinatorial explosion.

## Critical retained invariants

- risk determines process depth;
- risk != diff size;
- no every-agent swarm;
- no infinite retry;
- material scope/risk discovery triggers reclassification;
- parallelize only independent nodes;
- shared contract first;
- Workflow status != product feature lifecycle;
- explicit legal state transitions;
- Implementer != Final Reviewer;
- high-risk Implementer != Reviewer != Merge Controller.

===== END VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====


---

## VIRTUAL FILE 42/44 — `analysis/SOURCE_SECTION_DISPOSITION.md`

**Virtual path:** `analysis/SOURCE_SECTION_DISPOSITION.md`  
**Content checksum:** `4e3854859eca`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

# Source Section Disposition

**ID:** UPOS-04-AN-003  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../MODULE_04_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


**Frozen structural sections inspected:** 317  
**Direct Module-04 sections:** 46  
**Mixed Workflow-related sections:** 65

| Source unit | Line | Section | Disposition | Destination |
|---|---:|---|---|---|
| SRC-001 | 17 | 0. Executive model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-002 | 86 | 1. Relationship to the Documentation Operating Model | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-003 | 136 | 2. Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-004 | 224 | 3. Foundational principles | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-005 | 226 | 3.1 Human governance | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-006 | 234 | 3.2 Separation of duties | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-007 | 254 | 3.3 Source of Truth before inference | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-008 | 260 | 3.4 No silent invention | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-009 | 291 | 3.5 Evidence before approval | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-010 | 313 | 3.6 Least privilege | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-011 | 319 | 3.7 Small coherent changes | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-012 | 325 | 3.8 One PR, one intention | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-013 | 331 | 3.9 One commit, one logical change | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-014 | 337 | 3.10 No opportunistic refactoring by default | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-015 | 345 | 3.11 Risk-based governance | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-016 | 353 | 3.12 Organizational learning over hidden memory | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-017 | 371 | 4. Core terminology | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-018 | 373 | Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-019 | 377 | Skill | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-020 | 391 | Workflow | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-021 | 404 | Orchestrator | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-022 | 408 | Guardrail | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-023 | 412 | Gate | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-024 | 416 | Handoff | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-025 | 420 | Project Memory | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-026 | 424 | Run | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-027 | 428 | Evidence | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-028 | 434 | 5. Universal Agent Contract | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-029 | 497 | 6. Agent identity is not enough | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-030 | 521 | 7. Universal role families | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-031 | 559 | 8. Orchestrator | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-032 | 561 | Mission | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-033 | 565 | Responsibilities | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-034 | 583 | Must not | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-035 | 594 | 9. Product Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-036 | 621 | 10. Domain / Architecture Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-037 | 648 | 11. UX / Product Design Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-038 | 671 | 12. Design System Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-039 | 689 | 13. Implementer Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-040 | 718 | 14. Reviewer Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-041 | 749 | 15. QA Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-042 | 773 | 16. Security Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-043 | 798 | 17. Documentation Guardian | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-044 | 821 | 18. Merge Controller | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-045 | 851 | 19. Skills model | DEFERRED_TO_MODULE | UPOS-03 |
| SRC-046 | 870 | 20. Skill contract | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-03 |
| SRC-047 | 902 | 21. Example universal skills | DEFERRED_TO_MODULE | UPOS-03 |
| SRC-048 | 933 | 22. Workflow contract | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-049 | 954 | 23. Change classification | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-050 | 971 | 24. C0 — Micro | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-051 | 996 | 25. C1 — Small | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-052 | 1018 | 26. C2 — Standard Feature | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-053 | 1043 | 27. C3 — Cross-cutting | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-054 | 1070 | 28. C4 — Architectural | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-055 | 1097 | 29. C5 — High-risk | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-056 | 1128 | 30. Risk override rule | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-057 | 1144 | 31. Context assembly | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-058 | 1165 | 32. Context assembly order | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-059 | 1182 | 33. Context budget principle | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-060 | 1198 | 34. Memory model | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-061 | 1215 | 35. Project memory sources | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-062 | 1235 | 36. Learning is not hidden model training | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-063 | 1257 | 37. Learning promotion model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-064 | 1290 | 38. Permissions model | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-065 | 1317 | 39. Default role permission philosophy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-066 | 1319 | Orchestrator | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-067 | 1330 | Implementer | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-068 | 1342 | Reviewer | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-069 | 1353 | QA | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-070 | 1362 | Merge Controller | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-071 | 1374 | 40. Human approval model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-072 | 1391 | 41. Recommended adoption mode | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-073 | 1411 | 42. Planning model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-074 | 1434 | 43. Expected commits | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-075 | 1453 | 44. Git operating principles | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-076 | 1455 | 44.1 No direct push to protected main | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-077 | 1459 | 44.2 One branch per coherent task | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-078 | 1474 | 45. Atomic logical commits | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-079 | 1491 | 46. Bad commit granularity | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-080 | 1507 | 47. Bad oversized commit | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-081 | 1528 | 48. Commit categories | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-082 | 1548 | 49. Commit message contract | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-083 | 1566 | 50. Bug-fix commit strategy | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-084 | 1581 | 51. Review-fix commits | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-085 | 1591 | 52. PR operating model | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-086 | 1601 | 53. Good PR | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-087 | 1624 | 54. Bad PR | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-088 | 1640 | 55. PR size policy | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-089 | 1656 | 56. PR description contract | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-090 | 1692 | 57. Creation loop | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-091 | 1707 | 58. Verification loop | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-092 | 1723 | 59. Self-check | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-093 | 1741 | 60. Independent review protocol | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-094 | 1758 | 61. Review finding severity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-095 | 1778 | 62. Review output contract | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-096 | 1815 | 63. Reviewer independence | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-097 | 1831 | 64. QA protocol | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-098 | 1847 | 65. QA dimensions | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-099 | 1868 | 66. Documentation gate | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-07 |
| SRC-100 | 1886 | 67. Architecture gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-101 | 1903 | 68. Security gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-102 | 1920 | 69. Database migration gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-103 | 1935 | 70. Merge readiness | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-104 | 1949 | 71. Merge authority | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-105 | 1966 | 72. Merge strategy | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-106 | 1982 | 73. Handoff protocol | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-107 | 2027 | 74. Handoff context minimization | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-108 | 2042 | 75. Guardrails | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-109 | 2058 | 76. Guardrail types | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-110 | 2070 | 77. Escalation model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-111 | 2087 | 78. Escalation targets | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-112 | 2101 | 79. Failure and recovery | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-113 | 2119 | 80. Retry policy | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-114 | 2137 | 81. Scope Guardian | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-115 | 2158 | 82. Concurrency model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-116 | 2182 | 83. Task isolation | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-117 | 2202 | 84. Shared file collision | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-118 | 2216 | 85. Workflow — Micro Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-119 | 2237 | 86. Workflow — Bug Fix | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-120 | 2255 | 87. Workflow — New Feature | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-121 | 2276 | 88. Workflow — UI Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-122 | 2292 | 89. Workflow — Design System Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-123 | 2308 | 90. Workflow — Architecture Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-124 | 2326 | 91. Workflow — API Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-125 | 2341 | 92. Workflow — Database Migration | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-126 | 2357 | 93. Workflow — Security Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-127 | 2372 | 94. Workflow — Refactor | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-128 | 2387 | 95. Workflow — Dependency Upgrade | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-129 | 2401 | 96. Workflow — Hotfix | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-130 | 2421 | 97. Workflow — Documentation Change | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-131 | 2436 | 98. Workflow — Release | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-132 | 2452 | 99. Observability model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-133 | 2485 | 100. Dashboard-ready metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-134 | 2510 | 101. Do not optimize for activity | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-135 | 2525 | 102. Quality metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-136 | 2542 | 103. Agent performance | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-137 | 2559 | 104. Agent learning record | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-138 | 2583 | 105. Skill evolution | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-139 | 2604 | 106. Workflow evolution | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-140 | 2617 | 107. Agent contract evolution | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-141 | 2630 | 108. Model/provider independence | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-142 | 2648 | 109. Tool independence | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-143 | 2665 | 110. Safety around secrets | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-144 | 2683 | 111. Production access | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-145 | 2695 | 112. Protected files | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-146 | 2711 | 113. Definition of Ready — task | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-07 |
| SRC-147 | 2730 | 114. Definition of Ready — agent execution | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-148 | 2746 | 115. Definition of Done — implementation | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-149 | 2760 | 116. Definition of Done — PR | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-150 | 2775 | 117. Definition of Done — workflow | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-07 |
| SRC-151 | 2788 | 118. Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-152 | 2864 | 119. Maturity model | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-153 | 2866 | Level 0 — Single Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-154 | 2870 | Level 1 — Role Profiles | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-155 | 2874 | Level 2 — Governed Workflows | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-156 | 2878 | Level 3 — Orchestrated Team | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-157 | 2882 | Level 4 — Automated Verification | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-158 | 2886 | Level 5 — Controlled Autonomy | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-159 | 2890 | Level 6 — Learning Organization | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-160 | 2898 | 120. Recommended adoption sequence | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-161 | 2900 | Stage 1 — Documentation foundation | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-162 | 2904 | Stage 2 — Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-163 | 2908 | Stage 3 — Three roles | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-164 | 2920 | Stage 4 — Add QA and Documentation Guardian | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-165 | 2924 | Stage 5 — Add specialist agents | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-166 | 2928 | Stage 6 — Formal workflows | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-167 | 2932 | Stage 7 — Telemetry | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-168 | 2936 | Stage 8 — Limited autonomous merge | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-169 | 2942 | 121. Recommended first implementation | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-170 | 2982 | 122. Universal Orchestrator algorithm | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-171 | 3009 | 123. Authority conflict resolution | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-172 | 3028 | 124. Security veto | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-173 | 3038 | 125. Architecture veto | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-174 | 3051 | 126. Reviewer veto | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-175 | 3072 | 127. Human override | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-176 | 3091 | 128. Agent output discipline | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-177 | 3107 | 129. Change Classification output | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-178 | 3137 | 130. Implementation Plan output | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-179 | 3174 | 131. Review Result output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-180 | 3206 | 132. QA Result output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-181 | 3232 | 133. Merge Readiness output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-182 | 3252 | 134. Change review feedback loop | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-183 | 3266 | 135. Oversized PR handling | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-184 | 3281 | 136. Scope expansion handling | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-185 | 3298 | 137. Unplanned architecture discovery | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-186 | 3313 | 138. Unplanned product ambiguity | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-187 | 3327 | 139. Unplanned security concern | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-188 | 3333 | 140. Documentation drift detection | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-189 | 3348 | 141. Agent sandbox hygiene | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-190 | 3368 | 142. Branch lifetime | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-191 | 3376 | 143. Stacked PRs | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-192 | 3384 | 144. Feature flags | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-193 | 3399 | 145. Rollback thinking | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-194 | 3411 | 146. Dependency graph awareness | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-195 | 3429 | 147. Cost awareness | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-196 | 3439 | 148. Latency awareness | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-197 | 3457 | 149. Human attention as scarce resource | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-198 | 3474 | 150. Agent communication rule | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-199 | 3482 | 151. Decision preservation | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-200 | 3499 | 152. No circular authority | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-201 | 3514 | 153. Independent model diversity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-202 | 3524 | 154. Review freshness | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-203 | 3532 | 155. Merge queue compatibility | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-204 | 3538 | 156. CI as evidence provider | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-205 | 3555 | 157. Agent-specific test ownership | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-206 | 3577 | 158. Test integrity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-207 | 3583 | 159. Snapshot integrity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-208 | 3589 | 160. Security scanner integrity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-209 | 3595 | 161. Linter suppression | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-210 | 3601 | 162. Technical debt creation | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-211 | 3609 | 163. Technical debt review | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-212 | 3623 | 164. Post-merge verification | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-213 | 3636 | 165. Post-merge learning trigger | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-214 | 3652 | 166. Incident integration | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-215 | 3667 | 167. Dashboard model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-216 | 3690 | 168. Agent workload | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-217 | 3709 | 169. Workflow bottleneck analysis | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-218 | 3724 | 170. Maturity gates for autonomy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-219 | 3740 | 171. Autonomy expansion | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-220 | 3755 | 172. Project-specific overrides | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-221 | 3769 | 173. Universal vs project-specific rules | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-222 | 3791 | 174. Agent manifests should be versioned | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-223 | 3807 | 175. Governance change workflow | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-224 | 3821 | 176. Universal starter agent set | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-225 | 3846 | 177. Universal full agent set | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-226 | 3874 | 178. Agent composition | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-227 | 3896 | 179. Universal policy files | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-228 | 3913 | 180. AI Agent README | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-229 | 3927 | 181. Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-230 | 3944 | 182. Universal file naming | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-231 | 3963 | 183. Agent contract versioning | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-232 | 3975 | 184. Skill versioning | DEFERRED_TO_MODULE | UPOS-03 |
| SRC-233 | 3981 | 185. Workflow versioning | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-234 | 3987 | 186. Telemetry retention | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-235 | 3993 | 187. Sensitive context policy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-236 | 3999 | 188. Secret redaction | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-237 | 4005 | 189. Auditability | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-238 | 4019 | 190. Reproducibility | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-239 | 4035 | 191. Agent hallucination handling | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-240 | 4047 | 192. Missing Source of Truth | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-241 | 4060 | 193. Stale Source of Truth | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-242 | 4072 | 194. Feature lifecycle integration | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-243 | 4080 | 195. Agent lifecycle | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-244 | 4095 | 196. Task lifecycle | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-245 | 4114 | 197. PR lifecycle | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-246 | 4120 | 198. Agent run lifecycle | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-247 | 4136 | 199. Workflow state machine | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-248 | 4142 | 200. No hidden background authority | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-249 | 4148 | 201. Human pause points | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-250 | 4162 | 202. Plan change protocol | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-251 | 4174 | 203. Reclassification | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-252 | 4184 | 204. Risk inheritance | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-253 | 4190 | 205. Change decomposition | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-254 | 4196 | 206. Multi-agent code ownership | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-255 | 4202 | 207. Shared contract first | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-256 | 4215 | 208. Reviewer context independence | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-257 | 4233 | 209. QA context independence | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-258 | 4241 | 210. Merge Controller context | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-259 | 4249 | 211. Product Owner context | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-260 | 4266 | 212. Decision packet | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-261 | 4294 | 213. Do not fake consensus | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-262 | 4302 | 214. Conflict resolution by authority | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-263 | 4317 | 215. Majority voting | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-264 | 4323 | 216. Agent confidence | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-265 | 4331 | 217. Evidence hierarchy | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-266 | 4350 | 218. Change evidence bundle | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-07 |
| SRC-267 | 4367 | 219. Artifact retention | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-268 | 4390 | 220. Privacy of reasoning | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-269 | 4398 | 221. Universal anti-patterns | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-270 | 4400 | 221.1 Agent swarm without ownership | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-271 | 4404 | 221.2 Self-approval | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-272 | 4408 | 221.3 Every task runs every agent | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-273 | 4412 | 221.4 Giant context dump | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-274 | 4416 | 221.5 Prompt duplication | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-275 | 4420 | 221.6 Hidden project memory | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-276 | 4424 | 221.7 Activity metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-277 | 4428 | 221.8 AI-created architecture by accident | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-278 | 4432 | 221.9 Fake review | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-279 | 4436 | 221.10 Git history as keystroke log | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-280 | 4442 | 222. Governance health checks | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-281 | 4459 | 223. Quarterly / milestone review | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-282 | 4475 | 224. Universal adoption checklist | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-283 | 4494 | 225. Minimal viable agent system | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-284 | 4513 | 226. Intermediate agent system | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-285 | 4531 | 227. Advanced agent system | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-286 | 4550 | 228. Final operating model | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-02 |
| SRC-287 | 4600 | Appendix A — Project Agent Manifest template | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-288 | 4679 | Appendix B — Agent Contract template | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-289 | 4722 | Appendix C — Skill template | DEFERRED_TO_MODULE | UPOS-03 |
| SRC-290 | 4757 | Appendix D — Workflow template | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-291 | 4798 | Appendix E — Change Plan template | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-06 |
| SRC-292 | 4832 | Appendix F — Handoff template | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-293 | 4861 | Appendix G — Review Result template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-294 | 4905 | Appendix H — QA Result template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-295 | 4929 | Appendix I — Merge Readiness template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-296 | 4957 | Appendix J — Risk Classification Matrix | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-297 | 4970 | Appendix K — Permission Matrix example | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-298 | 4985 | Appendix L — Git Policy starter | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-299 | 5021 | Appendix M — Review Policy starter | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-300 | 5048 | Appendix N — Human Approval Policy starter | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-10 |
| SRC-301 | 5073 | Appendix O — Example New Feature workflow | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-302 | 5115 | Appendix P — Example Bug Fix workflow | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-303 | 5140 | Appendix Q — Example Architecture Change workflow | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-304 | 5174 | Appendix R — Learning Record template | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-09 |
| SRC-305 | 5202 | Appendix S — Telemetry schema starter | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-08 |
| SRC-306 | 5229 | Appendix T — Adoption directive for an existing project | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-307 | 5279 | Final principles | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-308 | 5281 | 1 | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-309 | 5285 | 2 | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-310 | 5289 | 3 | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-311 | 5293 | 4 | EXTRACTED_TO_MODULE_04 | Module 04 canonical artifacts |
| SRC-312 | 5297 | 5 | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-313 | 5301 | 6 | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-314 | 5305 | 7 | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-315 | 5309 | 8 | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-316 | 5313 | 9 | MIXED_EXTRACTED_AND_DEFERRED | Workflow semantics → Module 04; remaining → UPOS-11 |
| SRC-317 | 5317 | 10 | DEFERRED_TO_MODULE | UPOS-02 |

===== END VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====


---

## VIRTUAL FILE 43/44 — `analysis/TRACEABILITY_VALIDATION.md`

**Virtual path:** `analysis/TRACEABILITY_VALIDATION.md`  
**Content checksum:** `be930db6168e`

===== BEGIN VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====

# UPOS-004 Traceability Validation

**ID:** UPOS-04-AN-009  
**Type:** VALIDATION REPORT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../MODULE_04_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Results

| Check | Result |
|---|---|
| Frozen structural sections inspected | 317 |
| Direct Module-04 structural sections | 46 |
| Mixed Workflow-related structural sections | 65 |
| Extracted Module-04 requirements | 64 |
| Direct Module-04 source sections lacking mapping | 0 |
| Base Workflow Definitions | 8 |
| Concern Profiles | 7 |
| Workflow contracts missing required sections | 0 |
| Profile contracts missing required sections | 0 |
| Unknown UPOS-003 Skill IDs referenced | 0 |
| Hard-coded provider/project-path leakage | 0 |
| Unresolved P0/P1 Module-04 gaps | 0 |
| Routing Decision stable identity | PASS |
| Workflow Instance stable identity | PASS |
| Task stable identity | PASS |
| Base Workflow stages independently addressable | PASS |
| Profile-added stages/checkpoints independently addressable | PASS |
| Declared Workflow transitions independently addressable | PASS |
| Retry bounded | PASS |
| Rework bounded | PASS |
| Failure taxonomy complete | PASS |
| Workflow Catalog required fields | PASS |
| Profile Catalog required fields | PASS |
| Catalog supersession/replacement support | PASS |
| Normative requirement depends exclusively on archived analysis | 0 |

```text
UNMAPPED MODULE-04 SOURCE REQUIREMENTS = 0
```

## Failure / convergence validation

```text
RETRY
!= REWORK
!= RECOVERY
!= RECLASSIFICATION
!= REROUTING
!= ESCALATION
```

**PASS**

```text
No infinite retry loops.
No infinite rework loops.
```

**PASS**

## Boundary validation

- Role/authority/SoD remain UPOS-002: **PASS**
- Skill procedure/evaluation remain UPOS-003: **PASS**
- Context retrieval/memory remain UPOS-005: **PASS**
- Git/PR/merge mechanics remain UPOS-006: **PASS**
- Quality evidence/verdict semantics remain UPOS-007: **PASS**
- Telemetry/event semantics remain UPOS-008: **PASS**
- Learning promotion remains UPOS-009/01: **PASS**
- Permission grants/protected actions remain UPOS-010: **PASS**
- Project/provider bindings remain UPOS-011: **PASS**

## Three-axis architecture

```text
Change Class
+
Work Type
+
Concern Profiles
```

and:

```text
Base Workflow
+
Concern Profiles
+
Change Class
=
Resolved Workflow Configuration
```

remain unchanged: **PASS**

## Final reconciliation scope

Only the requested conformance corrections were made:

1. all 7 canonical Profiles explicitly declare `Dependencies` and `Conflicts`;
2. stable semantic identities exist for Task, Routing Decision, Workflow Instance, Stage and Transition;
3. Retry/Rework/Recovery/Reclassification/Rerouting/Escalation are normatively distinct;
4. retry and rework are bounded with controlled non-convergence handling;
5. Workflow failure taxonomy is explicit and ownership-safe;
6. Workflow/Profile Catalogs satisfy lifecycle/supersession/discovery conformance;
7. traceability covers the material final reconciliation requirements.

No new Base Workflow, Concern Profile, downstream module, runtime, schema, provider integration, or UPOS-005 design was introduced.

## Verdict

PASS — corrected UPOS-004 Workflow Engine v1.0 satisfies the final reconciliation/conformance gates.

```text
NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 05–11
```

UPOS-004 v1.0 is frozen as the canonical Module 04 baseline.

===== END VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====


---

## VIRTUAL FILE 44/44 — `analysis/WORKFLOW_MODEL_DECISION.md`

**Virtual path:** `analysis/WORKFLOW_MODEL_DECISION.md`  
**Content checksum:** `f13f9941eb1a`

===== BEGIN VIRTUAL FILE: analysis/WORKFLOW_MODEL_DECISION.md =====

# Workflow Model Decision — Three-Axis Resolution

**ID:** UPOS-04-AN-004  
**Type:** ARCHITECTURE ANALYSIS / MODEL DECISION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../WORK_TYPE_AND_CONCERN_MODEL.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Hypotheses considered

### A — One Workflow per named frozen-source change type

Rejected.

Reason: UI/API/DB/Security/Architecture overlap in the same task, creating ambiguous selection/combinatorial variants.

### B — One generic mega-workflow with conditional branches

Rejected as primary model.

Reason: hides Work Type intent and becomes difficult to reason/version/audit.

### C — Base Workflow + Concern Profiles + Change Class

Accepted.

```text
Primary intention → Base Workflow
Cross-cutting impacts → Profiles
Risk/impact depth → C0–C5
```

## Source preservation

Frozen named workflows are not discarded.

They are normalized:

- UI/Design System/Architecture/API/DB/Security → Concern Profiles;
- Micro → C0 depth on Generic Change;
- Bug/Feature/Refactor/Dependency Upgrade/Docs/Hotfix/Release → Base Workflows.

## Result

The selected model preserves semantics and allows multi-concern Tasks without multiplying Workflow Definitions.

===== END VIRTUAL FILE: analysis/WORKFLOW_MODEL_DECISION.md =====
