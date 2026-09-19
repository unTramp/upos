# Learning Outcome Standard

**ID:** UPOS-09-LOS-001  
**Type:** LEARNING OUTCOME STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/LEARNING_OUTCOME_TEMPLATE.md



## 1. Identity

Every Learning Outcome has stable:

```text
learning_outcome_id
```

## 2. Contract

```text
learning_outcome_id
improvement_proposal_ref
validation_plan_ref

changed_artifact_ref
changed_artifact_version

baseline_refs
comparison_refs
measurement_or_observation_refs

expected_effect
observed_effect

speed_effect
quality_effect
cost_effect
human_attention_effect
governance_effect
security_or_other_owner_effect_refs

confounders_observed
confidence
limitations

outcome
assessed_by_ref
assessed_at

related_prior_outcome_ref
supersedes
replacement
```

## 3. Outcome states

```text
IMPROVED
DEGRADED
NO_MEANINGFUL_CHANGE
INCONCLUSIVE
MIXED_TRADEOFF
```

## 4. Multi-dimensional improvement

No single dimension automatically dominates.

```text
faster != necessarily better
cheaper != necessarily better
less human attention != necessarily better
```

An improvement in one dimension with material regression in another is `MIXED_TRADEOFF` or `DEGRADED` according to the declared validation/guardrail semantics.

## 5. Causal caution

A favorable observed effect does not prove the proposed change caused it.

Outcome MUST preserve:

```text
comparison basis
confounders
confidence/uncertainty
limitations
```

## 6. Regression loop

A `DEGRADED` or `MIXED_TRADEOFF` Outcome MAY become evidence for a new Learning Candidate/Proposal.

It MUST NOT trigger automatic rollback/mutation; owner Workflow/Governance decides the action.

## 7. Challenge old rules

An established rule may itself become a learning target if later evidence shows cost without measurable benefit.

UPOS-009 proposes change; the canonical owner decides supersession.
