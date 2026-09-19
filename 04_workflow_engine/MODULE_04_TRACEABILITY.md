# Module 04 Traceability

**ID:** UPOS-04-TRC-001  
**Type:** TRACEABILITY / NORMATIVE COVERAGE  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** analysis/SOURCE_SECTION_DISPOSITION.md, analysis/TRACEABILITY_VALIDATION.md


**Frozen source SHA-256:** `f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699`  
**Implementation directive SHA-256:** `7c8465f949ef875e88c98044f051cb5a49f52e332e626316c91f35486536685b`

## Traceability rule

Each Module-04 requirement maps:

```text
stable requirement ID
→ frozen source / implementation directive section
→ extracted semantic requirement
→ canonical Module 04 artifact
```

Mixed source sections extract only Workflow-owned semantics; remaining semantics are deferred.

## Requirements

| Requirement | Source | Extracted requirement | Canonical artifact |
|---|---|---|---|
| `WFL-REQ-001` | §3.11 | Process depth must be risk-based; trivial and high-risk changes must not use identical orchestration depth. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-002` | §22, Appendix D | Every production Workflow must define trigger/applicability, entry/exit conditions, risk classes, Roles, Skills, sources, steps/stages, parallelism, external gates, human approvals, failure handling, completion and observability interfaces. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-003` | §23 | Canonical Change Classes are C0 Micro, C1 Small, C2 Standard, C3 Cross-cutting, C4 Architectural, C5 High-risk. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-004` | §24 | C0 represents micro/isolated low-risk work and normally uses minimal orchestration depth. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-005` | §25 | C1 represents small bounded work with independent review and lightweight validation. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-006` | §26 | C2 represents standard feature/change work inside existing architecture with normal review/QA/docs orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-007` | §27 | C3 represents cross-cutting work spanning multiple layers/contexts and requires integration-aware orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-008` | §28 | C4 represents durable architectural change and requires architecture decision orchestration including RFC/review/human/ADR references. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-009` | §29 | C5 represents high-risk change such as auth/authz/billing/destructive data/privacy/secrets/production migration/security boundary/irreversible AI action and requires enhanced protected orchestration. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-010` | §30 | Classification is based on impact, not line count; small diffs may be high-risk. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-011` | §79 | Workflow failure handling must support explicit recovery options such as retry, re-plan, reassign, split, rollback reference, abort or human escalation. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-012` | §80 | Retries must be bounded; exact thresholds may be project-specific and repeated failure should trigger re-plan/escalation rather than indefinite loops. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-013` | §85 | Frozen Micro Change semantics are preserved as GENERIC_CHANGE routed at C0 with lightweight implementation/review/readiness depth. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-014` | §86, Appendix P | Bug Fix orchestration includes reproduction, regression test where practical, plan/fix, independent review, QA, conditional docs and readiness. | `workflows/bug-fix.md` |
| `WFL-REQ-015` | §87, Appendix O | Feature orchestration includes Product/spec, impact analysis, classification, plan, implementation, independent review, QA, conditional Security/docs and readiness/human references. | `workflows/feature.md` |
| `WFL-REQ-016` | §88 | UI Change semantics are modeled as a UI Concern Profile applied to the selected base Work Type rather than a competing Workflow. | `profiles/ui.md` |
| `WFL-REQ-017` | §89 | Design System Change semantics are modeled as a Design System Concern Profile with registry/reuse decision, DS review, spec/implementation, visual QA and migration/deprecation references. | `profiles/design-system.md` |
| `WFL-REQ-018` | §90, Appendix Q | Architecture Change semantics are modeled as an Architecture Profile; durable architecture changes require C4 and RFC/review/human/ADR/migration planning orchestration. | `profiles/architecture.md` |
| `WFL-REQ-019` | §91 | API Change semantics are modeled as an API Profile with contract impact, backward compatibility/versioning, tests/consumer/docs checkpoints. | `profiles/api.md` |
| `WFL-REQ-020` | §92 | Database Migration semantics are modeled as a Database Migration Profile with data impact, migration/compatibility, backup/recovery, verification and rollback/forward-fix references. | `profiles/database-migration.md` |
| `WFL-REQ-021` | §93 | Security Change semantics are modeled as a Security Profile with threat/security design, approval, security review, QA and audit/evidence references. | `profiles/security.md` |
| `WFL-REQ-022` | §94 | Refactor Work Type must state behavior-preservation intent/reason/scope and must not silently mix unrelated feature change. | `workflows/refactor.md` |
| `WFL-REQ-023` | §95 | Dependency Upgrade Work Type must analyze breaking/security implications and include build/test/regression orchestration references. | `workflows/dependency-upgrade.md` |
| `WFL-REQ-024` | §96 | Hotfix is recovery-optimized but must not skip safety; it uses expedited independent review/validation/human/release follow-up as required. | `workflows/hotfix.md` |
| `WFL-REQ-025` | §97 | Documentation Change Work Type checks canonical ownership, updates documentation, validates links/contradictions/review, and avoids code gates unless behavior/generated docs require them. | `workflows/documentation-change.md` |
| `WFL-REQ-026` | §98 | Release Work Type orchestrates release candidate checks, migration/release notes/security/ops/human checkpoints, deployment reference, verification and rollback if needed. | `workflows/release.md` |
| `WFL-REQ-027` | §122 | Routing conceptually resolves project sources/outcome/classification/affected domains/workflow/roles/human gates/context before execution and handles conflict/gate failure explicitly. | `ROUTING_STANDARD.md` |
| `WFL-REQ-028` | §129 | Change Classification output/routing decision must be structured and attributable, including class, rationale, affected concerns/specialists and gate implications. | `ROUTING_STANDARD.md` |
| `WFL-REQ-029` | §136 | Material scope expansion requires pause and classification of discovered work; no silent expansion. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-030` | §146 | Workflow orchestration must model dependencies and parallelize only independent nodes. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-031` | §185 | Workflow Definition version must change when required gates or sequence materially changes. | `WORKFLOW_LIFECYCLE_AND_VERSIONING.md` |
| `WFL-REQ-032` | §194 | Workflow/task status is distinct from Product feature lifecycle and must not reuse feature enums. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-033` | §196 | Task lifecycle must be explicit and distinct from Workflow Instance/Agent Run/PR/product lifecycles. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-034` | §199 | Workflow automation requires an explicit legal state-transition model. | `WORKFLOW_STATE_MODEL.md` |
| `WFL-REQ-035` | §202 | Material implementation-plan change requires reason/update and reclassification if risk/impact changes. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-036` | §203 | Upward reclassification must be supported; downward reclassification requires evidence. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-037` | §204 | Risk inheritance applies to inseparable critical sub-changes; C5 may elevate the containing route. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-038` | §205 | Change decomposition is by coherent ownership/dependency, not arbitrary file count. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-039` | §207 | Cross-boundary parallel implementation should establish shared contracts before dependent parallel stages execute. | `PARALLELISM_AND_DEPENDENCY_ORCHESTRATION.md` |
| `WFL-REQ-040` | §221.3 | Workflow routing must not run every agent for every task; only justified Roles/Skills participate. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-041` | Appendix D | Workflow template semantics are normalized into the canonical Workflow Contract Standard. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-042` | Appendix J | Risk matrix intent is consumed for orchestration depth, while Review/QA/Human semantics remain owned by external modules. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-043` | Appendix O | Example New Feature route is preserved by the Feature base workflow plus applied concerns/classification. | `workflows/feature.md` |
| `WFL-REQ-044` | Appendix P | Example Bug Fix route is preserved by the Bug Fix base workflow. | `workflows/bug-fix.md` |
| `WFL-REQ-045` | Appendix Q | Example Architecture Change route is preserved by Base Workflow + Architecture Profile + C4 classification. | `profiles/architecture.md` |
| `WFL-REQ-046` | Final principle 4 | Risk determines process depth. | `WORKFLOW_OPERATING_MODEL.md` |
| `WFL-REQ-047` | Implementation directive §2–3 | Task, Change Class, Work Type, Concern, Workflow Definition, Profile, Instance, Stage, Transition, Gate Reference, Routing Decision and Workflow Result are distinct concepts. | `README.md` |
| `WFL-REQ-048` | Implementation directive §3 | Routing uses three independent axes: Change Class, Work Type, and Concerns, composed as Base Workflow + Profiles + Class. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-049` | Implementation directive §3 | UI, Design System, Architecture, API, Database and Security are Concern Profiles rather than mutually exclusive primary Workflows in v1. | `WORK_TYPE_AND_CONCERN_MODEL.md` |
| `WFL-REQ-050` | Implementation directive §7 | Classification dimensions must carry provenance SOURCE_DERIVED / TASK_DIRECTIVE_REFINEMENT / NEW_PROPOSAL. | `CHANGE_CLASSIFICATION_STANDARD.md` |
| `WFL-REQ-051` | Implementation directive §8 | classify-change Skill produces a recommendation; UPOS-004 owns canonical class semantics and routing. | `ROUTING_STANDARD.md` |
| `WFL-REQ-052` | Implementation directive §9 | Material new facts invalidate stale classification and trigger pause/reclassification/rerouting checks. | `RECLASSIFICATION_AND_REROUTING.md` |
| `WFL-REQ-053` | Implementation directive §10 | Workflow contracts reference Roles/Skills/gates/approvals without copying their owned semantics. | `WORKFLOW_CONTRACT_STANDARD.md` |
| `WFL-REQ-054` | Implementation directive §11 | Workflow Definition and Workflow Instance are distinct; each Instance is attributable to Definition/version, Task, routing/classification/work type/concerns/stages/roles/skills/gates. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-055` | Implementation directive §12 | Workflow Definition lifecycle is distinct from Workflow Instance execution state. | `WORKFLOW_LIFECYCLE_AND_VERSIONING.md` |

| `WFL-REQ-056` | Final reconciliation directive §2 | Every Routing Decision has stable `routing_decision_id` independent from Task/Workflow Instance and suitable for provenance. | `ROUTING_STANDARD.md`, `templates/ROUTING_DECISION_TEMPLATE.md` |
| `WFL-REQ-057` | Final reconciliation directive §2 | Every Task and Workflow Instance has stable semantic identity: `task_id` and `workflow_instance_id`. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md` |
| `WFL-REQ-058` | Final reconciliation directive §2 | Every canonical/resolved Stage and every declared Transition is independently addressable by stable `stage_id` / `transition_id` (or explicitly deterministic equivalent). | `WORKFLOW_CONTRACT_STANDARD.md`, `WORKFLOW_STATE_MODEL.md`, `workflows/*.md`, `profiles/*.md` |
| `WFL-REQ-059` | Final reconciliation directive §3 | Retry, Rework, Recovery, Reclassification, Rerouting and Escalation are distinct orchestration concepts and MUST NOT be conflated. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-060` | Final reconciliation directive §4 | Retry and rework are both bounded; non-convergence/exhaustion requires a controlled transition rather than an infinite loop. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-061` | Final reconciliation directive §5 | Workflow failure taxonomy includes transient execution, contract, missing truth, canonical conflict, authority conflict, scope expansion, risk discovery, gate rejection, security veto, human decision, dependency, persistent provider/tool, and non-convergent rework categories with allowed orchestration responses. | `FAILURE_RETRY_RECOVERY.md` |
| `WFL-REQ-062` | Final reconciliation directive §6 | Workflow Catalog is a conformance/discovery index with stable identity, purpose, lifecycle, compatibility, required Role/Skill refs, dependencies/conflicts, supersession/replacement and contract references. | `WORKFLOW_CATALOG.md` |
| `WFL-REQ-063` | Final reconciliation directive §1 | Every canonical Workflow Profile explicitly declares all required Profile Standard fields, including `Dependencies` and `Conflicts`; absence is not equivalent to `none`. | `WORKFLOW_PROFILE_STANDARD.md`, `profiles/*.md` |
| `WFL-REQ-064` | Final reconciliation directive §2/8 | Workflow semantic identities are exposed for future observability/provenance without defining UPOS-008 event/trace semantics. | `TASK_AND_WORKFLOW_INSTANCE_MODEL.md`, `WORKFLOW_STATE_MODEL.md`, `CROSS_MODULE_INTERFACES.md` |

## Coverage statement

`UNMAPPED MODULE-04 SOURCE REQUIREMENTS = 0` means all Workflow-owned requirements identified from the frozen source, implementation directive, and final reconciliation directive are mapped or explicitly deferred.

It does not claim downstream modules are already implemented.
