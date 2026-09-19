# Module 02 Ownership Map

**ID:** UPOS-02-AN-002  
**Type:** ANALYSIS / BOUNDARY MAP  
**Status:** ARCHIVED
**Normativity:** EVIDENCE
**Owner:** UPOS-002 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical implementation/audit evidence is found factually incorrect; normative changes belong in canonical Module 02 artifacts.
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-002 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current organizational rules are owned by the canonical Module 02 normative artifacts; `MODULE_02_TRACEABILITY.md` remains the canonical coverage artifact.


## 1. Owns

| Concern | Module 02 canonical artifact |
|---|---|
| Agent organizational definition | `AGENT_OPERATING_MODEL.md` |
| Agent Contract | `AGENT_CONTRACT_STANDARD.md` |
| Role families / composition | `ROLE_CATALOG.md` |
| Role/Definition/Instance/Run distinction | `AGENT_OPERATING_MODEL.md` |
| Organizational authority/delegation | `AUTHORITY_MODEL.md` |
| Separation of duties | `SEPARATION_OF_DUTIES.md` |
| Handoff organizational contract | `HANDOFF_STANDARD.md` |
| Escalation / scoped veto | `ESCALATION_AND_VETO_MODEL.md` |
| Human governance / explicit override | `HUMAN_GOVERNANCE.md` |
| Agent Definition lifecycle/versioning | `AGENT_LIFECYCLE.md` |
| Core Role definitions | `contracts/*.md` |
| Cross-module organizational interfaces | `CROSS_MODULE_INTERFACES.md` |

## 2. Does not own

| Concern | Deferred owner |
|---|---|
| Skills / skill registry / procedure | UPOS-03 |
| Workflow definitions / C0-C5 / routing / retry | UPOS-04 |
| Retrieval / context assembly / memory | UPOS-05 |
| Git / branches / commits / PR / merge mechanics | UPOS-06 |
| Review/QA procedures / evidence / quality gates | UPOS-07 |
| Telemetry / traces / dashboard | UPOS-08 |
| Learning detection/promotion/evolution | UPOS-09 + UPOS-01 |
| Permission taxonomy / protected actions / secrets / production | UPOS-10 |
| Project manifest / providers / concrete paths | UPOS-11 |

## 3. Boundary tests

A rule belongs to Module 02 if its central question is:

```text
Who is organizationally responsible?
What authority does that Role have?
Which responsibilities must be independent?
How may responsibility be transferred?
When must the Role stop/escalate?
How does human organizational authority interact?
How does an Agent Definition evolve?
```

A rule does not belong to Module 02 if its central question is:

```text
How does the skill execute?
Which workflow step runs next?
How is context retrieved?
How is Git operated?
How exactly is QA performed?
How is the event stored?
How is learning promoted?
Which permission is technically granted?
Where is a project file/provider bound?
```

## 4. Interface rule

Module 02 may say:

> Reviewer must be independent and must produce a structured verification output.

It may not say:

> Reviewer runs these exact QA commands and uses this evidence schema.

The latter belongs to UPOS-07/06/11.
