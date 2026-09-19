# Module 07 Cross-Module Interfaces

**ID:** UPOS-07-XMI-001  
**Type:** CROSS-MODULE INTERFACE CONTRACT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-007 Quality System  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

**UPOS-007 provides**
- Quality Findings/Evidence references;
- documentation drift/nonconformance evidence;
- Assessment/Gate artifacts that may become governed evidence.

**UPOS-007 consumes**
- authoritative requirements/acceptance criteria;
- Product/Domain/Architecture constraints;
- documentation standards;
- accepted decisions;
- source owner/status/version/conflict semantics.

**MUST NOT redefine**
- project truth, canonical owner/source, requirement meaning, promotion, canonical conflict resolution.

## UPOS-002 — Agent Organization

**Provides**
- independent verification results;
- Quality Assessments;
- Findings;
- Quality readiness.

**Consumes**
- Reviewer/QA/Specialist/Merge Controller Role identities;
- Agent Run refs;
- SoD/authority/veto/Human Governance refs.

**MUST NOT redefine**
- Role authority, veto, delegation, approval, merge authority.

Required invariants:

```text
Implementer != Final Reviewer
high-risk:
Implementer != Reviewer != Merge Controller
```

## UPOS-003 — Skills System

**Provides canonical semantics consumed by Interface Skills**
- `review-diff`
- `review-architecture`
- `qa-validation`
- `assess-merge-readiness`
- `reconcile-documentation`

and supports `analyze-impact`, `reproduce-bug`, `write-regression-test`.

**Consumes**
- Skill IDs/versions/invocation/result refs.

**MUST NOT redefine**
- Skill procedure.

## UPOS-004 — Workflow Engine

**Provides**
- Quality Assessment results;
- Gate Results;
- Quality readiness;
- blocking/inconclusive Quality conditions.

**Consumes**
- Task/Workflow/Stage/Change Class/Concern refs;
- gate references;
- rework/re-review/re-validation orchestration.

**MUST NOT redefine**
- gate placement, Stage order, Workflow transition, retry/rework/reroute behavior.

```text
UPOS-004 = WHEN gate occurs
UPOS-007 = HOW quality gate is evaluated / WHAT result means
```

## UPOS-005 — Context & Memory

**Provides**
- Quality Context Requirements;
- bounded follow-up evidence/context need references.

**Consumes**
- `context_bundle_id`;
- Context provenance/validity;
- source versions;
- Reviewer/QA Context isolation/independence semantics.

**MUST NOT redefine**
- retrieval, Context Request/Bundle assembly, memory, Context freshness.

## UPOS-006 — Engineering Governance

**Provides to UPOS-006**
- Quality Assessment/Gate/readiness refs;
- evidence applicability/staleness implications for engineering artifact changes.

**Consumes from UPOS-006**
- `engineering_change_id`;
- `repository_change_unit_id`;
- exact base/head/commit/revision/diff refs;
- `integration_request_ref`;
- Engineering Check refs/results;
- review-artifact-changed signals;
- mechanical mergeability.

**MUST NOT redefine**
- branch/commit/Integration Request/CI execution/merge mechanics.

```text
MECHANICALLY_MERGEABLE
!= QUALITY_READY
```

## UPOS-008 — Observability

**Exposes stable semantic refs**
- `quality_criteria_set_id`;
- `quality_assessment_id`;
- `evidence_record_id`;
- `finding_id`;
- `quality_gate_id`;
- `quality_gate_result_id`;
- `quality_exception_id`;
- target refs;
- verdict;
- severity;
- freshness/applicability state.

**MUST NOT define**
- event_id, trace_id, span_id, metric schema, dashboard, alerting, aggregation.

## UPOS-009 — Learning

**Provides potential learning evidence**
- recurring findings;
- repeated non-actionable/advisory finding patterns;
- repeated review failure/rework patterns;
- stale evidence patterns;
- escaped-quality issue refs;
- waiver recurrence;
- flaky evidence signals.

**Consumes**
- approved proposals to improve Quality policy/criteria/gates.

**MUST NOT**
- learn/promote silently.

## UPOS-010 — Security & Permissions

**Provides**
- Quality requirement/gate references that may depend on external Security results.

**Consumes**
- Security result refs;
- permission constraints;
- protected evidence constraints;
- Human/Security approval refs.

**MUST NOT redefine**
- Security semantics, veto, access grant, secret policy, protected-action permission.

Sensitive evidence MUST use externally permitted redacted/reference-only forms as required. Quality artifacts MUST NOT copy secrets merely for convenience.

## UPOS-011 — Project Adapter

**Provides abstract needs**
- test/check kind requirements;
- target/artifact retrieval needs;
- Quality-tool capability requirements.

**Consumes concrete bindings**
- CI/test commands/providers;
- test framework/tool adapters;
- project thresholds;
- browser/device matrix;
- performance criteria mappings;
- repository/provider integrations.

**MUST NOT hard-code**
- provider commands/tool products in universal Quality semantics.

## Cross-cutting machine-readable schemas/runtime layer

Future schemas may encode:

```text
QualityCriteriaSet
EvidenceRecord
Finding
QualityAssessment
QualityGate
QualityGateResult
QualityException
```

Markdown remains normative.

Schemas/runtime MUST NOT invent independent Quality semantics.
