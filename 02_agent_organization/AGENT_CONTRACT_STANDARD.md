# Agent Contract Standard

**ID:** UPOS-02-STD-002  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-02 Agent Organization  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Material change to Module 02 semantics, agent authority, role composition, separation of duties, handoff, escalation, human governance, or Agent Definition lifecycle  
**Related:** `templates/AGENT_CONTRACT_TEMPLATE.md`, `AGENT_LIFECYCLE.md`, `AUTHORITY_MODEL.md`

## 0. Purpose

Define the minimum normative content of a production-grade Agent Definition.

A Role label such as:

```text
"You are a senior architect."
```

is not an Agent Contract.

## 1. Mandatory contract fields

Every production Agent Definition MUST define:

```text
Identity
Role
Mission
Owns
Scope
Non-scope
Authority
Required Sources
Optional Sources
Inputs
Outputs
Tool Interface Requirements
Permission Interface Requirements
Skill Interface Requirements
Quality Interface Requirements
Escalation
Handoffs
Prohibited Behavior
Lifecycle / Version
```

## 2. Identity

Identity must include:

- stable Agent Definition ID;
- human-readable name;
- Role ID/name;
- version;
- lifecycle status.

Identity MUST NOT be only a provider/model identifier.

## 3. Role

The contract references exactly one canonical Role from `ROLE_CATALOG.md` or a governed project extension.

A production Agent Definition MUST NOT fuse multiple organizational Roles into one ambiguous authority contract.

If one configured Agent Instance is capable of several compatible Roles, it binds several distinct Agent Definitions and each Agent Run selects one Role/Definition identity.

Role composition never erases each Role's authority boundary.

## 4. Mission

Mission is one concise statement of the outcome the agent is organizationally responsible for.

A mission must not imply authority outside `Owns`/`Scope`.

## 5. Owns

`Owns` lists the organizational decisions/results for which the Role is the primary accountable actor.

Ownership is scoped.

`Owns` MUST NOT claim canonical project knowledge owned by UPOS-01 documentation layers unless the Role is the authorized owner for that fact scope.

## 6. Scope

`Scope` defines where the agent may act.

A scope can include:

- fact/decision scope;
- type of work;
- artifact class;
- bounded project area resolved through project adapters.

Scope may be narrowed per task/run.

## 7. Non-scope

`Non-scope` explicitly lists adjacent responsibilities the agent must not absorb.

It is mandatory for roles that border other authority domains.

## 8. Authority

Authority references `AUTHORITY_MODEL.md`.

The contract states which organizational authority kinds the Role may exercise and under what conditions.

The contract MUST NOT grant universal authority.

## 9. Required Sources

Required Sources are abstract canonical source classes, not hard-coded project paths.

Example:

```text
Domain canonical source for affected lifecycle
Relevant accepted decisions
Task/approved plan
```

Concrete source resolution is performed through UPOS-01 + UPOS-05 + UPOS-11 interfaces.

If a required source cannot be resolved, the agent escalates rather than inventing.

## 10. Optional Sources

Optional Sources may improve execution but do not replace Required Sources.

Historical/research/evidence sources must retain their upstream authority classification.

## 11. Inputs

Inputs describe the organizational payload the Run requires.

Input schemas may later be machine-readable, but their semantic owner remains this contract or the downstream owning module.

## 12. Outputs

Outputs must identify their epistemic/organizational class.

Examples:

```text
PROPOSAL
OBSERVATION
REVIEW_FINDING
DECISION_PACKET
HANDOFF
READINESS_ASSESSMENT
```

An output is not automatically `CANONICAL`.

Canonical promotion is governed by UPOS-01 Knowledge Lifecycle.

## 13. Tool Interface Requirements

The contract may state required tool capabilities.

Example:

```text
requires repository read
requires change inspection
requires structured handoff emission
```

Concrete tool/provider binding belongs to UPOS-11.

Tool possession does not grant organizational authority.

## 14. Permission Interface Requirements

The contract declares permission needs as interface requirements.

UPOS-10 owns:

- permission taxonomy;
- grants;
- protected actions;
- production/secrets policy;
- enforcement.

Agent Contract wording MUST NOT bypass UPOS-10.

## 15. Skill Interface Requirements

The contract may require or permit Skill IDs/capabilities.

UPOS-03 owns:

- skill procedure;
- registry;
- versions;
- evaluation.

Module 02 does not copy Skill internals into Agent Definitions.

## 16. Quality Interface Requirements

The contract states which downstream quality interactions apply.

UPOS-07 owns:

- review procedure;
- QA procedure;
- evidence semantics;
- gate semantics.

A Role cannot satisfy an independence requirement merely by declaring its own quality output.

## 17. Escalation

Every contract must state conditions that force stop/escalation.

At minimum, consider:

- source conflict;
- required truth missing;
- authority boundary reached;
- scope expansion;
- specialist veto;
- protected human decision;
- inability to reach a governed result.

Retry thresholds/mechanics belong to UPOS-04.

## 18. Handoffs

The contract lists normal outgoing/incoming organizational handoffs and expected recipient Roles.

All handoffs follow `HANDOFF_STANDARD.md`.

## 19. Prohibited Behavior

The contract makes critical non-authorities explicit.

Examples:

```text
must not invent domain semantics
must not self-approve final review
must not silently override specialist veto
must not canonize unreviewed proposal
```

## 20. Lifecycle / Version

Every Agent Definition follows `AGENT_LIFECYCLE.md`.

Material changes to:

- authority;
- scope/non-scope;
- separation constraints;
- required sources;
- required outputs;
- escalation;
- prohibited behavior;

require a reviewed version change.

## 21. Frozen `Process` field normalization

The frozen design-source Agent Contract template included a `Process` field.

UPOS-002 preserves that intent without making Agent Organization the owner of executable procedure:

```text
organizational invariants / mandatory role behavior
→ Agent Contract

reusable procedure
→ UPOS-03 Skill

cross-role sequencing / workflow procedure
→ UPOS-04 Workflow
```

An Agent Contract MAY state a non-negotiable organizational step such as:

```text
must resolve canonical source before making a scoped decision
must escalate on authority conflict
```

It MUST NOT duplicate a detailed implementation/review/workflow procedure that belongs to another module.

## 22. Contract inheritance and reuse

Shared language may be referenced from Module 02 standards.

Do not copy foundational policies into every contract.

A contract should be specific enough to operate the Role while referencing canonical standards for shared rules.

## 23. Conformance

An Agent Definition is conformant only when all mandatory fields are present and it does not steal ownership from another U-POS module.

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
