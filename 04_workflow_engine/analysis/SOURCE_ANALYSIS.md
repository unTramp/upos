# UPOS-004 Source Analysis

**ID:** UPOS-04-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-004 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 04 artifacts.  
**Related:** ../MODULE_04_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-004 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current Workflow semantics are owned by canonical Module 04 normative artifacts; `MODULE_04_TRACEABILITY.md` remains the canonical coverage artifact.


## Sources

- UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle — active upstream governance.
- UPOS-002 Agent Organization v1.0 — frozen organizational contract.
- UPOS-003 Skills System v1.0 — frozen Skill contract/library.
- `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.md` — frozen master design input.
- UPOS-004 implementation directive — task refinement.

## Direct Workflow-owned frozen sections

Architecture traceability assigns 46 structural units to Module 04, including:

- §3.11;
- §22–30;
- §79–80;
- §85–98;
- §122;
- §129;
- §136;
- §146;
- §185;
- §194;
- §196;
- §199;
- §202–205;
- §207;
- §221.3;
- Appendix D/J/O/P/Q;
- Final Principle 4.

## Main normalization

Frozen source models UI/DS/Architecture/API/DB/Security as named workflows.

Source analysis shows they are orthogonal concerns and can coexist.

Decision:

```text
Base Work Type Workflow
+
Concern Profiles
+
Change Class
=
Resolved Workflow Configuration
```

This preserves source intent while avoiding combinatorial explosion.

## Critical retained invariants

- risk determines process depth;
- risk != diff size;
- no every-agent swarm;
- no infinite retry;
- material scope/risk discovery triggers reclassification;
- parallelize only independent nodes;
- shared contract first;
- Workflow status != product feature lifecycle;
- explicit legal state transitions;
- Implementer != Final Reviewer;
- high-risk Implementer != Reviewer != Merge Controller.
