# Human Governance Standard

**ID:** UPOS-02-STD-008  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AUTHORITY_MODEL.md`, `ESCALATION_AND_VETO_MODEL.md`, `SEPARATION_OF_DUTIES.md`

## 0. Purpose

Define the organizational position of humans in U-POS without duplicating downstream permission/approval policy.

The governing principle is:

> **AI execution may be extensive; final protected governance authority remains explicit and policy-bound.**

## 1. Human governance is a constitutional layer

Human Governance may:

- own protected product/governance decisions;
- approve/reject protected proposals;
- resolve authority ambiguity;
- accept/reject risk where policy permits;
- change canonical governance through the appropriate process;
- revoke/delegate agent authority;
- pause/terminate agent work.

Human Governance is not required to micromanage every low-risk action.

## 2. Protected decisions

Module 02 recognizes the concept of a **human-protected decision**.

Exact protected action taxonomy and approval enforcement belong to UPOS-10/project policy.

Typical high-impact areas may include:

- major Product Vision/Scope;
- Domain invariants/lifecycles;
- major Architecture boundaries;
- Security/privacy;
- authorization;
- billing/money;
- retention/deletion;
- irreversible operations;
- major autonomous authority changes.

This list is illustrative at Module 02 level; the controlling policy is downstream/upstream governance.

## 3. Initial operational posture

Module 02 supports a conservative initial posture:

```text
AI:
analyze
propose
coordinate
implement within authority
review within independent role
validate within role
collect evidence
issue readiness recommendation

Human:
retains final authority for protected decisions/actions required by policy
```

Exact change-class thresholds are owned by UPOS-04/UPOS-10, not Module 02.

## 4. Human override

A human override must be explicit when it bypasses/replaces an agent decision or veto.

Record at minimum:

```text
decision
scope
reason
risk accepted
authorized owner
date/time
affected veto/finding
follow-up if any
```

Durable decision/promotion follows UPOS-01.

## 5. Override is not universal bypass

Human Governance operates inside organizational/legal/security policy.

If UPOS-10/project governance marks a constraint non-overridable, Module 02 does not create a bypass.

## 6. Decision packet

Agents SHOULD present concise decision packets for protected human decisions.

Recommended structure:

```text
Question
Why now
Canonical sources
Known facts/evidence
Options
Trade-offs
Risks
Reversibility
Agent recommendation, if requested
Decision owner
```

Recommendations must not hide material disagreement.

## 7. Do not fake consensus

If agents materially disagree, the human decision packet must surface the disagreement and each scoped basis.

Do not report:

```text
"the agents agree"
```

unless they actually do.

## 8. Human attention as scarce governance capacity

Human attention should be focused on:

- ambiguity;
- high impact;
- high risk;
- irreversible change;
- policy/authority changes;
- unresolved specialist conflict.

Downstream policies may automate low-risk work after evidence supports it.

## 9. Human authority delegation

Human owners may delegate bounded authority.

Delegation must be explicit and follows `AUTHORITY_MODEL.md`.

Delegation does not permanently transfer ownership of the governance system.

## 10. Authority changes are governance changes

Material changes such as:

- enabling autonomous merge;
- granting new protected authority;
- removing independent review;
- broadening production-impact authority;

must be reviewed/versioned through the appropriate governance process.

The exact workflow belongs to UPOS-04/UPOS-10/UPOS-11.

## 11. Canonicalization

A human decision does not become discoverable canonical project truth merely because it occurred in chat.

Material decisions must be propagated using UPOS-01 Source-of-Truth and Knowledge Lifecycle rules.

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
