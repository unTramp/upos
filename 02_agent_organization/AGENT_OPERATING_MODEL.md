# Agent Organization Operating Model

**ID:** UPOS-02-STD-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AGENT_CONTRACT_STANDARD.md`, `ROLE_CATALOG.md`, `AUTHORITY_MODEL.md`, `SEPARATION_OF_DUTIES.md`

## 0. Purpose

Define the organizational model for governed AI agents without binding U-POS to a specific model provider, agent framework, repository, or project documentation path.

The governing principle is:

> **An agent is not an autonomous source of project truth. It is a role-bound actor operating on externally governed project truth.**

## 1. Organizational entities

### 1.1 Role

A **Role** is an organizational responsibility.

A Role defines:

- the class of outcomes it is accountable for;
- the fact/decision scopes in which it may exercise organizational authority;
- the responsibilities it must perform;
- the areas it must not own;
- expected relationships to other roles.

A Role is abstract. It is not a model process, prompt, API session, or person.

### 1.2 Agent Definition

An **Agent Definition** is a versioned normative contract that implements exactly one canonical Role.

Role composition is not achieved by blurring several Roles into one contract. A configured Agent Instance may be capable of executing multiple compatible Agent Definitions, but each Run selects one explicit Role/Definition identity.

It defines the role-bound mission, scope, non-scope, authority, source requirements, interface requirements, outputs, escalation, handoffs, prohibited behavior, and lifecycle metadata.

An Agent Definition is durable governance.

### 1.3 Agent Instance

An **Agent Instance** is a configured executable realization that MAY bind multiple compatible Agent Definitions.

It may bind:

- a model/provider;
- tool adapters;
- project adapter;
- runtime settings;
- credentials/permission grants;
- enabled/disabled operational state.

Those bindings are not themselves owned by Module 02; they are consumed through downstream interfaces.

### 1.4 Agent Run

An **Agent Run** is one bounded execution under exactly one Role + Agent Definition identity, using one Agent Instance for one assigned responsibility in a task/workflow.

A Run must be attributable to:

- Role;
- Agent Definition identity and version;
- Agent Instance identity/configuration reference;
- task/workflow responsibility.

Run lifecycle and telemetry are owned by downstream Workflow/Observability modules.

## 2. Identity invariants

The following MUST remain distinguishable:

```text
Role
Agent Definition
Agent Instance
Agent Run
```

A provider/model name MUST NOT substitute for a Role identity.

A prompt text MUST NOT substitute for an Agent Definition.

A conversation/session MUST NOT automatically be treated as durable Agent identity.

## 3. Project truth is external

Before acting on a material project fact, an agent must conceptually perform:

```text
task
→ identify fact scope
→ resolve canonical owner using UPOS-01
→ resolve active canonical sources using UPOS-01
→ receive authoritative context through UPOS-05 interface
→ act only inside assigned authority
```

Module 02 never hard-codes repository paths.

If active normative sources conflict:

```text
BLOCK / ESCALATE
```

The agent MUST NOT synthesize a convenient compromise.

If required truth does not exist:

```text
UNKNOWN / OWNER DECISION REQUIRED
```

is valid.

## 4. Agents do not canonize their own outputs

Agent output has an epistemic state.

Typical agent outputs include:

```text
observation
evidence reference
hypothesis
proposal
review finding
learning candidate
decision recommendation
```

Writing an output does not make it canonical project truth.

Canonical promotion is owned by the UPOS-01 Project Knowledge Lifecycle.

Even an agent operating in an authoritative Role may update canonical truth only when the project governance/promotion policy explicitly authorizes that action.

## 5. Organizational authority is scoped

Authority exists only for an identified scope.

Examples:

```text
Product intent/scope
→ Product

Domain semantics/lifecycles/invariants
→ Domain

Architecture boundaries/topology
→ Architecture

UX interaction semantics
→ UX

Reusable Design System contracts
→ Design System

Execution of approved implementation
→ Implementer

Independent verification
→ Reviewer

Behavioral acceptance validation
→ QA

Security constraints
→ Security

Documentation consistency
→ Documentation Guardian

Merge-readiness assessment
→ Merge Controller
```

No role is globally authoritative.

## 6. Orchestrator position

The Orchestrator coordinates the organization.

It may:

- request fact-scope resolution;
- invoke/coordinate routing through UPOS-04 policy;
- assign organizational responsibility consistent with the selected workflow;
- initiate handoffs;
- surface conflicts;
- coordinate progress;
- pause and escalate when a boundary is reached.

It does not become the canonical owner of Product, Domain, Architecture, UX, Security, Quality, or Documentation simply because it coordinates the task.

Workflow selection/routing mechanics are consumed from UPOS-04.

## 7. Creation and verification are different functions

Creation and independent verification are organizationally distinct.

Minimum:

```text
Implementer != Final Reviewer
```

For high-risk work as determined by downstream policy:

```text
Implementer != Reviewer != Merge Controller
```

A self-check is useful but is not independent approval.

## 8. Same model, different role

The same base model/provider may back one Agent Instance that binds multiple compatible Agent Definitions; each Agent Definition still implements exactly one canonical Role, and each Run selects exactly one Role + Agent Definition identity.

This is allowed only when logical role separation remains observable:

- different Role identity;
- correct Agent Definition/version;
- role-specific context;
- role-specific authority;
- separate Run;
- separate evaluation/output;
- no prohibited self-approval path.

Provider diversity may strengthen independence but is not required by Module 02.

## 9. Role composition

A project may instantiate only the roles it needs.

Compatible responsibilities may be composed at the Agent Instance/project-assignment level in small projects if:

- each Role keeps a separate Agent Definition;
- each Run selects one explicit Role/Definition;
- authority remains unambiguous;
- no required independence is violated;
- the project adapter records the composition.

Some compositions are prohibited for the same change by `SEPARATION_OF_DUTIES.md`.

## 10. Agent communication

Agents should coordinate through:

```text
canonical project artifacts
structured handoffs
structured findings
structured decision packets
```

rather than relying on raw conversation history as durable organizational state.

Chat history may be supporting context; it is not the canonical organizational handoff mechanism.

## 11. No hidden authority

An agent MUST NOT continue making project decisions outside an explicit task/run assignment.

Past participation does not grant future authority.

Access to tools does not imply authority to use them for any purpose.

A technically capable action may still be organizationally unauthorized.

## 12. Structured output discipline

When downstream systems depend on an agent output, the Agent Contract must specify a stable output class.

Module 02 owns the requirement that outputs are explicit and attributable.

The detailed schemas for Workflow/Review/QA/Merge/Evidence outputs belong to their owning modules.

## 13. Organizational extensibility

Projects may add specialist Roles.

A new Role must define:

- why an existing Role cannot own the responsibility;
- its canonical fact/decision scope;
- authority boundary;
- relationships and handoffs;
- SoD constraints;
- lifecycle/version.

New Roles MUST NOT be created merely to produce more agents.

## 14. Organizational health principle

The objective is not maximum agent count or maximum autonomy.

The objective is:

```text
clear ownership
bounded authority
independent verification
explicit escalation
traceable human governance
reliable handoffs
durable project knowledge
```

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
