# Learning Entity Model Analysis

**ID:** UPOS-09-AN-004  
**Type:** ENTITY MODEL ANALYSIS  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-009 Implementation  
**Version:** 1.0.0-provisional.1  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## Adopted stable identities

```text
pattern_candidate_id
learning_candidate_id
root_cause_assessment_id
improvement_proposal_id
validation_plan_id
learning_outcome_id
```

## Rejected identity candidates

```text
learning_signal_id
learning_evidence_set_id
confirmed_pattern_id
root_cause_hypothesis_id
improvement_opportunity_id
promotion_recommendation_id
learning_backlog_item_id
```

Reason: they are source refs, embedded relations, states or projections without a sufficiently independent lifecycle in v1.

## Identity explosion test

An ID is adopted only when the object:
- is independently referenced across artifacts;
- has an independent lifecycle/version/history;
- needs durable audit/supersession;
- cannot be represented safely as a relation/state of another object.
