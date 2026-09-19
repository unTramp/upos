# Learning Provenance Standard

**ID:** UPOS-09-LPR-001  
**Type:** PROVENANCE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —



## 1. Required reconstructible chain

For material learning, future audit SHOULD reconstruct:

```text
Observation / Signal refs
↓
Evidence refs
↓
Pattern Candidate
↓
Learning Candidate
↓
Root Cause Assessment
↓
Improvement Proposal
↓
Validation Plan
↓
canonical owner resolution
↓
external owner Decision/change
↓
new artifact version
↓
Learning Outcome
```

Not every Candidate needs every link, but missing links MUST be explicit rather than fabricated.

## 2. Identity reuse

UPOS-009 consumes upstream identities unchanged.

Examples:

```text
task_id
workflow_instance_id
stage_id
agent_run_id
skill_id/version
skill invocation/result refs
context_bundle_id
engineering_change_id
repository_change_unit_id
quality_assessment_id
quality_gate_result_id
finding_id
human decision refs
future UPOS-008 observation refs
```

## 3. Version provenance

Proposal/Outcome records MUST identify the target/baseline/changed versions sufficiently to avoid comparing ambiguous `latest/current` states.

## 4. No hidden provenance

Free-text statements such as:

```text
"the workflow seems bad"
"the agent learned this"
"we improved quality"
```

are not sufficient material provenance.

## 5. Supersession

Candidate, Proposal, Validation Plan, Root Cause Assessment and Outcome records preserve:

```text
supersedes
replacement
```

or equivalent explicit relationship when applicable.

Historical records remain attributable.
