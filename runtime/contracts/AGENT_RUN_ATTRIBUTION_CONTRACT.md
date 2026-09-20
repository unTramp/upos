# Agent Run Attribution Contract

**ID:** UPOS-02-AGENT-RUN-ATTRIBUTION  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-02  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents organizational attribution for one bounded Agent Run while leaving technical execution state and retry semantics to UPOS-04.

## Required boundaries

- preserve AgentRunRef, Role, Agent Definition/version and Agent Instance attribution;
- preserve Task/Workflow/Stage responsibility refs where applicable;
- do not define CREATED/RUNNING/COMPLETED/FAILED/CANCELLED under UPOS-02;
- do not own retry or Workflow blocking semantics.

## Machine representation

- schema: `schemas/02/agent_organization/agent-run-attribution.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `02_agent_organization/AGENT_OPERATING_MODEL.md`
- `02_agent_organization/AGENT_LIFECYCLE.md`
