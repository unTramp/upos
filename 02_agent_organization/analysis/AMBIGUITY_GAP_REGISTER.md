# UPOS-002 Ambiguity and Gap Register

**ID:** UPOS-02-AN-004  
**Type:** ANALYSIS / GAP REGISTER  
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


| ID | Ambiguity / overlap | Resolution for UPOS-002 | Deferred owner |
|---|---|---|---|
| G02-001 | Frozen source combines Domain / Architecture | Split into distinct Roles because UPOS-01 fact scopes differ; allow explicit compatible composition | — |
| G02-002 | Human Governance vs human approval policy | Module 02 owns constitutional human authority/override; approval mechanics/protected actions remain downstream | UPOS-10 / UPOS-04 |
| G02-003 | Security veto overlaps Security policy | Module 02 owns veto organizational contract; substantive security rule and overridability remain Security policy | UPOS-10 |
| G02-004 | Reviewer veto overlaps Quality | Module 02 owns organizational blocking authority/independence; review criteria/evidence/verdict mechanics remain Quality | UPOS-07 |
| G02-005 | Merge Controller overlaps Git/Quality/Permissions | Module 02 owns Role mission/readiness authority; merge mechanics→06, evidence→07, permission/approval→10 | 06/07/10 |
| G02-006 | Orchestrator appears to select workflow/risk | Module 02 owns coordination authority; classification/routing algorithm/state remains Workflow Engine | UPOS-04 |
| G02-007 | Frozen Agent lifecycle includes `DISABLED` | Normalize `DISABLED` to instance/config operational availability; definition lifecycle remains semantic governance lifecycle | UPOS-11/runtime |
| G02-008 | Agent Run lifecycle appears in frozen source | Module 02 owns Run concept/identity distinction only; run state machine/telemetry remain downstream | UPOS-04/08 |
| G02-009 | Versioning lacks machine format | Module 02 defines material-change/version requirement; schema representation is deferred to the cross-cutting machine-readable schemas layer | U-POS machine-readable schemas layer / cross-cutting schemas |
| G02-010 | Agent output vs canonical knowledge | Agent output retains epistemic state; promotion is never owned by Module 02 | UPOS-01 / UPOS-09 |
| G02-011 | Agent Contract includes Skills/Permissions/Quality/Tools | Contract contains interface requirements only; internals remain downstream | 03/07/10/11 |
| G02-012 | Same base model / Agent Instance binds multiple compatible Agent Definitions | Allowed only when each Agent Definition implements exactly one canonical Role and each Run selects exactly one Role + Agent Definition identity; provider/model selection remains adapter concern | UPOS-11 |
| G02-013 | Frozen human approval examples use C0–C5 | Module 02 states human-protected authority only; exact class thresholds remain Workflow/Security policy | UPOS-04/10 |
| G02-014 | Project-specific role composition | Module 02 defines universal compatibility/SoD; concrete composition belongs project binding | UPOS-11 |
| G02-015 | Can human override every veto? | No universal bypass; override exists only when policy permits; non-overridable controls stay enforceable | UPOS-10 |

| G02-016 | Agent Definition vs compatible multi-definition Agent Instance | One Agent Definition implements exactly one canonical Role; one Agent Instance/base model may bind multiple compatible Agent Definitions; each Run selects exactly one Role + Agent Definition identity | UPOS-11/08 for binding/telemetry |

## Open gaps

No P0/P1 semantic gap remains inside the requested Module 02 ownership.

Future downstream modules still need to formalize the interfaces referenced above.
