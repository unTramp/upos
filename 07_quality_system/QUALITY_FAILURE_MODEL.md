# Quality Failure Model

**ID:** UPOS-07-QFM-001  
**Type:** QUALITY FAILURE / CONDITION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Boundary

Quality failure conditions explain why an Assessment/Gate cannot support the desired Quality result.

UPOS-004 owns orchestration response.

UPOS-007 MUST NOT define retry/rework/rerouting transitions here.

## 2. Taxonomy

| Condition | Quality meaning | Typical Assessment/Gate implication | External owner/interface |
|---|---|---|---|
| `CRITERIA_UNRESOLVED` | mandatory criterion meaning/applicability cannot be authoritatively resolved | BLOCKED or INCONCLUSIVE; never PASS | UPOS-01 |
| `REQUIRED_EVIDENCE_MISSING` | required evidence class/item is absent | BLOCKED if unobtainable prerequisite; otherwise no PASS | UPOS-003/006/011 as source |
| `EVIDENCE_INSUFFICIENT` | evidence exists but cannot support required conclusion | INCONCLUSIVE | UPOS-007 |
| `EVIDENCE_STALE` | previously applicable evidence is not current for target/assumptions | INCONCLUSIVE/BLOCKED until revalidated | UPOS-005/006 signals |
| `TARGET_CHANGED` | exact artifact state differs from evaluated state | previous result not valid for new target without revalidation | UPOS-006 |
| `BLOCKING_FINDING_OPEN` | unresolved blocking Quality finding applies | FAIL / Gate NOT_SATISFIED absent valid exception | UPOS-007 |
| `ACCEPTANCE_CRITERION_UNSATISFIED` | applicable required acceptance criterion is demonstrably unmet | FAIL | UPOS-01 criterion meaning |
| `ASSESSMENT_INCOMPLETE` | required evaluation work not completed | no PASS; BLOCKED/INCONCLUSIVE by cause | UPOS-007/004 |
| `INDEPENDENCE_VIOLATION` | required independent evidence was produced by prohibited relationship | evidence invalid for independence; BLOCKED/INCONCLUSIVE | UPOS-002 |
| `PROVENANCE_INSUFFICIENT` | evidence/target/producer cannot be attributed adequately | INCONCLUSIVE/BLOCKED | UPOS-005/006/007 |
| `EXCEPTION_INVALID` | relied-upon waiver is expired/revoked/out-of-scope/unverifiable | affected issue treated as unwaived | UPOS-002/010/Human Governance |
| `EXTERNAL_GATE_UNRESOLVED` | required external Security/Human/permission result unavailable | BLOCKED | UPOS-010/002 |

## 3. Unknown

When evidence cannot support a conclusion:

```text
INCONCLUSIVE
```

is preferred to fabricated confidence.

## 4. Missing required evidence

Required evidence MUST NOT be silently downgraded to optional because it is inconvenient/unavailable.

## 5. Security boundary

`SECURITY_RESULT_REFERENCE` or external Security gate may be unresolved.

Generic Quality PASS MUST NOT override Security veto/approval requirements.

## 6. Workflow boundary

UPOS-007 returns a Quality condition/verdict/gate result.

UPOS-004 decides whether to rework, pause, escalate, reroute, cancel, or continue.
