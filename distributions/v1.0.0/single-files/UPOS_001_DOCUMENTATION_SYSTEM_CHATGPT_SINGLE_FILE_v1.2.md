# Universal Project Documentation System — ChatGPT Single-File Edition v1.2

**Purpose:** Portable single-file representation of the complete documentation system for ChatGPT/AI review, migration planning, auditing, and implementation guidance.  
**System version:** 1.2  
**Implementation Guide:** 2.0  
**Generated:** 2026-09-19  
**Embedded virtual files:** 56  

---

# 0. IMPORTANT — How ChatGPT must interpret this file

This file is a **transport bundle**, not a new monolithic source of truth.

It contains many logical documents embedded into one physical Markdown file because chat products may limit the number of uploaded files.

Treat every section marked:

```text
===== BEGIN VIRTUAL FILE: <path> =====
...
===== END VIRTUAL FILE: <path> =====
```

as if `<path>` were a separate file in a repository.

## 0.1 Virtual-folder semantics

When reasoning about this bundle:

1. Preserve the virtual path of every embedded document.
2. Preserve each document's own `Type`, `Status`, `Normativity`, `Owner`, `Lifetime`, and `Scope`.
3. Do **not** merge all embedded rules into one undifferentiated authority.
4. Resolve ownership/conflicts using:
   - `00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md`
   - project `SOURCE_OF_TRUTH.md` when instantiated.
5. The Design System is only the `06_design_system/` module; it does not own Product, Domain, UX, Quality, Decisions, or Plans.
6. Distinguish:
   - document lifecycle status;
   - feature lifecycle;
   - design-system object lifecycle;
   - domain lifecycle.
7. Treat Plans as temporary execution documents, not permanent doctrine.
8. Treat Reports/Evidence as point-in-time evidence, not timeless contracts.
9. Treat Decision Records as rationale/history, not mutable implementation specs.
10. If a project does not need a layer/template, do not create it merely because it exists in this bundle.

## 0.2 ChatGPT read order

For project adoption/migration, read in this order:

```text
1. README.md
2. 00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
3. 00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
4. 00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md
5. UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md
6. 00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md
7. target project's existing documentation/code
8. only then open the relevant layer-specific standards/templates
```

For Design System work additionally read:

```text
06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md
06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md
06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md
06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md
```

## 0.3 Default AI behavior

If asked to adopt this system in a repository:

- default to **Mode B — Documentation reconciliation with implementation verification**;
- audit before moving files;
- do not silently change product semantics;
- do not invent missing truth;
- create an inventory, conflict register, source-of-truth map, and target architecture before mass migration;
- use staged PRs for large repositories;
- instantiate only documentation justified by project complexity.

## 0.4 When asked "where should this document go?"

Use virtual ownership:

```text
Product/business                         → 01_product/
Domain semantics/lifecycles             → 02_domain/
Architecture/boundaries                 → 03_architecture/
Feature/screen behavior                 → 04_product_specs/
UX/IA/navigation/content language       → 05_ux/
Reusable visual/interaction system      → 06_design_system/
Engineering implementation rules        → 07_engineering/
API/data/integrations                    → 08_data_api/
AI contracts                             → 09_ai/
Security/privacy                         → 10_security_privacy/
Quality/testing/evidence                 → 11_quality_testing/
Analytics/metrics                        → 12_analytics/
Operations/release/runbooks              → 13_operations/
Decision rationale                       → 14_decisions/
Current execution/migrations             → 15_plans/
Contributor/AI guidance                  → 16_onboarding/
Lookup/reference                         → 17_reference/
Historical/superseded                    → 99_archive/
```

---

# 1. Virtual repository structure

```text
UNIVERSAL_PROJECT_DOCUMENTATION_SYSTEM/
├── README.md
├── UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md
├── CHANGELOG.md
├── MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md
├── 00_governance
│   ├── DOCS_AS_CODE_STANDARD_v1.0.md
│   ├── DOCUMENT_MANIFEST_SCHEMA_v1.0.json
│   ├── PROJECT_DOCUMENTATION_CATALOG_v1.0.md
│   ├── PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
│   ├── PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
│   ├── PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md
│   ├── PROJECT_DOCUMENTATION_PROFILES_v1.0.md
│   └── templates
│       ├── DOCS_README_TEMPLATE.md
│       └── SOURCE_OF_TRUTH_TEMPLATE.md
├── 01_product
│   └── templates
│       ├── PRODUCT_VISION_TEMPLATE.md
│       └── SCOPE_TEMPLATE.md
├── 02_domain
│   └── templates
│       ├── DOMAIN_MODEL_TEMPLATE.md
│       └── LIFECYCLE_TEMPLATE.md
├── 03_architecture
│   └── templates
│       ├── ADR_TEMPLATE.md
│       └── MASTER_ARCHITECTURE_TEMPLATE.md
├── 04_product_specs
│   └── templates
│       ├── FEATURE_SPEC_TEMPLATE.md
│       ├── FLOW_SPEC_TEMPLATE.md
│       └── SCREEN_EXPERIENCE_SPEC_TEMPLATE.md
├── 05_ux
│   └── templates
│       ├── CONTENT_DESIGN_TEMPLATE.md
│       ├── IA_NAVIGATION_TEMPLATE.md
│       └── UX_CONSTITUTION_TEMPLATE.md
├── 06_design_system
│   ├── DESIGN_HANDOFF_STANDARD_v1.3.md
│   ├── DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md
│   ├── DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md
│   ├── DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md
│   ├── DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json
│   ├── README_TEMPLATE.md
│   ├── UI_KIT_WEB_SPECIFICATION_v1.2.md
│   └── templates
│       ├── COMPONENT_SPEC_TEMPLATE.md
│       ├── PAGE_GRAMMAR_SPEC_TEMPLATE.md
│       └── PATTERN_SPEC_TEMPLATE.md
├── 07_engineering
│   └── templates
│       ├── CODEBASE_GUIDE_TEMPLATE.md
│       └── ENGINEERING_PRINCIPLES_TEMPLATE.md
├── 08_data_api
│   └── templates
│       ├── API_CONTRACT_TEMPLATE.md
│       └── EVENT_CONTRACT_TEMPLATE.md
├── 09_ai
│   └── templates
│       └── AI_SYSTEM_OVERVIEW_TEMPLATE.md
├── 10_security_privacy
│   └── templates
│       └── SECURITY_MODEL_TEMPLATE.md
├── 11_quality_testing
│   └── templates
│       ├── TESTING_STANDARD_TEMPLATE.md
│       └── VISUAL_QA_REPORT_TEMPLATE.md
├── 12_analytics
│   └── templates
│       └── METRIC_CATALOG_TEMPLATE.md
├── 13_operations
│   └── templates
│       └── RUNBOOK_TEMPLATE.md
├── 14_decisions
│   └── templates
│       ├── DDR_TEMPLATE.md
│       ├── DESIGN_RFC_TEMPLATE.md
│       └── PDR_TEMPLATE.md
├── 15_plans
│   └── templates
│       ├── CURRENT_UI_CHANGE_PLAN_TEMPLATE.md
│       └── MIGRATION_PLAN_TEMPLATE.md
├── 16_onboarding
│   └── templates
│       ├── AI_AGENT_GUIDE_TEMPLATE.md
│       └── UI_PR_CHECKLIST_TEMPLATE.md
├── 17_reference
│   └── templates
│       └── GLOSSARY_TEMPLATE.md
├── 99_archive
│   └── README.md
└── examples
    ├── design-system.registry.example.json
    └── document-manifest.example.json
```

---

# 2. Canonical responsibilities

## Governance

Defines the project documentation operating system itself.

Governance includes two explicit companion models:

```text
Source-of-Truth Model
→ who owns truth and how authority/conflicts are resolved

Knowledge Lifecycle Model
→ how observations/evidence become governed project knowledge
```

Governance includes two explicit companion models:

```text
Source-of-Truth Model
→ who owns truth and how authority/conflicts are resolved

Knowledge Lifecycle Model
→ how observations/evidence become governed project knowledge
```

## Product / Domain / Architecture

Define why the product exists, what concepts mean, and how the system is structurally organized.

## Product Specs

Define feature/screen/flow behavior.

## UX

Defines experience principles, IA, navigation, flows, and product language.

## Design System

Defines reusable visual/interaction language:

```text
Foundations
Primitives
Components
Patterns
Page Grammars
```

## Engineering / Data / AI / Security

Define implementation and technical contracts.

## Quality / Analytics / Operations

Define verification, measurement, and production operation.

## Decisions

Preserve why durable decisions were made.

## Plans

Describe what is being changed now.

---

# 3. Single-file usage prompt

A user can attach only this Markdown file to a new ChatGPT conversation and say:

> Study the attached Universal Project Documentation System. Treat each `VIRTUAL FILE` section as a separate logical repository file. Use its virtual folder path to determine ownership and authority. I want to apply this system to my project. First audit my existing documentation according to the Implementation Guide; do not change product semantics and do not create empty ceremonial docs.

For Design System-only work:

> Use the `06_design_system/` virtual module as the governing standard, but preserve upstream Product/Domain/UX ownership. Search for reusable objects before proposing new components or patterns.

---

# 4. Embedded virtual files


---

## VIRTUAL FILE 1/56 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `373c19911fbf`

===== BEGIN VIRTUAL FILE: README.md =====

# Universal Project Documentation System v1.2

**ID:** DOC-SYS-ROOT  
**Type:** STANDARD PACK  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.2.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Any change to the universal documentation architecture  
**Supersedes:** —  
**Related:** —


## 0. Purpose

This package defines a **project-agnostic documentation operating system** for serious software/product work.

It is designed to prevent the most common documentation failure modes:

- multiple competing "sources of truth";
- giant MASTER files mixing timeless principles with temporary execution;
- duplicated product/domain/API/UI truth;
- stale screenshots treated as contracts;
- plans that silently become permanent doctrine;
- code behavior that exists nowhere in documentation;
- design-system rules mixed with UX, QA, plans and decision history;
- AI agents inventing missing entities, routes, states, APIs or UI patterns.

The governing principle is:

> **One fact should have one canonical owner, many links, and as few copies as possible.**

---

# 1. System architecture

```text
LEVEL 0  — GOVERNANCE
LEVEL 1  — PRODUCT TRUTH
LEVEL 2  — DOMAIN TRUTH
LEVEL 3  — ARCHITECTURE TRUTH
LEVEL 4  — PRODUCT / FEATURE CONTRACTS
LEVEL 5  — EXPERIENCE TRUTH
LEVEL 6  — DESIGN SYSTEM
LEVEL 7  — ENGINEERING CONTRACTS
LEVEL 8  — DATA / API / INTEGRATION CONTRACTS
LEVEL 9  — AI CONTRACTS
LEVEL 10 — SECURITY / PRIVACY / COMPLIANCE
LEVEL 11 — QUALITY / TESTING
LEVEL 12 — ANALYTICS / TELEMETRY
LEVEL 13 — OPERATIONS / RELEASE
LEVEL 14 — DECISION HISTORY
LEVEL 15 — CURRENT EXECUTION
LEVEL 16 — ONBOARDING / CONTRIBUTION
LEVEL 17 — REFERENCE
LEVEL 99 — ARCHIVE
```

The levels are **authority domains**, not mandatory folders for every Day-1 MVP.

---

# 2. Canonical package structure

```text
UNIVERSAL_PROJECT_DOCUMENTATION_SYSTEM_v1.2/
│
├── README.md
├── CHANGELOG.md
├── MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md
│
├── 00_governance/
│   ├── PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
│   ├── DOCS_AS_CODE_STANDARD_v1.0.md
│   ├── PROJECT_DOCUMENTATION_CATALOG_v1.0.md
│   ├── PROJECT_DOCUMENTATION_PROFILES_v1.0.md
│   ├── DOCUMENT_MANIFEST_SCHEMA_v1.0.json
│   └── templates/
│
├── 01_product/templates/
├── 02_domain/templates/
├── 03_architecture/templates/
├── 04_product_specs/templates/
├── 05_ux/templates/
│
├── 06_design_system/
│   ├── README_TEMPLATE.md
│   ├── DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md
│   ├── DESIGN_HANDOFF_STANDARD_v1.3.md
│   ├── UI_KIT_WEB_SPECIFICATION_v1.2.md
│   ├── DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md
│   ├── DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json
│   ├── DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md
│   └── templates/
│
├── 07_engineering/templates/
├── 08_data_api/templates/
├── 09_ai/templates/
├── 10_security_privacy/templates/
├── 11_quality_testing/templates/
├── 12_analytics/templates/
├── 13_operations/templates/
├── 14_decisions/templates/
├── 15_plans/templates/
├── 16_onboarding/templates/
├── 17_reference/templates/
├── 99_archive/
└── examples/
```

---

# 3. The key decomposition decision

The package deliberately separates:

```text
UX / EXPERIENCE
    from
DESIGN SYSTEM
    from
QUALITY EVIDENCE
    from
DECISIONS
    from
CURRENT PLANS
```

Examples:

```text
Navigation semantics
→ 05_ux

Button / component visual contract
→ 06_design_system

Visual QA report
→ 11_quality_testing

Why a new pattern was adopted
→ 14_decisions

Current UI migration sequence
→ 15_plans
```

This prevents Design System documentation from becoming another all-purpose monolith.

---

# 4. Stable truth vs living truth vs temporary execution

Every important document declares a `Lifetime`:

```text
STABLE
LIVING
TEMPORARY
HISTORICAL
```

Typical mapping:

```text
Product principles             STABLE
Master architecture            STABLE/LIVING
API contract                   LIVING
Design-system registry         LIVING
Current redesign plan          TEMPORARY
Audit report                   HISTORICAL
Archived old architecture      HISTORICAL
```

---

# 5. Document status is not object status

The package intentionally uses different lifecycles.

## Document lifecycle

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ SUPERSEDED
→ ARCHIVED
```

## Design-system object lifecycle

```text
EXPERIMENTAL
→ CANDIDATE
→ REVIEW
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ DEPRECATED
→ REMOVED
```

## Feature lifecycle

Projects may use:

```text
IDEA
→ DISCOVERY
→ SPEC_DRAFT
→ REVIEW
→ APPROVED
→ IMPLEMENTING
→ SHIPPED
→ DEPRECATED
→ REMOVED
```

Domain lifecycles are owned by the domain and may be entirely different.

> **Never reuse one status enum for everything.**

---

# 6. Source-of-truth model

No single file is globally authoritative.

Authority is scoped.

Recommended precedence:

```text
Product / business truth
→ 01_product

Domain semantics / lifecycles
→ 02_domain

Architecture ownership / boundaries
→ 03_architecture

Feature behavior
→ 04_product_specs

Experience / navigation / flows / language
→ 05_ux

Reusable visual / interaction system
→ 06_design_system

Implementation standards
→ 07_engineering

Wire/data contracts
→ 08_data_api

AI architecture / prompts / eval contracts
→ 09_ai

Security/privacy
→ 10_security_privacy

Quality / test evidence
→ 11_quality_testing

Measurement
→ 12_analytics

Release / restore / incident operation
→ 13_operations

Why a decision was made
→ 14_decisions

What is being changed now
→ 15_plans
```

---

# 7. Design System as a module

The Design System module contains only what it should own:

```text
Governance
Handoff
UI Kit Web
Visual profile
Registry
Foundations
Primitives
Components
Patterns
Page Grammars
Boards
Deprecated objects
```

It does **not** own:

```text
full feature screens
cross-product flows
content language
visual QA reports
current redesign plans
decision history
PR contribution workflow
```

Those belong to their corresponding project layers.

---

# 8. Machine-readable manifests

Two registries exist for different scopes:

```text
DOCUMENT MANIFEST
→ metadata about project documents

DESIGN SYSTEM REGISTRY
→ metadata about design-system objects
```

Both are intended to support:

- indexing;
- link validation;
- freshness checks;
- ownership checks;
- search;
- UI Kit generation;
- AI-agent navigation;
- drift detection.

---

# 9. Recommended project adoption

## Existing project

```text
1. Inventory documentation.
2. Classify every document.
3. Identify canonical owner for each fact.
4. Create docs/README + SOURCE_OF_TRUTH.
5. Mark obvious superseded docs.
6. Split stable truth from temporary execution.
7. Reconcile Product / Domain / Architecture / UX.
8. Introduce Design System module.
9. Add missing critical contracts.
10. Add integrity automation.
```

Do not delete old documentation before unique information is reconciled.

## New project

```text
1. README + docs/README
2. Product vision + scope
3. Domain model as needed
4. Master architecture
5. Feature spec pattern
6. UX Constitution
7. Engineering principles
8. Testing baseline
9. Active plan
10. Design System module as UI becomes reusable
```

---

# 10. Read order for AI agents

```text
1. root README
2. docs/README
3. SOURCE_OF_TRUTH
4. relevant product/feature spec
5. relevant domain + architecture contracts
6. relevant UX/design-system contracts
7. engineering/data/security standards
8. current plan
9. code
```

The AI agent must search before inventing.

---

# 11. Package profiles

Use `00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md`.

Profiles cover:

- Starter/MVP;
- Production;
- Complex/regulated;
- Mobile;
- SaaS;
- API/platform;
- AI product;
- Internal tool.

The model is modular: **not every project creates every document**.

---

# 12. Recommended next step

For a concrete repository:

1. copy this pack into a temporary governance workspace;
2. run a documentation inventory;
3. create project-specific `docs/README.md`;
4. create `SOURCE_OF_TRUTH.md`;
5. instantiate only the templates the project actually needs;
6. reconcile existing design-system docs into the Level-6 module;
7. archive superseded material only after reconciliation.
---

# Adoption / Migration Playbook

The target-state standards and the migration procedure are deliberately separate.

Use:

```text
UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md
```

when introducing this system into an existing or new repository.

It defines:

- migration modes A–E;
- safety boundaries;
- discovery and inventory;
- conflict resolution;
- source-of-truth mapping;
- Product / Domain / Architecture extraction;
- UX vs Design System separation;
- Design System registry reconciliation;
- manifests and traceability;
- AI/Codex execution directives;
- staged PR adoption;
- final migration Definition of Done.

For large repositories, use staged adoption rather than one giant documentation PR.

===== END VIRTUAL FILE: README.md =====

---

## VIRTUAL FILE 2/56 — `UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md`

**Virtual path:** `UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md`  
**Content checksum:** `168c76872d38`

===== BEGIN VIRTUAL FILE: UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md =====

# Universal Project Documentation Implementation Guide v2.0

**ID:** DOC-GUIDE-001  
**Type:** GUIDE / ADOPTION PLAYBOOK  
**Status:** ACTIVE  
**Normativity:** NORMATIVE FOR DOCUMENTATION ADOPTION AND MIGRATION  
**Owner:** Project Governance  
**Version:** 2.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Universal Project Documentation System architecture, migration model, manifest/registry contract, or adoption policy changes  
**Companion system:** `Universal Project Documentation System v1.2`  
**Primary standard:** `00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md`  
**Audience:** Product Owner, Tech Lead, Architecture Owner, Product Design, Design System Owner, Engineering Leads, QA, Security, Documentation Owner, AI coding agents, Codex/Claude Code-style agents, contributors

---

# 0. Purpose

This guide defines the exact procedure for adopting the **Universal Project Documentation System** in:

- an existing messy repository;
- an existing well-documented repository;
- a monolithic MASTER/TЗ repository;
- a new greenfield project;
- a large repository requiring incremental migration;
- an AI-assisted development workflow.

The Operating Model defines:

> **what the target documentation system is.**

This Implementation Guide defines:

> **how to reach that target safely.**

Do not treat this guide as:

> “Move Markdown files into a new folder tree.”

Treat it as:

> **A controlled migration of project knowledge into a governed, discoverable, traceable source-of-truth system.**

---

# 1. Relationship between the universal documents

A project adopting the system does **not** need to load every standard into every task.

Use the documentation stack progressively.

## Core adoption documents

```text
1. README.md
2. 00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
3. 00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
4. 00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md
5. UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md
```

## Open when needed

```text
00_governance/DOCS_AS_CODE_STANDARD_v1.0.md
00_governance/PROJECT_DOCUMENTATION_CATALOG_v1.0.md
00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md
00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json
```

## Design-system migration

Read when the repository contains reusable UI/design-system work:

```text
06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md
06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md
06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md
06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md
06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json
```

## Principle

> **Load the rule set that owns the current migration decision.**

Do not dump dozens of standards into an AI prompt without need.

---

# 2. Core migration principles

## Rule 1 — Knowledge before folders

The migration target is not a pretty directory tree.

The target is:

- clear canonical ownership;
- fewer contradictions;
- stable truth separated from temporary work;
- discoverable documentation;
- preserved decision history;
- reduced ambiguity for humans and AI.

---

## Rule 2 — Reorganize knowledge before redesigning the product

Unless explicitly authorized, documentation migration MUST NOT silently change:

```text
product behavior
domain semantics
domain state names
business rules
permissions
authorization logic
API behavior
database schema
application routes
feature scope
UX behavior
design-system behavior
infrastructure
deployment topology
analytics definitions
security/privacy policy
```

Default:

> **Document first. Refactor later in separate work.**

---

## Rule 3 — Unknown is better than invented certainty

If existing sources do not establish truth:

```text
UNKNOWN
TBD
OWNER DECISION REQUIRED
CONFLICT UNRESOLVED
```

is correct.

An AI agent MUST NOT fill documentation gaps by inventing convenient product semantics.

---

## Rule 4 — One fact, one canonical owner

Examples:

```text
Subscription lifecycle
→ Domain

Navigation semantics
→ UX

Button contract
→ Design System

HTTP schema
→ API contract

Deployment procedure
→ Operations
```

Other documents link.

They do not re-own the fact.

---

## Rule 5 — Preserve history until reconciliation is complete

Do not delete legacy MASTER docs merely because new canonical docs now exist.

First:

1. extract unique knowledge;
2. resolve conflicts;
3. establish replacement;
4. add supersession;
5. repair references;
6. then archive.

---

# 3. Migration modes

Choose one mode before modifying documentation.

---

## Mode A — Documentation-only migration

### Use when

- project is active;
- code is sensitive;
- documentation is messy;
- lowest possible product risk is required.

### Allowed

```text
create docs structure
classify
split docs
merge exact duplicates
move docs
add metadata
create Source of Truth
create indexes
create manifest
mark superseded docs
archive docs
add docs CI
```

### Forbidden

```text
code changes
schema changes
route changes
API behavior changes
domain behavior changes
UI behavior changes
infrastructure changes
```

### Recommendation

Preferred first mode for most mature repositories.

---

## Mode B — Documentation reconciliation with implementation verification

### Use when

Documentation may be stale and the repository must be inspected to determine reality.

Agent MAY inspect:

```text
source code
tests
routes
schema
OpenAPI
GraphQL
migrations
package configuration
feature flags
CI/CD
runtime config
deployment files
design-system source
stories
```

Purpose is only to determine:

```text
what is implemented
what documentation is stale
where code and docs disagree
```

Implementation remains unchanged.

### Recommended default

For AI-assisted migration of an active product, **Mode B is usually the best default**.

---

## Mode C — Documentation + corrective implementation

Use only after the canonical documentation architecture is established.

Example:

```text
Canonical contract says X.
Implementation does Y.
Owners confirm X.
```

Then create a **separate corrective implementation task**.

Do not mix corrective code changes into the initial documentation migration unless explicitly authorized.

---

## Mode D — Greenfield bootstrap

Use for a new repository.

There is no legacy migration.

Goal:

- establish minimal governance;
- create only justified canonical docs;
- avoid speculative bureaucracy;
- make future growth compatible with the universal model.

Recommended bootstrap appears later in this guide.

---

## Mode E — Incremental adoption

Use for large living repositories where a full migration would be disruptive.

Apply the universal model immediately to:

```text
new features
new architecture decisions
new reusable UI
touched legacy areas
new APIs
new runbooks
new AI capabilities
```

Legacy docs are migrated progressively.

This is preferable to a multi-month “documentation rewrite project”.

---

# 4. Migration safety levels

Before each proposed action classify risk.

## SAFE

May usually be automated:

```text
add metadata
create index
fix obvious broken links
move clearly historical reports
add superseded banner
create manifest entry
normalize exact duplicate references
create empty archive README
```

## REVIEW

Requires reasoning/review:

```text
split mixed MASTER
merge overlapping active docs
move canonical owner
normalize terminology
extract architecture from multiple sources
change document normativity
classify one document as superseded
```

## OWNER DECISION REQUIRED

Do not resolve automatically:

```text
two active product specs disagree
authorization rules conflict
billing semantics conflict
retention/privacy conflict
domain lifecycles disagree
architecture ownership conflicts
destructive-action semantics differ
accepted decisions contradict current docs
```

---

# 5. Required inputs

Minimum:

```text
Universal Project Documentation System v1.2
target repository
```

For an AI agent, supply/direct it to:

```text
README.md
PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
IMPLEMENTATION_GUIDE_v2.0.md
```

Useful optional sources:

```text
legacy MASTER / ТЗ
product requirements
architecture docs
UX docs
design files/specs
roadmaps
research
API docs
DB docs
README files
PR/issue conventions
runbooks
analytics docs
security docs
```

The repository must be audited before asking the owner to re-explain the whole project manually.

---

# 6. Required migration outputs

Minimum for an existing non-trivial repository:

```text
docs/README.md

docs/00_governance/
├── SOURCE_OF_TRUTH.md
├── DOCUMENTATION_INVENTORY.md
├── DOCUMENTATION_CONFLICTS.md
├── TARGET_DOCUMENTATION_ARCHITECTURE.md
├── MIGRATION_REPORT.md
└── GLOSSARY.md             # when terminology complexity justifies it

docs/15_plans/
└── ACTIVE_PLAN.md

docs/16_onboarding/
└── AI_AGENT_GUIDE.md       # strongly recommended for AI-assisted repos

docs/99_archive/
└── README.md
```

For larger projects:

```text
docs/00_governance/DOCUMENT_MANIFEST.json
```

Do not create empty ceremonial files for every layer.

---

# 7. Complete phase model

```text
PHASE 0  — Safety & Repository Baseline
PHASE 1  — Repository Discovery
PHASE 2  — Documentation Inventory
PHASE 3  — Classification
PHASE 4  — Ownership & Source-of-Truth Mapping
PHASE 5  — Conflict, Duplication & Drift Analysis
PHASE 6  — Target Documentation Architecture
PHASE 7  — Governance Foundation
PHASE 8  — Product Truth Extraction
PHASE 9  — Domain Truth Extraction
PHASE 10 — Architecture Reconciliation
PHASE 11 — Product Spec Decomposition
PHASE 12 — UX Reconciliation
PHASE 13 — Design System Reconciliation
PHASE 14 — Engineering / Data / AI / Security
PHASE 15 — Quality / Analytics / Operations
PHASE 16 — Decision Memory Extraction
PHASE 17 — Current Plans Separation
PHASE 18 — Supersession & Archive
PHASE 19 — Manifest / Registry
PHASE 20 — Onboarding & AI Guidance
PHASE 21 — Integrity Automation
PHASE 22 — Final Reconciliation
PHASE 23 — Ongoing Governance
```

Not all phases require a separate PR.

They are semantic phases, not bureaucracy.

---

# 8. PHASE 0 — Safety & Repository Baseline

Before modifying documentation record:

```text
repository
branch
commit
date
working tree state
migration mode
migration owner
documentation-system version
implementation-guide version
```

Recommended:

```text
docs/00_governance/MIGRATION_REPORT.md
```

Start with:

```markdown
# Documentation Migration Report

**Baseline branch:** main
**Baseline commit:** <hash>
**Started:** YYYY-MM-DD
**Migration mode:** B — Reconciliation with verification
**Documentation System:** v1.1
**Implementation Guide:** v2.0
```

If working tree is dirty, report it before large moves.

---

# 9. PHASE 1 — Repository Discovery

Scan documentation:

```text
*.md
*.mdx
*.txt
*.rst
README*
docs/**
spec/**
specs/**
requirements/**
architecture/**
design/**
ux/**
notes/**
research/**
plans/**
decisions/**
adr/**
rfc/**
runbooks/**
```

Also inspect implementation sources relevant to truth verification:

```text
package.json
pubspec.yaml
Cargo.toml
go.mod
requirements.txt
Dockerfile
docker-compose*
.env.example
CI config
migrations
OpenAPI
GraphQL schemas
DB schema
routes
feature flags
tests
deployment
design-system source
Storybook
analytics schemas
```

Do not reorganize yet.

Goal:

> Understand both claimed knowledge and implementation evidence.

---

# 10. PHASE 2 — Documentation Inventory

Create:

```text
docs/00_governance/DOCUMENTATION_INVENTORY.md
```

Every meaningful documentation artifact gets one row.

Recommended columns:

| Field | Meaning |
|---|---|
| Path | Current location |
| Title | Human title |
| Inferred class | MASTER / SPEC / PLAN / ... |
| Document status | ACTIVE / historical / unknown |
| Normativity | Normative / informative / evidence / generated |
| Lifetime | Stable / living / temporary / historical |
| Scope | Product / Domain / Architecture / ... |
| Owner | Known / inferred / unknown |
| Baseline | Date/commit if relevant |
| Freshness | Current / review due / unknown |
| Duplicate of | Similar source |
| Conflicts with | Contradictory source |
| Action | KEEP / MOVE / RENAME / SPLIT / MERGE / SUPERSEDE / ARCHIVE / DELETE |
| Target | Proposed canonical location |
| Notes | Reasoning |

Example:

```markdown
| Path | Class | Lifetime | Scope | Problem | Action | Target |
|---|---|---|---|---|---|---|
| MASTER_TZ.md | MIXED | MIXED | Multi | Product + architecture + roadmap | SPLIT | multiple |
| docs/ui.md | MIXED | MIXED | UX/DS/Plan | Stable UX + current defects | SPLIT | 05_ux + 06_design_system + 15_plans |
| api.md | CONTRACT | LIVING | API | Valid but unindexed | MOVE | 08_data_api/API_CONTRACTS.md |
| old-roadmap.md | PLAN | HISTORICAL | Plans | Completed | ARCHIVE | 99_archive/plans/ |
```

---

# 11. Inventory rules

Never classify only from filename.

A file called:

```text
architecture.md
```

may actually be:

- a plan;
- a report;
- an RFC;
- current master architecture.

A file called:

```text
MASTER.md
```

may contain:

- product vision;
- domain model;
- feature specs;
- architecture;
- UX;
- implementation plan;
- current defects.

Read enough to determine **semantic ownership**.

---

# 12. PHASE 3 — Classification

Classify document class:

```text
CONSTITUTION
MASTER
CONTRACT
SPECIFICATION
STANDARD
PLAN
RFC
DECISION_RECORD
RUNBOOK
GUIDE
REFERENCE
REPORT
EVIDENCE
GENERATED
ARCHIVE
MIXED
```

`MIXED` is valid during migration only.

Also classify:

## Document lifecycle

```text
DRAFT
REVIEW
APPROVED
ACTIVE
DEPRECATED
SUPERSEDED
ARCHIVED
UNKNOWN
```

## Normativity

```text
NORMATIVE
INFORMATIVE
EVIDENCE
GENERATED
UNKNOWN
```

## Lifetime

```text
STABLE
LIVING
TEMPORARY
HISTORICAL
UNKNOWN
```

## Freshness

```text
CURRENT
REVIEW_DUE
STALE_REVIEW_REQUIRED
UNKNOWN
NOT_APPLICABLE
```

---

# 13. Critical status rule

Never collapse different status systems.

Examples:

```text
Document status: ACTIVE
Feature status: SHIPPED
Design-system object lifecycle: IMPLEMENTED
Domain order status: FULFILLED
```

The migration agent MUST preserve these as distinct dimensions.

Do not “clean them up” into a universal `Status`.

---

# 14. PHASE 4 — Ownership & Source-of-Truth Mapping

Create:

```text
docs/00_governance/SOURCE_OF_TRUTH.md
```

Authority is scoped.

Recommended map:

```text
Product / business
→ 01_product

Domain semantics / lifecycles
→ 02_domain

Architecture / ownership
→ 03_architecture

Feature behavior
→ 04_product_specs

UX / IA / flows / content language
→ 05_ux

Reusable visual / interaction system
→ 06_design_system

Engineering implementation rules
→ 07_engineering

API / data / integrations
→ 08_data_api

AI architecture / behavior
→ 09_ai

Security / privacy
→ 10_security_privacy

Quality / test evidence
→ 11_quality_testing

Analytics / metrics
→ 12_analytics

Operations / releases
→ 13_operations

Decision rationale
→ 14_decisions

Current sequencing
→ 15_plans
```

For each high-value fact ask:

```text
Where is it currently defined?
Is that source active?
Is it duplicated?
Do duplicates agree?
Which layer should own it?
Does implementation match?
Does an accepted decision supersede it?
```

---

# 15. PHASE 5 — Conflict, Duplication & Drift Analysis

Create:

```text
docs/00_governance/DOCUMENTATION_CONFLICTS.md
```

Recommended record:

```markdown
## CONFLICT-001 — Session duration

**Scope:** Security/Auth
**Doc A:** ...
**Claim A:** ...
**Doc B:** ...
**Claim B:** ...
**Implementation evidence:** ...
**Accepted decisions:** ...
**Canonical owner:** ...
**Risk:** ...
**Recommended action:** ...
**Status:** OPEN / RESOLVED / OWNER_DECISION_REQUIRED
```

---

# 16. Conflict resolution policy

May often resolve automatically when:

```text
one source is clearly historical
one explicitly supersedes another
one is a temporary plan and one is stable truth
one is generated from canonical schema
```

Escalate when active normative sources disagree about:

```text
product semantics
billing
authorization
security
privacy/retention
destructive behavior
domain lifecycles
architecture ownership
```

---

# 17. Drift taxonomy during migration

Record separately:

## DOC DRIFT

Docs stale relative to implementation.

## IMPLEMENTATION DRIFT

Code differs from confirmed canonical contract.

## PRODUCT DRIFT

Shipped experience contradicts approved product/UX principles.

## SCHEMA DRIFT

Code/data/API implementations diverge.

## DESIGN DRIFT

UI differs from approved reusable design-system contract.

## OPERATIONS DRIFT

Runbook/docs no longer match deployed process.

Do not automatically assume code is correct.

---

# 18. PHASE 6 — Target Documentation Architecture

Before moving files create:

```text
docs/00_governance/TARGET_DOCUMENTATION_ARCHITECTURE.md
```

Contents:

```text
Current tree
Target tree
Project profile
Mapping
Docs to KEEP
MOVE
SPLIT
MERGE
SUPERSEDE
ARCHIVE
New canonical docs
Open conflicts
Migration order
```

Do not create every universal folder by default.

Use `PROJECT_DOCUMENTATION_PROFILES`.

---

# 19. Target tree decision rule

Create a folder/layer only when at least one of these is true:

- it owns material canonical truth;
- it reduces ambiguity;
- it has an independent lifecycle/owner;
- project risk warrants it;
- near-term work needs it.

Avoid ceremonial empty directories.

---

# 20. PHASE 7 — Governance Foundation

Create/reconcile first:

```text
docs/README.md
docs/00_governance/SOURCE_OF_TRUTH.md
docs/00_governance/DOCUMENTATION_INVENTORY.md
docs/00_governance/DOCUMENTATION_CONFLICTS.md
docs/00_governance/TARGET_DOCUMENTATION_ARCHITECTURE.md
docs/00_governance/MIGRATION_REPORT.md
docs/15_plans/ACTIVE_PLAN.md
docs/99_archive/README.md
```

Optional:

```text
GLOSSARY.md
DOCUMENT_MANIFEST.json
TRACEABILITY.md
```

This creates navigation before mass extraction.

---

# 21. PHASE 8 — Product Truth Extraction

Extract stable product truth before detailed implementation docs.

Typical:

```text
PRODUCT_VISION
PRODUCT_PRINCIPLES
USER_PROBLEMS / JTBD
SCOPE
SUCCESS_CRITERIA
BUSINESS_RULES
```

Rules:

```text
PRESERVE confirmed semantics
NORMALIZE terminology
REMOVE temporary execution noise
LINK canonical owners
MARK uncertainty
```

Do not invent missing strategy.

---

# 22. PHASE 9 — Domain Truth Extraction

Typical:

```text
DOMAIN_MODEL
DOMAIN_GLOSSARY
ENTITY_CATALOG
LIFECYCLES
INVARIANTS
OWNERSHIP_BOUNDARIES
```

Important:

> Database schema is not automatically the domain model.

Do not derive desired domain semantics solely from implementation convenience.

---

# 23. PHASE 10 — Architecture Reconciliation

Create/reconcile only what project needs:

```text
MASTER_ARCHITECTURE
SYSTEM_CONTEXT
CONTAINER_VIEW
DATA_FLOW
TRUST_BOUNDARIES
NON_FUNCTIONAL_REQUIREMENTS
```

Architecture docs should explain:

- ownership;
- boundaries;
- dependencies;
- failure model;
- major flows.

Low-level implementation detail belongs in Engineering.

Significant historical architecture decisions belong in ADRs.

---

# 24. PHASE 11 — Product Spec Decomposition

Large MASTER requirement documents should be decomposed by capability.

Example:

```text
04_product_specs/
├── auth/
├── onboarding/
├── search/
├── billing/
├── publishing/
└── settings/
```

Each feature spec owns only feature-specific behavior.

Feature specs reference, rather than duplicate:

```text
Domain
Architecture
UX
Design System
Security
API/Data
Analytics
```

---

# 25. Screen and Flow migration rule

Whole-screen/flow contracts are **not Design System truth**.

Move:

```text
Screen Experience Spec
→ 04_product_specs/ or 05_ux/

User Flow / Flow Spec
→ 04_product_specs/ or 05_ux/
```

They may reference:

```text
Page Grammar
Components
Patterns
```

from Design System.

---

# 26. PHASE 12 — UX Reconciliation

Separate durable experience truth from:

- visual system;
- feature behavior;
- current defects;
- redesign plans.

Typical target:

```text
05_ux/
├── UX_CONSTITUTION.md
├── INFORMATION_ARCHITECTURE.md
├── NAVIGATION_MODEL.md
├── USER_FLOWS.md
├── CONTENT_DESIGN.md
├── ACCESSIBILITY_UX.md
└── research/
```

---

# 27. Split Project Design Constitution

If legacy docs contain a mixed `Project Design Constitution`:

## Move to UX Constitution

```text
product feeling
UX laws
information hierarchy
navigation semantics
forms policy
progressive disclosure
human-control principles
data honesty UX
AI UX
error/recovery philosophy
responsive philosophy
```

## Move to Design System Profile

```text
canvas
surfaces
colors
typography
spacing
radius
borders
elevation
icons
motion
density
media treatment
data visualization language
```

## Move Content Design separately

```text
terminology
CTA grammar
capitalization
errors
empty-state language
date/time/number rules
```

---

# 28. Research migration

Research is evidence, not automatically product truth.

Recommended:

```text
05_ux/research/
01_product/research/
```

depending on ownership.

Promotion path:

```text
Research finding
→ product/UX decision
→ contract/principle/spec update
```

Do not paste research conclusions directly into constitutions without decision.

---

# 29. PHASE 13 — Design System Reconciliation

This is now a dedicated migration workstream.

Read:

```text
06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md
06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md
06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md
06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json
```

---

# 30. Design System migration target

Recommended:

```text
06_design_system/
├── README.md
├── DESIGN_SYSTEM_OPERATING_MODEL.md
├── DESIGN_HANDOFF_STANDARD.md
├── UI_KIT_WEB_SPECIFICATION.md
├── DESIGN_SYSTEM_PROFILE.md
├── REGISTRY.json
├── CHANGELOG.md
│
├── foundations/
├── primitives/
├── components/
├── patterns/
├── page-grammars/
├── boards/
├── implemented/
└── deprecated/
```

Only create categories that have real content.

---

# 31. Design System taxonomy migration

Classify reusable UI assets into:

```text
FOUNDATION
PRIMITIVE
COMPONENT
PATTERN
PAGE_GRAMMAR
```

Do not classify:

```text
full screens
whole user flows
current redesign plans
QA reports
decision history
```

as Design System objects.

---

# 32. Design System object lifecycle migration

Legacy statuses must be mapped carefully.

Target DS object lifecycle:

```text
EXPERIMENTAL
CANDIDATE
REVIEW
APPROVED
IMPLEMENTING
IMPLEMENTED
DEPRECATED
REMOVED
```

Keep separate:

```text
Document status
Object lifecycle
```

Example:

```text
Document status: ACTIVE
Object lifecycle: IMPLEMENTED
```

---

# 33. Design System three-truth reconciliation

For each important reusable object find:

## Visual truth

```text
board
approved design
approved screenshot
```

## Behavioral truth

```text
Markdown/MDX spec
```

## Implementation truth

```text
code
story
tests
```

Registry should track:

```text
visualVersion
specVersion
codeVersion
parity
```

If they disagree:

```text
OUT_OF_SYNC
```

Do not silently label object `IMPLEMENTED` as fully reconciled.

---

# 34. Design System Registry creation

Create:

```text
06_design_system/REGISTRY.json
```

Use the supplied schema.

Each relevant object should link:

```text
id
type
contractVersion
objectStatus
owner
purpose
spec
board
source
story
tests
relations
truths
review metadata
traceability
deprecation
```

---

# 35. Design System traceability

Where valuable link reusable UI to:

```text
feature specs
UX docs
requirements
architecture refs
design decisions
tests
telemetry
evidence
```

Do not force full traceability onto trivial primitives.

---

# 36. Design System Profile extraction

Create:

```text
06_design_system/DESIGN_SYSTEM_PROFILE.md
```

Extract only visual-system truth.

Do not duplicate UX Constitution.

---

# 37. Page Grammar extraction

Repeated screen-composition rules may be promoted into Page Grammars.

Examples:

```text
Catalog
Deep Work
Review
Monitor
Master/Detail
```

Only promote when genuinely reusable.

Do not mechanically turn every screen layout into a grammar.

---

# 38. Visual boards

Boards should exist for important/high-risk reusable objects.

Do not generate boards for trivial dividers merely for completeness.

Boards are visual contracts, not marketing slides.

---

# 39. UI Kit Web adoption

UI Kit Web may be introduced:

## During initial migration

when project already has a mature reusable system.

## After registry stabilization

when design system is being reconstructed from scattered UI.

Preferred sequence:

```text
Registry
→ core object contracts
→ stories/live examples
→ UI Kit Atlas
→ detail pages
→ static export
```

Do not build a beautiful empty portal before canonical metadata exists.

---

# 40. Design decisions migration

Design RFCs and DDRs live under:

```text
14_decisions/design/
```

Examples:

```text
Why mobile detail uses Bottom Sheet
Why navigation changed from tabs to rail
Why one pattern replaced another
```

The DS spec defines the current contract.

DDR preserves why.

---

# 41. Visual QA migration

Move QA evidence out of Design System canonical docs.

Target:

```text
11_quality_testing/
├── VISUAL_REGRESSION.md
├── reports/
└── evidence/
```

Design System Registry may reference the evidence.

Quality owns the report.

---

# 42. Current redesign plans

Move to:

```text
15_plans/
```

A current redesign plan may contain:

```text
baseline
current defects
migration sequence
PR sequence
temporary constraints
completion condition
```

It is not a Constitution and not a Design System standard.

---

# 43. PHASE 14 — Engineering / Data / AI / Security

Reconcile canonical technical contracts.

## Engineering

```text
ENGINEERING_PRINCIPLES
CODEBASE_GUIDE
FRONTEND_ARCHITECTURE
BACKEND_ARCHITECTURE
ERROR_HANDLING
OBSERVABILITY
PERFORMANCE
```

## Data/API

```text
DATA_MODEL
API_CONTRACTS
EVENT_CONTRACTS
MIGRATIONS
VERSIONING
RETENTION
```

## AI

Only when meaningful:

```text
AI_SYSTEM_OVERVIEW
MODEL_PROVIDER_BOUNDARIES
CONTEXT_ASSEMBLY
PROMPT_CONTRACTS
HUMAN_APPROVAL
EVALS
SAFETY
```

## Security

```text
SECURITY_MODEL
THREAT_MODEL
AUTHENTICATION
AUTHORIZATION
PRIVACY
DATA_CLASSIFICATION
AUDIT
```

Do not create layers the project does not need.

---

# 44. PHASE 15 — Quality / Analytics / Operations

## Quality

```text
TESTING_STANDARD
QUALITY_STRATEGY
ACCESSIBILITY_TESTING
VISUAL_REGRESSION
PERFORMANCE_TESTING
TEST_DATA
```

## Analytics

```text
EVENT_TAXONOMY
METRIC_CATALOG
KPI_DEFINITIONS
EXPERIMENTATION
```

## Operations

```text
ENVIRONMENTS
DEPLOYMENT
RELEASE_PROCESS
ROLLBACK
BACKUP_RESTORE
INCIDENT_RESPONSE
runbooks/
```

---

# 45. PHASE 16 — Decision Memory Extraction

Extract durable non-obvious decisions.

Use:

```text
ADR
PDR
DDR
SDR
```

Create a decision record when:

- decision is significant;
- alternatives existed;
- rationale will likely be questioned later;
- durable contract changed.

Do not create decision records for trivial edits.

---

# 46. Decision extraction heuristic

Ask:

> Will a competent future contributor reasonably ask “why did we do this?” in six months?

If yes, preserve rationale.

Legacy docs often hide valuable decision context in long prose.

Do not discard it during cleanup.

---

# 47. PHASE 17 — Current Plans Separation

Extract temporary execution:

```text
current implementation tasks
migration steps
known current defects
PR sequence
release rollout
current milestone
temporary constraints
```

into:

```text
15_plans/
```

Plans require:

```text
baseline
target
owner
completion condition
archive action
```

---

# 48. Durable vs temporary split question

Ask:

> Would this sentence still belong in the same document after the current initiative completes tomorrow?

If **yes**:

likely durable/living truth.

If **no**:

likely Plan/Report/Evidence.

---

# 49. PHASE 18 — Supersession & Archive

Do not immediately delete old canonical-looking docs.

Add:

```markdown
> [!WARNING]
> **Status: SUPERSEDED**
>
> This document is preserved for historical traceability.
>
> Canonical replacement:
> - `<path>`
>
> Superseded on: YYYY-MM-DD
```

Archive only after unique content is preserved.

---

# 50. Archive structure

Example:

```text
99_archive/
├── product/
├── domain/
├── architecture/
├── ux/
├── design-system/
├── plans/
├── audits/
└── legacy-master/
```

Archive is memory, not trash.

---

# 51. PHASE 19 — Document Manifest

For medium/large repositories create:

```text
docs/00_governance/DOCUMENT_MANIFEST.json
```

Validate against:

```text
DOCUMENT_MANIFEST_SCHEMA_v1.0.json
```

Manifest records:

```text
document ID
path
type
document status
normativity
owner
version
lifetime
canonical scope
last reviewed
review trigger
freshness
supersession
related refs
implementation/test/evidence refs
generated metadata
```

---

# 52. Manifest vs Design System Registry

Do not merge them.

## Document Manifest

Tracks project documentation artifacts.

## Design System Registry

Tracks reusable Design System objects.

One DS object may have several documentation/code artifacts.

They solve different problems.

---

# 53. PHASE 20 — Onboarding & AI Guidance

Create:

```text
docs/16_onboarding/START_HERE.md
docs/16_onboarding/AI_AGENT_GUIDE.md
```

Optional short root pointers:

```text
AGENTS.md
CODEX.md
CLAUDE.md
```

These must link canonical guidance rather than duplicate it.

---

# 54. AI read order

Recommended:

```text
1. root README
2. docs/README
3. SOURCE_OF_TRUTH
4. relevant feature/product spec
5. relevant Domain/Architecture
6. relevant UX/Design System
7. Engineering/Data/Security rules
8. current plan
9. code
```

---

# 55. AI anti-hallucination contract

Before modifying a domain, AI must:

```text
search docs
search implementation
identify canonical owner
identify lifecycle
identify permissions
identify tests
identify existing design-system objects
```

AI must not invent:

```text
entities
routes
statuses
permissions
API endpoints
database fields
metrics
business rules
design-system components
feature flags
```

without evidence or explicit authorization.

---

# 56. PHASE 21 — Integrity Automation

Only after structure stabilizes.

Useful checks:

```text
broken links
duplicate document IDs
invalid document statuses
missing owner
missing lifetime
superseded without replacement
manifest inconsistency
duplicate canonical scope
stale review date
invalid DS registry
DS registry source path missing
deprecated DS object still newly referenced
```

Do not build heavy tooling before canonical structure exists.

---

# 57. Optional integrity script

Suggested:

```text
scripts/check_docs.py
```

Possible responsibilities:

```text
validate document manifest
validate DS registry
resolve internal links
verify unique IDs
verify status enums
verify supersession chains
warn freshness
check referenced paths
```

---

# 58. PHASE 22 — Final Reconciliation

Before migration completion answer:

```text
Does every major truth have a canonical owner?
Do multiple active docs own the same fact?
Are stable truths separated from plans?
Are historical docs visibly historical?
Can a new engineer find architecture?
Can a product person find feature truth?
Can a designer find UX and DS rules?
Can an AI agent determine authority?
Can current work be found quickly?
Can important historical decisions be explained?
Are critical undocumented areas listed?
```

---

# 59. Initial migration Definition of Done

```text
[ ] docs/README exists
[ ] SOURCE_OF_TRUTH exists
[ ] inventory exists
[ ] conflict register exists
[ ] target architecture exists
[ ] major active docs classified
[ ] major active docs have owners
[ ] document status/lifetime are not conflated
[ ] critical mixed docs split or scheduled
[ ] duplicate active truths resolved
[ ] stable truth separated from current plans
[ ] legacy docs superseded/archived deliberately
[ ] AI/contributor read order documented
[ ] no product semantics changed accidentally
[ ] unresolved high-risk conflicts explicitly listed
[ ] manifest added if project complexity justifies it
[ ] design-system registry reconciled if DS exists
```

---

# 60. PHASE 23 — Ongoing Governance

After migration, documentation maintenance becomes normal project work.

Every meaningful change should ask:

```text
Product truth changed?
Domain semantics changed?
Architecture changed?
Feature behavior changed?
UX changed?
Design System contract changed?
Engineering standard changed?
API/data changed?
AI behavior changed?
Security/privacy changed?
Quality strategy/evidence changed?
Analytics changed?
Operations changed?
Decision record needed?
Plan updated?
```

Update the **owning canonical document**, not arbitrary nearby Markdown.

---

# 61. Recommended staged PR sequence

For a substantial existing project:

```text
PR-DOC-01 — Audit & Baseline
PR-DOC-02 — Governance Foundation
PR-DOC-03 — Product Truth
PR-DOC-04 — Domain Truth
PR-DOC-05 — Architecture
PR-DOC-06 — Product Specs
PR-DOC-07 — UX
PR-DOC-08 — Design System
PR-DOC-09 — Engineering / Data / AI / Security
PR-DOC-10 — Quality / Analytics / Operations
PR-DOC-11 — Decisions
PR-DOC-12 — Plans & Archive
PR-DOC-13 — Manifests / Registries
PR-DOC-14 — Onboarding
PR-DOC-15 — Integrity Automation
```

Combine PRs for smaller projects.

---

# 62. PR-DOC-01 — Audit & Baseline

Create:

```text
DOCUMENTATION_INVENTORY
DOCUMENTATION_CONFLICTS
TARGET_DOCUMENTATION_ARCHITECTURE
MIGRATION_REPORT
```

Do not:

```text
delete docs
rewrite architecture
move huge trees
change code
```

Exit:

> We understand the current knowledge system.

---

# 63. PR-DOC-02 — Governance Foundation

Create/reconcile:

```text
docs/README
SOURCE_OF_TRUTH
governance metadata
ACTIVE_PLAN
archive README
```

Exit:

> Contributors can determine where truth should live.

---

# 64. PR-DOC-03/04/05 — Stable core truth

Order:

```text
Product
→ Domain
→ Architecture
```

Reason:

Lower layers depend on stable semantics.

---

# 65. PR-DOC-06 — Product Specs

Decompose giant requirements into capability-owned specs.

Do not copy global architecture/domain rules into every feature.

---

# 66. PR-DOC-07 — UX

Establish:

```text
UX Constitution
IA
Navigation
Content Design
User Flows
```

Move current redesign defects into Plans/Reports.

---

# 67. PR-DOC-08 — Design System

Establish:

```text
DS Operating Model
DS Profile
DS Registry
core foundations
core primitives/components
patterns
page grammars
handoff contracts
UI Kit plan
```

Do not pull whole feature/screens into the DS module.

---

# 68. PR-DOC-09/10 — Technical and assurance layers

Only create documents justified by project complexity.

Avoid “completeness theater”.

---

# 69. PR-DOC-11 — Decision memory

Extract significant rationale into ADR/PDR/DDR/SDR.

---

# 70. PR-DOC-12 — Plans & Archive

Separate execution from permanent truth.

Preserve history.

---

# 71. PR-DOC-13 — Manifests / Registries

After naming and locations stabilize:

- build Document Manifest;
- build/reconcile DS Registry;
- validate schemas.

Do not build manifest too early while paths are changing daily.

---

# 72. PR-DOC-14/15 — Onboarding & automation

Finish with:

- AI guide;
- contributor guide;
- integrity checks.

---

# 73. KEEP rule

Use `KEEP` when:

- one clear purpose;
- current;
- correct ownership;
- target location acceptable.

May still add metadata/links.

---

# 74. MOVE rule

Use when content is healthy but ownership/location is wrong.

Move does not mean rewrite.

---

# 75. RENAME rule

Use for canonical discoverability.

Avoid cosmetic mass-renaming.

Truth and traceability are more important than pretty filenames.

---

# 76. SPLIT rule

Use when one document mixes independent responsibilities/lifetimes.

Common:

```text
principles + current tasks
architecture + roadmap
UX Constitution + audit
API contract + migration notes
feature behavior + implementation plan
Design System + visual QA evidence
```

---

# 77. MERGE rule

Use only when:

- same conceptual owner;
- both intended to be active;
- substantial overlap;
- no useful independent lifecycle.

Reconcile differences before merge.

---

# 78. SUPERSEDE rule

Use when a new canonical source replaces the old but history remains useful.

Always point forward.

---

# 79. ARCHIVE rule

Use when:

- completed plan;
- historical report;
- retired spec;
- superseded architecture;
- old research snapshot;
- deprecated design proposal.

---

# 80. DELETE rule

Rare.

Only when:

```text
exact duplicate
no unique historical value
no references
canonical replacement exists
```

If uncertain, archive.

---

# 81. Handling README

Root README:

```text
product intro
quick setup
key commands
docs entry link
```

Do not make README a second MASTER.

---

# 82. Handling monolithic MASTER / ТЗ

Process:

```text
1. preserve original
2. classify sections by owner/lifetime
3. extract Product
4. extract Domain
5. extract Architecture
6. extract Feature Specs
7. extract UX
8. extract Design System
9. extract technical contracts
10. extract Plans
11. extract decision rationale
12. verify no unique content lost
13. mark superseded
14. archive later
```

Do not split mechanically by heading.

---

# 83. Handling multiple “final” versions

For:

```text
MASTER.md
MASTER_v2.md
MASTER_v3_final.md
MASTER_new.md
```

determine canonicality using:

```text
git history
dates
references
implementation alignment
explicit supersession
owner intent
accepted decisions
```

Never infer from filename alone.

---

# 84. Handling code-vs-doc disagreement

Three common cases:

```text
docs stale
implementation wrong
migration incomplete
```

Determine canonical owner.

Implementation evidence is not automatically desired truth.

---

# 85. Handling undocumented implementation

If code clearly contains behavior absent from docs:

1. record as `CURRENT IMPLEMENTATION EVIDENCE`;
2. identify owner;
3. decide whether behavior is intentional;
4. promote only after explicit reconciliation.

Do not silently canonize accidental behavior.

---

# 86. Handling generated docs

Generated:

```text
OpenAPI
DB diagrams
coverage
typed API refs
generated registries/indexes
```

must state:

```text
GENERATED
SOURCE
COMMAND
DO NOT EDIT
```

Generated schema should not be manually copied into multiple docs.

---

# 87. Handling API docs

If OpenAPI exists:

```text
OpenAPI
→ machine-readable endpoint schema
```

Human docs may own:

```text
philosophy
versioning
error model
idempotency
cross-endpoint behavior
examples
migration/deprecation
```

---

# 88. Handling visual/UI documentation

Separate:

```text
UX Constitution
Design System Profile
Design System Operating Model
Design Handoff Standard
Design System Registry
Current UI Change Plan
Design decisions
Visual QA evidence
```

Never let screenshots alone define behavior.

---

# 89. Handling current-state audits

Audits require:

```text
date
repository baseline
environment
scope
limitations
```

They are reports/evidence.

Resolved audits may move to archive.

Do not place findings inside timeless constitutions.

---

# 90. Handling project size

## Starter/MVP

Target minimal set:

```text
README
docs/README
SOURCE_OF_TRUTH
PRODUCT_VISION
SCOPE
MASTER_ARCHITECTURE
FEATURE_SPECS
UX_CONSTITUTION
ENGINEERING_PRINCIPLES
TESTING
ACTIVE_PLAN
DECISIONS
LOCAL_SETUP
```

## Production

Add justified:

```text
DOMAIN_MODEL
DESIGN_SYSTEM
API_CONTRACTS
DATA_MODEL
SECURITY
ANALYTICS
DEPLOYMENT
ROLLBACK
RUNBOOKS
```

## Complex/regulated

Add:

```text
formal traceability
compliance
lineage
threat models
SLO/DR
RFC governance
manifest
integrity CI
evidence retention
```

---

# 91. Handling mobile products

Prioritize:

```text
navigation
deep links
offline/cache
state ownership
OS permissions
device support
release/store process
analytics
```

Design-system migration should capture:

```text
touch targets
platform modes
native/web differences
safe areas
keyboard behavior
```

where relevant.

---

# 92. Handling SaaS

Prioritize:

```text
tenancy
identity
authorization
billing
roles
audit
data ownership
export/delete
deployment
rollback
incident response
```

---

# 93. Handling API/platform

Prioritize:

```text
API contracts
versioning
idempotency
rate limits
errors
event contracts
SDK behavior
deprecation
```

---

# 94. Handling AI-heavy products

Prioritize:

```text
AI_SYSTEM_OVERVIEW
AI_PRINCIPLES
CONTEXT_ASSEMBLY
MODEL_PROVIDER_BOUNDARIES
PROMPT_CONTRACTS
HUMAN_APPROVAL
EVALS
SAFETY
AI_TELEMETRY
```

Explicitly define:

```text
what AI proposes
what AI executes
what requires human approval
what becomes permanent knowledge
what happens when AI is unavailable
```

---

# 95. Greenfield bootstrap — Mode D

For a new project:

## Step 1

Create:

```text
README
docs/README
SOURCE_OF_TRUTH
```

## Step 2

Create only:

```text
PRODUCT_VISION
SCOPE
MASTER_ARCHITECTURE
ACTIVE_PLAN
LOCAL_SETUP
```

## Step 3

Add Domain when domain complexity appears.

## Step 4

Add Feature Specs as capabilities are designed.

## Step 5

Add UX Constitution when product interaction language emerges.

## Step 6

Add Design System module when reusable UI/patterns emerge.

## Step 7

Add Quality/Security/Ops/Analytics layers according to real risk.

Do not scaffold 50 empty files on Day 1.

---

# 96. Incremental adoption — Mode E

For very large active repositories:

```text
New work
→ must use new documentation model.

Touched legacy area
→ reconcile nearby canonical docs.

Untouched legacy area
→ migrate later based on risk.
```

Maintain a migration backlog:

```text
P0 — high-risk contradictory truth
P1 — frequently changed areas
P2 — onboarding pain
P3 — historical cleanup
```

---

# 97. Migration report output

Final report should contain:

1. baseline;
2. mode;
3. documents discovered;
4. canonical docs established;
5. docs split;
6. docs merged;
7. docs moved/renamed;
8. docs superseded;
9. docs archived;
10. source-of-truth map;
11. unresolved conflicts;
12. missing high-priority docs;
13. implementation-vs-doc drift;
14. DS registry reconciliation if relevant;
15. manifest result;
16. integrity checks added;
17. recommended next PR;
18. product/engineering follow-ups.

---

# 98. Migration success metrics

Success is not:

```text
number of Markdown files
folder coverage
page count
```

Success is:

```text
fewer contradictions
clearer ownership
faster onboarding
safer changes
less AI invention
better traceability
easier discovery
clear separation of stable truth vs temporary work
```

---

# 99. Documentation integrity metrics after adoption

Useful:

```text
broken links
unowned active docs
duplicate active canonical scopes
overdue reviews
stale-review signals
superseded docs still linked as canonical
open blocking conflicts
manifest/path mismatches
DS registry/code mismatches
untested runbooks
traceability gaps
```

Avoid a fake single score.

---

# 100. Exact AI / Codex execution directive

The following can be supplied directly to an AI coding agent together with the Universal Project Documentation System.

```text
You are adopting the Universal Project Documentation System in this repository.

AUTHORITATIVE REFERENCES

1. README.md
2. 00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md
3. UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md

Open other standards only when the current phase requires them.

GOAL

Migrate project knowledge into a coherent governed documentation system without silently changing product semantics or implementation behavior.

DEFAULT MODE

Mode B — Documentation reconciliation with implementation verification.

You MAY inspect source code, tests, routes, schema, APIs, CI, configuration, design-system code, stories and deployment files to verify documentation claims.

You MUST NOT change product code, schema, routes, API behavior, domain semantics, permissions, lifecycle values, UI behavior or infrastructure unless a separate explicit task authorizes it.

PHASE A — BASELINE

1. Record branch, commit, date and working-tree state.
2. Record migration mode and versions of documentation standards.
3. Create/update MIGRATION_REPORT.md.
4. Do not reorganize yet.

PHASE B — DISCOVERY

1. Scan repository documentation and documentation-like artifacts.
2. Inspect structural implementation sources needed for verification.
3. Identify legacy MASTER/TZ files, plans, reports, decisions, UX/design docs and generated docs.

PHASE C — INVENTORY

Create DOCUMENTATION_INVENTORY.md.

For every meaningful document record:
- path
- class
- document lifecycle status
- normativity
- lifetime
- scope/layer
- owner
- freshness
- duplicates
- conflicts
- action
- target path

Allowed actions:
KEEP
MOVE
RENAME
SPLIT
MERGE
SUPERSEDE
ARCHIVE
DELETE

DELETE only exact low-value duplicates with no historical value.

PHASE D — SOURCE OF TRUTH

Create SOURCE_OF_TRUTH.md.

Authority is scoped:
Product → 01_product
Domain → 02_domain
Architecture → 03_architecture
Feature behavior → 04_product_specs
UX → 05_ux
Design System → 06_design_system
Engineering → 07_engineering
API/Data → 08_data_api
AI → 09_ai
Security → 10_security_privacy
Quality → 11_quality_testing
Analytics → 12_analytics
Operations → 13_operations
Decisions → 14_decisions
Current execution → 15_plans

Do not use one global source-of-truth ranking for every fact.

PHASE E — CONFLICT ANALYSIS

Create DOCUMENTATION_CONFLICTS.md.

Do not silently resolve active normative conflicts involving:
- product semantics
- permissions
- billing
- security/privacy
- destructive behavior
- domain lifecycles
- architecture ownership

Mark OWNER_DECISION_REQUIRED when necessary.

PHASE F — TARGET ARCHITECTURE

Create TARGET_DOCUMENTATION_ARCHITECTURE.md.

Tailor structure to actual project complexity.
Do not create empty ceremonial folders.

PHASE G — STABLE TRUTH EXTRACTION

Extract in dependency order:
1. Product
2. Domain
3. Architecture
4. Product Specs
5. UX
6. Design System
7. Engineering/Data/AI/Security
8. Quality/Analytics/Operations

Preserve confirmed semantics.
Normalize terminology only when unambiguous.
Mark uncertainty explicitly.
Do not invent missing truth.

PHASE H — DESIGN SYSTEM

If project has reusable UI, read:
- DESIGN_SYSTEM_OPERATING_MODEL_v1.1
- DESIGN_HANDOFF_STANDARD_v1.3
- DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0
- DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1

Separate:
- UX Constitution
- Design System Profile
- reusable DS objects
- whole screen/flow specs
- current UI migration plans
- visual QA reports
- design decisions

Create/reconcile REGISTRY.json.

Classify DS objects only as:
FOUNDATION
PRIMITIVE
COMPONENT
PATTERN
PAGE_GRAMMAR

Do not classify full screens/flows as DS canonical objects.

PHASE I — TEMPORARY EXECUTION

Move current implementation sequencing, redesign tasks and migration steps to 15_plans/.

Plans must state:
- baseline
- target
- owner
- completion condition
- archive action

PHASE J — DECISIONS

Extract durable non-obvious rationale into:
ADR
PDR
DDR
SDR

Do not create decision records for trivial edits.

PHASE K — SUPERSESSION / ARCHIVE

Do not delete legacy MASTER documents until unique information is preserved.

Add SUPERSEDED banners pointing to canonical replacements.

Archive only after:
- replacement exists
- links updated
- unique content verified

PHASE L — MANIFESTS

When structure is stable:
- create/validate DOCUMENT_MANIFEST.json for medium/large repos
- create/validate Design System REGISTRY.json where relevant

Do not merge the two metadata scopes.

PHASE M — ONBOARDING

Create:
- docs/README.md
- 16_onboarding/AI_AGENT_GUIDE.md

Define AI read order and anti-hallucination rules.

PHASE N — INTEGRITY

Add lightweight validation:
- internal links
- unique IDs
- valid statuses
- owners
- lifetimes
- supersession
- manifest consistency
- registry path consistency

PHASE O — FINAL RECONCILIATION

Verify:
- major truth has one canonical owner
- stable truth separated from plans
- historical docs visibly historical
- duplicate active truth resolved
- unresolved high-risk conflicts listed
- no accidental product semantics changes
- new contributors can navigate documentation
- AI agents can determine authority

OUTPUT

Return:
1. Baseline.
2. Inventory summary.
3. Files created.
4. Files moved/renamed.
5. Documents split/merged.
6. Documents superseded/archived.
7. Canonical Source-of-Truth map.
8. Unresolved conflicts.
9. Missing high-priority documentation.
10. Code-vs-doc drift.
11. Design-system reconciliation result.
12. Manifest/registry validation result.
13. Recommended next PR.
14. Product/engineering follow-up work.

IMPORTANT

Documentation migration is not a product redesign.
Unknown is better than fabricated completeness.
One fact gets one canonical owner.
Links are preferable to duplicated truth.
Archive is project memory, not trash.
```

---

# 101. Staged AI execution for large repositories

Do not ask one agent to migrate a huge repository in one pass.

## Stage 1 — Audit only

```text
Perform Phases 0–6.

Do not move/rewrite canonical docs.

Deliver:
- Inventory
- Conflict Register
- Target Architecture
- Source-of-Truth proposal
- Migration Report
- Proposed PR sequence
```

## Stage 2 — Governance only

```text
Create governance foundation.

Do not split major MASTER docs yet.
```

## Stage 3 — Product / Domain / Architecture

```text
Extract stable truth.
Preserve legacy docs as superseded candidates.
```

## Stage 4 — Product Specs / UX

```text
Decompose feature contracts and reconcile experience truth.
```

## Stage 5 — Design System

```text
Separate UX from DS.
Create/reconcile DS Profile, Registry, object taxonomy and Handoff contracts.
```

## Stage 6 — Technical layers

```text
Engineering / Data / AI / Security / Quality / Ops.
```

## Stage 7 — Decisions / Plans / Archive

```text
Extract rationale.
Separate current execution.
Archive superseded material.
```

## Stage 8 — Manifests / Integrity

```text
Create machine-readable manifests and CI checks.
```

---

# 102. Strategy for an already well-documented repository

Do not rewrite good documentation for template conformity.

Prefer:

```text
add governance
add index
add Source of Truth
add metadata
split only mixed docs
move only when ownership improves
archive true duplicates
add manifests
```

The goal is coherence, not cosmetic uniformity.

---

# 103. Strategy for a poorly documented repository

Start with high-value truth:

```text
Product Vision
Scope
Domain Model
Master Architecture
Feature specs for critical behavior
UX Constitution
Engineering Principles
Testing
Active Plan
```

Then grow according to risk.

Do not fabricate a 50-file documentation universe.

---

# 104. Strategy for monolithic MASTER/TЗ projects

Preserve original.

Map every meaningful section to canonical scope.

Extract in dependency order.

Verify no unique knowledge lost.

Mark original superseded.

Archive only after references are stable.

This is a semantic migration, not a heading split.

---

# 105. Adoption outcome

At completion, a contributor should know immediately where to look for:

```text
Why are we building this?
→ Product

What does this concept mean?
→ Domain

How is the system structured?
→ Architecture

How must this feature behave?
→ Product Spec

How should the experience work?
→ UX

What reusable UI already exists?
→ Design System / UI Kit

How should code be structured?
→ Engineering

What is the exact API/data contract?
→ Data/API

How is AI controlled?
→ AI

What security/privacy rules apply?
→ Security

How do we verify it?
→ Quality

How is success measured?
→ Analytics

How is it deployed/recovered?
→ Operations

Why was this decision made?
→ Decision History

What are we changing right now?
→ Plans
```

That is the intended adoption result.

---

# 106. Final migration principles

> **Inventory before reorganizing.**

> **Classify before moving.**

> **Map ownership before splitting.**

> **Separate stable truth from temporary execution.**

> **Preserve history until canonical extraction is verified.**

> **One fact should have one canonical owner.**

> **Links are preferable to duplicated truth.**

> **Unknown is preferable to invented certainty.**

> **Documentation migration must not silently redesign the product.**

> **Archive is memory, not trash.**

> **The final measure is not documentation volume; it is reduced ambiguity.**

===== END VIRTUAL FILE: UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md =====

---

## VIRTUAL FILE 3/56 — `CHANGELOG.md`

**Virtual path:** `CHANGELOG.md`  
**Content checksum:** `31f5bc36e35c`

===== BEGIN VIRTUAL FILE: CHANGELOG.md =====

# Universal Project Documentation System — Changelog

## 1.2.0 — 2026-09-19

### Added

- `00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md`
- `00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md`
- Explicit canonical-source resolution algorithm for humans and AI agents.
- Conflict taxonomy for scoped authority and code/document drift.
- Epistemic Knowledge Lifecycle from signal/observation through evidence, proposal, validation, canonical promotion, challenge, supersession and archive.
- AI knowledge-promotion boundaries and organizational learning loop.
- Formal integration points for the future U-POS Agent Organization, Context/Memory and Observability modules.

### Clarified

- The existing scoped Source-of-Truth rules remain authoritative; the new Source-of-Truth Model formalizes them as a reusable governance contract.
- Document lifecycle and Knowledge lifecycle are separate concepts.
- Evidence, Reports, Decisions and canonical truth have different authority roles.
- AI-generated observations/proposals are knowledge candidates, not automatic canonical truth.

## 1.1.1 — 2026-09-19

### Added

- `UNIVERSAL_PROJECT_DOCUMENTATION_IMPLEMENTATION_GUIDE_v2.0.md`
- Migration modes A–E, including Greenfield Bootstrap and Incremental Adoption.
- Dedicated Design System reconciliation phase.
- Explicit UX / Design System / Quality / Decisions / Plans migration boundaries.
- Document Manifest + Design System Registry adoption sequencing.
- AI/Codex staged migration directive.
- Freshness, traceability and separate document/object status migration rules.

### Adoption contract

The Operating Model defines the target state.

The Implementation Guide defines the safe migration/adoption procedure.

## 1.1.0 — 2026-09-19

### Architecture

- Established Universal Project Documentation System as the parent system.
- Made Design System a specialized Level-6 module.
- Separated UX/Experience truth from reusable Design System truth.
- Separated Quality evidence, Decision history, Current Plans and Contribution workflow from Design System.

### Added

- Project Documentation Operating Model v1.1
- Docs-as-Code Standard v1.0
- Project Documentation Catalog v1.0
- Project Documentation Profiles v1.0
- Document Manifest JSON Schema v1.0
- Design System Documentation Integration v1.0
- Design Decision Record template
- Review/freshness metadata
- Open Questions structure
- Design System traceability metadata

### Changed

- Project Design Constitution split into:
  - UX Constitution
  - Design System Profile
- Design System Registry upgraded to v1.1 with:
  - review metadata
  - freshness
  - traceability
- Design Handoff Standard upgraded to v1.3.
- UI Kit Web Specification upgraded to v1.2.
- Design System Operating Model upgraded to v1.1.

### Moved

- Content Design → UX
- Screen/Flow specs → Product Specs / UX
- Visual QA Report → Quality
- Design RFC / DDR → Decisions
- Current UI Change Plan → Plans
- UI PR Checklist → Onboarding

===== END VIRTUAL FILE: CHANGELOG.md =====

---

## VIRTUAL FILE 4/56 — `MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md`

**Virtual path:** `MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md`  
**Content checksum:** `27052612525a`

===== BEGIN VIRTUAL FILE: MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md =====

# Migration from Universal Design System Standard Pack v1

**ID:** DOC-MIG-001  
**Type:** PLAN  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance + Design System  
**Version:** 1.0.0  
**Lifetime:** TEMPORARY  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Migration completed  
**Supersedes:** —  
**Related:** —


# Purpose

Reconcile the earlier Design System-only package into the full Universal Project Documentation System.

---

# 1. Keep in Design System

```text
Design System Operating Model
Design Handoff Standard
UI Kit Web Specification
Design System Registry Schema
Component Spec Template
Pattern Spec Template
Page Grammar Spec Template
```

---

# 2. Split

Old:

```text
PROJECT_DESIGN_CONSTITUTION
```

New:

```text
05_ux/UX_CONSTITUTION
06_design_system/DESIGN_SYSTEM_PROFILE
```

Reason:

Experience laws and visual system have different ownership/lifetimes.

---

# 3. Move out of Design System

```text
CONTENT_DESIGN_GUIDE
→ 05_ux/

SCREEN_SPEC
→ 04_product_specs/

FLOW_SPEC
→ 04_product_specs/ / 05_ux/

VISUAL_QA_REPORT
→ 11_quality_testing/

DESIGN_RFC
→ 14_decisions/

CURRENT_UI_CHANGE_PLAN
→ 15_plans/

UI_PR_CHECKLIST
→ 16_onboarding/
```

---

# 4. Add

```text
DDR template
Design System README template
Design System Documentation Integration
Document Manifest Schema
Docs-as-Code Standard
Project Documentation Catalog
Project Documentation Profiles
review/freshness metadata
traceability metadata
Open Questions section
```

---

# 5. Lifecycle correction

Do not use Design System object status as document status.

Example:

```text
Document status: ACTIVE
Object lifecycle: IMPLEMENTED
```

---

# 6. Registry upgrade

Upgrade Design System Registry to v1.1:

- review metadata;
- freshness;
- traceability;
- canonical relationships;
- parity.

---

# 7. Completion criteria

Migration is complete when:

```text
[ ] Project Documentation Operating Model adopted
[ ] DS module contains only DS-owned truth
[ ] UX Constitution separated from visual DS Profile
[ ] temporary UI plans moved to Plans
[ ] visual QA moved to Quality
[ ] design RFC/DDR moved to Decisions
[ ] DS Registry uses v1.1 schema
[ ] docs index/source-of-truth map updated
```

===== END VIRTUAL FILE: MIGRATION_FROM_DESIGN_SYSTEM_PACK_v1.md =====

---

## VIRTUAL FILE 5/56 — `00_governance/DOCS_AS_CODE_STANDARD_v1.0.md`

**Virtual path:** `00_governance/DOCS_AS_CODE_STANDARD_v1.0.md`  
**Content checksum:** `c9738a7e7062`

===== BEGIN VIRTUAL FILE: 00_governance/DOCS_AS_CODE_STANDARD_v1.0.md =====

# Docs-as-Code Standard v1.0

**ID:** DOC-STD-002  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance / Engineering  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Documentation tooling, manifest, metadata, or integrity pipeline changes  
**Supersedes:** —  
**Related:** DOC-STD-001


# 1. Purpose

Define how project documentation is stored, indexed, validated, generated, and reviewed.

---

# 2. Repository-first default

Normative and living documentation SHOULD be:

- Markdown/MDX/structured text;
- version controlled;
- reviewed in PR;
- linkable;
- searchable;
- consumable by humans and AI agents.

Binary artifacts MAY accompany docs when they serve evidence or visual contracts.

---

# 3. Metadata header

Important docs SHOULD expose:

```text
ID
Type
Status
Normativity
Owner
Version
Lifetime
Created
Last reviewed
Review trigger
Supersedes
Related
```

Trivial guides MAY use reduced metadata.

---

# 4. IDs

Suggested prefixes:

```text
DOC
PROD
DOM
ARCH
SPEC
UX
DS
ENG
API
DATA
AI
SEC
QA
AN
OPS
ADR
PDR
DDR
SDR
RFC
PLAN
RUN
REF
```

IDs MUST be unique within a project when used.

---

# 5. Naming

Good:

```text
AUTHORIZATION.md
MASTER_ARCHITECTURE.md
CONTENT_DESIGN.md
DESIGN_HANDOFF_STANDARD.md
RELEASE_PROCESS.md
```

Bad:

```text
notes-final-v2.md
misc.md
important.md
new-final.md
```

Do not use `final` as lifecycle/version metadata.

---

# 6. Date naming

Use date prefixes for snapshots/reports:

```text
2026-09-19-performance-audit.md
```

Do not date-prefix timeless active standards by default.

---

# 7. Diagrams

Every diagram must answer a question.

Recommended maintainable formats:

```text
Mermaid flowchart
sequenceDiagram
stateDiagram-v2
erDiagram
```

Keep textual explanation.

A diagram is not self-explanatory documentation.

---

# 8. Screenshot policy

Use screenshots for:

- visual design contracts;
- visual QA evidence;
- UX audit evidence;
- operational instructions when stable.

Do not use screenshots as the sole behavioral source.

Important screenshots SHOULD include:

- version/baseline;
- environment/viewport where relevant.

---

# 9. Generated docs

Generated files MUST state:

```text
GENERATED FILE
Source: ...
Command: ...
Do not edit manually.
```

Generated artifacts SHOULD be regenerated, not patched.

---

# 10. Document manifest

Larger projects SHOULD maintain machine-readable:

```text
docs/DOCUMENT_MANIFEST.json
```

The manifest may drive:

- docs index;
- ownership checks;
- freshness checks;
- search;
- AI-agent retrieval;
- CI integrity.

Use `DOCUMENT_MANIFEST_SCHEMA_v1.0.json`.

---

# 11. CI integrity checks

Useful checks:

```text
broken internal links
missing required metadata
duplicate document IDs
invalid status/type/lifetime
ACTIVE doc superseded by another ACTIVE doc
missing owner
overdue review
orphaned canonical spec
invalid supersession link
deprecated API still referenced
missing changelog for breaking change
missing manifest entry
```

Only automate checks that provide real value.

---

# 12. Freshness automation

Freshness MUST NOT mutate semantic document status.

Example:

```text
Status: ACTIVE
Freshness: STALE_REVIEW_REQUIRED
```

Review dates/triggers may generate warnings.

---

# 13. Machine-generated index

`docs/README.md` MAY be partially generated from manifest.

Human-curated orientation SHOULD remain.

---

# 14. Changelogs

Use separate changelogs for separate scopes.

Examples:

```text
root CHANGELOG
→ product releases

design-system/CHANGELOG
→ design-system releases

API_CHANGELOG
→ breaking API contract changes
```

Do not mix unrelated scopes.

---

# 15. Link policy

Prefer repository-relative links for docs.

External links SHOULD have stable ownership where possible.

Broken links SHOULD fail/warn CI for normative docs.

---

# 16. Code ↔ docs references

Specs MAY expose:

```text
Implementation refs
Test refs
Telemetry refs
Decision refs
```

Do not hardcode volatile line numbers as permanent architecture truth.

---

# 17. Tool neutrality

The standard does not require a particular static-site generator.

Possible:

- GitHub Markdown;
- Docusaurus;
- MkDocs;
- Astro;
- Next.js;
- Storybook for Design System;
- custom docs portal.

Source truth remains in canonical docs/registries.

---

# 18. AI readability

Avoid:

- critical meaning encoded only in images;
- inconsistent headings;
- ambiguous status terms;
- unmarked historical content;
- hidden precedence.

Prefer:

- explicit metadata;
- stable headings;
- canonical links;
- machine-readable manifests;
- textual alternatives for visual artifacts.

---

# 19. Quality gate

For normative docs:

```text
[ ] purpose clear
[ ] owner clear
[ ] scope clear
[ ] out-of-scope clear
[ ] status clear
[ ] lifetime clear
[ ] terms defined
[ ] canonical links correct
[ ] temporary details excluded
[ ] conflicts resolved
[ ] acceptance/testability present where relevant
```

===== END VIRTUAL FILE: 00_governance/DOCS_AS_CODE_STANDARD_v1.0.md =====

---

## VIRTUAL FILE 6/56 — `00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json`

**Virtual path:** `00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json`  
**Content checksum:** `8198ec43c74c`

===== BEGIN VIRTUAL FILE: 00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json =====

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/document-manifest.schema.v1.json",
  "title": "Universal Project Document Manifest v1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "project",
    "documents"
  ],
  "properties": {
    "schemaVersion": {
      "const": "1.0.0"
    },
    "project": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^[a-z0-9][a-z0-9-]*$"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "docsRoot": {
          "type": [
            "string",
            "null"
          ]
        },
        "sourceOfTruthPath": {
          "type": [
            "string",
            "null"
          ]
        },
        "docsIndexPath": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/document"
      }
    }
  },
  "$defs": {
    "docType": {
      "enum": [
        "CONSTITUTION",
        "MASTER",
        "CONTRACT",
        "SPECIFICATION",
        "STANDARD",
        "PLAN",
        "RFC",
        "DECISION_RECORD",
        "RUNBOOK",
        "GUIDE",
        "REFERENCE",
        "REPORT",
        "EVIDENCE",
        "GENERATED",
        "ARCHIVE"
      ]
    },
    "status": {
      "enum": [
        "DRAFT",
        "REVIEW",
        "APPROVED",
        "ACTIVE",
        "DEPRECATED",
        "SUPERSEDED",
        "ARCHIVED"
      ]
    },
    "normativity": {
      "enum": [
        "NORMATIVE",
        "INFORMATIVE",
        "EVIDENCE",
        "GENERATED"
      ]
    },
    "lifetime": {
      "enum": [
        "STABLE",
        "LIVING",
        "TEMPORARY",
        "HISTORICAL"
      ]
    },
    "freshness": {
      "enum": [
        "CURRENT",
        "REVIEW_DUE",
        "STALE_REVIEW_REQUIRED",
        "NOT_APPLICABLE"
      ]
    },
    "document": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "path",
        "type",
        "status",
        "normativity",
        "owner",
        "lifetime"
      ],
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "title": {
          "type": [
            "string",
            "null"
          ]
        },
        "path": {
          "type": "string",
          "minLength": 1
        },
        "type": {
          "$ref": "#/$defs/docType"
        },
        "status": {
          "$ref": "#/$defs/status"
        },
        "normativity": {
          "$ref": "#/$defs/normativity"
        },
        "owner": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": [
            "string",
            "null"
          ]
        },
        "lifetime": {
          "$ref": "#/$defs/lifetime"
        },
        "canonicalScope": {
          "type": [
            "string",
            "null"
          ]
        },
        "created": {
          "type": [
            "string",
            "null"
          ],
          "format": "date"
        },
        "lastReviewed": {
          "type": [
            "string",
            "null"
          ],
          "format": "date"
        },
        "reviewTrigger": {
          "type": [
            "string",
            "null"
          ]
        },
        "freshness": {
          "$ref": "#/$defs/freshness"
        },
        "supersedes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "supersededBy": {
          "type": [
            "string",
            "null"
          ]
        },
        "related": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "implementationRefs": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "testRefs": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "evidenceRefs": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "generated": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "isGenerated": {
              "type": "boolean"
            },
            "source": {
              "type": [
                "string",
                "null"
              ]
            },
            "command": {
              "type": [
                "string",
                "null"
              ]
            }
          }
        }
      }
    }
  }
}

===== END VIRTUAL FILE: 00_governance/DOCUMENT_MANIFEST_SCHEMA_v1.0.json =====

---

## VIRTUAL FILE 7/56 — `00_governance/PROJECT_DOCUMENTATION_CATALOG_v1.0.md`

**Virtual path:** `00_governance/PROJECT_DOCUMENTATION_CATALOG_v1.0.md`  
**Content checksum:** `6a65f84a4057`

===== BEGIN VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_CATALOG_v1.0.md =====

# Project Documentation Catalog v1.0

**ID:** DOC-REF-001  
**Type:** REFERENCE  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** LIVING  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** A new canonical documentation class/layer is introduced  
**Supersedes:** —  
**Related:** DOC-STD-001


# Purpose

This catalog answers:

> What kinds of project documentation may exist, who owns them, and when are they warranted?

It is not a command to create every file.

---

# 1. Governance

Typical:

```text
docs/README.md
SOURCE_OF_TRUTH.md
DOCUMENTATION_OPERATING_MODEL.md
DOCS_AS_CODE_STANDARD.md
GLOSSARY.md
DOCUMENT_MANIFEST.json
TRACEABILITY.md
```

Create when:

- project has multiple active document classes;
- multiple contributors/AI agents need precedence;
- documentation drift becomes costly.

---

# 2. Product

Typical:

```text
PRODUCT_VISION.md
PRODUCT_PRINCIPLES.md
USER_PROBLEMS_JTBD.md
PERSONAS.md
SCOPE.md
SUCCESS_CRITERIA.md
BUSINESS_RULES.md
```

Owner:

```text
Product
```

Purpose:

- why product exists;
- who it serves;
- outcomes;
- product boundaries.

---

# 3. Domain

Typical:

```text
DOMAIN_MODEL.md
DOMAIN_GLOSSARY.md
ENTITY_CATALOG.md
LIFECYCLES.md
OWNERSHIP_BOUNDARIES.md
INVARIANTS.md
```

Owner:

```text
Domain / Architecture
```

Purpose:

- canonical meaning independent of UI/database.

---

# 4. Architecture

Typical:

```text
MASTER_ARCHITECTURE.md
SYSTEM_CONTEXT.md
CONTAINER_VIEW.md
COMPONENT_VIEW.md
DATA_FLOW.md
TRUST_BOUNDARIES.md
NON_FUNCTIONAL_REQUIREMENTS.md
```

Architecture decisions live under Decision History.

---

# 5. Product / Feature Contracts

Typical feature folder:

```text
feature/
├── PRODUCT_SPEC.md
├── UX_FLOW.md
├── API_CONTRACT.md
├── TEST_MATRIX.md
└── assets/
```

Small features MAY use one file.

Feature spec owns feature behavior, not global architecture.

---

# 6. UX / Experience

Typical:

```text
UX_CONSTITUTION.md
INFORMATION_ARCHITECTURE.md
NAVIGATION_MODEL.md
USER_FLOWS.md
CONTENT_DESIGN.md
ACCESSIBILITY_UX.md
research/
```

UX owns:

- experience principles;
- navigation semantics;
- information hierarchy;
- user-flow intent;
- product language.

UX does not own backend/domain truth.

---

# 7. Design System

Canonical module:

```text
DESIGN_SYSTEM_OPERATING_MODEL.md
DESIGN_HANDOFF_STANDARD.md
UI_KIT_WEB_SPECIFICATION.md
DESIGN_SYSTEM_PROFILE.md
REGISTRY.json
CHANGELOG.md
foundations/
primitives/
components/
patterns/
page-grammars/
boards/
implemented/
deprecated/
```

Design System owns reusable visual/interaction language.

It does not own whole product flows or temporary migration plans.

---

# 8. Engineering

Typical:

```text
ENGINEERING_PRINCIPLES.md
CODEBASE_GUIDE.md
FRONTEND_ARCHITECTURE.md
BACKEND_ARCHITECTURE.md
STATE_MANAGEMENT.md
ERROR_HANDLING.md
CONCURRENCY_IDEMPOTENCY.md
JOBS_WORKERS.md
STORAGE_MEDIA.md
INTEGRATIONS.md
OBSERVABILITY.md
PERFORMANCE.md
coding-standards/
```

---

# 9. Data / API / Integration

Typical:

```text
DATA_MODEL.md
DATABASE_SCHEMA.md
API_CONTRACTS.md
EVENT_CONTRACTS.md
DATA_MIGRATIONS.md
RETENTION.md
IMPORT_EXPORT.md
API_VERSIONING.md
```

Prefer generated OpenAPI/DB diagrams where appropriate, with human context separately.

---

# 10. AI

Create only when AI materially affects product/system.

Typical:

```text
AI_SYSTEM_OVERVIEW.md
AI_PRINCIPLES.md
MODEL_PROVIDER_BOUNDARIES.md
PROMPT_CONTRACTS.md
CONTEXT_ASSEMBLY.md
HUMAN_APPROVAL.md
EVALS.md
SAFETY_GUARDRAILS.md
AI_TELEMETRY.md
```

---

# 11. Security / Privacy

Typical:

```text
SECURITY_MODEL.md
THREAT_MODEL.md
AUTHENTICATION.md
AUTHORIZATION.md
SECRETS.md
PRIVACY.md
DATA_CLASSIFICATION.md
AUDIT_LOGGING.md
compliance/
```

---

# 12. Quality / Testing

Typical:

```text
QUALITY_STRATEGY.md
TESTING_STANDARD.md
TEST_PYRAMID.md
E2E.md
ACCESSIBILITY_TESTING.md
PERFORMANCE_TESTING.md
VISUAL_REGRESSION.md
TEST_DATA.md
DEFINITION_OF_DONE.md
reports/
evidence/
```

Reports/evidence are not design-system truth.

---

# 13. Analytics / Telemetry

Typical:

```text
ANALYTICS_STRATEGY.md
EVENT_TAXONOMY.md
METRIC_CATALOG.md
KPI_DEFINITIONS.md
EXPERIMENTATION.md
ATTRIBUTION.md
DATA_QUALITY.md
```

---

# 14. Operations / Release

Typical:

```text
ENVIRONMENTS.md
DEPLOYMENT.md
RELEASE_PROCESS.md
ROLLBACK.md
BACKUP_RESTORE.md
INCIDENT_RESPONSE.md
SLO_SLI.md
ON_CALL.md
runbooks/
```

Runbooks should be tested.

---

# 15. Decisions

Typical:

```text
architecture/ADR-...
product/PDR-...
design/DDR-...
security/SDR-...
rfcs/
```

Preserve why.

---

# 16. Plans / Current Execution

Typical:

```text
ACTIVE_PLAN.md
migrations/
redesign/
rollout/
completed/
```

Plans are temporary.

---

# 17. Onboarding / Contribution

Typical:

```text
START_HERE.md
LOCAL_SETUP.md
REPOSITORY_TOUR.md
FIRST_PR.md
AI_AGENT_GUIDE.md
TROUBLESHOOTING.md
```

---

# 18. Reference

Typical:

```text
ROUTES.md
ENV_VARS.md
ERROR_CODES.md
FEATURE_FLAGS.md
THIRD_PARTY_SERVICES.md
COMMANDS.md
```

---

# 19. Archive

Archive:

- superseded architecture;
- completed plans;
- historical audits;
- old design-system versions;
- retired specs.

Archive preserves context but is not active instruction.

===== END VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_CATALOG_v1.0.md =====

---

## VIRTUAL FILE 8/56 — `00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md`

**Virtual path:** `00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md`  
**Content checksum:** `ca24e5648077`

===== BEGIN VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md =====

# Universal Project Documentation Operating Model v1.1

**ID:** DOC-STD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.1.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Documentation architecture, lifecycle, precedence, or governance model changes  
**Supersedes:** —  
**Related:** DOC-STD-002, DOC-REF-001, DOC-REF-002


## 0. Purpose

This standard defines:

- what classes of documentation exist;
- which layer owns which truth;
- how documents relate;
- how conflicts are resolved;
- how documents evolve;
- how staleness is detected;
- how decisions are preserved;
- how humans and AI agents determine authority.

It does **not** require maximal documentation.

It requires **minimal ambiguity**.

---

# 1. Normative language

- **MUST / MUST NOT** — required.
- **SHOULD / SHOULD NOT** — default recommendation; deviation requires reason.
- **MAY** — optional.

---

# 2. Layer model

```text
0  Governance
1  Product
2  Domain
3  Architecture
4  Product / Feature Contracts
5  UX / Experience
6  Design System
7  Engineering
8  Data / API / Integrations
9  AI
10 Security / Privacy / Compliance
11 Quality / Testing
12 Analytics / Telemetry
13 Operations / Release
14 Decision History
15 Current Execution
16 Onboarding / Contribution
17 Reference
99 Archive
```

The model is modular.

A small project MAY combine files while preserving **ownership boundaries**.

---

# 3. Documentation classes

Every important document SHOULD have a class.

```text
CONSTITUTION
MASTER
CONTRACT
SPECIFICATION
STANDARD
PLAN
RFC
DECISION_RECORD
RUNBOOK
GUIDE
REFERENCE
REPORT
EVIDENCE
GENERATED
ARCHIVE
```

## Constitution

Durable principles.

Answers:

> What should remain true even as implementation changes?

## Master

Canonical high-level system model.

Answers:

> What is the system structurally?

## Contract

Exact boundary shared by multiple parties.

Answers:

> What must both sides agree on?

## Specification

One capability in enough detail to implement and validate.

Answers:

> Exactly how must this capability behave?

## Standard

Reusable method or quality bar.

Answers:

> How do we consistently do this kind of work?

## Plan

Current/future execution.

Answers:

> How are we moving from current state to target state?

Plans are disposable.

## RFC

Proposal before a significant decision.

## Decision Record

Durable memory of accepted/rejected choice and rationale.

## Runbook

Operational procedure.

## Guide

Routine contributor instruction.

## Reference

Canonical lookup information.

## Report

Point-in-time analysis.

## Evidence

Screenshots, traces, benchmark output, test reports, research recordings, etc.

## Generated

Derived from code/schema/tooling.

## Archive

Historical, not active instruction.

---

# 4. Normativity

Every important document SHOULD state:

```text
NORMATIVE
INFORMATIVE
EVIDENCE
GENERATED
```

Normativity and lifecycle status are different dimensions.

---

# 5. Lifetime

Every important document SHOULD state:

```text
STABLE
LIVING
TEMPORARY
HISTORICAL
```

## Stable

Changes rarely; event-triggered review.

## Living

Continuously maintained with product/system.

## Temporary

Expected to complete/archive.

## Historical

Preserved for traceability.

---

# 6. Document lifecycle

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ SUPERSEDED
→ ARCHIVED
```

`STALE` is not a semantic lifecycle status.

Use a freshness signal instead.

---

# 7. Freshness

Recommended maintenance state:

```text
CURRENT
REVIEW_DUE
STALE_REVIEW_REQUIRED
NOT_APPLICABLE
```

An `ACTIVE` document can be overdue for review without ceasing to be authoritative.

---

# 8. Required metadata

For important normative/living documents:

```text
ID
Type
Status
Normativity
Owner
Version
Lifetime
Created
Last reviewed
Review trigger
Supersedes
Related
```

Optional:

```text
Superseded by
Canonical scope
Implementation refs
Evidence refs
Freshness
```

---

# 9. Scoped source of truth

No document wins globally.

For the complete authority-resolution contract, conflict taxonomy, canonical-source algorithm, and AI behavior, use:

```text
PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md
```

For how observations/evidence become decisions, canonical knowledge, learnings, superseded knowledge, and project memory, use:

```text
PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md
```

Examples:

```text
Product principles
→ product layer

Subscription lifecycle
→ domain layer

Service ownership
→ architecture layer

Search behavior
→ feature spec

Navigation semantics
→ UX

Button visual contract
→ design system

HTTP response schema
→ API contract

Deployment command
→ operations
```

A lower-level document MAY refine local detail.

It MUST NOT silently contradict the canonical owner.

---

# 10. Conflict resolution

When two active docs conflict:

1. identify the exact fact;
2. identify canonical scope owner;
3. check accepted decisions;
4. do not average conflicting instructions;
5. update/supersede losing document;
6. record a decision if conflict reveals a missing rule.

Known contradictions MUST NOT remain unresolved.

---

# 11. Stable vs temporary separation

MUST split when a document mixes:

- timeless principle + current task;
- architecture + current migration;
- stable product behavior + implementation sequence;
- contract + audit evidence;
- current status + historical decision memory.

Examples:

```text
UX_CONSTITUTION
≠
UI_REDESIGN_PLAN

MASTER_ARCHITECTURE
≠
MIGRATION_PLAN

API_CONTRACT
≠
API_AUDIT_REPORT
```

---

# 12. Duplication rule

Duplication is acceptable only for:

- short orientation;
- context;
- navigation.

Duplicated summaries SHOULD link canonical source.

Do not copy entire contract sections into many specs.

---

# 13. Dependency direction

Preferred:

```text
Principles
↓
Domain / Architecture
↓
Contracts / Specifications
↓
Implementation Standards
↓
Plans
↓
Evidence / Reports
```

Foundational documents MUST NOT depend on temporary plans.

---

# 14. Document ownership

Every normative or living document MUST have an owner.

Owner may be a role:

```text
Product
Architecture
Frontend
Backend
Design System
Security
Data
SRE
QA
```

Unowned documents decay.

---

# 15. Review triggers

Prefer event-driven review.

Examples:

```text
MASTER_ARCHITECTURE
→ new service
→ new storage
→ auth model change
→ new bounded context

UX_CONSTITUTION
→ global navigation change
→ major interaction-grammar change

DESIGN_SYSTEM_OPERATING_MODEL
→ lifecycle/governance/registry model change

SECURITY_MODEL
→ new trust boundary
→ new sensitive data
→ major external integration
```

Periodic audits are still useful.

---

# 16. Versioning documents

Use semantic intent.

## Major

- breaking contract;
- changed core semantics;
- changed architecture boundary.

## Minor

- compatible addition;
- new subsection;
- clarified rule with material value.

## Revision

- typo;
- link;
- formatting;
- non-semantic cleanup.

Not every small guide needs explicit semver.

Git history may be sufficient.

---

# 17. Decision memory

Use:

```text
ADR — Architecture Decision Record
PDR — Product Decision Record
DDR — Design Decision Record
SDR — Security Decision Record
```

Decision records SHOULD be immutable except:

- status;
- links;
- supersession metadata.

Chats are discovery, not durable decision memory.

---

# 18. RFC → decision

Use RFC **before** significant change.

Use a Decision Record **after** acceptance when durable rationale matters.

```text
RFC
→ discussion
→ accepted/rejected
→ decision record
→ implementation
```

Not every small change needs an RFC.

---

# 19. Plans

Plans MUST state:

```text
Status
Baseline
Target
Owner
Start
Completion condition
Archive action
```

A completed plan SHOULD be archived.

The desired behavior belongs in contracts/specs, not only in plan.

---

# 20. Reports

Point-in-time reports MUST declare:

```text
Date
Baseline
Environment
Method/scope
Limitations
```

Reports are evidence, not timeless doctrine.

---

# 21. Open questions

Unresolved questions SHOULD be either:

- local to owning spec; or
- centralized with links.

Recommended fields:

```text
Question
Owner
Opened
Blocking?
Decision deadline
Status
Resolution link
```

Resolved questions SHOULD become decisions/contracts.

---

# 22. Documentation debt

Track material documentation debt.

Example:

```text
DOC-DEBT-012
Problem:
API errors documented inconsistently.

Impact:
AI agents invent behavior.

Owner:
Backend.

Target:
v1.8
```

Do not create debt tickets for trivial typos.

---

# 23. Traceability

High-risk/complex projects SHOULD support:

```text
User problem
↓
Requirement
↓
Feature spec
↓
Domain / architecture contract
↓
Implementation
↓
Tests
↓
Telemetry
↓
Decision / learning
```

Requirement IDs are optional for small products.

---

# 24. Docs as code

Normative/living docs SHOULD:

- live in version control;
- be reviewed in PR;
- use stable links;
- use maintainable diagrams;
- separate generated docs;
- expose machine-readable indexes when useful.

Detailed practices belong to `DOCS_AS_CODE_STANDARD_v1.0.md`.

---

# 25. AI agent rules

AI agents MUST:

1. read documentation map;
2. read source-of-truth map;
3. search existing docs/code before creating;
4. identify canonical owner;
5. preserve domain semantics;
6. report unresolved contradictions;
7. update canonical docs when behavior changes and authorization allows.

AI agents MUST NOT invent for convenience:

- routes;
- entities;
- DB fields;
- API endpoints;
- status values;
- permissions;
- metrics;
- feature flags;
- design-system objects.

---

# 26. Drift taxonomy

Projects SHOULD detect meaningful:

```text
DOC DRIFT
IMPLEMENTATION DRIFT
PRODUCT DRIFT
SCHEMA DRIFT
DESIGN DRIFT
OPERATIONS DRIFT
```

Each drift type should have a detection/reconciliation path.

---

# 27. Definition of Ready for implementation

A feature is ready when relevant risk is resolved:

```text
[ ] problem/user job known
[ ] scope/non-goals known
[ ] domain semantics known
[ ] architecture impact resolved
[ ] UX flow sufficiently resolved
[ ] API/data contract sufficiently resolved
[ ] security/privacy reviewed where relevant
[ ] acceptance criteria exist
[ ] blocking questions resolved
```

Not every feature needs every document.

---

# 28. Documentation Definition of Done

A documentation change is done when:

```text
[ ] canonical owner updated
[ ] duplicated truth reconciled
[ ] references fixed
[ ] metadata updated
[ ] superseded docs marked
[ ] generated docs/tests updated if relevant
[ ] index/manifest updated if discoverability changed
```

---

# 29. PR documentation impact

Significant PRs SHOULD answer:

```text
Product behavior changed?
Architecture changed?
API/data changed?
UX/design-system changed?
Security/privacy changed?
Operations changed?
Which canonical docs changed?
Decision record needed?
```

---

# 30. Archive

Archive rather than delete when historical reasoning is valuable.

Archived docs MUST state:

```text
Status: ARCHIVED / SUPERSEDED
Superseded by: ...
Archived at: ...
```

Delete only when:

- pure duplicate;
- no unique historical value;
- no external references;
- replacement fully preserves necessary context.

---

# 31. Health measures

Useful signals:

```text
broken links
overdue reviews
unowned active docs
duplicate active specs
deprecated references
open blocking questions
orphaned contracts
untested runbooks
traceability gaps
manifest mismatches
```

Avoid fake aggregate documentation scores.

---

# 32. Maturity model

```text
Level 0 — Tribal
Level 1 — Files
Level 2 — Indexed
Level 3 — Governed
Level 4 — Traceable
Level 5 — Self-checking
```

Not every area must be Level 5.

---

# 33. Golden rules

> **A fact has one canonical owner.**

> **Plans are disposable. Contracts are not.**

> **Preserve why, not only what.**

> **If an AI agent cannot determine authority, documentation architecture is incomplete.**

> **Complexity may live in architecture/documentation; ambiguity should not leak into implementation.**

===== END VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_OPERATING_MODEL_v1.1.md =====

---

## VIRTUAL FILE 9/56 — `00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md`

**Virtual path:** `00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md`  
**Content checksum:** `06913d3ba358`

===== BEGIN VIRTUAL FILE: 00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md =====

# Project Source-of-Truth Model v1.0

**ID:** DOC-GOV-SOT-001  
**Type:** STANDARD / GOVERNANCE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Changes to documentation authority, ownership, conflict resolution, decision precedence, or canonicalization policy  
**Supersedes:** —  
**Related:** DOC-STD-001, `templates/SOURCE_OF_TRUTH_TEMPLATE.md`, PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md

---

## 0. Purpose

This standard defines the universal model for determining:

- which project source owns a fact;
- which statement is authoritative when multiple sources exist;
- how local specifications refine upstream truth;
- how accepted decisions affect canonical documentation;
- how implementation evidence participates without automatically becoming doctrine;
- how conflicts are detected, classified, resolved, and recorded;
- how humans and AI agents identify the correct source before acting.

The governing principle is:

> **Authority is scoped. No single project document is globally authoritative for every kind of truth.**

This model operationalizes the Source-of-Truth rules already present in the Project Documentation Operating Model.

---

# 1. What “Source of Truth” means

A Source of Truth is not simply:

> “the newest file”

and not:

> “the biggest MASTER document”

and not:

> “whatever the code currently does.”

A Source of Truth is:

> **the currently authorized canonical owner of a defined class of project facts.**

Examples:

```text
Product direction
→ Product

Domain lifecycle
→ Domain

Service ownership
→ Architecture

Feature-specific behavior
→ Product Spec

Navigation semantics
→ UX

Reusable component behavior
→ Design System

Wire schema
→ API/Data

Authorization policy
→ Security

Current migration sequence
→ Plan
```

---

# 2. Core entities

The model distinguishes the following concepts.

## 2.1 Claim

A statement asserting that something is true.

Example:

```text
A published revision is immutable.
```

## 2.2 Fact scope

The authority domain that should own the claim.

Example:

```text
published revision lifecycle
→ Domain
```

## 2.3 Canonical owner

The project layer or explicitly delegated document responsible for authoritative truth in that scope.

## 2.4 Canonical source

The active normative document, contract, registry, schema, or decision that expresses the canonical owner's current truth.

## 2.5 Refinement

A narrower rule that adds local detail without contradicting the upstream owner.

Example:

```text
Global:
Destructive actions require confirmation.

Feature:
Deleting a workspace requires typing the workspace name.
```

## 2.6 Conflict

Two active sources make incompatible claims about the same fact.

## 2.7 Evidence

Observed information about implementation, runtime, research, tests, analytics, incidents, or users.

Evidence can challenge canonical truth.

Evidence does not automatically become canonical truth.

## 2.8 Decision

An accepted choice that may create, change, or supersede canonical truth.

A Decision Record preserves why.

The owning canonical document preserves what is currently true.

---

# 3. Scoped authority map

Default universal ownership:

```text
Product / business truth
→ 01_product/

Domain semantics / lifecycles / invariants
→ 02_domain/

Architecture ownership / boundaries / topology
→ 03_architecture/

Feature-specific behavior
→ 04_product_specs/

UX / IA / navigation / user flows / content language
→ 05_ux/

Reusable visual / interaction system
→ 06_design_system/

Engineering implementation standards
→ 07_engineering/

API / data / integrations
→ 08_data_api/

AI system contracts
→ 09_ai/

Security / privacy / compliance
→ 10_security_privacy/

Quality strategy / test evidence
→ 11_quality_testing/

Analytics / metrics
→ 12_analytics/

Operations / release / restore / incident procedures
→ 13_operations/

Decision rationale
→ 14_decisions/

Current execution / migrations / sequencing
→ 15_plans/

Contributor guidance
→ 16_onboarding/

Lookup/reference
→ 17_reference/

Historical/superseded material
→ 99_archive/
```

A concrete project MAY adapt this map.

Any adaptation MUST be explicit in the project's `SOURCE_OF_TRUTH.md`.

---

# 4. Authority is by scope, not by folder number

The layer numbers provide organization.

They do not mean:

```text
01_product always overrides 10_security
```

That would be incorrect.

Examples:

```text
Product says:
Users should be able to export data.

Security says:
Export requires recent re-authentication.

Result:
No conflict.
Security refines the protected execution condition.
```

Another example:

```text
Feature Spec says:
Any authenticated user may delete an Organization.

Authorization Contract says:
Only Organization Owner may delete it.

Result:
Real conflict.
Security/Authorization owns permission semantics.
Feature Spec must be corrected.
```

---

# 5. Canonicality dimensions

A source is authoritative only when the relevant dimensions are satisfied.

Recommended evaluation:

```text
Scope ownership
Status
Normativity
Freshness
Specificity
Accepted decisions
Version compatibility
```

## 5.1 Scope ownership

Most important.

A document outside the owning scope cannot silently redefine upstream truth.

## 5.2 Status

Typical authority:

```text
ACTIVE
> APPROVED for future target state
> REVIEW / DRAFT
> DEPRECATED
> SUPERSEDED
> ARCHIVED
```

Do not use this as a blind global ranking.

An `APPROVED` target architecture may intentionally describe future state while current `ACTIVE` operations still describe production.

## 5.3 Normativity

```text
NORMATIVE
```

can own a contract.

```text
EVIDENCE
REPORT
INFORMATIVE
```

can inform/challenge it but do not automatically override it.

## 5.4 Freshness

A stale source may require review.

Staleness does not itself authorize another scope to take ownership.

## 5.5 Specificity

A local source may refine the owner when explicitly permitted.

Specificity cannot justify contradiction.

---

# 6. Canonical source resolution algorithm

Humans and AI agents SHOULD use this sequence before changing important behavior.

```text
1. Identify the exact claim/fact being decided.
2. Classify its fact scope.
3. Resolve the canonical owner for that scope.
4. Locate ACTIVE normative source(s) from that owner.
5. Check accepted Decision Records that affect the claim.
6. Check narrower feature/local contracts for valid refinement.
7. Check version/baseline applicability.
8. Compare implementation/runtime evidence.
9. If aligned → proceed.
10. If implementation differs → record drift.
11. If canonical sources disagree → register conflict.
12. If no owner/source exists → mark UNKNOWN / OWNER DECISION REQUIRED.
```

Do not skip directly from:

```text
"I found code that does X"
```

to:

```text
"Therefore X is product truth."
```

---

# 7. Refinement rule

A child/local contract MAY add detail when all are true:

```text
same upstream semantics preserved
no invariant is violated
no permission is weakened
no lifecycle transition is invented
no API/data contract is contradicted
no security/privacy constraint is bypassed
```

Good:

```text
UX Constitution:
Errors must provide recovery when recoverable.

Upload Feature Spec:
On transient upload failure show Retry.
```

Bad:

```text
Security:
Deletion requires Owner permission.

Feature Spec:
Editor may delete from this screen.
```

---

# 8. Decision precedence

A Decision Record is historical rationale.

It does not replace the canonical contract forever.

Correct sequence:

```text
RFC / evidence
→ Decision
→ ADR/PDR/DDR/SDR
→ canonical owner updated
```

After promotion:

```text
Canonical document
= current truth

Decision Record
= why it became truth
```

If an accepted decision has not yet been propagated into its canonical owner:

```text
state = OUT_OF_SYNC
```

The discrepancy must be reconciled.

---

# 9. Implementation evidence

Implementation is a critical evidence source.

It can prove:

```text
what currently happens
what schema currently exists
what route currently exists
what tests currently enforce
```

It cannot alone prove:

```text
what product behavior should be
what policy is intended
what future architecture is approved
what security permission should be
```

Use three possible drift interpretations:

```text
DOC_DRIFT
Documentation is stale.

IMPLEMENTATION_DRIFT
Implementation violates confirmed contract.

TRANSITIONAL_DRIFT
An approved migration is intentionally incomplete.
```

Do not automatically assume either docs or code wins.

---

# 10. Generated contracts

Generated artifacts may be canonical for their specific machine contract when explicitly designated.

Examples:

```text
OpenAPI
→ HTTP wire schema

database migration/schema
→ deployed storage shape

generated protobuf schema
→ message shape
```

But:

```text
Database schema
≠ Domain Model

OpenAPI
≠ Product behavior

Storybook
≠ complete UX Constitution
```

Machine truth remains scoped.

---

# 11. Conflict taxonomy

## SOT-C1 — Duplicate aligned

Two sources repeat the same fact.

Action:

```text
choose owner
replace duplicate with link/summary
```

## SOT-C2 — Historical conflict

Old/historical source contradicts active truth.

Action:

```text
mark/archive/supersede
repair references
```

## SOT-C3 — Local refinement ambiguity

Unclear whether local detail refines or contradicts upstream truth.

Action:

```text
owner review
```

## SOT-C4 — Active normative conflict

Two active authoritative-looking sources disagree.

Action:

```text
BLOCK affected change
identify owner
resolve explicitly
```

## SOT-C5 — Code/document drift

Implementation differs from canonical contract.

Action:

```text
classify DOC_DRIFT / IMPLEMENTATION_DRIFT / TRANSITIONAL_DRIFT
```

## SOT-C6 — Missing owner

Important fact has no canonical owner.

Action:

```text
OWNER DECISION REQUIRED
```

## SOT-C7 — Accepted decision not propagated

Decision exists but current canonical docs do not reflect it.

Action:

```text
reconcile canonical owner
```

---

# 12. High-risk conflict rule

The following conflicts MUST NOT be silently resolved by an AI agent:

```text
billing/money
authentication
authorization
privacy
retention
destructive actions
data ownership
domain lifecycle
compliance
production safety
irreversible migration
```

Required:

```text
explicit owner or human governance decision
```

---

# 13. Project `SOURCE_OF_TRUTH.md`

Every non-trivial instantiated project SHOULD have:

```text
docs/00_governance/SOURCE_OF_TRUTH.md
```

It is a project adapter of this universal model.

It should declare:

```text
Scope
Canonical owner
Canonical path/source
Status
Notes / refinements
```

Recommended table:

```markdown
| Scope | Canonical owner | Canonical source | Notes |
|---|---|---|---|
| Product principles | Product | docs/01_product/PRODUCT_PRINCIPLES.md | |
| Domain lifecycles | Domain | docs/02_domain/LIFECYCLES.md | |
| Architecture | Architecture | docs/03_architecture/MASTER_ARCHITECTURE.md | |
```

The existing `SOURCE_OF_TRUTH_TEMPLATE.md` is the starter template.

---

# 14. Source-of-Truth Registry entry

For larger projects, a machine-readable record MAY include:

```json
{
  "scope": "domain.lifecycle.subscription",
  "owner": "Domain",
  "canonicalSource": "docs/02_domain/LIFECYCLES.md",
  "status": "ACTIVE",
  "normativity": "NORMATIVE",
  "relatedDecisions": ["PDR-014"],
  "lastReviewed": "YYYY-MM-DD"
}
```

Do not create a registry for small projects without need.

---

# 15. Cross-layer examples

## Example A — UX and Design System

```text
UX:
Peer views inside one workspace use local peer navigation.

Design System:
LocalSegmentedNav is the reusable component for that interaction.

Feature:
Brain uses Overview / Inbox / Tone & Voice.
```

All three can be true without duplication of ownership.

## Example B — Domain and UI

```text
Domain:
Revision status = APPROVED.

Design System:
StatusChip visual role = positive.

Feature:
Display APPROVED using StatusChip.
```

Design System does not own the lifecycle value.

## Example C — Plan and Architecture

```text
Architecture:
Search will be owned by Search service in target architecture.

Migration Plan:
Current release still reads from legacy monolith until Phase 3.
```

This is transitional state, not necessarily contradiction.

---

# 16. AI-agent Source-of-Truth contract

Before making a significant change, an AI agent MUST:

```text
1. classify the fact scope;
2. read the project's SOURCE_OF_TRUTH map;
3. read the owning canonical source;
4. read relevant local specs;
5. check accepted decisions where material;
6. inspect implementation evidence;
7. report unresolved conflict instead of inventing resolution.
```

AI MUST NOT infer authority from:

```text
filename alone
file length
modification time alone
code convenience
visual reference
one comment
one old README
```

---

# 17. Source-of-Truth handoff to Agent Organization

The future AI Agent Operating Model should depend on this interface:

```text
resolve_scope(task)
→ resolve_canonical_owner(scope)
→ resolve_canonical_sources(owner, task)
→ assemble_context
→ execute within authority
```

Agents should not hard-code project-specific documentation paths.

Project-specific paths belong in:

```text
PROJECT_AGENT_MANIFEST
```

or equivalent project adapter.

---

# 18. Definition of Done

The Source-of-Truth model is correctly instantiated when:

```text
[ ] major scopes have canonical owners
[ ] critical canonical sources are discoverable
[ ] no known high-risk active conflicts remain hidden
[ ] local specs refine rather than silently override
[ ] accepted decisions are propagated
[ ] code-vs-doc drift is classified
[ ] archived material cannot masquerade as active truth
[ ] AI contributors have deterministic authority resolution
```

---

# 19. Golden rules

> **One fact should have one canonical owner.**

> **Authority is scoped, not global.**

> **Specificity may refine; it may not silently contradict.**

> **Evidence can challenge truth; evidence does not automatically become truth.**

> **A Decision Record explains why; the canonical contract states what is true now.**

> **Implementation is evidence of current behavior, not automatic authority over intent.**

> **When authority is ambiguous, stop guessing and make the ambiguity explicit.**

===== END VIRTUAL FILE: 00_governance/PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md =====

---

## VIRTUAL FILE 10/56 — `00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md`

**Virtual path:** `00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md`  
**Content checksum:** `5e1a7653f22c`

===== BEGIN VIRTUAL FILE: 00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md =====

# Project Knowledge Lifecycle Model v1.0

**ID:** DOC-GOV-KL-001  
**Type:** STANDARD / KNOWLEDGE GOVERNANCE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Changes to knowledge capture, evidence, validation, canonical promotion, learning, provenance, supersession, or AI memory policy  
**Supersedes:** —  
**Related:** DOC-STD-001, PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md, Decision Records, Reports/Evidence, project manifests

---

## 0. Purpose

This standard defines how **project knowledge itself** moves through the organization.

It answers:

- where a new observation starts;
- what counts as evidence;
- how hypotheses differ from facts;
- when a finding becomes a decision;
- when a decision changes canonical truth;
- how learnings become reusable rules, tests, skills, or policies;
- how stale knowledge is challenged;
- how superseded knowledge remains traceable;
- how AI agents may consume and produce knowledge safely.

This is intentionally different from:

```text
Document lifecycle
Feature lifecycle
Design-system object lifecycle
Domain lifecycle
```

Those lifecycles describe artifacts or product objects.

This model describes the **epistemic lifecycle of knowledge**.

---

# 1. Why a Knowledge Lifecycle is needed

A project continuously produces information from:

```text
users
research
analytics
tests
incidents
code review
production behavior
experiments
support
AI agents
engineering work
design work
architecture work
```

Without a knowledge lifecycle, all of these can accidentally become equal-looking Markdown statements.

That creates dangerous ambiguity:

```text
one interview quote
looks like
a product requirement

one AI suggestion
looks like
an architecture decision

one runtime behavior
looks like
approved doctrine

one old learning
looks like
current truth
```

The Knowledge Lifecycle prevents this.

---

# 2. Core distinction: information is not automatically knowledge

Use this conceptual ladder:

```text
SIGNAL
↓
OBSERVATION
↓
EVIDENCE
↓
INTERPRETATION / HYPOTHESIS
↓
PROPOSAL
↓
REVIEW / VALIDATION
↓
DECISION
↓
CANONICAL PROMOTION
↓
ACTIVE KNOWLEDGE
↓
MONITORING / CHALLENGE
↓
SUPERSESSION / RETIREMENT
↓
HISTORICAL MEMORY
```

Not every signal should reach the top.

---

# 3. Knowledge classes

## 3.1 Signal

Raw indication that something may matter.

Examples:

```text
user complaint
failed test
review comment
metric movement
production alert
AI observation
```

Signal is not truth.

## 3.2 Observation

A bounded statement about something observed.

Example:

```text
5 of 8 usability participants failed to find the Publish action.
```

Observation should include provenance.

## 3.3 Evidence

An artifact supporting or falsifying a claim.

Examples:

```text
test result
trace
screenshot
analytics query
interview notes
benchmark
incident timeline
production log
```

Evidence is scoped and may have limitations.

## 3.4 Hypothesis

An interpretation that may explain observations.

Example:

```text
The Publish action may be hard to discover because it is visually grouped with secondary actions.
```

A hypothesis is not canonical truth.

## 3.5 Proposal

A proposed change to product, architecture, design, policy, process, or documentation.

Typical artifact:

```text
RFC
PDR proposal
ADR proposal
DDR proposal
change plan
```

## 3.6 Decision

An accepted/rejected choice by the authorized owner.

Decision should record:

```text
context
choice
rationale
trade-offs
owner
date
```

## 3.7 Canonical knowledge

A rule/fact incorporated into the owning Source of Truth.

Examples:

```text
Domain invariant
Product principle
Architecture boundary
Feature contract
Security policy
Design-system contract
Engineering standard
```

## 3.8 Learning

A generalized conclusion supported enough to influence future work.

Examples:

```text
Repeated reviewer findings show async UI changes often omit negative states.
```

A learning may lead to:

```text
standard update
skill update
test gate
workflow change
product principle
```

but does not automatically do so.

## 3.9 Historical knowledge

Previously valid or considered knowledge preserved for traceability but not active instruction.

---

# 4. Knowledge lifecycle states

Recommended semantic lifecycle:

```text
CAPTURED
→ CLASSIFIED
→ EVIDENCED
→ PROPOSED
→ REVIEWED
→ VALIDATED
→ PROMOTED
→ ACTIVE
→ CHALLENGED
→ SUPERSEDED / RETIRED
→ ARCHIVED
```

Alternative terminal paths:

```text
CAPTURED
→ REJECTED

PROPOSED
→ REJECTED

CHALLENGED
→ REVALIDATED
→ ACTIVE
```

Do not force every small piece of information through every state.

The lifecycle is a governance model, not mandatory bureaucracy.

---

# 5. State definitions

## CAPTURED

A signal/observation has been recorded.

Required:

```text
source
date/time or period
scope
```

## CLASSIFIED

The information has been assigned a type and likely owner.

Example:

```text
Type: UX research observation
Owner: UX
```

## EVIDENCED

Supporting evidence exists and provenance is recorded.

This does not mean the interpretation is correct.

## PROPOSED

A concrete claim/change is proposed.

## REVIEWED

Authorized reviewers have evaluated:

```text
evidence
alternatives
scope
risks
conflicts
```

## VALIDATED

The claim is sufficiently supported for the intended scope.

Validation strength depends on risk.

## PROMOTED

Authorized owner has approved incorporation into canonical project knowledge.

## ACTIVE

Canonical owner has been updated and the knowledge is current.

## CHALLENGED

New evidence materially calls the active knowledge into question.

The existing rule remains active unless explicitly suspended/replaced.

## REVALIDATED

Challenge reviewed; existing knowledge remains valid.

## SUPERSEDED

A newer active knowledge item replaces it.

## RETIRED

Knowledge no longer applies and has no direct successor.

## ARCHIVED

Historical context only.

## REJECTED

Proposal/claim was considered but not accepted.

Rejection may remain useful decision memory.

---

# 6. Promotion is explicit

The most important rule:

> **Knowledge does not become canonical because it was written down.**

Promotion requires:

```text
owner
scope
evidence appropriate to risk
review
decision/approval
canonical update
provenance
```

Examples:

```text
Research note
≠ Product Principle

AI recommendation
≠ Architecture rule

Reviewer finding
≠ Engineering Standard

Incident observation
≠ permanent policy
```

A promotion action is what changes status.

---

# 7. Promotion routes

## 7.1 Research → Product / UX

```text
Research evidence
→ synthesis
→ hypothesis
→ Product/UX proposal
→ PDR/DDR if material
→ canonical Product/UX doc
```

## 7.2 Engineering discovery → Architecture/Engineering

```text
implementation observation
→ evidence
→ RFC/ADR or standard proposal
→ review
→ canonical architecture/engineering update
```

## 7.3 Incident → Operations / Engineering / Security

```text
incident
→ timeline/evidence
→ root-cause analysis
→ learning
→ corrective decision
→ runbook/test/policy/architecture update
```

## 7.4 Analytics → Product decision

```text
metric observation
→ validated query
→ interpretation
→ product hypothesis
→ experiment/decision
→ canonical product update if accepted
```

## 7.5 Code review → Engineering learning

```text
review finding
→ repeated pattern
→ learning
→ standard/skill/checklist proposal
→ validation
→ promotion
```

## 7.6 AI-agent output → Project knowledge

```text
AI observation/proposal
→ provenance
→ owner review according to risk
→ accepted decision
→ canonical promotion
```

AI output MUST NOT skip directly to canonical truth for protected/high-impact scopes.

---

# 8. Evidence requirements are risk-based

Do not demand the same evidence level for everything.

Example:

Low risk:

```text
Rename an internal documentation heading.
```

May require no formal evidence.

High risk:

```text
Change authorization policy.
```

Requires much stronger validation.

Use risk classes from the future Agent/Change Operating Model when available.

Until then, consider:

```text
reversibility
user impact
security impact
financial impact
data impact
architecture scope
regulatory impact
```

---

# 9. Provenance contract

Every significant knowledge item SHOULD answer:

```text
Where did this come from?
Who/what produced it?
When?
Under what baseline/version?
What evidence supports it?
Who approved promotion?
What canonical source now owns it?
What supersedes it?
```

Recommended fields:

```text
knowledge_id
type
scope
owner
created_at
source_refs
evidence_refs
decision_refs
canonical_refs
status
promoted_at
promoted_by
supersedes
superseded_by
review_due
limitations
```

---

# 10. Knowledge record

For important reusable learnings, a project MAY use:

```markdown
# Learning — <Title>

**ID:** K-XXX
**Status:** ACTIVE
**Scope:** Engineering
**Owner:** Engineering
**Captured:** YYYY-MM-DD
**Promoted:** YYYY-MM-DD
**Evidence:** ...
**Decision:** ...
**Canonical target:** ...

## Observation

## Evidence

## Interpretation

## Decision / Learning

## Where it was promoted

## Limitations

## Revisit trigger
```

Do not create knowledge records for every trivial fact.

---

# 11. Canonical promotion rule

When knowledge is promoted:

```text
1. update owning canonical document;
2. link decision/evidence where material;
3. mark source proposal/learning appropriately;
4. update superseded knowledge;
5. update indexes/manifests if used.
```

The canonical document remains the place contributors read for current truth.

They should not need to reconstruct current truth from 30 old research notes.

---

# 12. Canonical demotion does not exist silently

An active rule cannot simply disappear.

Use:

```text
SUPERSEDED
or
RETIRED
```

with rationale or decision reference when material.

This preserves institutional memory.

---

# 13. Challenge process

New evidence may challenge active knowledge.

Example:

```text
Active:
Mobile bottom sheet improves task completion.

New evidence:
Accessibility audit shows severe focus-management problems.
```

Process:

```text
ACTIVE
→ CHALLENGED
→ review evidence
→ REVALIDATED
or
→ replacement proposal
→ SUPERSEDED
```

Do not overwrite history.

---

# 14. Freshness vs validity

Freshness and validity are different.

An active piece of knowledge may be:

```text
CURRENT
REVIEW_DUE
STALE_REVIEW_REQUIRED
```

without automatically becoming false.

A recent observation may also be wrong.

Use freshness only as a review signal.

---

# 15. Confidence

Avoid fake numerical confidence unless the project has a defined calibrated method.

Prefer descriptive evidence state:

```text
UNVERIFIED
SUPPORTED
VALIDATED_FOR_SCOPE
CONTESTED
```

Do not display arbitrary:

```text
Confidence: 93%
```

for qualitative project knowledge.

---

# 16. Knowledge scope

Every promoted knowledge item should have a bounded scope.

Examples:

```text
project-wide
frontend only
billing domain
mobile application
Search feature
Design System
production operations
```

A learning validated in one scope does not automatically generalize to all projects.

---

# 17. Knowledge portability

Universal knowledge and project-specific knowledge are different.

## Project knowledge

Example:

```text
Artist OS uses numbered authoring sections.
```

Lives in project docs.

## Universal knowledge

Example:

```text
Author and final reviewer should be separated for high-risk changes.
```

May belong to U-POS universal policy after sufficient validation.

Promotion across project boundaries requires explicit review.

Do not automatically generalize one project's preference into a universal standard.

---

# 18. Knowledge and Decision Records

Decision Records and Knowledge Records serve different purposes.

```text
Decision Record
→ why a choice was made

Canonical Contract
→ what is true now

Knowledge/Learning Record
→ what was learned and from what evidence
```

They may cross-link.

One artifact should not be forced to own all three responsibilities.

---

# 19. Knowledge and Plans

Plans may contain assumptions.

An assumption in a Plan is not canonical truth.

Example:

```text
Plan assumption:
We expect API migration to finish in Q4.
```

Do not promote it to architecture truth.

After execution, observations can become evidence for future decisions.

---

# 20. Knowledge and Reports

Reports are point-in-time evidence.

Example:

```text
Performance Audit — 2026-09-19
```

It may support a decision.

It should not be treated as timeless active instruction.

---

# 21. Knowledge and code

Code produces implementation evidence.

Examples:

```text
current behavior
current API shape
current performance
current test assumptions
```

A code pattern repeated many times can be:

```text
intentional standard
legacy convention
accidental duplication
technical debt
```

Do not promote it without review.

---

# 22. Knowledge and tests

Tests are strong evidence of expected implemented behavior.

But test presence alone does not establish product authority.

If a test contradicts confirmed canonical contract:

```text
the test may be wrong.
```

Classify the drift.

---

# 23. Knowledge and AI memory

For AI-assisted projects:

> **Project memory should primarily be built from governed project knowledge, not raw model conversation history.**

Preferred agent context:

```text
canonical docs
accepted decisions
validated learnings
relevant evidence
current plan
```

Lower priority:

```text
raw brainstorming
unreviewed AI notes
old chat transcripts
rejected proposals
```

unless directly relevant.

---

# 24. AI knowledge contribution classes

AI may produce:

```text
AI_OBSERVATION
AI_HYPOTHESIS
AI_PROPOSAL
AI_REVIEW_FINDING
AI_LEARNING_CANDIDATE
```

These labels make epistemic state explicit.

AI SHOULD NOT label its own unreviewed output:

```text
CANONICAL
VALIDATED
```

unless the operating policy explicitly permits autonomous promotion for that low-risk scope.

---

# 25. Human approval boundaries

Until overridden by the future Agent Operating Model, human/authorized-owner approval is required to promote knowledge that changes:

```text
Product Vision
Product Principles
major Scope
Domain invariants/lifecycles
Architecture boundaries
Security/privacy
Authorization
Billing
Data retention/deletion
irreversible operations
major UX direction
universal U-POS policies
```

Low-risk documentation corrections MAY be autonomously promoted if project policy allows.

---

# 26. Repeated findings → organizational learning

A powerful learning loop:

```text
Agent/Reviewer finding
↓
same finding repeats
↓
pattern detected
↓
Learning Candidate
↓
root-cause review
↓
proposed change to:
  Skill
  Policy
  Standard
  Test
  Workflow
↓
promotion
↓
measure recurrence after change
```

This is how an AI-native engineering organization “learns” without fine-tuning the base model.

---

# 27. Learning effectiveness

After promoting a learning, measure whether it helped.

Examples:

```text
review finding frequency
rework rate
first-pass approval
escaped defects
human intervention
cycle time
```

Do not keep rules merely because they were once added.

A rule that adds cost without measurable value may itself be challenged.

---

# 28. Knowledge debt

Track high-value gaps:

```text
unknown owner
unvalidated critical assumption
accepted decision not propagated
stale high-risk policy
conflicting canonical claims
learning candidate not reviewed
```

Do not create tickets for every informal note.

---

# 29. Knowledge loss prevention

Before deleting or archiving a source:

```text
1. identify unique knowledge;
2. confirm canonical promotion where required;
3. preserve decision/evidence references;
4. preserve provenance;
5. then archive/delete according to documentation policy.
```

This aligns with Documentation Migration rules.

---

# 30. Knowledge traceability chain

For material changes, target:

```text
Signal / Problem
↓
Observation
↓
Evidence
↓
Proposal
↓
Decision
↓
Canonical Contract
↓
Implementation
↓
Test / Telemetry
↓
Learning
↓
Next Decision
```

Not every change needs every link.

High-risk changes should have stronger traceability.

---

# 31. Knowledge retrieval priority

When assembling context, prefer:

```text
1. Active canonical sources
2. Accepted decisions relevant to those sources
3. Validated active learnings
4. Current plan
5. Recent relevant evidence
6. Historical material
7. Raw/unreviewed notes
```

This order is a default, not a substitute for scope ownership.

---

# 32. Contradictory knowledge

If two knowledge items disagree:

```text
do not merge them into a compromise automatically.
```

Resolve through the Source-of-Truth Model:

```text
scope
owner
canonical source
decision
evidence
```

Keep dissenting/historical evidence where useful.

---

# 33. Knowledge lifecycle event model

Future observability may emit events such as:

```text
KNOWLEDGE_CAPTURED
KNOWLEDGE_CLASSIFIED
EVIDENCE_LINKED
PROPOSAL_CREATED
KNOWLEDGE_REVIEWED
KNOWLEDGE_VALIDATED
KNOWLEDGE_PROMOTED
KNOWLEDGE_CHALLENGED
KNOWLEDGE_REVALIDATED
KNOWLEDGE_SUPERSEDED
KNOWLEDGE_RETIRED
KNOWLEDGE_ARCHIVED
```

This allows future dashboards to show organizational learning.

---

# 34. Integration with Agent Organization

The future Agent Operating Model should use this model for:

```text
context assembly
memory
agent outputs
review findings
learning candidates
skill evolution
policy evolution
decision promotion
human approval
```

Suggested boundary:

```text
Agent Runtime
produces signals/evidence/proposals

Knowledge Lifecycle
governs promotion

Source-of-Truth Model
determines canonical owner

Documentation System
stores durable truth/history
```

---

# 35. Integration with Observability

A future Agent Observability layer should be able to answer:

```text
Which agent produced this observation?
Which evidence supported it?
Who validated it?
Where was it promoted?
Did it reduce future failures?
What knowledge was superseded?
```

This creates auditable organizational learning.

---

# 36. Definition of Done

The Knowledge Lifecycle is correctly instantiated when:

```text
[ ] evidence is distinguishable from canonical truth
[ ] proposals are distinguishable from accepted decisions
[ ] decisions propagate into canonical owners
[ ] important knowledge has provenance
[ ] AI outputs cannot silently become doctrine
[ ] active knowledge can be challenged/revalidated
[ ] superseded knowledge remains traceable
[ ] repeated failures can become learning candidates
[ ] promoted learnings can update standards/skills/tests/workflows
[ ] retrieval prioritizes governed current knowledge
```

---

# 37. Golden rules

> **Written does not mean canonical.**

> **Observed does not mean explained.**

> **Evidence supports a claim; evidence is not the claim.**

> **A decision creates authority only within the owner's scope.**

> **Promotion into canonical truth is explicit.**

> **New evidence can challenge old knowledge without erasing history.**

> **AI may generate knowledge candidates; governance decides what becomes institutional memory.**

> **The project should learn through governed memory before considering model fine-tuning.**

===== END VIRTUAL FILE: 00_governance/PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md =====

---

## VIRTUAL FILE 11/56 — `00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md`

**Virtual path:** `00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md`  
**Content checksum:** `fb4051c6bad4`

===== BEGIN VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md =====

# Project Documentation Profiles v1.0

**ID:** DOC-REF-002  
**Type:** REFERENCE  
**Status:** ACTIVE  
**Normativity:** INFORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** LIVING  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Project maturity/type profiles change  
**Supersedes:** —  
**Related:** DOC-STD-001, DOC-REF-001


# 1. Principle

Not every project needs every document.

Choose documentation by:

- risk;
- complexity;
- team size;
- regulatory burden;
- lifecycle;
- integration surface;
- operational criticality;
- AI usage;
- UI complexity.

---

# 2. Starter / MVP

Minimum useful set:

```text
README.md
docs/README.md
PRODUCT_VISION.md
SCOPE.md
MASTER_ARCHITECTURE.md
FEATURE_SPECS.md
UX_CONSTITUTION.md
ENGINEERING_PRINCIPLES.md
API_DATA.md
TESTING.md
ACTIVE_PLAN.md
DECISIONS/
LOCAL_SETUP.md
```

Add Design System when reusable UI begins to emerge.

---

# 3. Production product

Add:

```text
DOMAIN_MODEL.md
DESIGN_SYSTEM/
API_CONTRACTS.md
DATA_MODEL.md
SECURITY_MODEL.md
ANALYTICS_STRATEGY.md
DEPLOYMENT.md
ROLLBACK.md
INCIDENT_RESPONSE.md
RUNBOOKS/
ACCESSIBILITY_TESTING.md
OBSERVABILITY.md
DATA_MIGRATIONS.md
```

---

# 4. Complex / enterprise / regulated

Add:

```text
requirement IDs
formal traceability
compliance mapping
data lineage
retention
access reviews
change approvals
evidence retention
DR testing
vendor risk
formal threat modeling
formal RFC process
document manifest
CI documentation integrity
```

---

# 5. Mobile app profile

Emphasize:

- app lifecycle;
- navigation/deep links;
- offline/cache;
- OS permissions;
- device/OS support;
- app-store release;
- background tasks;
- local storage;
- accessibility on target devices.

---

# 6. SaaS profile

Emphasize:

- tenancy;
- auth/authz;
- billing;
- roles;
- audit;
- export/delete;
- environment strategy;
- migrations;
- observability.

---

# 7. API / platform profile

Emphasize:

- API contracts;
- versioning;
- rate limits;
- idempotency;
- events;
- SDKs;
- deprecation;
- examples;
- compatibility guarantees.

---

# 8. AI product profile

Emphasize:

- AI system overview;
- provider/model boundaries;
- context assembly;
- human approval;
- provenance;
- evals;
- safety;
- degraded mode;
- prompt contracts;
- AI telemetry;
- privacy/data minimization.

---

# 9. Internal tool profile

Emphasize:

- permissions;
- operational impact;
- audit;
- data correctness;
- destructive actions;
- runbooks;
- admin override rules.

---

# 10. High-UI-complexity product profile

Add early:

```text
UX_CONSTITUTION
INFORMATION_ARCHITECTURE
NAVIGATION_MODEL
CONTENT_DESIGN
DESIGN_SYSTEM_OPERATING_MODEL
DESIGN_HANDOFF_STANDARD
REGISTRY.json
UI KIT WEB
VISUAL_REGRESSION
```

---

# 11. Low-UI API/backend profile

Design System MAY be minimal or absent.

Do not create UI governance merely to fill a folder.

===== END VIRTUAL FILE: 00_governance/PROJECT_DOCUMENTATION_PROFILES_v1.0.md =====

---

## VIRTUAL FILE 12/56 — `00_governance/templates/DOCS_README_TEMPLATE.md`

**Virtual path:** `00_governance/templates/DOCS_README_TEMPLATE.md`  
**Content checksum:** `d1b52e82e03f`

===== BEGIN VIRTUAL FILE: 00_governance/templates/DOCS_README_TEMPLATE.md =====

# Project Documentation

## Start here

1. Product Vision
2. Scope
3. Master Architecture
4. Current Active Plan
5. Local Setup

## Source of truth

See `00_governance/SOURCE_OF_TRUTH.md`.

## Product
...

## Domain
...

## Architecture
...

## Product Specifications
...

## UX
...

## Design System
...

## Engineering
...

## Data / API
...

## AI
...

## Security / Privacy
...

## Quality / Testing
...

## Analytics
...

## Operations
...

## Decisions
...

## Current Plans
...

## Reference
...

## Archive
...

===== END VIRTUAL FILE: 00_governance/templates/DOCS_README_TEMPLATE.md =====

---

## VIRTUAL FILE 13/56 — `00_governance/templates/SOURCE_OF_TRUTH_TEMPLATE.md`

**Virtual path:** `00_governance/templates/SOURCE_OF_TRUTH_TEMPLATE.md`  
**Content checksum:** `020a0e6d675b`

===== BEGIN VIRTUAL FILE: 00_governance/templates/SOURCE_OF_TRUTH_TEMPLATE.md =====

# Source of Truth

**Type:** STANDARD / REFERENCE  
**Status:** ACTIVE  
**Owner:** Project Governance  

## Principle

No document is globally authoritative for every decision.

Authority is scoped.

## Product / Business
Owner: `01_product/`

## Domain semantics
Owner: `02_domain/`

## Architecture
Owner: `03_architecture/`

## Feature behavior
Owner: `04_product_specs/`

## UX / IA / content
Owner: `05_ux/`

## Reusable visual / interaction system
Owner: `06_design_system/`

## Engineering implementation rules
Owner: `07_engineering/`

## API / data / integrations
Owner: `08_data_api/`

## AI
Owner: `09_ai/`

## Security / privacy
Owner: `10_security_privacy/`

## Quality / test evidence
Owner: `11_quality_testing/`

## Analytics
Owner: `12_analytics/`

## Operations
Owner: `13_operations/`

## Decision rationale
Owner: `14_decisions/`

## Current sequencing
Owner: `15_plans/`

## Conflict rule

A lower-level/local document may refine but MUST NOT silently contradict the canonical owner in its scope.

===== END VIRTUAL FILE: 00_governance/templates/SOURCE_OF_TRUTH_TEMPLATE.md =====

---

## VIRTUAL FILE 14/56 — `01_product/templates/PRODUCT_VISION_TEMPLATE.md`

**Virtual path:** `01_product/templates/PRODUCT_VISION_TEMPLATE.md`  
**Content checksum:** `776f5d1524bb`

===== BEGIN VIRTUAL FILE: 01_product/templates/PRODUCT_VISION_TEMPLATE.md =====

# Product Vision — <Product>

**Type:** CONSTITUTION / MASTER  
**Status:** DRAFT  
**Normativity:** NORMATIVE  
**Owner:** Product  
**Lifetime:** STABLE

## Problem

## Target user

## Primary value proposition

## Desired future state

## Strategic differentiation

## Product boundaries

## Long-term product question

## Non-goals

## Evidence / assumptions

===== END VIRTUAL FILE: 01_product/templates/PRODUCT_VISION_TEMPLATE.md =====

---

## VIRTUAL FILE 15/56 — `01_product/templates/SCOPE_TEMPLATE.md`

**Virtual path:** `01_product/templates/SCOPE_TEMPLATE.md`  
**Content checksum:** `cfca6b59c750`

===== BEGIN VIRTUAL FILE: 01_product/templates/SCOPE_TEMPLATE.md =====

# Scope — <Product / Release>

**Type:** CONTRACT  
**Status:** DRAFT  
**Owner:** Product  
**Lifetime:** LIVING

## In scope

## Out of scope

## Deferred

## Non-goals

## Dependencies

## Review trigger

===== END VIRTUAL FILE: 01_product/templates/SCOPE_TEMPLATE.md =====

---

## VIRTUAL FILE 16/56 — `02_domain/templates/DOMAIN_MODEL_TEMPLATE.md`

**Virtual path:** `02_domain/templates/DOMAIN_MODEL_TEMPLATE.md`  
**Content checksum:** `ecba0b7a9881`

===== BEGIN VIRTUAL FILE: 02_domain/templates/DOMAIN_MODEL_TEMPLATE.md =====

# Domain Model

**Type:** MASTER  
**Status:** DRAFT  
**Owner:** Domain / Architecture  
**Lifetime:** STABLE

## Bounded contexts

## Major entities

## Relationships

## Ownership

## Invariants

## Lifecycles

## Cross-domain references

## Terminology

## Diagrams

## Related decisions

===== END VIRTUAL FILE: 02_domain/templates/DOMAIN_MODEL_TEMPLATE.md =====

---

## VIRTUAL FILE 17/56 — `02_domain/templates/LIFECYCLE_TEMPLATE.md`

**Virtual path:** `02_domain/templates/LIFECYCLE_TEMPLATE.md`  
**Content checksum:** `454a9fce19d2`

===== BEGIN VIRTUAL FILE: 02_domain/templates/LIFECYCLE_TEMPLATE.md =====

# Lifecycle — <Entity>

**Type:** CONTRACT  
**Status:** DRAFT  
**Owner:** Domain  
**Lifetime:** LIVING

## States

## Allowed transitions

## Who can transition

## Preconditions

## Side effects

## Terminal states

## Reversal policy

## Audit requirements

## Tests

===== END VIRTUAL FILE: 02_domain/templates/LIFECYCLE_TEMPLATE.md =====

---

## VIRTUAL FILE 18/56 — `03_architecture/templates/ADR_TEMPLATE.md`

**Virtual path:** `03_architecture/templates/ADR_TEMPLATE.md`  
**Content checksum:** `659d2e1848fd`

===== BEGIN VIRTUAL FILE: 03_architecture/templates/ADR_TEMPLATE.md =====

# ADR-XXX — <Title>

**Type:** DECISION_RECORD  
**Status:** ACCEPTED  
**Owner:** Architecture  
**Lifetime:** HISTORICAL

## Context

## Decision

## Why

## Alternatives considered

## Consequences

### Positive

### Negative

## Risks

## Migration

## Validation

## Supersedes / superseded by

===== END VIRTUAL FILE: 03_architecture/templates/ADR_TEMPLATE.md =====

---

## VIRTUAL FILE 19/56 — `03_architecture/templates/MASTER_ARCHITECTURE_TEMPLATE.md`

**Virtual path:** `03_architecture/templates/MASTER_ARCHITECTURE_TEMPLATE.md`  
**Content checksum:** `83be487bbc9d`

===== BEGIN VIRTUAL FILE: 03_architecture/templates/MASTER_ARCHITECTURE_TEMPLATE.md =====

# Master Architecture

**Type:** MASTER  
**Status:** DRAFT  
**Owner:** Architecture  
**Lifetime:** STABLE

## Architecture goals

## System boundaries

## Major modules / services

## Ownership

## Key flows

## Persistence strategy

## Async model

## External integrations

## Trust boundaries

## Failure philosophy

## Non-functional constraints

## Related ADRs

## Out of scope

===== END VIRTUAL FILE: 03_architecture/templates/MASTER_ARCHITECTURE_TEMPLATE.md =====

---

## VIRTUAL FILE 20/56 — `04_product_specs/templates/FEATURE_SPEC_TEMPLATE.md`

**Virtual path:** `04_product_specs/templates/FEATURE_SPEC_TEMPLATE.md`  
**Content checksum:** `cae0b222e6c6`

===== BEGIN VIRTUAL FILE: 04_product_specs/templates/FEATURE_SPEC_TEMPLATE.md =====

# Feature — <Name>

**ID:** SPEC-XXX  
**Type:** SPECIFICATION  
**Document status:** DRAFT  
**Feature status:** SPEC_DRAFT  
**Owner:** Product  
**Lifetime:** LIVING

## 1. Problem

## 2. User job

## 3. Goals

## 4. Non-goals

## 5. Scope

## 6. Terminology

## 7. Domain concepts

## 8. User scenarios

## 9. Functional behavior

## 10. State / lifecycle

## 11. Permissions

## 12. Validation

## 13. Error behavior

## 14. Loading / empty / unavailable

## 15. Data requirements

## 16. API / events

## 17. UX requirements

## 18. Accessibility

## 19. Security / privacy

## 20. Analytics

## 21. Performance / NFR

## 22. Edge cases

## 23. Migration / backward compatibility

## 24. Acceptance criteria

## 25. Test matrix

## 26. Open questions

| Question | Owner | Blocking | Deadline | Status |
|---|---|---:|---|---|

## 27. Related decisions

===== END VIRTUAL FILE: 04_product_specs/templates/FEATURE_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 21/56 — `04_product_specs/templates/FLOW_SPEC_TEMPLATE.md`

**Virtual path:** `04_product_specs/templates/FLOW_SPEC_TEMPLATE.md`  
**Content checksum:** `fe84d01896dd`

===== BEGIN VIRTUAL FILE: 04_product_specs/templates/FLOW_SPEC_TEMPLATE.md =====

# Flow — <Name>

**Type:** SPECIFICATION  
**Document status:** DRAFT  
**Owner:** Product + UX  
**Lifetime:** LIVING

## Purpose

## User job

## Entry conditions

## Flow map

```text
State / Screen A
→ State / Screen B
→ State / Screen C
```

## Decision points

## Transition rules

## Domain transitions

## Persistence boundaries

## Back behavior

## Cancel behavior

## Retry behavior

## Error recovery

## Irreversible actions

## Approval / commit boundaries

## Responsive / platform differences

## Accessibility

## Localization

## Analytics boundaries

## Exit conditions

## Acceptance criteria

## Open questions

===== END VIRTUAL FILE: 04_product_specs/templates/FLOW_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 22/56 — `04_product_specs/templates/SCREEN_EXPERIENCE_SPEC_TEMPLATE.md`

**Virtual path:** `04_product_specs/templates/SCREEN_EXPERIENCE_SPEC_TEMPLATE.md`  
**Content checksum:** `62a56153b783`

===== BEGIN VIRTUAL FILE: 04_product_specs/templates/SCREEN_EXPERIENCE_SPEC_TEMPLATE.md =====

# Screen Experience — <Name>

**Type:** SPECIFICATION  
**Document status:** DRAFT  
**Owner:** Product + UX  
**Lifetime:** LIVING  
**Related feature:** <...>  
**Page Grammar:** <DS registry ID>

## 1. Primary user job

## 2. Primary question

## 3. Primary action

## 4. Information hierarchy

## 5. Canonical data read

## 6. Canonical data written

## 7. Domain transitions

## 8. Components used

## 9. Patterns used

## 10. Layout / composition

## 11. Navigation behavior

## 12. Responsive / environment behavior

## 13. States

## 14. Loading / empty / error / unavailable

## 15. Localization

## 16. Accessibility

## 17. Content rules

## 18. Analytics

## 19. Security / privacy considerations

## 20. Do / Don't

## 21. Out of scope

## 22. Acceptance criteria

## 23. Implementation evidence

===== END VIRTUAL FILE: 04_product_specs/templates/SCREEN_EXPERIENCE_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 23/56 — `05_ux/templates/CONTENT_DESIGN_TEMPLATE.md`

**Virtual path:** `05_ux/templates/CONTENT_DESIGN_TEMPLATE.md`  
**Content checksum:** `320eaa0cdb2f`

===== BEGIN VIRTUAL FILE: 05_ux/templates/CONTENT_DESIGN_TEMPLATE.md =====

# Content Design — <Product>

**Type:** STANDARD  
**Status:** DRAFT  
**Owner:** Product / Content Design  
**Lifetime:** STABLE

## Product voice

## Tone by context

| Context | Tone |
|---|---|
| Success | |
| Error | |
| Warning | |
| Empty | |
| Destructive | |
| Education | |

## Canonical terminology

| Concept | Use | Avoid |
|---|---|---|

## CTA grammar

## Capitalization

## Punctuation

## Status language

## Error-message pattern

## Empty-state pattern

## Confirmation language

## Destructive-action language

## Dates / time / numbers / currency / units

## Localization rules

## Accessibility language

## AI-generated content labels if applicable

## Do / Don't

===== END VIRTUAL FILE: 05_ux/templates/CONTENT_DESIGN_TEMPLATE.md =====

---

## VIRTUAL FILE 24/56 — `05_ux/templates/IA_NAVIGATION_TEMPLATE.md`

**Virtual path:** `05_ux/templates/IA_NAVIGATION_TEMPLATE.md`  
**Content checksum:** `37240d949b5c`

===== BEGIN VIRTUAL FILE: 05_ux/templates/IA_NAVIGATION_TEMPLATE.md =====

# Information Architecture & Navigation Model

**Type:** MASTER / STANDARD  
**Status:** DRAFT  
**Owner:** Product Design  
**Lifetime:** STABLE

## Top-level information architecture

## Route/workspace boundaries

## Global navigation

## Local navigation

## Tabs

## Segmented controls

## Wizards / steppers

## Breadcrumbs

## Back behavior

## Deep links

## Command palette

## Mobile transformation

## Accessibility

## Naming / terminology

## Rationale

===== END VIRTUAL FILE: 05_ux/templates/IA_NAVIGATION_TEMPLATE.md =====

---

## VIRTUAL FILE 25/56 — `05_ux/templates/UX_CONSTITUTION_TEMPLATE.md`

**Virtual path:** `05_ux/templates/UX_CONSTITUTION_TEMPLATE.md`  
**Content checksum:** `759ebe3c2cea`

===== BEGIN VIRTUAL FILE: 05_ux/templates/UX_CONSTITUTION_TEMPLATE.md =====

# UX Constitution — <Product>

**ID:** UX-CONST-001  
**Type:** CONSTITUTION  
**Status:** DRAFT  
**Normativity:** NORMATIVE  
**Owner:** Product Design / Product  
**Lifetime:** STABLE

## 0. Purpose

Defines durable experience laws, not current redesign tasks.

## 1. Product feeling

## 2. Core UX laws

## 3. Information hierarchy

## 4. Global IA principles

## 5. Navigation semantics

### Global navigation
### Local peer navigation
### Sequential/wizard navigation
### Authoring navigation
### Breadcrumb/back/deep-link behavior

## 6. Forms policy

## 7. Progressive disclosure

## 8. Human-control / commitment principles

## 9. Data honesty / unknown-state philosophy

## 10. AI UX principles if relevant

## 11. Provenance / explainability

## 12. Error and recovery philosophy

## 13. Empty-state philosophy

## 14. Responsive philosophy

## 15. Accessibility UX baseline

## 16. Research/reference policy

## 17. UX anti-patterns

## 18. Global acceptance criteria

## 19. Related docs

- IA
- Navigation Model
- Content Design
- Design System

===== END VIRTUAL FILE: 05_ux/templates/UX_CONSTITUTION_TEMPLATE.md =====

---

## VIRTUAL FILE 26/56 — `06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md`

**Virtual path:** `06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md`  
**Content checksum:** `b9ad84650153`

===== BEGIN VIRTUAL FILE: 06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md =====

# Design Handoff Standard v1.3

**ID:** DS-STD-002  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System / Product Design  
**Version:** 1.3.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Artifact taxonomy, handoff contract, accessibility/responsive/i18n requirements change  
**Supersedes:** —  
**Related:** DS-STD-001, DS-STD-003


# 0. Scope

Defines how a Design System object is specified well enough to implement without guessing.

Canonical object types:

```text
Foundation
Primitive
Component
Pattern
Page Grammar
```

Screen/Flow experience specs live outside the Design System module and reference these objects.

---

# 1. Core rule

Important reusable object:

```text
VISUAL CONTRACT
+
BEHAVIORAL CONTRACT
+
IMPLEMENTATION TRUTH (when implemented)
```

Visual and behavioral contracts describe the same contract version.

---

# 2. Handoff levels

## Quick Concept

Exploration only.

## Spec Board

Approved visual contract.

## Behavioral Spec

Implementation contract.

---

# 3. Spec Board goals

Board should reveal:

- purpose;
- usage context;
- hierarchy;
- key states;
- key variants;
- environment differences;
- anatomy;
- related-object boundary;
- Do / Don't.

The UI specimen remains dominant.

---

# 4. Board metadata

Show where relevant:

```text
Registry ID
Name
Contract version
Object lifecycle status
Purpose
Design principle
States
Variants
Modes/environments
Anatomy
Typography
Tokens
Spacing
Dimensions
Icons
Interactions
A11y
Related boundary
Do / Don't
```

Document metadata belongs to the Markdown file header.

---

# 5. State / Variant / Mode / Environment

## State

Temporary runtime condition.

## Variant

Stable structural/semantic form.

## Mode

System-level design mode.

## Environment

Execution context:

- viewport;
- input;
- locale direction;
- platform/browser;
- zoom;
- reduced motion.

Do not overload one axis.

---

# 6. Content priority

```text
P0 — required in default state
P1 — useful support
P2 — details on demand
P3 — internal/debug/advanced
```

---

# 7. Summary / Details

> Summary = what the user needs now.

> Details = what the user may need next.

Default state SHOULD NOT contain unnecessary information for the current decision.

---

# 8. Anatomy

Every important component/pattern defines anatomy.

Example:

```text
Component
├── PrimaryContent
├── SupportingContent
├── Status
├── PrimaryAction
└── Details
```

---

# 9. Child-object contract

For meaningful child:

```text
Name
Role
Priority
Visual style/token
States
Behavior
Must-not behavior
Accessibility
Environment differences
```

---

# 10. Data requirements

Behavioral spec defines:

- required fields;
- optional fields;
- missing behavior;
- loading behavior;
- error behavior;
- stale behavior if relevant;
- data owner;
- illustrative fixture status.

Do not invent data to satisfy visual composition.

---

# 11. Rendering rules

Define:

- conditionals;
- ordering;
- wrapping;
- truncation;
- overflow;
- optional blocks;
- min/max sizes;
- list behavior;
- scroll ownership;
- sticky behavior.

---

# 12. Interaction contract

Use cause → effect.

Also define:

```text
MUST NOT HAPPEN
```

Explicit negative rules prevent accidental coupling.

---

# 13. Responsive / environment contract

Never write only `responsive`.

Specify transformations.

For supported environments define:

- layout;
- visibility;
- navigation/disclosure changes;
- touch behavior;
- keyboard behavior;
- zoom;
- RTL;
- theme/mode;
- reduced motion.

---

# 14. Localization / i18n

Where applicable define:

- text expansion;
- long words;
- wrapping/truncation;
- RTL;
- mixed scripts;
- font coverage;
- pluralization;
- number/date/currency;
- pseudo-localization.

---

# 15. Typography

Define role + semantic token.

```text
Role
Font/token
Size/token
Weight
Line-height
Tracking
Color
Wrap behavior
```

---

# 16. Token contract

Implementation SHOULD reference semantic tokens.

Raw values MAY appear on boards only as explanation.

---

# 17. Spacing / dimensions

Specify relationships rather than arbitrary pixel dumps.

For important interactive controls show annotated size diagram.

---

# 18. Iconography

Define:

- icon source;
- name;
- visible size;
- hit target;
- semantic role;
- accessible name/decorative status.

---

# 19. Motion

Define:

```text
What
Trigger
Duration/token
Easing/token
Reduced-motion fallback
```

---

# 20. Accessibility

Baseline follows project accessibility standard.

Where relevant:

- semantics;
- name;
- keyboard;
- focus order;
- focus-visible;
- Escape;
- trap/restore;
- error association;
- async announcements;
- touch target;
- contrast;
- non-color semantics;
- reduced motion.

---

# 21. Loading / Empty / Error / Unavailable / Unknown

Do not collapse these states.

Define exact semantics.

---

# 22. Stress fixtures

Relevant examples:

```text
short
long
very long word
no optional metadata
0/1/many items
slow loading
failed asset
failed request
localized expansion
RTL
narrow viewport
200% zoom
keyboard-only
reduced motion
```

---

# 23. Related-object boundary

Document:

```text
Related
Alternative
Do not confuse with
```

Explain differences by user job, hierarchy, interaction model.

---

# 24. Do / Don't

Specific, not aesthetic fluff.

Bad:

```text
Keep it clean.
```

Good:

```text
DO keep summary compact.
DON'T duplicate the same primary action.
```

---

# 25. Out of scope

Every behavioral spec states what this work does not include.

---

# 26. Open questions

Important specs MAY include:

| Question | Owner | Blocking | Deadline | Status |
|---|---|---:|---|---|

Resolved questions should be removed/replaced by contract or decision links.

---

# 27. Canonical object-spec structure

```markdown
# <Name> <Contract Version>

Document metadata...

**Registry ID:** ...
**Object lifecycle:** ...
**Platforms:** ...
**Modes:** ...
**Board:** ...
**Source:** ...
**Story:** ...

## Purpose
## User job
## When to use
## When not to use
## Related / do-not-confuse
## Data requirements
## Content priority
## Anatomy
## Default state
## States
## Variants
## Modes / environments
## Rendering rules
## Interactions
## Responsive behavior
## Localization / i18n
## Typography
## Tokens
## Spacing / dimensions
## Icons
## Motion
## Accessibility
## Loading / empty / error / unavailable
## Stress fixtures
## Edge cases
## Do
## Don't
## Out of scope
## Implementation notes
## Acceptance criteria
## QA matrix
## Open questions
## Visual references
## Implementation screenshots/evidence links
```

---

# 28. Acceptance criteria

Must be testable.

Avoid:

```text
Looks premium.
```

Prefer:

```text
Play does not toggle disclosure.
No horizontal overflow at 375px.
Escape closes overlay.
Focus returns to trigger.
```

---

# 29. QA matrix

Use relevant dimensions:

```text
Visual
Interaction
Data
Responsive/environment
Accessibility
Localization
Loading/error
Long content
Domain semantics
```

Actual QA reports live under Quality.

---

# 30. Quality bar

A contributor should be able to answer:

```text
What is this?
Why does it exist?
When do I use it?
What is primary?
What states exist?
What variants exist?
What environments matter?
What data is required?
How does it fail?
How is it accessible?
What must not happen?
What similar object is different?
```

===== END VIRTUAL FILE: 06_design_system/DESIGN_HANDOFF_STANDARD_v1.3.md =====

---

## VIRTUAL FILE 27/56 — `06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md`

**Virtual path:** `06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md`  
**Content checksum:** `19154b1e9bd3`

===== BEGIN VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md =====

# Design System Documentation Integration v1.0

**ID:** DS-STD-004  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System + Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Ownership boundary between Design System and adjacent project documentation changes  
**Supersedes:** —  
**Related:** DOC-STD-001, DS-STD-001, DS-STD-002, DS-STD-003


# Purpose

Resolve the question:

> Where does a UI-related fact belong?

---

# Ownership map

| Fact | Canonical owner |
|---|---|
| Product goal | `01_product/` |
| Domain lifecycle | `02_domain/` |
| Service/data ownership | `03_architecture/` |
| Feature behavior | `04_product_specs/` |
| Screen job / whole-screen experience | `04_product_specs/` + `05_ux/` |
| User flow | `04_product_specs/` / `05_ux/` |
| Navigation semantics | `05_ux/` |
| Product language / CTA grammar | `05_ux/CONTENT_DESIGN.md` |
| Reusable visual token | `06_design_system/` |
| Primitive/component | `06_design_system/` |
| Reusable interaction pattern | `06_design_system/` |
| Page Grammar | `06_design_system/` |
| Visual board for DS object | `06_design_system/boards/` |
| Why a pattern was chosen | `14_decisions/design/` |
| Visual QA result | `11_quality_testing/` |
| Visual regression policy | `11_quality_testing/` |
| Current redesign/migration sequence | `15_plans/` |
| PR workflow/checklist | `16_onboarding/` |

---

# Examples

## Phrase discovery

```text
Feature behavior
→ 04_product_specs/phrase-discovery/

Navigation / educational flow
→ 05_ux/

PhraseCard reusable contract
→ 06_design_system/components/phrase-card/

Why mobile details use Bottom Sheet
→ 14_decisions/design/DDR-...

Visual QA after implementation
→ 11_quality_testing/reports/
```

## Dashboard

```text
Metric definition
→ 12_analytics/

Dashboard feature behavior
→ 04_product_specs/

Dashboard IA
→ 05_ux/

MetricCard
→ 06_design_system/

Current dashboard redesign sequence
→ 15_plans/
```

---

# Rule

> **A Design System object may reference upstream Product/UX contracts, but it must not silently absorb their ownership.**

===== END VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_DOCUMENTATION_INTEGRATION_v1.0.md =====

---

## VIRTUAL FILE 28/56 — `06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md`

**Virtual path:** `06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md`  
**Content checksum:** `73d08ce53220`

===== BEGIN VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md =====

# Design System Operating Model v1.1

**ID:** DS-STD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System  
**Version:** 1.1.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Design-system governance, lifecycle, token, registry, or contribution model changes  
**Supersedes:** —  
**Related:** DS-STD-002, DS-STD-003, DS-STD-004


# 0. Scope boundary

This standard governs reusable visual and interaction language.

It does NOT own:

```text
Product/business truth
Domain lifecycles
Full feature behavior
Global UX Constitution
Content Design
Whole user flows
Visual QA reports
Current migration plans
Decision history
```

Those belong to other project documentation layers.

---

# 1. Canonical design-system hierarchy

```text
FOUNDATION
↓
PRIMITIVE
↓
COMPONENT
↓
PATTERN
↓
PAGE GRAMMAR
```

Screens consume the system but are owned by Product/UX specs.

Flows are Product/UX cross-cutting artifacts, not Design System objects.

A Screen MAY be designated a Design System benchmark, but its canonical screen contract remains outside the Design System module.

---

# 2. Three synchronized truths

For important reusable objects:

```text
VISUAL TRUTH
→ approved board

BEHAVIORAL TRUTH
→ object spec

IMPLEMENTATION TRUTH
→ code + stories/tests
```

For `IMPLEMENTED`:

```text
visualVersion
=
specVersion
=
codeVersion
```

Material drift must be explicit.

---

# 3. Roles

## Product

Owns product value and major UX trade-offs.

## Design System Owner

Owns:

- taxonomy;
- registry;
- lifecycle;
- reusable visual/interaction coherence;
- token governance;
- deprecation.

## Product Design

Owns:

- visual/interaction design intent;
- boards;
- hierarchy;
- states/variants;
- responsive intent.

## UI Engineering

Owns:

- accessible implementation;
- public API;
- performance;
- tests;
- token consumption.

## Domain / Architecture

Owns domain semantics.

## AI agent

Contributor only; must search registry and preserve semantics.

---

# 4. Design-system object lifecycle

```text
EXPERIMENTAL
→ CANDIDATE
→ REVIEW
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ DEPRECATED
→ REMOVED
```

This is not the document lifecycle.

Every object spec therefore SHOULD expose both:

```text
Document status
Object lifecycle status
```

---

# 5. Change classes

## Class 0 — local cosmetic correction

No contract change.

## Class 1 — existing object revision

Update spec/board/tests as needed.

## Class 2 — new reusable object

Requires registry search + spec + accessibility + implementation.

## Class 3 — new Pattern / Page Grammar

Requires Design RFC and benchmark/reference usage.

## Class 4 — project-wide experience/IA direction change

Escalates to UX Constitution / Product governance.

Design System MUST NOT approve a Class-4 product decision alone.

---

# 6. Reuse decision tree

```text
Need UI
│
├─ Same user job?
│   └─ reuse candidate
│
├─ Same hierarchy + interaction?
│   └─ variant/state extension
│
├─ Existing Pattern?
│   └─ reuse
│
├─ Existing Page Grammar?
│   └─ compose with it
│
├─ Feature-local one-off?
│   └─ keep local
│
└─ Recurring reusable job?
    └─ propose new system object
```

---

# 7. Token architecture

Use:

```text
Primitive token
↓
Semantic token
↓
Component token (only when justified)
```

Feature UI SHOULD primarily consume semantic tokens.

Recommended families:

```text
color.*
surface.*
text.*
border.*
action.*
status.*
spacing.*
radius.*
size.*
type.*
shadow.*
motion.*
breakpoint.*
z.*
focus.*
density.*
```

---

# 8. Registry

Canonical metadata:

```text
REGISTRY.json
```

Registry SHOULD drive:

- UI Kit inventory;
- search;
- status;
- version;
- relationships;
- deprecation;
- parity;
- ownership;
- review/freshness;
- traceability links.

Metadata is authored once.

---

# 9. Traceability

Registry MAY link design-system objects to:

```text
requirements
feature specs
UX docs
architecture refs
decision records
tests
telemetry
evidence
screens
```

This is optional for simple objects but valuable in complex systems.

---

# 10. Review metadata

Objects SHOULD support:

```text
lastReviewed
reviewTrigger
freshness
```

Freshness is not lifecycle status.

---

# 11. Versioning

## Major

Breaking object contract.

## Minor

Backward-compatible addition.

## Patch

Non-contract polish/fix.

Registry stores semantic contract version.

---

# 12. Design debt vs permanent exception

## Design debt

Temporary known deviation.

## Approved exception

Intentional permanent scoped exception.

Do not confuse them.

Repeated exceptions may indicate a missing rule/pattern.

---

# 13. Deprecation

```text
Mark DEPRECATED
→ replacement
→ migration notes
→ prevent new use
→ migrate
→ remove
→ preserve historical metadata
```

---

# 14. Required gates

Reusable object reaches `IMPLEMENTED` only when relevant:

```text
[ ] registry entry exists
[ ] visual contract exists
[ ] behavioral contract exists
[ ] code exists
[ ] version parity reconciled
[ ] token use compliant
[ ] states implemented
[ ] environment behavior verified
[ ] accessibility verified
[ ] localization stress verified where applicable
[ ] story/live example exists
[ ] tests pass
[ ] visual QA evidence exists where required
```

Visual QA evidence is stored in Quality, not as canonical DS truth.

---

# 15. Contribution flow

```text
NEED
↓
USER JOB
↓
SEARCH REGISTRY
↓
REUSE / EXTEND / CREATE?
↓
CONCEPT
↓
VISUAL CONTRACT
↓
BEHAVIORAL CONTRACT
↓
IMPLEMENTATION
↓
TESTS
↓
VISUAL QA
↓
ACCESSIBILITY QA
↓
PROMOTION
↓
REGISTRY / UI KIT / CHANGELOG
```

---

# 16. Design RFC

Class 3 changes use:

```text
14_decisions/design/rfcs/
```

After acceptance, a durable Design Decision Record MAY be created.

The Design System module links the decision; it does not own the decision-history folder.

---

# 17. Governance cadence

Per meaningful UI PR:

- reuse;
- token compliance;
- semantics;
- parity;
- accessibility;
- environment behavior.

Milestone audit:

- duplicates;
- hardcoded values;
- deprecated usage;
- debt;
- missing specs/boards/stories;
- registry drift;
- benchmark regressions.

---

# 18. Health measures

Use concrete signals:

```text
objects with board/spec/story
accessibility coverage
visual-regression coverage
deprecated usages
open design debt
duplicate families
hardcoded-token violations
registry/code mismatches
```

No fake aggregate design-system score.

---

# 19. Anti-patterns

Avoid:

- generic Card for every grouping;
- visual-reference architecture;
- code-only design truth;
- Figma-only truth;
- global domain status invented by UI;
- speculative component library detached from product use;
- silently divergent implementation;
- Design System owning UX/content/feature truth.

---

# 20. Final principle

> **The Design System is a governed reusable subsystem of the project documentation architecture, not the project documentation architecture itself.**

===== END VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_OPERATING_MODEL_v1.1.md =====

---

## VIRTUAL FILE 29/56 — `06_design_system/DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md`

**Virtual path:** `06_design_system/DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md`  
**Content checksum:** `d7850f6a6a1c`

===== BEGIN VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md =====

# Design System Profile — <Product>

**ID:** DS-PROFILE-001  
**Type:** CONSTITUTION / REFERENCE  
**Status:** DRAFT  
**Normativity:** NORMATIVE  
**Owner:** Design System  
**Lifetime:** STABLE

## Purpose

Defines project-specific visual DNA only.

UX laws/navigation/content language live in `05_ux/`.

## Canvas

## Surface language

## Primary accent

## Semantic accents

## Typography

```text
Display
UI
Body
Mono
Script/language-specific
```

## Spacing density

## Radius system

## Border system

## Elevation

## Iconography

## Motion character

## Focus language

## Supported modes

```text
Light
Dark
High contrast
Compact density
Comfortable density
```

Only include modes actually supported.

## Media / image style

## Illustration style

## Data visualization style

## Token source

## Visual anti-patterns

===== END VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_PROFILE_TEMPLATE_v1.0.md =====

---

## VIRTUAL FILE 30/56 — `06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json`

**Virtual path:** `06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json`  
**Content checksum:** `b1ea04ea360a`

===== BEGIN VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json =====

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/design-system-registry.schema.v1.1.json",
  "title": "Design System Registry v1.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "designSystem",
    "items"
  ],
  "properties": {
    "schemaVersion": {
      "const": "1.1.0"
    },
    "designSystem": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "version",
        "objectLifecycleBaseline"
      ],
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "objectLifecycleBaseline": {
          "const": "v1"
        },
        "profilePath": {
          "type": [
            "string",
            "null"
          ]
        },
        "uiKitPath": {
          "type": [
            "string",
            "null"
          ]
        },
        "tokenSourcePath": {
          "type": [
            "string",
            "null"
          ]
        },
        "changelogPath": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "items": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/item"
      }
    }
  },
  "$defs": {
    "type": {
      "enum": [
        "foundation",
        "primitive",
        "component",
        "pattern",
        "page-grammar"
      ]
    },
    "objectStatus": {
      "enum": [
        "EXPERIMENTAL",
        "CANDIDATE",
        "REVIEW",
        "APPROVED",
        "IMPLEMENTING",
        "IMPLEMENTED",
        "DEPRECATED",
        "REMOVED"
      ]
    },
    "freshness": {
      "enum": [
        "CURRENT",
        "REVIEW_DUE",
        "STALE_REVIEW_REQUIRED",
        "NOT_APPLICABLE"
      ]
    },
    "parity": {
      "enum": [
        "UNKNOWN",
        "IN_SYNC",
        "OUT_OF_SYNC",
        "NOT_APPLICABLE"
      ]
    },
    "item": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "slug",
        "type",
        "contractVersion",
        "objectStatus",
        "purpose",
        "paths",
        "truths"
      ],
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^[A-Z0-9][A-Z0-9_-]*$"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string",
          "pattern": "^[a-z0-9][a-z0-9-]*$"
        },
        "type": {
          "$ref": "#/$defs/type"
        },
        "contractVersion": {
          "type": "string"
        },
        "objectStatus": {
          "$ref": "#/$defs/objectStatus"
        },
        "owner": {
          "type": [
            "string",
            "null"
          ]
        },
        "purpose": {
          "type": "string"
        },
        "userJob": {
          "type": [
            "string",
            "null"
          ]
        },
        "designPrinciple": {
          "type": [
            "string",
            "null"
          ]
        },
        "platforms": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "modes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "aliases": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "review": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "lastReviewed": {
              "type": [
                "string",
                "null"
              ],
              "format": "date"
            },
            "reviewTrigger": {
              "type": [
                "string",
                "null"
              ]
            },
            "freshness": {
              "$ref": "#/$defs/freshness"
            }
          }
        },
        "paths": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "spec": {
              "type": [
                "string",
                "null"
              ]
            },
            "board": {
              "type": [
                "string",
                "null"
              ]
            },
            "source": {
              "type": [
                "string",
                "null"
              ]
            },
            "story": {
              "type": [
                "string",
                "null"
              ]
            },
            "tests": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "implementedScreenshots": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            }
          }
        },
        "relations": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "uses": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "usedBy": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "related": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "doNotConfuseWith": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "replacement": {
              "type": [
                "string",
                "null"
              ]
            }
          }
        },
        "truths": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "visualVersion",
            "specVersion",
            "codeVersion",
            "parity"
          ],
          "properties": {
            "visualVersion": {
              "type": [
                "string",
                "null"
              ]
            },
            "specVersion": {
              "type": [
                "string",
                "null"
              ]
            },
            "codeVersion": {
              "type": [
                "string",
                "null"
              ]
            },
            "parity": {
              "$ref": "#/$defs/parity"
            }
          }
        },
        "traceability": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "requirements": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "featureSpecs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "uxRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "architectureRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "decisionRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "testRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "telemetryRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            },
            "evidenceRefs": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "uniqueItems": true
            }
          }
        },
        "deprecation": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": false,
          "properties": {
            "reason": {
              "type": "string"
            },
            "replacement": {
              "type": [
                "string",
                "null"
              ]
            },
            "deprecatedAt": {
              "type": [
                "string",
                "null"
              ],
              "format": "date"
            },
            "targetRemoval": {
              "type": [
                "string",
                "null"
              ]
            },
            "migration": {
              "type": [
                "string",
                "null"
              ]
            }
          }
        }
      }
    }
  }
}

===== END VIRTUAL FILE: 06_design_system/DESIGN_SYSTEM_REGISTRY_SCHEMA_v1.1.json =====

---

## VIRTUAL FILE 31/56 — `06_design_system/README_TEMPLATE.md`

**Virtual path:** `06_design_system/README_TEMPLATE.md`  
**Content checksum:** `6f866e82bb9d`

===== BEGIN VIRTUAL FILE: 06_design_system/README_TEMPLATE.md =====

# <Project> Design System

## Purpose

This directory contains the governed reusable visual and interaction system.

## Read first

1. `DESIGN_SYSTEM_OPERATING_MODEL.md`
2. `DESIGN_HANDOFF_STANDARD.md`
3. `REGISTRY.json`
4. `DESIGN_SYSTEM_PROFILE.md`
5. UI Kit Web

## Authority

- Product/domain truth lives outside this module.
- UX navigation/content truth lives in `05_ux/`.
- Reusable UI contracts live here.
- Current migration plans live in `15_plans/`.
- Visual QA reports live in `11_quality_testing/`.
- Design decisions live in `14_decisions/`.

## Before creating UI

1. Search Registry.
2. Search feature-local implementation.
3. Check Patterns.
4. Check Page Grammars.
5. Reuse if user job + hierarchy + interaction match.
6. Extend only with an explicit variant/state contract.
7. Create a new reusable object only when justified.

## Object lifecycle

```text
EXPERIMENTAL
→ CANDIDATE
→ REVIEW
→ APPROVED
→ IMPLEMENTING
→ IMPLEMENTED
→ DEPRECATED
→ REMOVED
```

## Canonical metadata

`REGISTRY.json`

## UI Kit

`<url / command>`

## Tokens

`<path>`

## Changelog

`CHANGELOG.md`

===== END VIRTUAL FILE: 06_design_system/README_TEMPLATE.md =====

---

## VIRTUAL FILE 32/56 — `06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md`

**Virtual path:** `06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md`  
**Content checksum:** `a3f785e7f0e3`

===== BEGIN VIRTUAL FILE: 06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md =====

# UI Kit Web Specification v1.2

**ID:** DS-STD-003  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System / UI Engineering  
**Version:** 1.2.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** UI Kit information architecture, registry rendering, preview, export, or static-build contract changes  
**Supersedes:** —  
**Related:** DS-STD-001, DS-STD-002, DS-STD-004


# 0. Responsibility

Defines how design-system knowledge becomes a living, navigable web interface.

It does NOT redefine:

- object lifecycle;
- token semantics;
- UX Constitution;
- feature behavior;
- quality-report ownership.

---

# 1. Registry-driven requirement

UI Kit SHOULD consume canonical `REGISTRY.json`.

Registry drives:

- inventory;
- navigation;
- search;
- status;
- version;
- relationships;
- deprecation;
- traceability links;
- freshness;
- parity.

Metadata is authored once.

---

# 2. Information architecture

```text
Overview / Atlas
Foundations
Primitives
Components
Patterns
Page Grammars
Deprecated
Resources
```

Screens/Flows MAY appear as **reference consumers** through links to Product/UX specs, but their canonical contracts are not owned by the Design System module.

Optional:

```text
Benchmark Screens
```

as a visual-reference section.

---

# 3. Atlas

Atlas displays:

```text
Name
Contract version
Object lifecycle
Freshness/parity signal if useful
Mini real specimen
Short purpose
```

It is visual navigation.

---

# 4. Search

Search should index:

- name;
- aliases;
- ID;
- purpose;
- tags;
- tokens;
- status;
- related objects.

---

# 5. Filters

Recommended:

```text
Type
Lifecycle status
Platform
Mode
Tag
Implemented only
Deprecated
```

---

# 6. Object detail page

Recommended:

```text
Header
Visual Spec
Live Preview
States
Variants
Modes / Environments
Responsive
Anatomy
Content Priority
Tokens
Interactions
Accessibility
Localization
Do / Don't
Development
Changelog
Related Objects
Used In
Traceability
```

Hide irrelevant sections.

---

# 7. Header

Show:

```text
Name
Registry ID
Contract version
Object lifecycle
Owner
Type
Platforms
Purpose
Design principle
Parity
Last reviewed / freshness
```

Document lifecycle need not be visually prominent unless viewing the raw spec.

---

# 8. Design / Development

Recommended:

```text
[ Design ] [ Development ]
```

Design:

- board;
- states;
- anatomy;
- responsive;
- tokens.

Development:

- import;
- public API;
- events;
- source;
- story;
- tests;
- implementation notes.

---

# 9. Live preview controls

Only approved contract concepts:

```text
State
Variant
Mode
Viewport
Locale
Direction
Fixture
```

Do not expose every internal prop.

---

# 10. Environment toolbar

Typical:

```text
375
430
768
1024
1440
Custom
LTR / RTL
Light / Dark
Reduced motion
Density mode
```

Only if product actually supports them.

---

# 11. Tokens

Display values from real token source.

Do not manually duplicate resolved values where generation is possible.

---

# 12. Accessibility

Show:

- keyboard;
- focus;
- semantics;
- contrast;
- target size;
- overlay behavior;
- reduced motion.

Automated check result may supplement, not replace, contract.

---

# 13. Localization

For multilingual products:

- locale switch;
- pseudo-locale;
- RTL preview;
- long-text fixture.

---

# 14. Related / traceability

Display registry relations:

```text
Uses
Used by
Related
Do not confuse with
Replacement
Feature specs
Decision refs
Tests
Telemetry/evidence
```

---

# 15. Reference implementation

Preferred:

```text
React
TypeScript
Storybook
MDX
real design tokens
real components
static build
```

Not mandatory.

Alternative tools are acceptable if contract is met.

---

# 16. Stories / fixtures

Use deterministic, safe fixtures.

Use same fixtures where possible for:

- stories;
- docs;
- screenshots;
- component tests.

No production secrets/private user data.

---

# 17. Static export

Required for a mature UI Kit:

```text
ui-kit-static/
├── index.html
└── assets/
```

Recommended command:

```text
pnpm ui-kit:build
```

---

# 18. Package export

Recommended:

```text
pnpm ui-kit:package
```

Output:

```text
<project>-ui-kit-<ds-version>.zip
```

---

# 19. Hosting

May be:

- `/ui-kit`;
- internal hostname;
- GitHub Pages;
- Vercel/Netlify;
- S3/CDN;
- local static server.

---

# 20. Security / privacy

Never expose:

- secrets;
- real tokens;
- private user records;
- confidential media;
- unreleased sensitive material.

---

# 21. UI Kit accessibility

UI Kit itself SHOULD meet WCAG 2.2 AA.

Boards require textual equivalents for critical rules.

---

# 22. CI

Recommended:

```text
typecheck
lint
component tests
UI Kit build
a11y checks
visual regression
static export
```

Broken UI Kit build is a documentation-system regression.

---

# 23. First milestone

Minimum useful UI Kit:

```text
Atlas
Search
Design System Profile
Foundations
Buttons/Inputs/Chips
3–5 core Components
2–3 core Patterns
Page Grammar examples
Static build
```

---

# 24. Acceptance

```text
[ ] registry drives inventory
[ ] Atlas exists
[ ] navigation semantic
[ ] search works
[ ] version/lifecycle shown from registry
[ ] important objects link board + spec + implementation
[ ] preview uses actual code where possible
[ ] supported environments inspectable
[ ] deprecated objects separated
[ ] static build works
[ ] no sensitive production data
[ ] documentation accessible
[ ] no local lifecycle/token redefinitions
```

---

# 25. Final rule

> **HTML is the experience. Registry + specs are the durable structured source. Boards preserve visual intent. Code preserves implementation truth.**

===== END VIRTUAL FILE: 06_design_system/UI_KIT_WEB_SPECIFICATION_v1.2.md =====

---

## VIRTUAL FILE 33/56 — `06_design_system/templates/COMPONENT_SPEC_TEMPLATE.md`

**Virtual path:** `06_design_system/templates/COMPONENT_SPEC_TEMPLATE.md`  
**Content checksum:** `8c0719900209`

===== BEGIN VIRTUAL FILE: 06_design_system/templates/COMPONENT_SPEC_TEMPLATE.md =====

# <Component Name> <Contract Version>

**ID:** DS-C-XXX  
**Type:** SPECIFICATION  
**Document status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Design System  
**Lifetime:** LIVING  

**Registry ID:** <ID>  
**Object lifecycle:** CANDIDATE / REVIEW / APPROVED / IMPLEMENTING / IMPLEMENTED  
**Platforms:** <...>  
**Modes:** <...>  
**Visual board:** <path>  
**Source:** <path>  
**Story:** <path>

## Purpose
## User job
## When to use
## When not to use
## Related / do-not-confuse
## Data requirements
## Content priority
## Anatomy
## Default state
## States
## Variants
## Modes / environments
## Rendering rules
## Interactions
### Must happen
### Must not happen
## Responsive behavior
## Localization / i18n
## Typography
## Tokens
## Spacing / dimensions
## Icons
## Motion
## Accessibility
## Loading / empty / error / unavailable
## Stress fixtures
## Edge cases
## Do
## Don't
## Out of scope
## Implementation notes
## Acceptance criteria
## QA matrix
## Open questions
| Question | Owner | Blocking | Deadline | Status |
|---|---|---:|---|---|
## Visual references
## Evidence / implementation screenshots

===== END VIRTUAL FILE: 06_design_system/templates/COMPONENT_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 34/56 — `06_design_system/templates/PAGE_GRAMMAR_SPEC_TEMPLATE.md`

**Virtual path:** `06_design_system/templates/PAGE_GRAMMAR_SPEC_TEMPLATE.md`  
**Content checksum:** `f25e033ab225`

===== BEGIN VIRTUAL FILE: 06_design_system/templates/PAGE_GRAMMAR_SPEC_TEMPLATE.md =====

# Page Grammar — <Name> <Version>

**ID:** DS-PG-XXX  
**Type:** SPECIFICATION  
**Document status:** ACTIVE  
**Object lifecycle:** CANDIDATE  
**Owner:** Design System + Product Design  
**Lifetime:** LIVING

## User mode

`Browse / Decide / Review / Create / Monitor / Deep Work / Other`

## Primary question

## Required hierarchy

## Optional regions

## Navigation type

## Primary-action policy

## Form policy

## Context/support policy

## Surface/card policy

## Data-density policy

## Mobile / narrow transformation

## Accessibility

## Localization / content expansion

## Reference feature/screen specs

## Benchmark reference

## Anti-patterns

## Acceptance criteria

===== END VIRTUAL FILE: 06_design_system/templates/PAGE_GRAMMAR_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 35/56 — `06_design_system/templates/PATTERN_SPEC_TEMPLATE.md`

**Virtual path:** `06_design_system/templates/PATTERN_SPEC_TEMPLATE.md`  
**Content checksum:** `be0d27db5dee`

===== BEGIN VIRTUAL FILE: 06_design_system/templates/PATTERN_SPEC_TEMPLATE.md =====

# Pattern — <Name> <Contract Version>

**ID:** DS-PAT-XXX  
**Type:** SPECIFICATION  
**Document status:** ACTIVE  
**Object lifecycle:** CANDIDATE  
**Owner:** Design System  
**Lifetime:** LIVING

## Purpose
## Recurring user problem
## User job
## When to use
## When not to use
## Participating primitives/components
## Composition / sequence
## State model
## Domain assumptions
## Content priority
## Responsive / environment behavior
## Localization
## Accessibility
## Failure / retry behavior
## Reference feature/screen specs
## Related patterns
## Anti-patterns
## Out of scope
## Acceptance criteria
## Open questions

===== END VIRTUAL FILE: 06_design_system/templates/PATTERN_SPEC_TEMPLATE.md =====

---

## VIRTUAL FILE 36/56 — `07_engineering/templates/CODEBASE_GUIDE_TEMPLATE.md`

**Virtual path:** `07_engineering/templates/CODEBASE_GUIDE_TEMPLATE.md`  
**Content checksum:** `45cd358e5c8e`

===== BEGIN VIRTUAL FILE: 07_engineering/templates/CODEBASE_GUIDE_TEMPLATE.md =====

# Codebase Guide

**Type:** GUIDE  
**Status:** ACTIVE  
**Owner:** Engineering  
**Lifetime:** LIVING

## Major directories

## Ownership

## Dependency direction

## Entry points

## Where new code goes

## Where code must not go

## Common commands

## Related architecture docs

===== END VIRTUAL FILE: 07_engineering/templates/CODEBASE_GUIDE_TEMPLATE.md =====

---

## VIRTUAL FILE 37/56 — `07_engineering/templates/ENGINEERING_PRINCIPLES_TEMPLATE.md`

**Virtual path:** `07_engineering/templates/ENGINEERING_PRINCIPLES_TEMPLATE.md`  
**Content checksum:** `b06d73699136`

===== BEGIN VIRTUAL FILE: 07_engineering/templates/ENGINEERING_PRINCIPLES_TEMPLATE.md =====

# Engineering Principles — <Project>

**Type:** CONSTITUTION / STANDARD  
**Status:** DRAFT  
**Owner:** Engineering  
**Lifetime:** STABLE

## Principles

Examples:
- boring technology by default;
- explicit state;
- typed failures;
- idempotent side effects;
- observability by default;
- no business logic in UI.

For each principle:

## <Principle>
Why:
Implication:
Counterexample:

===== END VIRTUAL FILE: 07_engineering/templates/ENGINEERING_PRINCIPLES_TEMPLATE.md =====

---

## VIRTUAL FILE 38/56 — `08_data_api/templates/API_CONTRACT_TEMPLATE.md`

**Virtual path:** `08_data_api/templates/API_CONTRACT_TEMPLATE.md`  
**Content checksum:** `d0e3c27ca76f`

===== BEGIN VIRTUAL FILE: 08_data_api/templates/API_CONTRACT_TEMPLATE.md =====

# API Contract — <Capability>

**Type:** CONTRACT  
**Status:** DRAFT  
**Owner:** API / Backend  
**Lifetime:** LIVING

## Endpoint / operation

## Purpose

## Authentication

## Authorization

## Request

## Response

## Error codes

## Idempotency

## Pagination

## Rate limits

## Versioning

## Examples

## Backward compatibility

## Tests

===== END VIRTUAL FILE: 08_data_api/templates/API_CONTRACT_TEMPLATE.md =====

---

## VIRTUAL FILE 39/56 — `08_data_api/templates/EVENT_CONTRACT_TEMPLATE.md`

**Virtual path:** `08_data_api/templates/EVENT_CONTRACT_TEMPLATE.md`  
**Content checksum:** `4782f41d84de`

===== BEGIN VIRTUAL FILE: 08_data_api/templates/EVENT_CONTRACT_TEMPLATE.md =====

# Event Contract — <Event>

**Type:** CONTRACT  
**Status:** DRAFT  
**Owner:** Data / Backend  
**Lifetime:** LIVING

## Event name
## Producer
## Consumers
## Schema
## Version
## Ordering
## Delivery semantics
## Idempotency
## PII classification
## Retention
## Replay behavior
## Compatibility
## Tests

===== END VIRTUAL FILE: 08_data_api/templates/EVENT_CONTRACT_TEMPLATE.md =====

---

## VIRTUAL FILE 40/56 — `09_ai/templates/AI_SYSTEM_OVERVIEW_TEMPLATE.md`

**Virtual path:** `09_ai/templates/AI_SYSTEM_OVERVIEW_TEMPLATE.md`  
**Content checksum:** `3e19e1c7bfec`

===== BEGIN VIRTUAL FILE: 09_ai/templates/AI_SYSTEM_OVERVIEW_TEMPLATE.md =====

# AI System Overview

**Type:** MASTER  
**Status:** DRAFT  
**Owner:** AI / Architecture  
**Lifetime:** STABLE

## AI responsibilities

## AI non-responsibilities

## Providers / model classes

## Context sources

## Human-control points

## Data flows

## Provenance

## Failure / degraded mode

## Privacy boundaries

## Evaluation strategy

## Related prompt contracts

===== END VIRTUAL FILE: 09_ai/templates/AI_SYSTEM_OVERVIEW_TEMPLATE.md =====

---

## VIRTUAL FILE 41/56 — `10_security_privacy/templates/SECURITY_MODEL_TEMPLATE.md`

**Virtual path:** `10_security_privacy/templates/SECURITY_MODEL_TEMPLATE.md`  
**Content checksum:** `f7d9d9c504ea`

===== BEGIN VIRTUAL FILE: 10_security_privacy/templates/SECURITY_MODEL_TEMPLATE.md =====

# Security Model

**Type:** MASTER  
**Status:** DRAFT  
**Owner:** Security / Architecture  
**Lifetime:** STABLE

## Assets

## Principals

## Trust boundaries

## Sensitive data

## High-risk actions

## Security assumptions

## Authentication

## Authorization

## Audit

## Incident assumptions

## Related threat model

===== END VIRTUAL FILE: 10_security_privacy/templates/SECURITY_MODEL_TEMPLATE.md =====

---

## VIRTUAL FILE 42/56 — `11_quality_testing/templates/TESTING_STANDARD_TEMPLATE.md`

**Virtual path:** `11_quality_testing/templates/TESTING_STANDARD_TEMPLATE.md`  
**Content checksum:** `48041f35fefc`

===== BEGIN VIRTUAL FILE: 11_quality_testing/templates/TESTING_STANDARD_TEMPLATE.md =====

# Testing Standard — <Project>

**Type:** STANDARD  
**Status:** DRAFT  
**Owner:** QA / Engineering  
**Lifetime:** STABLE

## Test naming

## Ownership

## Fixtures

## Isolation

## Mocking

## Flakiness policy

## Unit

## Component

## Integration

## Contract

## E2E

## Accessibility

## Visual regression

## Performance

## AI evals if applicable

## Required CI gates

===== END VIRTUAL FILE: 11_quality_testing/templates/TESTING_STANDARD_TEMPLATE.md =====

---

## VIRTUAL FILE 43/56 — `11_quality_testing/templates/VISUAL_QA_REPORT_TEMPLATE.md`

**Virtual path:** `11_quality_testing/templates/VISUAL_QA_REPORT_TEMPLATE.md`  
**Content checksum:** `d91b8f74581c`

===== BEGIN VIRTUAL FILE: 11_quality_testing/templates/VISUAL_QA_REPORT_TEMPLATE.md =====

# Visual QA Report — <Object / Screen>

**ID:** QA-VIS-XXX  
**Type:** REPORT  
**Status:** ACTIVE / ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** QA / Design  
**Lifetime:** HISTORICAL  
**Date:** <...>  
**Baseline:** <commit/release>  
**Environment:** <...>

## Result

PASS / NEEDS_FIX / PASS_WITH_DEBT

## Visual parity

### Hierarchy
### Typography
### Spacing
### Tokens / color
### Borders / radius / elevation
### Density
### Icons

## Interaction parity

### States
### Navigation / disclosure
### Focus / keyboard

## Environment

### Mobile / narrow
### Desktop
### Zoom
### Localization / long content

## Accessibility

## Loading / empty / error

## Data honesty / domain semantics

## Deviations

## Design debt created

## Exceptions referenced

## Evidence

===== END VIRTUAL FILE: 11_quality_testing/templates/VISUAL_QA_REPORT_TEMPLATE.md =====

---

## VIRTUAL FILE 44/56 — `12_analytics/templates/METRIC_CATALOG_TEMPLATE.md`

**Virtual path:** `12_analytics/templates/METRIC_CATALOG_TEMPLATE.md`  
**Content checksum:** `c5bc08ff5bf6`

===== BEGIN VIRTUAL FILE: 12_analytics/templates/METRIC_CATALOG_TEMPLATE.md =====

# Metric Catalog

**Type:** REFERENCE / CONTRACT  
**Status:** ACTIVE  
**Owner:** Data / Product  
**Lifetime:** LIVING

## <Metric>

**Definition:**  
**Formula:**  
**Population:**  
**Window:**  
**Source:**  
**Exclusions:**  
**Owner:**  
**Known limitations:**

===== END VIRTUAL FILE: 12_analytics/templates/METRIC_CATALOG_TEMPLATE.md =====

---

## VIRTUAL FILE 45/56 — `13_operations/templates/RUNBOOK_TEMPLATE.md`

**Virtual path:** `13_operations/templates/RUNBOOK_TEMPLATE.md`  
**Content checksum:** `f6b42b88200f`

===== BEGIN VIRTUAL FILE: 13_operations/templates/RUNBOOK_TEMPLATE.md =====

# Runbook — <Incident / Operation>

**ID:** RUN-XXX  
**Type:** RUNBOOK  
**Status:** ACTIVE  
**Owner:** SRE / Operations  
**Lifetime:** LIVING  
**Last tested:** <date>  
**Required access:** <...>

## Trigger

## Safety checks

## Diagnosis

## Procedure

1.
2.
3.

## Verification

## Rollback

## Escalation

## Evidence to preserve

## Post-operation cleanup

===== END VIRTUAL FILE: 13_operations/templates/RUNBOOK_TEMPLATE.md =====

---

## VIRTUAL FILE 46/56 — `14_decisions/templates/DDR_TEMPLATE.md`

**Virtual path:** `14_decisions/templates/DDR_TEMPLATE.md`  
**Content checksum:** `4360abcfe396`

===== BEGIN VIRTUAL FILE: 14_decisions/templates/DDR_TEMPLATE.md =====

# DDR-XXX — <Title>

**Type:** DECISION_RECORD  
**Status:** ACCEPTED  
**Owner:** Product Design / Design System  
**Lifetime:** HISTORICAL

## Context

## UX problem

## Decision

## Why this pattern

## Alternatives rejected

## Consequences

### Positive
### Negative

## Accessibility implications

## Responsive implications

## Design-system impact

## Migration

## Validation

## Supersedes / superseded by

## Related specs / registry IDs

===== END VIRTUAL FILE: 14_decisions/templates/DDR_TEMPLATE.md =====

---

## VIRTUAL FILE 47/56 — `14_decisions/templates/DESIGN_RFC_TEMPLATE.md`

**Virtual path:** `14_decisions/templates/DESIGN_RFC_TEMPLATE.md`  
**Content checksum:** `92303493a1b8`

===== BEGIN VIRTUAL FILE: 14_decisions/templates/DESIGN_RFC_TEMPLATE.md =====

# RFC-DS-XXX — <Title>

**Type:** RFC  
**Status:** DRAFT  
**Owner:** Design System / Product Design  
**Lifetime:** TEMPORARY  
**Change class:** 3 / 4

## Problem

## User job

## Evidence

## Existing system reviewed

## Proposal

## Alternatives

## Why extension is insufficient

## Product/domain impact

## UX impact

## Design-system impact

## Token impact

## Accessibility impact

## Responsive/platform impact

## Localization/content impact

## Migration impact

## Risks

## Prototype / board

## Decision

APPROVE / REVISE / REJECT

## Decision rationale

## Follow-up DDR

===== END VIRTUAL FILE: 14_decisions/templates/DESIGN_RFC_TEMPLATE.md =====

---

## VIRTUAL FILE 48/56 — `14_decisions/templates/PDR_TEMPLATE.md`

**Virtual path:** `14_decisions/templates/PDR_TEMPLATE.md`  
**Content checksum:** `22c84ad0cdec`

===== BEGIN VIRTUAL FILE: 14_decisions/templates/PDR_TEMPLATE.md =====

# PDR-XXX — <Title>

**Type:** DECISION_RECORD  
**Status:** ACCEPTED  
**Owner:** Product  
**Lifetime:** HISTORICAL

## Problem

## Decision

## User impact

## Alternatives

## Evidence

## Trade-offs

## Revisit when

## Related specs

===== END VIRTUAL FILE: 14_decisions/templates/PDR_TEMPLATE.md =====

---

## VIRTUAL FILE 49/56 — `15_plans/templates/CURRENT_UI_CHANGE_PLAN_TEMPLATE.md`

**Virtual path:** `15_plans/templates/CURRENT_UI_CHANGE_PLAN_TEMPLATE.md`  
**Content checksum:** `9fbbeeaae858`

===== BEGIN VIRTUAL FILE: 15_plans/templates/CURRENT_UI_CHANGE_PLAN_TEMPLATE.md =====

# Current UI Change Plan — <Initiative>

**ID:** PLAN-UI-XXX  
**Type:** PLAN  
**Status:** ACTIVE  
**Owner:** Product / Design / Engineering  
**Lifetime:** TEMPORARY  
**Baseline:** <commit/release/date>  
**Target:** <...>  
**Started:** <...>  
**Completion condition:** <...>  
**Archive location:** <...>

## Objective

## Current state

## Target state

## Constraints

## Scope

## Out of scope

## Workstreams

## Priorities

### P0
### P1
### P2
### P3

## Dependencies

## Risks

## Migration strategy

## Verification

## Rollback / forward-fix

## PR sequence

## Open design debt

## Completion / archive action

===== END VIRTUAL FILE: 15_plans/templates/CURRENT_UI_CHANGE_PLAN_TEMPLATE.md =====

---

## VIRTUAL FILE 50/56 — `15_plans/templates/MIGRATION_PLAN_TEMPLATE.md`

**Virtual path:** `15_plans/templates/MIGRATION_PLAN_TEMPLATE.md`  
**Content checksum:** `0126c4b56b12`

===== BEGIN VIRTUAL FILE: 15_plans/templates/MIGRATION_PLAN_TEMPLATE.md =====

# Migration — <Name>

**Type:** PLAN  
**Status:** ACTIVE  
**Owner:** <...>  
**Lifetime:** TEMPORARY

## Baseline

## Target

## Why

## Preconditions

## Compatibility strategy

## Step sequence

## Data migration

## Rollout

## Verification

## Rollback / forward-fix

## Risks

## Observability

## Completion criteria

## Archive action

===== END VIRTUAL FILE: 15_plans/templates/MIGRATION_PLAN_TEMPLATE.md =====

---

## VIRTUAL FILE 51/56 — `16_onboarding/templates/AI_AGENT_GUIDE_TEMPLATE.md`

**Virtual path:** `16_onboarding/templates/AI_AGENT_GUIDE_TEMPLATE.md`  
**Content checksum:** `c4140207b919`

===== BEGIN VIRTUAL FILE: 16_onboarding/templates/AI_AGENT_GUIDE_TEMPLATE.md =====

# AI Agent Guide

## Read first

1. root README
2. docs/README
3. SOURCE_OF_TRUTH
4. relevant product spec
5. relevant domain/architecture docs
6. relevant UX/design docs
7. engineering/data/security standards
8. current plan

## Before editing

- search implementation;
- search docs;
- identify canonical owner;
- identify lifecycle/permissions;
- identify tests.

## Never invent

- domain entities;
- APIs;
- statuses;
- permissions;
- routes;
- metrics;
- design-system objects;
- feature flags.

## If docs conflict

- apply source-of-truth precedence;
- report unresolved contradiction;
- preserve higher-authority semantics.

## Before completing

- run required tests;
- update canonical docs if behavior changed;
- add decision record when significant;
- do not put temporary implementation state into stable doctrine.

===== END VIRTUAL FILE: 16_onboarding/templates/AI_AGENT_GUIDE_TEMPLATE.md =====

---

## VIRTUAL FILE 52/56 — `16_onboarding/templates/UI_PR_CHECKLIST_TEMPLATE.md`

**Virtual path:** `16_onboarding/templates/UI_PR_CHECKLIST_TEMPLATE.md`  
**Content checksum:** `59430473debc`

===== BEGIN VIRTUAL FILE: 16_onboarding/templates/UI_PR_CHECKLIST_TEMPLATE.md =====

# UI PR Checklist

## Change

## User job

## Product impact

## Domain impact

## UX impact

## Design-system impact

- Change class:
- Page Grammar:
- Patterns reused:
- Components reused:
- New DS object:
- Registry impact:
- Board/spec impact:

## API / data impact

## Security / privacy impact

## QA

- responsive/environment:
- localization/long content:
- keyboard/focus:
- accessibility:
- visual regression:
- implementation screenshots:

## Documentation

- [ ] No docs needed
- [ ] Product spec updated
- [ ] UX updated
- [ ] Design System updated
- [ ] Decision record added
- [ ] QA evidence linked
- [ ] Current plan updated

## Governance

Design debt:
Permanent exception:
Deprecated object introduced: NO

===== END VIRTUAL FILE: 16_onboarding/templates/UI_PR_CHECKLIST_TEMPLATE.md =====

---

## VIRTUAL FILE 53/56 — `17_reference/templates/GLOSSARY_TEMPLATE.md`

**Virtual path:** `17_reference/templates/GLOSSARY_TEMPLATE.md`  
**Content checksum:** `3772ab18495b`

===== BEGIN VIRTUAL FILE: 17_reference/templates/GLOSSARY_TEMPLATE.md =====

# Glossary

**Type:** REFERENCE  
**Status:** ACTIVE  
**Owner:** Project Governance  
**Lifetime:** LIVING

## <Term>

**Canonical meaning:**  
**Not the same as:**  
**Owner:**  
**Related terms:**  
**Domain / layer:**

===== END VIRTUAL FILE: 17_reference/templates/GLOSSARY_TEMPLATE.md =====

---

## VIRTUAL FILE 54/56 — `99_archive/README.md`

**Virtual path:** `99_archive/README.md`  
**Content checksum:** `85444c95077e`

===== BEGIN VIRTUAL FILE: 99_archive/README.md =====

# Archive

Archived documents remain available for traceability but are not active instructions.

Every archived document should state:

```text
Status: ARCHIVED / SUPERSEDED
Superseded by: <path>
Archived at: <date>
```

Do not delete important historical architecture/design decisions solely to make the repository look cleaner.

===== END VIRTUAL FILE: 99_archive/README.md =====

---

## VIRTUAL FILE 55/56 — `examples/design-system.registry.example.json`

**Virtual path:** `examples/design-system.registry.example.json`  
**Content checksum:** `69a30e09dc80`

===== BEGIN VIRTUAL FILE: examples/design-system.registry.example.json =====

{
  "schemaVersion": "1.1.0",
  "designSystem": {
    "id": "example-product-ds",
    "name": "Example Product Design System",
    "version": "1.1.0",
    "objectLifecycleBaseline": "v1",
    "profilePath": "docs/06_design_system/DESIGN_SYSTEM_PROFILE.md",
    "uiKitPath": "/ui-kit",
    "tokenSourcePath": "src/design-system/tokens",
    "changelogPath": "docs/06_design_system/CHANGELOG.md"
  },
  "items": [
    {
      "id": "COMP-PHRASE-CARD",
      "name": "Phrase Card",
      "slug": "phrase-card",
      "type": "component",
      "contractVersion": "2.0.0",
      "objectStatus": "IMPLEMENTED",
      "owner": "Design System",
      "purpose": "Compact content discovery with detail on demand.",
      "userJob": "Understand primary content quickly and inspect details only when needed.",
      "designPrinciple": "Summary first. Detail on demand.",
      "platforms": [
        "web",
        "mobile-web"
      ],
      "modes": [
        "light"
      ],
      "tags": [
        "learning",
        "audio",
        "disclosure"
      ],
      "aliases": [
        "phrase"
      ],
      "review": {
        "lastReviewed": "2026-09-19",
        "reviewTrigger": "Interaction contract or content-priority change",
        "freshness": "CURRENT"
      },
      "paths": {
        "spec": "docs/06_design_system/components/phrase-card/spec.md",
        "board": "docs/06_design_system/boards/phrase-card-v2.png",
        "source": "src/design-system/components/PhraseCard.tsx",
        "story": "src/design-system/components/PhraseCard.stories.tsx",
        "tests": [
          "src/design-system/components/PhraseCard.test.tsx"
        ],
        "implementedScreenshots": [
          "docs/11_quality_testing/evidence/phrase-card-mobile.png"
        ]
      },
      "relations": {
        "uses": [
          "PRIM-ICON-BUTTON",
          "PRIM-CHIP"
        ],
        "usedBy": [],
        "related": [
          "PATTERN-BOTTOM-SHEET-DETAILS"
        ],
        "doNotConfuseWith": [
          "COMP-PHRASE-PRACTICE"
        ],
        "replacement": null
      },
      "truths": {
        "visualVersion": "2.0.0",
        "specVersion": "2.0.0",
        "codeVersion": "2.0.0",
        "parity": "IN_SYNC"
      },
      "traceability": {
        "requirements": [],
        "featureSpecs": [
          "SPEC-PHRASE-DISCOVERY"
        ],
        "uxRefs": [
          "UX-CONST-001"
        ],
        "architectureRefs": [],
        "decisionRefs": [
          "DDR-012"
        ],
        "testRefs": [
          "src/design-system/components/PhraseCard.test.tsx"
        ],
        "telemetryRefs": [],
        "evidenceRefs": [
          "docs/11_quality_testing/evidence/phrase-card-mobile.png"
        ]
      },
      "deprecation": null
    }
  ]
}

===== END VIRTUAL FILE: examples/design-system.registry.example.json =====

---

## VIRTUAL FILE 56/56 — `examples/document-manifest.example.json`

**Virtual path:** `examples/document-manifest.example.json`  
**Content checksum:** `650488fedee6`

===== BEGIN VIRTUAL FILE: examples/document-manifest.example.json =====

{
  "schemaVersion": "1.0.0",
  "project": {
    "id": "example-product",
    "name": "Example Product",
    "docsRoot": "docs",
    "sourceOfTruthPath": "docs/00_governance/SOURCE_OF_TRUTH.md",
    "docsIndexPath": "docs/README.md"
  },
  "documents": [
    {
      "id": "UX-CONST-001",
      "title": "UX Constitution",
      "path": "docs/05_ux/UX_CONSTITUTION.md",
      "type": "CONSTITUTION",
      "status": "ACTIVE",
      "normativity": "NORMATIVE",
      "owner": "Product Design",
      "version": "1.0",
      "lifetime": "STABLE",
      "canonicalScope": "Experience principles and navigation semantics",
      "created": "2026-09-19",
      "lastReviewed": "2026-09-19",
      "reviewTrigger": "Major IA or interaction-grammar change",
      "freshness": "CURRENT",
      "supersedes": [],
      "supersededBy": null,
      "related": [
        "DS-STD-001"
      ],
      "implementationRefs": [],
      "testRefs": [],
      "evidenceRefs": [],
      "generated": {
        "isGenerated": false,
        "source": null,
        "command": null
      }
    }
  ]
}

===== END VIRTUAL FILE: examples/document-manifest.example.json =====

---

# 5. End-of-bundle rules

When this bundle is used in ChatGPT:

- cite/refer to virtual paths when explaining where a rule came from;
- do not treat the physical single-file packaging as a reason to collapse ownership;
- when generating project files, recreate the virtual folder structure appropriate to the target project's profile;
- if the user asks for a repository-ready package, split the relevant virtual sections back into individual files;
- if the user asks only for advice, do not generate every template automatically.

> **This file is optimized for transport into ChatGPT. The multi-file repository/ZIP remains the canonical maintainable distribution format.**
