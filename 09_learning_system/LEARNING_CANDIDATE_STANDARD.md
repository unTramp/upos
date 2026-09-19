# Learning Candidate Standard

**ID:** UPOS-09-LCS-001  
**Type:** LEARNING CANDIDATE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/LEARNING_CANDIDATE_TEMPLATE.md



## 1. Identity

Every Learning Candidate has stable:

```text
learning_candidate_id
```

## 2. Contract

```text
learning_candidate_id
title
summary
status
scope

signal_refs
evidence_refs
pattern_candidate_ref
affected_modules
suspected_canonical_owner_ref

root_cause_assessment_refs

impact_dimensions
risk_refs
frequency_summary
cost_effect
quality_effect
time_effect
human_attention_effect
governance_effect

known_uncertainty
candidate_recommendation

priority_dimensions
priority_rationale

created_by_ref
created_at

duplicate_of
related_candidate_refs
consolidated_into
supersedes
replacement
```

Non-applicable fields use explicit `N/A` / `none`.

## 3. Candidate lifecycle

```text
OPEN
→ TRIAGED
→ INVESTIGATING
→ VALIDATED
→ PROMOTED_TO_PROPOSAL

Alternative:
OPEN / TRIAGED / INVESTIGATING
→ REJECTED
→ DUPLICATE
→ CONSOLIDATED
→ SUPERSEDED
```

`PROMOTED_TO_PROPOSAL` means only that a Module-09 Improvement Proposal exists. It is not UPOS-01 canonical promotion.

## 4. Candidate validation

`VALIDATED` means the reusable learning claim is supported enough for proposal formation under the applicable learning policy.

It does not mean root cause certainty, owner acceptance, canonical knowledge or approved system change.

## 5. Deduplication / consolidation

Module 09 MUST support:

```text
duplicate_of
related_candidate_refs
consolidated_into
```

Consolidation preserves all source/evidence provenance. Original candidate identities remain historically addressable.

## 6. Rejected candidates

Rejected candidates remain durable historical records with:

```text
rejection_reason
decision_or_assessment_refs
reconsideration_trigger
```

New evidence MAY justify a new/superseding candidate or explicit re-open according to policy; do not repeatedly rediscover the same rejected claim without new material evidence.

## 7. Priority semantics

Priority is explainable and multi-dimensional.

Candidate priority MAY consider:

```text
severity supplied by owner
frequency
quality impact
cost impact
human attention
governance risk
affected population
confidence/uncertainty
estimated effort
```

No universal weighted score is canonical in v1.
