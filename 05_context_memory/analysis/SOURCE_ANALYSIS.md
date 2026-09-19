# UPOS-005 Source Analysis

**ID:** UPOS-05-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** ../MODULE_05_TRACEABILITY.md

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Inputs and authority

| Input | Role in Module 05 |
|---|---|
| UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle | ACTIVE upstream governance; owns truth/canonicality/provenance/promotion |
| UPOS-002 Agent Organization v1.0 | frozen upstream organizational contract |
| UPOS-003 Skills System v1.0 | frozen upstream Skill Context interface |
| UPOS-004 Workflow Engine v1.0 | frozen upstream Task/Workflow/Stage identity/orchestration |
| Universal AI Agent Operating Model v1.0 | FROZEN MASTER DESIGN INPUT only |
| UPOS-005 implementation directive | Module-05 design/acceptance directive |

Hashes:

```text
Frozen master: f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699
UPOS-01 Source-of-Truth: 06913d3ba3585f2dd8676f2edc2ad82b43fad548b91e5fb57bec18a7c975bafd
UPOS-01 Knowledge Lifecycle: 5e1a7653f22c218820b2c675f6f34bcf6bef5ad139bb0ce1639acae14cc2d885
Directive: addcc8990f2a1480303605286494d8c80c1b2267ae5c5e7f7838ffd4661c4571
```

## Frozen master directly relevant sections

Strong direct semantics were found in:

- §31 Context assembly;
- §32 Context assembly order;
- §33 Context budget principle;
- §34 Memory model;
- §35 Project memory sources;
- §74 Handoff context minimization;
- §187 Sensitive context policy;
- §190 Reproducibility;
- §208 Reviewer context independence;
- §209 QA context independence;
- §210 Merge Controller context;
- §211 Product Owner context;
- §212 Decision packet;
- anti-pattern §221.4 Giant context dump;
- anti-pattern §221.6 Hidden project memory.

Mixed semantics also appear in Source-of-Truth principles, Agent/Skill/Workflow required sources, learning-vs-memory, secret handling, auditability, missing/stale truth, run lifecycle, evidence hierarchy, artifact retention, and privacy of reasoning.

## Upstream requirements extracted

From UPOS-01:

```text
resolve exact fact scope
→ canonical owner
→ ACTIVE normative sources
→ accepted decisions
→ local refinements
→ version/baseline applicability
→ implementation evidence
→ conflict/UNKNOWN rather than invention
```

From Knowledge Lifecycle:

```text
raw conversation history != project memory
project memory should primarily be governed project knowledge
promotion is explicit
freshness != validity
historical knowledge remains labeled
epistemic/provenance classes must be preserved
```

## P0 governance conflict result

No P0 conflict was found with frozen UPOS-01–04.

The directive is compatible with upstream contracts when Module 05 is implemented as an execution-context layer, not a truth store.
