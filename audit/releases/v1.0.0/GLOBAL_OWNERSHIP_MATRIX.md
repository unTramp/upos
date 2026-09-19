# Global Ownership Matrix — U-POS v1

| Module | Canonical ownership | Must not own |
|---|---|---|
| 01 Documentation | project truth, documentation governance, Source-of-Truth resolution, knowledge lifecycle | agent authority, workflow execution, runtime telemetry |
| 02 Agent Organization | Roles, Agent Definitions/Instances/Runs, organizational authority, delegation, SoD, human governance | Skill procedure, workflow ordering, technical permission |
| 03 Skills | reusable bounded Skill definitions/procedures, skill lifecycle/versioning | organizational authority, workflow order, owner-domain verdicts |
| 04 Workflow Engine | work classification, routing, Workflow/Stage/Transition orchestration, retry/rework/recovery/reclassification/rerouting | quality verdict, permission decision, engineering mechanics |
| 05 Context & Memory | Context requirements/requests/bundles, retrieval/assembly/freshness, runtime memory taxonomy | canonical truth, workflow state, project memory truth ownership |
| 06 Engineering Governance | Engineering Change/RCU/workspace/branch/commit/Integration Request/merge/revert mechanics | Quality readiness, merge authority, technical permission |
| 07 Quality | criteria, evidence, findings, assessments, verdicts, gates, Quality Readiness | mechanical mergeability, organizational merge authority, permission |
| 08 Observability | events, traces/spans, metrics, telemetry quality, audit/provenance projections, read models, cost/capacity measurement | domain truth, workflow state, Quality verdict, Learning promotion |
| 09 Learning | signals/evidence interpretation, patterns, Learning Candidates, root-cause assessments, Improvement Proposals, validation/outcomes | canonical promotion, direct self-modification, owner-domain rules |
| 10 Security & Permissions | Security Subjects/Capabilities/Resources, Permission Requests/Decisions, Grants, Protected Actions, secrets/sensitive handling | organizational authority, workflow routing, provider IAM binding |
| 11 Project Adapter | project/provider/runtime bindings, resolution, validation, adapter contracts, drift/compatibility | domain semantics, policy meaning, Source of Truth |

## System-level separations preserved

```text
KNOWLEDGE != CONTEXT != MEMORY
SKILL CAPABILITY != ORGANIZATIONAL AUTHORITY
AUTHORITY != PERMISSION
QUALITY_READY != MECHANICALLY_MERGEABLE
QUALITY_READY != AUTHORIZED_TO_MERGE
QUALITY_READY != PERMITTED_TO_MERGE
EVENT != DOMAIN TRUTH
TRACE != WORKFLOW
READ MODEL != SOURCE OF TRUTH
LEARNING != SILENT SELF-MODIFICATION
PROVIDER SCOPE != U-POS PERMISSION
PROJECT MANIFEST != PROJECT KNOWLEDGE
PROJECT ADAPTER != SOURCE OF TRUTH
```
