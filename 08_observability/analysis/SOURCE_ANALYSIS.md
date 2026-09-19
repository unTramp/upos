# Source Analysis — UPOS-008

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## 1. Inputs

Final canonical upstream baselines used for freeze reconciliation:

```text
MASTER: f03b6fae20ac00241afd79a5763673c2781459870fd24608bee99c18b0c66699
UPOS-001: 0eed3f1319103b9fef7956519da9754986b7c512a05278c030c38edbaddcb3a1
UPOS-002: 34274f4f102150826e599def36b940d23c15a66a8b0be4b8f5e01964cc1dc043
UPOS-003: 94726e67917808cee0ca3a62d04ce22cdd9b3ad213ea69a93e630336159945ad
UPOS-004: abf2fbc069af77a70cf6ee2b1242435c6a510b7196b2cac92f03e91e5b09fae1
UPOS-005: 186ded26c69d7d1115fa25c50aa83beacfecda8b347175da1d29a294395a3528
UPOS-006: 49301fa994e2d47c146f84260e4783585c950faf0c73dbe129767c2c2c95e45e
UPOS-007: 36c52764ccafdfef053d224ec1af5d297e3cd6eceacbc45d287d4bc96a1833b0
```

The earlier aggregate `UPOS_CANONICAL_BASELINE_01_07_v1.0` was a transport convenience only and is not required to interpret the final Module-08 baseline.

## 2. Frozen master Observability-owned signals

Direct/mixed source areas include:

```text
§99  Observability model
§100 Dashboard-ready metrics
§101 Do not optimize for activity
§102 Quality metrics
§103 Agent performance
§147 Cost awareness
§148 Latency awareness
§149 Human attention as scarce resource
§167 Dashboard model
§168 Agent workload
§169 Workflow bottleneck analysis
§186 Telemetry retention              [mixed with Security/Project policy]
§188 Secret redaction                 [mixed; policy deferred to UPOS-010]
§189 Auditability
§190 Reproducibility
§221.7 Activity metrics anti-pattern
§222 Governance health checks          [mixed]
§223 Milestone review / telemetry quality [mixed]
Appendix S — Telemetry schema starter
```

Learning interpretation (§104–107 etc.) is deferred to UPOS-009. Permission/Security substantive policy is deferred to UPOS-010. Concrete provider/tool bindings are deferred to UPOS-011.

## 3. Upstream semantic spine

### UPOS-002

Stable:

```text
role_id
agent_definition_id + version
agent_run_id
```

Agent Instance is a configured runtime identity/reference; no universal stable `agent_instance_id` exists in the frozen baseline. Module 08 therefore consumes `agent_instance_ref` and defers concrete binding to UPOS-011.

### UPOS-003

Skill Invocation is a bounded execution attributable to Skill ID/version, Agent Run, task/work item, input/context refs and Skill Result.

Module 08 observes execution but does not create Skill invocation semantics.

### UPOS-004

Stable:

```text
task_id
routing_decision_id
workflow_instance_id
stage_id
transition_id
```

Owner states/retry/rework/reclassification/rerouting semantics remain UPOS-004.

### UPOS-005

Stable:

```text
context_request_id
context_bundle_id
memory_item_id
```

Module 08 may measure assembly/usage/budget but cannot reinterpret freshness/validity.

### UPOS-006

Stable Module-06 identities + VCS refs provide exact engineering attribution.

Review/QA result refs have already been reconciled to `quality_assessment_id`; Gate result refs to `quality_gate_result_id`.

### UPOS-007

Reconciled semantics important for Observability:

```text
assessment_cycle_kind = FIRST_PASS / RE_REVIEW / RE_VALIDATION / DELTA_REVIEW
zero/one/many context_bundle_refs
supporting_assessment_refs
Assessment interpreted as of assessed_at
Evidence Binding is Assessment-local
Finding/Exception lifecycle does not rewrite historical verdict
```

Quality metrics must consume these meanings rather than infer from comments/commits/current Finding state.

## 4. Main normalization decisions

1. Event Store is observational and never canonical domain state.
2. Producer, initiator and domain owner are separate fields.
3. Correlation and causation are separate relations.
4. Trace is not forced to equal Task/Workflow.
5. Completeness requires an expectation contract.
6. Read-model state can drift; owner state wins.
7. Metric formulas are versioned and visible outside the UI.
8. Unknown/no-data/incomplete remain explicit.
9. Conditional metrics remain unavailable rather than being approximated from weak proxies.
10. Observability can support future learning but cannot interpret/promote it.

## 5. P0/P1 source conflicts

```text
P0 conflicts: 0
Internal P1 ownership conflicts: 0
Downstream reconciliation dependencies: registered for UPOS-009/010/011
```
