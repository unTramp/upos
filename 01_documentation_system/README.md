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
