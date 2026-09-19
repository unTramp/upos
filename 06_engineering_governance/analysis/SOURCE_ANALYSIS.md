# UPOS-006 Source Analysis

**ID:** UPOS-06-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** —

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Sources and authority

1. UPOS-01 Documentation System / Source-of-Truth / Knowledge Lifecycle — ACTIVE upstream governance.
2. UPOS-002 Agent Organization v1.0 — FROZEN organizational authority/SoD.
3. UPOS-003 Skills System v1.0 — FROZEN Skill contracts and engineering `INTERFACE_SKILL` references.
4. UPOS-004 Workflow Engine v1.0 — FROZEN Task/Workflow/Stage/routing/rework semantics and stable IDs.
5. UPOS-005 Context & Memory — IN DEVELOPMENT; noncanonical design signal only.
6. `UNIVERSAL_AI_AGENT_OPERATING_MODEL_v1.0` — frozen master design input.
7. UPOS-006 implementation directive — Module-06 design/implementation authority for this branch.

## Main extraction result

Frozen master Engineering/Git/PR semantics are concentrated around:

```text
§3.7–3.10
§43–56
§57–59 (mixed)
§72
§81–84
§135–146 (mixed)
§154–164 (mixed)
§189–190
§197
§205–208 (mixed)
§218–220 (mixed)
§221.10
Appendix L
```

The Module-06 directive then materially refines these semantics with:

- Engineering Change / Repository Change Unit identities;
- provider-neutral Integration Request;
- Workspace isolation;
- multi-repository coordination;
- artifact staleness;
- mechanical mergeability boundary;
- Merge Operation identity;
- repository Revert/Backout;
- engineering provenance/failure taxonomy;
- provisional UPOS-005 reconciliation gate.

## P0 governance conflicts

None found against FROZEN UPOS-01–04.

## Critical boundaries confirmed

```text
Task / Workflow / rework orchestration → UPOS-004
Role / authority / Merge Controller    → UPOS-002
Skill procedure                         → UPOS-003
Context semantics                       → UPOS-005 pending
Quality verdicts/evidence sufficiency   → UPOS-007
Telemetry                               → UPOS-008
Permissions/protected actions           → UPOS-010
Provider/project wiring                 → UPOS-011
```

## Architecture decisions

1. Adopt `engineering_change_id`, `repository_change_unit_id`, `workspace_id`, `merge_operation_id`.
2. Do NOT create duplicate IDs for VCS/provider-native objects; use `branch_ref`, `commit_ref`, `integration_request_ref`, `revision_ref`, `check_ref`.
3. Use provider-neutral `Integration Request`; no hosting-provider ontology.
4. Preserve Git-like source-control assumption while keeping provider binding abstract.
5. Maintain small repository-mechanical lifecycles separate from Workflow/Quality states.
6. Treat Context references as placeholders only until FROZEN UPOS-005 reconciliation.
