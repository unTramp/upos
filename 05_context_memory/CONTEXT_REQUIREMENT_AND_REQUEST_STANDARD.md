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
