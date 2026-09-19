# UPOS-003 Skills System — ChatGPT Single-File Edition v1.0

**Module:** UPOS-003 — Skills System  
**System:** Universal Project Operating System  
**Canonical baseline:** FROZEN v1.0  
**Embedded virtual files:** 45  
**Generated:** 2026-09-19

---

# 0. Interpretation rule

This is a transport bundle, not a replacement monolith.

Each virtual-file block represents one repository file under `03_skills_system/`.

Normative authority remains with the embedded normative Markdown documents.

`analysis/` is historical EVIDENCE only.

`MODULE_03_TRACEABILITY.md` is the canonical normative coverage artifact.

## Core disposition semantics

```text
CANONICAL_UNIVERSAL_SKILL
= reusable bounded Skill whose core procedural semantics
  are fully owned by UPOS-003 and broadly project-independent

INTERFACE_SKILL
= reusable bounded Skill owned as a Skill Definition by UPOS-003
  whose correct execution depends on authoritative semantics
  provided by another U-POS module through an explicit interface
```

```text
INTERFACE_SKILL
!= lifecycle status
!= lower-quality Skill
!= temporary Skill
!= authority delegation
```

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Frozen validation

```text
UNMAPPED MODULE-03 SOURCE REQUIREMENTS = 0

NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 04–11
```

# 1. Virtual repository tree

```text
03_skills_system/
├── README.md
├── SKILLS_OPERATING_MODEL.md
├── SKILL_CONTRACT_STANDARD.md
├── SKILL_REGISTRY_STANDARD.md
├── SKILL_TAXONOMY.md
├── SKILL_LIFECYCLE.md
├── SKILL_VERSIONING.md
├── SKILL_DEPENDENCY_AND_COMPOSITION.md
├── SKILL_EVALUATION_STANDARD.md
├── SKILL_EVOLUTION_INTERFACE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_03_DEFINITION_OF_DONE.md
├── MODULE_03_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── skills/analyze-impact.md
├── skills/analyze-incident.md
├── skills/assemble-context.md
├── skills/assess-merge-readiness.md
├── skills/capture-learning.md
├── skills/classify-change.md
├── skills/create-adr.md
├── skills/create-atomic-commit.md
├── skills/create-ddr.md
├── skills/create-feature-spec.md
├── skills/create-implementation-plan.md
├── skills/create-pdr.md
├── skills/create-rfc.md
├── skills/implement-change.md
├── skills/prepare-release.md
├── skills/qa-validation.md
├── skills/reconcile-documentation.md
├── skills/reproduce-bug.md
├── skills/review-architecture.md
├── skills/review-diff.md
├── skills/review-security.md
├── skills/write-regression-test.md
├── templates/SKILL_CONTRACT_TEMPLATE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MODULE_03_OWNERSHIP_MAP.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/SKILL_CANDIDATE_CLASSIFICATION.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
```

# 2. Embedded files


---

## VIRTUAL FILE 1/45 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `d3c1ffe60d2e`

===== BEGIN VIRTUAL FILE: README.md =====

# UPOS-003 — Skills System

**ID:** UPOS-03-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, frozen master design source


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-003 defines how reusable capabilities are represented, governed, versioned, discovered, evaluated, composed, and evolved inside the Universal Project Operating System.

The module answers:

> What is a reusable capability inside U-POS, how is it formally defined, versioned, evaluated, combined, evolved, and used by agents without becoming an Agent Role or Workflow?

## 1. Fundamental model

```text
ROLE / AGENT
= WHO is organizationally responsible

SKILL
= reusable bounded capability / procedure

WORKFLOW
= WHEN, WHY and IN WHAT ORDER
  roles and skills participate

POLICY
= what is allowed / required / forbidden

CONTEXT
= authoritative information provided to execution

TOOL
= technical capability used to act
```

These concepts MUST NOT be used interchangeably.

## 2. Skill identity model

```text
SKILL DEFINITION
= versioned canonical reusable procedure contract

SKILL IMPLEMENTATION
= executable/provider/tool-specific realization
  if/when such layer exists

SKILL INVOCATION
= one bounded execution/use of a Skill
  inside an Agent Run / Workflow

SKILL RESULT
= attributable output of that invocation
```

A Skill Definition is normative. A future Skill Implementation is not allowed to silently redefine it.

## 3. Module 03 owns

- Skill definition and identity;
- Skill Contract;
- Skill taxonomy/categories;
- reusable procedure semantics;
- inputs/outputs;
- preconditions and meaningful postconditions;
- source-class requirements;
- context/tool/permission interface requirements;
- procedural invariants;
- skill-level quality criteria;
- skill-specific failure modes and escalation triggers;
- applicable-role interface;
- applicability constraints;
- dependencies and composition;
- invocation semantics at contract level;
- registry/discovery;
- lifecycle/versioning/compatibility/deprecation/supersession;
- skill evaluation semantics;
- Skill evolution interface;
- universal reusable Skill catalog;
- Module 03 cross-module interfaces;
- Module 03 source traceability.

## 4. Module 03 does not own

```text
Role / authority / SoD / handoff              → UPOS-002
Workflow orchestration / C0-C5 / routing      → UPOS-004
Context retrieval / memory / budget           → UPOS-005
Git branch / commit / PR / merge policy       → UPOS-006
Review/QA evidence and gate verdict semantics → UPOS-007
Telemetry / traces / metrics / dashboard      → UPOS-008
Learning detection/promotion                  → UPOS-009 + UPOS-01
Permissions / secrets / production            → UPOS-010
Project paths / providers / overrides          → UPOS-011
Canonical project knowledge governance         → UPOS-01
```

Module 03 MAY define interface requirements toward these owners. It MUST NOT privately redefine their semantics.

## 5. Central invariant

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

A Role may be capable of invoking a Skill but still lack authority to use its result to decide a specific project fact.

Authority remains owned by UPOS-002.

## 6. Knowledge invariant

Skill output does not become canonical truth merely because the Skill completed successfully.

```text
Skill Result
→ epistemic class / evidence / proposal / finding / candidate
→ UPOS-01 Knowledge Lifecycle
→ explicit validation/promotion where applicable
```

## 7. Read order

1. `SKILLS_OPERATING_MODEL.md`
2. `SKILL_CONTRACT_STANDARD.md`
3. `SKILL_TAXONOMY.md`
4. `SKILL_REGISTRY_STANDARD.md`
5. `SKILL_LIFECYCLE.md`
6. `SKILL_VERSIONING.md`
7. `SKILL_DEPENDENCY_AND_COMPOSITION.md`
8. `SKILL_EVALUATION_STANDARD.md`
9. `SKILL_EVOLUTION_INTERFACE.md`
10. `CROSS_MODULE_INTERFACES.md`
11. relevant `skills/*.md`
12. `MODULE_03_TRACEABILITY.md`

## 8. Upstream dependencies

UPOS-003 consumes:

- UPOS-01 Documentation System;
- Project Source-of-Truth Model;
- Project Knowledge Lifecycle Model;
- frozen UPOS-002 Agent Organization v1.0.

It references these systems and does not duplicate their ownership.

===== END VIRTUAL FILE: README.md =====


---

## VIRTUAL FILE 2/45 — `SKILLS_OPERATING_MODEL.md`

**Virtual path:** `SKILLS_OPERATING_MODEL.md`  
**Content checksum:** `7e069942de0d`

===== BEGIN VIRTUAL FILE: SKILLS_OPERATING_MODEL.md =====

# Skills Operating Model

**ID:** UPOS-03-SOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SKILL_CONTRACT_STANDARD.md, CROSS_MODULE_INTERFACES.md


## 1. Definition

A **Skill** is:

> a versioned reusable bounded procedure/capability that transforms defined inputs into defined outputs under explicit preconditions, constraints, quality criteria, and failure/escalation rules.

A production Skill MUST be reusable beyond one single task instance and MUST have semantic value beyond simply wrapping one tool command.

## 2. A Skill is not

A Skill is not:

- a Role;
- an Agent persona;
- a Workflow;
- a Task;
- a Policy;
- a Tool;
- a prompt fragment;
- an arbitrary checklist;
- a hidden multi-role process;
- a substitute for canonical project knowledge.

## 3. Skill disposition classes

UPOS-003 defines two normative Skill disposition classes for the v1 universal library.

### CANONICAL_UNIVERSAL_SKILL

A reusable bounded Skill whose core procedural semantics are fully owned by UPOS-003 and are broadly project-independent.

This classification means:

- the reusable procedure can be defined completely inside Module 03;
- correct execution does not depend on another U-POS module owning a central part of the procedure's semantic truth;
- the Skill may still consume external authoritative project context, policies, tools, or permissions through interfaces.

### INTERFACE_SKILL

A reusable bounded Skill owned as a Skill Definition by UPOS-003, but whose correct execution depends on authoritative semantics provided by another U-POS module through an explicit interface.

Examples include:

```text
classify-change
→ INTERFACE_SKILL
because classification/routing semantics belong to UPOS-004

assemble-context
→ INTERFACE_SKILL
because retrieval/budget/memory semantics belong to UPOS-005

create-atomic-commit
→ INTERFACE_SKILL
because Git/commit policy belongs to UPOS-006

review-diff / qa-validation
→ INTERFACE_SKILL
because evidence/verdict/quality semantics belong to UPOS-007

capture-learning
→ INTERFACE_SKILL
because systemic learning/promotion belongs to UPOS-009 + UPOS-01
```

`INTERFACE_SKILL` is classification/disposition metadata only.

```text
INTERFACE_SKILL
!= lifecycle status
!= lower-quality Skill
!= temporary Skill
!= authority delegation
```

A Skill's disposition MUST NOT be used to infer organizational authority, maturity, lifecycle state, or execution priority.

## 5. Boundedness

A Skill MUST have a bounded purpose.

A Skill becomes suspect when it:

- coordinates multiple organizational roles;
- silently decides workflow order;
- embeds broad project policy;
- owns a whole feature lifecycle;
- absorbs multiple unrelated outputs;
- requires unrelated authorities to complete.

Example:

```text
implement-change
= bounded execution capability against an approved Change Plan segment

build-entire-feature
= likely hidden Workflow / mega-skill and SHOULD be rejected or split
```

## 5. Reuse

Skills SHOULD be reusable across projects when the underlying capability is universal.

Project-specific details MUST enter through:

- Source Classes;
- Context interfaces;
- Tool interfaces;
- Permission interfaces;
- project/provider bindings owned by UPOS-011.

## 6. Skill invocation

A Skill Invocation is a bounded use of one Skill Definition within an Agent Run/Workflow.

A Skill Invocation MUST be attributable to:

- Skill ID;
- Skill version;
- invoking Role/Agent Run;
- task/work item;
- input/context references;
- produced Skill Result.

Exact runtime state/event representation is deferred to UPOS-004/08 and the cross-cutting machine-readable schemas layer.

## 7. Skill result

A Skill Result MUST preserve the output class required by its contract.

Typical classes include:

```text
ANALYSIS
PROPOSAL
PLAN
DECISION_RECORD_DRAFT
IMPLEMENTATION_CHANGE
TEST_CHANGE
REVIEW_FINDING
QA_OBSERVATION
READINESS_ASSESSMENT
DOCUMENTATION_CHANGE
LEARNING_CANDIDATE
RELEASE_PREPARATION
INCIDENT_ANALYSIS
```

A result class does not imply canonicality.

## 8. Authority separation

Applicable Roles describe capability compatibility.

They MUST NOT be interpreted as authority grants.

Example:

```text
Architecture Role may invoke create-adr
Security Role may invoke create-adr
Domain Role may invoke create-adr
```

but authority over the decision scope remains determined by UPOS-002 and UPOS-01 Source-of-Truth ownership.

## 9. Procedure ownership

A Skill MAY own its reusable procedure.

It MUST NOT own full cross-role orchestration.

```text
reproduce-bug         → Skill
write-regression-test → Skill
implement-change      → Skill
review-diff           → Skill
qa-validation         → Skill

Bug Fix sequencing and required gates
→ UPOS-004 Workflow Engine
```

## 10. Tool independence

A Skill MAY require abstract capabilities such as:

```text
repository-read
diff-inspection
test-execution
document-write
search
commit-capable-interface
```

Universal Skill Contracts SHOULD NOT hard-code a model/provider/repository vendor when an abstract capability is sufficient.

## 11. Context boundary

A Skill declares what Source Classes and Context interfaces it requires.

UPOS-003 does not define retrieval ranking, freshness rules, context budgets, or physical project paths.

## 12. Failure behavior

Skill-level failure semantics cover only execution of the bounded capability.

Cross-step retry/recovery sequencing belongs to UPOS-004.

Permission denial belongs to UPOS-010.

Provider/tool failure translation belongs to runtime/adapters.

## 13. Minimalism rule

The Skill library SHOULD remain intentionally small.

A candidate Skill must justify:

- repeatability;
- boundedness;
- reusable semantic procedure;
- meaningful contract;
- independent evaluation value.

Naming an action with a verb is not sufficient reason to create a Skill.

===== END VIRTUAL FILE: SKILLS_OPERATING_MODEL.md =====


---

## VIRTUAL FILE 3/45 — `SKILL_CONTRACT_STANDARD.md`

**Virtual path:** `SKILL_CONTRACT_STANDARD.md`  
**Content checksum:** `7039cdc02602`

===== BEGIN VIRTUAL FILE: SKILL_CONTRACT_STANDARD.md =====

# Skill Contract Standard

**ID:** UPOS-03-SCS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/SKILL_CONTRACT_TEMPLATE.md


## 1. Requirement

Every production-grade universal Skill MUST have a versioned Skill Contract.

## 2. Mandatory fields

A Skill Contract MUST contain:

```text
Identity
Purpose
Category
Scope
Non-scope

Inputs
Outputs

Preconditions
Postconditions where meaningful

Required Source Classes
Optional Source Classes

Required Context Interface
Tool Interface Requirements
Permission Interface Requirements

Applicable Roles
Applicable Work/Risk Constraints by reference

Procedure
Procedural Invariants

Quality Criteria
Validation Requirements

Failure Modes
Escalation Conditions

Dependencies
Composition Rules

Prohibited Behavior

Lifecycle
Version

Related Skills
Replacement / Supersession if applicable
```

## 3. Identity

Minimum identity:

- stable `skill_id`;
- canonical name;
- version;
- lifecycle status;
- primary category.

`skill_id` SHOULD remain stable across compatible versions.

## 4. Inputs and outputs

Inputs and outputs MUST describe semantic data, not a specific provider prompt format.

Inputs SHOULD identify whether a value is:

- required;
- optional;
- canonical-context reference;
- evidence reference;
- task-local material.

Outputs MUST define the expected Skill Result class.

## 5. Source classes

A Skill MUST declare required canonical Source Classes when its correctness depends on project truth.

It MUST NOT hard-code repository paths.

Example:

```text
Required Source Classes:
- Product Contract
- Architecture Contract
- relevant Decision Records
```

Physical resolution is external.

## 6. Context interface

The contract may state required context characteristics.

It MUST NOT define:

- retrieval algorithm;
- authority weighting;
- context budget;
- freshness algorithm;
- memory policy.

Those belong to UPOS-005.

## 7. Tool interface

Tool requirements MUST normally be capability-based, e.g.:

```text
repository-read
repository-write
diff-inspection
test-execution
search
document-write
```

Concrete tool/provider binding belongs to UPOS-011.

## 8. Permission interface

A Skill may declare required permission capabilities.

It MUST NOT grant them.

Example:

```text
create-atomic-commit requires a commit-capable interface
```

Who may receive that permission and under what repository policy is external.

## 9. Applicable roles

`Applicable Roles` means the Skill is semantically compatible with those Roles.

It does not alter Role authority.

## 10. Work/risk constraints

A Skill may reference externally owned work/risk constraints.

It MUST NOT redefine canonical C0–C5 semantics or Workflow consequences.

## 11. Procedure

Procedure is the bounded reusable method owned by the Skill.

It SHOULD be:

- ordered only where order is intrinsic to the capability;
- small enough to evaluate;
- independent of full multi-role orchestration.

## 12. Quality criteria

Quality criteria define what correct execution of the Skill means at the Skill Contract level.

They MUST avoid replacing downstream Quality verdict semantics.

## 13. Failure and escalation

Skill-specific failures include:

- missing required semantic input;
- violated precondition;
- ambiguous result;
- inability to satisfy output contract;
- detected boundary breach;
- unavailable required interface.

The Skill MUST escalate rather than invent missing authority or canonical project truth.

## 14. Dependencies

Dependencies MUST use explicit relationships defined by `SKILL_DEPENDENCY_AND_COMPOSITION.md`.

## 15. Lifecycle/version

Every Skill Definition MUST declare lifecycle and version under the Module 03 lifecycle/versioning standards.

===== END VIRTUAL FILE: SKILL_CONTRACT_STANDARD.md =====


---

## VIRTUAL FILE 4/45 — `SKILL_REGISTRY_STANDARD.md`

**Virtual path:** `SKILL_REGISTRY_STANDARD.md`  
**Content checksum:** `64ae3323cad7`

===== BEGIN VIRTUAL FILE: SKILL_REGISTRY_STANDARD.md =====

# Skill Registry Standard

**ID:** UPOS-03-REG-001  
**Type:** REGISTRY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** skills/*.md


## 1. Purpose

The Skill Registry is the canonical human-readable index/discovery layer for active and historical Skill Definitions.

It MUST NOT duplicate entire Skill Contracts.

## 2. Required registry fields

```text
skill_id
name
version
status
category
purpose
applicable_roles
dependencies
supersedes
replacement
contract_ref
```

## 3. Registry semantics

- one row identifies one Skill Definition version;
- `contract_ref` points to the canonical Skill Contract;
- applicable roles are capability compatibility, not authority grants;
- dependency summary is an index, not the normative dependency definition;
- supersession/replacement fields must agree with lifecycle/versioning documents.

## 4. Disposition metadata

The Registry MAY contain a `disposition` field in addition to the mandatory registry fields.

For v1 the canonical values are:

```text
CANONICAL_UNIVERSAL_SKILL
INTERFACE_SKILL
```

Their normative meanings are defined in `SKILLS_OPERATING_MODEL.md`.

Registry consumers MUST NOT treat `INTERFACE_SKILL` as:

```text
lifecycle status
quality downgrade
temporary status
authority delegation
```

It means only that correct execution depends on authoritative semantics supplied by another U-POS module through an explicit interface.

## 5. Machine-readable registry

A future machine-readable registry MAY mirror these index fields through the cross-cutting U-POS schemas/runtime layer.

It MUST remain traceable to normative Markdown and MUST NOT become an independent semantic source.

## 6. v1 registry

| skill_id | name | version | status | category | purpose | applicable_roles | dependencies | supersedes | replacement | contract_ref | disposition |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| `SKL-ANALYZE-IMPACT` | `analyze-impact` | 1.0.0 | ACTIVE | `analysis` | Analyze the bounded impact of a proposed or implemented change across declared project scopes. | Product, Domain, Architecture, Implementer, Reviewer, Security, Documentation Guardian | none | none | none | `skills/analyze-impact.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-ANALYZE-INCIDENT` | `analyze-incident` | 1.0.0 | ACTIVE | `operations` | Produce evidence-backed incident analysis separating observed facts, hypotheses, contributing causes and follow-up candidates. | DevOps / SRE, Architecture, Security, Implementer, QA | OPTIONALLY_USES analyze-impact | none | none | `skills/analyze-incident.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-ASSEMBLE-CONTEXT` | `assemble-context` | 1.0.0 | ACTIVE | `governance` | Request and organize a task-appropriate context bundle through the canonical Context interface. | Orchestrator, Implementer, Reviewer, QA, Architecture, Product, Security | none | none | none | `skills/assemble-context.md` | INTERFACE_SKILL |
| `SKL-ASSESS-MERGE-READINESS` | `assess-merge-readiness` | 1.0.0 | ACTIVE | `governance` | Collect and assess whether required readiness evidence appears present, deferring final readiness semantics/authority to UPOS-007/002/010. | Merge Controller, Reviewer, QA | none | none | none | `skills/assess-merge-readiness.md` | INTERFACE_SKILL |
| `SKL-CAPTURE-LEARNING` | `capture-learning` | 1.0.0 | ACTIVE | `governance` | Transform an evidence-backed recurring/systemic observation into a structured Learning Candidate without promoting it. | Documentation Guardian, Reviewer, QA, Architecture, Security, Orchestrator | none | none | none | `skills/capture-learning.md` | INTERFACE_SKILL |
| `SKL-CLASSIFY-CHANGE` | `classify-change` | 1.0.0 | ACTIVE | `classification` | Produce a structured change-classification recommendation against the canonical classification model. | Orchestrator, Product, Architecture, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/classify-change.md` | INTERFACE_SKILL |
| `SKL-CREATE-ADR` | `create-adr` | 1.0.0 | ACTIVE | `specification` | Record an architecture-oriented decision in the project's ADR format after the decision authority is established. | Architecture, Domain, Security | none | none | none | `skills/create-adr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-ATOMIC-COMMIT` | `create-atomic-commit` | 1.0.0 | ACTIVE | `implementation` | Assess a staged logical change against the external atomic-commit standard and prepare a commit request/metadata. | Implementer | none | none | none | `skills/create-atomic-commit.md` | INTERFACE_SKILL |
| `SKL-CREATE-DDR` | `create-ddr` | 1.0.0 | ACTIVE | `specification` | Record a design/UX/design-system decision under the project's DDR convention after valid authority exists. | UX / Product Design, Design System | none | none | none | `skills/create-ddr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-FEATURE-SPEC` | `create-feature-spec` | 1.0.0 | ACTIVE | `specification` | Draft or update a bounded feature specification from approved Product intent and authoritative constraints. | Product, Domain, Architecture, UX | OPTIONALLY_USES analyze-impact | none | none | `skills/create-feature-spec.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-IMPLEMENTATION-PLAN` | `create-implementation-plan` | 1.0.0 | ACTIVE | `planning` | Translate an approved bounded change into a coherent implementation plan without changing approved semantics. | Architecture, Implementer, Orchestrator | OPTIONALLY_USES analyze-impact | none | none | `skills/create-implementation-plan.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-PDR` | `create-pdr` | 1.0.0 | ACTIVE | `specification` | Record a product decision using the project PDR convention after valid Product authority exists. | Product | none | none | none | `skills/create-pdr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-RFC` | `create-rfc` | 1.0.0 | ACTIVE | `specification` | Produce a structured proposal for a material design/architecture/technical change requiring review before decision. | Architecture, Domain, Security, Product, Design System | OPTIONALLY_USES analyze-impact | none | none | `skills/create-rfc.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-IMPLEMENT-CHANGE` | `implement-change` | 1.0.0 | ACTIVE | `implementation` | Execute one bounded approved implementation change while preserving scope and authoritative contracts. | Implementer | OPTIONALLY_USES analyze-impact, OPTIONALLY_USES write-regression-test | none | none | `skills/implement-change.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-PREPARE-RELEASE` | `prepare-release` | 1.0.0 | ACTIVE | `operations` | Prepare a bounded release package/readiness set from an already selected release candidate without owning deployment Workflow sequencing. | DevOps / SRE, Implementer, Documentation Guardian | none | none | none | `skills/prepare-release.md` | INTERFACE_SKILL |
| `SKL-QA-VALIDATION` | `qa-validation` | 1.0.0 | ACTIVE | `verification` | Exercise intended behavior against acceptance/user/regression scenarios and return observations/evidence for the external QA verdict model. | QA | none | none | none | `skills/qa-validation.md` | INTERFACE_SKILL |
| `SKL-RECONCILE-DOCUMENTATION` | `reconcile-documentation` | 1.0.0 | ACTIVE | `governance` | Identify documentation impact of a bounded change and update/propose updates to the correct canonical owners without redefining project truth. | Documentation Guardian, Implementer, Product, Architecture | OPTIONALLY_USES analyze-impact | none | none | `skills/reconcile-documentation.md` | INTERFACE_SKILL |
| `SKL-REPRODUCE-BUG` | `reproduce-bug` | 1.0.0 | ACTIVE | `analysis` | Produce a controlled, evidence-backed reproduction of an observed defect or explicitly report that reproduction was not achieved. | Implementer, Reviewer, QA | none | none | none | `skills/reproduce-bug.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-REVIEW-ARCHITECTURE` | `review-architecture` | 1.0.0 | ACTIVE | `verification` | Evaluate a proposed/implemented change for conformance with canonical architecture contracts and decision boundaries. | Architecture, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/review-architecture.md` | INTERFACE_SKILL |
| `SKL-REVIEW-DIFF` | `review-diff` | 1.0.0 | ACTIVE | `verification` | Perform a bounded technical review of a change diff against authoritative contracts and externally owned quality semantics. | Reviewer, Architecture, Security, Domain, UX / Product Design, Design System | OPTIONALLY_USES analyze-impact | none | none | `skills/review-diff.md` | INTERFACE_SKILL |
| `SKL-REVIEW-SECURITY` | `review-security` | 1.0.0 | ACTIVE | `verification` | Assess a bounded change for security risks and contract conformance using externally owned Security authority/policy. | Security, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/review-security.md` | INTERFACE_SKILL |
| `SKL-WRITE-REGRESSION-TEST` | `write-regression-test` | 1.0.0 | ACTIVE | `implementation` | Create a focused automated test that proves a known defect/contract regression and protects the corrected behavior. | Implementer, Reviewer, QA | OPTIONALLY_USES reproduce-bug | none | none | `skills/write-regression-test.md` | CANONICAL_UNIVERSAL_SKILL |

===== END VIRTUAL FILE: SKILL_REGISTRY_STANDARD.md =====


---

## VIRTUAL FILE 5/45 — `SKILL_TAXONOMY.md`

**Virtual path:** `SKILL_TAXONOMY.md`  
**Content checksum:** `9c702cac822c`

===== BEGIN VIRTUAL FILE: SKILL_TAXONOMY.md =====

# Skill Taxonomy

**ID:** UPOS-03-TAX-001  
**Type:** TAXONOMY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Purpose

Taxonomy exists for discovery and governance, not bureaucracy.

## 2. Primary categories

UPOS-003 v1 retains the frozen-source baseline because the categories are broad, non-overlapping enough for discovery, and do not encode Workflow sequence:

1. `classification`
2. `planning`
3. `analysis`
4. `specification`
5. `implementation`
6. `verification`
7. `governance`
8. `operations`

Each Skill MUST have exactly one primary category.

## 3. Capability tags

A Skill MAY additionally use lightweight capability tags.

Examples:

```text
decision-record
architecture
security
documentation
testing
git-interface
context-interface
learning-interface
incident
release
```

Tags MUST NOT become hidden categories with independent governance.

## 4. Category semantics

### classification
Transforms described work/material into a structured classification recommendation against an externally owned classification model.

### planning
Produces bounded execution/planning artifacts.

### analysis
Produces structured analysis/evidence without directly changing implementation.

### specification
Produces normative-candidate or proposal artifacts describing desired behavior/decisions.

### implementation
Creates or modifies implementation artifacts under an approved scope.

### verification
Checks an artifact/behavior against externally owned contracts/criteria.

### governance
Maintains governed documentation/decision/readiness relationships without acquiring the authority of those owners.

### operations
Prepares/analyzes operational execution such as releases or incidents without silently owning operational Workflow sequencing.

## 5. Anti-proliferation rule

Do not create a new primary category merely because one Skill is difficult to classify.

Prefer a stable primary category plus tags unless a recurring family with materially distinct governance semantics emerges.

===== END VIRTUAL FILE: SKILL_TAXONOMY.md =====


---

## VIRTUAL FILE 6/45 — `SKILL_LIFECYCLE.md`

**Virtual path:** `SKILL_LIFECYCLE.md`  
**Content checksum:** `9f5fea5ffb47`

===== BEGIN VIRTUAL FILE: SKILL_LIFECYCLE.md =====

# Skill Lifecycle

**ID:** UPOS-03-LFC-001  
**Type:** LIFECYCLE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Skill Definition lifecycle

Canonical lifecycle:

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

Controlled alternate transitions MAY include:

```text
REVIEW → DRAFT
APPROVED → REVIEW
DEPRECATED → ACTIVE
```

if governance explicitly revalidates the Definition.

## 2. State meanings

### DRAFT
Contract is being authored and is not a production standard.

### REVIEW
Contract is under governance/technical review.

### APPROVED
Contract semantics are approved but may not yet be operationally adopted.

### ACTIVE
Contract is approved for production use.

### DEPRECATED
New invocation SHOULD stop where a supported replacement exists. Existing references may remain during migration.

### RETIRED
Skill Definition must not be selected for new governed work.

## 3. Separate invocation lifecycle

```text
Skill Definition lifecycle
!= Skill Invocation execution state
!= Agent Run lifecycle
!= Workflow lifecycle
```

Invocation states are runtime/workflow/observability concerns and are not defined here.

## 4. Deprecation

Deprecation MUST state:

- reason;
- replacement if any;
- migration compatibility;
- effective date/version where practical.

## 5. Retirement

A Skill MAY be retired only when active consumers can resolve a replacement or intentionally stop using the capability.

Historical contracts remain available for audit/provenance under Documentation governance.

===== END VIRTUAL FILE: SKILL_LIFECYCLE.md =====


---

## VIRTUAL FILE 7/45 — `SKILL_VERSIONING.md`

**Virtual path:** `SKILL_VERSIONING.md`  
**Content checksum:** `ba0918bdf709`

===== BEGIN VIRTUAL FILE: SKILL_VERSIONING.md =====

# Skill Versioning

**ID:** UPOS-03-VER-001  
**Type:** VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

Skill Definitions MUST be versioned when behavior materially changes.

U-POS v1 uses semantic versioning as a governance convention, independent of package-manager technology.

## 2. MAJOR

Increment MAJOR when compatibility is broken, including:

- incompatible input contract change;
- incompatible output contract/result class change;
- fundamental procedure semantic change;
- removal/reinterpretation of mandatory precondition;
- breaking change to dependencies/composition;
- breaking downstream expectation;
- changed failure/escalation behavior that invalidates existing consumers.

## 3. MINOR

Increment MINOR for backward-compatible capability expansion, including:

- optional input;
- optional source class;
- backward-compatible procedure refinement;
- additional validation that does not invalidate conforming consumers;
- new compatible applicable Role.

## 4. PATCH

Increment PATCH for non-semantic/editorial correction, clarification, typo, example repair, or wording that does not change execution obligations.

## 5. Material-change rule

When uncertain whether a change is PATCH or MINOR/MAJOR, evaluate whether a conforming existing invoker or evaluator could observe different required behavior.

If yes, it is not a PATCH.

## 6. Version and lifecycle

A new MAJOR version may coexist temporarily with a deprecated prior version.

Registry/supersession must make active recommendations explicit.

===== END VIRTUAL FILE: SKILL_VERSIONING.md =====


---

## VIRTUAL FILE 8/45 — `SKILL_DEPENDENCY_AND_COMPOSITION.md`

**Virtual path:** `SKILL_DEPENDENCY_AND_COMPOSITION.md`  
**Content checksum:** `cb924e2bfaeb`

===== BEGIN VIRTUAL FILE: SKILL_DEPENDENCY_AND_COMPOSITION.md =====

# Skill Dependency and Composition

**ID:** UPOS-03-DEP-001  
**Type:** DEPENDENCY / COMPOSITION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Relationship types

UPOS-003 defines:

```text
REQUIRES
OPTIONALLY_USES
COMPOSES_WITH
SUPERSEDES
CONFLICTS_WITH
```

## 2. REQUIRES

The Skill cannot satisfy its contract without the dependency capability/result.

`REQUIRES` does not automatically define Workflow order. UPOS-004 owns organizational sequencing.

## 3. OPTIONALLY_USES

The dependency can improve execution but is not required for contract conformance.

## 4. COMPOSES_WITH

Two Skills are explicitly compatible for bounded composition.

The relation does not imply either is mandatory.

## 5. SUPERSEDES

A newer/different Skill replaces the semantic capability of another Skill.

Supersession must align with lifecycle/versioning.

## 6. CONFLICTS_WITH

Two Skill Definitions cannot safely be applied to the same responsibility/result under stated conditions.

## 7. Composition rules

Composition MUST be:

- explicit;
- bounded;
- traceable;
- contract-compatible;
- non-circular where a cycle makes responsibility/execution ambiguous.

## 8. No hidden Workflow

Skill composition MUST NOT be used to encode a full multi-role Workflow.

If composition requires:

- organizational role routing;
- human gates;
- cross-role handoffs;
- merge/release sequencing;
- retry/recovery across stages;

the structure belongs in UPOS-004.

## 9. Mega-skill guardrail

A candidate mega-skill such as `build-entire-feature` SHOULD be rejected or split when its procedure merely hides:

```text
specification
→ implementation
→ independent review
→ QA
→ merge
```

That is organizational composition, not one bounded capability.

===== END VIRTUAL FILE: SKILL_DEPENDENCY_AND_COMPOSITION.md =====


---

## VIRTUAL FILE 9/45 — `SKILL_EVALUATION_STANDARD.md`

**Virtual path:** `SKILL_EVALUATION_STANDARD.md`  
**Content checksum:** `3fe65e289cae`

===== BEGIN VIRTUAL FILE: SKILL_EVALUATION_STANDARD.md =====

# Skill Evaluation Standard

**ID:** UPOS-03-EVAL-001  
**Type:** EVALUATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

A Skill is not successful because the invoking agent says it was successful.

Evaluation MUST be based on observable contract-level criteria.

## 2. Evaluation dimensions

At minimum consider:

1. contract conformance;
2. output correctness;
3. procedure adherence where procedure is normative;
4. quality criteria;
5. failure handling;
6. scope adherence;
7. downstream acceptance where relevant.

## 3. Contract conformance

Check:

- required inputs existed;
- preconditions were satisfied or escalated;
- required result class produced;
- prohibited behavior avoided;
- required source/context interfaces were respected.

## 4. Output correctness

Correctness is evaluated against the Skill's own semantic output contract and externally owned project contracts as referenced.

## 5. Procedure adherence

Only procedure steps owned by the Skill are evaluated here.

Workflow sequencing is outside this standard.

## 6. Failure handling

A conforming Skill MAY return a controlled failure/escalation instead of a nominal output.

Fabricating a result when required truth or capability is missing is evaluation failure.

## 7. No meaningless universal score

Do not reduce Skill quality to a universal `87/100`.

Prefer factual signals such as:

```text
required fields complete
preconditions respected
output schema/contract valid
blocking ambiguity escalated
tests/evidence references present when contract requires them
downstream consumer accepted/rejected
```

## 8. Cross-module boundary

- evidence semantics/gates/verdicts → UPOS-007;
- metric collection/trends/cost → UPOS-008;
- learning detection/promotion → UPOS-009;
- Module 03 defines what successful execution of the Skill Contract means.

===== END VIRTUAL FILE: SKILL_EVALUATION_STANDARD.md =====


---

## VIRTUAL FILE 10/45 — `SKILL_EVOLUTION_INTERFACE.md`

**Virtual path:** `SKILL_EVOLUTION_INTERFACE.md`  
**Content checksum:** `4c98abe34b2e`

===== BEGIN VIRTUAL FILE: SKILL_EVOLUTION_INTERFACE.md =====

# Skill Evolution Interface

**ID:** UPOS-03-EVO-001  
**Type:** EVOLUTION INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-009 Learning, UPOS-01 Knowledge Lifecycle


## 1. Principle

Skill evolution is evidence-driven, versioned, and explicit.

## 2. External learning flow

```text
Outcome
→ Evidence
→ Learning Candidate
→ UPOS-009 analysis
→ UPOS-01 Knowledge Lifecycle validation/promotion
→ proposed Skill Definition change
→ Module 03 review/version decision
→ new Skill version
→ future evaluation
```

## 3. Module 03 owns

UPOS-003 owns:

- evaluating a proposed Skill-definition change against the current contract;
- deciding whether it is PATCH/MINOR/MAJOR under this module's governance;
- publishing/deprecating Skill Definition versions;
- updating registry/dependencies/contracts.

## 4. Module 03 does not own

UPOS-003 does not own:

- detecting systemic learning across the organization;
- validating knowledge promotion;
- silently changing a Skill based on private model memory;
- modifying project standards without their owners.

## 5. Required proposal information

A proposed Skill evolution SHOULD include:

- triggering evidence;
- observed failure/inefficiency;
- proposed contract change;
- impacted procedure/input/output;
- compatibility impact;
- expected evaluation improvement;
- affected dependencies/consumers.

## 6. Hidden-learning prohibition

No model/provider's private memory may be treated as the canonical Skill Definition.

Only governed Skill Contract versions are canonical.

===== END VIRTUAL FILE: SKILL_EVOLUTION_INTERFACE.md =====


---

## VIRTUAL FILE 11/45 — `CROSS_MODULE_INTERFACES.md`

**Virtual path:** `CROSS_MODULE_INTERFACES.md`  
**Content checksum:** `3511a6cdc6db`

===== BEGIN VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

# Module 03 Cross-Module Interfaces

**ID:** UPOS-03-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-003 provides**
- Source Class requirements in Skill Contracts;
- Skill Result epistemic/output class;
- governed Skill Definition artifacts.

**UPOS-003 consumes**
- canonical owner/source resolution;
- provenance;
- document lifecycle;
- explicit knowledge promotion/supersession.

**MUST NOT redefine**
- project truth;
- canonicality;
- promotion rules.

## 2. UPOS-002 — Agent Organization

**Provides**
- applicable-role compatibility for Skills.

**Consumes**
- Role identity;
- Agent Definition skill interface;
- authority/delegation/SoD.

**MUST NOT redefine**
- Role responsibility or authority.

Invariant:

```text
Skill capability != organizational authority
```

## 3. UPOS-004 — Workflow Engine

**Provides**
- Skill IDs/contracts usable by Workflow definitions;
- applicability constraints;
- dependency information that may inform validation.

**Consumes**
- canonical C0–C5 classification model;
- workflow sequencing/routing;
- retry/recovery sequencing.

**MUST NOT redefine**
- change classes;
- Workflow order/gates.

## 4. UPOS-005 — Context & Memory

**Provides**
- Required/Optional Source Classes;
- Required Context Interface characteristics.

**Consumes**
- retrieval/resolution/context assembly;
- context budget/freshness/memory rules.

**MUST NOT redefine**
- retrieval algorithms or context policy.

## 5. UPOS-006 — Engineering Governance

**Provides**
- engineering-oriented reusable Skills such as `create-atomic-commit` and `implement-change`.

**Consumes**
- Git/branch/commit/PR/merge standards;
- Change Plan semantics.

**MUST NOT redefine**
- Git policy or merge strategy.

## 6. UPOS-007 — Quality System

**Provides**
- verification Skill procedures and Skill-level success criteria.

**Consumes**
- evidence semantics;
- finding severity;
- QA/review/readiness verdict semantics;
- quality gate interfaces.

**MUST NOT redefine**
- final quality verdict authority or evidence model.

## 7. UPOS-008 — Observability

**Provides**
- stable Skill identity/version/result references suitable for telemetry correlation.

**Consumes**
- event/trace/metric semantics.

**MUST NOT redefine**
- event model, cost metrics, retention.

## 8. UPOS-009 — Learning System

**Provides**
- versioned evolution target for Skills;
- Skill-evolution interface.

**Consumes**
- learning detection;
- repeated failure analysis;
- promotion proposals.

**MUST NOT redefine**
- organizational learning detection/promotion.

## 9. UPOS-010 — Security & Permissions

**Provides**
- abstract permission-interface requirements declared by Skills.

**Consumes**
- permission taxonomy/grants;
- protected-action rules;
- secrets/production policy.

**MUST NOT redefine**
- who is permitted to execute protected actions.

## 10. UPOS-011 — Project Adapter

**Provides**
- abstract tool/context/source/permission interface requirements.

**Consumes**
- project paths;
- provider bindings;
- concrete tool implementations;
- project-specific overrides/extensions.

**MUST NOT redefine**
- provider-specific wiring.

## 11. Cross-cutting machine-readable schemas layer

A future schema layer may encode Skill Definition/Invocation/Result structures.

Schemas MUST trace back to Module 03 normative Markdown and MUST NOT create independent Skill semantics.

===== END VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====


---

## VIRTUAL FILE 12/45 — `MODULE_03_DEFINITION_OF_DONE.md`

**Virtual path:** `MODULE_03_DEFINITION_OF_DONE.md`  
**Content checksum:** `39367b5a1301`

===== BEGIN VIRTUAL FILE: MODULE_03_DEFINITION_OF_DONE.md =====

# Module 03 Definition of Done

**ID:** UPOS-03-DOD-001  
**Type:** DEFINITION OF DONE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


UPOS-003 v1.0 is complete when:

- [x] Skills System has one clear ownership boundary.
- [x] Skill is formally distinct from Role/Agent/Workflow/Policy/Tool/Context.
- [x] Skill Definition, Skill Implementation, Skill Invocation, and Skill Result are distinguished.
- [x] canonical Skill Contract Standard exists.
- [x] Skill Registry model exists.
- [x] taxonomy/discovery model exists.
- [x] lifecycle exists.
- [x] versioning exists.
- [x] dependency/composition rules exist.
- [x] evaluation model exists.
- [x] evolution interface exists.
- [x] frozen-source candidates are classified.
- [x] all accepted universal Skills have real contracts.
- [x] Skills do not grant organizational authority.
- [x] Skills do not hard-code project paths/providers.
- [x] Context semantics remain with UPOS-005.
- [x] Workflow sequencing remains with UPOS-004.
- [x] Quality verdict/evidence semantics remain with UPOS-007.
- [x] Permissions remain with UPOS-010.
- [x] Learning promotion remains with UPOS-009/01.
- [x] Project bindings remain with UPOS-011.
- [x] upstream UPOS-01/002 are referenced, not duplicated.
- [x] cross-module interfaces are explicit.
- [x] no unresolved P0/P1 Module-03 semantic gaps remain.
- [x] `UNMAPPED MODULE-03 SOURCE REQUIREMENTS = 0`.

===== END VIRTUAL FILE: MODULE_03_DEFINITION_OF_DONE.md =====


---

## VIRTUAL FILE 13/45 — `MODULE_03_TRACEABILITY.md`

**Virtual path:** `MODULE_03_TRACEABILITY.md`  
**Content checksum:** `57249be8d984`

===== BEGIN VIRTUAL FILE: MODULE_03_TRACEABILITY.md =====

# Module 03 Traceability

**ID:** UPOS-03-TRC-001  
**Type:** TRACEABILITY / NORMATIVE COVERAGE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analysis/SOURCE_SECTION_DISPOSITION.md, analysis/TRACEABILITY_VALIDATION.md


## 0. Purpose

Prove that Skill semantics extracted from the frozen `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md` are preserved, assigned to canonical Module 03 artifacts, and separated from other U-POS ownership.

**Frozen source SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`

## 1. Traceability rule

Each Module-03 requirement has:

```text
stable requirement ID
→ frozen source section(s)
→ extracted semantic requirement
→ canonical Module 03 artifact
```

Mixed sections have only Skill semantics extracted. Remaining semantics are explicitly deferred.

## 2. Atomic Module 03 requirements

| Requirement | Frozen source | Extracted requirement | Canonical artifact |
|---|---|---|---|
| `SKL-REQ-001` | §4 Skill, §19 | Skill is a reusable bounded capability/procedure distinct from Role/Agent/Workflow/Policy/Context/Tool. | `SKILLS_OPERATING_MODEL.md` |
| `SKL-REQ-002` | §4 Agent, §4 Workflow, §19 | Role/Agent owns organizational responsibility; Skill owns reusable capability; Workflow owns coordinated sequencing. | `SKILLS_OPERATING_MODEL.md` |
| `SKL-REQ-003` | §19 | Skills should be reusable across projects where semantics are universal. | `SKILLS_OPERATING_MODEL.md` |
| `SKL-REQ-004` | §20, Appendix C | Production Skills require explicit contracts covering purpose, inputs, preconditions, sources, procedure, outputs, quality, failure, escalation, roles and version/status. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-005` | §20, Appendix C | Skill procedure is reusable and bounded; it must not absorb multi-role Workflow sequencing. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-006` | §21, §118, §121 | A small universal starter library is preferable to uncontrolled skill proliferation. | `SKILLS_OPERATING_MODEL.md` |
| `SKL-REQ-007` | §19 | Primary taxonomy baseline includes classification, planning, analysis, specification, implementation, verification, governance and operations. | `SKILL_TAXONOMY.md` |
| `SKL-REQ-008` | §5 Skills, §20 | Agent Contracts reference allowed/required Skills, but Skills do not redefine Role authority. | `CROSS_MODULE_INTERFACES.md` |
| `SKL-REQ-009` | §22 | Workflow definitions may require Skills; sequence/gates remain Workflow ownership. | `CROSS_MODULE_INTERFACES.md` |
| `SKL-REQ-010` | §3.12, §36, §37, §104, §105 | Durable learning may propose Skill updates, but hidden memory is not Skill truth and promotion is governed externally. | `SKILL_EVOLUTION_INTERFACE.md` |
| `SKL-REQ-011` | §105, §184 | Skills must be versioned when procedure/behavior materially changes. | `SKILL_VERSIONING.md` |
| `SKL-REQ-012` | §105 | Skill evolution should be evidence-driven by repeated execution/failure, not arbitrary drift. | `SKILL_EVOLUTION_INTERFACE.md` |
| `SKL-REQ-013` | §108 | Universal Skill contracts should remain provider-independent where possible. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-014` | §118, §121 | Skills have stable discoverable identities/files in a project integration, but universal contracts must not hard-code project paths. | `SKILL_REGISTRY_STANDARD.md` |
| `SKL-REQ-015` | §99, Appendix S | Skill invocation identity/version should be traceable by downstream observability without making Module 03 owner of telemetry. | `CROSS_MODULE_INTERFACES.md` |
| `SKL-REQ-016` | §119, §222 | Governance should detect deprecated Skill use and Skill-system health; metric collection remains external. | `SKILL_LIFECYCLE.md` |
| `SKL-REQ-017` | §163, §166 | Repeated technical/incident problems may indicate Skill problems and become evolution candidates through the learning system. | `SKILL_EVOLUTION_INTERFACE.md` |
| `SKL-REQ-018` | §228 | Final operating model may update Skills after observe/learn, but only through governed evolution. | `SKILL_EVOLUTION_INTERFACE.md` |
| `SKL-REQ-019` | §20 | Skill inputs/outputs and source requirements are semantic contracts, not provider prompt formats. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-020` | §20 | Skill quality criteria define successful bounded execution and must be observable/evaluable. | `SKILL_EVALUATION_STANDARD.md` |
| `SKL-REQ-021` | §20 | Skill failure modes and escalation are first-class contract semantics. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-022` | §20 | Applicable Roles are compatibility metadata, not authority grants. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-023` | §21 | classify-change is a reusable candidate capability but canonical classification/routing remain UPOS-004. | `skills/classify-change.md` |
| `SKL-REQ-024` | §21 | assemble-context is a reusable interface capability but retrieval/budget/memory remain UPOS-005. | `skills/assemble-context.md` |
| `SKL-REQ-025` | §21 | analyze-impact is a reusable bounded analysis capability. | `skills/analyze-impact.md` |
| `SKL-REQ-026` | §21 | create-feature-spec is a reusable specification capability producing a candidate/spec artifact, not automatic canonical truth. | `skills/create-feature-spec.md` |
| `SKL-REQ-027` | §21 | create-rfc is a reusable proposal capability distinct from the decision itself. | `skills/create-rfc.md` |
| `SKL-REQ-028` | §21 | create-adr is a reusable decision-record capability that requires pre-existing valid decision authority. | `skills/create-adr.md` |
| `SKL-REQ-029` | §21 | create-pdr is a reusable product decision-record capability that does not create Product authority. | `skills/create-pdr.md` |
| `SKL-REQ-030` | §21 | create-ddr is a reusable design decision-record capability that does not redefine Product/Domain semantics. | `skills/create-ddr.md` |
| `SKL-REQ-031` | §21 | create-implementation-plan translates approved intent into a bounded plan without owning Workflow routing. | `skills/create-implementation-plan.md` |
| `SKL-REQ-032` | §21 | reproduce-bug produces evidence-backed reproduction or explicit non-reproduction. | `skills/reproduce-bug.md` |
| `SKL-REQ-033` | §21 | write-regression-test produces focused protection for known behavior regression. | `skills/write-regression-test.md` |
| `SKL-REQ-034` | §21 | implement-change is bounded execution against approved scope and cannot silently change project semantics. | `skills/implement-change.md` |
| `SKL-REQ-035` | §21 | create-atomic-commit is a reusable interface procedure; commit policy remains UPOS-006. | `skills/create-atomic-commit.md` |
| `SKL-REQ-036` | §21 | review-diff is a bounded verification procedure; reviewer authority and verdict/evidence semantics remain UPOS-002/007. | `skills/review-diff.md` |
| `SKL-REQ-037` | §21 | review-architecture is bounded architecture conformance review and cannot become architecture decision authority by invocation alone. | `skills/review-architecture.md` |
| `SKL-REQ-038` | §21 | review-security is bounded security review and cannot redefine security veto/permission policy. | `skills/review-security.md` |
| `SKL-REQ-039` | §21 | qa-validation is a bounded behavioral validation procedure; QA verdict semantics remain UPOS-007. | `skills/qa-validation.md` |
| `SKL-REQ-040` | §21 | reconcile-documentation is a bounded documentation reconciliation capability using UPOS-01 canonical owners. | `skills/reconcile-documentation.md` |
| `SKL-REQ-041` | §21 | assess-merge-readiness gathers/readies evidence but final readiness semantics/merge authority remain external. | `skills/assess-merge-readiness.md` |
| `SKL-REQ-042` | §21, §98 | prepare-release is bounded release preparation; deployment/release Workflow sequencing remains external. | `skills/prepare-release.md` |
| `SKL-REQ-043` | §21, §166 | analyze-incident is reusable evidence-backed incident analysis distinct from Incident Workflow and learning promotion. | `skills/analyze-incident.md` |
| `SKL-REQ-044` | §21, §104, §105 | capture-learning may create a Learning Candidate but cannot promote it to canonical truth. | `skills/capture-learning.md` |
| `SKL-REQ-045` | §20, §108 | Tool requirements should be expressed as abstract capabilities where possible; provider bindings remain UPOS-011. | `SKILL_CONTRACT_STANDARD.md` |
| `SKL-REQ-046` | §20 | Permission requirements may be declared by a Skill but grants/taxonomy belong to UPOS-010. | `CROSS_MODULE_INTERFACES.md` |
| `SKL-REQ-047` | §20 | Required Source Classes may be declared by a Skill but Source-of-Truth resolution belongs to UPOS-01/05/11. | `CROSS_MODULE_INTERFACES.md` |
| `SKL-REQ-048` | §20 | Skill dependencies/composition must be explicit and must not be treated as Workflow order. | `SKILL_DEPENDENCY_AND_COMPOSITION.md` |
| `SKL-REQ-049` | §184 | Material Skill behavior changes require version change; non-semantic wording may remain patch-level. | `SKILL_VERSIONING.md` |
| `SKL-REQ-050` | §222 | Deprecated Skills should be discoverable so governance can detect continued use. | `SKILL_REGISTRY_STANDARD.md` |
| `SKL-REQ-051` | Implementation directive §19 + candidate audit | Skill disposition classes `CANONICAL_UNIVERSAL_SKILL` and `INTERFACE_SKILL` are normative Module-03 metadata; `INTERFACE_SKILL` means cross-module semantic dependency and does not imply lifecycle state, lower quality, temporariness, or authority delegation. | `SKILLS_OPERATING_MODEL.md`, `SKILL_REGISTRY_STANDARD.md` |

## 3. Directives from UPOS-003 implementation task

The implementation directive also refined requirements beyond the frozen source, including:

- explicit Skill Definition / Implementation / Invocation / Result identity model;
- Skill ≠ Role/Agent/Workflow/Policy/Context/Tool;
- Skill lifecycle;
- Registry semantics;
- explicit dependency relation types;
- cross-module boundary examples;
- no authority grant through capability;
- no hard-coded project paths/providers;
- analysis artifacts as historical evidence.

These are implemented in canonical Module 03 documents.

## 4. Coverage meaning

`UNMAPPED MODULE-03 SOURCE REQUIREMENTS = 0` means all Skill requirements identified in the frozen-source audit are mapped to Module 03 or explicitly deferred.

It does not claim UPOS-04…11 are implemented.

===== END VIRTUAL FILE: MODULE_03_TRACEABILITY.md =====


---

## VIRTUAL FILE 14/45 — `VIRTUAL_REPOSITORY_TREE.md`

**Virtual path:** `VIRTUAL_REPOSITORY_TREE.md`  
**Content checksum:** `364f5ec967aa`

===== BEGIN VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

# UPOS-003 Virtual Repository Tree

```text
03_skills_system/
├── README.md
├── SKILLS_OPERATING_MODEL.md
├── SKILL_CONTRACT_STANDARD.md
├── SKILL_REGISTRY_STANDARD.md
├── SKILL_TAXONOMY.md
├── SKILL_LIFECYCLE.md
├── SKILL_VERSIONING.md
├── SKILL_DEPENDENCY_AND_COMPOSITION.md
├── SKILL_EVALUATION_STANDARD.md
├── SKILL_EVOLUTION_INTERFACE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_03_DEFINITION_OF_DONE.md
├── MODULE_03_TRACEABILITY.md
├── skills/
│   ├── classify-change.md
│   ├── assemble-context.md
│   ├── analyze-impact.md
│   ├── create-feature-spec.md
│   ├── create-rfc.md
│   ├── create-adr.md
│   ├── create-pdr.md
│   ├── create-ddr.md
│   ├── create-implementation-plan.md
│   ├── reproduce-bug.md
│   ├── write-regression-test.md
│   ├── implement-change.md
│   ├── create-atomic-commit.md
│   ├── review-diff.md
│   ├── review-architecture.md
│   ├── review-security.md
│   ├── qa-validation.md
│   ├── reconcile-documentation.md
│   ├── assess-merge-readiness.md
│   ├── prepare-release.md
│   ├── analyze-incident.md
│   ├── capture-learning.md
├── templates/
│   └── SKILL_CONTRACT_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_03_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── SKILL_CANDIDATE_CLASSIFICATION.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── TRACEABILITY_VALIDATION.md
```

===== END VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====


---

## VIRTUAL FILE 15/45 — `skills/analyze-impact.md`

**Virtual path:** `skills/analyze-impact.md`  
**Content checksum:** `6c4400263e38`

===== BEGIN VIRTUAL FILE: skills/analyze-impact.md =====

# Skill — analyze-impact

**ID:** SKL-ANALYZE-IMPACT  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `analysis`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ANALYZE-IMPACT
name: analyze-impact
version: 1.0.0
status: ACTIVE
category: analysis
```

## Purpose

Analyze the bounded impact of a proposed or implemented change across declared project scopes.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change description/plan/diff
- authoritative context
- declared analysis scope

## Outputs

- ANALYSIS: impacted scopes, dependencies, risks, unknowns, required owner consultations

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant Product/Domain/Architecture/API/Security/UX/Operations contracts

## Optional Source Classes

- historical decisions
- tests/incidents

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `search`
- `diff inspection when applicable`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-authoritative-context`

This declaration does not grant permissions.

## Applicable Roles

- Product
- Domain
- Architecture
- Implementer
- Reviewer
- Security
- Documentation Guardian

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Define analysis boundary.
2. Identify directly changed contracts/artifacts.
3. Trace first-order dependencies using authoritative sources.
4. Identify cross-owner impacts and unknowns.
5. Separate facts, evidence, inference, and proposals.
6. Return impact analysis without changing owner decisions.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- impacts tied to evidence/source classes
- unknowns explicit
- no silent scope expansion
- owner boundaries preserved

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- insufficient authoritative context
- scope too broad for bounded analysis
- contradictory active sources

## Escalation Conditions

- material owner conflict
- high-risk unknown blocks safe conclusion

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/analyze-impact.md =====


---

## VIRTUAL FILE 16/45 — `skills/analyze-incident.md`

**Virtual path:** `skills/analyze-incident.md`  
**Content checksum:** `86f94e08cc86`

===== BEGIN VIRTUAL FILE: skills/analyze-incident.md =====

# Skill — analyze-incident

**ID:** SKL-ANALYZE-INCIDENT  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `operations`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ANALYZE-INCIDENT
name: analyze-incident
version: 1.0.0
status: ACTIVE
category: operations
```

## Purpose

Produce evidence-backed incident analysis separating observed facts, hypotheses, contributing causes and follow-up candidates.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- incident timeline/evidence
- affected system contracts
- analysis scope

## Outputs

- INCIDENT_ANALYSIS: observations, evidence, hypotheses/root-cause confidence, contributing factors, follow-up candidates

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Operations/Architecture/Security contracts
- logs/telemetry evidence
- relevant decisions

## Optional Source Classes

- deploy/change history
- similar incidents

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `logs/telemetry read`
- `repository/document read`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `incident evidence read as externally granted`

This declaration does not grant permissions.

## Applicable Roles

- DevOps / SRE
- Architecture
- Security
- Implementer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Establish timeline from evidence.
2. Separate confirmed observations from hypotheses.
3. Identify contract/system deviations and contributing conditions.
4. Assess root-cause confidence explicitly.
5. Produce follow-up candidates without self-promoting standards/skills/workflows.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- timeline/evidence attributable
- epistemic classes preserved
- root-cause confidence explicit
- follow-ups not silently canonized

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- evidence insufficient
- sensitive evidence inaccessible
- multiple plausible causes unresolved

## Escalation Conditions

- security/privacy impact
- material unresolved causal uncertainty

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/analyze-incident.md =====


---

## VIRTUAL FILE 17/45 — `skills/assemble-context.md`

**Virtual path:** `skills/assemble-context.md`  
**Content checksum:** `f727044b6179`

===== BEGIN VIRTUAL FILE: skills/assemble-context.md =====

# Skill — assemble-context

**ID:** SKL-ASSEMBLE-CONTEXT  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ASSEMBLE-CONTEXT
name: assemble-context
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Request and organize a task-appropriate context bundle through the canonical Context interface.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- task/skill purpose
- required source classes
- role identity
- UPOS-005 context interface

## Outputs

- CONTEXT_REQUEST or CONTEXT_BUNDLE_REFERENCE conforming to UPOS-005

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Source-of-Truth resolution interface metadata

## Optional Source Classes

- previous run artifact references

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `context/source resolver interface`
- `search/read capability`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-context according to external permission policy`

This declaration does not grant permissions.

## Applicable Roles

- Orchestrator
- Implementer
- Reviewer
- QA
- Architecture
- Product
- Security

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Derive required Source Classes from the consuming contract.
2. Request resolution through UPOS-005/UPOS-01 interfaces.
3. Organize returned references for the bounded task.
4. Report missing/stale/conflicting sources instead of compensating privately.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- no physical paths hard-coded
- required source classes covered or explicitly missing
- authority/freshness decisions delegated to owner interfaces

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- context resolver unavailable
- required source unresolved
- permission prevents required context

## Escalation Conditions

- missing canonical source blocks execution
- active sources conflict

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/assemble-context.md =====


---

## VIRTUAL FILE 18/45 — `skills/assess-merge-readiness.md`

**Virtual path:** `skills/assess-merge-readiness.md`  
**Content checksum:** `d2996f1a5134`

===== BEGIN VIRTUAL FILE: skills/assess-merge-readiness.md =====

# Skill — assess-merge-readiness

**ID:** SKL-ASSESS-MERGE-READINESS  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-ASSESS-MERGE-READINESS
name: assess-merge-readiness
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Collect and assess whether required readiness evidence appears present, deferring final readiness semantics/authority to UPOS-007/002/010.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/PR reference
- required gate set from external Workflow/Quality policy
- available evidence/approvals

## Outputs

- READINESS_ASSESSMENT input for MergeReadiness contract

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- UPOS-007 Quality contracts
- UPOS-004 Workflow requirements
- UPOS-010 approval policy
- UPOS-006 merge policy

## Optional Source Classes

- review/QA/security/doc outputs

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `PR/CI/evidence read interfaces`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-evidence; merge capability not implied`

This declaration does not grant permissions.

## Applicable Roles

- Merge Controller
- Reviewer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Resolve externally required gates/approvals for this work.
2. Collect references to their results.
3. Detect missing/stale/conflicting evidence.
4. Return readiness assessment without inventing PASS semantics or exercising merge authority.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- all externally required evidence accounted for
- missing evidence explicit
- no self-approval inference

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- required gate model unavailable
- evidence cannot be resolved

## Escalation Conditions

- conflicting verdicts/approvals
- human approval required but absent

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/assess-merge-readiness.md =====


---

## VIRTUAL FILE 19/45 — `skills/capture-learning.md`

**Virtual path:** `skills/capture-learning.md`  
**Content checksum:** `b0f225e044fc`

===== BEGIN VIRTUAL FILE: skills/capture-learning.md =====

# Skill — capture-learning

**ID:** SKL-CAPTURE-LEARNING  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CAPTURE-LEARNING
name: capture-learning
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Transform an evidence-backed recurring/systemic observation into a structured Learning Candidate without promoting it.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- outcome/failure/review/incident evidence
- candidate systemic pattern
- UPOS-009 Learning interface

## Outputs

- LEARNING_CANDIDATE

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant evidence and affected contracts

## Optional Source Classes

- historical similar findings
- metrics references

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document/evidence read`
- `structured write`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `learning-candidate write if externally authorized`

This declaration does not grant permissions.

## Applicable Roles

- Documentation Guardian
- Reviewer
- QA
- Architecture
- Security
- Orchestrator

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. State trigger and evidence.
2. Explain why the issue may be systemic rather than one-off.
3. Identify affected standards/skills/workflows/tests as candidates only.
4. Record uncertainty/counterevidence.
5. Submit candidate to UPOS-009/UPOS-01 promotion process.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- evidence linked
- systemic claim justified
- promotion target remains proposal
- no hidden canonical update

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- evidence too weak
- pattern is task-specific
- candidate duplicates active learning

## Escalation Conditions

- candidate would change protected universal policy/authority

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/capture-learning.md =====


---

## VIRTUAL FILE 20/45 — `skills/classify-change.md`

**Virtual path:** `skills/classify-change.md`  
**Content checksum:** `4e53b56055be`

===== BEGIN VIRTUAL FILE: skills/classify-change.md =====

# Skill — classify-change

**ID:** SKL-CLASSIFY-CHANGE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `classification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CLASSIFY-CHANGE
name: classify-change
version: 1.0.0
status: ACTIVE
category: classification
```

## Purpose

Produce a structured change-classification recommendation against the canonical classification model.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- task/change description
- authoritative affected-domain context
- canonical change-classification model reference

## Outputs

- CLASSIFICATION_RECOMMENDATION with rationale, uncertainty, affected domains, referenced classification criteria

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Product/Feature Contract as relevant
- Domain/Architecture/Security contracts as relevant

## Optional Source Classes

- historical similar changes
- incident/review evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `source search/read`
- `structured analysis`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-authoritative-context`

This declaration does not grant permissions.

## Applicable Roles

- Orchestrator
- Product
- Architecture
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Normalize the requested change into one coherent intention.
2. Identify affected project scopes without deciding their ownership.
3. Read the externally owned classification criteria.
4. Compare the change against those criteria and risk signals.
5. Return recommendation plus uncertainty/escalation; do not route the Workflow.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- classification recommendation cites authoritative criteria
- affected scopes are explicit
- uncertainty is not hidden
- no routing/gate semantics are invented

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- canonical classification model unavailable
- conflicting authoritative context
- change description too ambiguous

## Escalation Conditions

- classification cannot be justified from owner model
- candidate crosses protected/high-risk semantics requiring owner decision

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/classify-change.md =====


---

## VIRTUAL FILE 21/45 — `skills/create-adr.md`

**Virtual path:** `skills/create-adr.md`  
**Content checksum:** `3d34f5a0271c`

===== BEGIN VIRTUAL FILE: skills/create-adr.md =====

# Skill — create-adr

**ID:** SKL-CREATE-ADR  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-ADR
name: create-adr
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Record an architecture-oriented decision in the project's ADR format after the decision authority is established.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved decision or explicitly delegated decision authority
- decision context
- alternatives/consequences
- ADR standard

## Outputs

- DECISION_RECORD_DRAFT / ADR

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Architecture/Domain/Security contracts
- related RFC/decisions

## Optional Source Classes

- implementation evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `decision-record write capability if authorized`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Domain
- Security

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm decision authority/status.
2. Capture context/problem.
3. Record considered alternatives.
4. Record the selected decision without expanding scope.
5. Record consequences and supersession links.
6. Return ADR artifact for canonical documentation lifecycle.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- decision provenance clear
- alternatives/consequences preserved
- supersession linked
- no unapproved decision invented

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- decision not actually approved/delegated
- owner ambiguous
- decision conflicts with active higher authority

## Escalation Conditions

- authority or canonical conflict unresolved

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-adr.md =====


---

## VIRTUAL FILE 22/45 — `skills/create-atomic-commit.md`

**Virtual path:** `skills/create-atomic-commit.md`  
**Content checksum:** `861bfcbb8981`

===== BEGIN VIRTUAL FILE: skills/create-atomic-commit.md =====

# Skill — create-atomic-commit

**ID:** SKL-CREATE-ATOMIC-COMMIT  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-ATOMIC-COMMIT
name: create-atomic-commit
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Assess a staged logical change against the external atomic-commit standard and prepare a commit request/metadata.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- staged/selected change set
- bounded change intention
- UPOS-006 atomic commit policy

## Outputs

- COMMIT_PREPARATION: validated logical change set + proposed commit metadata/message, or SPLIT_REQUIRED

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Engineering/Git governance

## Optional Source Classes

- Change Plan expected commits

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `diff inspection`
- `git/commit-capable interface`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `commit-capable interface requirement only; grant external`

This declaration does not grant permissions.

## Applicable Roles

- Implementer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify the single logical intention represented by the change set.
2. Compare against external atomic-commit policy.
3. Detect unrelated/multi-purpose changes.
4. Recommend split when necessary.
5. Prepare commit metadata without redefining branch/commit policy.
6. Invoke commit interface only if externally authorized.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- one logical intention
- no unrelated changes
- metadata describes why/what
- external policy referenced

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- change set not coherent
- working tree ambiguous
- commit permission unavailable

## Escalation Conditions

- policy conflict or protected repository rule blocks commit

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-atomic-commit.md =====


---

## VIRTUAL FILE 23/45 — `skills/create-ddr.md`

**Virtual path:** `skills/create-ddr.md`  
**Content checksum:** `40d49c50cad6`

===== BEGIN VIRTUAL FILE: skills/create-ddr.md =====

# Skill — create-ddr

**ID:** SKL-CREATE-DDR  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-DDR
name: create-ddr
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Record a design/UX/design-system decision under the project's DDR convention after valid authority exists.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved/delegated design decision
- design context
- alternatives/consequences
- DDR standard

## Outputs

- DECISION_RECORD_DRAFT / DDR

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- UX/Design System/Product/Domain contracts as relevant

## Optional Source Classes

- research/accessibility evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `decision-record write capability if authorized`

This declaration does not grant permissions.

## Applicable Roles

- UX / Product Design
- Design System

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm design scope and authority.
2. Capture user/problem context.
3. Record alternatives and constraints.
4. Record decision and consequences.
5. Link superseded design decisions.
6. Return DDR artifact.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- does not invent Product/Domain semantics
- design rationale preserved
- accessibility/constraint implications noted where relevant

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- scope/authority ambiguous
- upstream semantics unresolved

## Escalation Conditions

- decision would alter Product/Domain/Security truth

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-ddr.md =====


---

## VIRTUAL FILE 24/45 — `skills/create-feature-spec.md`

**Virtual path:** `skills/create-feature-spec.md`  
**Content checksum:** `b6f16fb6b3fe`

===== BEGIN VIRTUAL FILE: skills/create-feature-spec.md =====

# Skill — create-feature-spec

**ID:** SKL-CREATE-FEATURE-SPEC  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-FEATURE-SPEC
name: create-feature-spec
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Draft or update a bounded feature specification from approved Product intent and authoritative constraints.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved feature intent
- scope/non-goals
- authoritative constraints
- specification template/standard

## Outputs

- PROPOSAL/SPEC_CANDIDATE feature specification

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Product Vision/Principles
- relevant Domain/Architecture/UX/Security contracts

## Optional Source Classes

- research evidence
- existing feature specs
- analytics learnings

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `document-write capability if authorized externally`

This declaration does not grant permissions.

## Applicable Roles

- Product
- Domain
- Architecture
- UX

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Resolve feature scope and owning product intent.
2. Collect relevant constraints by source class.
3. Draft behavior, acceptance intent, non-goals, edge cases, dependencies and open questions.
4. Mark unresolved semantics explicitly.
5. Return proposal for owner review/promotion.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- scope/non-goals explicit
- canonical constraints referenced
- unknowns not fabricated
- does not redefine upstream global contracts

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- feature intent not approved/clear
- critical owner conflict
- required canonical sources missing

## Escalation Conditions

- new domain/architecture/security decision required

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-feature-spec.md =====


---

## VIRTUAL FILE 25/45 — `skills/create-implementation-plan.md`

**Virtual path:** `skills/create-implementation-plan.md`  
**Content checksum:** `b6c16ffabf00`

===== BEGIN VIRTUAL FILE: skills/create-implementation-plan.md =====

# Skill — create-implementation-plan

**ID:** SKL-CREATE-IMPLEMENTATION-PLAN  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `planning`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-IMPLEMENTATION-PLAN
name: create-implementation-plan
version: 1.0.0
status: ACTIVE
category: planning
```

## Purpose

Translate an approved bounded change into a coherent implementation plan without changing approved semantics.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved change/spec/decision
- authoritative technical context
- engineering constraints

## Outputs

- PLAN: bounded Change Plan candidate

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Feature/Product Contract
- Domain/Architecture/API/Engineering contracts
- relevant decisions

## Optional Source Classes

- existing code/tests
- migration/runbook info

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `search`
- `analysis`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read-authoritative-context`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Implementer
- Orchestrator

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Restate approved outcome and non-scope.
2. Identify affected components/contracts.
3. Order intrinsic implementation dependencies without defining organizational Workflow.
4. Define validation needs and risk notes.
5. Propose logical change slices/expected commits by reference to UPOS-006 policy.
6. Record unknowns and owner decisions required.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- plan preserves approved semantics
- non-scope explicit
- logical dependencies visible
- no opportunistic refactor hidden

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- approved intent ambiguous
- critical technical source missing
- plan would require unapproved architecture/domain change

## Escalation Conditions

- new durable decision required

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-implementation-plan.md =====


---

## VIRTUAL FILE 26/45 — `skills/create-pdr.md`

**Virtual path:** `skills/create-pdr.md`  
**Content checksum:** `2218d5d766ad`

===== BEGIN VIRTUAL FILE: skills/create-pdr.md =====

# Skill — create-pdr

**ID:** SKL-CREATE-PDR  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-PDR
name: create-pdr
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Record a product decision using the project PDR convention after valid Product authority exists.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved/delegated product decision
- decision context
- alternatives/consequences
- PDR standard

## Outputs

- DECISION_RECORD_DRAFT / PDR

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Product contracts
- related research/specs/decisions

## Optional Source Classes

- analytics evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `decision-record write capability if authorized`

This declaration does not grant permissions.

## Applicable Roles

- Product

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm Product decision scope and authority.
2. Capture problem/context.
3. Record alternatives/trade-offs.
4. Record decision and consequences.
5. Link superseded/refined product decisions.
6. Return PDR artifact.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- scope belongs to Product authority
- evidence/proposal distinguished
- consequences explicit

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- decision not approved
- scope belongs to another owner
- canonical conflict

## Escalation Conditions

- cross-owner decision unresolved

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-pdr.md =====


---

## VIRTUAL FILE 27/45 — `skills/create-rfc.md`

**Virtual path:** `skills/create-rfc.md`  
**Content checksum:** `5c8d798f0911`

===== BEGIN VIRTUAL FILE: skills/create-rfc.md =====

# Skill — create-rfc

**ID:** SKL-CREATE-RFC  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `specification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-CREATE-RFC
name: create-rfc
version: 1.0.0
status: ACTIVE
category: specification
```

## Purpose

Produce a structured proposal for a material design/architecture/technical change requiring review before decision.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- problem statement
- constraints
- alternatives/evidence
- RFC standard

## Outputs

- PROPOSAL: RFC draft

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant canonical contracts and decisions

## Optional Source Classes

- benchmarks
- research
- incident evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`
- `analysis`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `document-write capability if authorized`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Domain
- Security
- Product
- Design System

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. State problem and decision scope.
2. Record constraints and non-goals.
3. Develop credible alternatives including status quo where meaningful.
4. Compare trade-offs and risks.
5. State recommendation as proposal, not approved decision.
6. Record open questions and required authorities.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- alternatives genuine
- trade-offs explicit
- authority not assumed
- proposal clearly separated from decision

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- decision scope owner unknown
- insufficient alternatives/evidence
- conflicting canonical constraints

## Escalation Conditions

- proposal requires protected human/security authority

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/create-rfc.md =====


---

## VIRTUAL FILE 28/45 — `skills/implement-change.md`

**Virtual path:** `skills/implement-change.md`  
**Content checksum:** `176fb63c1cd6`

===== BEGIN VIRTUAL FILE: skills/implement-change.md =====

# Skill — implement-change

**ID:** SKL-IMPLEMENT-CHANGE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact, write-regression-test


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-IMPLEMENT-CHANGE
name: implement-change
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Execute one bounded approved implementation change while preserving scope and authoritative contracts.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- approved Change Plan segment
- authoritative context
- current implementation/tests

## Outputs

- IMPLEMENTATION_CHANGE plus implementation evidence references

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant Product/Domain/Architecture/API/Engineering/UX/Design/Security contracts

## Optional Source Classes

- related decisions
- existing tests

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository read/write`
- `test/lint/build capabilities as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `code-write capabilities externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Implementer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm bounded intention/non-scope.
2. Inspect existing implementation and tests.
3. Make the minimum coherent change satisfying the approved contract.
4. Update/add tests appropriate to the change.
5. Run relevant checks through available interfaces.
6. Report unexpected required scope/semantic changes instead of silently adopting them.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- approved intent satisfied
- scope preserved
- unrelated refactor excluded
- tests/checks appropriate
- unknowns/escalations explicit

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- plan conflicts with canonical source
- required scope expands materially
- tool/test capability unavailable

## Escalation Conditions

- new domain/product/architecture/security decision required
- protected permission needed

## Dependencies

- `OPTIONALLY_USES analyze-impact`
- `OPTIONALLY_USES write-regression-test`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`
- `write-regression-test`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/implement-change.md =====


---

## VIRTUAL FILE 29/45 — `skills/prepare-release.md`

**Virtual path:** `skills/prepare-release.md`  
**Content checksum:** `cd8df0a40d51`

===== BEGIN VIRTUAL FILE: skills/prepare-release.md =====

# Skill — prepare-release

**ID:** SKL-PREPARE-RELEASE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `operations`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-PREPARE-RELEASE
name: prepare-release
version: 1.0.0
status: ACTIVE
category: operations
```

## Purpose

Prepare a bounded release package/readiness set from an already selected release candidate without owning deployment Workflow sequencing.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- release candidate reference
- release requirements
- change/release notes inputs

## Outputs

- RELEASE_PREPARATION: release notes/checklist/artifact references/readiness gaps

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Operations/Release contracts
- Change/Decision records
- migration/runbook contracts

## Optional Source Classes

- CI/evidence summaries

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/artifact read`
- `document write`
- `build artifact inspection as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `release-preparation capabilities; deploy permission not implied`

This declaration does not grant permissions.

## Applicable Roles

- DevOps / SRE
- Implementer
- Documentation Guardian

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify release candidate and externally required release artifacts.
2. Assemble notes/migration/rollback references.
3. Check presence of required preparation items.
4. Report readiness gaps.
5. Do not deploy, merge, or define release gates/order.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- candidate/version unambiguous
- known migrations/rollback references surfaced
- no deployment authority assumed

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- release candidate unclear
- required operational source missing

## Escalation Conditions

- migration/rollback/security requirement unresolved

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/prepare-release.md =====


---

## VIRTUAL FILE 30/45 — `skills/qa-validation.md`

**Virtual path:** `skills/qa-validation.md`  
**Content checksum:** `c23da1fdc7dd`

===== BEGIN VIRTUAL FILE: skills/qa-validation.md =====

# Skill — qa-validation

**ID:** SKL-QA-VALIDATION  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** INTERFACE_SKILL  
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-QA-VALIDATION
name: qa-validation
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Exercise intended behavior against acceptance/user/regression scenarios and return observations/evidence for the external QA verdict model.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- acceptance intent/spec
- build/change under test
- QA scope
- UPOS-007 evidence/verdict interface

## Outputs

- QA_OBSERVATION / evidence references for QAResult

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Feature/Product Contract
- bug reproduction
- risk/user scenarios
- relevant UX/API contracts

## Optional Source Classes

- test suite results
- historical regressions

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `application/test execution`
- `logs/screenshots as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `test environment access externally granted`

This declaration does not grant permissions.

## Applicable Roles

- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Derive scenarios from authoritative acceptance/bug/risk context.
2. Exercise happy, negative and relevant edge paths.
3. Record observed results and reproducible evidence.
4. Separate observation from externally owned QA verdict semantics.
5. Report blocked coverage explicitly.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- scenario coverage tied to contract/risk
- evidence attributable
- blocked areas visible
- does not equal 'tests passed'

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- environment unavailable
- acceptance contract missing
- test data/access unavailable

## Escalation Conditions

- material behavior ambiguous
- required protected access unavailable

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/qa-validation.md =====


---

## VIRTUAL FILE 31/45 — `skills/reconcile-documentation.md`

**Virtual path:** `skills/reconcile-documentation.md`  
**Content checksum:** `14303782acd6`

===== BEGIN VIRTUAL FILE: skills/reconcile-documentation.md =====

# Skill — reconcile-documentation

**ID:** SKL-RECONCILE-DOCUMENTATION  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `governance`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-RECONCILE-DOCUMENTATION
name: reconcile-documentation
version: 1.0.0
status: ACTIVE
category: governance
```

## Purpose

Identify documentation impact of a bounded change and update/propose updates to the correct canonical owners without redefining project truth.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/spec/decision
- documentation Source-of-Truth map
- documentation impact scope

## Outputs

- DOCUMENTATION_CHANGE and/or DOCUMENTATION_IMPACT_REPORT

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- UPOS-01 documentation governance
- affected canonical documents

## Optional Source Classes

- diff/PR evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `document read/write`
- `search`
- `link validation`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `document-write if externally authorized`

This declaration does not grant permissions.

## Applicable Roles

- Documentation Guardian
- Implementer
- Product
- Architecture

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify changed fact scopes/contracts.
2. Resolve canonical documentation owners via UPOS-01.
3. Update only owned/authorized documentation or produce proposed changes.
4. Preserve provenance/supersession links.
5. Report unresolved doc-vs-code conflicts rather than choosing silently.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- canonical owner targeted
- no duplicated truth introduced
- temporary/current state not injected into stable truth
- conflicts visible

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- canonical owner cannot be resolved
- active normative docs conflict
- write authority unavailable

## Escalation Conditions

- product/domain/architecture meaning is ambiguous

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/reconcile-documentation.md =====


---

## VIRTUAL FILE 32/45 — `skills/reproduce-bug.md`

**Virtual path:** `skills/reproduce-bug.md`  
**Content checksum:** `cdcf90870a70`

===== BEGIN VIRTUAL FILE: skills/reproduce-bug.md =====

# Skill — reproduce-bug

**ID:** SKL-REPRODUCE-BUG  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `analysis`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REPRODUCE-BUG
name: reproduce-bug
version: 1.0.0
status: ACTIVE
category: analysis
```

## Purpose

Produce a controlled, evidence-backed reproduction of an observed defect or explicitly report that reproduction was not achieved.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- bug report/symptom
- environment/context
- expected behavior contract

## Outputs

- EVIDENCE/ANALYSIS: reproducible steps/fixture and observed vs expected result, or NOT_REPRODUCED result

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant feature/API/domain/test contracts

## Optional Source Classes

- logs
- incident evidence
- prior regressions

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `runtime/test execution as available`
- `repository read`
- `logs/search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `test/runtime access as externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Implementer
- Reviewer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Define expected behavior from canonical source.
2. Isolate minimal reproduction conditions.
3. Execute/observe without altering production truth.
4. Capture deterministic steps/inputs/evidence where possible.
5. Separate reproduction from root-cause hypothesis.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- expected vs observed explicit
- reproduction evidence attributable
- no false certainty when non-reproducible

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- environment unavailable
- expected behavior unspecified
- non-deterministic reproduction

## Escalation Conditions

- cannot establish expected contract
- reproduction needs protected production access

## Dependencies

- `None`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- None

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/reproduce-bug.md =====


---

## VIRTUAL FILE 33/45 — `skills/review-architecture.md`

**Virtual path:** `skills/review-architecture.md`  
**Content checksum:** `ede584b40fe3`

===== BEGIN VIRTUAL FILE: skills/review-architecture.md =====

# Skill — review-architecture

**ID:** SKL-REVIEW-ARCHITECTURE  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REVIEW-ARCHITECTURE
name: review-architecture
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Evaluate a proposed/implemented change for conformance with canonical architecture contracts and decision boundaries.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/RFC/diff
- canonical architecture context
- review scope

## Outputs

- ANALYSIS/REVIEW_FINDING candidates tagged architecture

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Master Architecture
- ADRs
- Domain ownership boundaries
- relevant NFRs

## Optional Source Classes

- implementation diff
- performance/security evidence

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `diagram/search`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read/review capability`

This declaration does not grant permissions.

## Applicable Roles

- Architecture
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify architecture contracts affected.
2. Check boundary/ownership/data-flow/integration conformance.
3. Detect new durable decisions hidden in implementation.
4. Separate architecture violations from optional improvements.
5. Return evidence-backed findings/proposals.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- canonical architecture referenced
- new boundary decisions surfaced
- no Product/Domain authority assumption

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- architecture source unresolved
- change requires architecture decision not yet made

## Escalation Conditions

- material architecture conflict or missing ADR/RFC decision

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/review-architecture.md =====


---

## VIRTUAL FILE 34/45 — `skills/review-diff.md`

**Virtual path:** `skills/review-diff.md`  
**Content checksum:** `df4ad1872d15`

===== BEGIN VIRTUAL FILE: skills/review-diff.md =====

# Skill — review-diff

**ID:** SKL-REVIEW-DIFF  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REVIEW-DIFF
name: review-diff
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Perform a bounded technical review of a change diff against authoritative contracts and externally owned quality semantics.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- diff/change artifacts
- authoritative context
- review scope/dimensions
- UPOS-007 review/evidence interface

## Outputs

- REVIEW_FINDING candidates / structured review analysis for UPOS-007 verdict semantics

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant Product/Domain/Architecture/Engineering/Security/UX/Quality contracts

## Optional Source Classes

- tests/CI evidence
- Change Plan

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `diff/repository inspection`
- `search`
- `test-result read`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `read/review capability externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Reviewer
- Architecture
- Security
- Domain
- UX / Product Design
- Design System

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Confirm review scope and independence requirements from upstream contracts.
2. Read authoritative expectations before judging implementation.
3. Inspect changed behavior and relevant neighboring code.
4. Identify concrete defects/risks with evidence and owner dimension.
5. Return structured findings without issuing unauthorized final verdict semantics.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- findings specific/evidence-backed
- scope-aware
- no style-only noise presented as blocking
- authority boundaries preserved

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- required context/evidence missing
- review independence invalid
- diff too broad to review reliably

## Escalation Conditions

- blocking uncertainty
- scope/authority conflict
- quality system requires additional gate

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/review-diff.md =====


---

## VIRTUAL FILE 35/45 — `skills/review-security.md`

**Virtual path:** `skills/review-security.md`  
**Content checksum:** `e01ae56b789e`

===== BEGIN VIRTUAL FILE: skills/review-security.md =====

# Skill — review-security

**ID:** SKL-REVIEW-SECURITY  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analyze-impact


**Disposition:** INTERFACE_SKILL  
**Category:** `verification`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-REVIEW-SECURITY
name: review-security
version: 1.0.0
status: ACTIVE
category: verification
```

## Purpose

Assess a bounded change for security risks and contract conformance using externally owned Security authority/policy.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- change/diff/design
- security context
- threat/review scope
- UPOS-010/07 interfaces

## Outputs

- ANALYSIS/REVIEW_FINDING candidates tagged security

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- Security/Privacy contracts
- Auth/AuthZ rules
- data classification
- relevant architecture

## Optional Source Classes

- scanner output
- threat model
- incident history

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository/document read`
- `security scanner results as available`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `security review/read capabilities`

This declaration does not grant permissions.

## Applicable Roles

- Security
- Reviewer

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Identify protected/security-relevant surfaces.
2. Compare behavior against canonical security constraints.
3. Analyze abuse/misuse/privilege/data exposure paths.
4. Validate scanner findings rather than blindly trust/suppress them.
5. Return scoped evidence-backed findings; veto/approval semantics remain external.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- security scope explicit
- findings actionable/evidence-backed
- false certainty avoided
- no permission/veto policy invented

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- security source unavailable
- protected evidence inaccessible
- scope exceeds bounded review

## Escalation Conditions

- potential material vulnerability
- required Security authority decision

## Dependencies

- `OPTIONALLY_USES analyze-impact`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `analyze-impact`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/review-security.md =====


---

## VIRTUAL FILE 36/45 — `skills/write-regression-test.md`

**Virtual path:** `skills/write-regression-test.md`  
**Content checksum:** `259b2c0f4764`

===== BEGIN VIRTUAL FILE: skills/write-regression-test.md =====

# Skill — write-regression-test

**ID:** SKL-WRITE-REGRESSION-TEST  
**Type:** SKILL CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** reproduce-bug


**Disposition:** CANONICAL_UNIVERSAL_SKILL  
**Category:** `implementation`  
**Lifecycle:** ACTIVE  
**Version:** 1.0.0

## Identity

```text
skill_id: SKL-WRITE-REGRESSION-TEST
name: write-regression-test
version: 1.0.0
status: ACTIVE
category: implementation
```

## Purpose

Create a focused automated test that proves a known defect/contract regression and protects the corrected behavior.

## Scope

This contract owns the reusable bounded procedure described below.

## Non-scope

This Skill does not grant organizational authority and does not redefine Workflow sequencing, Context retrieval semantics, quality verdict semantics, permission grants, project/provider bindings, or canonical project truth.

## Inputs

- reproduction/evidence
- expected behavior contract
- test framework interface

## Outputs

- TEST_CHANGE: focused regression test(s)

## Preconditions

- invoking Agent Run has a Role/Agent Definition allowed to use this capability;
- required authority remains valid under UPOS-002;
- required Source Classes can be resolved or the Skill escalates;
- required tool/permission interfaces are available or failure is explicit.

## Postconditions

On nominal completion, the declared Skill Result exists and is attributable to this Skill ID/version and invocation context.

Completion does not imply canonical knowledge promotion or downstream Workflow success.

## Required Source Classes

- relevant behavior/test/engineering contracts

## Optional Source Classes

- existing neighboring tests

## Required Context Interface

Context is requested/resolved through UPOS-005 and UPOS-01 Source-of-Truth governance. Physical project paths are not part of this universal contract.

## Tool Interface Requirements

- `repository read/write`
- `test execution`

Concrete providers/tools are bound by UPOS-011.

## Permission Interface Requirements

- `code/test write as externally granted`

This declaration does not grant permissions.

## Applicable Roles

- Implementer
- Reviewer
- QA

Applicable Role means capability compatibility only:

```text
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
```

## Applicable Work / Risk Constraints

Any risk/change-class restrictions are consumed by reference from UPOS-004/010. This Skill does not define C0–C5 or human-gate policy.

## Procedure

1. Translate the reproduced contract violation into a deterministic assertion.
2. Choose the narrowest appropriate test layer.
3. Make the test fail for the defect when safely verifiable.
4. Avoid overspecifying unrelated implementation details.
5. Run relevant test evidence through external quality tooling.

## Procedural Invariants

- preserve bounded Skill purpose;
- preserve authority/source boundaries;
- never fabricate required project truth;
- do not silently expand into a multi-role Workflow;
- return controlled failure/escalation when a required interface is unavailable.

## Quality Criteria

- test protects behavior, not accident
- failure mode represented
- test is maintainable and scoped

## Validation Requirements

Validation SHOULD demonstrate observable conformance to the criteria above. Evidence/verdict semantics remain with UPOS-007 and telemetry with UPOS-008.

## Failure Modes

- defect not reproducible
- test layer cannot observe contract
- expected behavior ambiguous

## Escalation Conditions

- test requires architectural seam/change outside scope

## Dependencies

- `OPTIONALLY_USES reproduce-bug`

Dependency relations do not define Workflow ordering.

## Composition Rules

May be composed only through explicit compatible contracts. Cross-role sequencing belongs to UPOS-004.

## Prohibited Behavior

- using this Skill as authority the invoking Role does not possess;
- hard-coding project paths/providers;
- silently promoting result to canonical truth;
- redefining downstream owner semantics;
- hiding a full cross-role Workflow inside the Skill.

## Lifecycle

`DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Invocation execution state is external.

## Version

`1.0.0`

Material behavior changes follow `SKILL_VERSIONING.md`.

## Related Skills

- `reproduce-bug`

## Replacement / Supersession

None in v1.0.

===== END VIRTUAL FILE: skills/write-regression-test.md =====


---

## VIRTUAL FILE 37/45 — `templates/SKILL_CONTRACT_TEMPLATE.md`

**Virtual path:** `templates/SKILL_CONTRACT_TEMPLATE.md`  
**Content checksum:** `6ae7949224f4`

===== BEGIN VIRTUAL FILE: templates/SKILL_CONTRACT_TEMPLATE.md =====

# Skill Contract Template

**ID:** UPOS-03-TPL-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Skill — <canonical-name>

**ID:** <stable skill id>
**Type:** SKILL CONTRACT
**Status:** <DRAFT|REVIEW|APPROVED|ACTIVE|DEPRECATED|RETIRED>
**Normativity:** NORMATIVE
**Owner:** UPOS-003 Skills System
**Version:** <semver>
**Lifetime:** STABLE

**Disposition:** <CANONICAL_UNIVERSAL_SKILL|INTERFACE_SKILL>
**Category:** <classification|planning|analysis|specification|implementation|verification|governance|operations>

## Identity

## Purpose

## Scope

## Non-scope

## Inputs

## Outputs

## Preconditions

## Postconditions

## Required Source Classes

## Optional Source Classes

## Required Context Interface

## Tool Interface Requirements

## Permission Interface Requirements

## Applicable Roles

## Applicable Work / Risk Constraints

## Procedure

## Procedural Invariants

## Quality Criteria

## Validation Requirements

## Failure Modes

## Escalation Conditions

## Dependencies

## Composition Rules

## Prohibited Behavior

## Lifecycle

## Version

## Related Skills

## Replacement / Supersession
```

===== END VIRTUAL FILE: templates/SKILL_CONTRACT_TEMPLATE.md =====


---

## VIRTUAL FILE 38/45 — `analysis/AMBIGUITY_GAP_REGISTER.md`

**Virtual path:** `analysis/AMBIGUITY_GAP_REGISTER.md`  
**Content checksum:** `cc7574fd6c02`

===== BEGIN VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

# UPOS-003 Ambiguity & Gap Register

**ID:** UPOS-03-AN-005  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


| ID | Issue | Module-03 resolution | Deferred owner | Status |
|---|---|---|---|---|
| G03-001 | Skill vs Workflow | Bounded reusable procedure remains Skill; cross-role order/gates/routing remain UPOS-004. | UPOS-004 | CLOSED |
| G03-002 | Skill vs Agent Process | Reusable procedure is extracted from old Agent `Process`; Agent keeps organizational invariants/interfaces. | UPOS-002 | CLOSED |
| G03-003 | Skill vs Context Assembly | Skill may request/organize context but retrieval/freshness/budget/memory remain UPOS-005. | UPOS-005 | CLOSED |
| G03-004 | Skill vs Quality Procedure | Skill-level procedure/criteria are allowed; evidence/verdict/gate semantics remain UPOS-007. | UPOS-007 | CLOSED |
| G03-005 | Skill vs Tool | Skill may require abstract capabilities; concrete tools/providers remain adapters. | UPOS-011 | CLOSED |
| G03-006 | Skill vs Permission | Skill declares capability requirement but cannot grant permission. | UPOS-010 | CLOSED |
| G03-007 | Skill vs Policy | Skill consumes policy and cannot redefine allowed/required/forbidden organization-wide behavior. | UPOS-004/06/07/10 | CLOSED |
| G03-008 | Skill vs Learning | Skill can create Learning Candidate or be evolution target; detection/promotion remain UPOS-009/01. | UPOS-009 + UPOS-01 | CLOSED |
| G03-009 | Skill vs project adapter | Universal Skill Contract uses abstract sources/tools and no project paths/providers. | UPOS-011 | CLOSED |
| G03-010 | Definition vs Invocation | Definition lifecycle/version is Module 03; invocation runtime state/event is deferred. | UPOS-004/08/schemas | CLOSED |
| G03-011 | Dependency vs sequencing | Dependency expresses capability relationship, not Workflow order. | UPOS-004 | CLOSED |
| G03-012 | prepare-release breadth | Bounded to preparation/readiness artifacts; deploy/release sequencing excluded. | UPOS-004/06/10 | CLOSED |
| G03-013 | implement-change breadth | Bounded to one approved Change Plan segment; feature lifecycle remains Workflow. | UPOS-004/06 | CLOSED |
| G03-014 | Schema/runtime representation | Machine form deferred to cross-cutting schemas/runtime; Markdown remains normative. | cross-cutting schemas/runtime | CLOSED |

## Result

No unresolved P0/P1 Module-03 semantic gap remains at v1.0 freeze.

===== END VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====


---

## VIRTUAL FILE 39/45 — `analysis/IMPLEMENTATION_PLAN.md`

**Virtual path:** `analysis/IMPLEMENTATION_PLAN.md`  
**Content checksum:** `d4125f5855a2`

===== BEGIN VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

# UPOS-003 Implementation Plan

**ID:** UPOS-03-AN-007  
**Type:** IMPLEMENTATION PLAN / EVIDENCE  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Logical implementation sequence

1. establish Skills System scope/non-scope and identity model;
2. define Skill Contract;
3. define taxonomy and Registry;
4. define lifecycle/versioning;
5. define dependencies/composition;
6. define evaluation/evolution interfaces;
7. classify frozen starter candidates;
8. implement accepted Skill Contracts;
9. define cross-module interfaces/template;
10. complete traceability and validation.

## Expected logical commits

```text
docs(upos-003): establish skills system boundary
docs(upos-003): define skill contract and identity model
docs(upos-003): define taxonomy and registry
docs(upos-003): define skill lifecycle and versioning
docs(upos-003): define dependency and composition rules
docs(upos-003): define skill evaluation and evolution interfaces
docs(upos-003): add universal skill contracts
docs(upos-003): add templates and cross-module interfaces
docs(upos-003): complete source traceability audit
```

## Non-scope

No runtime, schemas, workflow engine, Git engine, QA engine, permissions engine, telemetry engine, learning engine, or project adapter is implemented here.

===== END VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====


---

## VIRTUAL FILE 40/45 — `analysis/MODULE_03_OWNERSHIP_MAP.md`

**Virtual path:** `analysis/MODULE_03_OWNERSHIP_MAP.md`  
**Content checksum:** `90adecf1be88`

===== BEGIN VIRTUAL FILE: analysis/MODULE_03_OWNERSHIP_MAP.md =====

# Module 03 Ownership Map

**ID:** UPOS-03-AN-002  
**Type:** ANALYSIS / BOUNDARY MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Owns

- Skill identity/definition;
- versioned Skill Contract;
- bounded procedure;
- inputs/outputs/preconditions;
- source/context/tool/permission interface requirements;
- applicable Role compatibility;
- procedural invariants;
- Skill-level quality criteria;
- failure/escalation;
- dependencies/composition;
- registry/taxonomy/discovery;
- lifecycle/versioning/deprecation/supersession;
- Skill evaluation;
- Skill evolution interface;
- universal Skill library.

## Does not own

| Concern | Owner |
|---|---|
| Roles/authority/SoD | UPOS-002 |
| Workflow/routing/C0-C5/retry | UPOS-004 |
| Retrieval/context/memory | UPOS-005 |
| Git/PR/merge policy | UPOS-006 |
| Evidence/verdict/gates | UPOS-007 |
| Telemetry/metrics | UPOS-008 |
| Learning detection/promotion | UPOS-009 + UPOS-01 |
| Permissions/protected actions | UPOS-010 |
| Provider/project bindings | UPOS-011 |

## Boundary test

A rule belongs to Module 03 when its central question is:

```text
What reusable bounded capability exists?
What inputs/outputs/preconditions/procedure define it?
How is it versioned/discovered/evaluated/composed?
```

It does not belong when the central question is:

```text
Who has authority?
Which step runs next?
How is context retrieved?
What is a valid PR/merge?
What evidence verdict blocks merge?
Who gets permission?
Which provider/path implements it?
```

===== END VIRTUAL FILE: analysis/MODULE_03_OWNERSHIP_MAP.md =====


---

## VIRTUAL FILE 41/45 — `analysis/PROPOSED_PACKAGE_TREE.md`

**Virtual path:** `analysis/PROPOSED_PACKAGE_TREE.md`  
**Content checksum:** `f5ab8ca06bbf`

===== BEGIN VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

# Proposed Package Tree

**ID:** UPOS-03-AN-006  
**Type:** ANALYSIS / PACKAGE DESIGN  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


```text
03_skills_system/
├── README.md
├── SKILLS_OPERATING_MODEL.md
├── SKILL_CONTRACT_STANDARD.md
├── SKILL_REGISTRY_STANDARD.md
├── SKILL_TAXONOMY.md
├── SKILL_LIFECYCLE.md
├── SKILL_VERSIONING.md
├── SKILL_DEPENDENCY_AND_COMPOSITION.md
├── SKILL_EVALUATION_STANDARD.md
├── SKILL_EVOLUTION_INTERFACE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_03_DEFINITION_OF_DONE.md
├── MODULE_03_TRACEABILITY.md
├── skills/
│   ├── classify-change.md
│   ├── assemble-context.md
│   ├── analyze-impact.md
│   ├── create-feature-spec.md
│   ├── create-rfc.md
│   ├── create-adr.md
│   ├── create-pdr.md
│   ├── create-ddr.md
│   ├── create-implementation-plan.md
│   ├── reproduce-bug.md
│   ├── write-regression-test.md
│   ├── implement-change.md
│   ├── create-atomic-commit.md
│   ├── review-diff.md
│   ├── review-architecture.md
│   ├── review-security.md
│   ├── qa-validation.md
│   ├── reconcile-documentation.md
│   ├── assess-merge-readiness.md
│   ├── prepare-release.md
│   ├── analyze-incident.md
│   ├── capture-learning.md
├── templates/
│   └── SKILL_CONTRACT_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_03_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── SKILL_CANDIDATE_CLASSIFICATION.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── TRACEABILITY_VALIDATION.md
```

The structure separates canonical standards, individual Skill Contracts, reusable template, and historical implementation/audit evidence.

===== END VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====


---

## VIRTUAL FILE 42/45 — `analysis/SKILL_CANDIDATE_CLASSIFICATION.md`

**Virtual path:** `analysis/SKILL_CANDIDATE_CLASSIFICATION.md`  
**Content checksum:** `1044be649383`

===== BEGIN VIRTUAL FILE: analysis/SKILL_CANDIDATE_CLASSIFICATION.md =====

# Skill Candidate Classification

**ID:** UPOS-03-AN-004  
**Type:** ANALYSIS / CANDIDATE CLASSIFICATION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** ../SKILL_REGISTRY_STANDARD.md

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Classification vocabulary

```text
CANONICAL_UNIVERSAL_SKILL
INTERFACE_SKILL
SHOULD_SPLIT
DEFERRED_TO_OTHER_MODULE
PROJECT_SPECIFIC
REDUNDANT
```

## Results

| Candidate | Disposition | Primary category | Rationale |
|---|---|---|---|
| `classify-change` | INTERFACE_SKILL | `classification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `assemble-context` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `analyze-impact` | CANONICAL_UNIVERSAL_SKILL | `analysis` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-feature-spec` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-rfc` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-adr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-pdr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-ddr` | CANONICAL_UNIVERSAL_SKILL | `specification` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-implementation-plan` | CANONICAL_UNIVERSAL_SKILL | `planning` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `reproduce-bug` | CANONICAL_UNIVERSAL_SKILL | `analysis` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `write-regression-test` | CANONICAL_UNIVERSAL_SKILL | `implementation` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `implement-change` | CANONICAL_UNIVERSAL_SKILL | `implementation` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `create-atomic-commit` | INTERFACE_SKILL | `implementation` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-diff` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-architecture` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `review-security` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `qa-validation` | INTERFACE_SKILL | `verification` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `reconcile-documentation` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `assess-merge-readiness` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `prepare-release` | INTERFACE_SKILL | `operations` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |
| `analyze-incident` | CANONICAL_UNIVERSAL_SKILL | `operations` | Bounded reusable capability has independent semantic value across projects and can be evaluated without owning a cross-role Workflow. |
| `capture-learning` | INTERFACE_SKILL | `governance` | Reusable bounded semantic procedure is useful, but authoritative classification/context/Git/quality/learning/release semantics remain with another module. |

## Summary

- `CANONICAL_UNIVERSAL_SKILL`: 11
- `INTERFACE_SKILL`: 11
- `SHOULD_SPLIT`: 0
- `DEFERRED_TO_OTHER_MODULE`: 0 among the frozen starter candidates
- `PROJECT_SPECIFIC`: 0
- `REDUNDANT`: 0

No candidate was accepted mechanically. Interface Skills were deliberately bounded so they do not steal downstream ownership.

===== END VIRTUAL FILE: analysis/SKILL_CANDIDATE_CLASSIFICATION.md =====


---

## VIRTUAL FILE 43/45 — `analysis/SOURCE_ANALYSIS.md`

**Virtual path:** `analysis/SOURCE_ANALYSIS.md`  
**Content checksum:** `9922ff674add`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

# UPOS-003 Source Analysis

**ID:** UPOS-03-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** ../MODULE_03_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Sources

1. UPOS-01 Documentation System / Source-of-Truth / Knowledge Lifecycle — active upstream governance.
2. UPOS-002 Agent Organization v1.0 — frozen organizational contract.
3. `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md` — frozen master design input.

**Frozen SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`

## Direct Skill-owned source

Primary frozen sections:

- §19 Skills model
- §20 Skill contract
- §21 Example universal skills
- §105 Skill evolution
- §184 Skill versioning
- Appendix C Skill template

## Mixed Skill-related source

Additional Skill semantics appear in:

- Core terminology;
- Agent Contract `Skills` / `Process`;
- Workflow required skills;
- organizational learning;
- repository layout/adoption examples;
- observability skill identity;
- technical-debt/incident learning signals;
- governance health/deprecation checks;
- final operating model.

These are extracted only where they define Skills. Other semantics remain deferred.

## Key decomposition decision

The old Agent Contract `Process` field does not make Agent Organization owner of reusable procedure.

Reusable bounded procedure is owned by UPOS-003.

Cross-role sequence remains UPOS-004.

===== END VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====


---

## VIRTUAL FILE 44/45 — `analysis/SOURCE_SECTION_DISPOSITION.md`

**Virtual path:** `analysis/SOURCE_SECTION_DISPOSITION.md`  
**Content checksum:** `09de95222e64`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

# Source Section Disposition

**ID:** UPOS-03-AN-003  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** ../MODULE_03_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


**Frozen structural sections inspected:** 317  
**Direct Module-03 sections:** 5  
**Mixed Skill-related sections:** 24

| Source unit | Line | Section | Disposition | Destination |
|---|---:|---|---|---|
| SRC-001 | 17 | 0. Executive model | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-002 | 86 | 1. Relationship to the Documentation Operating Model | OUTSIDE_MODULE_03 | UPOS-01 |
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
| SRC-015 | 345 | 3.11 Risk-based governance | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-016 | 353 | 3.12 Organizational learning over hidden memory | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-017 | 371 | 4. Core terminology | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-018 | 373 | Agent | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-019 | 377 | Skill | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-020 | 391 | Workflow | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-021 | 404 | Orchestrator | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-022 | 408 | Guardrail | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-023 | 412 | Gate | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-024 | 416 | Handoff | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-025 | 420 | Project Memory | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-026 | 424 | Run | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-027 | 428 | Evidence | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-028 | 434 | 5. Universal Agent Contract | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-029 | 497 | 6. Agent identity is not enough | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-030 | 521 | 7. Universal role families | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-031 | 559 | 8. Orchestrator | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-032 | 561 | Mission | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-033 | 565 | Responsibilities | DEFERRED_TO_MODULE | UPOS-02 |
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
| SRC-045 | 851 | 19. Skills model | EXTRACTED_TO_MODULE_03 | Module 03 normative package |
| SRC-046 | 870 | 20. Skill contract | EXTRACTED_TO_MODULE_03 | Module 03 normative package |
| SRC-047 | 902 | 21. Example universal skills | EXTRACTED_TO_MODULE_03 | Module 03 normative package |
| SRC-048 | 933 | 22. Workflow contract | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-04 |
| SRC-049 | 954 | 23. Change classification | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-050 | 971 | 24. C0 — Micro | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-051 | 996 | 25. C1 — Small | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-052 | 1018 | 26. C2 — Standard Feature | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-053 | 1043 | 27. C3 — Cross-cutting | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-054 | 1070 | 28. C4 — Architectural | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-055 | 1097 | 29. C5 — High-risk | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-056 | 1128 | 30. Risk override rule | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-057 | 1144 | 31. Context assembly | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-058 | 1165 | 32. Context assembly order | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-059 | 1182 | 33. Context budget principle | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-060 | 1198 | 34. Memory model | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-061 | 1215 | 35. Project memory sources | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-062 | 1235 | 36. Learning is not hidden model training | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-063 | 1257 | 37. Learning promotion model | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-064 | 1290 | 38. Permissions model | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-065 | 1317 | 39. Default role permission philosophy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-066 | 1319 | Orchestrator | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-067 | 1330 | Implementer | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-068 | 1342 | Reviewer | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-069 | 1353 | QA | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-070 | 1362 | Merge Controller | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-071 | 1374 | 40. Human approval model | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-072 | 1391 | 41. Recommended adoption mode | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-073 | 1411 | 42. Planning model | DEFERRED_TO_MODULE | UPOS-06 |
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
| SRC-086 | 1601 | 53. Good PR | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-087 | 1624 | 54. Bad PR | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-088 | 1640 | 55. PR size policy | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-089 | 1656 | 56. PR description contract | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-090 | 1692 | 57. Creation loop | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-091 | 1707 | 58. Verification loop | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-092 | 1723 | 59. Self-check | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-093 | 1741 | 60. Independent review protocol | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-094 | 1758 | 61. Review finding severity | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-095 | 1778 | 62. Review output contract | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-096 | 1815 | 63. Reviewer independence | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-097 | 1831 | 64. QA protocol | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-098 | 1847 | 65. QA dimensions | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-099 | 1868 | 66. Documentation gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-100 | 1886 | 67. Architecture gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-101 | 1903 | 68. Security gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-102 | 1920 | 69. Database migration gate | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-103 | 1935 | 70. Merge readiness | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-104 | 1949 | 71. Merge authority | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-105 | 1966 | 72. Merge strategy | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-106 | 1982 | 73. Handoff protocol | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-107 | 2027 | 74. Handoff context minimization | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-108 | 2042 | 75. Guardrails | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-109 | 2058 | 76. Guardrail types | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-110 | 2070 | 77. Escalation model | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-111 | 2087 | 78. Escalation targets | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-112 | 2101 | 79. Failure and recovery | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-113 | 2119 | 80. Retry policy | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-114 | 2137 | 81. Scope Guardian | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-115 | 2158 | 82. Concurrency model | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-116 | 2182 | 83. Task isolation | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-117 | 2202 | 84. Shared file collision | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-118 | 2216 | 85. Workflow — Micro Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-119 | 2237 | 86. Workflow — Bug Fix | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-120 | 2255 | 87. Workflow — New Feature | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-121 | 2276 | 88. Workflow — UI Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-122 | 2292 | 89. Workflow — Design System Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-123 | 2308 | 90. Workflow — Architecture Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-124 | 2326 | 91. Workflow — API Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-125 | 2341 | 92. Workflow — Database Migration | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-126 | 2357 | 93. Workflow — Security Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-127 | 2372 | 94. Workflow — Refactor | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-128 | 2387 | 95. Workflow — Dependency Upgrade | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-129 | 2401 | 96. Workflow — Hotfix | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-130 | 2421 | 97. Workflow — Documentation Change | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-131 | 2436 | 98. Workflow — Release | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-132 | 2452 | 99. Observability model | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-08 |
| SRC-133 | 2485 | 100. Dashboard-ready metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-134 | 2510 | 101. Do not optimize for activity | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-135 | 2525 | 102. Quality metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-136 | 2542 | 103. Agent performance | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-137 | 2559 | 104. Agent learning record | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-138 | 2583 | 105. Skill evolution | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-139 | 2604 | 106. Workflow evolution | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-140 | 2617 | 107. Agent contract evolution | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-141 | 2630 | 108. Model/provider independence | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-142 | 2648 | 109. Tool independence | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-143 | 2665 | 110. Safety around secrets | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-144 | 2683 | 111. Production access | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-145 | 2695 | 112. Protected files | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-146 | 2711 | 113. Definition of Ready — task | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-147 | 2730 | 114. Definition of Ready — agent execution | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-148 | 2746 | 115. Definition of Done — implementation | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-149 | 2760 | 116. Definition of Done — PR | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-150 | 2775 | 117. Definition of Done — workflow | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-151 | 2788 | 118. Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-11 |
| SRC-152 | 2864 | 119. Maturity model | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-153 | 2866 | Level 0 — Single Agent | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-154 | 2870 | Level 1 — Role Profiles | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-155 | 2874 | Level 2 — Governed Workflows | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-156 | 2878 | Level 3 — Orchestrated Team | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-157 | 2882 | Level 4 — Automated Verification | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-158 | 2886 | Level 5 — Controlled Autonomy | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-159 | 2890 | Level 6 — Learning Organization | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-160 | 2898 | 120. Recommended adoption sequence | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-161 | 2900 | Stage 1 — Documentation foundation | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-162 | 2904 | Stage 2 — Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-163 | 2908 | Stage 3 — Three roles | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-164 | 2920 | Stage 4 — Add QA and Documentation Guardian | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-165 | 2924 | Stage 5 — Add specialist agents | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-166 | 2928 | Stage 6 — Formal workflows | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-167 | 2932 | Stage 7 — Telemetry | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-168 | 2936 | Stage 8 — Limited autonomous merge | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-169 | 2942 | 121. Recommended first implementation | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-11 |
| SRC-170 | 2982 | 122. Universal Orchestrator algorithm | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-171 | 3009 | 123. Authority conflict resolution | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-172 | 3028 | 124. Security veto | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-173 | 3038 | 125. Architecture veto | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-174 | 3051 | 126. Reviewer veto | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-175 | 3072 | 127. Human override | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-176 | 3091 | 128. Agent output discipline | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-177 | 3107 | 129. Change Classification output | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-178 | 3137 | 130. Implementation Plan output | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-179 | 3174 | 131. Review Result output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-180 | 3206 | 132. QA Result output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-181 | 3232 | 133. Merge Readiness output | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-182 | 3252 | 134. Change review feedback loop | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-183 | 3266 | 135. Oversized PR handling | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-184 | 3281 | 136. Scope expansion handling | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-185 | 3298 | 137. Unplanned architecture discovery | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-186 | 3313 | 138. Unplanned product ambiguity | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-187 | 3327 | 139. Unplanned security concern | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-188 | 3333 | 140. Documentation drift detection | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-189 | 3348 | 141. Agent sandbox hygiene | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-190 | 3368 | 142. Branch lifetime | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-191 | 3376 | 143. Stacked PRs | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-192 | 3384 | 144. Feature flags | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-193 | 3399 | 145. Rollback thinking | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-194 | 3411 | 146. Dependency graph awareness | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-195 | 3429 | 147. Cost awareness | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-196 | 3439 | 148. Latency awareness | DEFERRED_TO_MODULE | UPOS-08 |
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
| SRC-211 | 3609 | 163. Technical debt review | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-06 |
| SRC-212 | 3623 | 164. Post-merge verification | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-213 | 3636 | 165. Post-merge learning trigger | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-214 | 3652 | 166. Incident integration | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-215 | 3667 | 167. Dashboard model | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-216 | 3690 | 168. Agent workload | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-217 | 3709 | 169. Workflow bottleneck analysis | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-218 | 3724 | 170. Maturity gates for autonomy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-219 | 3740 | 171. Autonomy expansion | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-220 | 3755 | 172. Project-specific overrides | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-221 | 3769 | 173. Universal vs project-specific rules | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-222 | 3791 | 174. Agent manifests should be versioned | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-223 | 3807 | 175. Governance change workflow | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-224 | 3821 | 176. Universal starter agent set | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-225 | 3846 | 177. Universal full agent set | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-226 | 3874 | 178. Agent composition | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-227 | 3896 | 179. Universal policy files | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-228 | 3913 | 180. AI Agent README | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-229 | 3927 | 181. Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-230 | 3944 | 182. Universal file naming | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-231 | 3963 | 183. Agent contract versioning | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-232 | 3975 | 184. Skill versioning | EXTRACTED_TO_MODULE_03 | Module 03 normative package |
| SRC-233 | 3981 | 185. Workflow versioning | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-234 | 3987 | 186. Telemetry retention | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-235 | 3993 | 187. Sensitive context policy | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-236 | 3999 | 188. Secret redaction | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-237 | 4005 | 189. Auditability | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-238 | 4019 | 190. Reproducibility | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-239 | 4035 | 191. Agent hallucination handling | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-240 | 4047 | 192. Missing Source of Truth | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-241 | 4060 | 193. Stale Source of Truth | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-242 | 4072 | 194. Feature lifecycle integration | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-243 | 4080 | 195. Agent lifecycle | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-244 | 4095 | 196. Task lifecycle | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-245 | 4114 | 197. PR lifecycle | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-246 | 4120 | 198. Agent run lifecycle | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-247 | 4136 | 199. Workflow state machine | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-248 | 4142 | 200. No hidden background authority | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-249 | 4148 | 201. Human pause points | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-250 | 4162 | 202. Plan change protocol | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-251 | 4174 | 203. Reclassification | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-252 | 4184 | 204. Risk inheritance | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-253 | 4190 | 205. Change decomposition | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-254 | 4196 | 206. Multi-agent code ownership | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-255 | 4202 | 207. Shared contract first | DEFERRED_TO_MODULE | UPOS-04 |
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
| SRC-266 | 4350 | 218. Change evidence bundle | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-267 | 4367 | 219. Artifact retention | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-268 | 4390 | 220. Privacy of reasoning | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-269 | 4398 | 221. Universal anti-patterns | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-270 | 4400 | 221.1 Agent swarm without ownership | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-271 | 4404 | 221.2 Self-approval | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-272 | 4408 | 221.3 Every task runs every agent | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-273 | 4412 | 221.4 Giant context dump | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-274 | 4416 | 221.5 Prompt duplication | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-275 | 4420 | 221.6 Hidden project memory | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-276 | 4424 | 221.7 Activity metrics | DEFERRED_TO_MODULE | UPOS-08 |
| SRC-277 | 4428 | 221.8 AI-created architecture by accident | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-278 | 4432 | 221.9 Fake review | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-279 | 4436 | 221.10 Git history as keystroke log | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-280 | 4442 | 222. Governance health checks | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-08 |
| SRC-281 | 4459 | 223. Quarterly / milestone review | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-282 | 4475 | 224. Universal adoption checklist | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-283 | 4494 | 225. Minimal viable agent system | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-284 | 4513 | 226. Intermediate agent system | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-285 | 4531 | 227. Advanced agent system | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-286 | 4550 | 228. Final operating model | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-287 | 4600 | Appendix A — Project Agent Manifest template | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-288 | 4679 | Appendix B — Agent Contract template | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-02 |
| SRC-289 | 4722 | Appendix C — Skill template | EXTRACTED_TO_MODULE_03 | Module 03 normative package |
| SRC-290 | 4757 | Appendix D — Workflow template | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-04 |
| SRC-291 | 4798 | Appendix E — Change Plan template | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-292 | 4832 | Appendix F — Handoff template | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-293 | 4861 | Appendix G — Review Result template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-294 | 4905 | Appendix H — QA Result template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-295 | 4929 | Appendix I — Merge Readiness template | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-296 | 4957 | Appendix J — Risk Classification Matrix | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-297 | 4970 | Appendix K — Permission Matrix example | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-298 | 4985 | Appendix L — Git Policy starter | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-299 | 5021 | Appendix M — Review Policy starter | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-300 | 5048 | Appendix N — Human Approval Policy starter | DEFERRED_TO_MODULE | UPOS-10 |
| SRC-301 | 5073 | Appendix O — Example New Feature workflow | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-302 | 5115 | Appendix P — Example Bug Fix workflow | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-303 | 5140 | Appendix Q — Example Architecture Change workflow | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-304 | 5174 | Appendix R — Learning Record template | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-09 |
| SRC-305 | 5202 | Appendix S — Telemetry schema starter | MIXED_EXTRACTED_AND_DEFERRED | Skill semantics → Module 03; remaining → UPOS-08 |
| SRC-306 | 5229 | Appendix T — Adoption directive for an existing project | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-307 | 5279 | Final principles | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-308 | 5281 | 1 | DEFERRED_TO_MODULE | UPOS-05 |
| SRC-309 | 5285 | 2 | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-310 | 5289 | 3 | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-311 | 5293 | 4 | DEFERRED_TO_MODULE | UPOS-04 |
| SRC-312 | 5297 | 5 | DEFERRED_TO_MODULE | UPOS-06 |
| SRC-313 | 5301 | 6 | DEFERRED_TO_MODULE | UPOS-07 |
| SRC-314 | 5305 | 7 | DEFERRED_TO_MODULE | UPOS-09 |
| SRC-315 | 5309 | 8 | DEFERRED_TO_MODULE | UPOS-02 |
| SRC-316 | 5313 | 9 | DEFERRED_TO_MODULE | UPOS-11 |
| SRC-317 | 5317 | 10 | DEFERRED_TO_MODULE | UPOS-02 |

===== END VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====


---

## VIRTUAL FILE 45/45 — `analysis/TRACEABILITY_VALIDATION.md`

**Virtual path:** `analysis/TRACEABILITY_VALIDATION.md`  
**Content checksum:** `da85b9f94849`

===== BEGIN VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====

# UPOS-003 Traceability Validation

**ID:** UPOS-03-AN-008  
**Type:** VALIDATION REPORT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** ../MODULE_03_TRACEABILITY.md, SOURCE_SECTION_DISPOSITION.md

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Results

| Check | Result |
|---|---|
| Required normative package present | PASS |
| Frozen structural sections inspected | 317 |
| Direct Module-03 structural sections | 5 |
| Mixed Skill-related structural sections | 24 |
| Extracted Module-03 requirements | 51 |
| Candidate Skills classified | 22 |
| Canonical universal Skills | 11 |
| Interface Skills | 11 |
| Skill Contracts missing mandatory sections | 0 |
| Registry required fields present | PASS |
| Registry rows complete | PASS |
| Registry/Skill disposition consistency | PASS |
| Canonical disposition definitions in normative layer | PASS |
| Analysis artifacts historical EVIDENCE | PASS |
| Hard-coded provider/project-path leakage in core normative docs | 0 |
| Unresolved P0/P1 Module-03 gaps | 0 |

```text
UNMAPPED MODULE-03 SOURCE REQUIREMENTS = 0
```

## Boundary validation

- Skill != Role / Agent: **PASS**
- Skill != Workflow: **PASS**
- Skill != Policy: **PASS**
- Skill != Context System: **PASS**
- Skill != Tool/provider binding: **PASS**
- Skill capability != organizational authority: **PASS**
- `INTERFACE_SKILL` is disposition metadata, not lifecycle/quality/temporary/authority state: **PASS**
- Workflow sequencing remains UPOS-004: **PASS**
- Context retrieval remains UPOS-005: **PASS**
- Git policy remains UPOS-006: **PASS**
- Quality verdict/evidence semantics remain UPOS-007: **PASS**
- Telemetry remains UPOS-008: **PASS**
- Learning detection/promotion remains UPOS-009/01: **PASS**
- Permissions remain UPOS-010: **PASS**
- Project/provider bindings remain UPOS-011: **PASS**

## Registry conformance

Mandatory fields:

```text
skill_id
name
version
status
category
purpose
applicable_roles
dependencies
supersedes
replacement
contract_ref
```

Every canonical v1 registry row contains all mandatory fields. `disposition` remains an additional canonical metadata field.

## Final reconciliation checks

The final cleanup pass changed only the authorized areas:

1. canonical Skill Registry now conforms to its own required-field contract;
2. `CANONICAL_UNIVERSAL_SKILL` and `INTERFACE_SKILL` have normative definitions outside archived analysis;
3. `INTERFACE_SKILL` is explicitly non-authoritative disposition metadata;
4. Skill→Workflow, Skill→Context and Skill→Quality boundaries remain unchanged;
5. no new Skills, modules, workflows, runtime capabilities, schemas, or provider bindings were introduced.

## Verdict

PASS — corrected UPOS-003 v1.0 satisfies final reconciliation, registry conformance, disposition semantics, boundary integrity, and traceability gates.

```text
NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 04–11
```

UPOS-003 v1.0 is frozen as the canonical Module 03 baseline.

===== END VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====
