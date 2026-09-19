# Workflow State Model

**ID:** UPOS-04-STM-001  
**Type:** STATE MACHINE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-004 Workflow Engine  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Related:** —


## 1. Workflow Instance states

Canonical orchestration states:

```text
READY
RUNNING
PAUSED
BLOCKED
REWORK_REQUIRED
ESCALATED
COMPLETED
FAILED
CANCELLED
SUPERSEDED
```

## 2. Stage states

```text
PENDING
READY
RUNNING
BLOCKED
COMPLETED
SKIPPED
FAILED
CANCELLED
```

## 3. Stage identity

Every canonical or resolved Stage MUST be independently addressable by a stable:

```text
stage_id
```

The `stage_id` is semantic identity, not a display name.

For Base Workflow stages, v1 uses namespaced identifiers such as:

```text
WFL-FEATURE:SPEC
WFL-BUG-FIX:REVIEW
```

Profile-added checkpoints/stages use their Profile namespace, for example:

```text
WFP-UI:UI-VALIDATION
```

A resolved Workflow configuration MUST preserve the originating stable `stage_id` values so a later consumer can identify exactly which Stage produced/consumed an artifact.

## 4. Transition identity

Every declared transition rule MUST be independently addressable by a stable:

```text
transition_id
```

For Workflow-specific rules, v1 uses namespaced identifiers such as:

```text
WFL-FEATURE:TR-NORMAL-NEXT
WFL-FEATURE:TR-GATE-REWORK
```

Global Workflow-state transitions defined in this standard use stable identifiers listed below.

A `transition_id` MUST NOT be inferred from a human-readable display label.

## 5. Legal-transition principle

Automated/reference execution MUST only use transitions declared by the Workflow Definition/Profile resolution.

Typical instance transition rules:

| transition_id | From | To / condition |
|---|---|---|
| `WST-READY-RUNNING` | READY | RUNNING |
| `WST-RUNNING-PAUSED` | RUNNING | PAUSED |
| `WST-RUNNING-BLOCKED` | RUNNING | BLOCKED |
| `WST-RUNNING-REWORK` | RUNNING | REWORK_REQUIRED |
| `WST-RUNNING-ESCALATED` | RUNNING | ESCALATED |
| `WST-RUNNING-COMPLETED` | RUNNING | COMPLETED |
| `WST-RUNNING-FAILED` | RUNNING | FAILED |
| `WST-PAUSED-RUNNING` | PAUSED | RUNNING |
| `WST-BLOCKED-RUNNING` | BLOCKED | RUNNING |
| `WST-REWORK-RUNNING` | REWORK_REQUIRED | RUNNING |
| `WST-ESCALATED-RUNNING` | ESCALATED | RUNNING when authority/condition is resolved |
| `WST-ESCALATED-CANCELLED` | ESCALATED | CANCELLED |
| `WST-ESCALATED-FAILED` | ESCALATED | FAILED |
| `WST-ANY-CANCELLED` | any non-terminal state | CANCELLED when cancellation is authorized |
| `WST-ROUTE-SUPERSEDED` | current route | SUPERSEDED when rerouted |

## 6. Pause vs Block

`PAUSED`:
- deliberate checkpoint;
- may await human decision, scheduled action, or external condition.

`BLOCKED`:
- required condition/input/gate cannot currently be satisfied.

## 7. Rework

`REWORK_REQUIRED` means an existing stage/result must be revisited due to a failed external gate/finding or changed requirement.

Quality verdict meaning remains UPOS-007.

## 8. Escalated

`ESCALATED` means orchestration cannot proceed within currently delegated authority/routing.

Authority resolution remains UPOS-002/10/01.

## 9. Terminal semantics

`COMPLETED`, `FAILED`, `CANCELLED`, and `SUPERSEDED` are terminal for that Workflow Instance version/route.

A reroute creates/continues a new resolved configuration while preserving provenance to the superseded route.
