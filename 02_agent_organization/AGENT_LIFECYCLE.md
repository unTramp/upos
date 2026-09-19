# Agent Definition Lifecycle and Versioning Standard

**ID:** UPOS-02-STD-009  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AGENT_CONTRACT_STANDARD.md`, `ROLE_CATALOG.md`

## 0. Purpose

Define lifecycle/version semantics for **Agent Definitions** separately from Agent Instances, Agent Runs, tasks and workflows.

## 1. Required distinction

```text
Agent Definition lifecycle
!= Agent Instance operational state
!= Agent Run lifecycle
!= Task lifecycle
!= Workflow lifecycle
```

Module 02 owns Agent Definition lifecycle.

UPOS-04/UPOS-08 own Run/workflow execution state.

UPOS-11/runtime adapters own concrete Instance configuration/binding state.

## 2. Agent Definition lifecycle

Canonical lifecycle:

```text
DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

Permitted alternate paths include:

```text
DRAFT → RETIRED
REVIEW → DRAFT
APPROVED → REVIEW   # if material issues reopen before activation
ACTIVE → REVIEW     # when a material contract change is proposed as a new version
```

A new material version normally progresses independently while the prior ACTIVE version remains usable until replacement is activated.

## 3. State semantics

### DRAFT

Contract is being authored.

Not authorized for production organizational use unless project policy explicitly allows experimental mode.

### REVIEW

Contract authority/scope/SoD/interfaces are under governance review.

### APPROVED

Contract has been accepted for use but is not yet the active default definition.

### ACTIVE

Definition is the current approved contract for its identity/version line.

### DEPRECATED

Definition remains available for transition/backward compatibility but should not be assigned to new work unless explicitly required.

A replacement should be referenced where applicable.

### RETIRED

Definition must not be assigned to new work.

Retained only for historical traceability/audit.

## 4. What happened to `DISABLED`

The frozen design source listed `DISABLED` among possible agent lifecycle labels.

UPOS-002 normalizes this as an **operational Agent Instance/configuration state**, not an Agent Definition lifecycle state.

Reason:

- a valid ACTIVE definition may have zero currently enabled instances;
- temporary operational disablement does not semantically retire/deprecate the contract;
- definition lifecycle and runtime availability must not share one enum.

No source semantics are lost: the ability to disable an executable agent remains a required downstream interface.

## 5. Versioning rule

Agent Definitions must be versioned when behavior materially changes.

Material changes include:

- authority expansion/reduction;
- scope/non-scope change;
- role composition change;
- SoD implications;
- required source changes that alter behavior;
- output contract breaking change;
- escalation/veto change;
- prohibited behavior change.

## 6. Recommended version semantics

A project MAY use semantic versions:

```text
MAJOR
→ breaking authority/contract/behavioral change

MINOR
→ backward-compatible capability or optional contract addition

PATCH
→ editorial clarification with no semantic authority/behavior change
```

Concrete machine schema is deferred to the **U-POS machine-readable schemas layer / cross-cutting schemas**.

## 7. Version immutability

Once an Agent Definition version is ACTIVE and used for audited Runs, material semantic changes should create a new version rather than silently mutating historical meaning.

Editorial corrections may update metadata according to documentation governance if they do not change semantics.

## 8. Activation

Activation should verify at least:

- complete Agent Contract;
- authority boundary reviewed;
- SoD compatibility reviewed;
- cross-module interface references valid;
- required upstream sources resolvable in principle;
- no unresolved P0 authority conflict.

Exact activation workflow belongs to UPOS-04/project governance.

## 9. Deprecation

Deprecation should record:

- reason;
- replacement if any;
- migration/transition note;
- effective date.

Do not delete old definitions needed to interpret historical Runs.

## 10. Retirement

Retirement ends assignment eligibility.

Historical records must retain definition ID/version references.

## 11. Agent Instance operational state

Module 02 requires downstream systems to distinguish definition lifecycle from instance availability.

An implementation may expose states such as:

```text
CONFIGURED
ENABLED
DISABLED
UNAVAILABLE
```

but exact instance state machine is not canonical Module 02 semantics.

## 12. Agent Run identity

Every Run should be able to identify:

- Role;
- Agent Definition ID/version;
- Agent Instance reference;
- assigned task/responsibility.

Exact Run states/telemetry are deferred.

## 13. Lifecycle governance

Material contract evolution is itself a governance change.

It must not be learned/modified silently by an agent from prior chats or hidden memory.

Proposed improvements may enter the Learning/Knowledge Lifecycle; activation requires explicit governed promotion.

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
