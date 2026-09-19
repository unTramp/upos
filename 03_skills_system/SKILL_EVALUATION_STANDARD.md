# Skill Evaluation Standard

**ID:** UPOS-03-EVAL-001  
**Type:** EVALUATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Principle

A Skill is not successful because the invoking agent says it was successful.

Evaluation MUST be based on observable contract-level criteria.

## 2. Evaluation dimensions

At minimum consider:

1. contract conformance;
2. output correctness;
3. procedure adherence where procedure is normative;
4. quality criteria;
5. failure handling;
6. scope adherence;
7. downstream acceptance where relevant.

## 3. Contract conformance

Check:

- required inputs existed;
- preconditions were satisfied or escalated;
- required result class produced;
- prohibited behavior avoided;
- required source/context interfaces were respected.

## 4. Output correctness

Correctness is evaluated against the Skill's own semantic output contract and externally owned project contracts as referenced.

## 5. Procedure adherence

Only procedure steps owned by the Skill are evaluated here.

Workflow sequencing is outside this standard.

## 6. Failure handling

A conforming Skill MAY return a controlled failure/escalation instead of a nominal output.

Fabricating a result when required truth or capability is missing is evaluation failure.

## 7. No meaningless universal score

Do not reduce Skill quality to a universal `87/100`.

Prefer factual signals such as:

```text
required fields complete
preconditions respected
output schema/contract valid
blocking ambiguity escalated
tests/evidence references present when contract requires them
downstream consumer accepted/rejected
```

## 8. Cross-module boundary

- evidence semantics/gates/verdicts → UPOS-007;
- metric collection/trends/cost → UPOS-008;
- learning detection/promotion → UPOS-009;
- Module 03 defines what successful execution of the Skill Contract means.
