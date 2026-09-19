# Pattern Detection Standard

**ID:** UPOS-09-PDS-001  
**Type:** PATTERN STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/PATTERN_CANDIDATE_TEMPLATE.md



## 1. Pattern Candidate identity

Every independently tracked Pattern Candidate has stable:

```text
pattern_candidate_id
```

## 2. Required contract

```text
pattern_candidate_id
title
status
pattern_statement

population
time_window
sample_size

signal_refs
evidence_refs
detection_method
confirmation_policy_ref

affected_scope
affected_versions
known_limitations
possible_confounders

created_by_ref
created_at

duplicate_of
related_pattern_refs
consolidated_into
supersedes
replacement
```

## 3. Detection methods

Allowed detection classes:

```text
RULE_BASED
STATISTICAL
HUMAN_RECOGNIZED
AI_ASSISTED
MIXED
```

The actual method and limitations MUST be explicit.

AI-assisted detection does not upgrade a Pattern Candidate to confirmed truth.

## 4. Repetition threshold

UPOS-009 MUST NOT hard-code a universal occurrence threshold.

Confirmation criteria MAY vary by governed policy based on:

```text
severity
Change Class
risk
frequency
quality impact
cost
human attention
affected population
project policy
```

## 5. Confirmation

A Pattern Candidate becomes `CONFIRMED` only when the evidence satisfies the applicable confirmation policy for the stated population/scope.

Confirmation means:

```text
sufficient evidence that the described pattern exists
```

It does not mean:

```text
root cause proven
policy should change
proposal approved
```

## 6. High-severity single event

A Pattern Candidate MAY be confirmed/significant from one event only when upstream authoritative severity/risk semantics justify it and the applicable learning policy allows single-event escalation.

## 7. Pattern lifecycle

```text
OPEN
→ INVESTIGATING
→ CONFIRMED
  or NOT_CONFIRMED

OPEN / INVESTIGATING / CONFIRMED
→ DUPLICATE / CONSOLIDATED / SUPERSEDED

terminal historical projection:
ARCHIVED
```

`CONFIRMED` is not canonical promotion.
