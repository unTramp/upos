# Permission Request Standard

**ID:** UPOS-10-PRS-001  
**Type:** STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity

Every independently evaluated permission request has stable:

```text
permission_request_id
```

A new materially different intended action/resource/security scope creates a new request identity.

## 2. Minimum contract

```text
permission_request_id

subject_type
subject_ref
role_ref
agent_run_id

task_id
workflow_instance_id
stage_id

capability
action
resource_type
resource_ref
resource_scope
resource_state_ref

security_context_refs
purpose_ref
requested_duration
requested_effective_from

candidate_grant_refs
required_policy_refs
protected_action_id

created_at
requesting_actor_ref
```

Non-applicable fields are explicit `N/A`.

## 3. Request semantics

A Permission Request asks for evaluation. It grants nothing.

```text
PERMISSION REQUEST != GRANT
PERMISSION REQUEST != PERMISSION DECISION
PERMISSION REQUEST != PROTECTED ACTION EXECUTION
```

## 4. Exactness

A request SHOULD identify the narrowest practical resource and execution scope.

Broad requests such as:

```text
subject X can write production forever
```

violate least-privilege expectations unless explicitly justified by policy.

## 5. Purpose provenance

`purpose_ref` SHOULD resolve to governed Task/Workflow/Plan/Decision scope where relevant. Free text may supplement but must not replace authoritative purpose.

## 6. Re-evaluation

When the intended capability/action/resource/scope changes materially, do not mutate the old request into a new meaning. Create a new Permission Request and retain linkage through external provenance if needed.
