# Subject & Identity Interface

**ID:** UPOS-10-SII-001  
**Type:** INTERFACE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-010 Security & Permissions  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** coordinated UPOS-01–11 v1 baseline


## 1. Identity reuse

UPOS-010 consumes already-owned identities and references.

Agent execution:

```text
role_ref             → UPOS-002 role_id
agent_definition_ref → UPOS-002 agent_definition_id + version
agent_run_id          → UPOS-002 Agent Run identity
```

Workflow execution:

```text
task_id
workflow_instance_id
stage_id
```

Resource/provider/service identities are supplied by project/provider adapters and canonical resource owners.

## 2. Subject representation

A Permission Request MUST identify the subject using:

```text
subject_type
subject_ref
```

and where applicable the narrow execution identity:

```text
role_ref
agent_run_id
task_id
workflow_instance_id
stage_id
```

A Role alone is insufficient for execution-scoped authorization when a narrower Run/Task/Stage identity exists.

## 3. Subject types

Canonical abstract classes:

```text
HUMAN
AGENT_RUN
AGENT_INSTANCE
SERVICE
AUTOMATION
```

`ROLE` may appear as an organizational attribute/reference but is not treated as a standalone executing identity unless project policy explicitly uses a Role-bound service identity.

## 4. Identity proof / authentication boundary

UPOS-010 may require a security condition such as:

```text
subject authenticated
stronger authentication required
recent reauthentication required
identity assurance >= policy threshold
```

It does not define identity-provider mechanics, tokens, MFA implementation or credential issuance. UPOS-011 binds those conditions.

## 5. Execution scope

Permissions SHOULD be bound to the narrowest available governed scope:

```text
Agent Run
Task
Workflow Instance
Stage
Engineering Change / RCU
exact protected action
```

Standing actor-wide permission is exceptional, not default.

## 6. Cross-project isolation

A subject/grant/resource reference in Project A MUST NOT implicitly authorize equivalent-looking resources in Project B.

Project identity/scope must be explicit in binding or policy context where cross-project ambiguity is possible.
