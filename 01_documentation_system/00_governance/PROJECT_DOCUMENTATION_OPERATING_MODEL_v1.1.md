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
