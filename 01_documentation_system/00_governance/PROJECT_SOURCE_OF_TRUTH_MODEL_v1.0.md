# Project Source-of-Truth Model v1.0

**ID:** DOC-GOV-SOT-001  
**Type:** STANDARD / GOVERNANCE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** Project Governance  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Changes to documentation authority, ownership, conflict resolution, decision precedence, or canonicalization policy  
**Supersedes:** —  
**Related:** DOC-STD-001, `templates/SOURCE_OF_TRUTH_TEMPLATE.md`, PROJECT_KNOWLEDGE_LIFECYCLE_MODEL_v1.0.md

---

## 0. Purpose

This standard defines the universal model for determining:

- which project source owns a fact;
- which statement is authoritative when multiple sources exist;
- how local specifications refine upstream truth;
- how accepted decisions affect canonical documentation;
- how implementation evidence participates without automatically becoming doctrine;
- how conflicts are detected, classified, resolved, and recorded;
- how humans and AI agents identify the correct source before acting.

The governing principle is:

> **Authority is scoped. No single project document is globally authoritative for every kind of truth.**

This model operationalizes the Source-of-Truth rules already present in the Project Documentation Operating Model.

---

# 1. What “Source of Truth” means

A Source of Truth is not simply:

> “the newest file”

and not:

> “the biggest MASTER document”

and not:

> “whatever the code currently does.”

A Source of Truth is:

> **the currently authorized canonical owner of a defined class of project facts.**

Examples:

```text
Product direction
→ Product

Domain lifecycle
→ Domain

Service ownership
→ Architecture

Feature-specific behavior
→ Product Spec

Navigation semantics
→ UX

Reusable component behavior
→ Design System

Wire schema
→ API/Data

Authorization policy
→ Security

Current migration sequence
→ Plan
```

---

# 2. Core entities

The model distinguishes the following concepts.

## 2.1 Claim

A statement asserting that something is true.

Example:

```text
A published revision is immutable.
```

## 2.2 Fact scope

The authority domain that should own the claim.

Example:

```text
published revision lifecycle
→ Domain
```

## 2.3 Canonical owner

The project layer or explicitly delegated document responsible for authoritative truth in that scope.

## 2.4 Canonical source

The active normative document, contract, registry, schema, or decision that expresses the canonical owner's current truth.

## 2.5 Refinement

A narrower rule that adds local detail without contradicting the upstream owner.

Example:

```text
Global:
Destructive actions require confirmation.

Feature:
Deleting a workspace requires typing the workspace name.
```

## 2.6 Conflict

Two active sources make incompatible claims about the same fact.

## 2.7 Evidence

Observed information about implementation, runtime, research, tests, analytics, incidents, or users.

Evidence can challenge canonical truth.

Evidence does not automatically become canonical truth.

## 2.8 Decision

An accepted choice that may create, change, or supersede canonical truth.

A Decision Record preserves why.

The owning canonical document preserves what is currently true.

---

# 3. Scoped authority map

Default universal ownership:

```text
Product / business truth
→ 01_product/

Domain semantics / lifecycles / invariants
→ 02_domain/

Architecture ownership / boundaries / topology
→ 03_architecture/

Feature-specific behavior
→ 04_product_specs/

UX / IA / navigation / user flows / content language
→ 05_ux/

Reusable visual / interaction system
→ 06_design_system/

Engineering implementation standards
→ 07_engineering/

API / data / integrations
→ 08_data_api/

AI system contracts
→ 09_ai/

Security / privacy / compliance
→ 10_security_privacy/

Quality strategy / test evidence
→ 11_quality_testing/

Analytics / metrics
→ 12_analytics/

Operations / release / restore / incident procedures
→ 13_operations/

Decision rationale
→ 14_decisions/

Current execution / migrations / sequencing
→ 15_plans/

Contributor guidance
→ 16_onboarding/

Lookup/reference
→ 17_reference/

Historical/superseded material
→ 99_archive/
```

A concrete project MAY adapt this map.

Any adaptation MUST be explicit in the project's `SOURCE_OF_TRUTH.md`.

---

# 4. Authority is by scope, not by folder number

The layer numbers provide organization.

They do not mean:

```text
01_product always overrides 10_security
```

That would be incorrect.

Examples:

```text
Product says:
Users should be able to export data.

Security says:
Export requires recent re-authentication.

Result:
No conflict.
Security refines the protected execution condition.
```

Another example:

```text
Feature Spec says:
Any authenticated user may delete an Organization.

Authorization Contract says:
Only Organization Owner may delete it.

Result:
Real conflict.
Security/Authorization owns permission semantics.
Feature Spec must be corrected.
```

---

# 5. Canonicality dimensions

A source is authoritative only when the relevant dimensions are satisfied.

Recommended evaluation:

```text
Scope ownership
Status
Normativity
Freshness
Specificity
Accepted decisions
Version compatibility
```

## 5.1 Scope ownership

Most important.

A document outside the owning scope cannot silently redefine upstream truth.

## 5.2 Status

Typical authority:

```text
ACTIVE
> APPROVED for future target state
> REVIEW / DRAFT
> DEPRECATED
> SUPERSEDED
> ARCHIVED
```

Do not use this as a blind global ranking.

An `APPROVED` target architecture may intentionally describe future state while current `ACTIVE` operations still describe production.

## 5.3 Normativity

```text
NORMATIVE
```

can own a contract.

```text
EVIDENCE
REPORT
INFORMATIVE
```

can inform/challenge it but do not automatically override it.

## 5.4 Freshness

A stale source may require review.

Staleness does not itself authorize another scope to take ownership.

## 5.5 Specificity

A local source may refine the owner when explicitly permitted.

Specificity cannot justify contradiction.

---

# 6. Canonical source resolution algorithm

Humans and AI agents SHOULD use this sequence before changing important behavior.

```text
1. Identify the exact claim/fact being decided.
2. Classify its fact scope.
3. Resolve the canonical owner for that scope.
4. Locate ACTIVE normative source(s) from that owner.
5. Check accepted Decision Records that affect the claim.
6. Check narrower feature/local contracts for valid refinement.
7. Check version/baseline applicability.
8. Compare implementation/runtime evidence.
9. If aligned → proceed.
10. If implementation differs → record drift.
11. If canonical sources disagree → register conflict.
12. If no owner/source exists → mark UNKNOWN / OWNER DECISION REQUIRED.
```

Do not skip directly from:

```text
"I found code that does X"
```

to:

```text
"Therefore X is product truth."
```

---

# 7. Refinement rule

A child/local contract MAY add detail when all are true:

```text
same upstream semantics preserved
no invariant is violated
no permission is weakened
no lifecycle transition is invented
no API/data contract is contradicted
no security/privacy constraint is bypassed
```

Good:

```text
UX Constitution:
Errors must provide recovery when recoverable.

Upload Feature Spec:
On transient upload failure show Retry.
```

Bad:

```text
Security:
Deletion requires Owner permission.

Feature Spec:
Editor may delete from this screen.
```

---

# 8. Decision precedence

A Decision Record is historical rationale.

It does not replace the canonical contract forever.

Correct sequence:

```text
RFC / evidence
→ Decision
→ ADR/PDR/DDR/SDR
→ canonical owner updated
```

After promotion:

```text
Canonical document
= current truth

Decision Record
= why it became truth
```

If an accepted decision has not yet been propagated into its canonical owner:

```text
state = OUT_OF_SYNC
```

The discrepancy must be reconciled.

---

# 9. Implementation evidence

Implementation is a critical evidence source.

It can prove:

```text
what currently happens
what schema currently exists
what route currently exists
what tests currently enforce
```

It cannot alone prove:

```text
what product behavior should be
what policy is intended
what future architecture is approved
what security permission should be
```

Use three possible drift interpretations:

```text
DOC_DRIFT
Documentation is stale.

IMPLEMENTATION_DRIFT
Implementation violates confirmed contract.

TRANSITIONAL_DRIFT
An approved migration is intentionally incomplete.
```

Do not automatically assume either docs or code wins.

---

# 10. Generated contracts

Generated artifacts may be canonical for their specific machine contract when explicitly designated.

Examples:

```text
OpenAPI
→ HTTP wire schema

database migration/schema
→ deployed storage shape

generated protobuf schema
→ message shape
```

But:

```text
Database schema
≠ Domain Model

OpenAPI
≠ Product behavior

Storybook
≠ complete UX Constitution
```

Machine truth remains scoped.

---

# 11. Conflict taxonomy

## SOT-C1 — Duplicate aligned

Two sources repeat the same fact.

Action:

```text
choose owner
replace duplicate with link/summary
```

## SOT-C2 — Historical conflict

Old/historical source contradicts active truth.

Action:

```text
mark/archive/supersede
repair references
```

## SOT-C3 — Local refinement ambiguity

Unclear whether local detail refines or contradicts upstream truth.

Action:

```text
owner review
```

## SOT-C4 — Active normative conflict

Two active authoritative-looking sources disagree.

Action:

```text
BLOCK affected change
identify owner
resolve explicitly
```

## SOT-C5 — Code/document drift

Implementation differs from canonical contract.

Action:

```text
classify DOC_DRIFT / IMPLEMENTATION_DRIFT / TRANSITIONAL_DRIFT
```

## SOT-C6 — Missing owner

Important fact has no canonical owner.

Action:

```text
OWNER DECISION REQUIRED
```

## SOT-C7 — Accepted decision not propagated

Decision exists but current canonical docs do not reflect it.

Action:

```text
reconcile canonical owner
```

---

# 12. High-risk conflict rule

The following conflicts MUST NOT be silently resolved by an AI agent:

```text
billing/money
authentication
authorization
privacy
retention
destructive actions
data ownership
domain lifecycle
compliance
production safety
irreversible migration
```

Required:

```text
explicit owner or human governance decision
```

---

# 13. Project `SOURCE_OF_TRUTH.md`

Every non-trivial instantiated project SHOULD have:

```text
docs/00_governance/SOURCE_OF_TRUTH.md
```

It is a project adapter of this universal model.

It should declare:

```text
Scope
Canonical owner
Canonical path/source
Status
Notes / refinements
```

Recommended table:

```markdown
| Scope | Canonical owner | Canonical source | Notes |
|---|---|---|---|
| Product principles | Product | docs/01_product/PRODUCT_PRINCIPLES.md | |
| Domain lifecycles | Domain | docs/02_domain/LIFECYCLES.md | |
| Architecture | Architecture | docs/03_architecture/MASTER_ARCHITECTURE.md | |
```

The existing `SOURCE_OF_TRUTH_TEMPLATE.md` is the starter template.

---

# 14. Source-of-Truth Registry entry

For larger projects, a machine-readable record MAY include:

```json
{
  "scope": "domain.lifecycle.subscription",
  "owner": "Domain",
  "canonicalSource": "docs/02_domain/LIFECYCLES.md",
  "status": "ACTIVE",
  "normativity": "NORMATIVE",
  "relatedDecisions": ["PDR-014"],
  "lastReviewed": "YYYY-MM-DD"
}
```

Do not create a registry for small projects without need.

---

# 15. Cross-layer examples

## Example A — UX and Design System

```text
UX:
Peer views inside one workspace use local peer navigation.

Design System:
LocalSegmentedNav is the reusable component for that interaction.

Feature:
Brain uses Overview / Inbox / Tone & Voice.
```

All three can be true without duplication of ownership.

## Example B — Domain and UI

```text
Domain:
Revision status = APPROVED.

Design System:
StatusChip visual role = positive.

Feature:
Display APPROVED using StatusChip.
```

Design System does not own the lifecycle value.

## Example C — Plan and Architecture

```text
Architecture:
Search will be owned by Search service in target architecture.

Migration Plan:
Current release still reads from legacy monolith until Phase 3.
```

This is transitional state, not necessarily contradiction.

---

# 16. AI-agent Source-of-Truth contract

Before making a significant change, an AI agent MUST:

```text
1. classify the fact scope;
2. read the project's SOURCE_OF_TRUTH map;
3. read the owning canonical source;
4. read relevant local specs;
5. check accepted decisions where material;
6. inspect implementation evidence;
7. report unresolved conflict instead of inventing resolution.
```

AI MUST NOT infer authority from:

```text
filename alone
file length
modification time alone
code convenience
visual reference
one comment
one old README
```

---

# 17. Source-of-Truth handoff to Agent Organization

The future AI Agent Operating Model should depend on this interface:

```text
resolve_scope(task)
→ resolve_canonical_owner(scope)
→ resolve_canonical_sources(owner, task)
→ assemble_context
→ execute within authority
```

Agents should not hard-code project-specific documentation paths.

Project-specific paths belong in:

```text
PROJECT_AGENT_MANIFEST
```

or equivalent project adapter.

---

# 18. Definition of Done

The Source-of-Truth model is correctly instantiated when:

```text
[ ] major scopes have canonical owners
[ ] critical canonical sources are discoverable
[ ] no known high-risk active conflicts remain hidden
[ ] local specs refine rather than silently override
[ ] accepted decisions are propagated
[ ] code-vs-doc drift is classified
[ ] archived material cannot masquerade as active truth
[ ] AI contributors have deterministic authority resolution
```

---

# 19. Golden rules

> **One fact should have one canonical owner.**

> **Authority is scoped, not global.**

> **Specificity may refine; it may not silently contradict.**

> **Evidence can challenge truth; evidence does not automatically become truth.**

> **A Decision Record explains why; the canonical contract states what is true now.**

> **Implementation is evidence of current behavior, not automatic authority over intent.**

> **When authority is ambiguous, stop guessing and make the ambiguity explicit.**
