# UPOS-005 Context & Memory — ChatGPT Single-File Edition v1.0

**Module:** UPOS-005 — Context & Memory  
**System:** Universal Project Operating System  
**Canonical baseline:** FROZEN v1.0  
**Embedded virtual files:** 36  
**Generated:** 2026-09-19

---

# 0. Interpretation rule

This is a transport bundle, not a replacement monolith and not a new Source of Truth.

Each virtual-file block represents one repository file under `05_context_memory/`.

Normative authority remains with the embedded normative Markdown documents.

`analysis/` is historical EVIDENCE only.

`MODULE_05_TRACEABILITY.md` is the canonical normative coverage artifact.

## Core invariants

```text
MEMORY != TRUTH
CONTEXT != TRUTH
CACHE != TRUTH
DERIVED_SUMMARY != CANONICAL_SOURCE
RAW_CHAT_HISTORY != PROJECT_MEMORY
PROVIDER_PRIVATE_MEMORY != PROJECT_KNOWLEDGE
```

## Stable semantic identities

```text
context_request_id
context_bundle_id
memory_item_id
```

## Core flow

```text
Task / Workflow / Stage / Role / Skill
→ Context Requirements
→ Context Request
→ UPOS-01 canonical source resolution
→ UPOS-010 permission constraints
→ UPOS-011 physical provider resolution
→ UPOS-005 eligibility / retrieval / freshness
→ budget / representation / Context View
→ immutable Context Bundle
→ Agent Run / Skill Invocation
→ temporary Memory / output
→ candidate
→ UPOS-01 / UPOS-009 governance
```

## Frozen validation

```text
Template conformance = PASS
Unresolved P0/P1 Module-05 gaps = 0

UNMAPPED MODULE-05 SOURCE REQUIREMENTS = 0

NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 04 / 06–11
```

# 1. Virtual repository tree

```text
05_context_memory/
├── README.md
├── CONTEXT_MEMORY_OPERATING_MODEL.md
├── CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md
├── CONTEXT_BUNDLE_STANDARD.md
├── SOURCE_RESOLUTION_INTERFACE.md
├── RETRIEVAL_AND_SELECTION_STANDARD.md
├── CONTEXT_ASSEMBLY_STANDARD.md
├── CONTEXT_BUDGET_AND_REPRESENTATION.md
├── FRESHNESS_INVALIDATION_AND_REASSEMBLY.md
├── CONTEXT_ISOLATION_AND_VIEWS.md
├── CONTEXT_FAILURE_MODEL.md
├── MEMORY_TAXONOMY.md
├── MEMORY_READ_WRITE_STANDARD.md
├── MEMORY_LIFECYCLE_AND_INVALIDATION.md
├── PROJECT_MEMORY_INTERFACE.md
├── CONTEXT_MEMORY_LIFECYCLE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_05_DEFINITION_OF_DONE.md
├── MODULE_05_TRACEABILITY.md
├── VIRTUAL_REPOSITORY_TREE.md
├── templates/CONTEXT_BUNDLE_TEMPLATE.md
├── templates/CONTEXT_REQUEST_TEMPLATE.md
├── templates/CONTEXT_REQUIREMENT_TEMPLATE.md
├── templates/MEMORY_ITEM_TEMPLATE.md
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md
├── analysis/CONTEXT_ISOLATION_ANALYSIS.md
├── analysis/FIRST_DELIVERABLE_SUMMARY.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MEMORY_TAXONOMY_ANALYSIS.md
├── analysis/MODULE_05_OWNERSHIP_MAP.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
```

# 2. Embedded virtual files


---

## VIRTUAL FILE 1/36 — `README.md`

**Virtual path:** `README.md`  
**Content checksum:** `4efbeba59aff`

===== BEGIN VIRTUAL FILE: README.md =====

# UPOS-005 — Context & Memory

**ID:** UPOS-05-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01, UPOS-002, UPOS-003, UPOS-004


**Canonical baseline:** FROZEN v1.0 — further semantic changes require a new reviewed version.

## 0. Purpose

UPOS-005 defines how U-POS assembles the minimum sufficient, authoritative, fresh, relevant, permission-safe, role-appropriate and traceable execution context for a bounded consumer without creating a second Source of Truth.

It also defines bounded execution-support Memory and its strict separation from governed Project Knowledge.

## 1. Fundamental separation

```text
KNOWLEDGE
= governed project truth / evidence / proposal / historical knowledge
  owned by UPOS-01

CONTEXT
= execution-time selected information
  assembled for a bounded consumer and purpose

MEMORY
= retained execution-support information
  with explicit scope, provenance, lifetime and authority limits

RETRIEVAL
= process of locating eligible information

SOURCE RESOLUTION
= determination of canonical owner/source through UPOS-01

CONTEXT BUNDLE
= attributable assembled execution package

CACHE
= performance optimization
  with zero additional semantic authority
```

These terms MUST NOT be used interchangeably.

## 2. Critical invariants

```text
MEMORY != TRUTH
CONTEXT != TRUTH
CACHE != TRUTH
DERIVED_SUMMARY != CANONICAL_SOURCE
RAW_CHAT_HISTORY != PROJECT_MEMORY
PROVIDER_PRIVATE_MEMORY != PROJECT_KNOWLEDGE
```

Canonicality remains UPOS-01 ownership.

## 3. Context goal

Do not optimize for:

```text
maximum retrieved documents
maximum tokens
maximum remembered history
```

Optimize for:

```text
minimum sufficient
authoritative
fresh
relevant
permission-safe
role-appropriate
traceable
context
```

## 4. Core flow

```text
Task / Workflow / Stage / Role / Skill
↓
Context Requirements
↓
Context Request
↓
UPOS-01 canonical owner/source resolution
↓
UPOS-010 permission constraints
↓
UPOS-011 physical source/provider resolution
↓
UPOS-005 eligibility + retrieval
↓
authority-aware selection
↓
freshness validation
↓
budget / representation
↓
Context Bundle
↓
Agent Run / Skill Invocation
↓
output / temporary memory
↓
possible candidate
↓
UPOS-01 / UPOS-009 governance
```

## 5. Stable Module-05 identities

```text
context_request_id
context_bundle_id
memory_item_id
```

No additional global identity is introduced in v1 for source resolution or retrieval decisions. Their provenance is carried through upstream references and the Context Manifest.

## 6. Upstream execution identity references

Where applicable, a Context Request/Bundle references externally owned identities:

```text
project_id/reference
task_id
routing_decision_id
workflow_instance_id
stage_id
role_id
agent_definition_id/version
agent_run_id
skill_id/version
skill_invocation_ref
```

Module 05 consumes but does not own these identities.

## 7. Scope / non-scope

UPOS-005 owns retrieval/assembly/budget/freshness/isolation/memory semantics.

It MUST NOT redefine:

```text
project truth / canonical ownership             → UPOS-01
Role authority / Agent identity / SoD           → UPOS-002
Skill procedure                                 → UPOS-003
Workflow routing/state/stage order              → UPOS-004
Git/PR/merge mechanics                          → UPOS-006
Quality evidence/verdict/gates                  → UPOS-007
events/traces/metrics/dashboard                 → UPOS-008
organizational learning/promotion               → UPOS-009 + UPOS-01
access grants/secrets/security policy           → UPOS-010
paths/providers/search/storage/model bindings   → UPOS-011
```

## 8. Recommended read order

1. `CONTEXT_MEMORY_OPERATING_MODEL.md`
2. `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md`
3. `CONTEXT_BUNDLE_STANDARD.md`
4. `SOURCE_RESOLUTION_INTERFACE.md`
5. `RETRIEVAL_AND_SELECTION_STANDARD.md`
6. `CONTEXT_ASSEMBLY_STANDARD.md`
7. `CONTEXT_BUDGET_AND_REPRESENTATION.md`
8. `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md`
9. `CONTEXT_ISOLATION_AND_VIEWS.md`
10. `CONTEXT_FAILURE_MODEL.md`
11. `MEMORY_TAXONOMY.md`
12. `MEMORY_READ_WRITE_STANDARD.md`
13. `MEMORY_LIFECYCLE_AND_INVALIDATION.md`
14. `PROJECT_MEMORY_INTERFACE.md`
15. `CONTEXT_MEMORY_LIFECYCLE.md`
16. `CROSS_MODULE_INTERFACES.md`
17. `MODULE_05_TRACEABILITY.md`

===== END VIRTUAL FILE: README.md =====


---

## VIRTUAL FILE 2/36 — `CONTEXT_MEMORY_OPERATING_MODEL.md`

**Virtual path:** `CONTEXT_MEMORY_OPERATING_MODEL.md`  
**Content checksum:** `5d89b6da818a`

===== BEGIN VIRTUAL FILE: CONTEXT_MEMORY_OPERATING_MODEL.md =====

# Context & Memory Operating Model

**ID:** UPOS-05-CMO-001  
**Type:** OPERATING MODEL  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md, CONTEXT_BUNDLE_STANDARD.md


## 1. Governing principle

UPOS-005 is an execution-context system, not a knowledge-authority system.

It consumes governed knowledge and evidence, assembles bounded Context, and may retain noncanonical execution Memory.

## 2. Knowledge vs Context vs Memory

### Knowledge

Knowledge is governed under UPOS-01.

Module 05 may reference and represent Knowledge but cannot promote, demote, supersede, or re-own it.

### Context

Context is a consumer-specific selection.

The same canonical project may correctly produce different Context Views for Product, Architecture, Implementer, Reviewer, QA, Merge Controller, or Human decision-maker.

### Memory

Memory supports execution continuity.

Persistence duration does not create truth.

A persisted Task note remains noncanonical until separately governed.

## 3. Context is not a universal blob

Context MUST be bounded by:

```text
project
Task
Workflow Instance
Stage
Role
Agent Run
Skill Invocation where applicable
purpose
Change Class / concern implications
permission/security constraints
independence requirements
```

## 4. Context Request → Bundle

```text
Context Requirement
→ concrete Context Request
→ canonical source resolution
→ candidate retrieval
→ eligibility gate
→ relevance/priority
→ representation/budget
→ Context Manifest
→ immutable Context Bundle
```

## 5. Minimum sufficient context

The system SHOULD stop adding information when the bounded consumer has sufficient authoritative context to satisfy its contract safely.

More context is not automatically better.

## 6. Context policy version

Every production Context Request/Bundle MUST reference:

```text
context_policy_ref
context_policy_version
```

This explains why the same source universe can produce different valid bundles under different governed Context policies.

Context policy version is distinct from source versions and Bundle identity.

## 7. Determinism / explainability

Given the same:

```text
Task scope
Workflow/Stage
Role
Skill
source versions
policies
permissions
context policy version
```

assembly SHOULD be explainable and substantially reproducible.

Byte-identical retrieval is not required when a provider is nondeterministic.

Every material inclusion/exclusion/summary decision MUST remain justifiable.

## 8. No hidden learning

Private memory or repeated context patterns MUST NOT silently change policy, Skills, Workflows, or project truth.

Systemic finding flow:

```text
evidence
→ Learning Candidate
→ UPOS-009
→ UPOS-01 governance
→ proposed change to owned artifact
```

## 9. Provider independence

UPOS-005 Context semantics are provider-, model-, search-, storage-, and repository-platform independent.

Context semantics are independent from model, search engine, vector database, storage engine, repository host, or document platform.

Concrete bindings remain UPOS-011/runtime.

===== END VIRTUAL FILE: CONTEXT_MEMORY_OPERATING_MODEL.md =====


---

## VIRTUAL FILE 3/36 — `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md`

**Virtual path:** `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md`  
**Content checksum:** `9f5d6adbd7b5`

===== BEGIN VIRTUAL FILE: CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md =====

# Context Requirement & Request Standard

**ID:** UPOS-05-CRQ-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/CONTEXT_REQUIREMENT_TEMPLATE.md, templates/CONTEXT_REQUEST_TEMPLATE.md


## 1. Context Requirement

A Context Requirement is a reusable declaration of the information characteristics a consumer needs.

It may originate from:

- an Agent/Role interface;
- a Skill Contract;
- a Workflow/Stage Contract;
- an external Quality/Security/Engineering contract;
- a project adapter refinement that does not weaken universal constraints.

A Requirement declares **what is needed**, not how a provider retrieves it.

## 2. Context Request

A Context Request is a concrete request to satisfy one or more Context Requirements for a bounded execution scope.

Every production Context Request MUST have stable:

```text
context_request_id
```

## 3. Required attribution

Where applicable:

```text
context_request_id

project_id_ref
task_id
routing_decision_id
workflow_instance_id
stage_id

role_id
agent_definition_id
agent_definition_version
agent_run_id

skill_id
skill_version
skill_invocation_ref

purpose
required_source_classes
optional_source_classes

context_constraints
representation_constraints
budget_constraints

permission_security_constraint_refs

independence_requirements

context_policy_ref
context_policy_version

prior_context_bundle_id if this is rework/reassembly
```

Missing non-applicable upstream references MUST be represented explicitly as not applicable, not fabricated.

## 4. Required vs optional sources

### REQUIRED

Required Source Class/material:

- must be resolved or explicitly reported unsatisfied;
- MUST NOT be silently omitted because of budget;
- MUST NOT be substituted by lower-authority relevant material;
- may force `CONTEXT_INCOMPLETE` / blocked assembly when unavailable.

### OPTIONAL

Optional material may be omitted under relevance, freshness, permission, duplication, or budget policy.

Omission SHOULD be recorded when materially relevant to understanding the Bundle.

## 5. Requiredness vs priority

Requiredness and priority are different axes.

```text
required / optional
!=
priority level
```

A required source remains required even if a higher-relevance optional source exists.

## 6. Context constraints

A Request may carry semantic constraints such as:

- exact representation required;
- historical material allowed/forbidden;
- independent Reviewer view required;
- implementation evidence required;
- reference-only sensitive source allowed;
- time-sensitive freshness limit from external policy.

Module 05 interprets these constraints without inventing upstream authority.

## 7. Skill Context interface

```text
Skill Definition + version
+ Role
+ Task
+ Workflow Stage
→ Context Requirements
→ Context Request
→ Context Bundle
```

`SKL-ASSEMBLE-CONTEXT` may invoke/use this interface.

The Skill does not own retrieval/freshness/budget/memory semantics.

## 8. Workflow Stage interface

UPOS-004 owns when the Stage runs.

UPOS-005 owns what valid Context is assembled for that Stage/consumer.

## 9. Bounded follow-up requests

An Agent/Skill MAY request additional Context when:

- the new request is bounded;
- purpose is explicit;
- scope/permissions still apply;
- added material is genuinely needed.

It MUST NOT use follow-up retrieval as unrestricted project-history access.

===== END VIRTUAL FILE: CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md =====


---

## VIRTUAL FILE 4/36 — `CONTEXT_BUNDLE_STANDARD.md`

**Virtual path:** `CONTEXT_BUNDLE_STANDARD.md`  
**Content checksum:** `8b369b48ff7d`

===== BEGIN VIRTUAL FILE: CONTEXT_BUNDLE_STANDARD.md =====
# Context Bundle Standard

**ID:** UPOS-05-CBS-001  
**Type:** CONTRACT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/CONTEXT_BUNDLE_TEMPLATE.md


## 1. Definition

A Context Bundle is an attributable, immutable assembled execution snapshot satisfying a concrete Context Request to the extent reported by its validity state.

Every production Bundle MUST have stable:

```text
context_bundle_id
```

## 2. Minimum contract

A production Bundle MUST include or explicitly mark non-applicable:

```text
context_bundle_id
context_request_id

project_id_ref
task_id
routing_decision_id
workflow_instance_id
stage_id

role_id
agent_definition_id
agent_definition_version
agent_run_id

skill_id
skill_version
skill_invocation_ref

purpose

context_policy_ref
context_policy_version
assembly_policy_ref where separately configured
assembly_policy_version where separately configured

assembled_at

source_resolution_refs

validity_state
required_sources_satisfied

context_items
context_manifest

open_conflicts
open_unknowns

budget_accounting

supersedes_context_bundle_id if rebuilt
reassembly_reason if rebuilt
```

## 3. Context Item

Each meaningful Context Item MUST preserve:

```text
bundle_local_item_key
source_ref
source_class
source_version_or_revision
canonical_owner_ref where applicable
source_status/lifecycle reference
epistemic_class_ref
representation_type
derived_from if derived
freshness_assessment
inclusion_reason
priority
required_or_optional
permission_transformation_ref where applicable
```

`bundle_local_item_key` is addressable inside the Bundle but is not a new global identity.

## 4. Representation types

Canonical v1 representation types:

```text
EXACT
EXCERPT
DERIVED_SUMMARY
REFERENCE_ONLY
```

Their safety rules are defined in `CONTEXT_BUDGET_AND_REPRESENTATION.md`.

## 5. Context Manifest

Every production Bundle MUST include a Manifest sufficient to answer:

```text
what was required?
what was found?
what was included?
what was excluded?
why?
what was summarized?
from which source/version?
were all required sources satisfied?
what conflicts/unknowns remain?
what budget was available/consumed?
```

## 6. Required-source satisfaction

Bundle MUST explicitly report:

```text
required_sources_satisfied = true / false
```

Consumers MUST NOT infer completeness from item count.

## 7. Exclusion reasons

Canonical v1 exclusion vocabulary:

```text
OUT_OF_SCOPE
SUPERSEDED
RETIRED
STALE
PERMISSION_DENIED
BUDGET_OMITTED_OPTIONAL
LOW_RELEVANCE_OPTIONAL
WRONG_VERSION
WRONG_PROJECT
CONFLICTING_SOURCE
DUPLICATE
NOT_APPLICABLE_TO_STAGE
PROVENANCE_INSUFFICIENT
```

An exclusion reason does not redefine upstream source lifecycle or permission semantics.

## 8. Bundle immutability

Once a production Bundle is SEALED/consumed, its content MUST NOT be silently mutated.

If material source/context conditions change:

```text
CB-102
→ stale / invalidated for active use
→ reassembly
→ CB-103
→ supersedes_context_bundle_id = CB-102
```

The original consumed snapshot remains auditable.

## 9. Validity is separate from identity

Bundle identity does not change when a later assessment marks the immutable snapshot stale or invalidated.

Validity semantics are defined separately.

## 10. Context Bundle != prompt

A provider-specific prompt may be generated from a Bundle.

Prompt construction/formatting is runtime/adapter behavior and MUST NOT redefine Bundle semantics.
===== END VIRTUAL FILE: CONTEXT_BUNDLE_STANDARD.md =====


---

## VIRTUAL FILE 5/36 — `SOURCE_RESOLUTION_INTERFACE.md`

**Virtual path:** `SOURCE_RESOLUTION_INTERFACE.md`  
**Content checksum:** `4c5b08e1b212`

===== BEGIN VIRTUAL FILE: SOURCE_RESOLUTION_INTERFACE.md =====

# Source Resolution Interface

**ID:** UPOS-05-SRI-001  
**Type:** UPSTREAM INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01 Source-of-Truth Model


## 1. Ownership boundary

UPOS-005 consumes UPOS-01 source resolution.

It MUST NOT decide by itself:

- who owns a fact;
- which source is canonical;
- which normative source wins;
- whether knowledge is promoted;
- whether a conflict is resolved.

## 2. Required conceptual flow

```text
Context Request
↓
resolve_scope(task / requested fact scope)
↓
resolve_canonical_owner(scope)
↓
resolve_active_canonical_sources(owner, request)
↓
resolve relevant accepted decisions/refinements
↓
check baseline/version applicability
↓
UPOS-005 retrieval/eligibility/assembly
```

## 3. UPOS-01 algorithm consumed

Module 05 must preserve the upstream logic:

```text
fact scope
→ canonical owner
→ ACTIVE normative sources
→ relevant accepted decisions
→ valid local refinement
→ version/baseline applicability
→ implementation evidence
→ conflict / UNKNOWN when unresolved
```

## 4. Source resolution output expectations

UPOS-005 expects resolution references sufficient to identify:

```text
fact_scope
canonical_owner_ref
canonical_source_refs
source status/normativity
decision/refinement refs
version/baseline applicability
known conflict status
known UNKNOWN / OWNER DECISION REQUIRED status
```

Exact machine structure is cross-cutting schemas/runtime.

## 5. Missing owner/source

If UPOS-01 reports no canonical owner/source:

```text
do not infer truth
do not promote nearest note
do not treat implementation as intended policy
```

Module 05 emits a Context failure/result that UPOS-004 can route.

## 6. Canonical conflict

If active normative sources conflict, Module 05 MUST NOT:

- average them;
- vote between them;
- pick newest blindly;
- choose highest embedding similarity;
- synthesize a compromise as truth.

Result is a Context conflict condition.

Truth resolution remains with UPOS-01/owner.

## 7. Implementation evidence

Implementation/code/tests/runtime artifacts may show what currently happens.

They remain implementation evidence and MUST NOT silently override confirmed normative sources.

Drift should remain visible.

## 8. Historical material

Historical/superseded/retired material MAY be included for explicit historical relevance only.

Its status MUST remain visible in Context.

## 9. Source not found vs source does not exist

```text
SOURCE_NOT_FOUND
= retrieval/resolution attempt did not locate expected material

SOURCE_DOES_NOT_EXIST
= absence has been established by canonical governance/owner resolution
```

Retrieval failure is not proof of nonexistence.

===== END VIRTUAL FILE: SOURCE_RESOLUTION_INTERFACE.md =====


---

## VIRTUAL FILE 6/36 — `RETRIEVAL_AND_SELECTION_STANDARD.md`

**Virtual path:** `RETRIEVAL_AND_SELECTION_STANDARD.md`  
**Content checksum:** `463c4ef33af0`

===== BEGIN VIRTUAL FILE: RETRIEVAL_AND_SELECTION_STANDARD.md =====

# Retrieval & Selection Standard

**ID:** UPOS-05-RSS-001  
**Type:** RETRIEVAL STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** SOURCE_RESOLUTION_INTERFACE.md


## 1. Retrieval Candidate

A Retrieval Candidate is discovered information that has not yet been admitted to Context.

Candidate attributes SHOULD include:

```text
source_ref
source_class
canonical_owner_ref
normativity/status
source_version_or_revision
version_applicability
scope_applicability
project_applicability
freshness
permission_eligibility
epistemic_class_ref
relevance
representation_possibilities
provenance_sufficiency
```

## 2. Authority-aware order

Retrieval MUST NOT be pure semantic similarity search.

Conceptual order:

```text
1. bounded request and scope
2. UPOS-01 canonical owner/source resolution
3. UPOS-010 permission/security constraints
4. UPOS-011 physical retrieval/provider mapping
5. project/scope/version/lifecycle eligibility
6. freshness/applicability assessment
7. epistemic/normativity preservation
8. relevance ranking among eligible candidates
9. required/optional obligation handling
10. budget/representation optimization
```

Invariant:

```text
HIGH RELEVANCE
MUST NOT OVERRIDE
LOWER AUTHORITY
```

## 3. Source eligibility gate

Candidate may be ineligible due to:

```text
wrong project
wrong scope
wrong version/baseline
superseded/retired status
permission denied
stale beyond applicable policy
canonical conflict
not applicable to current Stage/Role/Skill
insufficient provenance
```

Ineligible material MUST NOT silently enter Context because search returned it.

## 4. Relevance ranking

Relevance is applied only inside an eligible authority envelope.

Relevance MAY consider:

- direct Task/Stage/Skill relation;
- affected domain/component;
- decision applicability;
- implementation surface;
- evidence recency where applicable;
- historical similarity when explicitly useful.

It MUST NOT convert a lower-authority candidate into normative truth.

## 5. Knowledge retrieval priority consumed from UPOS-01

Default background order:

```text
1. Active canonical sources
2. Accepted relevant decisions
3. Validated active learnings
4. Current plan
5. Recent relevant evidence
6. Historical material
7. Raw/unreviewed notes
```

This order is not a substitute for fact-scope ownership or Context requiredness.

## 6. Incremental / just-in-time retrieval

UPOS-005 supports:

```text
initial minimal Bundle
+
bounded follow-up Context Request
```

Do not front-load an entire repository merely because it is accessible.

## 7. Explainability

For a material inclusion/exclusion, the system SHOULD be able to explain:

- why source was eligible;
- why included;
- why excluded;
- why representation was summary/reference/excerpt;
- why historical material was used;
- why Bundle was rebuilt.

Opaque similarity rank alone is insufficient.

## 8. Provider retrieval failure

Provider/search failure MUST be surfaced as technical retrieval failure.

It MUST NOT be interpreted as proof that project knowledge does not exist.

===== END VIRTUAL FILE: RETRIEVAL_AND_SELECTION_STANDARD.md =====


---

## VIRTUAL FILE 7/36 — `CONTEXT_ASSEMBLY_STANDARD.md`

**Virtual path:** `CONTEXT_ASSEMBLY_STANDARD.md`  
**Content checksum:** `4bfd9a3826a9`

===== BEGIN VIRTUAL FILE: CONTEXT_ASSEMBLY_STANDARD.md =====

# Context Assembly Standard

**ID:** UPOS-05-CAS-001  
**Type:** ASSEMBLY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** CONTEXT_BUNDLE_STANDARD.md, CONTEXT_ISOLATION_AND_VIEWS.md


## 1. Assembly sequence

```text
1. validate bounded Context Request
2. resolve canonical owner/source universe through UPOS-01
3. apply permission/security constraints
4. retrieve physical candidates via abstract provider interface
5. apply project/scope/version/lifecycle eligibility
6. evaluate freshness/applicability
7. preserve epistemic/source labels
8. satisfy required sources
9. rank optional/supporting candidates
10. choose safe representation
11. fit Context Budget
12. build Context View for consumer
13. build Context Manifest
14. seal immutable Context Bundle
```

## 2. Assembly order from frozen master

The frozen sequence:

```text
task / issue
project manifest
relevant source of truth
relevant specification
relevant decisions
relevant implementation
relevant tests
current plan
```

is preserved as a useful assembly heuristic but is subordinate to UPOS-01 ownership, concrete Context Requirements, permissions, and current applicability.

## 3. Epistemic class preservation

Context MUST preserve UPOS-01 knowledge classes where applicable:

```text
Signal
Observation
Evidence
Hypothesis
Proposal
Decision
Canonical knowledge
Learning
Historical knowledge
```

Other artifacts such as Review Findings may retain artifact subtype without inventing a competing truth hierarchy.

## 4. Context contamination guard

Assembly MUST guard against:

- unverified Agent speculation presented as fact;
- stale summary presented as current source;
- wrong-project material;
- wrong-version design/spec;
- Implementer justification treated as independent Reviewer evidence;
- historical/superseded decision treated as active;
- private model memory used as project truth;
- implementation evidence silently overriding normative source.

## 5. Context Manifest

Manifest is mandatory for production Bundles and records requirement satisfaction, source resolution refs, included items, exclusions/reasons, representations, freshness, budget, conflicts and unknowns.

## 6. Skill interface

`SKL-ASSEMBLE-CONTEXT` is an UPOS-003 `INTERFACE_SKILL`.

Formal separation:

```text
SKL-ASSEMBLE-CONTEXT
= bounded Skill-level capability to request/use Context assembly

UPOS-005
= canonical retrieval/resolution/budget/freshness/memory/assembly semantics
```

## 7. Workflow Stage interface

A Stage can declare Context needs.

UPOS-004 owns stage timing/order.

UPOS-005 resolves what Context the bounded Stage consumer receives.

## 8. Rework Context

On rework/re-review, original Bundle MUST be revalidated against:

```text
new finding
changed artifact
changed canonical source
new decision
new scope
new Change Class/Profile/route
permission changes
```

Reuse is allowed only if validity remains demonstrated.

## 9. Human decision package

When a Workflow requires Human Governance, Module 05 MAY assemble focused Context containing:

- decision needed;
- scope;
- canonical sources;
- options/proposals;
- evidence;
- risks;
- conflicts/unknowns;
- affected artifacts;
- prior decisions.

Human authority remains external.

## 10. No context dumping

`all docs → all agents` is an anti-pattern.

Assembly SHOULD terminate when minimum sufficient context is reached.

===== END VIRTUAL FILE: CONTEXT_ASSEMBLY_STANDARD.md =====


---

## VIRTUAL FILE 8/36 — `CONTEXT_BUDGET_AND_REPRESENTATION.md`

**Virtual path:** `CONTEXT_BUDGET_AND_REPRESENTATION.md`  
**Content checksum:** `1ec3a56848dd`

===== BEGIN VIRTUAL FILE: CONTEXT_BUDGET_AND_REPRESENTATION.md =====

# Context Budget & Representation

**ID:** UPOS-05-CBR-001  
**Type:** BUDGET / REPRESENTATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Context Budget

Context Budget is the bounded capacity available for one Context View/Bundle.

Budget semantics may consider:

```text
consumer Role
Stage
Skill
Task complexity
Change Class
required source size
optional evidence
model/provider capacity interface
cost/latency constraints
```

Concrete provider token limits/costs belong to UPOS-011/008.

## 2. Minimum sufficient principle

```text
maximum available context != optimal context
```

Budget optimization MUST prefer the smallest set that safely satisfies required information needs.

## 3. Required material is non-droppable

A required authoritative source/constraint MUST NOT be silently omitted because of budget.

When it cannot fit safely:

```text
safe summary/excerpt if permitted
incremental/staged retrieval
split execution
request larger-capability provider through external adapter
block / emit BUDGET_INSUFFICIENT
```

Arbitrary tail truncation is prohibited.

## 4. Priority levels

Priority is separate from requiredness.

Canonical v1 priority labels:

```text
P0_CONSTRAINT
= mandatory authoritative constraints/invariants

P1_DIRECT
= direct Task/Stage/decision context

P2_SUPPORTING
= supporting evidence/implementation/tests needed for the purpose

P3_HISTORICAL
= relevant historical/background context

P4_ENRICHMENT
= optional enrichment
```

Budget pressure removes/condenses the lowest-value optional material first.

## 5. Representation classes

### EXACT
Full exact content when wording/structure itself is needed.

### EXCERPT
Verbatim bounded subset retaining exact source reference/location.

### DERIVED_SUMMARY
Derived compression preserving provenance and explicitly noncanonical status.

### REFERENCE_ONLY
Pointer/reference when content need not be embedded or when policy requires restricted representation.

## 6. Exact/excerpt preference

Exact or tightly traceable excerpt SHOULD be preferred where semantic drift would be dangerous, including where applicable:

- canonical invariants;
- exact API/data/security contracts;
- lifecycle/state transitions;
- decision constraints;
- acceptance criteria whose wording materially affects interpretation.

## 7. Summary safety

Every `DERIVED_SUMMARY` MUST:

```text
be labeled derived
retain source_ref
retain source version/revision
retain derivation relationship
state material limitations where needed
be invalidated/revalidated when assumptions/source version change
```

A model-generated summary is never canonical merely because its source was canonical.

## 8. Sensitive minimization

When UPOS-010 returns sensitivity constraints, representation may use:

- minimum necessary excerpt;
- redacted representation;
- reference-only representation;
- Role-scoped isolation.

Module 05 applies constraints but does not define who is permitted.

## 9. Budget accounting

Bundle Manifest SHOULD report factual accounting:

```text
budget_limit_or_reference
budget_consumed
required_material_count/size
optional_material_count/size
summarized_material
omitted_optional_material
overflow_condition if any
```

Cost metrics/aggregation remain UPOS-008.

===== END VIRTUAL FILE: CONTEXT_BUDGET_AND_REPRESENTATION.md =====


---

## VIRTUAL FILE 9/36 — `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md`

**Virtual path:** `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md`  
**Content checksum:** `28bf5bcba24e`

===== BEGIN VIRTUAL FILE: FRESHNESS_INVALIDATION_AND_REASSEMBLY.md =====

# Freshness, Invalidation & Reassembly

**ID:** UPOS-05-FIR-001  
**Type:** FRESHNESS / INVALIDATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Freshness != canonicality

A source may be:

- authoritative but stale for this execution;
- relevant but superseded;
- historical and valid as history;
- recent but noncanonical/incorrect.

UPOS-005 consumes source lifecycle/status from UPOS-01 and derives execution applicability.

## 2. Freshness assessment

Freshness evaluation may consider:

```text
source lifecycle/status
source version/revision
baseline applicability
time-sensitive TTL supplied by policy
Task/Workflow changes
known canonical revision
upstream artifact replacement
```

Module 05 MUST NOT invent upstream lifecycle status.

## 3. Bundle validity states

Canonical Context Bundle validity states:

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
STALE
INVALIDATED
```

### VALID
Required sources satisfied, no blocking conflict, current for request.

### VALID_WITH_WARNINGS
Required sources satisfied; non-blocking optional/history/representation warning exists.

### INCOMPLETE
One or more required requirements are unsatisfied. Bundle may exist for diagnosis but MUST NOT be presented as fully valid execution context.

### STALE
Previously valid Bundle has detected freshness/assumption change and requires revalidation before continued material use.

### INVALIDATED
Bundle is no longer acceptable for active execution under the request because a material assumption/source/permission/route changed or contamination was discovered.

`BLOCKED` is an assembly/request outcome, not a Bundle content state.

## 4. Invalidation/revalidation triggers

Where applicable:

```text
canonical source version/revision changes
canonical owner changes
source becomes superseded/retired
normative conflict appears
Task scope changes
Workflow reclassification
Workflow rerouting
Stage materially changes
Skill version changes
Role changes
permission/security constraints change
time-sensitive source expires
upstream artifact replaced
material source changes during Agent Run
```

## 5. Reclassification/rerouting interface

Example:

```text
C1 Bug Fix
→ CB-100

database migration discovered
→ UPOS-004 reclassifies/reroutes
→ DATABASE_MIGRATION profile added
→ CB-100 revalidation fails
→ CB-101 assembled
→ CB-101 supersedes CB-100
```

Module 05 reports Context validity/reassembly result.

UPOS-004 decides orchestration response.

## 6. Reassembly

Reassembly creates a new `context_bundle_id`.

It MUST NOT mutate the old consumed Bundle.

## 7. Context Delta

A reassembly MAY include a Context Delta report:

```text
prior_context_bundle_id
new_context_bundle_id
reassembly_reason
changed_requirements
changed_source_versions
reused items
replaced items
removed items
new items
changed exclusions/conflicts
```

Context Delta is an audit/reassembly artifact, not a mutable Context object or new Source of Truth.

## 8. Source changes during an Agent Run

If a material required source changes during execution:

```text
mark Bundle STALE / INVALIDATED as appropriate
→ notify Workflow interface
→ revalidate/reassemble
```

Agent MUST NOT silently finish high-impact execution using invalidated critical Context.

Exact pause/restart/retry action remains UPOS-004.

## 9. Reuse

Before reusing a prior Bundle/Item/Memory:

```text
check project/scope
check source version
check provenance
check freshness
check permissions
check role/independence
check current applicability
```

No blind nearest-memory reuse.

===== END VIRTUAL FILE: FRESHNESS_INVALIDATION_AND_REASSEMBLY.md =====


---

## VIRTUAL FILE 10/36 — `CONTEXT_ISOLATION_AND_VIEWS.md`

**Virtual path:** `CONTEXT_ISOLATION_AND_VIEWS.md`  
**Content checksum:** `e7ca4af10cbc`

===== BEGIN VIRTUAL FILE: CONTEXT_ISOLATION_AND_VIEWS.md =====

# Context Isolation & Views

**ID:** UPOS-05-CIV-001  
**Type:** ISOLATION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-002 Agent Organization


## 1. Context View

A Context View is a bounded projection of eligible Context for one consumer/purpose.

A View may differ by:

```text
Role
authority scope reference
Workflow Stage
Skill
Agent Run
permissions
independence constraints
Change Class / Concern
```

Seeing information never grants authority over its fact scope.

## 2. Role-aware examples

### Product
Intent, requirements, constraints, relevant evidence/decisions.

### Architecture
Product intent + Domain contracts + current architecture + relevant decisions/evidence.

### Implementer
Approved plan + applicable contracts + implementation surface + tests.

### Reviewer
Authoritative requirements/contracts + diff + relevant tests/evidence + decisions.

### QA
Expected behavior + acceptance/risk scenarios + testable change, not merely producer narrative.

### Merge Controller
Structured gate/readiness evidence, not full implementation reasoning.

### Human decision-maker
Focused decision packet with canonical sources/options/evidence/risks/conflicts.

## 3. Reviewer independence

Critical invariant:

```text
producer context
!= reviewer authoritative context
```

Reviewer MUST NOT automatically inherit:

- Implementer scratch reasoning;
- private chain-of-thought;
- unverified assumptions;
- self-approval claims;
- producer-only Run Working Memory.

Reviewer independently receives required authoritative sources.

Producer notes MAY be included only when explicitly relevant and labeled as producer-provided, non-independent material.

## 4. Same underlying model/provider

The same base model/provider may power different Roles only when UPOS-002 logical separation is preserved.

Module 05 supports this by keeping Context Requests/Bundles and working memory scoped separately per Role/Run.

## 5. QA independence

QA SHOULD begin from expected behavior/contracts and risks.

Implementation details can be supplemental, not the sole basis of the QA View.

## 6. Cross-project isolation

Default invariant:

```text
Project A Context
MUST NOT leak into
Project B Context
```

Cross-project/federated knowledge requires an explicit authorized mechanism.

Project identity/mappings remain UPOS-011; access grants remain UPOS-010.

## 7. Cross-task isolation

Task Working Memory from Task A MUST NOT automatically become Context for Task B.

Permitted reuse requires one of:

- governed canonical project knowledge;
- explicit governed reusable artifact;
- validated historical evidence relevant to current scope;
- explicit authorized source reference.

## 8. Sensitive Context isolation

UPOS-005 applies minimum-necessary inclusion/redaction/reference-only constraints returned by UPOS-010.

It does not define access policy.

## 9. Context contamination detection

Detected wrong-project/wrong-version/private-memory/producer-bias contamination makes affected material ineligible and may invalidate the Bundle.

===== END VIRTUAL FILE: CONTEXT_ISOLATION_AND_VIEWS.md =====


---

## VIRTUAL FILE 11/36 — `CONTEXT_FAILURE_MODEL.md`

**Virtual path:** `CONTEXT_FAILURE_MODEL.md`  
**Content checksum:** `b010b2861462`

===== BEGIN VIRTUAL FILE: CONTEXT_FAILURE_MODEL.md =====

# Context Failure Model

**ID:** UPOS-05-CFM-001  
**Type:** FAILURE / RESULT STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-004 Workflow Engine


## 1. Boundary

UPOS-005 emits Context result/failure semantics.

UPOS-004 owns the orchestration response.

Example:

```text
UPOS-005:
MISSING_REQUIRED_SOURCE — Architecture Contract unresolved

UPOS-004:
block Stage / escalate / request owner decision
```

## 2. Failure taxonomy

| Failure | Context meaning | Executable Bundle? | Degraded/diagnostic Bundle? | Required external interface |
|---|---|---|---|---|
| `MISSING_REQUIRED_SOURCE` | required source class/material is unsatisfied | no | yes, `INCOMPLETE` | UPOS-01 owner resolution + UPOS-004 |
| `SOURCE_RESOLUTION_FAILURE` | canonical scope/owner/source resolution could not complete | no | diagnostic only | UPOS-01 / UPOS-011 |
| `CANONICAL_CONFLICT` | active authoritative sources conflict | no | yes, conflict-labeled | UPOS-01 + UPOS-004 |
| `STALE_REQUIRED_CONTEXT` | required material is stale/not applicable enough for current execution | no until revalidated | yes, `STALE` | freshness/reassembly + UPOS-004 |
| `PERMISSION_BLOCKED` | required material cannot be delivered under current access constraints | no | metadata-only diagnostic if allowed | UPOS-010 + UPOS-004 |
| `BUDGET_INSUFFICIENT` | required material cannot be represented safely within budget | no | yes for diagnosis | budget response + UPOS-004/011 |
| `REPRESENTATION_UNSAFE` | no safe representation satisfies semantic/security need | no | possibly metadata-only | UPOS-010/004 |
| `PROVENANCE_MISSING` | candidate lacks provenance needed for trusted inclusion | no if required; optional excluded otherwise | yes if required gap exposed | UPOS-01/011 |
| `CROSS_SCOPE_CONTAMINATION` | material from wrong project/task/version/role boundary entered candidate/Bundle | no until rebuilt | invalidated snapshot retained for audit | isolation + UPOS-004 |
| `INVALID_MEMORY_REUSE` | stale/out-of-scope/noncanonical memory was proposed for reuse | exclude memory; Bundle depends on remaining context | yes if requirements still satisfied | memory policy + UPOS-004 if blocking |
| `PROVIDER_RETRIEVAL_FAILURE` | physical retrieval/search provider failed | unknown; must not infer absence | diagnostic | UPOS-011/runtime + UPOS-004 if blocking |

## 3. Source lookup outcomes

`SOURCE_NOT_FOUND` is a retrieval outcome and may lead to `MISSING_REQUIRED_SOURCE`.

It MUST NOT be equated with `SOURCE_DOES_NOT_EXIST` without upstream governance evidence.

## 4. Degraded Context rule

A Bundle may be `VALID_WITH_WARNINGS` only when all required source requirements remain satisfied and no blocking conflict exists.

Optional source omission may be a warning.

Missing required authoritative source cannot be represented as `VALID`.

## 5. Context health signals

Factual non-metric health signals include:

```text
required_sources_satisfied
canonical_conflict_present
stale_required_source
unknown_source_version
budget_overflow
summary_used
context_rebuilt
unauthorized_source_excluded
cross_project_leak_detected
missing_provenance
permission_transformation_applied
```

UPOS-008 may later measure/aggregate them.

## 6. Failure result explainability

A Context failure/result SHOULD identify:

```text
context_request_id
failure class
affected requirement/source class
relevant source/provider/permission refs
why executable Bundle could/could not be produced
recommended external interface to invoke
```

It MUST NOT prescribe Workflow transition semantics beyond returning the condition.

===== END VIRTUAL FILE: CONTEXT_FAILURE_MODEL.md =====


---

## VIRTUAL FILE 12/36 — `MEMORY_TAXONOMY.md`

**Virtual path:** `MEMORY_TAXONOMY.md`  
**Content checksum:** `9d5cab48ac50`

===== BEGIN VIRTUAL FILE: MEMORY_TAXONOMY.md =====

# Memory Taxonomy

**ID:** UPOS-05-MTX-001  
**Type:** MEMORY TAXONOMY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Critical invariant

```text
MEMORY != TRUTH
```

Persistence, retrieval frequency, model confidence, or embedding similarity do not create canonicality.

## 2. RUN_WORKING_MEMORY

```text
RUN_WORKING_MEMORY
= ephemeral noncanonical execution support
  scoped to one Agent Run
```

May include:

- temporary notes;
- intermediate calculations;
- retrieval pointers;
- partial working artifacts.

Default: not persisted after the Run unless explicit policy requires retention.

## 3. TASK_WORKING_MEMORY

```text
TASK_WORKING_MEMORY
= bounded noncanonical operational memory
  retained across multiple Runs/Stages
  for one Task
```

May include:

- unresolved working questions;
- temporary artifact references;
- coordination notes;
- temporary mappings.

It MUST NOT duplicate UPOS-004 Workflow state.

## 4. RETRIEVAL_CACHE

```text
RETRIEVAL_CACHE
= optimization for previously retrieved/resolved information
```

Invariant:

```text
CACHE HAS ZERO ADDITIONAL AUTHORITY
```

Cache entries remain tied to source identity/version/scope/freshness and permission eligibility.

## 5. GOVERNED_PROJECT_MEMORY_VIEW

```text
GOVERNED_PROJECT_MEMORY_VIEW
= Context/Retrieval interface over knowledge governed by UPOS-01
```

It is not an independent Module-05 truth database.

Durable project truth remains in UPOS-01 governed sources.

## 6. Raw conversation history

```text
raw chat history != Project Memory
```

Conversation can contain Signal/Observation/Evidence/Hypothesis/Proposal candidates.

Durable truth requires governed capture/resolution/promotion.

## 7. Provider/model memory

```text
provider private memory
model latent memory
conversation personalization memory
```

MUST NOT be treated as canonical U-POS project knowledge.

If useful information exists only there:

```text
surface as candidate
→ verify
→ resolve canonical owner
→ govern through UPOS-01
```

## 8. No generic permanent memory bucket

UPOS-005 v1 intentionally rejects an undifferentiated persistent `memory` bucket.

===== END VIRTUAL FILE: MEMORY_TAXONOMY.md =====


---

## VIRTUAL FILE 13/36 — `MEMORY_READ_WRITE_STANDARD.md`

**Virtual path:** `MEMORY_READ_WRITE_STANDARD.md`  
**Content checksum:** `1ce92314a49c`

===== BEGIN VIRTUAL FILE: MEMORY_READ_WRITE_STANDARD.md =====
# Memory Read / Write Standard

**ID:** UPOS-05-MRW-001  
**Type:** MEMORY ACCESS STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/MEMORY_ITEM_TEMPLATE.md


## 1. Stable identity

Every persisted Module-05 memory item MUST have:

```text
memory_item_id
```

## 2. Persisted memory write contract

Every write MUST specify:

```text
memory_item_id
memory_class

project_id_ref
scope_refs
task_id and/or agent_run_id as applicable

producer_role_ref
producer_agent_run_ref

provenance
source_refs
created_from_refs

epistemic_class_ref
representation_content_type
content_or_artifact_ref

created_at
lifetime_class
expiration_or_review_trigger if applicable
invalidation_conditions

permission_security_constraint_refs where applicable

memory_state

canonicality = false
```

Exception: `GOVERNED_PROJECT_MEMORY_VIEW` is not written as a new canonical memory item; it references UPOS-01 governed knowledge.

## 3. Epistemic status

Memory SHOULD preserve UPOS-01 epistemic classes rather than invent a competing truth taxonomy.

Working status/lifetime is separate from epistemic class.

## 4. Read eligibility

Before a memory item can affect Context, check:

```text
project scope
Task/Run scope
provenance
source relationship
freshness/state
permission eligibility
current applicability
Role/independence constraints
```

## 5. Run Working Memory read/write

Run memory is private to the bounded Agent Run by default.

It MUST NOT automatically flow into another Role/Run.

## 6. Task Working Memory read/write

Task memory may be shared only inside the same Task according to Role/permission/independence constraints.

It MUST NOT become cross-task knowledge by persistence alone.

## 7. Cross-task reuse

Cross-task reuse requires governed reusable source/evidence or explicit authorized reference and a new applicability/freshness check.

## 8. Memory promotion boundary

Memory does not promote itself.

```text
Run/Task memory observation
→ candidate artifact/proposal/evidence
→ UPOS-01 Knowledge Lifecycle and/or UPOS-009
→ review/validation/promotion
→ new canonical source if approved
→ Module 05 may retrieve it later
```

`memory_item.status = permanent` would not create canonicality and is not a valid promotion mechanism.

## 9. Private reasoning

Module-05 workflows MUST NOT depend on storing hidden model chain-of-thought.

Store attributable artifacts, evidence, decisions, concise rationale, and explicit working notes where needed.
===== END VIRTUAL FILE: MEMORY_READ_WRITE_STANDARD.md =====


---

## VIRTUAL FILE 14/36 — `MEMORY_LIFECYCLE_AND_INVALIDATION.md`

**Virtual path:** `MEMORY_LIFECYCLE_AND_INVALIDATION.md`  
**Content checksum:** `2fbdce7df010`

===== BEGIN VIRTUAL FILE: MEMORY_LIFECYCLE_AND_INVALIDATION.md =====

# Memory Lifecycle & Invalidation

**ID:** UPOS-05-MLI-001  
**Type:** MEMORY LIFECYCLE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Memory item states

Canonical execution-support states:

```text
ACTIVE
STALE
EXPIRED
INVALIDATED
ARCHIVED
```

These states are not UPOS-01 Knowledge Lifecycle states.

## 2. Lifetime classes

Canonical semantic lifetime classes:

```text
RUN
TASK
TTL_BOUND
UNTIL_INVALIDATED
GOVERNED_REFERENCE
```

Actual data retention/security deletion requirements remain external.

## 3. RUN lifetime

Valid only for the originating Agent Run unless explicitly captured/promoted through governed interfaces.

## 4. TASK lifetime

Valid only inside the originating Task subject to freshness/scope/permission rules.

At Task completion, active reuse ends. Retention may archive or expire according to policy.

## 5. TTL_BOUND

Validity expires at an externally configured time/condition.

Expiry is not proof the underlying project fact is false.

## 6. UNTIL_INVALIDATED

May remain active until a declared invalidation trigger occurs.

No indefinite authority is implied.

## 7. GOVERNED_REFERENCE

Pointer/view relationship to UPOS-01 governed knowledge.

The referenced source lifecycle governs knowledge validity; Module-05 memory state only governs the reference/view usability.

## 8. Invalidation triggers

Memory becomes stale/expired/invalidated where applicable when:

- underlying source is superseded/retired/revised;
- Task/Run scope ends;
- Task scope materially changes;
- assumption is invalidated;
- Workflow reroutes/reclassifies materially;
- permission eligibility changes;
- TTL expires;
- canonical conflict appears;
- project/baseline/version applicability changes.

## 9. Invalidated memory

May remain historically attributable when allowed, but MUST NOT silently feed active Context.

## 10. Retrieval Cache invalidation

Cache must invalidate/revalidate against source version, scope, freshness and permission changes.

A cached copy MUST NOT override current source resolution.

===== END VIRTUAL FILE: MEMORY_LIFECYCLE_AND_INVALIDATION.md =====


---

## VIRTUAL FILE 15/36 — `PROJECT_MEMORY_INTERFACE.md`

**Virtual path:** `PROJECT_MEMORY_INTERFACE.md`  
**Content checksum:** `d913671da058`

===== BEGIN VIRTUAL FILE: PROJECT_MEMORY_INTERFACE.md =====

# Governed Project Memory Interface

**ID:** UPOS-05-PMI-001  
**Type:** PROJECT MEMORY INTERFACE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** UPOS-01 Knowledge Lifecycle


## 1. Architectural rule

UPOS-005 MUST NOT create:

```text
project_memory_database
```

as an independent semantic Source of Truth.

Instead:

```text
GOVERNED_PROJECT_MEMORY_VIEW
= retrieval/context interface over UPOS-01 governed knowledge
```

## 2. Preferred durable project memory inputs

Consumed from UPOS-01 governed knowledge:

- Product Principles / Product contracts;
- Domain Model / invariants;
- Architecture contracts;
- Feature Specs;
- accepted ADR/PDR/DDR/etc.;
- Engineering Standards;
- Design System contracts;
- validated tests/evidence where appropriate;
- Runbooks;
- promoted Learnings;
- Postmortems/historical knowledge.

Their canonicality/lifecycle remains upstream.

## 3. Low-authority/history inputs

Raw brainstorming, unreviewed AI notes, old chats, rejected proposals, scratch plans may be retrieved only for explicit relevance and MUST remain clearly noncanonical/historical/proposal-class material.

## 4. Promotion

Module 05 may surface a candidate from Memory.

It cannot promote it.

Promotion remains:

```text
candidate
→ UPOS-01 / UPOS-009
→ review / validation
→ canonical owner/source update if approved
```

## 5. Knowledge change propagation

When upstream governed knowledge changes, Module 05 must invalidate/revalidate affected Context Bundles, Context Views, Memory references, and Retrieval Cache entries according to policy.

## 6. No hidden conversation dependency

A project is not considered to "know" something merely because an Agent/provider remembers a past conversation.

A durable fact must resolve to governed project knowledge or be treated as an unverified candidate.

===== END VIRTUAL FILE: PROJECT_MEMORY_INTERFACE.md =====


---

## VIRTUAL FILE 16/36 — `CONTEXT_MEMORY_LIFECYCLE.md`

**Virtual path:** `CONTEXT_MEMORY_LIFECYCLE.md`  
**Content checksum:** `f1736cee2655`

===== BEGIN VIRTUAL FILE: CONTEXT_MEMORY_LIFECYCLE.md =====

# Context & Memory Lifecycle

**ID:** UPOS-05-CML-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Context Request lifecycle

Semantic request states:

```text
OPEN
RESOLVING
RETRIEVING
ASSEMBLING
FULFILLED
BLOCKED
FAILED
CANCELLED
```

These states describe Context assembly, not Workflow state.

## 2. Context Bundle lifecycle

Bundle content lifecycle:

```text
ASSEMBLING
→ SEALED
→ CONSUMED
→ HISTORICAL
```

This is distinct from validity:

```text
VALID
VALID_WITH_WARNINGS
INCOMPLETE
STALE
INVALIDATED
```

## 3. Immutability

After `SEALED`, Bundle payload is immutable for provenance.

Validity assessments may evolve without rewriting the payload.

Reassembly produces a new Bundle identity.

## 4. Context Bundle identity vs version

A Context Bundle is not semver-versioned.

```text
new assembly/reassembly
→ new context_bundle_id
```

Normative Module-05 contracts themselves use governed document versions.

## 5. Context policy version

`context_policy_version` is recorded on Request/Bundle and may change independently from source versions.

A policy change MAY trigger reassembly where material.

## 6. Memory lifecycle

Memory item lifecycle is defined in `MEMORY_LIFECYCLE_AND_INVALIDATION.md`.

It MUST NOT be confused with UPOS-01 Knowledge Lifecycle.

## 7. Replay/audit support

The system must preserve enough semantic references to reconstruct:

```text
Task
Workflow Instance
Stage
Role / Agent Run
Skill Invocation
Context Request
Context Bundle
source versions
memory items that affected execution
output reference
```

Event Store/trace implementation remains UPOS-008/runtime.

===== END VIRTUAL FILE: CONTEXT_MEMORY_LIFECYCLE.md =====


---

## VIRTUAL FILE 17/36 — `CROSS_MODULE_INTERFACES.md`

**Virtual path:** `CROSS_MODULE_INTERFACES.md`  
**Content checksum:** `01980fce7cc8`

===== BEGIN VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====

# Module 05 Cross-Module Interfaces

**ID:** UPOS-05-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-005 provides**
- Source Class requirements/queries for execution;
- Bundle provenance/source references;
- Memory candidate/promotion inputs.

**UPOS-005 consumes**
- fact scope;
- canonical owner/source resolution;
- active normative source status;
- decisions/refinements;
- knowledge lifecycle/supersession;
- epistemic classes/provenance.

**MUST NOT redefine**
- truth, ownership, precedence, promotion, conflict resolution.

## UPOS-002 — Agent Organization

**Provides**
- Role/Run-specific Context Views;
- Context isolation supporting independent Roles.

**Consumes**
- Role identity;
- Agent Definition/version;
- Agent Run;
- authority/SoD;
- handoff/Human Governance constraints.

**MUST NOT redefine**
- authority, delegation, SoD, veto, approval.

Invariant supported:

```text
Implementer context != automatically Reviewer context
```

## UPOS-003 — Skills System

**Provides**
- resolved Context for Skill Invocation;
- follow-up bounded Context interface.

**Consumes**
- Required/Optional Source Classes;
- Required Context Interface;
- Skill identity/version.

**MUST NOT redefine**
- Skill procedure/evaluation.

## UPOS-004 — Workflow Engine

**Provides**
- Stage-aware Context Bundles;
- Context validity/invalidation/reassembly results.

**Consumes**
- task_id;
- routing_decision_id;
- workflow_instance_id;
- stage_id;
- Change Class/concerns;
- reclassification/rerouting information.

**MUST NOT redefine**
- routing, state, transitions, retry/rework/recovery sequencing.

## UPOS-006 — Engineering Governance

**Provides**
- Context requirements/references needed for engineering execution/review.

**Consumes**
- abstract repository/diff/commit/PR artifact interfaces when they exist.

**MUST NOT redefine**
- Git, branch, commit, PR, merge, worktree policy.

## UPOS-007 — Quality System

**Provides**
- independent Reviewer/QA Context Views;
- Bundle provenance usable by evidence consumers.

**Consumes**
- Quality-owned evidence/context requirements;
- finding/gate outputs only as labeled external artifacts.

**MUST NOT redefine**
- PASS/FAIL/BLOCKED, finding severity, evidence/gate semantics.

## UPOS-008 — Observability

**Provides stable semantic references**
- context_request_id;
- context_bundle_id;
- memory_item_id;
- task/workflow/stage/agent/skill refs;
- source refs/versions;
- validity/freshness states;
- budget summary;
- Context health signals.

**Consumes**
- event/trace/metric/retention semantics.

**MUST NOT redefine**
- event_id, trace_id, span_id, metric schema, dashboard, telemetry retention.

## UPOS-009 — Learning

**Provides**
- Context/Memory failure evidence and candidate inputs.

**Consumes**
- learning detection/promotion proposals affecting Context policies.

**MUST NOT redefine**
- learning promotion/evolution or silently evolve policy.

## UPOS-010 — Security & Permissions

**Provides**
- execution surface for permission-aware retrieval, minimization, redaction/reference-only/isolation.

**Consumes**
- access grants;
- sensitive/secret/protected-data policy;
- permission/security constraint decisions.

**MUST NOT redefine**
- who is allowed access or Security veto substance.

## UPOS-011 — Project Adapter

**Provides abstract requirements**
- source mapping needs;
- search/retrieval capability needs;
- storage/cache capability needs;
- model capacity interface needs.

**Consumes concrete bindings**
- physical source paths/IDs;
- search provider;
- repository/document provider;
- storage/cache backend;
- model/provider capacity;
- project-specific policy refinements.

**MUST NOT hard-code**
- provider/vendor/path choices in universal Module-05 semantics.

## Cross-cutting machine-readable schemas/runtime layer

Future machine-readable ContextRequest, ContextBundle, MemoryItem and related schemas MUST trace to these normative Markdown contracts.

Schemas/runtime MUST NOT invent independent Context/Memory semantics.

===== END VIRTUAL FILE: CROSS_MODULE_INTERFACES.md =====


---

## VIRTUAL FILE 18/36 — `MODULE_05_DEFINITION_OF_DONE.md`

**Virtual path:** `MODULE_05_DEFINITION_OF_DONE.md`  
**Content checksum:** `4606a3a81363`

===== BEGIN VIRTUAL FILE: MODULE_05_DEFINITION_OF_DONE.md =====
# Module 05 Definition of Done

**ID:** UPOS-05-DOD-001  
**Type:** DEFINITION OF DONE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


UPOS-005 v1.0 is complete when:

- [x] Context, Memory and Knowledge formally distinct
- [x] `Memory != Truth` invariant explicit
- [x] `Context != Truth` invariant explicit
- [x] Context Request model exists
- [x] Context Bundle model exists
- [x] stable Context/Memory identities exist
- [x] Context Bundle attributable to Task/Workflow/Stage/Role/Run/Skill
- [x] Context Bundle is immutable consumed snapshot
- [x] reassembly creates new Bundle identity
- [x] source resolution delegates canonical ownership to UPOS-01
- [x] retrieval is authority-aware before relevance ranking
- [x] relevance cannot override authority
- [x] required vs optional sources formally distinct
- [x] required source cannot be silently dropped due to budget
- [x] exact/excerpt/derived-summary/reference representations governed
- [x] summaries remain derived/provenance-linked
- [x] Context Budget model exists
- [x] overflow behavior controlled
- [x] just-in-time/incremental retrieval addressed
- [x] Context Views are Role/Stage/Skill aware
- [x] Reviewer independence preserved
- [x] cross-project isolation exists
- [x] cross-task memory leakage prohibited by default
- [x] freshness model exists
- [x] invalidation triggers exist
- [x] Workflow reclassification/rerouting triggers Context revalidation
- [x] Context failure taxonomy exists
- [x] Context validity states exist
- [x] Run Working Memory defined
- [x] Task Working Memory defined
- [x] Retrieval Cache defined
- [x] Governed Project Memory View defined
- [x] Task Memory does not duplicate Workflow state
- [x] raw conversation history != Project Memory
- [x] provider/model private memory != Project Memory
- [x] memory write policy exists
- [x] memory lifetime/invalidation exists
- [x] memory cannot promote itself
- [x] promotion delegates to UPOS-01/009
- [x] source provenance preserved
- [x] UPOS-01 epistemic classes preserved
- [x] historical/superseded sources remain labeled
- [x] no hard-coded project paths/providers
- [x] permissions remain UPOS-010
- [x] Workflow orchestration remains UPOS-004
- [x] telemetry remains UPOS-008
- [x] learning remains UPOS-009
- [x] project bindings remain UPOS-011
- [x] Context policy version recorded
- [x] required-source satisfaction explicit
- [x] exclusion reason vocabulary exists
- [x] budget accounting exists
- [x] Context Requirement template conforms to Context Requirement Standard
- [x] Context Request template conforms to Context Request Standard
- [x] Context Bundle template conforms to Context Bundle Standard
- [x] Memory Item template conforms to Memory Read/Write Standard
- [x] no mandatory normative field exists only in a Standard without Template representation unless explicitly runtime-only/non-template
- [x] no unresolved P0/P1 Module-05 semantic gaps
- [x] `UNMAPPED MODULE-05 SOURCE REQUIREMENTS = 0`
===== END VIRTUAL FILE: MODULE_05_DEFINITION_OF_DONE.md =====


---

## VIRTUAL FILE 19/36 — `MODULE_05_TRACEABILITY.md`

**Virtual path:** `MODULE_05_TRACEABILITY.md`  
**Content checksum:** `a50b7a3ae97d`

===== BEGIN VIRTUAL FILE: MODULE_05_TRACEABILITY.md =====
# Module 05 Traceability

**ID:** UPOS-05-TRC-001  
**Type:** TRACEABILITY / NORMATIVE COVERAGE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analysis/SOURCE_SECTION_DISPOSITION.md, analysis/TRACEABILITY_VALIDATION.md


**Frozen master SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`  
**UPOS-01 Source-of-Truth SHA-256:** `06913d3ba3585f2dd8676f2edc2ad82b43fad548b91e5fb57bec18a7c975bafd`  
**UPOS-01 Knowledge Lifecycle SHA-256:** `5e1a7653f22c218820b2c675f6f34bcf6bef5ad139bb0ce1639acae14cc2d885`  
**Implementation directive SHA-256:** `addcc8990f2a1480303605286494d8c80c1b2267ae5c5e7f7838ffd4661c4571`

## 1. Coverage model

Every identified Module-05 requirement maps:

```text
stable requirement ID
→ source/directive section
→ extracted requirement
→ canonical artifact
```

Frozen structural sections also have explicit disposition in `analysis/SOURCE_SECTION_DISPOSITION.md`.

## 2. Requirements

| Requirement | Source | Extracted requirement | Canonical artifact |
|---|---|---|---|
| `CTX-REQ-001` | UPOS-01 SOT §6 | Context source selection begins from exact fact scope, canonical owner, active normative sources, decisions/refinements and version applicability. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-002` | UPOS-01 SOT §9 | Implementation is evidence of current behavior and must not silently become intended product/policy truth. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-003` | UPOS-01 SOT §16 | Agent Context must resolve scope/owner/sources and report unresolved conflict rather than invent project facts. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-004` | UPOS-01 SOT §17 | Module 05 consumes the Source-of-Truth interface and does not hard-code project documentation paths. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-005` | UPOS-01 Knowledge §9 | Significant Context/Memory provenance must preserve origin, producer, version/baseline, evidence and supersession references. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-006` | UPOS-01 Knowledge §14 | Freshness and validity are distinct; recency does not equal correctness. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-007` | UPOS-01 Knowledge §23 | Project memory should primarily derive from governed project knowledge, not raw model conversation history. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-008` | UPOS-01 Knowledge §30 | Material execution should remain traceable through knowledge/evidence/decision/implementation relationships. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-009` | UPOS-01 Knowledge §31 | Context retrieval prefers active canonical sources and relevant accepted/validated knowledge before historical/raw notes. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-010` | UPOS-01 Knowledge §32 | Contradictory knowledge is not averaged; conflict resolves through Source-of-Truth governance. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-011` | Frozen §3.3/§3.4 | Context cannot replace Source-of-Truth with inference or silently invented project facts. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-012` | Frozen §3.12/§36 | Organizational learning belongs in governed durable artifacts rather than hidden model memory. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-013` | Frozen §31 | Agents receive minimal sufficient context selected by task, role, domain/risk, ownership, decisions, code and tests. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-014` | Frozen §32 | Context assembly preserves task/source/spec/decision/implementation/test/plan ordering as a heuristic subordinate to authority. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-015` | Frozen §33 | Context budget favors relevance, authority and freshness over maximum volume. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-016` | Frozen §34 | Temporary execution context, durable governed project memory and organizational learning are distinct. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-017` | Frozen §35 | Project memory sources are durable governed project artifacts; Module 05 accesses them via a governed view. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-018` | Frozen §74 | Handoff/context should be minimized and structured rather than passing full chat transcripts. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-019` | Frozen §150/§151 | Project artifacts remain durable memory; chat transcripts are not canonical memory. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-020` | Frozen §187/§188 | Sensitive Context is role/minimum-necessary scoped and consumes external secret/redaction constraints. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-021` | Frozen §190 | Context/source versions must support future reconstruction of what informed execution. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-022` | Frozen §191–193 | Unsupported/missing/stale project facts must be surfaced, not silently canonized or replaced by runtime evidence. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-023` | Frozen §208 | Reviewer Context is logically independent and excludes implementation chain-of-thought/private scratch by default. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-024` | Frozen §209 | QA Context begins from expected behavior rather than implementation narrative alone. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-025` | Frozen §210 | Merge Controller Context may be a focused evidence/readiness View rather than full implementation reasoning. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-026` | Frozen §211–212 | Human approval receives focused decision Context while authority remains external. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-027` | Frozen §217 | Context preserves evidence/authority class and does not treat agent intuition as strong project evidence. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-028` | Frozen §219–220 | Temporary scratch/raw reasoning is not automatically durable; workflows do not depend on hidden reasoning retention. | `MEMORY_READ_WRITE_STANDARD.md` |
| `CTX-REQ-029` | Frozen §221.4 | Giant all-document Context dumps are an anti-pattern. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-030` | Frozen §221.6 | Important project memory must not exist only in chat. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-031` | Directive §0 | Use UPOS-01 active governance, frozen UPOS-002/003/004 and frozen master according to their declared authority. | `README.md` |
| `CTX-REQ-032` | Directive §1 | Module 05 owns bounded execution Context & Memory semantics without creating a second Source of Truth. | `README.md` |
| `CTX-REQ-033` | Directive §2 | Knowledge, Context, Memory, Retrieval, Source Resolution, Context Bundle and Cache are formally distinct. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-034` | Directive §3 | Memory != Truth and Context != Truth are hard invariants. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-035` | Directive §4 | Module-05 ownership includes Context requirements/requests, retrieval/assembly/budget/freshness/isolation and bounded memory semantics. | `README.md` |
| `CTX-REQ-036` | Directive §5 | Module 05 does not absorb truth, authority, Skill, Workflow, Git, Quality, Observability, Learning, Security or Adapter ownership. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-037` | Directive §6 | Formalize Context Requirement, Context Request, Context Bundle and Context Item semantics. | `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` |
| `CTX-REQ-038` | Directive §7 | Stable Module-05 identities are context_request_id, context_bundle_id and memory_item_id; additional IDs require purpose. | `README.md` |
| `CTX-REQ-039` | Directive §8 | Every Context Request carries bounded execution attribution and policy/constraint references. | `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` |
| `CTX-REQ-040` | Directive §9 | Every production Bundle has provenance, scope, source/version, representation, freshness, budget, satisfaction/conflict and supersession data. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-041` | Directive §10 | Consumed Bundle content is immutable; material rebuild creates a new Bundle identity. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-042` | Directive §11 | Canonical owner/source resolution is consumed from UPOS-01 and is not redefined. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-043` | Directive §12 | Retrieval is authority-aware before relevance; similarity never overrides authority. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-044` | Directive §13 | Retrieval Candidate attributes distinguish eligibility, authority, freshness, relevance and representation possibilities. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-045` | Directive §14 | Source eligibility is checked before relevance ranking. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-046` | Directive §15 | Required and optional sources are distinct; required sources cannot be silently budget-dropped. | `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` |
| `CTX-REQ-047` | Directive §16 | Context representation classes are EXACT, EXCERPT, DERIVED_SUMMARY and REFERENCE_ONLY. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-048` | Directive §17 | Summaries are derived, provenance-linked, limitation-aware and never canonical by themselves. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-049` | Directive §18 | Module 05 owns Context Budget semantics while concrete provider capacity belongs downstream. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-050` | Directive §19 | Priority is explicit and budget pressure removes lowest-value optional material first. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-051` | Directive §20 | Required-context overflow uses controlled summarization/staging/splitting/provider escalation/blocking, never arbitrary truncation. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-052` | Directive §21 | Incremental/just-in-time bounded retrieval is supported instead of front-loading the project. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-053` | Directive §22 | Context is Role-specific rather than a universal blob. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-054` | Directive §23 | Reviewer receives independent authoritative Context and does not automatically inherit Implementer scratch/private reasoning. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-055` | Directive §24 | Context View is a bounded Role/Run/Stage/Skill projection and does not grant authority. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-056` | Directive §25 | Context contamination risks are labeled/prevented through provenance, scope and epistemic preservation. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-057` | Directive §26 | Cross-project Context isolation is default. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-058` | Directive §27 | Task working memory does not automatically cross Task boundaries. | `CONTEXT_ISOLATION_AND_VIEWS.md` |
| `CTX-REQ-059` | Directive §28 | Freshness is assessed separately from authority/canonicality. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-060` | Directive §29 | Material source/scope/role/policy changes trigger Context revalidation/invalidation. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-061` | Directive §30 | UPOS-004 reclassification/rerouting triggers Context revalidation/reassembly without Module 05 rerouting the Workflow. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-062` | Directive §31 | Context Delta may describe immutable Bundle reassembly without creating a mutable accumulating context object. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-063` | Directive §32 | Memory is taxonomized rather than stored in one generic bucket. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-064` | Directive §33 | Run Working Memory is ephemeral noncanonical support scoped to one Agent Run. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-065` | Directive §34 | Task Working Memory is bounded noncanonical support scoped to one Task. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-066` | Directive §35 | Task Working Memory does not duplicate UPOS-004 Workflow state. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-067` | Directive §36 | Retrieval Cache adds zero authority and remains source/version/scope/freshness-bound. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-068` | Directive §37 | Governed Project Memory View is a retrieval interface over UPOS-01 knowledge, not a new database of truth. | `PROJECT_MEMORY_INTERFACE.md` |
| `CTX-REQ-069` | Directive §38 | Raw conversation history is not Project Memory. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-070` | Directive §39 | Private provider/model/personalization memory is not canonical U-POS project knowledge. | `MEMORY_TAXONOMY.md` |
| `CTX-REQ-071` | Directive §40 | Every persisted memory write has stable identity, class, scope, provenance, epistemic/lifetime/invalidation data and canonicality=false. | `MEMORY_READ_WRITE_STANDARD.md` |
| `CTX-REQ-072` | Directive §41 | Memory cannot promote itself; promotion delegates to UPOS-01/009. | `MEMORY_READ_WRITE_STANDARD.md` |
| `CTX-REQ-073` | Directive §42 | Memory semantic lifetime classes are explicit and do not imply indefinite retention. | `MEMORY_LIFECYCLE_AND_INVALIDATION.md` |
| `CTX-REQ-074` | Directive §43 | Memory becomes stale/expired/invalidated on source/scope/permission/TTL/conflict changes. | `MEMORY_LIFECYCLE_AND_INVALIDATION.md` |
| `CTX-REQ-075` | Directive §44 | Memory reuse requires scope/provenance/freshness/permission/applicability checks. | `MEMORY_READ_WRITE_STANDARD.md` |
| `CTX-REQ-076` | Directive §45 | Every meaningful Context Item preserves source/version/owner/epistemic/representation/derivation/freshness provenance. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-077` | Directive §46 | Every Bundle contains a Context Manifest explaining requirements, inclusion/exclusion, summaries, conflicts and budget. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-078` | Directive §47 | Retrieval inclusion/exclusion is explainable rather than relying only on opaque embedding ranking. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-079` | Directive §48 | Missing required authoritative Context yields explicit incomplete/blocking failure rather than inference. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-080` | Directive §49 | Canonical conflict is surfaced; Module 05 does not average/vote/select by recency/similarity. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-081` | Directive §50 | SOURCE_NOT_FOUND is distinct from governed proof that a source does not exist. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-082` | Directive §51 | Implementation evidence remains implementation evidence and cannot silently override normative truth. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-083` | Directive §52 | Historical/superseded/retired material remains labeled and included only for explicit relevance. | `SOURCE_RESOLUTION_INTERFACE.md` |
| `CTX-REQ-084` | Directive §53 | Context preserves UPOS-01 epistemic classes rather than inventing competing truth classes. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-085` | Directive §54 | Skill Context requirements are resolved through Module 05 while Skill procedure remains UPOS-003. | `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` |
| `CTX-REQ-086` | Directive §55 | Workflow Stage declares timing/need while Module 05 assembles Context; sequencing remains UPOS-004. | `CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md` |
| `CTX-REQ-087` | Directive §56 | Rework/re-review revalidates Context rather than blindly reusing original Bundle. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-088` | Directive §57 | Human decision Context can be focused while authority remains UPOS-002/010. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-089` | Directive §58 | Context retrieval consumes UPOS-010 permission/security constraints and does not grant access. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-090` | Directive §59 | Sensitive Context supports minimum-necessary/redacted/reference-only/Role-scoped representation. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-091` | Directive §60 | Universal Context uses abstract Source Classes; physical project mappings belong UPOS-011. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-092` | Directive §61 | Module 05 remains model/provider/storage/search independent. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-093` | Directive §62 | Module 05 defines retrieval outcome semantics; provider/backend choice remains UPOS-011/runtime. | `RETRIEVAL_AND_SELECTION_STANDARD.md` |
| `CTX-REQ-094` | Directive §63 | Module 05 exposes stable Context/Memory provenance identities while telemetry semantics remain UPOS-008. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-095` | Directive §64 | Bundle semantics support future control-plane questions about actual received sources, omissions, summaries, staleness/rebuild and memory influence. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-096` | Directive §65 | Context health signals are factual signals, not metrics/aggregation. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-097` | Directive §66 | Context-level failure taxonomy distinguishes missing source/resolution/conflict/stale/permission/budget/representation/provenance/contamination/memory/provider failures. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-098` | Directive §67 | Required source failure cannot produce fully valid Context; optional omissions may permit warnings. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-099` | Directive §68 | Bundle identity is separate from validity state; immutable snapshot may later be stale/invalidated. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-100` | Directive §69 | Memory item execution-support states are distinct from Knowledge Lifecycle. | `MEMORY_LIFECYCLE_AND_INVALIDATION.md` |
| `CTX-REQ-101` | Directive §70 | Context/Memory must not silently evolve Skills/Workflows/policy through hidden learning. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-102` | Directive §71 | SKL-ASSEMBLE-CONTEXT calls Module-05 interfaces; it does not own Context semantics. | `CONTEXT_ASSEMBLY_STANDARD.md` |
| `CTX-REQ-103` | Directive §72 | Maximum available context is not optimal; Context Minimalism is normative. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-104` | Directive §73 | Assembly must be explainable/substantially reproducible for the same scope/sources/policies/permissions. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-105` | Directive §74 | Material source change during Agent Run marks Context stale/invalidated and reports to Workflow interface. | `FRESHNESS_INVALIDATION_AND_REASSEMBLY.md` |
| `CTX-REQ-106` | Directive §75 | Context preserves enough metadata for Task→Workflow→Stage→Run→Skill→Bundle→sources/memory→output replay. | `CONTEXT_MEMORY_LIFECYCLE.md` |
| `CTX-REQ-107` | Directive §76 | Bundle identity is not semantic version; normative Module-05 contracts use controlled versioning. | `CONTEXT_MEMORY_LIFECYCLE.md` |
| `CTX-REQ-108` | Directive §77 | Module 05 prescribes no SQL/vector/Redis/filesystem/graph/provider-memory storage implementation. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-109` | Directive §78 | Package decomposition covers Request/Bundle/Resolution/Retrieval/Assembly/Budget/Freshness/Isolation/Failure/Memory/interfaces/traceability. | `README.md` |
| `CTX-REQ-110` | Directive §79 | Analysis-first artifacts precede normative implementation and become historical EVIDENCE at freeze. | `analysis/FIRST_DELIVERABLE_SUMMARY.md` |
| `CTX-REQ-111` | Directive §80 | Relevant frozen sections have explicit EXTRACTED/MIXED/DEFERRED/OUTSIDE disposition. | `analysis/SOURCE_SECTION_DISPOSITION.md` |
| `CTX-REQ-112` | Directive §81 | Specified Context/Memory boundary ambiguities are resolved with no open P0/P1 at freeze. | `analysis/AMBIGUITY_GAP_REGISTER.md` |
| `CTX-REQ-113` | Directive §82 | Traceability maps stable requirements from frozen/upstream/directive sources to canonical artifacts. | `MODULE_05_TRACEABILITY.md` |
| `CTX-REQ-114` | Directive §83 | Cross-module interfaces cover UPOS-01/02/03/04/06–11 and schemas/runtime with provides/consumes/non-redefinition. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-115` | Directive §84 | Expected interface semantics for each upstream/downstream module are preserved without ownership leakage. | `CROSS_MODULE_INTERFACES.md` |
| `CTX-REQ-116` | Directive §85 | Context failure result and Workflow recovery response are explicitly separate ownership concerns. | `CONTEXT_FAILURE_MODEL.md` |
| `CTX-REQ-117` | Directive §86 | Context Request/Bundle records context_policy_ref/version for reproducibility. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |
| `CTX-REQ-118` | Directive §87 | Bundle reports required_sources_satisfied explicitly. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-119` | Directive §88 | Standard exclusion reasons explain why discovered material was omitted. | `CONTEXT_BUNDLE_STANDARD.md` |
| `CTX-REQ-120` | Directive §89 | Bundle exposes factual budget accounting without defining cost metrics. | `CONTEXT_BUDGET_AND_REPRESENTATION.md` |
| `CTX-REQ-121` | Directive §90 | The required first analysis deliverable is produced before normative implementation. | `analysis/FIRST_DELIVERABLE_SUMMARY.md` |
| `CTX-REQ-122` | Directive §91 | Implementation is decomposed into coherent logical documentation changes rather than one giant conceptual change. | `analysis/IMPLEMENTATION_PLAN.md` |
| `CTX-REQ-123` | Directive §92 | Module-05 DoD encodes all required completion conditions. | `MODULE_05_DEFINITION_OF_DONE.md` |
| `CTX-REQ-124` | Directive §93 | Final package exposes canonical artifacts, entity/failure/memory/interface/traceability/validation outputs. | `README.md` |
| `CTX-REQ-125` | Directive §94 | Final principles optimize for minimum sufficient authoritative/fresh/permission-safe/traceable Context without hidden second truth. | `CONTEXT_MEMORY_OPERATING_MODEL.md` |

## 3. Final conformance reconciliation requirements

| Requirement | Source | Reconciled requirement | Canonical Module-05 artifact |
|---|---|---|---|
| `CTX-CONF-001` | Final conformance cleanup §1 | Context Bundle operational template explicitly represents `assembly_policy_ref` and `assembly_policy_version` where separately configured / explicit N/A otherwise. | `CONTEXT_BUNDLE_STANDARD.md`; `templates/CONTEXT_BUNDLE_TEMPLATE.md` |
| `CTX-CONF-002` | Final conformance cleanup §1 | Each Context Item can represent `permission_transformation_ref` without redefining UPOS-010 permission semantics. | `CONTEXT_BUNDLE_STANDARD.md`; `templates/CONTEXT_BUNDLE_TEMPLATE.md` |
| `CTX-CONF-003` | Final conformance cleanup §2 | Memory write contract/template use explicit `scope_refs`, `representation_content_type`, and `content_or_artifact_ref` semantics. | `MEMORY_READ_WRITE_STANDARD.md`; `templates/MEMORY_ITEM_TEMPLATE.md` |
| `CTX-CONF-004` | Final conformance cleanup §3–5 | All four canonical operational templates mechanically conform to their owning normative Standards. | `templates/*`; `analysis/TRACEABILITY_VALIDATION.md` |
| `CTX-CONF-005` | Final conformance cleanup §6–7 | Final coverage/validation explicitly includes operational-template conformance and zero unresolved P0/P1 gaps. | `MODULE_05_DEFINITION_OF_DONE.md`; `analysis/TRACEABILITY_VALIDATION.md` |

## 3. Coverage meaning

```text
UNMAPPED MODULE-05 SOURCE REQUIREMENTS = 0
```

means:

- identified Context/Memory semantics from frozen master are extracted or explicitly deferred;
- relevant UPOS-01 requirements are mapped;
- all top-level implementation-directive sections §0–§94 are covered;
- final conformance reconciliation requirements `CTX-CONF-001…005` are mapped;
- each extracted requirement targets an existing canonical/evidence artifact appropriate to its nature.

It does not claim UPOS-006–011 are implemented.
===== END VIRTUAL FILE: MODULE_05_TRACEABILITY.md =====


---

## VIRTUAL FILE 20/36 — `VIRTUAL_REPOSITORY_TREE.md`

**Virtual path:** `VIRTUAL_REPOSITORY_TREE.md`  
**Content checksum:** `b89be5fa52d3`

===== BEGIN VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====

# UPOS-005 Virtual Repository Tree

```text
05_context_memory/
├── analysis/AMBIGUITY_GAP_REGISTER.md
├── analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md
├── analysis/CONTEXT_ISOLATION_ANALYSIS.md
├── analysis/FIRST_DELIVERABLE_SUMMARY.md
├── analysis/IMPLEMENTATION_PLAN.md
├── analysis/MEMORY_TAXONOMY_ANALYSIS.md
├── analysis/MODULE_05_OWNERSHIP_MAP.md
├── analysis/PROPOSED_PACKAGE_TREE.md
├── analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md
├── analysis/SOURCE_ANALYSIS.md
├── analysis/SOURCE_SECTION_DISPOSITION.md
├── analysis/TRACEABILITY_VALIDATION.md
├── CONTEXT_ASSEMBLY_STANDARD.md
├── CONTEXT_BUDGET_AND_REPRESENTATION.md
├── CONTEXT_BUNDLE_STANDARD.md
├── CONTEXT_FAILURE_MODEL.md
├── CONTEXT_ISOLATION_AND_VIEWS.md
├── CONTEXT_MEMORY_LIFECYCLE.md
├── CONTEXT_MEMORY_OPERATING_MODEL.md
├── CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md
├── CROSS_MODULE_INTERFACES.md
├── FRESHNESS_INVALIDATION_AND_REASSEMBLY.md
├── MEMORY_LIFECYCLE_AND_INVALIDATION.md
├── MEMORY_READ_WRITE_STANDARD.md
├── MEMORY_TAXONOMY.md
├── MODULE_05_DEFINITION_OF_DONE.md
├── MODULE_05_TRACEABILITY.md
├── PROJECT_MEMORY_INTERFACE.md
├── README.md
├── RETRIEVAL_AND_SELECTION_STANDARD.md
├── SOURCE_RESOLUTION_INTERFACE.md
├── templates/CONTEXT_BUNDLE_TEMPLATE.md
├── templates/CONTEXT_REQUEST_TEMPLATE.md
├── templates/CONTEXT_REQUIREMENT_TEMPLATE.md
├── templates/MEMORY_ITEM_TEMPLATE.md
├── VIRTUAL_REPOSITORY_TREE.md
```

===== END VIRTUAL FILE: VIRTUAL_REPOSITORY_TREE.md =====


---

## VIRTUAL FILE 21/36 — `templates/CONTEXT_BUNDLE_TEMPLATE.md`

**Virtual path:** `templates/CONTEXT_BUNDLE_TEMPLATE.md`  
**Content checksum:** `c878dfbe78f0`

===== BEGIN VIRTUAL FILE: templates/CONTEXT_BUNDLE_TEMPLATE.md =====
# Context Bundle Template

**ID:** UPOS-05-TPL-003  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Context Bundle

context_bundle_id:
context_request_id:

project_id_ref:
task_id:
routing_decision_id:
workflow_instance_id:
stage_id:

role_id:
agent_definition_id:
agent_definition_version:
agent_run_id:

skill_id:
skill_version:
skill_invocation_ref:

purpose:

context_policy_ref:
context_policy_version:
assembly_policy_ref: N/A
assembly_policy_version: N/A
assembled_at:

validity_state:
required_sources_satisfied:

source_resolution_refs:

included_context_items:
- bundle_local_item_key:
  source_ref:
  source_class:
  source_version_or_revision:
  canonical_owner_ref:
  source_status:
  epistemic_class_ref:
  representation_type:
  derived_from:
  freshness_assessment:
  inclusion_reason:
  priority:
  required_or_optional:
  permission_transformation_ref: N/A

excluded_candidates:
- source_ref:
  exclusion_reason:
  materiality:

open_conflicts:
open_unknowns:

budget_accounting:
  budget_limit_or_reference:
  budget_consumed:
  required_material:
  optional_material:
  summarized_material:
  omitted_optional_material:

supersedes_context_bundle_id:
reassembly_reason:
```
===== END VIRTUAL FILE: templates/CONTEXT_BUNDLE_TEMPLATE.md =====


---

## VIRTUAL FILE 22/36 — `templates/CONTEXT_REQUEST_TEMPLATE.md`

**Virtual path:** `templates/CONTEXT_REQUEST_TEMPLATE.md`  
**Content checksum:** `4640dc2b46fc`

===== BEGIN VIRTUAL FILE: templates/CONTEXT_REQUEST_TEMPLATE.md =====

# Context Request Template

**ID:** UPOS-05-TPL-002  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Context Request

context_request_id:

project_id_ref:
task_id:
routing_decision_id:
workflow_instance_id:
stage_id:

role_id:
agent_definition_id:
agent_definition_version:
agent_run_id:

skill_id:
skill_version:
skill_invocation_ref:

purpose:

required_source_classes:
optional_source_classes:

context_constraints:
representation_constraints:
budget_constraints:
permission_security_constraint_refs:
independence_requirements:

context_policy_ref:
context_policy_version:

prior_context_bundle_id:
```

===== END VIRTUAL FILE: templates/CONTEXT_REQUEST_TEMPLATE.md =====


---

## VIRTUAL FILE 23/36 — `templates/CONTEXT_REQUIREMENT_TEMPLATE.md`

**Virtual path:** `templates/CONTEXT_REQUIREMENT_TEMPLATE.md`  
**Content checksum:** `ab43cb717a26`

===== BEGIN VIRTUAL FILE: templates/CONTEXT_REQUIREMENT_TEMPLATE.md =====

# Context Requirement Template

**ID:** UPOS-05-TPL-001  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Context Requirement — <name>

Owner Contract Reference:
Consumer Type:
Purpose:

Required Source Classes:
Optional Source Classes:

Representation Constraints:
Freshness Constraints:
Independence Constraints:
Permission/Security Constraint References:

Requiredness Notes:
Failure if Unsatisfied:
```

===== END VIRTUAL FILE: templates/CONTEXT_REQUIREMENT_TEMPLATE.md =====


---

## VIRTUAL FILE 24/36 — `templates/MEMORY_ITEM_TEMPLATE.md`

**Virtual path:** `templates/MEMORY_ITEM_TEMPLATE.md`  
**Content checksum:** `24671e3e9f7e`

===== BEGIN VIRTUAL FILE: templates/MEMORY_ITEM_TEMPLATE.md =====
# Memory Item Template

**ID:** UPOS-05-TPL-004  
**Type:** TEMPLATE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-005 Context & Memory  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


```markdown
# Memory Item

memory_item_id:
memory_class:
memory_state:

project_id_ref:
scope_refs:
task_id:
agent_run_id:

producer_role_ref:
producer_agent_run_ref:

epistemic_class_ref:
provenance:
source_refs:
created_from_refs:

representation_content_type:
content_or_artifact_ref:

created_at:
lifetime_class:
expiration_or_review_trigger:
invalidation_conditions:

permission_security_constraint_refs:

canonicality: false
```
===== END VIRTUAL FILE: templates/MEMORY_ITEM_TEMPLATE.md =====


---

## VIRTUAL FILE 25/36 — `analysis/AMBIGUITY_GAP_REGISTER.md`

**Virtual path:** `analysis/AMBIGUITY_GAP_REGISTER.md`  
**Content checksum:** `0fa1e49a47a7`

===== BEGIN VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====

# UPOS-005 Ambiguity & Gap Register

**ID:** UPOS-05-AN-008  
**Type:** ANALYSIS / GAP REGISTER  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


| ID | Issue | Module-05 resolution | Deferred owner | Severity | Status |
|---|---|---|---|---|---|
| G05-001 | Context vs Knowledge | Knowledge remains UPOS-01; Context is execution-time selection. | UPOS-01 | P0 | CLOSED |
| G05-002 | Context vs Memory | Context is assembled per execution; Memory is retained execution support with explicit scope/lifetime. | — | P1 | CLOSED |
| G05-003 | Memory vs Project Knowledge | Governed Project Memory is a view over UPOS-01, not a second store. | UPOS-01 | P0 | CLOSED |
| G05-004 | Task Memory vs Workflow State | Task memory stores support material; Workflow state remains UPOS-004. | UPOS-004 | P0 | CLOSED |
| G05-005 | Context Requirement vs Skill Contract | Skill declares Source/Context needs; Module 05 resolves them. | UPOS-003 | P1 | CLOSED |
| G05-006 | Context Requirement vs Workflow Stage Contract | Stage declares need/timing; Module 05 assembles valid context. | UPOS-004 | P1 | CLOSED |
| G05-007 | Context Bundle vs Prompt | Bundle is provider-independent semantic package; prompt formatting is adapter/runtime concern. | UPOS-011/runtime | P1 | CLOSED |
| G05-008 | Context Bundle vs Source of Truth | Bundle snapshots sources; canonicality remains UPOS-01. | UPOS-01 | P0 | CLOSED |
| G05-009 | Retrieval vs Source Resolution | Source Resolution determines owner/canonical universe; retrieval locates eligible material. | UPOS-01 | P0 | CLOSED |
| G05-010 | Authority ranking vs relevance ranking | Authority eligibility precedes relevance; relevance cannot override authority. | UPOS-01 | P0 | CLOSED |
| G05-011 | Freshness vs canonicality | Freshness is execution applicability; canonicality/owner status remains upstream. | UPOS-01 | P1 | CLOSED |
| G05-012 | Stale vs superseded | STALE is Context freshness assessment; SUPERSEDED is consumed source lifecycle/status. | UPOS-01 | P1 | CLOSED |
| G05-013 | Summary vs canonical source | Summary is DERIVED_SUMMARY with provenance and never canonical by itself. | UPOS-01 | P0 | CLOSED |
| G05-014 | Cache vs Memory | Cache is retrieval optimization; working memory supports execution. | — | P1 | CLOSED |
| G05-015 | Cache vs Source | Cache preserves source identity/version and adds zero authority. | UPOS-01 | P0 | CLOSED |
| G05-016 | Context reuse vs stale reuse | Reuse requires revalidation of scope/source version/freshness/permissions. | — | P1 | CLOSED |
| G05-017 | Run memory vs Task memory | Run memory is ephemeral single-run; Task memory spans bounded Task execution. | — | P1 | CLOSED |
| G05-018 | Task memory vs cross-task knowledge | Task memory does not cross task boundary without governed reusable reference/promotion. | UPOS-01 | P0 | CLOSED |
| G05-019 | Context isolation vs Security permissions | Module 05 performs isolation/minimization using constraints returned by UPOS-010; it does not grant access. | UPOS-010 | P0 | CLOSED |
| G05-020 | Reviewer independence vs Implementer context | Reviewer gets independent authoritative Context View; producer notes are separately labeled. | UPOS-002/007 | P0 | CLOSED |
| G05-021 | Context invalidation vs Workflow reroute | UPOS-004 reroute/reclassify triggers Module-05 revalidation/reassembly; Module 05 does not route. | UPOS-004 | P1 | CLOSED |
| G05-022 | Context failure vs Workflow failure | Module 05 emits Context result/failure; UPOS-004 selects orchestration response. | UPOS-004 | P0 | CLOSED |
| G05-023 | Memory evolution vs Learning System | Memory observations become candidates; promotion/evolution remains UPOS-009/01. | UPOS-009/01 | P0 | CLOSED |
| G05-024 | Project Memory vs provider/model memory | Private provider/model memory is never canonical U-POS knowledge. | UPOS-01/011 | P0 | CLOSED |
| G05-025 | Bundle immutable vs validity changes | Bundle payload is immutable; later validity assessments do not mutate consumed content. | — | P1 | CLOSED |
| G05-026 | Required source exceeds budget | Cannot silently omit; use safe summarization/staged retrieval/split/block/escalate. | UPOS-004/011 | P0 | CLOSED |
| G05-027 | Source not found vs absence | Technical retrieval failure is not proof source does not exist. | UPOS-01/011 | P1 | CLOSED |
| G05-028 | Context policy version | Bundle records context policy/version for reproducibility; source versions remain separate. | — | P1 | CLOSED |

## Result

No unresolved P0/P1 Module-05 semantic gap remains before normative implementation.

===== END VIRTUAL FILE: analysis/AMBIGUITY_GAP_REGISTER.md =====


---

## VIRTUAL FILE 26/36 — `analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md`

**Virtual path:** `analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md`  
**Content checksum:** `a8e0eef72dba`

===== BEGIN VIRTUAL FILE: analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md =====

# Context Entity Model Analysis

**ID:** UPOS-05-AN-004  
**Type:** ANALYSIS / ENTITY MODEL  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Recommended ontology

```text
KNOWLEDGE
= governed project truth/evidence/proposal/history
  owned by UPOS-01

CONTEXT REQUIREMENT
= reusable declaration of needed information characteristics

CONTEXT REQUEST
= concrete bounded request for execution context

SOURCE RESOLUTION
= canonical owner/source determination through UPOS-01

RETRIEVAL CANDIDATE
= discovered source/material candidate not yet included

CONTEXT ITEM
= attributable included information unit

CONTEXT BUNDLE
= immutable assembled execution snapshot

CONTEXT VIEW
= bounded projection for a Role/Run/Stage/Skill consumer

MEMORY ITEM
= retained noncanonical execution-support item

CACHE
= retrieval optimization with zero added authority
```

## Stable identity decision

Required Module-05 identities:

```text
context_request_id
context_bundle_id
memory_item_id
```

Not introduced in v1:

```text
context_resolution_id
retrieval_decision_id
```

Reason: source resolution remains an upstream/interface result and retrieval inclusion/exclusion decisions are sufficiently attributable through the Context Manifest. New global identity entities would add complexity without an independent lifecycle/ownership need.

## Provenance chain

```text
project reference
→ task_id
→ routing_decision_id
→ workflow_instance_id
→ stage_id
→ role_id
→ agent_definition/version
→ agent_run_id
→ skill_id/version + invocation reference where applicable
→ context_request_id
→ context_bundle_id
→ source references / memory references
```

## Immutability decision

Bundle payload is immutable once SEALED/consumed.

Late freshness/validity changes do not rewrite consumed content. They create a new validity assessment and, when required, a new Bundle:

```text
CB-102
→ stale / invalidated for active use
→ reassembly
→ CB-103
→ supersedes_context_bundle_id = CB-102
```

===== END VIRTUAL FILE: analysis/CONTEXT_ENTITY_MODEL_ANALYSIS.md =====


---

## VIRTUAL FILE 27/36 — `analysis/CONTEXT_ISOLATION_ANALYSIS.md`

**Virtual path:** `analysis/CONTEXT_ISOLATION_ANALYSIS.md`  
**Content checksum:** `6a88d38d0fba`

===== BEGIN VIRTUAL FILE: analysis/CONTEXT_ISOLATION_ANALYSIS.md =====

# Context Isolation Analysis

**ID:** UPOS-05-AN-007  
**Type:** ANALYSIS / CONTEXT ISOLATION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Context View

A Context View is a bounded projection of eligible information for a specific consumer.

Relevant dimensions:

```text
project
Task
Workflow Instance
Stage
Role
Agent Run
Skill Invocation
Change Class
permissions/security constraints
independence requirements
```

## Reviewer independence

```text
producer context
!= reviewer authoritative context
```

Reviewer MUST independently receive the authoritative sources needed to evaluate the change.

Reviewer context MUST NOT automatically inherit:

- Implementer scratch notes;
- private chain-of-thought/reasoning;
- unverified assumptions;
- self-approval claims;
- producer-only transient memory.

Producer notes MAY be included only as clearly labeled producer-provided material when relevant.

## QA independence

QA Context View should begin from expected behavior/contracts and risk, not only implementation narrative.

## Cross-project isolation

```text
Project A context
MUST NOT leak into
Project B context
```

unless an explicit shared/federated mechanism is authorized externally.

## Cross-task isolation

Task memory from Task A is not injected into Task B merely because a model/search engine can retrieve it.

## Authority boundary

Access to a source does not grant authority over that fact scope.

===== END VIRTUAL FILE: analysis/CONTEXT_ISOLATION_ANALYSIS.md =====


---

## VIRTUAL FILE 28/36 — `analysis/FIRST_DELIVERABLE_SUMMARY.md`

**Virtual path:** `analysis/FIRST_DELIVERABLE_SUMMARY.md`  
**Content checksum:** `72aafce0b767`

===== BEGIN VIRTUAL FILE: analysis/FIRST_DELIVERABLE_SUMMARY.md =====

# UPOS-005 First Deliverable Summary

**ID:** UPOS-05-AN-011  
**Type:** ANALYSIS / FIRST DELIVERABLE  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## 1. Scope
Execution-time Context & Memory semantics: requirements/requests, retrieval eligibility, assembly, budget, views, freshness, failures, temporary memory and governed project-memory access.

## 2. Non-scope
Truth/authority/workflow/Git/quality/telemetry/learning/security grants/provider bindings remain UPOS-01/02/04/06–11.

## 3. Ontology
`Knowledge != Context != Memory != Retrieval != Source Resolution != Context Bundle != Cache`.

## 4. Request → Bundle
`Requirements → Context Request → UPOS-01 resolution → permission/provider interfaces → eligible candidates → selection/representation/budget → immutable Context Bundle`.

## 5. Stable identity
`context_request_id`, `context_bundle_id`, `memory_item_id`; upstream identities are referenced, not re-owned.

## 6. Source resolution vs retrieval
UPOS-01 decides canonical owner/source universe; UPOS-005 retrieves/selects within that authority envelope.

## 7. Authority-aware retrieval
Authority/scope/version/permission/freshness eligibility precedes relevance and budget.

## 8. Bundle contract
Immutable, attributable, policy-versioned snapshot with Context Manifest, provenance, validity, budget accounting, exclusions, conflicts/unknowns and supersession link.

## 9. Budget
Optimize for minimum sufficient authoritative context; required material cannot be silently budget-dropped.

## 10. Compression
`EXACT / EXCERPT / DERIVED_SUMMARY / REFERENCE_ONLY`; summaries remain derived and provenance-linked.

## 11. Freshness
Freshness separate from authority/canonicality; material source/route changes trigger revalidation and possibly a new Bundle.

## 12. Context View
Role/Run/Stage/Skill projection over eligible material, with permissions and independence constraints.

## 13. Reviewer independence
Reviewer independently receives authoritative requirements and does not inherit Implementer scratch/private reasoning automatically.

## 14. Memory taxonomy
`RUN_WORKING_MEMORY`, `TASK_WORKING_MEMORY`, `RETRIEVAL_CACHE`, `GOVERNED_PROJECT_MEMORY_VIEW`.

## 15. Project-memory boundary
Governed Project Memory View is a retrieval/view interface over UPOS-01, not a new database of truth.

## 16. Memory write/promotion
Persisted items remain noncanonical unless they are references into governed knowledge. Promotion is UPOS-01/009.

## 17. Failure taxonomy
Explicit Context failures with degraded/blocked semantics; Workflow response remains UPOS-004.

## 18. Cross-module interfaces
Explicit provides/consumes/MUST NOT redefine for UPOS-01–04 and 06–11.

## 19. Ambiguity/gaps
28 boundary/gap items resolved; no open P0/P1.

## 20. Package tree
See `PROPOSED_PACKAGE_TREE.md`.

## 21. Implementation plan
See `IMPLEMENTATION_PLAN.md`.

## 22. Expected commits
11 coherent documentation commits are proposed; no giant commit is assumed.

## 23. Definition of Done
The directive's Module-05 DoD will be encoded canonically in `MODULE_05_DEFINITION_OF_DONE.md`.

===== END VIRTUAL FILE: analysis/FIRST_DELIVERABLE_SUMMARY.md =====


---

## VIRTUAL FILE 29/36 — `analysis/IMPLEMENTATION_PLAN.md`

**Virtual path:** `analysis/IMPLEMENTATION_PLAN.md`  
**Content checksum:** `3581ff55e9a2`

===== BEGIN VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====

# UPOS-005 Implementation Plan

**ID:** UPOS-05-AN-010  
**Type:** IMPLEMENTATION PLAN / EVIDENCE  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Implementation sequence

1. establish Context/Memory ownership boundary and ontology;
2. define Context Requirement / Request identity and attribution;
3. define Context Bundle / Manifest / immutable snapshot semantics;
4. define UPOS-01 Source Resolution boundary;
5. define authority-aware retrieval/eligibility/exclusion semantics;
6. define assembly, priority, budget, representation and safe compression;
7. define freshness, validity, invalidation, delta/reassembly;
8. define Role Context Views and independence/isolation;
9. define Context failure/result taxonomy;
10. define Memory taxonomy/read-write/lifetime/invalidation;
11. define Governed Project Memory View and promotion boundary;
12. define cross-module interfaces/templates/lifecycle;
13. complete source/directive/upstream traceability;
14. validate no ownership leakage and zero unmapped requirements.

## Expected logical commits

```text
docs(upos-005): establish context and memory ownership boundary
docs(upos-005): define context request and bundle contracts
docs(upos-005): define source resolution and retrieval semantics
docs(upos-005): define context assembly budget and representation
docs(upos-005): define freshness invalidation and reassembly
docs(upos-005): define role views and context isolation
docs(upos-005): define context failure model
docs(upos-005): define memory taxonomy and read-write policy
docs(upos-005): define governed project memory interface
docs(upos-005): add templates and cross-module interfaces
docs(upos-005): complete source traceability audit
```

Invariant:

```text
one commit = one coherent logical change
```

## Non-scope

No UPOS-006 design, Git mechanics, Quality verdict system, telemetry/event model, Learning engine, Security permission model, project/provider adapter, machine schema, vector database, cache backend, or model-provider implementation.

===== END VIRTUAL FILE: analysis/IMPLEMENTATION_PLAN.md =====


---

## VIRTUAL FILE 30/36 — `analysis/MEMORY_TAXONOMY_ANALYSIS.md`

**Virtual path:** `analysis/MEMORY_TAXONOMY_ANALYSIS.md`  
**Content checksum:** `d46ef70aa7ad`

===== BEGIN VIRTUAL FILE: analysis/MEMORY_TAXONOMY_ANALYSIS.md =====

# Memory Taxonomy Analysis

**ID:** UPOS-05-AN-006  
**Type:** ANALYSIS / MEMORY TAXONOMY  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## v1 taxonomy

### RUN_WORKING_MEMORY

Ephemeral noncanonical support for one Agent Run.

Examples:

- temporary notes;
- intermediate calculations;
- retrieval pointers;
- partial working artifacts.

Default: not persisted beyond Run without explicit policy.

### TASK_WORKING_MEMORY

Bounded noncanonical operational memory retained across Runs/Stages for one Task.

It MUST NOT duplicate UPOS-004 Workflow state.

### RETRIEVAL_CACHE

Performance optimization for previously resolved/retrieved material.

Invariant:

```text
CACHE HAS ZERO ADDITIONAL AUTHORITY
```

### GOVERNED_PROJECT_MEMORY_VIEW

Not a new semantic database.

```text
GOVERNED_PROJECT_MEMORY_VIEW
= Context/Retrieval view over knowledge governed by UPOS-01
```

## Rejected generic bucket

A single persistent `memory` bucket is rejected because it conflates:

- scratch state;
- task coordination;
- cached retrieval;
- canonical project knowledge.

## Cross-task rule

Task Working Memory is not automatically reusable by another Task.

Cross-task reuse must pass through governed knowledge/evidence/artifact references and current scope/freshness/permission checks.

## Provider/model memory

Provider private memory, latent model memory, personalization memory, and raw conversation history are not Project Memory and cannot be hidden dependencies.

===== END VIRTUAL FILE: analysis/MEMORY_TAXONOMY_ANALYSIS.md =====


---

## VIRTUAL FILE 31/36 — `analysis/MODULE_05_OWNERSHIP_MAP.md`

**Virtual path:** `analysis/MODULE_05_OWNERSHIP_MAP.md`  
**Content checksum:** `54d31a9ec5db`

===== BEGIN VIRTUAL FILE: analysis/MODULE_05_OWNERSHIP_MAP.md =====

# Module 05 Ownership Map

**ID:** UPOS-05-AN-002  
**Type:** ANALYSIS / OWNERSHIP MAP  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Module 05 owns

```text
Context Requirement / Context Request semantics
authority-aware retrieval orchestration
source eligibility for execution context
relevance selection after authority eligibility
Context assembly
required vs optional treatment
representation / summarization safety
context budget / prioritization / overflow
Context Bundle / Context Manifest
context freshness / validity / invalidation / reassembly
Role/Run/Skill/Stage Context Views and isolation
context reuse
Run Working Memory
Task Working Memory
Retrieval Cache semantics
Governed Project Memory View interface
memory read/write/lifetime/invalidation
memory-to-knowledge promotion interface
cross-task/cross-project isolation semantics
Context/Memory failure semantics
Module-05 lifecycle/versioning semantics
```

## Module 05 does not own

| Concern | Canonical owner |
|---|---|
| project truth, fact scopes, canonical owner/source, normative conflicts, promotion | UPOS-01 |
| Role authority, Agent identity, SoD, handoff authority, Human Governance | UPOS-002 |
| Skill procedure / Skill evaluation | UPOS-003 |
| Workflow routing/state/stage order/retry-rework orchestration | UPOS-004 |
| Git/branch/commit/PR/merge mechanics | UPOS-006 |
| Review/QA evidence/verdict/gates | UPOS-007 |
| event/trace/metrics/dashboard/telemetry retention | UPOS-008 |
| organizational learning detection/promotion | UPOS-009 + UPOS-01 |
| access grants/secrets/security/protected-data policy | UPOS-010 |
| physical paths/providers/search/storage/model bindings | UPOS-011 |

## Boundary test

A rule belongs here when the central question is:

```text
What valid information should this bounded execution receive?
How is eligible information found, selected, represented, budgeted,
freshness-checked, isolated, and retained temporarily?
```

It does not belong here when the central question is:

```text
Which claim is project truth?
Who may decide it?
When does the Workflow transition?
What does QA PASS mean?
Who may read a secret?
Which vector database/search provider/path is used?
```

===== END VIRTUAL FILE: analysis/MODULE_05_OWNERSHIP_MAP.md =====


---

## VIRTUAL FILE 32/36 — `analysis/PROPOSED_PACKAGE_TREE.md`

**Virtual path:** `analysis/PROPOSED_PACKAGE_TREE.md`  
**Content checksum:** `04132ac85fe0`

===== BEGIN VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====

# Proposed Package Tree

**ID:** UPOS-05-AN-009  
**Type:** ANALYSIS / PACKAGE DESIGN  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


```text
05_context_memory/
├── README.md
├── CONTEXT_MEMORY_OPERATING_MODEL.md
├── CONTEXT_REQUIREMENT_AND_REQUEST_STANDARD.md
├── CONTEXT_BUNDLE_STANDARD.md
├── SOURCE_RESOLUTION_INTERFACE.md
├── RETRIEVAL_AND_SELECTION_STANDARD.md
├── CONTEXT_ASSEMBLY_STANDARD.md
├── CONTEXT_BUDGET_AND_REPRESENTATION.md
├── FRESHNESS_INVALIDATION_AND_REASSEMBLY.md
├── CONTEXT_ISOLATION_AND_VIEWS.md
├── CONTEXT_FAILURE_MODEL.md
├── MEMORY_TAXONOMY.md
├── MEMORY_READ_WRITE_STANDARD.md
├── MEMORY_LIFECYCLE_AND_INVALIDATION.md
├── PROJECT_MEMORY_INTERFACE.md
├── CONTEXT_MEMORY_LIFECYCLE.md
├── CROSS_MODULE_INTERFACES.md
├── MODULE_05_DEFINITION_OF_DONE.md
├── MODULE_05_TRACEABILITY.md
├── templates/
│   ├── CONTEXT_REQUIREMENT_TEMPLATE.md
│   ├── CONTEXT_REQUEST_TEMPLATE.md
│   ├── CONTEXT_BUNDLE_TEMPLATE.md
│   └── MEMORY_ITEM_TEMPLATE.md
└── analysis/
    ├── SOURCE_ANALYSIS.md
    ├── MODULE_05_OWNERSHIP_MAP.md
    ├── SOURCE_SECTION_DISPOSITION.md
    ├── CONTEXT_ENTITY_MODEL_ANALYSIS.md
    ├── RETRIEVAL_AUTHORITY_ANALYSIS.md
    ├── MEMORY_TAXONOMY_ANALYSIS.md
    ├── CONTEXT_ISOLATION_ANALYSIS.md
    ├── AMBIGUITY_GAP_REGISTER.md
    ├── PROPOSED_PACKAGE_TREE.md
    ├── IMPLEMENTATION_PLAN.md
    └── TRACEABILITY_VALIDATION.md

```

The candidate package is retained. The decomposition is sufficiently clean: Request/Bundle, Resolution/Retrieval, Assembly/Budget, Freshness/Isolation/Failure, and Memory are independent ownership slices without creating a second truth system.

===== END VIRTUAL FILE: analysis/PROPOSED_PACKAGE_TREE.md =====


---

## VIRTUAL FILE 33/36 — `analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md`

**Virtual path:** `analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md`  
**Content checksum:** `66f71c34f454`

===== BEGIN VIRTUAL FILE: analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md =====

# Retrieval Authority Analysis

**ID:** UPOS-05-AN-005  
**Type:** ANALYSIS / RETRIEVAL AUTHORITY  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** —

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Rejected model

```text
semantic similarity
→ highest score
→ treat as authoritative
```

Rejected because relevance is not authority.

## Adopted order

```text
1. bounded request/scope
2. UPOS-01 fact-scope + canonical-owner/source resolution
3. UPOS-010 permission/security constraints
4. UPOS-011 physical retrieval/provider mapping
5. project/scope/version/lifecycle eligibility
6. freshness/applicability assessment
7. epistemic/normativity preservation
8. relevance ranking within eligible candidates
9. required/optional obligation handling
10. budget/representation optimization
11. Context Manifest + Bundle
```

Invariant:

```text
HIGH RELEVANCE
MUST NOT OVERRIDE
LOWER AUTHORITY
```

## Required vs optional

`REQUIRED/OPTIONAL` is an obligation axis.

Context priority is a separate selection axis.

A required source cannot be removed simply because an optional item scores as more relevant.

## Source-not-found distinction

```text
SOURCE_NOT_FOUND
= retrieval/resolution attempt did not find the source

SOURCE_DOES_NOT_EXIST
= absence is established by canonical owner/source governance
```

The first MUST NOT be silently converted into the second.

## Retrieval technology

No vector database/search backend/model is canonicalized by Module 05.

===== END VIRTUAL FILE: analysis/RETRIEVAL_AUTHORITY_ANALYSIS.md =====


---

## VIRTUAL FILE 34/36 — `analysis/SOURCE_ANALYSIS.md`

**Virtual path:** `analysis/SOURCE_ANALYSIS.md`  
**Content checksum:** `3a9708165dbe`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====

# UPOS-005 Source Analysis

**ID:** UPOS-05-AN-001  
**Type:** ANALYSIS / SOURCE AUDIT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** ../MODULE_05_TRACEABILITY.md

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


## Inputs and authority

| Input | Role in Module 05 |
|---|---|
| UPOS-01 Documentation / Source-of-Truth / Knowledge Lifecycle | ACTIVE upstream governance; owns truth/canonicality/provenance/promotion |
| UPOS-002 Agent Organization v1.0 | frozen upstream organizational contract |
| UPOS-003 Skills System v1.0 | frozen upstream Skill Context interface |
| UPOS-004 Workflow Engine v1.0 | frozen upstream Task/Workflow/Stage identity/orchestration |
| Universal AI Agent Operating Model v1.0 | FROZEN MASTER DESIGN INPUT only |
| UPOS-005 implementation directive | Module-05 design/acceptance directive |

Hashes:

```text
Frozen master: f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699
UPOS-01 Source-of-Truth: 06913d3ba3585f2dd8676f2edc2ad82b43fad548b91e5fb57bec18a7c975bafd
UPOS-01 Knowledge Lifecycle: 5e1a7653f22c218820b2c675f6f34bcf6bef5ad139bb0ce1639acae14cc2d885
Directive: addcc8990f2a1480303605286494d8c80c1b2267ae5c5e7f7838ffd4661c4571
```

## Frozen master directly relevant sections

Strong direct semantics were found in:

- §31 Context assembly;
- §32 Context assembly order;
- §33 Context budget principle;
- §34 Memory model;
- §35 Project memory sources;
- §74 Handoff context minimization;
- §187 Sensitive context policy;
- §190 Reproducibility;
- §208 Reviewer context independence;
- §209 QA context independence;
- §210 Merge Controller context;
- §211 Product Owner context;
- §212 Decision packet;
- anti-pattern §221.4 Giant context dump;
- anti-pattern §221.6 Hidden project memory.

Mixed semantics also appear in Source-of-Truth principles, Agent/Skill/Workflow required sources, learning-vs-memory, secret handling, auditability, missing/stale truth, run lifecycle, evidence hierarchy, artifact retention, and privacy of reasoning.

## Upstream requirements extracted

From UPOS-01:

```text
resolve exact fact scope
→ canonical owner
→ ACTIVE normative sources
→ accepted decisions
→ local refinements
→ version/baseline applicability
→ implementation evidence
→ conflict/UNKNOWN rather than invention
```

From Knowledge Lifecycle:

```text
raw conversation history != project memory
project memory should primarily be governed project knowledge
promotion is explicit
freshness != validity
historical knowledge remains labeled
epistemic/provenance classes must be preserved
```

## P0 governance conflict result

No P0 conflict was found with frozen UPOS-01–04.

The directive is compatible with upstream contracts when Module 05 is implemented as an execution-context layer, not a truth store.

===== END VIRTUAL FILE: analysis/SOURCE_ANALYSIS.md =====


---

## VIRTUAL FILE 35/36 — `analysis/SOURCE_SECTION_DISPOSITION.md`

**Virtual path:** `analysis/SOURCE_SECTION_DISPOSITION.md`  
**Content checksum:** `d2befd5c2802`

===== BEGIN VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====

# Frozen Source Section Disposition

**ID:** UPOS-05-AN-003  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** ../MODULE_05_TRACEABILITY.md

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


**Frozen structural headings inspected:** 504  
**Extracted directly to Module 05:** 15  
**Mixed Context/Memory sections:** 46  
**Outside Module 05:** 443

`MIXED_EXTRACTED_AND_DEFERRED` means only Context/Memory semantics are extracted; remaining semantics stay with the indicated owner(s).

| Source unit | Line | Level | Section | Disposition | Remaining/deferred ownership |
|---|---:|---:|---|---|---|
| SRC-001 | 1 | 1 | Universal AI Agent Operating Model v1.0 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-002 | 17 | 1 | 0. Executive model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-001 |
| SRC-003 | 86 | 1 | 1. Relationship to the Documentation Operating Model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-001 |
| SRC-004 | 136 | 1 | 2. Project Agent Manifest | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-005 | 151 | 1 | Project Agent Manifest | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-006 | 224 | 1 | 3. Foundational principles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-007 | 226 | 2 | 3.1 Human governance | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-008 | 234 | 2 | 3.2 Separation of duties | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-009 | 254 | 2 | 3.3 Source of Truth before inference | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-010 | 260 | 2 | 3.4 No silent invention | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-011 | 291 | 2 | 3.5 Evidence before approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-012 | 313 | 2 | 3.6 Least privilege | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-013 | 319 | 2 | 3.7 Small coherent changes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-014 | 325 | 2 | 3.8 One PR, one intention | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-015 | 331 | 2 | 3.9 One commit, one logical change | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-016 | 337 | 2 | 3.10 No opportunistic refactoring by default | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-017 | 345 | 2 | 3.11 Risk-based governance | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-018 | 353 | 2 | 3.12 Organizational learning over hidden memory | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-019 | 371 | 1 | 4. Core terminology | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-020 | 373 | 2 | Agent | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-021 | 377 | 2 | Skill | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-022 | 391 | 2 | Workflow | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-023 | 404 | 2 | Orchestrator | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-024 | 408 | 2 | Guardrail | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-025 | 412 | 2 | Gate | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-026 | 416 | 2 | Handoff | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-027 | 420 | 2 | Project Memory | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-028 | 424 | 2 | Run | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-029 | 428 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-030 | 434 | 1 | 5. Universal Agent Contract | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-031 | 441 | 1 | Agent — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-032 | 443 | 2 | Identity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-033 | 446 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-034 | 449 | 2 | Owns | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-035 | 452 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-036 | 455 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-037 | 458 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-038 | 461 | 2 | Optional sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-039 | 464 | 2 | Tools | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-040 | 467 | 2 | Permissions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-041 | 470 | 2 | Skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-042 | 473 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-043 | 476 | 2 | Process | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-044 | 479 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-045 | 482 | 2 | Quality gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-046 | 485 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-047 | 488 | 2 | Handoffs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-048 | 491 | 2 | Prohibited behavior | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-049 | 497 | 1 | 6. Agent identity is not enough | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-050 | 521 | 1 | 7. Universal role families | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-051 | 559 | 1 | 8. Orchestrator | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-052 | 561 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-053 | 565 | 2 | Responsibilities | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-054 | 583 | 2 | Must not | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-055 | 594 | 1 | 9. Product Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-056 | 621 | 1 | 10. Domain / Architecture Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-057 | 648 | 1 | 11. UX / Product Design Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-058 | 671 | 1 | 12. Design System Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-059 | 689 | 1 | 13. Implementer Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-060 | 718 | 1 | 14. Reviewer Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-061 | 749 | 1 | 15. QA Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-062 | 773 | 1 | 16. Security Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-063 | 798 | 1 | 17. Documentation Guardian | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-064 | 821 | 1 | 18. Merge Controller | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-065 | 851 | 1 | 19. Skills model | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-066 | 870 | 1 | 20. Skill contract | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-067 | 875 | 1 | Skill — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-068 | 877 | 2 | Purpose | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-069 | 879 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-070 | 881 | 2 | Preconditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-071 | 883 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-072 | 885 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-073 | 887 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-074 | 889 | 2 | Quality criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-075 | 891 | 2 | Failure modes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-076 | 893 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-077 | 895 | 2 | Applicable roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-078 | 897 | 2 | Applicable risk classes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-079 | 902 | 1 | 21. Example universal skills | MIXED_EXTRACTED_AND_DEFERRED | UPOS-003 |
| SRC-080 | 933 | 1 | 22. Workflow contract | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-081 | 954 | 1 | 23. Change classification | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-082 | 971 | 1 | 24. C0 — Micro | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-083 | 996 | 1 | 25. C1 — Small | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-084 | 1018 | 1 | 26. C2 — Standard Feature | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-085 | 1043 | 1 | 27. C3 — Cross-cutting | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 |
| SRC-086 | 1070 | 1 | 28. C4 — Architectural | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-087 | 1097 | 1 | 29. C5 — High-risk | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-088 | 1128 | 1 | 30. Risk override rule | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-089 | 1144 | 1 | 31. Context assembly | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-090 | 1165 | 1 | 32. Context assembly order | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-091 | 1182 | 1 | 33. Context budget principle | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-092 | 1198 | 1 | 34. Memory model | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-093 | 1215 | 1 | 35. Project memory sources | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-094 | 1235 | 1 | 36. Learning is not hidden model training | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-095 | 1257 | 1 | 37. Learning promotion model | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-096 | 1290 | 1 | 38. Permissions model | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-097 | 1317 | 1 | 39. Default role permission philosophy | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-098 | 1319 | 2 | Orchestrator | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-099 | 1330 | 2 | Implementer | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-100 | 1342 | 2 | Reviewer | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-101 | 1353 | 2 | QA | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-102 | 1362 | 2 | Merge Controller | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-103 | 1374 | 1 | 40. Human approval model | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-104 | 1391 | 1 | 41. Recommended adoption mode | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-105 | 1411 | 1 | 42. Planning model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-004 |
| SRC-106 | 1434 | 1 | 43. Expected commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-107 | 1453 | 1 | 44. Git operating principles | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-108 | 1455 | 2 | 44.1 No direct push to protected main | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-109 | 1459 | 2 | 44.2 One branch per coherent task | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-110 | 1474 | 1 | 45. Atomic logical commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-111 | 1491 | 1 | 46. Bad commit granularity | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-112 | 1507 | 1 | 47. Bad oversized commit | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-113 | 1528 | 1 | 48. Commit categories | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-114 | 1548 | 1 | 49. Commit message contract | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-115 | 1566 | 1 | 50. Bug-fix commit strategy | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-116 | 1581 | 1 | 51. Review-fix commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-117 | 1591 | 1 | 52. PR operating model | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-118 | 1601 | 1 | 53. Good PR | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-119 | 1624 | 1 | 54. Bad PR | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-120 | 1640 | 1 | 55. PR size policy | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-004 |
| SRC-121 | 1656 | 1 | 56. PR description contract | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-122 | 1661 | 2 | Why | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-123 | 1663 | 2 | What | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-124 | 1665 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-125 | 1667 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-126 | 1669 | 2 | Risk class | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-127 | 1671 | 2 | Architecture/domain impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-128 | 1673 | 2 | API/data impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-129 | 1675 | 2 | UX/design impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-130 | 1677 | 2 | Security/privacy impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-131 | 1679 | 2 | Test evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-132 | 1681 | 2 | QA evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-133 | 1683 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-134 | 1685 | 2 | Rollback | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-135 | 1687 | 2 | Known limitations | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-136 | 1692 | 1 | 57. Creation loop | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-137 | 1707 | 1 | 58. Verification loop | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-138 | 1723 | 1 | 59. Self-check | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-139 | 1741 | 1 | 60. Independent review protocol | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-140 | 1758 | 1 | 61. Review finding severity | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-141 | 1778 | 1 | 62. Review output contract | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-142 | 1815 | 1 | 63. Reviewer independence | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-143 | 1831 | 1 | 64. QA protocol | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-144 | 1847 | 1 | 65. QA dimensions | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-145 | 1868 | 1 | 66. Documentation gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-146 | 1886 | 1 | 67. Architecture gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-147 | 1903 | 1 | 68. Security gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-148 | 1920 | 1 | 69. Database migration gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-149 | 1935 | 1 | 70. Merge readiness | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-150 | 1949 | 1 | 71. Merge authority | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-151 | 1966 | 1 | 72. Merge strategy | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-152 | 1982 | 1 | 73. Handoff protocol | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-153 | 2027 | 1 | 74. Handoff context minimization | EXTRACTED_TO_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-154 | 2042 | 1 | 75. Guardrails | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-155 | 2058 | 1 | 76. Guardrail types | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-156 | 2070 | 1 | 77. Escalation model | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-157 | 2087 | 1 | 78. Escalation targets | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-158 | 2101 | 1 | 79. Failure and recovery | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-159 | 2119 | 1 | 80. Retry policy | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-160 | 2137 | 1 | 81. Scope Guardian | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-161 | 2158 | 1 | 82. Concurrency model | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-162 | 2182 | 1 | 83. Task isolation | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-163 | 2202 | 1 | 84. Shared file collision | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-164 | 2216 | 1 | 85. Workflow — Micro Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-165 | 2237 | 1 | 86. Workflow — Bug Fix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-166 | 2255 | 1 | 87. Workflow — New Feature | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-167 | 2276 | 1 | 88. Workflow — UI Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-168 | 2292 | 1 | 89. Workflow — Design System Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-169 | 2308 | 1 | 90. Workflow — Architecture Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-170 | 2326 | 1 | 91. Workflow — API Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-171 | 2341 | 1 | 92. Workflow — Database Migration | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-172 | 2357 | 1 | 93. Workflow — Security Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-173 | 2372 | 1 | 94. Workflow — Refactor | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-174 | 2387 | 1 | 95. Workflow — Dependency Upgrade | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-175 | 2401 | 1 | 96. Workflow — Hotfix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-176 | 2421 | 1 | 97. Workflow — Documentation Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-177 | 2436 | 1 | 98. Workflow — Release | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-178 | 2452 | 1 | 99. Observability model | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-179 | 2485 | 1 | 100. Dashboard-ready metrics | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-180 | 2510 | 1 | 101. Do not optimize for activity | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-181 | 2525 | 1 | 102. Quality metrics | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-182 | 2542 | 1 | 103. Agent performance | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-183 | 2559 | 1 | 104. Agent learning record | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-184 | 2583 | 1 | 105. Skill evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-185 | 2604 | 1 | 106. Workflow evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-186 | 2617 | 1 | 107. Agent contract evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-187 | 2630 | 1 | 108. Model/provider independence | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-188 | 2648 | 1 | 109. Tool independence | MIXED_EXTRACTED_AND_DEFERRED | UPOS-011 |
| SRC-189 | 2665 | 1 | 110. Safety around secrets | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-190 | 2683 | 1 | 111. Production access | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-191 | 2695 | 1 | 112. Protected files | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-192 | 2711 | 1 | 113. Definition of Ready — task | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-193 | 2730 | 1 | 114. Definition of Ready — agent execution | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 / 005 / 006 / 007 |
| SRC-194 | 2746 | 1 | 115. Definition of Done — implementation | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-195 | 2760 | 1 | 116. Definition of Done — PR | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-196 | 2775 | 1 | 117. Definition of Done — workflow | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-197 | 2788 | 1 | 118. Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | UPOS-011 / cross-cutting |
| SRC-198 | 2864 | 1 | 119. Maturity model | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-199 | 2866 | 2 | Level 0 — Single Agent | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-200 | 2870 | 2 | Level 1 — Role Profiles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-201 | 2874 | 2 | Level 2 — Governed Workflows | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-202 | 2878 | 2 | Level 3 — Orchestrated Team | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-203 | 2882 | 2 | Level 4 — Automated Verification | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-204 | 2886 | 2 | Level 5 — Controlled Autonomy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-205 | 2890 | 2 | Level 6 — Learning Organization | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-206 | 2898 | 1 | 120. Recommended adoption sequence | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-207 | 2900 | 2 | Stage 1 — Documentation foundation | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-208 | 2904 | 2 | Stage 2 — Project Agent Manifest | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-209 | 2908 | 2 | Stage 3 — Three roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-210 | 2920 | 2 | Stage 4 — Add QA and Documentation Guardian | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-211 | 2924 | 2 | Stage 5 — Add specialist agents | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-212 | 2928 | 2 | Stage 6 — Formal workflows | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-213 | 2932 | 2 | Stage 7 — Telemetry | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-214 | 2936 | 2 | Stage 8 — Limited autonomous merge | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-215 | 2942 | 1 | 121. Recommended first implementation | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-216 | 2982 | 1 | 122. Universal Orchestrator algorithm | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 005 |
| SRC-217 | 3009 | 1 | 123. Authority conflict resolution | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-218 | 3028 | 1 | 124. Security veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-219 | 3038 | 1 | 125. Architecture veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-220 | 3051 | 1 | 126. Reviewer veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-221 | 3072 | 1 | 127. Human override | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-222 | 3091 | 1 | 128. Agent output discipline | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-223 | 3107 | 1 | 129. Change Classification output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-224 | 3137 | 1 | 130. Implementation Plan output | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-225 | 3174 | 1 | 131. Review Result output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-226 | 3206 | 1 | 132. QA Result output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-227 | 3232 | 1 | 133. Merge Readiness output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-228 | 3252 | 1 | 134. Change review feedback loop | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-229 | 3266 | 1 | 135. Oversized PR handling | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-230 | 3281 | 1 | 136. Scope expansion handling | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-231 | 3298 | 1 | 137. Unplanned architecture discovery | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-232 | 3313 | 1 | 138. Unplanned product ambiguity | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-233 | 3327 | 1 | 139. Unplanned security concern | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-234 | 3333 | 1 | 140. Documentation drift detection | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-235 | 3348 | 1 | 141. Agent sandbox hygiene | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-236 | 3368 | 1 | 142. Branch lifetime | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-237 | 3376 | 1 | 143. Stacked PRs | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-238 | 3384 | 1 | 144. Feature flags | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-239 | 3399 | 1 | 145. Rollback thinking | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-240 | 3411 | 1 | 146. Dependency graph awareness | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-241 | 3429 | 1 | 147. Cost awareness | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-242 | 3439 | 1 | 148. Latency awareness | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-243 | 3457 | 1 | 149. Human attention as scarce resource | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-244 | 3474 | 1 | 150. Agent communication rule | MIXED_EXTRACTED_AND_DEFERRED | UPOS-008 / 004 / 001 / 005 |
| SRC-245 | 3482 | 1 | 151. Decision preservation | MIXED_EXTRACTED_AND_DEFERRED | UPOS-008 / 004 / 001 / 005 |
| SRC-246 | 3499 | 1 | 152. No circular authority | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-247 | 3514 | 1 | 153. Independent model diversity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-248 | 3524 | 1 | 154. Review freshness | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-249 | 3532 | 1 | 155. Merge queue compatibility | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-250 | 3538 | 1 | 156. CI as evidence provider | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-251 | 3555 | 1 | 157. Agent-specific test ownership | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-252 | 3577 | 1 | 158. Test integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-253 | 3583 | 1 | 159. Snapshot integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-254 | 3589 | 1 | 160. Security scanner integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-255 | 3595 | 1 | 161. Linter suppression | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-256 | 3601 | 1 | 162. Technical debt creation | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-257 | 3609 | 1 | 163. Technical debt review | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-258 | 3623 | 1 | 164. Post-merge verification | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-259 | 3636 | 1 | 165. Post-merge learning trigger | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-260 | 3652 | 1 | 166. Incident integration | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-261 | 3667 | 1 | 167. Dashboard model | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-262 | 3690 | 1 | 168. Agent workload | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-263 | 3709 | 1 | 169. Workflow bottleneck analysis | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-264 | 3724 | 1 | 170. Maturity gates for autonomy | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-265 | 3740 | 1 | 171. Autonomy expansion | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-266 | 3755 | 1 | 172. Project-specific overrides | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-267 | 3769 | 1 | 173. Universal vs project-specific rules | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-268 | 3791 | 1 | 174. Agent manifests should be versioned | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-269 | 3807 | 1 | 175. Governance change workflow | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-270 | 3821 | 1 | 176. Universal starter agent set | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-271 | 3846 | 1 | 177. Universal full agent set | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-272 | 3874 | 1 | 178. Agent composition | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-273 | 3896 | 1 | 179. Universal policy files | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 003 / 004 |
| SRC-274 | 3913 | 1 | 180. AI Agent README | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-275 | 3927 | 1 | 181. Compatibility with AGENTS.md / tool-specific files | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 003 / 004 |
| SRC-276 | 3944 | 1 | 182. Universal file naming | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-277 | 3963 | 1 | 183. Agent contract versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-278 | 3975 | 1 | 184. Skill versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-279 | 3981 | 1 | 185. Workflow versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-280 | 3987 | 1 | 186. Telemetry retention | OUTSIDE_MODULE_05 | UPOS-008 / 010 |
| SRC-281 | 3993 | 1 | 187. Sensitive context policy | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-282 | 3999 | 1 | 188. Secret redaction | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-283 | 4005 | 1 | 189. Auditability | OUTSIDE_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-284 | 4019 | 1 | 190. Reproducibility | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-285 | 4035 | 1 | 191. Agent hallucination handling | OUTSIDE_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-286 | 4047 | 1 | 192. Missing Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-287 | 4060 | 1 | 193. Stale Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-288 | 4072 | 1 | 194. Feature lifecycle integration | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-289 | 4080 | 1 | 195. Agent lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-290 | 4095 | 1 | 196. Task lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-291 | 4114 | 1 | 197. PR lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-292 | 4120 | 1 | 198. Agent run lifecycle | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 006 |
| SRC-293 | 4136 | 1 | 199. Workflow state machine | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-294 | 4142 | 1 | 200. No hidden background authority | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-295 | 4148 | 1 | 201. Human pause points | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-296 | 4162 | 1 | 202. Plan change protocol | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-297 | 4174 | 1 | 203. Reclassification | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-298 | 4184 | 1 | 204. Risk inheritance | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-299 | 4190 | 1 | 205. Change decomposition | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-300 | 4196 | 1 | 206. Multi-agent code ownership | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-301 | 4202 | 1 | 207. Shared contract first | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-302 | 4215 | 1 | 208. Reviewer context independence | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-303 | 4233 | 1 | 209. QA context independence | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-304 | 4241 | 1 | 210. Merge Controller context | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-305 | 4249 | 1 | 211. Product Owner context | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-306 | 4266 | 1 | 212. Decision packet | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-307 | 4271 | 1 | Decision Required | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-308 | 4273 | 2 | Question | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-309 | 4275 | 2 | Why now | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-310 | 4277 | 2 | Option A | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-311 | 4279 | 2 | Option B | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-312 | 4281 | 2 | Trade-offs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-313 | 4283 | 2 | Risk | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-314 | 4285 | 2 | Reversibility | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-315 | 4287 | 2 | Recommended next step | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-316 | 4289 | 2 | Decision owner | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-317 | 4294 | 1 | 213. Do not fake consensus | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-318 | 4302 | 1 | 214. Conflict resolution by authority | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-319 | 4317 | 1 | 215. Majority voting | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-320 | 4323 | 1 | 216. Agent confidence | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-321 | 4331 | 1 | 217. Evidence hierarchy | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-322 | 4350 | 1 | 218. Change evidence bundle | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-323 | 4367 | 1 | 219. Artifact retention | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-008 / UPOS-010 |
| SRC-324 | 4390 | 1 | 220. Privacy of reasoning | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-008 / UPOS-010 |
| SRC-325 | 4398 | 1 | 221. Universal anti-patterns | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-326 | 4400 | 2 | 221.1 Agent swarm without ownership | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-327 | 4404 | 2 | 221.2 Self-approval | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-328 | 4408 | 2 | 221.3 Every task runs every agent | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-329 | 4412 | 2 | 221.4 Giant context dump | EXTRACTED_TO_MODULE_05 | Cross-cutting anti-patterns |
| SRC-330 | 4416 | 2 | 221.5 Prompt duplication | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-331 | 4420 | 2 | 221.6 Hidden project memory | EXTRACTED_TO_MODULE_05 | Cross-cutting anti-patterns |
| SRC-332 | 4424 | 2 | 221.7 Activity metrics | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-333 | 4428 | 2 | 221.8 AI-created architecture by accident | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-334 | 4432 | 2 | 221.9 Fake review | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-335 | 4436 | 2 | 221.10 Git history as keystroke log | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-336 | 4442 | 1 | 222. Governance health checks | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-337 | 4459 | 1 | 223. Quarterly / milestone review | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-338 | 4475 | 1 | 224. Universal adoption checklist | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting governance |
| SRC-339 | 4494 | 1 | 225. Minimal viable agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-340 | 4513 | 1 | 226. Intermediate agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-341 | 4531 | 1 | 227. Advanced agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-342 | 4550 | 1 | 228. Final operating model | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting governance |
| SRC-343 | 4600 | 1 | Appendix A — Project Agent Manifest template | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-344 | 4603 | 1 | Project Agent Manifest | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-345 | 4608 | 2 | Project | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-346 | 4614 | 2 | Sources of Truth | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-347 | 4631 | 2 | Commands | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-348 | 4644 | 2 | Git | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-349 | 4651 | 2 | Risk-sensitive areas | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-350 | 4660 | 2 | Human approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-351 | 4668 | 2 | Protected paths | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-352 | 4672 | 2 | Agent runtime notes | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-353 | 4679 | 1 | Appendix B — Agent Contract template | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-354 | 4682 | 1 | Agent — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-355 | 4687 | 2 | Identity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-356 | 4689 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-357 | 4691 | 2 | Owns | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-358 | 4693 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-359 | 4695 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-360 | 4697 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-361 | 4699 | 2 | Tools | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-362 | 4701 | 2 | Permissions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-363 | 4703 | 2 | Skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-364 | 4705 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-365 | 4707 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-366 | 4709 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-367 | 4711 | 2 | Quality gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-368 | 4713 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-369 | 4715 | 2 | Handoffs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-370 | 4717 | 2 | Prohibited behavior | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-371 | 4722 | 1 | Appendix C — Skill template | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-372 | 4725 | 1 | Skill — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-373 | 4730 | 2 | Purpose | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-374 | 4732 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-375 | 4734 | 2 | Preconditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-376 | 4736 | 2 | Sources | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-377 | 4738 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-378 | 4744 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-379 | 4746 | 2 | Quality criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-380 | 4748 | 2 | Failure modes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-381 | 4750 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-382 | 4752 | 2 | Roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-383 | 4757 | 1 | Appendix D — Workflow template | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-384 | 4760 | 1 | Workflow — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-385 | 4765 | 2 | Trigger | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-386 | 4767 | 2 | Applicable risk classes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-387 | 4769 | 2 | Entry conditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-388 | 4771 | 2 | Required roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-389 | 4773 | 2 | Required skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-390 | 4775 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-391 | 4777 | 2 | Steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-392 | 4783 | 2 | Parallel steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-393 | 4785 | 2 | Gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-394 | 4787 | 2 | Human approvals | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-395 | 4789 | 2 | Failure handling | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-396 | 4791 | 2 | Completion criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-397 | 4793 | 2 | Telemetry | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-398 | 4798 | 1 | Appendix E — Change Plan template | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-399 | 4801 | 1 | Change Plan — <Task> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-400 | 4803 | 2 | Goal | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-401 | 4805 | 2 | Risk class | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-402 | 4807 | 2 | Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-403 | 4809 | 2 | Affected domains | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-404 | 4811 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-405 | 4813 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-406 | 4815 | 2 | Implementation steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-407 | 4817 | 2 | Tests | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-408 | 4819 | 2 | Expected commits | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-409 | 4821 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-410 | 4823 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-411 | 4825 | 2 | Rollback | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-412 | 4827 | 2 | Open questions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-413 | 4832 | 1 | Appendix F — Handoff template | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-414 | 4835 | 1 | Handoff | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-415 | 4840 | 2 | Task | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-416 | 4842 | 2 | Context | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-417 | 4844 | 2 | Canonical sources | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-418 | 4846 | 2 | Decisions already made | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-419 | 4848 | 2 | Constraints | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-420 | 4850 | 2 | Open questions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-421 | 4852 | 2 | Expected output | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-422 | 4854 | 2 | Authority | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-423 | 4856 | 2 | Prohibited changes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-424 | 4861 | 1 | Appendix G — Review Result template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-425 | 4864 | 1 | Review Result | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-426 | 4868 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-427 | 4871 | 2 | Correctness | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-428 | 4874 | 2 | Architecture | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-429 | 4877 | 2 | Domain semantics | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-430 | 4880 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-431 | 4883 | 2 | Testing | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-432 | 4886 | 2 | UX / Accessibility | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-433 | 4889 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-434 | 4892 | 2 | Findings | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-435 | 4894 | 3 | BLOCKING | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-436 | 4896 | 3 | MAJOR | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-437 | 4898 | 3 | MINOR | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-438 | 4900 | 3 | NIT | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-439 | 4905 | 1 | Appendix H — QA Result template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-440 | 4908 | 1 | QA Result | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-441 | 4912 | 2 | Acceptance criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-442 | 4914 | 2 | Scenarios executed | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-443 | 4916 | 2 | Negative scenarios | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-444 | 4918 | 2 | Regression coverage | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-445 | 4920 | 2 | Failures | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-446 | 4922 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-447 | 4924 | 2 | Residual risk | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-448 | 4929 | 1 | Appendix I — Merge Readiness template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-449 | 4932 | 1 | Merge Readiness | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-450 | 4936 | 2 | CI | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-451 | 4938 | 2 | Review | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-452 | 4940 | 2 | QA | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-453 | 4942 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-454 | 4944 | 2 | Architecture | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-455 | 4946 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-456 | 4948 | 2 | Branch status | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-457 | 4950 | 2 | Human approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-458 | 4952 | 2 | Missing requirements | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-459 | 4957 | 1 | Appendix J — Risk Classification Matrix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-460 | 4970 | 1 | Appendix K — Permission Matrix example | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-461 | 4985 | 1 | Appendix L — Git Policy starter | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-462 | 4988 | 1 | Git Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-463 | 4990 | 2 | Protected branches | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-464 | 4994 | 2 | Branches | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-465 | 4998 | 2 | Commits | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-466 | 5006 | 2 | Pull Requests | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-467 | 5010 | 2 | Review | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-468 | 5014 | 2 | Merge | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-469 | 5021 | 1 | Appendix M — Review Policy starter | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-470 | 5024 | 1 | Review Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-471 | 5026 | 2 | Reviewer objective | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-472 | 5030 | 2 | Severity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-473 | 5037 | 2 | Independence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-474 | 5041 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-475 | 5048 | 1 | Appendix N — Human Approval Policy starter | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-476 | 5051 | 1 | Human Approval Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-477 | 5073 | 1 | Appendix O — Example New Feature workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-478 | 5115 | 1 | Appendix P — Example Bug Fix workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-479 | 5140 | 1 | Appendix Q — Example Architecture Change workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-480 | 5174 | 1 | Appendix R — Learning Record template | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-481 | 5177 | 1 | Learning — <Title> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-482 | 5179 | 2 | Trigger | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-483 | 5181 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-484 | 5183 | 2 | Root cause | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-485 | 5185 | 2 | Why systemic | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-486 | 5187 | 2 | New rule | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-487 | 5189 | 2 | Updated skill | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-488 | 5191 | 2 | Updated workflow | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-489 | 5193 | 2 | New test / guardrail | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-490 | 5195 | 2 | Owner | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-491 | 5197 | 2 | Status | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-492 | 5202 | 1 | Appendix S — Telemetry schema starter | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-493 | 5229 | 1 | Appendix T — Adoption directive for an existing project | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting adoption |
| SRC-494 | 5279 | 1 | Final principles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-495 | 5281 | 2 | 1 | OUTSIDE_MODULE_05 | UPOS-001 |
| SRC-496 | 5285 | 2 | 2 | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-497 | 5289 | 2 | 3 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-498 | 5293 | 2 | 4 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-499 | 5297 | 2 | 5 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-500 | 5301 | 2 | 6 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-501 | 5305 | 2 | 7 | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-502 | 5309 | 2 | 8 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-503 | 5313 | 2 | 9 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-504 | 5317 | 2 | 10 | OUTSIDE_MODULE_05 | UPOS-002 |

===== END VIRTUAL FILE: analysis/SOURCE_SECTION_DISPOSITION.md =====


---

## VIRTUAL FILE 36/36 — `analysis/TRACEABILITY_VALIDATION.md`

**Virtual path:** `analysis/TRACEABILITY_VALIDATION.md`  
**Content checksum:** `dc265962a251`

===== BEGIN VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====
# UPOS-005 Traceability Validation

**ID:** UPOS-05-AN-012  
**Type:** VALIDATION REPORT  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** ../MODULE_05_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-005 v1.0 validation state at freeze time. It is not timeless normative truth.

## Results

| Check | Result |
|---|---|
| Required canonical normative files present | PASS |
| Directive sections §0–§94 mapped | PASS |
| Stable `context_request_id` | PASS |
| Stable `context_bundle_id` | PASS |
| Stable `memory_item_id` | PASS |
| Context Request attribution contract | PASS |
| Context Bundle contract | PASS |
| Context Requirement template conforms to Standard | PASS |
| Context Request template conforms to Standard | PASS |
| Context Bundle template conforms to Standard | PASS |
| Memory Item template conforms to Standard | PASS |
| Mandatory normative field exists only in Standard without Template representation | 0 |
| Required-source satisfaction explicit | PASS |
| Bundle immutable consumed snapshot | PASS |
| Reassembly creates new Bundle identity | PASS |
| Authority-aware retrieval before relevance | PASS |
| Required source protected from budget omission | PASS |
| Context representation / derived summary safety | PASS |
| Context freshness / invalidation / reassembly | PASS |
| Context View / Reviewer independence | PASS |
| Cross-project / cross-task isolation | PASS |
| Context failure taxonomy | PASS |
| Memory taxonomy | PASS |
| Governed Project Memory View boundary | PASS |
| `SKL-ASSEMBLE-CONTEXT` upstream interface found | PASS |
| UPOS-004 Task/Routing/Workflow/Stage identities found | PASS |
| Hard-coded physical provider/project-path bindings | 0 |
| Analysis artifacts historical EVIDENCE | PASS |
| Unresolved P0/P1 Module-05 gaps | 0 |

```text
UNMAPPED MODULE-05 SOURCE REQUIREMENTS = 0
```

## Ownership validation

- project truth/canonicality/promotion remain UPOS-01: **PASS**
- Role authority/Agent/SoD remain UPOS-002: **PASS**
- Skill procedure remains UPOS-003: **PASS**
- Workflow orchestration remains UPOS-004: **PASS**
- Git/PR/merge remains UPOS-006: **PASS**
- Quality verdict/evidence semantics remain UPOS-007: **PASS**
- telemetry/event/metrics remain UPOS-008: **PASS**
- learning promotion remains UPOS-009 + UPOS-01: **PASS**
- permissions/security policy remain UPOS-010: **PASS**
- physical source/provider/storage/model bindings remain UPOS-011: **PASS**

```text
NO KNOWN OWNERSHIP LEAKAGE INTO
UPOS-01 / 02 / 03 / 04 / 06–11
```

## Critical invariants

```text
MEMORY != TRUTH
CONTEXT != TRUTH
CACHE != TRUTH
DERIVED_SUMMARY != CANONICAL_SOURCE
RAW_CHAT_HISTORY != PROJECT_MEMORY
PROVIDER_PRIVATE_MEMORY != PROJECT_KNOWLEDGE
```

**PASS**

## Verdict

PASS — UPOS-005 Context & Memory v1.0 satisfies source governance, retrieval, assembly, budget, freshness, isolation, failure, memory, traceability, operational-template conformance and boundary gates.

UPOS-005 v1.0 is frozen as the canonical Module 05 baseline.
===== END VIRTUAL FILE: analysis/TRACEABILITY_VALIDATION.md =====
