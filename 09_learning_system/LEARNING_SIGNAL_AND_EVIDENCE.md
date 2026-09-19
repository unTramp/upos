# Learning Signal and Evidence Standard

**ID:** UPOS-09-LSE-001  
**Type:** SIGNAL / EVIDENCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Signal sources

Signals MAY originate from:

```text
repeated Workflow failure / retry / rework
repeated or severe Quality Finding
escaped regression
Context failure
permission denial pattern
human intervention/escalation
high latency or cost
low first-pass acceptance
frequent waiver
revert/collision/merge-conflict pattern
successful repeated practice
unexpectedly strong result
owner-declared severe single event
```

Signal intake MUST preserve source identity/provenance; it MUST NOT convert source meaning.

## 2. Single-event significance

Repetition is not mandatory when an upstream owner classifies an event as sufficiently severe.

Examples may include catastrophic impact, major security incident, severe governance failure or critical escaped defect.

UPOS-009 consumes severity/significance from the authoritative owner; it does not invent Security/Quality severity.

## 3. Evidence provenance

Every material learning claim MUST reference attributable evidence.

Permitted reference classes include:

```text
UPOS-008 `event_id` / `trace_id` refs
UPOS-008 Metric Observation value records linked to `metric_definition_id`
UPOS-008 data completeness/coverage refs
quality_assessment_id
quality_gate_result_id
finding_id
workflow_instance_id
stage_id / transition_id
context_bundle_id
engineering_change_id
repository_change_unit_id
commit/integration/revision refs
agent_run_id
skill_id/version
skill invocation/result refs
human decision/approval refs
UPOS-010 permission_request_id / permission_decision_id
UPOS-010 grant_id / protected_action_id / security_exception_id where relevant
security_policy_ref/version and owner reason/result refs where relevant
canonical artifact/version refs
```

## 4. Learning Evidence Set contract

Each evidence set inside a consuming record SHOULD state:

```text
purpose / claim supported
population/scope
time window if applicable
included evidence refs
supporting evidence
contradicting evidence
selection method
known omissions
source freshness/applicability limitations
```

## 5. No hidden reasoning

Learning Evidence MUST NOT rely on hidden chain-of-thought.

Use attributable artifacts such as:

```text
explicit decisions
reason codes
user-visible rationale
result refs
measurements
Findings/Assessments
documented hypotheses/limitations
```

## 6. Provider/model memory boundary

Private model memory, latent model adaptation and provider personalization are not organizational evidence or learning unless an explicit attributable project-controlled artifact captures the relevant claim/evidence.

```text
MODEL MEMORY != ORGANIZATIONAL LEARNING
```

## 7. Evidence sufficiency

UPOS-009 defines learning-analysis sufficiency for Pattern/Candidate/Root Cause/Proposal/Outcome purposes.

It does not redefine UPOS-007 Quality Evidence sufficiency/Quality Verdicts.

Where Quality artifacts are consumed, their exact historical meaning remains UPOS-007-owned.
