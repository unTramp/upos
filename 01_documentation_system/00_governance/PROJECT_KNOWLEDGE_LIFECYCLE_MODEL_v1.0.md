# Project Knowledge Lifecycle Model v1.0

**ID:** DOC-GOV-KL-001  
**Type:** STANDARD / KNOWLEDGE GOVERNANCE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Changes to knowledge capture, evidence, validation, canonical promotion, learning, provenance, supersession, or AI memory policy  
**Supersedes:** —  
**Related:** DOC-STD-001, PROJECT_SOURCE_OF_TRUTH_MODEL_v1.0.md, Decision Records, Reports/Evidence, project manifests

---

## 0. Purpose

This standard defines how **project knowledge itself** moves through the organization.

It answers:

- where a new observation starts;
- what counts as evidence;
- how hypotheses differ from facts;
- when a finding becomes a decision;
- when a decision changes canonical truth;
- how learnings become reusable rules, tests, skills, or policies;
- how stale knowledge is challenged;
- how superseded knowledge remains traceable;
- how AI agents may consume and produce knowledge safely.

This is intentionally different from:

```text
Document lifecycle
Feature lifecycle
Design-system object lifecycle
Domain lifecycle
```

Those lifecycles describe artifacts or product objects.

This model describes the **epistemic lifecycle of knowledge**.

---

# 1. Why a Knowledge Lifecycle is needed

A project continuously produces information from:

```text
users
research
analytics
tests
incidents
code review
production behavior
experiments
support
AI agents
engineering work
design work
architecture work
```

Without a knowledge lifecycle, all of these can accidentally become equal-looking Markdown statements.

That creates dangerous ambiguity:

```text
one interview quote
looks like
a product requirement

one AI suggestion
looks like
an architecture decision

one runtime behavior
looks like
approved doctrine

one old learning
looks like
current truth
```

The Knowledge Lifecycle prevents this.

---

# 2. Core distinction: information is not automatically knowledge

Use this conceptual ladder:

```text
SIGNAL
↓
OBSERVATION
↓
EVIDENCE
↓
INTERPRETATION / HYPOTHESIS
↓
PROPOSAL
↓
REVIEW / VALIDATION
↓
DECISION
↓
CANONICAL PROMOTION
↓
ACTIVE KNOWLEDGE
↓
MONITORING / CHALLENGE
↓
SUPERSESSION / RETIREMENT
↓
HISTORICAL MEMORY
```

Not every signal should reach the top.

---

# 3. Knowledge classes

## 3.1 Signal

Raw indication that something may matter.

Examples:

```text
user complaint
failed test
review comment
metric movement
production alert
AI observation
```

Signal is not truth.

## 3.2 Observation

A bounded statement about something observed.

Example:

```text
5 of 8 usability participants failed to find the Publish action.
```

Observation should include provenance.

## 3.3 Evidence

An artifact supporting or falsifying a claim.

Examples:

```text
test result
trace
screenshot
analytics query
interview notes
benchmark
incident timeline
production log
```

Evidence is scoped and may have limitations.

## 3.4 Hypothesis

An interpretation that may explain observations.

Example:

```text
The Publish action may be hard to discover because it is visually grouped with secondary actions.
```

A hypothesis is not canonical truth.

## 3.5 Proposal

A proposed change to product, architecture, design, policy, process, or documentation.

Typical artifact:

```text
RFC
PDR proposal
ADR proposal
DDR proposal
change plan
```

## 3.6 Decision

An accepted/rejected choice by the authorized owner.

Decision should record:

```text
context
choice
rationale
trade-offs
owner
date
```

## 3.7 Canonical knowledge

A rule/fact incorporated into the owning Source of Truth.

Examples:

```text
Domain invariant
Product principle
Architecture boundary
Feature contract
Security policy
Design-system contract
Engineering standard
```

## 3.8 Learning

A generalized conclusion supported enough to influence future work.

Examples:

```text
Repeated reviewer findings show async UI changes often omit negative states.
```

A learning may lead to:

```text
standard update
skill update
test gate
workflow change
product principle
```

but does not automatically do so.

## 3.9 Historical knowledge

Previously valid or considered knowledge preserved for traceability but not active instruction.

---

# 4. Knowledge lifecycle states

Recommended semantic lifecycle:

```text
CAPTURED
→ CLASSIFIED
→ EVIDENCED
→ PROPOSED
→ REVIEWED
→ VALIDATED
→ PROMOTED
→ ACTIVE
→ CHALLENGED
→ SUPERSEDED / RETIRED
→ ARCHIVED
```

Alternative terminal paths:

```text
CAPTURED
→ REJECTED

PROPOSED
→ REJECTED

CHALLENGED
→ REVALIDATED
→ ACTIVE
```

Do not force every small piece of information through every state.

The lifecycle is a governance model, not mandatory bureaucracy.

---

# 5. State definitions

## CAPTURED

A signal/observation has been recorded.

Required:

```text
source
date/time or period
scope
```

## CLASSIFIED

The information has been assigned a type and likely owner.

Example:

```text
Type: UX research observation
Owner: UX
```

## EVIDENCED

Supporting evidence exists and provenance is recorded.

This does not mean the interpretation is correct.

## PROPOSED

A concrete claim/change is proposed.

## REVIEWED

Authorized reviewers have evaluated:

```text
evidence
alternatives
scope
risks
conflicts
```

## VALIDATED

The claim is sufficiently supported for the intended scope.

Validation strength depends on risk.

## PROMOTED

Authorized owner has approved incorporation into canonical project knowledge.

## ACTIVE

Canonical owner has been updated and the knowledge is current.

## CHALLENGED

New evidence materially calls the active knowledge into question.

The existing rule remains active unless explicitly suspended/replaced.

## REVALIDATED

Challenge reviewed; existing knowledge remains valid.

## SUPERSEDED

A newer active knowledge item replaces it.

## RETIRED

Knowledge no longer applies and has no direct successor.

## ARCHIVED

Historical context only.

## REJECTED

Proposal/claim was considered but not accepted.

Rejection may remain useful decision memory.

---

# 6. Promotion is explicit

The most important rule:

> **Knowledge does not become canonical because it was written down.**

Promotion requires:

```text
owner
scope
evidence appropriate to risk
review
decision/approval
canonical update
provenance
```

Examples:

```text
Research note
≠ Product Principle

AI recommendation
≠ Architecture rule

Reviewer finding
≠ Engineering Standard

Incident observation
≠ permanent policy
```

A promotion action is what changes status.

---

# 7. Promotion routes

## 7.1 Research → Product / UX

```text
Research evidence
→ synthesis
→ hypothesis
→ Product/UX proposal
→ PDR/DDR if material
→ canonical Product/UX doc
```

## 7.2 Engineering discovery → Architecture/Engineering

```text
implementation observation
→ evidence
→ RFC/ADR or standard proposal
→ review
→ canonical architecture/engineering update
```

## 7.3 Incident → Operations / Engineering / Security

```text
incident
→ timeline/evidence
→ root-cause analysis
→ learning
→ corrective decision
→ runbook/test/policy/architecture update
```

## 7.4 Analytics → Product decision

```text
metric observation
→ validated query
→ interpretation
→ product hypothesis
→ experiment/decision
→ canonical product update if accepted
```

## 7.5 Code review → Engineering learning

```text
review finding
→ repeated pattern
→ learning
→ standard/skill/checklist proposal
→ validation
→ promotion
```

## 7.6 AI-agent output → Project knowledge

```text
AI observation/proposal
→ provenance
→ owner review according to risk
→ accepted decision
→ canonical promotion
```

AI output MUST NOT skip directly to canonical truth for protected/high-impact scopes.

---

# 8. Evidence requirements are risk-based

Do not demand the same evidence level for everything.

Example:

Low risk:

```text
Rename an internal documentation heading.
```

May require no formal evidence.

High risk:

```text
Change authorization policy.
```

Requires much stronger validation.

Use risk classes from the future Agent/Change Operating Model when available.

Until then, consider:

```text
reversibility
user impact
security impact
financial impact
data impact
architecture scope
regulatory impact
```

---

# 9. Provenance contract

Every significant knowledge item SHOULD answer:

```text
Where did this come from?
Who/what produced it?
When?
Under what baseline/version?
What evidence supports it?
Who approved promotion?
What canonical source now owns it?
What supersedes it?
```

Recommended fields:

```text
knowledge_id
type
scope
owner
created_at
source_refs
evidence_refs
decision_refs
canonical_refs
status
promoted_at
promoted_by
supersedes
superseded_by
review_due
limitations
```

---

# 10. Knowledge record

For important reusable learnings, a project MAY use:

```markdown
# Learning — <Title>

**ID:** K-XXX
**Status:** ACTIVE
**Scope:** Engineering
**Owner:** Engineering
**Captured:** YYYY-MM-DD
**Promoted:** YYYY-MM-DD
**Evidence:** ...
**Decision:** ...
**Canonical target:** ...

## Observation

## Evidence

## Interpretation

## Decision / Learning

## Where it was promoted

## Limitations

## Revisit trigger
```

Do not create knowledge records for every trivial fact.

---

# 11. Canonical promotion rule

When knowledge is promoted:

```text
1. update owning canonical document;
2. link decision/evidence where material;
3. mark source proposal/learning appropriately;
4. update superseded knowledge;
5. update indexes/manifests if used.
```

The canonical document remains the place contributors read for current truth.

They should not need to reconstruct current truth from 30 old research notes.

---

# 12. Canonical demotion does not exist silently

An active rule cannot simply disappear.

Use:

```text
SUPERSEDED
or
RETIRED
```

with rationale or decision reference when material.

This preserves institutional memory.

---

# 13. Challenge process

New evidence may challenge active knowledge.

Example:

```text
Active:
Mobile bottom sheet improves task completion.

New evidence:
Accessibility audit shows severe focus-management problems.
```

Process:

```text
ACTIVE
→ CHALLENGED
→ review evidence
→ REVALIDATED
or
→ replacement proposal
→ SUPERSEDED
```

Do not overwrite history.

---

# 14. Freshness vs validity

Freshness and validity are different.

An active piece of knowledge may be:

```text
CURRENT
REVIEW_DUE
STALE_REVIEW_REQUIRED
```

without automatically becoming false.

A recent observation may also be wrong.

Use freshness only as a review signal.

---

# 15. Confidence

Avoid fake numerical confidence unless the project has a defined calibrated method.

Prefer descriptive evidence state:

```text
UNVERIFIED
SUPPORTED
VALIDATED_FOR_SCOPE
CONTESTED
```

Do not display arbitrary:

```text
Confidence: 93%
```

for qualitative project knowledge.

---

# 16. Knowledge scope

Every promoted knowledge item should have a bounded scope.

Examples:

```text
project-wide
frontend only
billing domain
mobile application
Search feature
Design System
production operations
```

A learning validated in one scope does not automatically generalize to all projects.

---

# 17. Knowledge portability

Universal knowledge and project-specific knowledge are different.

## Project knowledge

Example:

```text
Artist OS uses numbered authoring sections.
```

Lives in project docs.

## Universal knowledge

Example:

```text
Author and final reviewer should be separated for high-risk changes.
```

May belong to U-POS universal policy after sufficient validation.

Promotion across project boundaries requires explicit review.

Do not automatically generalize one project's preference into a universal standard.

---

# 18. Knowledge and Decision Records

Decision Records and Knowledge Records serve different purposes.

```text
Decision Record
→ why a choice was made

Canonical Contract
→ what is true now

Knowledge/Learning Record
→ what was learned and from what evidence
```

They may cross-link.

One artifact should not be forced to own all three responsibilities.

---

# 19. Knowledge and Plans

Plans may contain assumptions.

An assumption in a Plan is not canonical truth.

Example:

```text
Plan assumption:
We expect API migration to finish in Q4.
```

Do not promote it to architecture truth.

After execution, observations can become evidence for future decisions.

---

# 20. Knowledge and Reports

Reports are point-in-time evidence.

Example:

```text
Performance Audit — 2026-09-19
```

It may support a decision.

It should not be treated as timeless active instruction.

---

# 21. Knowledge and code

Code produces implementation evidence.

Examples:

```text
current behavior
current API shape
current performance
current test assumptions
```

A code pattern repeated many times can be:

```text
intentional standard
legacy convention
accidental duplication
technical debt
```

Do not promote it without review.

---

# 22. Knowledge and tests

Tests are strong evidence of expected implemented behavior.

But test presence alone does not establish product authority.

If a test contradicts confirmed canonical contract:

```text
the test may be wrong.
```

Classify the drift.

---

# 23. Knowledge and AI memory

For AI-assisted projects:

> **Project memory should primarily be built from governed project knowledge, not raw model conversation history.**

Preferred agent context:

```text
canonical docs
accepted decisions
validated learnings
relevant evidence
current plan
```

Lower priority:

```text
raw brainstorming
unreviewed AI notes
old chat transcripts
rejected proposals
```

unless directly relevant.

---

# 24. AI knowledge contribution classes

AI may produce:

```text
AI_OBSERVATION
AI_HYPOTHESIS
AI_PROPOSAL
AI_REVIEW_FINDING
AI_LEARNING_CANDIDATE
```

These labels make epistemic state explicit.

AI SHOULD NOT label its own unreviewed output:

```text
CANONICAL
VALIDATED
```

unless the operating policy explicitly permits autonomous promotion for that low-risk scope.

---

# 25. Human approval boundaries

Until overridden by the future Agent Operating Model, human/authorized-owner approval is required to promote knowledge that changes:

```text
Product Vision
Product Principles
major Scope
Domain invariants/lifecycles
Architecture boundaries
Security/privacy
Authorization
Billing
Data retention/deletion
irreversible operations
major UX direction
universal U-POS policies
```

Low-risk documentation corrections MAY be autonomously promoted if project policy allows.

---

# 26. Repeated findings → organizational learning

A powerful learning loop:

```text
Agent/Reviewer finding
↓
same finding repeats
↓
pattern detected
↓
Learning Candidate
↓
root-cause review
↓
proposed change to:
  Skill
  Policy
  Standard
  Test
  Workflow
↓
promotion
↓
measure recurrence after change
```

This is how an AI-native engineering organization “learns” without fine-tuning the base model.

---

# 27. Learning effectiveness

After promoting a learning, measure whether it helped.

Examples:

```text
review finding frequency
rework rate
first-pass approval
escaped defects
human intervention
cycle time
```

Do not keep rules merely because they were once added.

A rule that adds cost without measurable value may itself be challenged.

---

# 28. Knowledge debt

Track high-value gaps:

```text
unknown owner
unvalidated critical assumption
accepted decision not propagated
stale high-risk policy
conflicting canonical claims
learning candidate not reviewed
```

Do not create tickets for every informal note.

---

# 29. Knowledge loss prevention

Before deleting or archiving a source:

```text
1. identify unique knowledge;
2. confirm canonical promotion where required;
3. preserve decision/evidence references;
4. preserve provenance;
5. then archive/delete according to documentation policy.
```

This aligns with Documentation Migration rules.

---

# 30. Knowledge traceability chain

For material changes, target:

```text
Signal / Problem
↓
Observation
↓
Evidence
↓
Proposal
↓
Decision
↓
Canonical Contract
↓
Implementation
↓
Test / Telemetry
↓
Learning
↓
Next Decision
```

Not every change needs every link.

High-risk changes should have stronger traceability.

---

# 31. Knowledge retrieval priority

When assembling context, prefer:

```text
1. Active canonical sources
2. Accepted decisions relevant to those sources
3. Validated active learnings
4. Current plan
5. Recent relevant evidence
6. Historical material
7. Raw/unreviewed notes
```

This order is a default, not a substitute for scope ownership.

---

# 32. Contradictory knowledge

If two knowledge items disagree:

```text
do not merge them into a compromise automatically.
```

Resolve through the Source-of-Truth Model:

```text
scope
owner
canonical source
decision
evidence
```

Keep dissenting/historical evidence where useful.

---

# 33. Knowledge lifecycle event model

Future observability may emit events such as:

```text
KNOWLEDGE_CAPTURED
KNOWLEDGE_CLASSIFIED
EVIDENCE_LINKED
PROPOSAL_CREATED
KNOWLEDGE_REVIEWED
KNOWLEDGE_VALIDATED
KNOWLEDGE_PROMOTED
KNOWLEDGE_CHALLENGED
KNOWLEDGE_REVALIDATED
KNOWLEDGE_SUPERSEDED
KNOWLEDGE_RETIRED
KNOWLEDGE_ARCHIVED
```

This allows future dashboards to show organizational learning.

---

# 34. Integration with Agent Organization

The future Agent Operating Model should use this model for:

```text
context assembly
memory
agent outputs
review findings
learning candidates
skill evolution
policy evolution
decision promotion
human approval
```

Suggested boundary:

```text
Agent Runtime
produces signals/evidence/proposals

Knowledge Lifecycle
governs promotion

Source-of-Truth Model
determines canonical owner

Documentation System
stores durable truth/history
```

---

# 35. Integration with Observability

A future Agent Observability layer should be able to answer:

```text
Which agent produced this observation?
Which evidence supported it?
Who validated it?
Where was it promoted?
Did it reduce future failures?
What knowledge was superseded?
```

This creates auditable organizational learning.

---

# 36. Definition of Done

The Knowledge Lifecycle is correctly instantiated when:

```text
[ ] evidence is distinguishable from canonical truth
[ ] proposals are distinguishable from accepted decisions
[ ] decisions propagate into canonical owners
[ ] important knowledge has provenance
[ ] AI outputs cannot silently become doctrine
[ ] active knowledge can be challenged/revalidated
[ ] superseded knowledge remains traceable
[ ] repeated failures can become learning candidates
[ ] promoted learnings can update standards/skills/tests/workflows
[ ] retrieval prioritizes governed current knowledge
```

---

# 37. Golden rules

> **Written does not mean canonical.**

> **Observed does not mean explained.**

> **Evidence supports a claim; evidence is not the claim.**

> **A decision creates authority only within the owner's scope.**

> **Promotion into canonical truth is explicit.**

> **New evidence can challenge old knowledge without erasing history.**

> **AI may generate knowledge candidates; governance decides what becomes institutional memory.**

> **The project should learn through governed memory before considering model fine-tuning.**
