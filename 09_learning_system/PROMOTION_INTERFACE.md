# Promotion Interface

**ID:** UPOS-09-PRO-001  
**Type:** PROMOTION / OWNER-RESOLUTION INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-009 Learning System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-01 Knowledge Lifecycle



## 1. Fundamental boundary

```text
UPOS-009
= interpret evidence
+ form candidate
+ analyze cause
+ form proposal
+ validate proposal/outcome
+ recommend/rout to owner

UPOS-01 / canonical owner
= review
+ decide
+ promote/update canonical truth/artifact
+ supersede/retire authoritative versions
```

## 2. Owner-resolution algorithm

For every Improvement Proposal:

```text
1. identify behavior/artifact proposed for change;
2. identify fact/semantic scope;
3. resolve canonical owner/source through UPOS-01;
4. resolve owning U-POS module/project layer;
5. confirm target artifact/version;
6. detect conflicts/unknown owner;
7. if unresolved → CANONICAL_OWNER_UNRESOLVED;
8. if resolved → hand off Proposal + evidence + validation plan;
9. owner invokes its governed change/review process;
10. record external decision/change/version refs;
11. later assess Learning Outcome.
```

## 3. Improvement routing

Default universal routing:

```text
Agent organization/contract → UPOS-002
Skill → UPOS-003
Workflow/routing/profile → UPOS-004
Context/Memory policy → UPOS-005
Engineering Governance → UPOS-006
Quality policy/criterion/gate → UPOS-007
Observability definition → UPOS-008
Learning System itself → UPOS-009 through governed version change
Security/permission → UPOS-010
project/provider binding → UPOS-011
project truth/documentation → UPOS-01/project canonical owner
```

## 4. Promotion recommendation contract

A recommendation includes:

```text
proposal_ref
recommendation
basis_refs
known_limitations
canonical_owner_ref
required external review/authority refs
recommended next action
generated_at
```

Recommendation values:

```text
READY_FOR_OWNER_REVIEW
NOT_READY
BLOCKED
INCONCLUSIVE
```

## 5. No direct mutation

A `READY_FOR_OWNER_REVIEW` recommendation does not authorize an edit/merge/promotion.

Authorization remains with owning governance and UPOS-002/010/Human Governance where applicable.

## 6. UPOS-01 knowledge promotion

If an accepted owner change represents durable project knowledge:

```text
proposal
→ owner decision
→ canonical update/new version
→ provenance links
→ source Candidate/Proposal state update
→ monitoring
```

UPOS-009 may link this chain but does not substitute for it.
