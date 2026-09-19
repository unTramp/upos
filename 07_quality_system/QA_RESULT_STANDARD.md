# QA Result Standard

**ID:** UPOS-07-QAR-001  
**Type:** QA RESULT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** QUALITY_ASSESSMENT_STANDARD.md


## 1. QA Result representation

A QA Result is a `QualityAssessment` with:

```text
assessment_type = QA_VALIDATION
```

It has no separate `qa_result_id`.

## 2. QA focus

QA evaluates observable behavior/outcomes against expected governed criteria/scenarios.

As applicable:

```text
acceptance criteria
happy path
negative paths
boundary conditions
state transitions
error recovery
regression surface
permissions behavior by reference
responsive/accessibility behavior
backward compatibility
```

The relevant subset is determined by criteria/risk/policy.

## 3. QA Context independence

QA begins from expected behavior/contracts and risk, not producer narrative alone.

Context assembly remains UPOS-005.

## 4. Review != QA

```text
REVIEW
= inspect change/design/code/artifacts for conformance/quality

QA
= validate resulting behavior/outcomes against expected criteria/scenarios
```

They may overlap but are not automatically interchangeable.

## 5. Runtime evidence

Runtime/test evidence can support QA criteria but cannot prove architecture/documentation/security claims it does not cover.

## 6. Regression protection

For defect-fix Quality evaluation, when applicable and practical, evidence SHOULD establish:

```text
defect reproduced or otherwise demonstrated
+
fix behavior validated
+
regression protection exists
```

The exact Workflow sequence remains UPOS-004.

Test implementation procedure remains UPOS-003.

## 7. QA limitations

Flaky/unreliable environment/evidence must be explicitly qualified.

`PASS` is only allowed when required applicable QA criteria are sufficiently evidenced.
