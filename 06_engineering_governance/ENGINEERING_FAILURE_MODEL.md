# Engineering Failure Model

**ID:** UPOS-06-EFM-001  
**Type:** ENGINEERING FAILURE TAXONOMY  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-006 Engineering Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 failure/reclassification interfaces


## 1. Purpose

Module 06 classifies repository-engineering failure conditions and reports engineering constraints/signals.

It does NOT own Workflow retry/rework/recovery sequencing.

## 2. Taxonomy

| Failure | Engineering meaning | Detectability | Module-06 response / Workflow signal |
|---|---|---|---|
| `WORKSPACE_CONTAMINATION` | writable workspace contains state outside assigned RCU/owner scope | workspace/diff inspection | block mutation; isolate/clean/transfer; signal Workflow |
| `WRONG_BASE` | RCU/branch/workspace began from or points to unintended base | revision comparison | block integration; correct base/update; signal if scope/risk changes |
| `BRANCH_SCOPE_VIOLATION` | branch contains unrelated Task/RCU work | provenance/diff analysis | split/clean or block; emit scope signal |
| `UNRELATED_CHANGE_DETECTED` | Commit/IR contains opportunistic unrelated change | diff/provenance analysis | remove/split; emit scope expansion signal |
| `COMMIT_NON_ATOMIC` | Commit combines separable unrelated logical intents | commit/diff analysis | split/reconstruct where practical; block readiness mechanics if policy requires |
| `UNRESOLVED_VCS_CONFLICT` | version-control conflict unresolved | VCS state | `CONFLICT_PRESENT`; block merge mechanics |
| `CONCURRENT_WRITE_COLLISION` | independent writers mutate conflicting/shared state unsafely | workspace ownership/collision analysis | serialize/isolate/coordinate; signal UPOS-004 |
| `STALE_BASE` | base materially advanced beyond engineering policy | base/head comparison | `REBASE_REQUIRED` or coordination required |
| `CHECK_ARTIFACT_MISMATCH` | check result points to older/different artifact than current candidate | artifact ref comparison | mark stale association; expose to UPOS-007 |
| `REVIEW_ARTIFACT_CHANGED` | reviewed base/head/commit set changed | artifact ref comparison | expose artifact-change signal; do not preserve validity claim |
| `INTEGRATION_REQUEST_SCOPE_DRIFT` | IR purpose/scope no longer matches contained changes | scope/provenance analysis | block/split/update route as governed |
| `MERGE_CONFLICT` | integration operation cannot apply cleanly | VCS/provider mechanics | `MECHANICALLY_BLOCKED`; return conflict signal |
| `PROVENANCE_INCOMPLETE` | required artifact relationship cannot be reconstructed | provenance validation | block high-value integration mechanic per policy; request missing refs |
| `HISTORY_REWRITE_DETECTED` | commit/head identity changed by rebase/amend/force update | revision/ref comparison | preserve old refs; expose stale review/check associations |
| `GENERATED_ARTIFACT_MISMATCH` | generated artifact/source/generator relation is inconsistent | artifact consistency check | block or flag; invoke project generator/quality interfaces |

## 3. Workflow boundary

For failures requiring:

```text
retry
rework
replan
reclassification
rerouting
escalation
cancellation
```

Module 06 emits the condition; UPOS-004 owns orchestration.

## 4. Quality/Security boundary

Module 06 MUST NOT reinterpret external findings/vetoes.

It only binds their references to repository artifacts and exposes artifact changes.

## 5. Non-convergence

Repeated engineering conflicts or scope drift may be reported as evidence to Workflow/Learning systems.

Module 06 does not create its own infinite repair loop.
