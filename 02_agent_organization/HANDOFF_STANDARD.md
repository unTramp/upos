# Agent Handoff Standard

**ID:** UPOS-02-STD-006  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `templates/HANDOFF_TEMPLATE.md`, `AUTHORITY_MODEL.md`, `ESCALATION_AND_VETO_MODEL.md`

## 0. Purpose

Define the organizational contract for transferring responsibility/context between Roles.

A Handoff is not a raw transcript dump and not an implicit authority transfer.

## 1. Handoff principle

A good handoff allows the receiving Role to answer:

```text
What am I being asked to produce?
Which truth is authoritative?
What has already been decided?
What constraints apply?
Which evidence/artifacts matter?
What remains open?
What authority do I have?
What authority do I explicitly not have?
What action is expected next?
```

## 2. Mandatory fields

Every material Handoff MUST preserve:

```text
from
to
task
expected outcome
canonical sources
decisions already made
constraints
artifacts
evidence refs
open questions
authority delegated
authority explicitly not delegated
required next action
```

It SHOULD also carry:

- handoff ID;
- source Agent Definition/Run reference;
- target Role;
- reason for handoff;
- known blockers;
- relevant provenance.

## 3. `from`

Identifies the sending Role/Run.

A Handoff should not attribute claims merely to a model provider.

## 4. `to`

Identifies the receiving Role, not only a person/model name.

Concrete instance assignment may be resolved downstream.

## 5. Canonical sources

Canonical sources must be resolved through UPOS-01 interfaces.

The Handoff SHOULD transmit references/identifiers, not duplicated truth where avoidable.

## 6. Decisions already made

Only accepted decisions should be labelled as decisions.

Proposals/hypotheses/findings must retain their epistemic state.

## 7. Constraints

Constraints include organizational, canonical and task-bounded limitations.

A sender cannot invent new constraints outside its authority.

## 8. Artifacts and evidence refs

Artifacts/evidence are referenced with provenance where possible.

Evidence does not automatically become canonical truth.

## 9. Open questions

Open questions remain explicit.

The sender MUST NOT hide unresolved ambiguity by writing a confident summary.

## 10. Authority delegated

If authority is delegated, the Handoff must state exactly:

- what authority;
- for what scope;
- for what responsibility;
- any expiry/return condition.

## 11. Authority explicitly not delegated

This field prevents accidental authority expansion.

Example:

```text
May propose architecture impact.
May not change product scope.
May not approve security exception.
```

## 12. Required next action

The Handoff identifies the organizational outcome expected next.

Detailed workflow transition mechanics belong to UPOS-04.

## 13. Handoff types

Module 02 recognizes semantic categories such as:

- delegation handoff;
- consultation handoff;
- verification handoff;
- escalation handoff;
- decision-request handoff.

A project/runtime may represent these differently.

## 14. Acceptance/rejection

The receiving Role may reject or escalate a Handoff when:

- required context is missing;
- canonical sources conflict;
- authority is invalid;
- task lies outside Role scope;
- protected decision requires another owner.

Exact runtime state/retry behavior belongs to UPOS-04.

## 15. No raw conversation as canonical handoff

Raw conversation history may be attached as supporting context when necessary.

The canonical handoff must remain structured.

Important decisions must be materialized into governed project artifacts through UPOS-01.

## 16. Handoff and context minimization

Module 02 requires semantic completeness, not maximal volume.

UPOS-05 owns context-budget/retrieval mechanics.

## 17. Handoff and telemetry

Module 02 owns handoff meaning.

UPOS-08 owns event/trace recording.

The handoff should expose stable identifiers sufficient for later observability.

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
