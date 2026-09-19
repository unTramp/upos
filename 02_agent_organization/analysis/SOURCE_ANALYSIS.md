# UPOS-002 Source Analysis

**ID:** UPOS-02-AN-001  
**Type:** ANALYSIS / DESIGN EVIDENCE  
**Status:** ARCHIVED
**Normativity:** EVIDENCE
**Owner:** UPOS-002 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical implementation/audit evidence is found factually incorrect; normative changes belong in canonical Module 02 artifacts.
**Related:** `../MODULE_02_TRACEABILITY.md`

> **Historical evidence notice:** This file records the completed UPOS-002 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current organizational rules are owned by the canonical Module 02 normative artifacts; `MODULE_02_TRACEABILITY.md` remains the canonical coverage artifact.



## 0. Source integrity

| Source | SHA-256 |
|---|---|
| UPOS-01 Documentation System bundle | `0eed3f1319103b9fef7956519da9754986b7c512a05278c030c38edbaddcb3a1` |
| Project Source-of-Truth Model | `06913d3ba3585f2dd8676f2edc2ad82b43fad548b91e5fb57bec18a7c975bafd` |
| Project Knowledge Lifecycle Model | `5e1a7653f22c218820b2c675f6f34bcf6bef5ad139bb0ce1639acae14cc2d885` |
| Frozen AI Agent Operating Model | `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699` |

## 1. Source authority model

### Source A — UPOS-01 Documentation System

**Authority:** ACTIVE upstream normative system.

Used for:

- documentation authority boundaries;
- durable canonical knowledge;
- document/decision ownership;
- project knowledge governance.

Module 02 references it and does not copy/decompose it.

### Source B — Project Source-of-Truth Model (`DOC-GOV-SOT-001`)

**Authority:** ACTIVE upstream normative governance contract.

Consumed interface:

```text
resolve fact scope
→ resolve canonical owner
→ resolve canonical sources
→ detect conflict/missing owner
```

Key consequence for Module 02:

> Agent authority never substitutes for canonical fact ownership.

### Source C — Project Knowledge Lifecycle (`DOC-GOV-KL-001`)

**Authority:** ACTIVE upstream normative governance contract.

Consumed boundary:

```text
agent output
→ observation/evidence/hypothesis/proposal/finding/learning candidate
→ review/validation/promotion
→ canonical knowledge only when UPOS-01 governance permits
```

Key consequence:

> Agent output is not doctrine.

### Source D — Frozen `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md`

**Authority:** FROZEN MASTER DESIGN INPUT.

**SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`

Used only to recover Module 02 semantics and identify deferred semantics for UPOS-03…11.

It is not copied wholesale into Module 02.

## 2. Extracted Module 02 themes

The frozen source contains Module 02 semantics across:

- foundational Human Governance / SoD / authority principles;
- Agent terminology and Agent Contract;
- role families and role descriptions;
- Orchestrator boundaries;
- reviewer independence;
- handoff;
- escalation;
- authority conflict/veto/human override;
- communication/no circular authority;
- agent composition;
- Agent Contract versioning/lifecycle;
- hallucination/missing-source behavior;
- no hidden authority;
- decision packets/consensus;
- anti-patterns;
- minimal/intermediate/advanced organizational sets;
- final organizational principles;
- Agent Contract and Handoff appendices.

The frozen source also contains large bodies owned by other U-POS modules. Those are classified, not copied.

## 3. Key normalization decisions

1. **Domain and Architecture become separate Roles.**  
   The frozen source sometimes combines them. Their canonical fact scopes differ under UPOS-01, so contracts are separate while compatible composition remains possible.

2. **Agent Definition lifecycle is separated from runtime availability.**  
   `DISABLED` is preserved as an instance/configuration operational concept; Agent Definition lifecycle uses `DRAFT → REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`.

3. **Human Governance vs Permission Policy is separated.**  
   Module 02 owns the constitutional human organizational role/override semantics. UPOS-10 owns concrete approvals, protected actions, permission enforcement and non-overridable controls.

4. **Veto ownership is split by semantics.**  
   Module 02 defines organizational veto contract; the specialist module defines the substantive rule/evidence criteria.

5. **Orchestrator authority is explicitly non-universal.**  
   Coordination is not fact ownership.

6. **Agent output receives an epistemic boundary.**  
   Canonical promotion is upstream Knowledge Lifecycle, not Agent Organization.

7. **One Agent Definition implements one Role.**  
   A base model/Agent Instance may bind multiple compatible Agent Definitions, each implementing exactly one canonical Role; each Run selects exactly one Role + Agent Definition identity. This keeps authority, review independence and future observability unambiguous.

## 4. Source preservation rule

Every top-level frozen-source section is classified in `SOURCE_SECTION_DISPOSITION.md`.

Every Module-02-owned extracted requirement is mapped in `../MODULE_02_TRACEABILITY.md`.

No downstream-owned section is copied merely for completeness.
