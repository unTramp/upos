# UPOS-002 — Agent Organization

**ID:** UPOS-02-MOD-001  
**Type:** MODULE INDEX / NORMATIVE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AGENT_OPERATING_MODEL.md`, `AGENT_CONTRACT_STANDARD.md`, `ROLE_CATALOG.md`, `AUTHORITY_MODEL.md`, `SEPARATION_OF_DUTIES.md`, `HANDOFF_STANDARD.md`, `ESCALATION_AND_VETO_MODEL.md`, `HUMAN_GOVERNANCE.md`, `AGENT_LIFECYCLE.md`, `CROSS_MODULE_INTERFACES.md`, `MODULE_02_TRACEABILITY.md`
**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-002 defines the **organizational constitution for AI agents** operating inside U-POS.

It answers:

```text
What is a Role?
What is an Agent Definition?
What is an Agent Instance?
What is an Agent Run?
Which responsibility belongs to which role?
Who may decide what?
Who may delegate what?
Who must remain independent?
How is work handed off?
When must an agent stop and escalate?
What does a scoped veto mean?
Where does human authority sit?
How do Agent Definitions evolve?
```

It does **not** define workflows, Git mechanics, QA procedure, permissions implementation, telemetry, learning promotion, or project-specific bindings.

## 1. Canonical package

```text
02_agent_organization/
├── README.md
├── AGENT_OPERATING_MODEL.md
├── AGENT_CONTRACT_STANDARD.md
├── ROLE_CATALOG.md
├── AUTHORITY_MODEL.md
├── SEPARATION_OF_DUTIES.md
├── HANDOFF_STANDARD.md
├── ESCALATION_AND_VETO_MODEL.md
├── HUMAN_GOVERNANCE.md
├── AGENT_LIFECYCLE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_02_TRACEABILITY.md
│
├── contracts/
│   ├── orchestrator.md
│   ├── product.md
│   ├── domain.md
│   ├── architecture.md
│   ├── ux.md
│   ├── design-system.md
│   ├── implementer.md
│   ├── reviewer.md
│   ├── qa.md
│   ├── security.md
│   ├── documentation-guardian.md
│   └── merge-controller.md
│
├── templates/
│   ├── AGENT_CONTRACT_TEMPLATE.md
│   └── HANDOFF_TEMPLATE.md
│
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_02_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── IMPLEMENTATION_PLAN.md
    └── TRACEABILITY_VALIDATION.md
```

## 2. Core invariant

```text
Implementer != Final Reviewer
```

For work classified as high-risk by the owning workflow/security policy:

```text
Implementer != Reviewer != Merge Controller
```

This is logical separation of responsibility, not a requirement for different model vendors.

## 3. Organizational model

```text
UPOS-01 CANONICAL PROJECT TRUTH
              │
              ▼
       SOURCE RESOLUTION
              │
              ▼
      AGENT ORGANIZATION
              │
     ┌────────┼─────────┐
     ▼        ▼         ▼
 AUTHORITY  HANDOFF   ESCALATION
     │        │         │
     └────────┼─────────┘
              ▼
        ROLE-BOUND WORK
              │
              ▼
  DOWNSTREAM EXECUTION SYSTEMS
```

## 4. Conceptual identity model

```text
ROLE
= organizational responsibility

AGENT DEFINITION
= versioned normative contract implementing exactly one canonical Role

AGENT INSTANCE
= configured executable realization that MAY bind multiple compatible Agent Definitions

AGENT RUN
= one bounded execution under exactly one Role + Agent Definition identity
```

These concepts MUST NOT be used interchangeably.

## 5. Canonical ownership

This module is canonical for:

- agent organizational identity;
- Agent Contract requirements;
- roles and role families;
- role responsibilities and non-scope;
- organizational authority and delegation;
- separation of duties;
- role relationship rules;
- organizational handoff semantics;
- escalation and scoped veto semantics;
- human governance and explicit human override;
- Agent Definition lifecycle and versioning;
- role composition constraints.

## 6. Explicit non-ownership

This module is not canonical for:

- skill procedures/registry;
- workflow/C0–C5 routing;
- context retrieval/memory;
- Git/commit/PR/merge mechanics;
- review/QA procedure and evidence models;
- telemetry/dashboard;
- learning promotion;
- permission taxonomy/secrets/production access;
- project manifests/provider adapters.

## 7. Required reading order

For work changing Module 02:

1. upstream Project Source-of-Truth Model;
2. upstream Project Knowledge Lifecycle Model;
3. this README;
4. `AGENT_OPERATING_MODEL.md`;
5. the specific owning standard;
6. affected role contract;
7. `MODULE_02_TRACEABILITY.md`.

## 8. Frozen design source

`UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md` is a frozen design input.

It is **not** the active Module 02 contract.

Module 02 preserves its owned semantics through explicit traceability and defers non-owned semantics to the future owning modules.

## 9. Completion status

The Module 02 normative package is complete when:

```text
UNMAPPED MODULE-02 SOURCE REQUIREMENTS = 0
```

See `MODULE_02_TRACEABILITY.md` and `analysis/TRACEABILITY_VALIDATION.md`.

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
