# Module 03 Ownership Map

**ID:** UPOS-03-AN-002  
**Type:** ANALYSIS / BOUNDARY MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-003 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 03 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the completed UPOS-003 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Skills semantics are owned by canonical Module 03 normative artifacts; `MODULE_03_TRACEABILITY.md` remains the canonical coverage artifact.


## Owns

- Skill identity/definition;
- versioned Skill Contract;
- bounded procedure;
- inputs/outputs/preconditions;
- source/context/tool/permission interface requirements;
- applicable Role compatibility;
- procedural invariants;
- Skill-level quality criteria;
- failure/escalation;
- dependencies/composition;
- registry/taxonomy/discovery;
- lifecycle/versioning/deprecation/supersession;
- Skill evaluation;
- Skill evolution interface;
- universal Skill library.

## Does not own

| Concern | Owner |
|---|---|
| Roles/authority/SoD | UPOS-002 |
| Workflow/routing/C0-C5/retry | UPOS-004 |
| Retrieval/context/memory | UPOS-005 |
| Git/PR/merge policy | UPOS-006 |
| Evidence/verdict/gates | UPOS-007 |
| Telemetry/metrics | UPOS-008 |
| Learning detection/promotion | UPOS-009 + UPOS-01 |
| Permissions/protected actions | UPOS-010 |
| Provider/project bindings | UPOS-011 |

## Boundary test

A rule belongs to Module 03 when its central question is:

```text
What reusable bounded capability exists?
What inputs/outputs/preconditions/procedure define it?
How is it versioned/discovered/evaluated/composed?
```

It does not belong when the central question is:

```text
Who has authority?
Which step runs next?
How is context retrieved?
What is a valid PR/merge?
What evidence verdict blocks merge?
Who gets permission?
Which provider/path implements it?
```
