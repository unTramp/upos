# Execution Attempt Runtime Contract

**ID:** UPOS-04-EXECUTION-ATTEMPT  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-04  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents technical execution-attempt state around an already-owned AgentRunRef or SkillInvocationRef. It introduces no independent attempt identity.

## Required boundaries

- states are exactly CREATED, RUNNING, COMPLETED, FAILED, CANCELLED;
- FAILED requires `failure_ref`;
- terminal states require `terminal_at`;
- no `execution_attempt_id`, `run_attempt_id`, or `invocation_attempt_id`;
- owner lifecycle/result semantics remain separate.

## Machine representation

- schema: `schemas/04/workflow/execution-attempt.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `04_workflow_engine/FAILURE_RETRY_RECOVERY.md`
- `02_agent_organization/AGENT_OPERATING_MODEL.md`
- `03_skills_system/SKILLS_OPERATING_MODEL.md`
