# Module 02 Cross-Module Interface Contract

**ID:** UPOS-02-STD-010  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `README.md`, `AGENT_CONTRACT_STANDARD.md`, `AUTHORITY_MODEL.md`

## 0. Purpose

Define what Agent Organization requires from other U-POS modules without taking ownership of their internals.

Module 02 must remain conceptually usable while downstream modules are still unimplemented.

## 1. UPOS-01 Documentation / Source of Truth / Knowledge

### Consumes

```text
resolve fact scope
resolve canonical owner
resolve active canonical sources
identify source conflicts
identify accepted decisions/refinements
classify/promote project knowledge
```

### Module 02 guarantee

Agents never treat their own output as canonical merely because it was produced.

### Does not duplicate

- Source-of-Truth precedence/conflict taxonomy;
- Knowledge Lifecycle states/promotion;
- documentation paths/lifecycle.

## 2. UPOS-03 Skills

### Requires

```text
resolve Skill Definition by ID/capability
verify skill is allowed for Role
obtain skill procedure/version
```

### Module 02 owns only

Which Role may require/use a skill interface.

## 3. UPOS-04 Workflow Engine

### Requires

```text
task/workflow assignment
change/risk classification result
workflow-selected Roles
run/retry state
pause/escalation integration
```

### Module 02 owns only

Role/authority/handoff/escalation semantics.

Orchestrator organizational authority does not imply ownership of routing algorithm semantics.

## 4. UPOS-05 Context & Memory

### Requires

```text
authoritative Context Bundle for Role/task
canonical source references
context minimization
decision/evidence references
```

### Module 02 owns only

Which source classes a Role requires and the rule that authority must be respected.

## 5. UPOS-06 Engineering Governance

### Requires

For engineering Roles, interfaces for:

```text
change plan
implementation execution environment
branch/worktree isolation
Git/PR state
merge operation state
```

### Module 02 owns only

Implementer/Reviewer/Merge Controller organizational responsibilities and SoD.

## 6. UPOS-07 Quality

### Requires

```text
independent review interface
QA interface
evidence/gate interface
readiness status
```

### Module 02 owns only

Verification-role identities, organizational independence, and scoped authority.

## 7. UPOS-08 Observability

### Requires

Stable identifiers sufficient to trace:

```text
Role
Agent Definition/version
Agent Instance
Agent Run
handoff
escalation
human override
veto
```

### Module 02 does not store

Hidden chain-of-thought as organizational truth.

## 8. UPOS-09 Learning

### Requires

Ability to submit:

```text
learning candidate
agent-contract improvement proposal
role-overlap finding
handoff failure pattern
```

### Boundary

Learning does not mutate ACTIVE Agent Definitions automatically.

Evolution goes through governed definition lifecycle and UPOS-01 Knowledge Lifecycle.

## 9. UPOS-10 Security & Permissions

### Requires

```text
permission evaluation
protected-action policy
human-approval policy
security veto policy
secret/production constraints
```

### Module 02 owns only

Organizational authority/SoD/human-governance semantics and Role interface requirements.

## 10. UPOS-11 Project Adapter

### Requires

```text
project-specific canonical-source bindings
Agent Definition → concrete Instance bindings
provider/tool bindings
project Role composition
project overrides within allowed bounds
```

### Boundary

Project adapters may specialize universal defaults.

They MUST NOT silently remove non-overridable Module 02 invariants such as required SoD.

## 11. Failure behavior before downstream implementation exists

If an interface is not yet implemented:

- Module 02 docs remain normative;
- humans/manual processes may satisfy the interface;
- no placeholder automation is allowed to fabricate the missing result;
- unresolved requirements remain explicit.

This permits staged U-POS implementation without semantic duplication.

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
