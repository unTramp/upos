# Frozen Source Section Disposition

**ID:** UPOS-06-AN-011  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-006 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Final reconciliation against FROZEN UPOS-005 v1.0 or discovery of factual error  
**Related:** ../MODULE_06_TRACEABILITY.md

> This file is point-in-time implementation/audit evidence. It does not own timeless Module-06 semantics. Canonical semantics live in the normative Module-06 documents and `MODULE_06_TRACEABILITY.md`.


> **Historical evidence notice:** This file records point-in-time UPOS-006 decomposition/implementation/reconciliation evidence. It is not timeless normative truth. Current Engineering Governance semantics are owned by canonical Module-06 normative artifacts; `MODULE_06_TRACEABILITY.md` is the canonical coverage artifact.

## Rule

```text
EXTRACTED_TO_MODULE_06
MIXED_EXTRACTED_AND_DEFERRED
DEFERRED_TO_MODULE
OUTSIDE_MODULE_06
```

The table records top-level frozen-master disposition plus key engineering subsections.

| Source section | Title | Disposition | Destination |
|---|---|---|---|
| §0 | Executive model | MIXED_EXTRACTED_AND_DEFERRED | OTHER / owning U-POS module |
| §1 | Relationship to the Documentation Operating Model | DEFERRED_TO_MODULE | UPOS-01/11 |
| §2 | Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-01/11 |
| §3 | Foundational principles | MIXED_EXTRACTED_AND_DEFERRED | OTHER / owning U-POS module |
| §4 | Core terminology | DEFERRED_TO_MODULE | UPOS-002 |
| §5 | Universal Agent Contract | DEFERRED_TO_MODULE | UPOS-002 |
| §6 | Agent identity is not enough | DEFERRED_TO_MODULE | UPOS-002 |
| §7 | Universal role families | DEFERRED_TO_MODULE | UPOS-002 |
| §8 | Orchestrator | DEFERRED_TO_MODULE | UPOS-002 |
| §9 | Product Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §10 | Domain / Architecture Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §11 | UX / Product Design Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §12 | Design System Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §13 | Implementer Agent | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-002 |
| §14 | Reviewer Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §15 | QA Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §16 | Security Agent | DEFERRED_TO_MODULE | UPOS-002 |
| §17 | Documentation Guardian | DEFERRED_TO_MODULE | UPOS-002 |
| §18 | Merge Controller | DEFERRED_TO_MODULE | UPOS-002 |
| §19 | Skills model | DEFERRED_TO_MODULE | UPOS-003 |
| §20 | Skill contract | DEFERRED_TO_MODULE | UPOS-003 |
| §21 | Example universal skills | DEFERRED_TO_MODULE | UPOS-003 |
| §22 | Workflow contract | DEFERRED_TO_MODULE | UPOS-004 |
| §23 | Change classification | DEFERRED_TO_MODULE | UPOS-004 |
| §24 | C0 — Micro | DEFERRED_TO_MODULE | UPOS-004 |
| §25 | C1 — Small | DEFERRED_TO_MODULE | UPOS-004 |
| §26 | C2 — Standard Feature | DEFERRED_TO_MODULE | UPOS-004 |
| §27 | C3 — Cross-cutting | DEFERRED_TO_MODULE | UPOS-004 |
| §28 | C4 — Architectural | DEFERRED_TO_MODULE | UPOS-004 |
| §29 | C5 — High-risk | DEFERRED_TO_MODULE | UPOS-004 |
| §30 | Risk override rule | DEFERRED_TO_MODULE | UPOS-004 |
| §31 | Context assembly | DEFERRED_TO_MODULE | UPOS-005 |
| §32 | Context assembly order | DEFERRED_TO_MODULE | UPOS-005 |
| §33 | Context budget principle | DEFERRED_TO_MODULE | UPOS-005 |
| §34 | Memory model | DEFERRED_TO_MODULE | UPOS-005 |
| §35 | Project memory sources | DEFERRED_TO_MODULE | UPOS-005 |
| §36 | Learning is not hidden model training | DEFERRED_TO_MODULE | UPOS-009/01 |
| §37 | Learning promotion model | DEFERRED_TO_MODULE | UPOS-009/01 |
| §38 | Permissions model | DEFERRED_TO_MODULE | UPOS-010 |
| §39 | Default role permission philosophy | DEFERRED_TO_MODULE | UPOS-002 |
| §40 | Human approval model | DEFERRED_TO_MODULE | UPOS-002 |
| §41 | Recommended adoption mode | DEFERRED_TO_MODULE | UPOS-002 |
| §42 | Planning model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §43 | Expected commits | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §44 | Git operating principles | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §45 | Atomic logical commits | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §46 | Bad commit granularity | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §47 | Bad oversized commit | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §48 | Commit categories | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §49 | Commit message contract | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §50 | Bug-fix commit strategy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §51 | Review-fix commits | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §52 | PR operating model | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §53 | Good PR | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §54 | Bad PR | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §55 | PR size policy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §56 | PR description contract | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §57 | Creation loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §58 | Verification loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §59 | Self-check | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §60 | Independent review protocol | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §61 | Review finding severity | DEFERRED_TO_MODULE | UPOS-007 |
| §62 | Review output contract | DEFERRED_TO_MODULE | UPOS-007 |
| §63 | Reviewer independence | DEFERRED_TO_MODULE | UPOS-007 |
| §64 | QA protocol | DEFERRED_TO_MODULE | UPOS-007 |
| §65 | QA dimensions | DEFERRED_TO_MODULE | UPOS-007 |
| §66 | Documentation gate | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §67 | Architecture gate | DEFERRED_TO_MODULE | UPOS-007 |
| §68 | Security gate | DEFERRED_TO_MODULE | UPOS-007 |
| §69 | Database migration gate | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §70 | Merge readiness | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §71 | Merge authority | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §72 | Merge strategy | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §73 | Handoff protocol | DEFERRED_TO_MODULE | UPOS-002 |
| §74 | Handoff context minimization | DEFERRED_TO_MODULE | UPOS-002 |
| §75 | Guardrails | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §76 | Guardrail types | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §77 | Escalation model | DEFERRED_TO_MODULE | UPOS-002 |
| §78 | Escalation targets | DEFERRED_TO_MODULE | UPOS-002 |
| §79 | Failure and recovery | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §80 | Retry policy | DEFERRED_TO_MODULE | UPOS-004 |
| §81 | Scope Guardian | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §82 | Concurrency model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §83 | Task isolation | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §84 | Shared file collision | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §85 | Workflow — Micro Change | DEFERRED_TO_MODULE | UPOS-004 |
| §86 | Workflow — Bug Fix | DEFERRED_TO_MODULE | UPOS-004 |
| §87 | Workflow — New Feature | DEFERRED_TO_MODULE | UPOS-004 |
| §88 | Workflow — UI Change | DEFERRED_TO_MODULE | UPOS-004 |
| §89 | Workflow — Design System Change | DEFERRED_TO_MODULE | UPOS-004 |
| §90 | Workflow — Architecture Change | DEFERRED_TO_MODULE | UPOS-004 |
| §91 | Workflow — API Change | DEFERRED_TO_MODULE | UPOS-004 |
| §92 | Workflow — Database Migration | DEFERRED_TO_MODULE | UPOS-004 |
| §93 | Workflow — Security Change | DEFERRED_TO_MODULE | UPOS-004 |
| §94 | Workflow — Refactor | DEFERRED_TO_MODULE | UPOS-004 |
| §95 | Workflow — Dependency Upgrade | DEFERRED_TO_MODULE | UPOS-004 |
| §96 | Workflow — Hotfix | DEFERRED_TO_MODULE | UPOS-004 |
| §97 | Workflow — Documentation Change | DEFERRED_TO_MODULE | UPOS-004 |
| §98 | Workflow — Release | DEFERRED_TO_MODULE | UPOS-004 |
| §99 | Observability model | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-008 |
| §100 | Dashboard-ready metrics | DEFERRED_TO_MODULE | UPOS-008 |
| §101 | Do not optimize for activity | DEFERRED_TO_MODULE | UPOS-008 |
| §102 | Quality metrics | DEFERRED_TO_MODULE | UPOS-008 |
| §103 | Agent performance | DEFERRED_TO_MODULE | UPOS-008 |
| §104 | Agent learning record | DEFERRED_TO_MODULE | UPOS-003 |
| §105 | Skill evolution | DEFERRED_TO_MODULE | UPOS-003 |
| §106 | Workflow evolution | DEFERRED_TO_MODULE | UPOS-009/01 |
| §107 | Agent contract evolution | DEFERRED_TO_MODULE | UPOS-009/01 |
| §108 | Model/provider independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §109 | Tool independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §110 | Safety around secrets | DEFERRED_TO_MODULE | UPOS-010 |
| §111 | Production access | DEFERRED_TO_MODULE | UPOS-010 |
| §112 | Protected files | DEFERRED_TO_MODULE | UPOS-010 |
| §113 | Definition of Ready — task | DEFERRED_TO_MODULE | UPOS-007 |
| §114 | Definition of Ready — agent execution | DEFERRED_TO_MODULE | UPOS-007 |
| §115 | Definition of Done — implementation | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §116 | Definition of Done — PR | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §117 | Definition of Done — workflow | DEFERRED_TO_MODULE | UPOS-007 |
| §118 | Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §119 | Maturity model | DEFERRED_TO_MODULE | UPOS-011 |
| §120 | Recommended adoption sequence | DEFERRED_TO_MODULE | UPOS-011 |
| §121 | Recommended first implementation | DEFERRED_TO_MODULE | UPOS-011 |
| §122 | Universal Orchestrator algorithm | DEFERRED_TO_MODULE | UPOS-004 |
| §123 | Authority conflict resolution | DEFERRED_TO_MODULE | UPOS-002 |
| §124 | Security veto | DEFERRED_TO_MODULE | UPOS-002 |
| §125 | Architecture veto | DEFERRED_TO_MODULE | UPOS-002 |
| §126 | Reviewer veto | DEFERRED_TO_MODULE | UPOS-002 |
| §127 | Human override | DEFERRED_TO_MODULE | UPOS-002 |
| §128 | Agent output discipline | DEFERRED_TO_MODULE | UPOS-002 |
| §129 | Change Classification output | DEFERRED_TO_MODULE | UPOS-004 |
| §130 | Implementation Plan output | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §131 | Review Result output | DEFERRED_TO_MODULE | UPOS-004 |
| §132 | QA Result output | DEFERRED_TO_MODULE | UPOS-004 |
| §133 | Merge Readiness output | DEFERRED_TO_MODULE | UPOS-004 |
| §134 | Change review feedback loop | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §135 | Oversized PR handling | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §136 | Scope expansion handling | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §137 | Unplanned architecture discovery | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §138 | Unplanned product ambiguity | DEFERRED_TO_MODULE | UPOS-004 |
| §139 | Unplanned security concern | DEFERRED_TO_MODULE | UPOS-004 |
| §140 | Documentation drift detection | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §141 | Agent sandbox hygiene | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §142 | Branch lifetime | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §143 | Stacked PRs | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §144 | Feature flags | DEFERRED_TO_MODULE | UPOS-011 |
| §145 | Rollback thinking | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §146 | Dependency graph awareness | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §147 | Cost awareness | DEFERRED_TO_MODULE | UPOS-008 |
| §148 | Latency awareness | DEFERRED_TO_MODULE | UPOS-008 |
| §149 | Human attention as scarce resource | DEFERRED_TO_MODULE | UPOS-008 |
| §150 | Agent communication rule | DEFERRED_TO_MODULE | UPOS-002 |
| §151 | Decision preservation | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §152 | No circular authority | DEFERRED_TO_MODULE | UPOS-002 |
| §153 | Independent model diversity | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §154 | Review freshness | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §155 | Merge queue compatibility | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-011 |
| §156 | CI as evidence provider | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §157 | Agent-specific test ownership | DEFERRED_TO_MODULE | UPOS-007 |
| §158 | Test integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §159 | Snapshot integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §160 | Security scanner integrity | DEFERRED_TO_MODULE | UPOS-007 |
| §161 | Linter suppression | DEFERRED_TO_MODULE | UPOS-007 |
| §162 | Technical debt creation | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §163 | Technical debt review | DEFERRED_TO_MODULE | UPOS-009/01 |
| §164 | Post-merge verification | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §165 | Post-merge learning trigger | DEFERRED_TO_MODULE | UPOS-009/01 |
| §166 | Incident integration | DEFERRED_TO_MODULE | UPOS-009/01 |
| §167 | Dashboard model | DEFERRED_TO_MODULE | UPOS-008 |
| §168 | Agent workload | DEFERRED_TO_MODULE | UPOS-008 |
| §169 | Workflow bottleneck analysis | DEFERRED_TO_MODULE | UPOS-008 |
| §170 | Maturity gates for autonomy | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §171 | Autonomy expansion | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §172 | Project-specific overrides | DEFERRED_TO_MODULE | UPOS-011 |
| §173 | Universal vs project-specific rules | DEFERRED_TO_MODULE | UPOS-011 |
| §174 | Agent manifests should be versioned | DEFERRED_TO_MODULE | UPOS-011 |
| §175 | Governance change workflow | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §176 | Universal starter agent set | DEFERRED_TO_MODULE | UPOS-002 |
| §177 | Universal full agent set | DEFERRED_TO_MODULE | UPOS-002 |
| §178 | Agent composition | DEFERRED_TO_MODULE | UPOS-002 |
| §179 | Universal policy files | DEFERRED_TO_MODULE | UPOS-011 |
| §180 | AI Agent README | DEFERRED_TO_MODULE | UPOS-011 |
| §181 | Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | UPOS-011 |
| §182 | Universal file naming | DEFERRED_TO_MODULE | UPOS-011 |
| §183 | Agent contract versioning | DEFERRED_TO_MODULE | UPOS-002 |
| §184 | Skill versioning | DEFERRED_TO_MODULE | UPOS-003 |
| §185 | Workflow versioning | DEFERRED_TO_MODULE | UPOS-004 |
| §186 | Telemetry retention | DEFERRED_TO_MODULE | UPOS-008 |
| §187 | Sensitive context policy | DEFERRED_TO_MODULE | UPOS-005 |
| §188 | Secret redaction | DEFERRED_TO_MODULE | UPOS-010 |
| §189 | Auditability | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §190 | Reproducibility | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §191 | Agent hallucination handling | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §192 | Missing Source of Truth | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §193 | Stale Source of Truth | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §194 | Feature lifecycle integration | DEFERRED_TO_MODULE | UPOS-004 |
| §195 | Agent lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| §196 | Task lifecycle | DEFERRED_TO_MODULE | UPOS-004 |
| §197 | PR lifecycle | EXTRACTED_TO_MODULE_06 | UPOS-006 |
| §198 | Agent run lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| §199 | Workflow state machine | DEFERRED_TO_MODULE | UPOS-004 |
| §200 | No hidden background authority | DEFERRED_TO_MODULE | UPOS-002 |
| §201 | Human pause points | DEFERRED_TO_MODULE | UPOS-002 |
| §202 | Plan change protocol | DEFERRED_TO_MODULE | UPOS-004 |
| §203 | Reclassification | DEFERRED_TO_MODULE | UPOS-004 |
| §204 | Risk inheritance | DEFERRED_TO_MODULE | UPOS-004 |
| §205 | Change decomposition | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §206 | Multi-agent code ownership | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §207 | Shared contract first | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-004 |
| §208 | Reviewer context independence | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-005 |
| §209 | QA context independence | DEFERRED_TO_MODULE | UPOS-005 |
| §210 | Merge Controller context | DEFERRED_TO_MODULE | UPOS-002 |
| §211 | Product Owner context | DEFERRED_TO_MODULE | UPOS-002 |
| §212 | Decision packet | DEFERRED_TO_MODULE | UPOS-002 |
| §213 | Do not fake consensus | DEFERRED_TO_MODULE | UPOS-002 |
| §214 | Conflict resolution by authority | DEFERRED_TO_MODULE | UPOS-002 |
| §215 | Majority voting | DEFERRED_TO_MODULE | UPOS-002 |
| §216 | Agent confidence | DEFERRED_TO_MODULE | UPOS-002 |
| §217 | Evidence hierarchy | DEFERRED_TO_MODULE | UPOS-007 |
| §218 | Change evidence bundle | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → UPOS-007 |
| §219 | Artifact retention | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §220 | Privacy of reasoning | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §221 | Universal anti-patterns | MIXED_EXTRACTED_AND_DEFERRED | Engineering mechanics → UPOS-006; remaining → OTHER / owning U-POS module |
| §222 | Governance health checks | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §223 | Quarterly / milestone review | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §224 | Universal adoption checklist | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §225 | Minimal viable agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §226 | Intermediate agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §227 | Advanced agent system | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §228 | Final operating model | DEFERRED_TO_MODULE | OTHER / owning U-POS module |
| §3.7 | Small coherent changes | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit / IR standards |
| §3.8 | One PR, one intention | EXTRACTED_TO_MODULE_06 | UPOS-006 Integration Request Standard |
| §3.9 | One commit, one logical change | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit Standard |
| §3.10 | No opportunistic refactoring by default | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit / Engineering Change scope |
| §44.1 | No direct push to protected main | MIXED_EXTRACTED_AND_DEFERRED | engineering invariant → UPOS-006; grants/provider → UPOS-010/011 |
| §44.2 | One branch per coherent task | MIXED_EXTRACTED_AND_DEFERRED | normalized to RCU/branch semantics → UPOS-006; naming → UPOS-011 |
| §221.10 | Git history as keystroke log | EXTRACTED_TO_MODULE_06 | UPOS-006 Atomic Commit Standard |
| Appendix L | Git Policy starter | MIXED_EXTRACTED_AND_DEFERRED | engineering mechanics → UPOS-006; authority/quality/provider portions deferred |

## Note

Mixed sections contribute only repository engineering mechanics to UPOS-006.
Role authority, Workflow orchestration, Context, Quality, Observability, Learning, Permissions, and provider bindings remain with their owners.
