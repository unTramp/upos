# Failure, Retry and Recovery

**ID:** UPOS-04-FRR-001  
**Type:** FAILURE / RECOVERY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** RECLASSIFICATION_AND_REROUTING.md, WORKFLOW_STATE_MODEL.md

## 1. Concept separation

UPOS-004 distinguishes:

```text
RETRY
= repeat the same bounded operation/stage after a transient or repeatable failure
  without semantic rejection of the produced result

REWORK
= return to the producer stage because the produced output was rejected,
  insufficient, or non-conformant

RECOVERY
= controlled alternate orchestration path after failure

RECLASSIFICATION
= reassessment of impact/risk because material facts changed

REROUTING
= creation/resolution of a changed Workflow configuration

ESCALATION
= transition to different/higher authority because current delegated
  authority/routing cannot resolve the condition
```

Invariant:

```text
RETRY
!= REWORK
!= RECOVERY
!= RECLASSIFICATION
!= REROUTING
!= ESCALATION
```

## 2. Universal non-convergence invariant

```text
No infinite retry loops.
No infinite rework loops.
```

Retry and rework MUST both be bounded before autonomous/reference execution relies on them.

The exact numeric threshold MAY be supplied by:

```text
Workflow policy
Project policy
UPOS-011 binding
```

Threshold exhaustion MUST cause a controlled transition appropriate to the cause, such as:

```text
ESCALATE
REPLAN
RECLASSIFY
REROUTE
REQUEST_OWNER_DECISION
CANCEL
FAIL
```

Frozen-source examples such as `2 failed implementation attempts` or `3 review rejection cycles` remain illustrative and are not universal mandatory thresholds.

## 3. Workflow failure taxonomy

This taxonomy classifies orchestration response. It does not take substantive ownership from Security, Quality, Permissions, Source-of-Truth, or provider adapters.

| Failure class | Workflow meaning | Permitted orchestration responses |
|---|---|---|
| `TRANSIENT_EXECUTION_FAILURE` | Same bounded operation may succeed later without semantic change | retry; block; escalate/fail when retry budget is exhausted |
| `CONTRACT_FAILURE` | Produced/required artifact is non-conformant with an applicable contract | rework; replan; block; escalate; fail |
| `MISSING_REQUIRED_TRUTH` | Required canonical/source truth cannot be resolved | block; escalate; request owner decision; cancel/fail if unresolved |
| `CANONICAL_CONFLICT` | Active authoritative sources conflict | block; escalate; request owner decision; replan after resolution |
| `AUTHORITY_CONFLICT` | Current route/Role cannot resolve required authority | block; escalate; reroute/reassign through external authority rules; cancel |
| `SCOPE_EXPANSION` | Required work exceeds classified/routed scope | replan; reclassify; reroute; split task; cancel |
| `RISK_DISCOVERY` | New facts materially change impact/risk | pause/block; reclassify; reroute; escalate |
| `GATE_REJECTION` | An externally owned gate rejects/does not accept an artifact/result | rework; replan; block; escalate; fail according to external gate semantics |
| `SECURITY_VETO` | UPOS-010/Security authority reports a blocking veto | block; escalate; cancel/fail; rework only when the external remediation contract permits it |
| `HUMAN_DECISION_REQUIRED` | Current route requires a human/owner decision | pause/block; escalate; request owner decision; cancel |
| `DEPENDENCY_FAILURE` | Required upstream stage/service/artifact/dependency is unavailable or failed | retry if transient; block; replan; reroute; fail |
| `PERSISTENT_TOOL_PROVIDER_FAILURE` | Tool/provider failure persists beyond retry budget | block; replan; reroute through a valid external adapter/policy; escalate; fail |
| `NON_CONVERGENT_REWORK` | Repeated rework does not converge within declared bound | escalate; replan; reclassify; reroute; request owner decision; cancel/fail |

### Ownership boundary

- `GATE_REJECTION` does not define Quality PASS/FAIL; UPOS-007 owns that.
- `SECURITY_VETO` does not define Security veto substance; UPOS-010 owns that.
- `AUTHORITY_CONFLICT` does not redefine Role authority; UPOS-002 owns that.
- `MISSING_REQUIRED_TRUTH` / `CANONICAL_CONFLICT` do not redefine canonicality; UPOS-01/05 own source resolution.
- provider/tool semantics remain UPOS-011/runtime adapters.

## 4. Retry

Retry is appropriate only when the same bounded operation remains semantically valid, the failure is transient/repeatable, required truth/authority/policy did not change, and retry budget remains.

Do not retry unchanged for canonical conflict, authority conflict, scope expansion, changed risk, persistent gate rejection, or exhausted provider/tool failure.

## 5. Rework

Rework returns responsibility to the producer stage because an output is rejected, insufficient, or non-conformant.

A rework loop MUST:

- identify the producer stage/result being corrected;
- preserve independent Reviewer/QA roles where required;
- consume the externally owned finding/rejection without redefining it;
- have an explicit bounded rework policy;
- transition to controlled escalation/replan/reclassification/rerouting/owner decision/cancel/fail when the bound is exhausted.

Rework MUST NOT silently become an infinite review-fix-review cycle.

## 6. Recovery

Recovery is a controlled alternate orchestration path after failure.

Recovery may include replan, reassign/reroute, split task, rollback request/reference, pause/block, human/owner escalation, cancel, or fail.

Recovery MUST preserve Role authority, SoD, source validity, stronger Change-Class requirements, and external approval/gate constraints.

## 7. Reclassification / rerouting relationship

Reclassification is used when impact/risk facts changed.

Rerouting is used when the resolved Workflow configuration must change.

They are governed by `RECLASSIFICATION_AND_REROUTING.md`.

Retry or rework MUST NOT be used to avoid required reclassification/rerouting.

## 8. Rollback

UPOS-004 may require a rollback/recovery strategy reference at C3+ and especially C4/C5.

Actual Git/data/deployment rollback mechanics remain external.

## 9. Terminal failure

A Workflow may terminate `FAILED` when safe controlled recovery is unavailable, exhausted, explicitly rejected, or no longer justified.

Failure does not silently canonize partial outputs.
