# Learning Operating Model

**ID:** UPOS-09-LOM-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** LEARNING_ONTOLOGY.md, PROMOTION_INTERFACE.md



## 1. Definition

Organizational learning in U-POS is a governed process that converts attributable execution observations into reusable improvement proposals and measured post-change outcomes.

It is not latent model adaptation, private provider memory, automatic prompt mutation or autonomous policy rewriting.

## 2. Learning flow

```text
Signal intake
→ Evidence qualification
→ Pattern analysis
→ Learning Candidate
→ Root Cause Assessment
→ Improvement Opportunity
→ Improvement Proposal
→ Validation Plan
→ canonical-owner resolution
→ external owner change/review/promotion process
→ changed artifact/version
→ Learning Outcome
→ continue / challenge / supersede / propose again
```

The flow MAY stop safely at any stage.

## 3. Anti-self-modification invariant

UPOS-009 MUST NOT directly rewrite:

```text
UPOS-009 itself
Agent Definitions
Skills
Workflows
Context policy
Engineering standards
Quality rules
Security rules
Project Adapter bindings
canonical project knowledge
```

based solely on a Signal, Pattern, Candidate, metric movement, AI analysis or Learning Outcome.

All material change routes to the current canonical owner.

## 4. UPOS-01 relationship

UPOS-009 specializes learning analysis but consumes the UPOS-01 Knowledge Lifecycle:

```text
SIGNAL
→ OBSERVATION
→ EVIDENCE
→ INTERPRETATION / HYPOTHESIS
→ PROPOSAL
→ REVIEW / VALIDATION
→ DECISION
→ CANONICAL PROMOTION
→ ACTIVE KNOWLEDGE
→ MONITORING
→ SUPERSESSION / RETIREMENT
```

UPOS-009 does not create a parallel canonicality/promotion engine.

A validated Learning Candidate remains noncanonical until UPOS-01/owning-module governance changes the authoritative artifact.

## 5. Proportionality

There is no universal Learning Gate after every Task.

Learning intake/analysis MAY be triggered by policy, owner request, high-severity events, repeated observations, scheduled review or Observability signal.

The rigor of evidence/root-cause/validation MUST be proportional to:

```text
impact
risk
irreversibility
frequency
affected population
governance significance
security significance supplied by owner
cost / human attention
uncertainty
```

## 6. Fail-safe behavior

When evidence, owner, root cause or validation is unresolved:

```text
do not self-modify
do not silently promote
preserve provenance
mark limitation/failure state
route/escalate to owner/workflow
```

## 7. Success includes learning from success

The Learning System treats both failure and successful repeated behavior as learnable signals, while preserving the same evidence and causal-discipline requirements.

## 8. No metric gaming

A proposed improvement MUST NOT optimize one dimension by silently degrading another.

At minimum evaluate where applicable:

```text
SPEED
QUALITY
COST
HUMAN_ATTENTION
GOVERNANCE
```

Security/privacy/risk effects are consumed from their owners and may add blocking constraints.
