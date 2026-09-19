# Root Cause Analysis Standard

**ID:** UPOS-09-RCA-001  
**Type:** ROOT CAUSE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/ROOT_CAUSE_ASSESSMENT_TEMPLATE.md



## 1. Core invariant

```text
CORRELATION != ROOT CAUSE
```

Version correlation, metric movement or temporal sequence alone does not prove causation.

## 2. Root Cause Assessment identity

Every independently reviewable Root Cause Assessment has stable:

```text
root_cause_assessment_id
```

## 3. Assessment contract

```text
root_cause_assessment_id
learning_candidate_ref
status
affected_scope

hypotheses:
  - statement
    root_cause_class
    supporting_evidence_refs
    contradicting_evidence_refs
    alternative_explanations
    confidence
    uncertainty
    proposed_validation_method

leading_hypothesis
unresolved_questions
confounders
assessment_method
assessor_refs
assessed_at
limitations

related_prior_assessment_ref
supersedes
replacement
```

## 4. Confidence

Default explainable confidence:

```text
LOW
MEDIUM
HIGH
UNRESOLVED
```

Numerical confidence MAY be used only when the method gives statistically meaningful semantics.

## 5. Root cause classes

Extensible v1 taxonomy:

```text
SKILL_GAP
WORKFLOW_GAP
CONTEXT_GAP
QUALITY_GAP
ENGINEERING_GOVERNANCE_GAP
DOCUMENTATION_GAP
AUTHORITY_OR_ORG_GAP
OBSERVABILITY_GAP
SECURITY_OR_PERMISSION_GAP
PROJECT_BINDING_GAP
TOOL_OR_PROVIDER_LIMITATION
MULTI_FACTOR
UNKNOWN
```

These classes route analysis; they do not transfer ownership of the underlying semantics.

## 6. Completion states

```text
OPEN
ASSESSING
COMPLETED
INCONCLUSIVE
SUPERSEDED
```

`COMPLETED` does not require one certain root cause. A completed assessment may explicitly conclude multiple interacting causes or bounded uncertainty.

## 7. Causal discipline

Assessment MUST record material alternative explanations and confounders.

Examples:

```text
Change Class mix changed
project/cohort changed
model/provider changed
sample size changed
Quality policy changed
human involvement changed
context policy changed
external incident/seasonality changed
```
