# Workflow Instance Runtime Contract

**ID:** UPOS-04-WORKFLOW-INSTANCE-RUNTIME  
**Version:** 0.1.0  
**Phase:** 3 / Slice 1  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-04  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents Workflow Instance and Stage runtime state using frozen UPOS-04 vocabularies and explicit expected-state transition preconditions.

## Required boundaries

- consume canonical WorkflowInstanceRef, StageRef, TaskRef and RoutingDecisionRef;
- preserve frozen Workflow/Stage states;
- transition requests are representations, not executed transitions;
- scheduling and orchestration remain outside Phase 3.

## Machine representation

- schema: `schemas/04/workflow/workflow-instance-runtime.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `04_workflow_engine/TASK_AND_WORKFLOW_INSTANCE_MODEL.md`
- `04_workflow_engine/WORKFLOW_STATE_MODEL.md`
