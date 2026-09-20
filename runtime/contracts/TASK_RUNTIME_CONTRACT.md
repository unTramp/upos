# Task Runtime Contract

**ID:** UPOS-04-TASK-RUNTIME  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-04  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents canonical Task runtime state using the frozen UPOS-04 Task vocabulary and canonical TaskRef. Transition data is precondition/intent only; transition execution remains outside Phase 3.

## Required boundaries

- consume exact versioned Phase-2 TaskRef;
- preserve only frozen UPOS-04 Task states;
- do not introduce a parallel Task identity;
- do not implement routing, scheduling, or orchestration.

## Machine representation

- schema: `schemas/04/workflow/task-runtime.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `04_workflow_engine/TASK_AND_WORKFLOW_INSTANCE_MODEL.md`
- `runtime/RUNTIME_CONTRACT_GOVERNANCE.md`
- `runtime/RUNTIME_COMPATIBILITY_AND_VERSIONING.md`
