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
