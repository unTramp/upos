# Role Catalog

**ID:** UPOS-02-STD-003  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `contracts/`, `AUTHORITY_MODEL.md`, `SEPARATION_OF_DUTIES.md`

## 0. Purpose

Define canonical organizational Roles available to U-POS projects.

A project MAY instantiate only the Roles justified by its work.

Role existence does not imply a dedicated provider/model/process must always be running.

## 1. Core Roles

| Role | Primary organizational responsibility | Primary authority scope | Mandatory? |
|---|---|---|---|
| Orchestrator | Coordinate role assignment, handoffs, boundaries and escalations | Process coordination only | Recommended |
| Product | Product intent, scope, non-goals, product trade-offs | Product/business scope | Conditional |
| Domain | Domain semantics, invariants, lifecycles, conceptual ownership | Domain scope | Conditional |
| Architecture | System boundaries, structural ownership, topology and integration constraints | Architecture scope | Conditional |
| UX | Information architecture, flows, interaction semantics and experience intent | UX scope | Conditional |
| Design System | Reusable visual/interaction contracts | Design System scope | Conditional |
| Implementer | Execute an approved change within bounded scope | Implementation execution | Core for code changes |
| Reviewer | Independently verify change suitability and issue review findings | Independent verification | Core for governed code changes |
| QA | Independently validate intended behavior and acceptance | Behavioral acceptance validation | Conditional by downstream quality policy |
| Security | Apply security constraints and scoped security veto | Security scope | Conditional |
| Documentation Guardian | Detect/reconcile documentation drift against canonical ownership | Documentation consistency | Conditional |
| Merge Controller | Assess organizational merge readiness from required gates/approvals | Readiness assessment | Conditional/core in orchestrated mode |

## 2. Orchestrator

Canonical contract: `contracts/orchestrator.md`.

Owns organizational coordination.

Does not own specialist truth.

## 3. Product

Canonical contract: `contracts/product.md`.

Owns product intent and scope where authorized by project governance.

Does not override Domain/Architecture/Security contracts outside Product scope.

## 4. Domain

Canonical contract: `contracts/domain.md`.

Owns the semantic model of the problem domain:

- entity meaning;
- lifecycle meaning;
- invariants;
- domain ownership boundaries.

Domain is intentionally distinct from Architecture.

## 5. Architecture

Canonical contract: `contracts/architecture.md`.

Owns structural system concerns:

- component/service boundaries;
- topology;
- dependency constraints;
- integration architecture;
- canonical technical ownership.

Architecture does not redefine Product intent or Domain semantics.

## 6. UX

Canonical contract: `contracts/ux.md`.

Owns user-experience semantics and interaction intent while respecting Domain and Product truth.

## 7. Design System

Canonical contract: `contracts/design-system.md`.

Owns reusable visual/interaction language, not whole feature behavior.

## 8. Implementer

Canonical contract: `contracts/implementer.md`.

Owns execution inside an approved scope/plan.

Implementation power is not product/domain/architecture authority.

## 9. Reviewer

Canonical contract: `contracts/reviewer.md`.

Owns independent verification findings.

Reviewer does not become Implementer by silently correcting its own blocking findings in the same review role.

## 10. QA

Canonical contract: `contracts/qa.md`.

Owns independent behavioral acceptance validation.

Detailed QA procedures remain UPOS-07.

## 11. Security

Canonical contract: `contracts/security.md`.

Owns security constraints inside security scope and may exercise evidence-based scoped veto.

Detailed security policy and permission enforcement remain UPOS-10.

## 12. Documentation Guardian

Canonical contract: `contracts/documentation-guardian.md`.

Owns detection/reconciliation of documentation consistency problems.

It does not rewrite Source-of-Truth or Knowledge Lifecycle rules.

## 13. Merge Controller

Canonical contract: `contracts/merge-controller.md`.

Owns readiness assessment.

It does not implement the change and does not redefine underlying gate semantics.

## 14. Optional specialist extensibility

Projects MAY define specialists such as:

```text
Data / Analytics
DevOps / SRE
Database
Performance
Accessibility
AI / ML
Frontend Platform
Backend Platform
Mobile Platform
Release
Incident
```

A specialist Role is justified when it has:

- distinct recurring responsibility;
- identifiable authority boundary;
- meaningful independent handoffs;
- workload/risk sufficient to warrant specialization.

## 15. Role composition

Small projects may configure one Agent Instance/base model to bind multiple compatible Agent Definitions, each implementing exactly one canonical Role, for example:

```text
Product + UX
Domain + Architecture
QA + Documentation Guardian
```

Composition is conditional, not universally recommended.

Each Role identity must remain explicit.

Each canonical Role keeps its own Agent Definition/version, and each Run is attributed to exactly one Role + Agent Definition identity.

## 16. Prohibited/controlled compositions

For the same change:

```text
Implementer + Final Reviewer
→ prohibited
```

For high-risk work:

```text
Implementer + Reviewer + Merge Controller
→ must be three logically distinct responsibilities/runs
```

Other compositions may be restricted by Security/Quality/project policy.

## 17. Do not instantiate a swarm

The catalog is a capability menu, not a staffing quota.

The smallest role set that preserves required authority and independence is preferred.

## Upstream governance dependencies

This document consumes, but does not redefine:

- **UPOS-01 Documentation System** — documentation ownership and durable project knowledge governance.
- **Project Source-of-Truth Model (`DOC-GOV-SOT-001`)** — canonical owner/source resolution and conflict semantics.
- **Project Knowledge Lifecycle Model (`DOC-GOV-KL-001`)** — epistemic states and promotion into canonical project knowledge.

When an active normative conflict exists in upstream canonical sources, the affected agent action MUST stop and escalate. Module 02 does not invent a compromise.

## Downstream interface boundary

Module 02 defines organizational contracts only. Detailed semantics remain owned by:

- **UPOS-03 Skills** — skill procedures, registry, versions, evaluation.
- **UPOS-04 Workflow Engine** — workflow definitions, change classification/routing, task/run state and retry mechanics.
- **UPOS-05 Context & Memory** — retrieval, context assembly, context budgets, memory implementation.
- **UPOS-06 Engineering Governance** — Git, branches, commits, PR mechanics, merge mechanics, worktrees/concurrency.
- **UPOS-07 Quality System** — review/QA procedures, evidence model, quality gates and result semantics.
- **UPOS-08 Observability** — events, traces, metrics, provenance and dashboard data.
- **UPOS-09 Learning** — learning detection/evolution; canonical promotion remains governed with UPOS-01.
- **UPOS-10 Security & Permissions** — permission taxonomy, protected actions, secrets, production access and approval enforcement.
- **UPOS-11 Project Adapter** — project-specific bindings, manifests, providers, concrete paths and commands.

Module 02 MAY require an interface from these modules. It MUST NOT duplicate or privately redefine their owned semantics.
