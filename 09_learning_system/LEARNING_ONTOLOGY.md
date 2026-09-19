# Learning Ontology

**ID:** UPOS-09-LON-001  
**Type:** ONTOLOGY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Learning Signal

One potentially relevant observed indication supplied by a person, project artifact, Quality result, execution system or Observability source.

A Signal is not independently assigned a Module-09 global ID in v1. It is identified by its upstream/source reference plus intake context.

## 2. Learning Evidence

Attributable material used to support or contradict a learning claim.

Examples include upstream event/trace/metric references, Findings, Quality Assessments, Workflow/engineering/context refs, Skill result/invocation refs and human decisions.

```text
Learning Evidence != canonical truth
```

## 3. Learning Evidence Set

A bounded collection of evidence refs plus selection scope, evidence role and limitations used by one Pattern/Candidate/Root Cause/Proposal/Outcome analysis.

It is embedded in the consuming record; no `learning_evidence_set_id` exists in v1.

## 4. Pattern Candidate

A suspected repeated, structured or significant behavior requiring evaluation.

Stable identity:

```text
pattern_candidate_id
```

## 5. Confirmed Pattern

A Pattern Candidate whose evidence satisfies the applicable learning-policy confirmation conditions.

Confirmed Pattern is a state/assessment of the Pattern Candidate, not a separate entity/ID.

```text
CONFIRMED PATTERN != ROOT CAUSE
CONFIRMED PATTERN != POLICY
```

## 6. Learning Candidate

A governed candidate describing a potentially reusable lesson supported enough to merit investigation/owner routing.

Stable identity:

```text
learning_candidate_id
```

```text
LEARNING CANDIDATE != CANONICAL KNOWLEDGE
```

## 7. Root Cause Hypothesis

One proposed explanation for why the observed pattern/outcome occurs.

A Root Cause Hypothesis is embedded within a Root Cause Assessment.

## 8. Root Cause Assessment

An independently addressable bounded assessment comparing one or more hypotheses, alternatives, supporting/contradicting evidence and uncertainty.

Stable identity:

```text
root_cause_assessment_id
```

It may conclude a leading hypothesis, multiple plausible causes, or unresolved root cause.

## 9. Improvement Opportunity

A bounded location in a canonical system/artifact where an improvement may be possible.

It is embedded in a Candidate/Proposal and does not receive an independent v1 ID.

## 10. Improvement Proposal

A concrete noncanonical proposal to change a canonical-owner-controlled artifact.

Stable identity:

```text
improvement_proposal_id
```

```text
IMPROVEMENT PROPOSAL != APPROVED CHANGE
```

## 11. Validation Plan

A versioned/bounded specification for how expected effect will be evaluated before/after owner-controlled change.

Stable identity:

```text
validation_plan_id
```

## 12. Learning Outcome

An independently addressable post-change effect assessment comparing expected and observed effects with limitations/confounders.

Stable identity:

```text
learning_outcome_id
```

## 13. Promotion Recommendation

A Module-09 recommendation that a validated proposal is suitable to hand off to the canonical owner/change process.

It is not an approval, decision or canonical promotion and receives no separate global ID.

## 14. Learning Backlog

A governed projection/index of open Learning Candidates, Improvement Proposals, validation work and outcome follow-up.

It is not a new project Task backlog and does not own project prioritization.
