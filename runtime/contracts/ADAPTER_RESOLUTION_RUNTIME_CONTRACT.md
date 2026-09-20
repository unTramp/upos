# Adapter Resolution Runtime Contract

**ID:** UPOS-11-ADAPTER-RESOLUTION  
**Version:** 0.1.0  
**Phase:** 3 / Slice 2  
**Status:** CANDIDATE  
**Normativity:** NORMATIVE IMPLEMENTATION-LAYER CONTRACT  
**Semantic owner:** UPOS-11  
**Runtime/schema steward:** Phase-3 Runtime Contract Layer

## Contract

Represents one technical Adapter Resolution request, the binding evaluation basis, the adapter validation result, and either an owner Adapter Failure or an immutable Resolved Adapter View. It does not implement the resolver and does not contact a provider.

## Required boundaries

- introduces no new domain identity;
- `adapter_resolution_id` is success-only: it identifies the immutable Resolved Adapter View and never a resolution attempt;
- a resolution may fail before any `adapter_resolution_id` exists;
- `operation_request_key` is infrastructure-only technical request correlation;
- every material Adapter Failure produced by an Adapter Resolution MUST retain the originating `operation_request_key`;
- `operation_request_key != adapter_resolution_id`;
- binding candidates are references to canonical `binding_id`, never new entities;
- fallback is UPOS-11 alternate binding selection and is not UPOS-04 retry, rework, recovery or rerouting;
- fallback introduces no identity;
- Adapter Validation Result is not a Security Decision and not a Quality Verdict;
- `VALID_WITH_WARNINGS` must not conceal a missing REQUIRED binding;
- `INCOMPLETE` MAY yield a Resolved Adapter View only when `missing_required_binding_refs` is empty; optional/conditional incompleteness therefore remains representable;
- `INCOMPLETE` with one or more `missing_required_binding_refs` MUST NOT yield a Resolved Adapter View and follows the Adapter Failure path using an applicable existing canonical UPOS-11 failure class;
- Adapter Failure carries no independent identity, carries no `adapter_resolution_id`, and uses only canonical UPOS-11 failure classes;
- provider execution, invocation, health probing, credentials and secrets are out of scope;
- consume exact versioned Phase-2 UPOS-11 refs.

## Machine representation

- schema: `schemas/11/project_adapter/adapter-resolution-request.schema.json`
- schema: `schemas/11/project_adapter/adapter-validation-result.schema.json`
- schema: `schemas/11/project_adapter/adapter-failure.schema.json`
- schema: `schemas/11/project_adapter/resolved-adapter-view.schema.json`
- runtime contract version: `0.1.0`

## Normative sources

- `11_project_adapter/BINDING_RESOLUTION_STANDARD.md`
- `11_project_adapter/PROJECT_ADAPTER_ONTOLOGY.md`
- `11_project_adapter/BINDING_VALIDATION_STANDARD.md`
- `11_project_adapter/ADAPTER_FAILURE_MODEL.md`
- `11_project_adapter/PROJECT_ADAPTER_LIFECYCLE_AND_VERSIONING.md`
- `runtime/RUNTIME_OPERATION_AND_IDEMPOTENCY_STANDARD.md`
- `runtime/RUNTIME_CONTRACT_GOVERNANCE.md`
