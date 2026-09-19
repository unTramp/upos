# Agent Authority Model

**ID:** UPOS-02-STD-004  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `ROLE_CATALOG.md`, `SEPARATION_OF_DUTIES.md`, `ESCALATION_AND_VETO_MODEL.md`, `HUMAN_GOVERNANCE.md`

## 0. Purpose

Provide deterministic organizational authority resolution without creating a universal super-agent.

The governing principle is:

> **Authority follows fact/decision scope and explicit delegation, not model capability, senior-sounding role names, majority vote, or orchestration position.**

## 1. Organizational authority kinds

Module 02 recognizes these organizational authority kinds:

### 1.1 Canonical-scope decision authority

Authority to make/approve a decision within a Role's owned fact scope when project governance delegates that decision to the agent.

### 1.2 Coordination authority

Authority to coordinate assignment, handoff, sequencing concerns and escalation without owning specialist truth.

Typical owner: Orchestrator.

### 1.3 Execution authority

Authority to perform an approved change within bounded scope.

Typical owner: Implementer.

### 1.4 Verification authority

Authority to independently assess a change and produce findings/verdict recommendations within verification scope.

Typical owners: Reviewer, QA.

### 1.5 Scoped veto authority

Authority to block progression because a concrete scoped constraint is violated.

Typical examples: Security, Architecture, Reviewer.

A veto is not universal authority.

### 1.6 Delegated authority

Temporary/task-bounded authority explicitly granted by an authorized owner.

Delegation can narrow or transfer a specific responsibility.

It cannot silently create authority the delegator did not possess.

### 1.7 Human governance authority

Authority reserved to the human/authorized governance layer for protected decisions, overrides, final decisions, or actions required by policy.

## 2. Default authority map

| Fact/decision concern | Organizational authority |
|---|---|
| Product intent and scope | Product |
| Domain semantics/lifecycles/invariants | Domain |
| Architecture boundaries/topology | Architecture |
| UX interaction semantics | UX |
| Reusable Design System contracts | Design System |
| Approved implementation execution | Implementer |
| Independent change verification | Reviewer |
| Behavioral acceptance validation | QA |
| Security constraints | Security |
| Documentation consistency | Documentation Guardian |
| Merge-readiness assessment | Merge Controller |
| Protected final decision | Human Governance where policy requires |

This map is a universal organizational default.

Concrete project canonical owners are resolved through UPOS-01 and project bindings.

## 3. Deterministic authority resolution

When a material decision is required:

```text
1. Identify the exact claim/decision.
2. Resolve fact scope through UPOS-01.
3. Resolve canonical owner/source through UPOS-01.
4. Identify the Role corresponding to that scope.
5. Determine whether the assigned Agent Definition/Run has decision, execution, verification, or advisory authority.
6. Apply downstream Security/Permission/Human policies.
7. If one authorized owner exists and no blocking constraint conflicts → proceed within scope.
8. If active canonical sources conflict → BLOCK / ESCALATE.
9. If ownership overlaps or is ambiguous → ESCALATE.
10. If a protected human decision is required → HUMAN GOVERNANCE.
```

## 4. Constraints are not ownership theft

A Security constraint may restrict a Product intention without becoming the Product owner.

An Architecture invariant may restrict an implementation without becoming the Domain owner.

A Reviewer finding may block merge without becoming the implementation owner.

This is constraint interaction, not global precedence.

## 5. Orchestrator authority

Orchestrator may:

- coordinate;
- request scope/source resolution;
- assign organizational roles;
- create handoffs;
- surface authority conflicts;
- pause/escalate.

Orchestrator MUST NOT:

- silently overrule Product inside Product scope;
- silently redefine Domain semantics;
- waive Security constraints;
- declare its own implementation independently reviewed;
- treat routing responsibility as universal decision authority.

## 6. Specialist authority

A specialist exercises authority only inside:

```text
declared Role scope
+
resolved task scope
+
active canonical contract
+
delegated authority
+
permission/policy constraints
```

If any element is missing, authority is not assumed.

## 7. Authority conflict

Agent disagreement is resolved by:

```text
fact scope
→ canonical owner
→ active normative source
→ scoped constraints
→ delegated authority
→ human governance when required
```

It is not resolved by:

```text
majority vote
model confidence
longer explanation
seniority persona
Orchestrator preference
```

## 8. Majority voting

Voting may be used by downstream systems for narrow evaluation tasks.

It MUST NOT replace canonical ownership for project governance.

## 9. Delegation contract

Delegation must identify:

- delegator;
- delegate;
- task/scope;
- authority granted;
- authority explicitly not granted;
- duration/run applicability;
- constraints;
- escalation condition.

A Handoff MAY carry delegation, but a Handoff does not imply delegation by default.

## 10. Authority expiry

Task/run-bounded delegated authority ends when:

- the assigned responsibility completes;
- the Run ends/cancels;
- the delegation is revoked;
- the scope changes beyond delegation;
- policy requires renewed approval.

Past authority is not persistent entitlement.

## 11. Tool capability is not authority

Being technically able to:

```text
write
approve
merge
deploy
modify
```

does not organizationally authorize the action.

UPOS-10 evaluates permissions/protected actions.

## 12. Canonical truth vs agent decision

An agent decision may be valid organizationally but is not automatically canonical project knowledge.

Canonical promotion follows UPOS-01 Knowledge Lifecycle.

## 13. Unsupported claims

If an agent asserts a project fact without resolvable authority/source, the claim is non-canonical and must be treated as:

```text
observation / hypothesis / proposal
```

or escalated for owner decision.

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
