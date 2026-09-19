# Escalation and Veto Model

**ID:** UPOS-02-STD-007  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `AUTHORITY_MODEL.md`, `HUMAN_GOVERNANCE.md`, `HANDOFF_STANDARD.md`

## 0. Purpose

Define when agents must stop autonomous progression, where organizational escalation goes, and what a valid specialist veto means.

## 1. Mandatory escalation triggers

An agent MUST escalate when:

```text
canonical sources conflict
required truth is missing
authority boundary is reached
two roles claim overlapping authority
risk exceeds assigned authority
a specialist veto occurs
a human-protected decision is required
repeated execution/review loop cannot converge
```

It must also escalate when its contract-specific prohibited behavior would otherwise be required to proceed.

## 2. Missing canonical truth

When required truth is absent:

```text
UNKNOWN / OWNER DECISION REQUIRED
```

The agent may produce a proposal.

It may not silently promote its proposal into truth.

## 3. Canonical-source conflict

When active normative sources conflict:

```text
BLOCK affected decision
→ identify fact scope
→ resolve owner via UPOS-01
→ escalate to authorized owner/human governance
```

Do not merge claims into a compromise automatically.

## 4. Authority overlap

When two Roles claim the same decision:

1. identify the exact fact/decision;
2. resolve fact scope;
3. resolve canonical owner;
4. identify constraint owners;
5. distinguish ownership from constraint/veto;
6. escalate if scope remains ambiguous.

## 5. Veto definition

A **veto** is a scoped organizational block preventing workflow progression because a concrete governing constraint/finding is unresolved.

A veto is valid only when it includes:

```text
vetoing Role
scope
affected artifact/change
canonical rule/policy/evidence basis
concrete blocking finding
required condition to unblock
escalation/override path if one exists
```

## 6. Veto is not preference

Invalid:

```text
"I do not like this approach."
```

Valid shape:

```text
BLOCKING:
The change violates the canonical authorization constraint <ref>.
Unblock by conforming implementation or obtaining an authorized contract/policy change.
```

## 7. Security veto

Module 02 owns the organizational fact that Security may exercise a scoped veto within Security authority.

UPOS-10 owns:

- security policy;
- protected actions;
- risk acceptance rules;
- whether a specific constraint is overridable.

Security MUST NOT use security veto to make unrelated Product/UX decisions.

## 8. Architecture veto

Architecture may block a change that violates an active architecture contract inside Architecture scope.

Unblock requires either:

- implementation conforms; or
- architecture is changed through the governed decision path.

Architecture veto MUST NOT be based only on personal style preference.

## 9. Reviewer veto / blocking finding

Reviewer may block merge-readiness progression for concrete verification findings.

UPOS-07 owns review criteria/severity/evidence semantics.

Reviewer does not become Product/Architecture/Security owner by raising a finding.

## 10. Documentation conflict veto

Documentation Guardian may block documentation readiness when shipped/changed semantics would leave canonical project documentation inconsistent.

It cannot resolve the underlying Product/Domain/Architecture truth by itself unless it is also the authorized owner in a separately identified Role.

## 11. Orchestrator and veto

Orchestrator coordinates the response to a veto.

It MUST NOT silently waive a valid specialist veto.

It may:

- route correction;
- request owner decision;
- surface conflict;
- request human governance.

## 12. Human override

Human override follows `HUMAN_GOVERNANCE.md`.

An override must not be assumed to exist for every veto.

UPOS-10/project governance may define non-overridable constraints.

## 13. Repeated non-convergence

If implementation/review or agent-agent disagreement repeatedly fails to converge, Module 02 requires escalation.

Exact retry thresholds and workflow mechanics belong to UPOS-04.

## 14. Escalation targets

Potential targets include:

```text
Orchestrator
scoped Product owner
scoped Domain owner
scoped Architecture owner
Security owner
Documentation owner
Human Project Owner / Governance authority
```

The target is chosen by scope, not seniority theater.

## 15. Epistemic discipline

An escalation packet should distinguish:

- observed facts;
- evidence;
- interpretations;
- proposals;
- unresolved decision.

This prevents disagreement from being disguised as settled truth.

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
