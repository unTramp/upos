# Workflow Routing Standard

**ID:** UPOS-04-ROU-001  
**Type:** ROUTING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** templates/ROUTING_DECISION_TEMPLATE.md


## 1. Routing inputs

Routing consumes:

- Task/Change Request;
- Source-of-Truth/context availability;
- Work Type recommendation;
- Concern signals;
- C0–C5 classification recommendation;
- relevant external policy signals;
- Role/Skill availability compatibility;
- unresolved governance conflicts.

## 2. Classification is not routing

```text
SKL-CLASSIFY-CHANGE
→ classification recommendation

UPOS-004 Change Classification Standard
→ canonical C0–C5 semantics

Routing
→ base workflow + profiles + class + external references

Orchestrator
→ coordinates route under UPOS-002 authority
```

## 3. Routing algorithm

Conceptual deterministic order:

```text
1. Accept Task / Change Request.
2. Resolve canonical Source-of-Truth prerequisites by interface.
3. Determine one primary Work Type.
4. Detect zero or more Concerns.
5. Classify C0–C5 against canonical criteria.
6. Apply risk overrides / inheritance.
7. Select Base Workflow by Work Type.
8. Compose compatible Concern Profiles.
9. Apply Change-Class process depth.
10. Enforce UPOS-002 SoD/role constraints.
11. Bind required Skill references by stable ID/version compatibility.
12. Add required external gate/approval references.
13. Validate dependencies/parallelism.
14. Produce attributable Routing Decision.
15. If unresolved conflict remains → BLOCK / ESCALATE, not guess.
```

## 4. Routing Decision identity

Every Routing Decision MUST have a stable, independently addressable:

```text
routing_decision_id
```

`routing_decision_id` identifies the decision artifact itself, not merely the Task or Workflow Instance.

It MUST:

- remain immutable for that Routing Decision record;
- be independently referenceable by provenance, Workflow Instances, approvals, and later observability;
- not be inferred from a display label;
- not be silently reused for a materially changed rerouting decision.

A materially changed reroute creates a new `routing_decision_id` and SHOULD preserve a reference to the superseded/prior Routing Decision.

This section defines semantic identity only. Machine encoding belongs to the cross-cutting schemas/runtime layer.

## 5. Routing Decision contract

A Routing Decision MUST include:

```text
routing_decision_id
task_id
work_type
change_class
classification_rationale
concerns
base_workflow_id
base_workflow_version
profiles
role_requirements
skill_references
sod_constraints
external_gate_references
approval_references
reclassification_triggers
source/context references
open conflicts / unknowns
```

## 6. No every-agent routing

Only required Roles/Skills participate.

## 7. Project stricter rules

Projects MAY impose stricter routing/classification via UPOS-011 bindings/policies.

Project overrides MUST NOT weaken non-overridable universal invariants.

## 8. Routing failure

Routing fails safely when:

- no authoritative classification basis exists;
- required Source-of-Truth is in active normative conflict;
- selected profiles conflict;
- required SoD cannot be satisfied;
- mandatory external policy cannot be resolved.

Outcome:

```text
BLOCKED_ROUTING
→ escalation / owner decision
```
