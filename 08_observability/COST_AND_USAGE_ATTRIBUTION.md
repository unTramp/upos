# Cost and Usage Attribution

**ID:** UPOS-08-CST-001  
**Type:** COST / USAGE STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-008 Observability  
**Version:** 1.0.0

## 1. Scope

UPOS-008 owns normalized semantics for observing resource usage and attributing reproducible cost.

Pricing sources/provider APIs are UPOS-011 bindings.

## 2. Generic usage structure

A usage Event/Span/source record SHOULD be able to represent:

```text
usage_type
quantity
unit

provider_binding_ref
operation_ref

project_id
task_id
workflow_instance_id
agent_run_id
skill_invocation_ref
trace_id
span_id

raw_provider_usage_ref
price_basis_ref
price_basis_version_or_effective_at
currency
calculation_method
calculated_cost

fx_basis_ref                     # only if currency conversion applied
```

No global Resource Usage ID is required by Module 08 v1.

## 3. Usage types

Provider-neutral examples:

```text
INPUT_TOKENS
OUTPUT_TOKENS
CACHED_TOKENS
REASONING_TOKENS_REPORTED
API_REQUEST
COMPUTE_TIME
CPU_TIME
GPU_TIME
STORAGE_BYTES
NETWORK_BYTES
TOOL_EXECUTION_TIME
CI_MINUTES
OTHER_PROVIDER_UNIT
```

Record only categories actually reported/derived with a known basis.

## 4. Reasoning-token rule

Numeric `reasoning_tokens` MAY be recorded if externally reported by the provider.

This does not permit capture of hidden reasoning content.

## 5. Cost reproducibility

Any calculated monetary cost MUST preserve:

```text
raw usage
pricing source/reference
pricing/effective version/date
currency
calculation method
```

Historical cost MUST NOT be silently recomputed under today's pricing and presented as the original incurred cost.

A separate “cost at current pricing” analysis may exist if explicitly labeled.

## 6. Attribution scopes

When source data supports it, usage/cost may aggregate by:

```text
Agent Run
Skill Invocation
Context assembly
Task
Workflow Instance
Quality/review execution
provider binding
integrated change
```

Allocation rules for shared costs must be explicit in the Metric Definition.

## 7. Double counting

If provider billing data overlaps nested Spans/operations, Metric Definitions MUST specify one authoritative cost source/allocation basis.

Do not sum parent billed cost and child billed costs blindly.

## 8. Cost != value

```text
lower cost != better result
```

Cost observations should be interpreted alongside Quality, speed, human attention and governance data.
