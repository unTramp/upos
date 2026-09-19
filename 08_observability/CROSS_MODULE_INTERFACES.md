# Cross-Module Interfaces

**ID:** UPOS-08-XMI-001  
**Type:** INTERFACE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. UPOS-01 — Documentation / Source of Truth / Knowledge Lifecycle

### Consumes

```text
canonical source refs
document/decision revisions
knowledge lifecycle references
canonical conflict/drift refs
```

### Provides

```text
observable change/audit/provenance references
execution history/metrics usable as evidence
```

### MUST NOT redefine

```text
canonical truth
fact ownership
knowledge promotion
supersession meaning
```

## 2. UPOS-002 — Agent Organization

### Consumes

```text
role_id
agent_definition_id + version
agent_run_id
agent_instance_ref
authority/delegation/SoD/Human Governance refs
```

Note: frozen UPOS-002 does not define a universal stable `agent_instance_id`; UPOS-008 uses the configured runtime `agent_instance_ref` and defers concrete binding to UPOS-011.

### Provides

```text
Agent Run telemetry
capacity/workload observations
human-interaction observations
audit attribution
```

### MUST NOT redefine

```text
Role authority
accountability
SoD
Human Governance
Agent Instance semantics
```

## 3. UPOS-003 — Skills

### Consumes

```text
skill_id + version
skill_invocation_ref
Skill Result refs
```

### Provides

```text
invocation duration/failure/usage/cost/trace attribution
```

### MUST NOT redefine

Skill procedure, result semantics, applicability or quality criteria.

## 4. UPOS-004 — Workflow Engine

### Consumes

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
Workflow/Stage state/result refs
retry/rework/recovery/reclassification/rerouting/escalation refs
```

### Provides

```text
timeline projections
duration/block/rework/retry measurements
bottleneck observations
```

### MUST NOT redefine

Task/Workflow state, transition legality, retry/rework semantics, routing or Change Class.

## 5. UPOS-005 — Context & Memory

### Consumes

```text
context_request_id
context_bundle_id
Context validity/failure refs
budget/accounting refs
memory_item_id where observed
```

### Provides

```text
Context request/assembly latency
usage/budget observations
Context failure/invalidated/reassembly timeline observations
```

### MUST NOT redefine

Context validity/freshness, assembly/retrieval, budget or Memory semantics.

## 6. UPOS-006 — Engineering Governance

### Consumes

```text
engineering_change_id
repository_change_unit_id
workspace_id
branch_ref
commit_ref
integration_request_ref
check_ref
merge_operation_id
revision/integrated revision refs
```

### Provides

```text
engineering timelines
latency/usage observations
artifact/provenance projections
```

### MUST NOT redefine

atomicity, branch policy, Integration Request lifecycle, mechanical mergeability, merge mechanics or artifact staleness.

## 7. UPOS-007 — Quality System

### Consumes

```text
quality_assessment_id
assessment_type
assessment_cycle_kind
quality_verdict
evidence_record_id
finding_id
quality_gate_id
quality_gate_result_id
quality_exception_id
Quality Readiness refs
```

### Provides

```text
Quality operational metrics
first-pass/re-review metrics
Quality timelines
finding/gate/evidence aggregate observations
```

### MUST NOT redefine

Quality Verdict, Finding severity/category, Evidence sufficiency/freshness interpretation, Gate Result or readiness semantics.

## 8. UPOS-009 — Learning System

### Provides to Learning

```text
event_id
trace_id
Metric Observation value records linked to metric_definition_id
version/cohort comparison inputs
recurrence/retry/rework observations
cost/time/quality/human-attention measurements
data completeness/coverage metadata
```

Metric Observation remains a derived/value record and has no global `metric_observation_id`.

### Consumes from Learning

```text
pattern_candidate_id
learning_candidate_id
root_cause_assessment_id
improvement_proposal_id
validation_plan_id
learning_outcome_id
```

These are observed/correlated by reference only.

### MUST NOT redefine

Pattern interpretation, Learning Candidate semantics, root-cause assessment, proposal/promotion semantics or Learning lifecycle.

## 9. UPOS-010 — Security & Permissions

### Consumes

```text
permission_request_id
permission_decision_id
grant_id
protected_action_id
security_exception_id
security_policy_ref + security_policy_version
security reason/result refs
break-glass/elevation refs
security handling constraints/directives
```

Security handling metadata may include policy-scoped sensitivity, redaction, access and retention constraint references. UPOS-010 owns their security meaning.

### Provides

Security-relevant attributable Events, audit/provenance projections and aggregate metrics without raw secrets/protected payloads.

### MUST NOT redefine

Permission Decision, Grant semantics, Security Policy, security veto/exception authority, sensitive-data policy or protected-action authority.

## 10. UPOS-011 — Project Adapter

### Consumes concrete bindings for

```text
project_id
agent_instance_ref
Event sink / Event Store
trace backend/exporter
trace propagation carrier
Metric query/backend
projection store / Control Plane datasource
provider usage API
pricing source
clock/time source
repository/CI/provider event adapters
queue/capacity signal sources
sampling implementation
projection watermark source
security/access/retention enforcement bindings
```

### MUST NOT redefine

Binding/provider/runtime details never redefine Event/Trace/Metric/read-model semantics.

## 11. Cross-cutting schemas/runtime layer

Normative Markdown owns semantics.

Machine schemas/runtime:

```text
MAY encode/validate/transport Module-08 contracts
MUST NOT invent new semantics
```

## 12. Control Plane consumer

Control Plane reads Module-08 projections/metrics and owner-domain references.

Control Plane actions route to the owning module interfaces; they do not mutate projection state as domain truth.
