# UPOS-007 Source Analysis

**ID:** UPOS-07-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-007 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 07 artifacts.  
**Related:** ../MODULE_07_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-007 v1.0 decomposition/implementation/audit state at freeze time. It is not timeless normative truth. Current Quality semantics are owned by canonical Module 07 normative artifacts; `MODULE_07_TRACEABILITY.md` remains the canonical coverage artifact.


## Inputs and authority

| Input | Role |
|---|---|
| UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle | frozen upstream truth/criteria authority |
| UPOS-002 Agent Organization v1.0 | frozen Role/authority/SoD contract |
| UPOS-003 Skills System v1.0 | frozen verification Skill interfaces |
| UPOS-004 Workflow Engine v1.0 | frozen gate placement/rework orchestration |
| UPOS-005 Context & Memory v1.0 | frozen Reviewer/QA Context/provenance |
| UPOS-006 Engineering Governance v1.0 | frozen exact engineering target/check/mechanical mergeability |
| Universal AI Agent Operating Model v1.0 | FROZEN MASTER DESIGN INPUT |
| UPOS-007 implementation directive | Module-07 design/acceptance directive |

Local source hashes:

```text
Frozen master: f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699
UPOS-01 docs bundle: 0eed3f1319103b9fef7956519da9754986b7c512a05278c030c38edbaddcb3a1
UPOS-01 Source-of-Truth: 06913d3ba3585f2dd8676f2edc2ad82b43fad548b91e5fb57bec18a7c975bafd
UPOS-01 Knowledge Lifecycle: 5e1a7653f22c218820b2c675f6f34bcf6bef5ad139bb0ce1639acae14cc2d885
UPOS-005 frozen: 73d2353ece6d2bb3af7409f1db91a120a201d2df96972bb1433499440737c7c2
UPOS-006 frozen: 51211b5444ed5345255a848871040daaff0edc7998dd561e5ca81f4a45bfcefa
Directive: b34250c71c679cb73a0dd11d86a975ef962de1e69bb1ba57761ab45e390bfa3e
```

## Frozen master Quality-owned semantics

Strong Quality semantics exist in:

- evidence-before-approval;
- self-check vs independent verification;
- review protocol/findings/output/independence;
- QA protocol/dimensions;
- documentation/architecture/security/database gate examples;
- merge readiness semantics;
- DoR/DoD;
- review/QA/readiness output templates;
- review freshness;
- CI as evidence provider;
- test/snapshot/scanner/linter integrity;
- reproducibility;
- Reviewer/QA Context independence;
- evidence hierarchy/change evidence bundle;
- artifact retention/privacy of reasoning;
- fake-review anti-pattern.

## P0 conflict result

No P0 conflict found with frozen UPOS-01–06.

The directive is implementable if Module 07 is strictly an evaluation/evidence system:

```text
truth remains UPOS-01
authority remains UPOS-002
procedure remains UPOS-003
orchestration remains UPOS-004
Context remains UPOS-005
engineering mechanics remain UPOS-006
```

## Key reconciliation decisions

1. `ReviewResult` and `QAResult` normalize to `QualityAssessment + assessment_type`; no duplicate IDs.
2. Criterion identity uses upstream `criterion_ref` plus set-local `criterion_key`; no duplicate global requirement database.
3. Adopt `Quality Policy`, not `Quality Profile`.
4. Security substantive review/veto stays UPOS-010; Quality consumes external Security results.
5. CI/check success is Evidence, never a Verdict.
6. Completed Assessments are immutable snapshots; re-review creates a new Assessment.
