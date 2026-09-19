# Skill Registry Standard

**ID:** UPOS-03-REG-001  
**Type:** REGISTRY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-003 Skills System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** skills/*.md


## 1. Purpose

The Skill Registry is the canonical human-readable index/discovery layer for active and historical Skill Definitions.

It MUST NOT duplicate entire Skill Contracts.

## 2. Required registry fields

```text
skill_id
name
version
status
category
purpose
applicable_roles
dependencies
supersedes
replacement
contract_ref
```

## 3. Registry semantics

- one row identifies one Skill Definition version;
- `contract_ref` points to the canonical Skill Contract;
- applicable roles are capability compatibility, not authority grants;
- dependency summary is an index, not the normative dependency definition;
- supersession/replacement fields must agree with lifecycle/versioning documents.

## 4. Disposition metadata

The Registry MAY contain a `disposition` field in addition to the mandatory registry fields.

For v1 the canonical values are:

```text
CANONICAL_UNIVERSAL_SKILL
INTERFACE_SKILL
```

Their normative meanings are defined in `SKILLS_OPERATING_MODEL.md`.

Registry consumers MUST NOT treat `INTERFACE_SKILL` as:

```text
lifecycle status
quality downgrade
temporary status
authority delegation
```

It means only that correct execution depends on authoritative semantics supplied by another U-POS module through an explicit interface.

## 5. Machine-readable registry

A future machine-readable registry MAY mirror these index fields through the cross-cutting U-POS schemas/runtime layer.

It MUST remain traceable to normative Markdown and MUST NOT become an independent semantic source.

## 6. v1 registry

| skill_id | name | version | status | category | purpose | applicable_roles | dependencies | supersedes | replacement | contract_ref | disposition |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| `SKL-ANALYZE-IMPACT` | `analyze-impact` | 1.0.0 | ACTIVE | `analysis` | Analyze the bounded impact of a proposed or implemented change across declared project scopes. | Product, Domain, Architecture, Implementer, Reviewer, Security, Documentation Guardian | none | none | none | `skills/analyze-impact.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-ANALYZE-INCIDENT` | `analyze-incident` | 1.0.0 | ACTIVE | `operations` | Produce evidence-backed incident analysis separating observed facts, hypotheses, contributing causes and follow-up candidates. | DevOps / SRE, Architecture, Security, Implementer, QA | OPTIONALLY_USES analyze-impact | none | none | `skills/analyze-incident.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-ASSEMBLE-CONTEXT` | `assemble-context` | 1.0.0 | ACTIVE | `governance` | Request and organize a task-appropriate context bundle through the canonical Context interface. | Orchestrator, Implementer, Reviewer, QA, Architecture, Product, Security | none | none | none | `skills/assemble-context.md` | INTERFACE_SKILL |
| `SKL-ASSESS-MERGE-READINESS` | `assess-merge-readiness` | 1.0.0 | ACTIVE | `governance` | Collect and assess whether required readiness evidence appears present, deferring final readiness semantics/authority to UPOS-007/002/010. | Merge Controller, Reviewer, QA | none | none | none | `skills/assess-merge-readiness.md` | INTERFACE_SKILL |
| `SKL-CAPTURE-LEARNING` | `capture-learning` | 1.0.0 | ACTIVE | `governance` | Transform an evidence-backed recurring/systemic observation into a structured Learning Candidate without promoting it. | Documentation Guardian, Reviewer, QA, Architecture, Security, Orchestrator | none | none | none | `skills/capture-learning.md` | INTERFACE_SKILL |
| `SKL-CLASSIFY-CHANGE` | `classify-change` | 1.0.0 | ACTIVE | `classification` | Produce a structured change-classification recommendation against the canonical classification model. | Orchestrator, Product, Architecture, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/classify-change.md` | INTERFACE_SKILL |
| `SKL-CREATE-ADR` | `create-adr` | 1.0.0 | ACTIVE | `specification` | Record an architecture-oriented decision in the project's ADR format after the decision authority is established. | Architecture, Domain, Security | none | none | none | `skills/create-adr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-ATOMIC-COMMIT` | `create-atomic-commit` | 1.0.0 | ACTIVE | `implementation` | Assess a staged logical change against the external atomic-commit standard and prepare a commit request/metadata. | Implementer | none | none | none | `skills/create-atomic-commit.md` | INTERFACE_SKILL |
| `SKL-CREATE-DDR` | `create-ddr` | 1.0.0 | ACTIVE | `specification` | Record a design/UX/design-system decision under the project's DDR convention after valid authority exists. | UX / Product Design, Design System | none | none | none | `skills/create-ddr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-FEATURE-SPEC` | `create-feature-spec` | 1.0.0 | ACTIVE | `specification` | Draft or update a bounded feature specification from approved Product intent and authoritative constraints. | Product, Domain, Architecture, UX | OPTIONALLY_USES analyze-impact | none | none | `skills/create-feature-spec.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-IMPLEMENTATION-PLAN` | `create-implementation-plan` | 1.0.0 | ACTIVE | `planning` | Translate an approved bounded change into a coherent implementation plan without changing approved semantics. | Architecture, Implementer, Orchestrator | OPTIONALLY_USES analyze-impact | none | none | `skills/create-implementation-plan.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-PDR` | `create-pdr` | 1.0.0 | ACTIVE | `specification` | Record a product decision using the project PDR convention after valid Product authority exists. | Product | none | none | none | `skills/create-pdr.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-CREATE-RFC` | `create-rfc` | 1.0.0 | ACTIVE | `specification` | Produce a structured proposal for a material design/architecture/technical change requiring review before decision. | Architecture, Domain, Security, Product, Design System | OPTIONALLY_USES analyze-impact | none | none | `skills/create-rfc.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-IMPLEMENT-CHANGE` | `implement-change` | 1.0.0 | ACTIVE | `implementation` | Execute one bounded approved implementation change while preserving scope and authoritative contracts. | Implementer | OPTIONALLY_USES analyze-impact, OPTIONALLY_USES write-regression-test | none | none | `skills/implement-change.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-PREPARE-RELEASE` | `prepare-release` | 1.0.0 | ACTIVE | `operations` | Prepare a bounded release package/readiness set from an already selected release candidate without owning deployment Workflow sequencing. | DevOps / SRE, Implementer, Documentation Guardian | none | none | none | `skills/prepare-release.md` | INTERFACE_SKILL |
| `SKL-QA-VALIDATION` | `qa-validation` | 1.0.0 | ACTIVE | `verification` | Exercise intended behavior against acceptance/user/regression scenarios and return observations/evidence for the external QA verdict model. | QA | none | none | none | `skills/qa-validation.md` | INTERFACE_SKILL |
| `SKL-RECONCILE-DOCUMENTATION` | `reconcile-documentation` | 1.0.0 | ACTIVE | `governance` | Identify documentation impact of a bounded change and update/propose updates to the correct canonical owners without redefining project truth. | Documentation Guardian, Implementer, Product, Architecture | OPTIONALLY_USES analyze-impact | none | none | `skills/reconcile-documentation.md` | INTERFACE_SKILL |
| `SKL-REPRODUCE-BUG` | `reproduce-bug` | 1.0.0 | ACTIVE | `analysis` | Produce a controlled, evidence-backed reproduction of an observed defect or explicitly report that reproduction was not achieved. | Implementer, Reviewer, QA | none | none | none | `skills/reproduce-bug.md` | CANONICAL_UNIVERSAL_SKILL |
| `SKL-REVIEW-ARCHITECTURE` | `review-architecture` | 1.0.0 | ACTIVE | `verification` | Evaluate a proposed/implemented change for conformance with canonical architecture contracts and decision boundaries. | Architecture, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/review-architecture.md` | INTERFACE_SKILL |
| `SKL-REVIEW-DIFF` | `review-diff` | 1.0.0 | ACTIVE | `verification` | Perform a bounded technical review of a change diff against authoritative contracts and externally owned quality semantics. | Reviewer, Architecture, Security, Domain, UX / Product Design, Design System | OPTIONALLY_USES analyze-impact | none | none | `skills/review-diff.md` | INTERFACE_SKILL |
| `SKL-REVIEW-SECURITY` | `review-security` | 1.0.0 | ACTIVE | `verification` | Assess a bounded change for security risks and contract conformance using externally owned Security authority/policy. | Security, Reviewer | OPTIONALLY_USES analyze-impact | none | none | `skills/review-security.md` | INTERFACE_SKILL |
| `SKL-WRITE-REGRESSION-TEST` | `write-regression-test` | 1.0.0 | ACTIVE | `implementation` | Create a focused automated test that proves a known defect/contract regression and protects the corrected behavior. | Implementer, Reviewer, QA | OPTIONALLY_USES reproduce-bug | none | none | `skills/write-regression-test.md` | CANONICAL_UNIVERSAL_SKILL |
