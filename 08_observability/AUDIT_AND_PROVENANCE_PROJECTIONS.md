# Audit and Provenance Projections

**ID:** UPOS-08-APR-001  
**Type:** AUDIT / PROVENANCE PROJECTION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Audit Projection

An Audit Projection is a rebuildable view designed to answer attributable governance/execution questions.

It is not an authority source.

## 2. Required audit questions

Where source data exists, an Audit Projection SHOULD answer:

```text
who/what initiated the action?
which component observed/emitted it?
under which Role / Agent Run?
which Task / Routing / Workflow / Stage?
which Context Bundle(s)?
which exact engineering artifact/revision?
which Review/QA/Quality Assessment?
which Evidence/Finding/Gate Result?
which authority/permission/policy refs applied?
what owner result followed?
what was the explicit causal chain?
```

## 3. Provenance Projection

A Provenance Projection indexes relationships already owned elsewhere.

Target navigable chain:

```text
Task
↓
Routing Decision
↓
Workflow Instance / Stage / Transition
↓
Role / Agent Run
↓
Skill Invocation
↓
Context Request / Bundle
↓
Engineering Change / RCU
↓
Commit / Integration Request / Revision
↓
Quality Assessment
↓
Evidence / Finding / Gate Result
↓
Merge Operation / Integrated Revision
```

Not every Task has every link.

## 4. Ownership rule

If a relation is disputed:

```text
owner-module canonical relation wins
```

The projection is repaired; owner data is not rewritten by Module 08.

## 5. Audit vs diagnostic telemetry

Audit projections rely on declared `REQUIRED_AUDIT` source telemetry plus owner references.

Optional diagnostic logs MUST NOT be a hidden prerequisite for a required audit claim unless the capture contract explicitly upgrades them.

## 6. Audit completeness

Audit projection MUST expose:

```text
completeness_state
source coverage / capture-policy basis
known gaps
projection version
data revision
last_updated_at
```

Missing data does not permit fabricated attribution.

## 7. Payload minimization

Audit views SHOULD dereference governed artifacts on demand rather than duplicate full Context, diffs, documents, prompts, or evidence blobs.

## 8. Critical audit integrity

For audit-relevant observations preserve at least:

```text
immutable event identity
producer attribution
initiator attribution where known
target/domain refs
time
causation where known
result refs
policy/authority/permission refs where supplied
```

UPOS-008 v1 does not claim cryptographic tamper-proofing.

## 9. Security/access boundary

Who may view which audit data, retention obligations, legal deletion/redaction and protected actor data remain pending UPOS-010.
