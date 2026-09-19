# Event Taxonomy

**ID:** UPOS-08-ETX-001  
**Type:** TAXONOMY STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Purpose

The taxonomy limits uncontrolled Event-type growth while preserving owner-domain meaning.

Every Event has:

```text
event_class
namespaced event_type
domain_owner_module
primary domain reference
```

## 2. Canonical Event classes

```text
LIFECYCLE
STATE_TRANSITION
DECISION_REFERENCE
INVOCATION
RESULT
ARTIFACT_CHANGE
GATE_EVALUATION
HUMAN_INTERACTION
FAILURE
RESOURCE_USAGE
COST
GOVERNANCE
SECURITY_REFERENCE
LEARNING_REFERENCE
SYSTEM_HEALTH
CORRECTION
```

`SECURITY_REFERENCE` and `LEARNING_REFERENCE` classify observed references only. Their substantive semantics remain pending UPOS-010/009 reconciliation.

## 3. Event naming

Use controlled namespaced occurrence names:

```text
<owner-namespace>.<entity-or-operation>.<past-tense-occurrence>
```

Illustrative:

```text
workflow.instance.started
workflow.stage.transitioned
context.bundle.assembled
engineering.commit.recorded
quality.assessment.completed
quality.gate.evaluated
observability.event.corrected
```

These examples do not establish an exhaustive registry.

## 4. Event types describe occurrences, not commands

Prefer:

```text
quality.assessment.completed
```

over command-like:

```text
quality.assessment.complete
```

Actions/commands belong to owner interfaces, not Observability.

## 5. Do not encode domain status in uncontrolled type explosion

Avoid creating a separate Event type for every possible payload value if the domain contract already exposes a governed result/status field.

Example:

```text
quality.assessment.completed
owner_result_ref = PASS / FAIL / BLOCKED / INCONCLUSIVE
```

rather than four unrelated Event contracts unless a material event semantic difference requires it.

## 6. Event class != domain taxonomy

`FAILURE` class does not replace UPOS-004/005/006/007 failure taxonomies.

`GATE_EVALUATION` does not define Gate semantics.

`HUMAN_INTERACTION` does not define Human Governance authority.

## 7. Extension discipline

A new canonical Event type must justify:

- recurring observability value;
- stable owner-domain occurrence;
- non-duplication of existing type + payload/result reference;
- capture importance and intended consumers;
- relevant source/owner contract.

Provider-specific raw event names belong to adapters and should map to canonical types where semantically valid.
