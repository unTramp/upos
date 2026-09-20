#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY_SCHEMA = SCHEMAS / "meta" / "schema-registry.schema.json"
REGISTRY = SCHEMAS / "registry" / "schema-registry.json"
VALID_FIXTURE = SCHEMAS / "fixtures" / "registry.valid.json"
INVALID_FIXTURE = SCHEMAS / "fixtures" / "registry.invalid.json"

DOCUMENT_MANIFEST_SCHEMA = SCHEMAS / "01" / "documentation" / "document-manifest.schema.json"
SOT_ENTRY_SCHEMA = SCHEMAS / "01" / "documentation" / "source-of-truth-entry.schema.json"
SOT_REGISTRY_SCHEMA = SCHEMAS / "01" / "documentation" / "source-of-truth-registry.schema.json"

DOCUMENTATION_SIMPLE_FIXTURES = [
    (
        DOCUMENT_MANIFEST_SCHEMA,
        SCHEMAS / "fixtures" / "documentation" / "document-manifest.valid.json",
        SCHEMAS / "fixtures" / "documentation" / "document-manifest.invalid.json",
    ),
    (
        SOT_ENTRY_SCHEMA,
        SCHEMAS / "fixtures" / "documentation" / "source-of-truth-entry.valid.json",
        SCHEMAS / "fixtures" / "documentation" / "source-of-truth-entry.invalid.json",
    ),
]

SOT_REGISTRY_VALID = SCHEMAS / "fixtures" / "documentation" / "source-of-truth-registry.valid.json"
SOT_REGISTRY_INVALID_DUPLICATE = SCHEMAS / "fixtures" / "documentation" / "source-of-truth-registry.invalid-duplicate.json"
SOT_REGISTRY_INVALID_OWNER = SCHEMAS / "fixtures" / "documentation" / "source-of-truth-registry.invalid-owner-ambiguity.json"
SOT_REGISTRY_INVALID_ACTIVE_INFORMATIVE = SCHEMAS / "fixtures" / "documentation" / "source-of-truth-registry.invalid-active-informative.json"

PROJECT_MANIFEST_SCHEMA = SCHEMAS / "11" / "project_adapter" / "project-manifest.schema.json"
PROJECT_ADAPTER_SCHEMA = SCHEMAS / "11" / "project_adapter" / "project-adapter.schema.json"
ADAPTER_RESOLUTION_REF_SCHEMA = SCHEMAS / "11" / "project_adapter" / "adapter-resolution-reference.schema.json"

PROJECT_ADAPTER_FIXTURES = [
    (
        PROJECT_MANIFEST_SCHEMA,
        SCHEMAS / "fixtures" / "project_adapter" / "project-manifest.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "project-manifest.invalid.json",
    ),
    (
        ADAPTER_RESOLUTION_REF_SCHEMA,
        SCHEMAS / "fixtures" / "project_adapter" / "adapter-resolution-reference.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "adapter-resolution-reference.invalid.json",
    ),
]

PROJECT_ADAPTER_DIRECT_FIXTURES = [
    (
        SCHEMAS / "11" / "project_adapter" / "binding.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "binding.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "binding.invalid-specialized-type.json",
    ),
    (
        SCHEMAS / "11" / "project_adapter" / "identity-binding.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "identity-binding.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "identity-binding.invalid-missing-provider-version.json",
    ),
    (
        SCHEMAS / "11" / "project_adapter" / "resource-binding.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "resource-binding.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "resource-binding.invalid-missing-resource-type.json",
    ),
    (
        SCHEMAS / "11" / "project_adapter" / "secret-binding.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "secret-binding.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "secret-binding.invalid-missing-use-mode.json",
    ),
    (
        SCHEMAS / "11" / "project_adapter" / "capability-binding.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "capability-binding.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "capability-binding.invalid-missing-support-state.json",
    ),
    (
        SCHEMAS / "11" / "project_adapter" / "provider-adapter.schema.json",
        SCHEMAS / "fixtures" / "project_adapter" / "provider-adapter.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "provider-adapter.invalid-missing-version.json",
    ),
]

ARTIST_OS_PROJECT_MANIFEST = SCHEMAS / "dogfooding" / "artist-os" / "project-manifest.json"
ARTIST_OS_PROJECT_ADAPTER = SCHEMAS / "dogfooding" / "artist-os" / "project-adapter.json"
IDENTITY_FIXTURE_ROOT = SCHEMAS / "fixtures" / "identity_references"
CROSS_MODULE_REFERENCE_SCHEMA = SCHEMAS / "meta" / "cross-module-reference-conformance.schema.json"
CROSS_MODULE_REFERENCE_VALID = SCHEMAS / "fixtures" / "cross_module_references" / "valid.json"
CROSS_MODULE_REFERENCE_INVALID = SCHEMAS / "fixtures" / "cross_module_references" / "invalid-imported-version-requirement.json"
ARTIST_OS_IDENTITY_NAMESPACE = SCHEMAS / "dogfooding" / "artist-os" / "identity-namespace-compatibility.json"

RUNTIME_COMMON_FIXTURES = [
    (
        SCHEMAS / "common" / "runtime-operation-control.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-control.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-control.invalid-empty-key.json",
    ),
    (
        SCHEMAS / "common" / "runtime-operation-outcome.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-outcome.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-outcome.invalid-domain-verdict.json",
    ),
    (
        SCHEMAS / "common" / "runtime-failure-envelope.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-failure-envelope.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-failure-envelope.invalid-runtime-error-id.json",
    ),
]

RUNTIME_OWNER_RESULT_OUTCOME_VALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-outcome.security-deny.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-outcome.quality-fail.valid.json",
]
RUNTIME_OWNER_RESULT_OUTCOME_INVALID = SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-operation-outcome.invalid-quality-pass-state.json"
RUNTIME_OWNER_RESULT_FAILURE_INVALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-failure-envelope.invalid-security-deny.json",
    SCHEMAS / "fixtures" / "runtime" / "common" / "runtime-failure-envelope.invalid-quality-fail.json",
]

RUNTIME_ATTRIBUTION_FIXTURES = [
    (
        SCHEMAS / "02" / "agent_organization" / "agent-run-attribution.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "agent_organization" / "agent-run-attribution.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "agent_organization" / "agent-run-attribution.invalid-execution-state.json",
    ),
    (
        SCHEMAS / "03" / "skills" / "skill-invocation-attribution.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "skills" / "skill-invocation-attribution.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "skills" / "skill-invocation-attribution.invalid-execution-state.json",
    ),
]

RUNTIME_TASK_FIXTURES = [
    (
        SCHEMAS / "04" / "workflow" / "task-runtime.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "task-runtime.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "task-runtime.invalid-in-review-state.json",
    ),
]

RUNTIME_ROUTING_FIXTURES = [
    (
        SCHEMAS / "04" / "workflow" / "routing-runtime.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "routing-runtime.valid-failed-no-decision.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "routing-runtime.invalid-missing-request-key.json",
    ),
]

RUNTIME_WORKFLOW_FIXTURES = [
    (
        SCHEMAS / "04" / "workflow" / "workflow-instance-runtime.schema.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "workflow-instance-runtime.valid.json",
        SCHEMAS / "fixtures" / "runtime" / "workflow" / "workflow-instance-runtime.invalid-state.json",
    ),
]

RUNTIME_EXECUTION_ATTEMPT_SCHEMA = SCHEMAS / "04" / "workflow" / "execution-attempt.schema.json"
RUNTIME_EXECUTION_ATTEMPT_VALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.failed.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.created.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.cancelled.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.versioned.valid.json",
]
RUNTIME_EXECUTION_ATTEMPT_INVALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.invalid-blocked-state.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.invalid-synthetic-id.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.invalid-unsupported-version.json",
]

RUNTIME_RETRY_SCHEMA = SCHEMAS / "04" / "workflow" / "retry-provenance.schema.json"
RUNTIME_RETRY_VALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.agent-run.valid.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.skill-invocation.valid.json",
]
RUNTIME_RETRY_INVALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.invalid-missing-predecessor.json",
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.invalid-missing-trigger.json",
]
RUNTIME_RETRY_INVALID_SAME_REF = SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.invalid-reused-identity.json"
RUNTIME_RETRY_CHAIN_VALID = SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-chain.agent-run.valid.json"

RUNTIME_EVENT_SCHEMA = SCHEMAS / "08" / "observability" / "event.schema.json"
RUNTIME_EVENT_VALID = SCHEMAS / "fixtures" / "runtime" / "observability" / "event.valid.json"
RUNTIME_EVENT_CORRECTION_VALID = SCHEMAS / "fixtures" / "runtime" / "observability" / "event.correction-new-id.valid.json"
RUNTIME_EVENT_INVALID_CORRECTION = SCHEMAS / "fixtures" / "runtime" / "observability" / "event.invalid-correction-missing-reason.json"
RUNTIME_EVENT_INVALID_SAME_CORRECTION = SCHEMAS / "fixtures" / "runtime" / "observability" / "event.invalid-correction-reuses-id.json"
RUNTIME_EVENT_REDELIVERY = [
    SCHEMAS / "fixtures" / "runtime" / "observability" / "event.redelivery-a.json",
    SCHEMAS / "fixtures" / "runtime" / "observability" / "event.redelivery-b.json",
]

RUNTIME_EXECUTION_SPINE_VALID = SCHEMAS / "fixtures" / "runtime" / "execution-spine.valid.json"
RUNTIME_OPERATION_KEY_COLLISION_INVALIDS = [
    SCHEMAS / "fixtures" / "runtime" / "common" / "operation-request-key.invalid-permission-decision.json",
    SCHEMAS / "fixtures" / "runtime" / "common" / "operation-request-key.invalid-adapter-resolution.json",
]
RUNTIME_REDELIVERY_AS_RETRY_INVALID = SCHEMAS / "fixtures" / "runtime" / "workflow" / "technical-redelivery.invalid-as-retry.json"
RUNTIME_PRIVATE_REASONING_INVALID = SCHEMAS / "fixtures" / "runtime" / "execution-spine.invalid-private-reasoning.json"
RUNTIME_ROUTING_INVALID_SAME_KEY = (
    SCHEMAS / "fixtures" / "runtime" / "workflow" / "routing-runtime.invalid-request-key-equals-decision.json"
)

ADAPTER_FIXTURES = SCHEMAS / "fixtures" / "runtime" / "project_adapter"
ADAPTER_SCHEMA_PATHS = {
    "request": SCHEMAS / "11" / "project_adapter" / "adapter-resolution-request.schema.json",
    "validation": SCHEMAS / "11" / "project_adapter" / "adapter-validation-result.schema.json",
    "failure": SCHEMAS / "11" / "project_adapter" / "adapter-failure.schema.json",
    "view": SCHEMAS / "11" / "project_adapter" / "resolved-adapter-view.schema.json",
}
ADAPTER_COMPOSITE_KEYS = {
    "request": "request",
    "validation_result": "validation",
    "adapter_failure": "failure",
    "resolved_adapter_view": "view",
}
ADAPTER_POSITIVE_FIXTURES = [
    ("adapter-resolution-request.valid.json", "request"),
    ("adapter-resolution-request.redelivery-a.json", "request"),
    ("adapter-resolution-request.redelivery-b.json", "request"),
    ("adapter-validation-result.valid.json", "validation"),
    ("adapter-validation-result.warnings.valid.json", "validation"),
    ("adapter-validation-result.incomplete-optional.valid.json", "validation"),
    ("adapter-failure.binding-conflict.valid.json", "failure"),
    ("resolved-adapter-view.valid.json", "view"),
    ("resolved-adapter-view.fallback.valid.json", "view"),
    ("resolved-adapter-view.precedence.valid.json", "view"),
    ("resolved-adapter-view.historical.valid.json", "view"),
]
ADAPTER_COMPOSITE_FIXTURES = [
    "adapter-resolution.direct.valid.json",
    "adapter-resolution.fallback.valid.json",
    "adapter-resolution.precedence.valid.json",
    "adapter-resolution.incomplete-optional.valid.json",
    "adapter-resolution.failed-binding-conflict.valid.json",
]
ADAPTER_COMPOSITE_REQUEST_KEY_MISMATCH = "adapter-resolution.failed-request-key-mismatch.invalid.json"
ADAPTER_EVENT_FIXTURES = [
    "event.adapter-resolution-requested.valid.json",
    "event.adapter-binding-evaluated.valid.json",
    "event.adapter-validation-result.valid.json",
    "event.adapter-resolution-succeeded.valid.json",
    "event.adapter-resolution-failed.valid.json",
    "event.adapter-fallback-selected.valid.json",
]
# (fixture, schema key, expected validator keyword, substring the message must name)
ADAPTER_NEGATIVE_FIXTURES = [
    ("adapter-failure.invalid-resolution-id-on-failure.json", "failure", "additionalProperties", "adapter_resolution_id"),
    ("adapter-resolution-request.invalid-attempt-id.json", "request", "additionalProperties", "adapter_resolution_attempt_id"),
    ("resolved-adapter-view.invalid-binding-attempt-id.json", "view", "additionalProperties", "binding_attempt_id"),
    ("adapter-resolution-request.invalid-missing-request-key.json", "request", "required", "operation_request_key"),
    ("adapter-failure.invalid-missing-request-key.json", "failure", "required", "operation_request_key"),
    ("resolved-adapter-view.invalid-fallback-id.json", "view", "additionalProperties", "fallback_id"),
    ("resolved-adapter-view.invalid-provider-execution.json", "view", "additionalProperties", "api_endpoint"),
    ("adapter-validation-result.invalid-security-verdict.json", "validation", "enum", "DENY"),
    ("adapter-validation-result.invalid-quality-verdict.json", "validation", "enum", "PASS"),
    ("resolved-adapter-view.invalid-retry-as-fallback.json", "view", "additionalProperties", "relation"),
    ("resolved-adapter-view.invalid-trace-runtime.json", "view", "additionalProperties", "span_manager"),
    ("resolved-adapter-view.invalid-unsupported-version.json", "view", "const", "0.1.0"),
    ("adapter-resolution-request.invalid-unknown-contract-ref.json", "request", "const", "UPOS-11-ADAPTER-RESOLUTION"),
    ("resolved-adapter-view.invalid-fabricated-scope.json", "view", "required", "project_id"),
    ("adapter-validation-result.invalid-warnings-hide-required.json", "validation", "maxItems", "empty"),
    ("resolved-adapter-view.invalid-generic-adapter-id.json", "view", "additionalProperties", "adapter_id"),
    ("adapter-resolution-request.invalid-generic-resolution-id.json", "request", "additionalProperties", "resolution_id"),
    ("adapter-failure.invalid-noncanonical-code.json", "failure", "enum", "FALLBACK_EXHAUSTED"),
    ("resolved-adapter-view.invalid-missing-runtime-contract-ref.json", "view", "required", "runtime_contract_ref"),
    ("resolved-adapter-view.invalid-missing-runtime-contract-version.json", "view", "required", "runtime_contract_version"),
    ("resolved-adapter-view.invalid-missing-runtime-schema-version.json", "view", "required", "runtime_schema_version"),
]
PROVIDER_EXECUTION_FIELDS = {
    "api_endpoint", "credentials", "secret_value", "access_token", "invoke",
    "request_body", "response_body", "http_method", "provider_client",
}

FORBIDDEN_SYNTHETIC_IDENTITY_FIELDS = {
    "agent_instance_id",
    "context_view_id",
    "integration_request_id",
    "quality_readiness_id",
    "metric_observation_id",
    "learning_signal_id",
    "learning_evidence_set_id",
    "confirmed_pattern_id",
    "root_cause_hypothesis_id",
    "improvement_opportunity_id",
    "promotion_recommendation_id",
    "learning_backlog_item_id",
    "project_manifest_id",
    "project_adapter_id",
    "security_approval_id",
    "execution_attempt_id",
    "run_attempt_id",
    "invocation_attempt_id",
    "runtime_error_id",
    "retry_id",
    "retry_attempt_id",
    "adapter_resolution_attempt_id",
    "adapter_attempt_id",
    "binding_attempt_id",
    "resolution_id",
    "adapter_id",
    "fallback_id",
    "adapter_validation_id",
    "adapter_failure_id",
    "project_adapter_id",
    "project_manifest_id",
}

RUNTIME_CONTRACT_ARTIFACTS = {
    "UPOS-RUNTIME-GOV-001": ("runtime/RUNTIME_CONTRACT_GOVERNANCE.md", "0.1.0"),
    "UPOS-RUNTIME-OPS-001": ("runtime/RUNTIME_OPERATION_AND_IDEMPOTENCY_STANDARD.md", "0.1.0"),
    "UPOS-RUNTIME-RES-001": ("runtime/RUNTIME_RESULT_AND_FAILURE_STANDARD.md", "0.1.0"),
    "UPOS-RUNTIME-VER-001": ("runtime/RUNTIME_COMPATIBILITY_AND_VERSIONING.md", "0.1.0"),
    "UPOS-RUNTIME-REC-001": ("runtime/RUNTIME_RECONSTRUCTABILITY_STANDARD.md", "0.1.0"),
    "UPOS-RUNTIME-PER-001": ("runtime/RUNTIME_PERSISTENCE_BOUNDARY.md", "0.1.0"),
    "UPOS-02-AGENT-RUN-ATTRIBUTION": ("runtime/contracts/AGENT_RUN_ATTRIBUTION_CONTRACT.md", "0.1.0"),
    "UPOS-03-SKILL-INVOCATION-ATTRIBUTION": ("runtime/contracts/SKILL_INVOCATION_ATTRIBUTION_CONTRACT.md", "0.1.0"),
    "UPOS-04-TASK-RUNTIME": ("runtime/contracts/TASK_RUNTIME_CONTRACT.md", "0.1.0"),
    "UPOS-04-ROUTING-RUNTIME": ("runtime/contracts/ROUTING_RUNTIME_CONTRACT.md", "0.1.0"),
    "UPOS-04-WORKFLOW-INSTANCE-RUNTIME": ("runtime/contracts/WORKFLOW_INSTANCE_RUNTIME_CONTRACT.md", "0.1.0"),
    "UPOS-04-EXECUTION-ATTEMPT": ("runtime/contracts/EXECUTION_ATTEMPT_RUNTIME_CONTRACT.md", "0.1.0"),
    "UPOS-04-RETRY-PROVENANCE": ("runtime/contracts/RETRY_PROVENANCE_RUNTIME_CONTRACT.md", "0.1.0"),
    "UPOS-08-EVENT-EMISSION": ("runtime/contracts/EVENT_EMISSION_INTERFACE.md", "0.1.0"),
    "UPOS-08-EVT-001": ("08_observability/EVENT_STANDARD.md", "1.0.0"),
    "UPOS-11-ADAPTER-RESOLUTION": ("runtime/contracts/ADAPTER_RESOLUTION_RUNTIME_CONTRACT.md", "0.1.0"),
}

# Fixtures whose entire purpose is to violate runtime contract reference or version
# carriage. They are excluded from the resolution walk so that the walk reports real
# defects only; each one is separately asserted to reject by the enforcing path.
CONTRACT_CARRIAGE_NEGATIVE_SUFFIXES = (
    ".invalid-unsupported-version.json",
    ".invalid-unknown-contract-ref.json",
    ".invalid-missing-runtime-contract-ref.json",
    ".invalid-missing-runtime-contract-version.json",
    ".invalid-missing-runtime-schema-version.json",
)

OWNER_BY_PREFIX = {
    "upos.common.": "NONE_INFRASTRUCTURE",
    "upos.01.documentation.": "UPOS-01",
    "upos.02.agent_organization.": "UPOS-02",
    "upos.03.skills.": "UPOS-03",
    "upos.04.workflow.": "UPOS-04",
    "upos.05.context_memory.": "UPOS-05",
    "upos.06.engineering.": "UPOS-06",
    "upos.07.quality.": "UPOS-07",
    "upos.08.observability.": "UPOS-08",
    "upos.09.learning.": "UPOS-09",
    "upos.10.security.": "UPOS-10",
    "upos.11.project_adapter.": "UPOS-11",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


class RuntimeConformanceViolation(ValueError):
    """Deterministic cross-record/runtime-contract conformance rejection."""


PROHIBITED_PRIVATE_REASONING_FIELDS = {
    "private_chain_of_thought",
    "chain_of_thought",
    "private_reasoning",
    "reasoning_trace",
}


def enforce_distinct_values(
    left_name: str,
    left_value: Any,
    right_name: str,
    right_value: Any,
) -> None:
    if left_value is not None and right_value is not None and left_value == right_value:
        raise RuntimeConformanceViolation(
            f"{left_name} must differ from {right_name}: {left_value!r}"
        )


def enforce_operation_request_key_separation(data: dict[str, Any]) -> None:
    control = data.get("operation_control")
    if not isinstance(control, dict):
        return
    request_key = control.get("operation_request_key")
    enforce_distinct_values(
        "operation_request_key",
        request_key,
        "owner_result_ref",
        data.get("owner_result_ref"),
    )
    outcome = data.get("runtime_outcome")
    if isinstance(outcome, dict):
        enforce_distinct_values(
            "operation_request_key",
            request_key,
            "runtime_outcome.owner_result_ref",
            outcome.get("owner_result_ref"),
        )


def enforce_routing_request_result_separation(data: dict[str, Any]) -> None:
    control = data.get("operation_control")
    if not isinstance(control, dict):
        return
    enforce_distinct_values(
        "operation_request_key",
        control.get("operation_request_key"),
        "routing_decision_ref",
        data.get("routing_decision_ref"),
    )


def enforce_retry_identity_separation(data: dict[str, Any]) -> None:
    enforce_distinct_values(
        "successor_ref",
        data.get("successor_ref"),
        "predecessor_ref",
        data.get("predecessor_ref"),
    )


def enforce_redelivery_not_retry(data: dict[str, Any]) -> None:
    control = data.get("operation_control")
    retry = data.get("retry_provenance")
    if not isinstance(control, dict) or not isinstance(retry, dict):
        return
    same_subject = (
        control.get("subject_ref") is not None
        and control.get("subject_ref") == retry.get("predecessor_ref")
        and retry.get("predecessor_ref") == retry.get("successor_ref")
    )
    if same_subject:
        raise RuntimeConformanceViolation(
            "technical redelivery of the same bounded execution identity "
            "must not be represented as UPOS-04 RETRY_OF"
        )


def enforce_event_correction_identity(data: dict[str, Any]) -> None:
    if data.get("correction_of_event_id") is None:
        return
    enforce_distinct_values(
        "event_id",
        data.get("event_id"),
        "correction_of_event_id",
        data.get("correction_of_event_id"),
    )


def enforce_no_private_reasoning(value: Any, *, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in PROHIBITED_PRIVATE_REASONING_FIELDS:
                raise RuntimeConformanceViolation(
                    f"private reasoning field is forbidden in persisted runtime provenance: {path}.{key}"
                )
            enforce_no_private_reasoning(child, path=f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            enforce_no_private_reasoning(child, path=f"{path}[{index}]")


def expect_runtime_conformance_pass(
    label: str,
    check,
    data: dict[str, Any],
) -> None:
    try:
        check(data)
    except RuntimeConformanceViolation as exc:
        fail(f"{label} unexpectedly rejected by runtime conformance: {exc}")
    print(f"FOCUSED PASS: {label}")


def expect_runtime_conformance_reject(
    label: str,
    check,
    data: dict[str, Any],
) -> None:
    try:
        check(data)
    except RuntimeConformanceViolation:
        print(f"FOCUSED REJECT: {label}")
        return
    fail(f"{label} unexpectedly passed runtime conformance")


def iter_refs(value: Any):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                yield child
            yield from iter_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_refs(child)


def expected_owner(schema_key: str) -> str | None:
    for prefix, owner in OWNER_BY_PREFIX.items():
        if schema_key.startswith(prefix):
            return owner
    return None


def load_schema_documents() -> tuple[dict[str, Path], dict[str, dict[str, Any]]]:
    schema_files = sorted(SCHEMAS.rglob("*.schema.json"))
    if not schema_files:
        fail("no JSON Schema documents found")

    ids: dict[str, Path] = {}
    docs: dict[str, dict[str, Any]] = {}

    for path in schema_files:
        schema = load_json(path)

        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(f"{path.relative_to(ROOT)} does not pin JSON Schema Draft 2020-12")

        schema_id = schema.get("$id")
        if not isinstance(schema_id, str) or not schema_id.startswith("urn:upos:schema:"):
            fail(f"{path.relative_to(ROOT)} has missing/non-canonical $id")

        if schema_id in ids:
            fail(
                f"duplicate schema $id {schema_id}: "
                f"{ids[schema_id].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )

        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            fail(f"invalid JSON Schema {path.relative_to(ROOT)}: {exc.message}")

        ids[schema_id] = path
        docs[schema_id] = schema

    for schema_id, schema in docs.items():
        path = ids[schema_id]
        for ref in iter_refs(schema):
            if ref.startswith("#"):
                continue
            base = ref.split("#", 1)[0]
            if not base.startswith("urn:upos:schema:"):
                fail(
                    f"unsupported external $ref in {path.relative_to(ROOT)}: {ref}; "
                    "use canonical U-POS schema URN"
                )
            if base not in ids:
                fail(f"unresolved canonical $ref in {path.relative_to(ROOT)}: {ref}")

    return ids, docs


def build_resource_registry(docs: dict[str, dict[str, Any]]) -> Registry:
    registry = Registry()
    for schema_id, schema in docs.items():
        registry = registry.with_resource(schema_id, Resource.from_contents(schema))
    return registry


def validator_for(
    schema_path: Path,
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> Draft202012Validator:
    schema = load_json(schema_path)
    return Draft202012Validator(
        schema,
        registry=resource_registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )


def validate_registry(schema_ids: dict[str, Path]) -> None:
    validator = Draft202012Validator(load_json(REGISTRY_SCHEMA))
    registry = load_json(REGISTRY)

    try:
        validator.validate(registry)
    except ValidationError as exc:
        location = "/".join(str(x) for x in exc.absolute_path) or "<root>"
        fail(f"registry validation failed at {location}: {exc.message}")

    key_versions = set()
    uris = set()
    keys = {entry["schema_key"] for entry in registry["entries"]}
    uri_to_key = {
        entry["schema_uri"]: entry["schema_key"]
        for entry in registry["entries"]
    }

    for entry in registry["entries"]:
        key_version = (entry["schema_key"], entry["schema_version"])
        if key_version in key_versions:
            fail(f"duplicate registry key/version: {entry['schema_key']}@{entry['schema_version']}")
        key_versions.add(key_version)

        if entry["schema_uri"] in uris:
            fail(f"duplicate registry schema_uri: {entry['schema_uri']}")
        uris.add(entry["schema_uri"])

        owner = expected_owner(entry["schema_key"])
        if owner is None:
            fail(f"unknown schema namespace: {entry['schema_key']}")
        if owner != entry["semantic_owner_module"]:
            fail(
                f"semantic owner mismatch for {entry['schema_key']}: "
                f"expected {owner}, got {entry['semantic_owner_module']}"
            )

        artifact = ROOT / entry["artifact_path"]
        if not artifact.is_file():
            fail(f"registered schema artifact missing: {entry['artifact_path']}")

        artifact_schema = load_json(artifact)
        if artifact_schema.get("$id") != entry["schema_uri"]:
            fail(
                f"registry/artifact $id mismatch for {entry['schema_key']}: "
                f"{entry['schema_uri']} != {artifact_schema.get('$id')}"
            )

        if entry["schema_uri"] not in schema_ids:
            fail(f"registered schema URI not discovered by validator: {entry['schema_uri']}")

        uri_version = entry["schema_uri"].rsplit(":", 1)[-1]
        if uri_version != entry["schema_version"]:
            fail(
                f"schema URI/version mismatch for {entry['schema_key']}: "
                f"{uri_version} != {entry['schema_version']}"
            )

        for ref in entry["normative_source_refs"]:
            if not (ROOT / ref).is_file():
                fail(f"normative source ref missing for {entry['schema_key']}: {ref}")

        declared_dependencies = set(entry["reference_dependencies"])
        for dep in declared_dependencies:
            if dep == entry["schema_key"]:
                fail(f"schema cannot depend on itself: {entry['schema_key']}")
            if dep not in keys:
                fail(f"unresolved registry dependency for {entry['schema_key']}: {dep}")

        actual_dependencies: set[str] = set()
        for ref in iter_refs(artifact_schema):
            if ref.startswith("#"):
                continue
            ref_uri = ref.split("#", 1)[0]
            ref_key = uri_to_key.get(ref_uri)
            if ref_key is None:
                fail(
                    f"registered schema {entry['schema_key']} references unregistered "
                    f"schema URI: {ref_uri}"
                )
            if ref_key != entry["schema_key"]:
                actual_dependencies.add(ref_key)

        missing_declared = actual_dependencies - declared_dependencies
        stale_declared = declared_dependencies - actual_dependencies
        if missing_declared:
            fail(
                f"registry dependency metadata missing actual $ref dependencies for "
                f"{entry['schema_key']}: {sorted(missing_declared)}"
            )
        if stale_declared:
            fail(
                f"registry dependency metadata has stale/non-$ref dependencies for "
                f"{entry['schema_key']}: {sorted(stale_declared)}"
            )


def validate_pair(
    schema_path: Path,
    valid_path: Path,
    invalid_path: Path,
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validator = validator_for(schema_path, docs, resource_registry)

    try:
        validator.validate(load_json(valid_path))
    except ValidationError as exc:
        fail(
            f"positive fixture unexpectedly failed for {schema_path.relative_to(ROOT)}: "
            f"{exc.message}"
        )

    try:
        validator.validate(load_json(invalid_path))
    except ValidationError:
        pass
    else:
        fail(f"negative fixture unexpectedly passed for {schema_path.relative_to(ROOT)}")


def validate_sot_registry_semantics(data: dict[str, Any], *, expect_valid: bool) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    authority_keys: set[tuple[str, str, str]] = set()
    active_owners: dict[str, set[str]] = {}
    active_sources: dict[tuple[str, str], set[str]] = {}

    for entry in data.get("entries", []):
        scope = entry.get("scope")
        owner = entry.get("owner")
        source = entry.get("canonicalSource")
        status = entry.get("status")

        if scope and owner and source:
            key = (scope, owner, source)
            if key in authority_keys:
                errors.append(
                    f"duplicate authority record for scope={scope!r}, owner={owner!r}, source={source!r}"
                )
            authority_keys.add(key)

        if scope and owner and status == "ACTIVE":
            active_owners.setdefault(scope, set()).add(owner)
            if source:
                active_sources.setdefault((scope, owner), set()).add(source)

    for scope, owners in active_owners.items():
        if len(owners) > 1:
            errors.append(
                f"multiple ACTIVE canonical owners for exact scope {scope!r}: {sorted(owners)}"
            )

    for (scope, owner), sources in active_sources.items():
        if len(sources) > 1:
            warnings.append(
                "multiple ACTIVE canonical sources under the same owner "
                f"for scope={scope!r}, owner={owner!r}; content-level SOT-C4 review may be required"
            )

    if expect_valid and errors:
        fail("Source-of-Truth registry semantic validation failed: " + "; ".join(errors))

    if not expect_valid and not errors:
        fail("negative Source-of-Truth registry semantic fixture unexpectedly passed")

    return warnings


def validate_sot_registry_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validator = validator_for(SOT_REGISTRY_SCHEMA, docs, resource_registry)

    valid = load_json(SOT_REGISTRY_VALID)
    try:
        validator.validate(valid)
    except ValidationError as exc:
        fail(f"positive Source-of-Truth registry fixture unexpectedly failed: {exc.message}")
    warnings = validate_sot_registry_semantics(valid, expect_valid=True)
    for warning in warnings:
        print(f"WARNING: {warning}")

    duplicate = load_json(SOT_REGISTRY_INVALID_DUPLICATE)
    try:
        validator.validate(duplicate)
    except ValidationError as exc:
        fail(
            "duplicate authority fixture should be structurally valid before custom semantic "
            f"validation, but failed schema validation: {exc.message}"
        )
    validate_sot_registry_semantics(duplicate, expect_valid=False)

    owner_ambiguity = load_json(SOT_REGISTRY_INVALID_OWNER)
    try:
        validator.validate(owner_ambiguity)
    except ValidationError as exc:
        fail(
            "owner ambiguity fixture should be structurally valid before custom semantic "
            f"validation, but failed schema validation: {exc.message}"
        )
    validate_sot_registry_semantics(owner_ambiguity, expect_valid=False)

    active_informative = load_json(SOT_REGISTRY_INVALID_ACTIVE_INFORMATIVE)
    try:
        validator.validate(active_informative)
    except ValidationError:
        pass
    else:
        fail("ACTIVE informative Source-of-Truth registry fixture unexpectedly passed")



def validate_project_manifest_adapter_pair(
    manifest: dict[str, Any],
    adapter: dict[str, Any],
    *,
    expect_valid: bool,
) -> None:
    errors: list[str] = []

    project_id = manifest.get("project", {}).get("project_id")
    if project_id != adapter.get("project_id"):
        errors.append(
            f"project mismatch: manifest={project_id!r}, adapter={adapter.get('project_id')!r}"
        )

    if manifest.get("manifest_version") != adapter.get("project_manifest_version"):
        errors.append("manifest/adapter manifest version mismatch")

    if manifest.get("project_adapter_version") != adapter.get("project_adapter_version"):
        errors.append("manifest/adapter adapter version mismatch")

    if manifest.get("upos_baseline", {}).get("version") != adapter.get("upos_baseline"):
        errors.append("manifest/adapter U-POS baseline mismatch")

    binding_ids: dict[str, dict[str, Any]] = {}
    repository_refs: dict[str, dict[str, Any]] = {}

    for binding in adapter.get("bindings", []):
        binding_id = binding["binding_id"]
        if binding_id in binding_ids:
            errors.append(f"duplicate binding_id: {binding_id}")
        binding_ids[binding_id] = binding

        binding_type = binding.get("binding_type")
        if binding_type == "REPOSITORY_BINDING":
            repository_ref = binding.get("repository_ref")
            if repository_ref in repository_refs:
                errors.append(f"duplicate repository_ref: {repository_ref}")
            elif repository_ref:
                repository_refs[repository_ref] = binding
        elif "scope" in binding:
            if binding.get("scope", {}).get("project_id") != adapter.get("project_id"):
                errors.append(f"binding {binding_id} belongs to a different project scope")

    # Repository declarations preserve both the reusable repository_ref and
    # the concrete Repository Binding identity.
    all_refs: set[str] = set()
    for declaration in manifest.get("repositories", []):
        repository_ref = declaration.get("repository_ref")
        binding_id = declaration.get("binding_id")
        all_refs.add(binding_id)
        binding = binding_ids.get(binding_id)
        if binding is None:
            errors.append(f"manifest repository declaration references missing binding: {binding_id}")
            continue
        if binding.get("binding_type") != "REPOSITORY_BINDING":
            errors.append(
                f"manifest repository binding {binding_id} has incompatible type "
                f"{binding.get('binding_type')}"
            )
        if binding.get("repository_ref") != repository_ref:
            errors.append(
                f"manifest repository_ref {repository_ref!r} does not match "
                f"Repository Binding {binding_id} repository_ref "
                f"{binding.get('repository_ref')!r}"
            )

    # Specialized repository-relative contracts must resolve repository_ref,
    # never a Repository Binding ID substituted by convenience.
    for binding in adapter.get("bindings", []):
        if binding.get("binding_type") == "PATH_BINDING":
            repository_ref = binding.get("repository_ref")
            if repository_ref not in repository_refs:
                errors.append(
                    f"path binding {binding['binding_id']} references unknown "
                    f"repository_ref: {repository_ref}"
                )

    # Repository Binding path_binding_refs must point back to PATH_BINDINGs
    # in the same repository namespace.
    for repository_ref, repository_binding in repository_refs.items():
        for path_binding_id in repository_binding.get("path_binding_refs", []):
            path_binding = binding_ids.get(path_binding_id)
            if path_binding is None:
                errors.append(
                    f"Repository Binding {repository_binding['binding_id']} references "
                    f"missing path binding: {path_binding_id}"
                )
                continue
            if path_binding.get("binding_type") != "PATH_BINDING":
                errors.append(
                    f"Repository Binding {repository_binding['binding_id']} path ref "
                    f"{path_binding_id} is not PATH_BINDING"
                )
            elif path_binding.get("repository_ref") != repository_ref:
                errors.append(
                    f"path binding {path_binding_id} repository_ref "
                    f"{path_binding.get('repository_ref')!r} does not match owning "
                    f"Repository Binding repository_ref {repository_ref!r}"
                )

    provider_adapters: dict[tuple[str, str], dict[str, Any]] = {}
    for provider in adapter.get("provider_adapters", []):
        identity = (
            provider["provider_adapter_ref"],
            provider["provider_adapter_version"],
        )
        if identity in provider_adapters:
            errors.append(
                "duplicate Provider Adapter identity: "
                f"{identity[0]}@{identity[1]}"
            )
        provider_adapters[identity] = provider

    for declaration in manifest.get("providers", []):
        identity = (
            declaration.get("provider_adapter_ref"),
            declaration.get("provider_adapter_version"),
        )
        if identity not in provider_adapters:
            errors.append(
                "manifest providers references missing Provider Adapter: "
                f"{identity[0]}@{identity[1]}"
            )

    for binding in adapter.get("bindings", []):
        provider_ref = binding.get("provider_adapter_ref")
        provider_version = binding.get("provider_adapter_version")
        if provider_ref is not None or provider_version is not None:
            if not provider_ref or not provider_version:
                errors.append(
                    f"binding {binding['binding_id']} has incomplete Provider Adapter identity"
                )
            elif (provider_ref, provider_version) not in provider_adapters:
                errors.append(
                    f"binding {binding['binding_id']} references missing Provider Adapter "
                    f"{provider_ref}@{provider_version}"
                )

    command_ids: dict[str, dict[str, Any]] = {}
    for command in adapter.get("command_bindings", []):
        command_id = command["command_binding_id"]
        if command_id in command_ids:
            errors.append(f"duplicate command_binding_id: {command_id}")
        command_ids[command_id] = command
        repository_ref = command.get("repository_ref")
        if repository_ref not in repository_refs:
            errors.append(
                f"command binding {command_id} references unknown repository_ref: "
                f"{repository_ref}"
            )

    expected_types = {
        "paths": {"PATH_BINDING"},
        "environments": {"ENVIRONMENT_BINDING"},
        "identity_bindings": {"IDENTITY_BINDING"},
        "resource_bindings": {"RESOURCE_BINDING"},
        "capability_bindings": {"CAPABILITY_BINDING"},
        "secret_bindings": {"SECRET_BINDING"},
        "quality_bindings": {"QUALITY_BINDING"},
        "observability_bindings": {"OBSERVABILITY_BINDING"},
        "learning_bindings": {"LEARNING_BINDING"},
    }

    for section, allowed_types in expected_types.items():
        for ref in manifest.get(section, []):
            all_refs.add(ref)
            binding = binding_ids.get(ref)
            if binding is None:
                errors.append(f"manifest {section} references missing binding: {ref}")
                continue
            if binding.get("binding_type") not in allowed_types:
                errors.append(
                    f"manifest {section} ref {ref} has incompatible type "
                    f"{binding.get('binding_type')}"
                )

    for ref in manifest.get("commands", []):
        if ref not in command_ids:
            errors.append(f"manifest commands references missing command binding: {ref}")

    for ref in manifest.get("runtime", {}).get("binding_refs", []):
        all_refs.add(ref)
        if ref not in binding_ids:
            errors.append(f"manifest runtime references missing binding: {ref}")

    # Security bindings may compose multiple binding classes; existence is
    # enforced here while permission semantics remain UPOS-010-owned.
    for ref in manifest.get("security_bindings", []):
        all_refs.add(ref)
        if ref not in binding_ids:
            errors.append(f"manifest security_bindings references missing binding: {ref}")

    # Requiredness is only evaluated where the frozen specialized/generic
    # contract actually defines it. Do not invent requiredness for
    # Repository/Environment Binding standards that omit that field.
    unreferenced_required = [
        b["binding_id"]
        for b in adapter.get("bindings", [])
        if b.get("requiredness") == "REQUIRED"
        and b["binding_id"] not in all_refs
    ]
    if unreferenced_required:
        errors.append(
            "REQUIRED bindings are not referenced by manifest: "
            + ", ".join(sorted(unreferenced_required))
        )

    if expect_valid and errors:
        fail("Project Manifest/Adapter validation failed: " + "; ".join(errors))
    if not expect_valid and not errors:
        fail("negative Project Manifest/Adapter semantic fixture unexpectedly passed")

def validate_project_adapter_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    for schema_path, valid_path, invalid_path in PROJECT_ADAPTER_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)

    for schema_path, valid_path, invalid_path in PROJECT_ADAPTER_DIRECT_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)

    adapter_validator = validator_for(PROJECT_ADAPTER_SCHEMA, docs, resource_registry)

    manifest = load_json(
        SCHEMAS / "fixtures" / "project_adapter" / "project-manifest.valid.json"
    )
    adapter = load_json(
        SCHEMAS / "fixtures" / "project_adapter" / "project-adapter.valid.json"
    )
    try:
        adapter_validator.validate(adapter)
    except ValidationError as exc:
        fail(f"positive Project Adapter fixture unexpectedly failed: {exc.message}")
    validate_project_manifest_adapter_pair(manifest, adapter, expect_valid=True)

    invalid_adapter = load_json(
        SCHEMAS / "fixtures" / "project_adapter" / "project-adapter.invalid.json"
    )
    try:
        adapter_validator.validate(invalid_adapter)
    except ValidationError as exc:
        fail(
            "negative Project Adapter semantic fixture should pass structural schema "
            f"before semantic validation, but failed: {exc.message}"
        )
    validate_project_manifest_adapter_pair(manifest, invalid_adapter, expect_valid=False)

    artist_manifest = load_json(ARTIST_OS_PROJECT_MANIFEST)
    artist_adapter = load_json(ARTIST_OS_PROJECT_ADAPTER)
    manifest_validator = validator_for(PROJECT_MANIFEST_SCHEMA, docs, resource_registry)

    try:
        manifest_validator.validate(artist_manifest)
        adapter_validator.validate(artist_adapter)
    except ValidationError as exc:
        fail(f"Artist OS Phase 2C dogfooding schema validation failed: {exc.message}")

    validate_project_manifest_adapter_pair(
        artist_manifest,
        artist_adapter,
        expect_valid=True,
    )


def validate_identity_reference_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    schema_paths = sorted(SCHEMAS.glob("[0-9][0-9]/*/identity-references.schema.json"))
    for schema_path in schema_paths:
        fixture_dir = IDENTITY_FIXTURE_ROOT / schema_path.parent.name
        valid_path = fixture_dir / "valid.json"
        invalid_paths = sorted(fixture_dir.glob("invalid-*.json"))

        if not valid_path.is_file():
            fail(f"missing positive identity fixture for {schema_path.relative_to(ROOT)}")
        if not invalid_paths:
            fail(f"missing negative identity fixture for {schema_path.relative_to(ROOT)}")

        validator = validator_for(schema_path, docs, resource_registry)
        try:
            validator.validate(load_json(valid_path))
        except ValidationError as exc:
            fail(
                f"positive identity fixture unexpectedly failed for "
                f"{schema_path.relative_to(ROOT)}: {exc.message}"
            )

        for invalid_path in invalid_paths:
            try:
                validator.validate(load_json(invalid_path))
            except ValidationError:
                continue
            fail(
                f"negative identity fixture unexpectedly passed for "
                f"{schema_path.relative_to(ROOT)}: {invalid_path.name}"
            )


def collect_schema_property_names(value: Any) -> set[str]:
    names: set[str] = set()
    if isinstance(value, dict):
        properties = value.get("properties")
        if isinstance(properties, dict):
            names.update(properties.keys())
        for child in value.values():
            names.update(collect_schema_property_names(child))
    elif isinstance(value, list):
        for child in value:
            names.update(collect_schema_property_names(child))
    return names


def resolve_runtime_contract_reference(
    ref_key: str,
    ref: Any,
    version: Any,
) -> str | None:
    """Fail-closed runtime contract resolution.

    Returns None when the reference resolves at a supported version, otherwise a
    description of the defect. Both the fixture walk and the focused Slice-2
    proofs call this single function, so no proof can claim a rejection that the
    enforcing path would not actually produce.
    """
    if ref not in RUNTIME_CONTRACT_ARTIFACTS:
        return f"unresolved {ref_key}: {ref!r}"
    expected_version = RUNTIME_CONTRACT_ARTIFACTS[ref][1]
    if version != expected_version:
        return (
            f"unsupported {ref_key} version: "
            f"{ref}@{version!r}; supported={expected_version}"
        )
    return None


def validate_runtime_contract_references() -> None:
    for contract_ref, (artifact_path, supported_version) in RUNTIME_CONTRACT_ARTIFACTS.items():
        artifact = ROOT / artifact_path
        if not artifact.is_file():
            fail(f"runtime contract reference {contract_ref} resolves to missing artifact: {artifact_path}")
        text = artifact.read_text(encoding="utf-8")
        if f"**ID:** {contract_ref}" not in text:
            fail(f"runtime contract artifact ID mismatch for {contract_ref}: {artifact_path}")
        if f"**Version:** {supported_version}" in text:
            continue
        fail(
            f"runtime contract artifact version mismatch for {contract_ref}: "
            f"expected {supported_version} in {artifact_path}"
        )

    fixture_root = SCHEMAS / "fixtures" / "runtime"
    contract_key_to_version_key = {
        "runtime_contract_ref": "runtime_contract_version",
        "event_contract_ref": "event_contract_version",
        "producer_contract_ref": "producer_contract_version",
    }

    def walk(value: Any, source: Path, path: str = "$") -> None:
        if isinstance(value, dict):
            for ref_key, version_key in contract_key_to_version_key.items():
                if ref_key not in value:
                    continue
                problem = resolve_runtime_contract_reference(
                    ref_key, value.get(ref_key), value.get(version_key)
                )
                if problem is not None:
                    fail(f"{problem} in {source.relative_to(ROOT)} at {path}")
            for key, child in value.items():
                walk(child, source, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, source, f"{path}[{index}]")

    for fixture in sorted(fixture_root.rglob("*.json")):
        if fixture.name.endswith(CONTRACT_CARRIAGE_NEGATIVE_SUFFIXES):
            continue
        walk(load_json(fixture), fixture)


def validate_durable_runtime_version_carriage(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    cases = [
        (
            SCHEMAS / "02" / "agent_organization" / "agent-run-attribution.schema.json",
            SCHEMAS / "fixtures" / "runtime" / "agent_organization" / "agent-run-attribution.valid.json",
        ),
        (
            SCHEMAS / "03" / "skills" / "skill-invocation-attribution.schema.json",
            SCHEMAS / "fixtures" / "runtime" / "skills" / "skill-invocation-attribution.valid.json",
        ),
        (
            SCHEMAS / "04" / "workflow" / "task-runtime.schema.json",
            SCHEMAS / "fixtures" / "runtime" / "workflow" / "task-runtime.valid.json",
        ),
        (
            SCHEMAS / "04" / "workflow" / "workflow-instance-runtime.schema.json",
            SCHEMAS / "fixtures" / "runtime" / "workflow" / "workflow-instance-runtime.valid.json",
        ),
        (
            RUNTIME_EXECUTION_ATTEMPT_SCHEMA,
            SCHEMAS / "fixtures" / "runtime" / "workflow" / "execution-attempt.created.valid.json",
        ),
        (
            RUNTIME_RETRY_SCHEMA,
            SCHEMAS / "fixtures" / "runtime" / "workflow" / "retry-provenance.agent-run.valid.json",
        ),
    ]

    required_version_fields = (
        "runtime_contract_ref",
        "runtime_contract_version",
        "runtime_schema_version",
    )

    for schema_path, fixture_path in cases:
        validator = validator_for(schema_path, docs, resource_registry)
        stored = load_json(fixture_path)

        for field in required_version_fields:
            if field not in stored:
                fail(
                    f"stored durable fixture {fixture_path.relative_to(ROOT)} "
                    f"is missing required version carriage field: {field}"
                )

        try:
            validator.validate(stored)
        except ValidationError as exc:
            fail(
                f"stored durable versioned fixture unexpectedly failed for "
                f"{schema_path.relative_to(ROOT)}: {exc.message}"
            )
        print(
            f"FOCUSED PASS: stored durable version carriage "
            f"{schema_path.relative_to(ROOT)}"
        )

        for field in required_version_fields:
            missing = json.loads(json.dumps(stored))
            del missing[field]
            try:
                validator.validate(missing)
            except ValidationError:
                print(
                    f"FOCUSED REJECT: missing {field} "
                    f"{schema_path.relative_to(ROOT)}"
                )
            else:
                fail(
                    f"durable record missing {field} unexpectedly passed for "
                    f"{schema_path.relative_to(ROOT)}"
                )

        unsupported_contract = json.loads(json.dumps(stored))
        unsupported_contract["runtime_contract_version"] = "99.0.0"
        try:
            validator.validate(unsupported_contract)
        except ValidationError:
            print(
                f"FOCUSED REJECT: unsupported runtime contract version "
                f"{schema_path.relative_to(ROOT)}"
            )
        else:
            fail(
                f"unsupported runtime contract version unexpectedly passed for "
                f"{schema_path.relative_to(ROOT)}"
            )

        unsupported_schema = json.loads(json.dumps(stored))
        unsupported_schema["runtime_schema_version"] = "99.0.0"
        try:
            validator.validate(unsupported_schema)
        except ValidationError:
            print(
                f"FOCUSED REJECT: unsupported runtime schema version "
                f"{schema_path.relative_to(ROOT)}"
            )
        else:
            fail(
                f"unsupported runtime schema version unexpectedly passed for "
                f"{schema_path.relative_to(ROOT)}"
            )


def validate_forbidden_identity_properties(
    docs: dict[str, dict[str, Any]],
) -> None:
    for schema_id, schema in docs.items():
        forbidden = (
            collect_schema_property_names(schema)
            & FORBIDDEN_SYNTHETIC_IDENTITY_FIELDS
        )
        if forbidden:
            fail(
                f"schema {schema_id} introduces frozen-rejected synthetic identity "
                f"field(s): {sorted(forbidden)}"
            )


def validate_artist_os_identity_namespace() -> None:
    data = load_json(ARTIST_OS_IDENTITY_NAMESPACE)
    project_namespace = data.get("project_namespace")
    reserved_prefix = data.get("reserved_framework_schema_prefix")
    concepts = data.get("project_concepts")
    automatic_mappings = data.get("automatic_mappings")

    if not isinstance(project_namespace, str) or not project_namespace:
        fail("Artist OS namespace fixture has missing project_namespace")
    if not isinstance(reserved_prefix, str) or not reserved_prefix:
        fail("Artist OS namespace fixture has missing reserved framework prefix")
    if project_namespace == "upos" or project_namespace.startswith(reserved_prefix):
        fail("Artist OS product namespace collides with reserved U-POS namespace")
    if not isinstance(concepts, list) or not concepts:
        fail("Artist OS namespace fixture has no product concepts")
    if automatic_mappings != []:
        fail("Artist OS namespace fixture authorizes automatic U-POS mappings")

    expected_prefix = project_namespace + "."
    for concept in concepts:
        if not isinstance(concept, str) or not concept.startswith(expected_prefix):
            fail(f"Artist OS product concept is outside project namespace: {concept!r}")
        if concept.startswith(reserved_prefix):
            fail(f"Artist OS product concept collides with U-POS namespace: {concept!r}")


def validate_operation_request_key_boundaries(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    control_validator = validator_for(
        SCHEMAS / "common" / "runtime-operation-control.schema.json",
        docs,
        resource_registry,
    )
    for invalid_path in RUNTIME_OPERATION_KEY_COLLISION_INVALIDS:
        data = load_json(invalid_path)
        try:
            control_validator.validate(data["operation_control"])
        except ValidationError as exc:
            fail(f"operation-key collision fixture must have a valid operation_control: {invalid_path.name}: {exc.message}")
        expect_runtime_conformance_reject(
            f"operation-key/owner-result collision fixture {invalid_path.name}",
            enforce_operation_request_key_separation,
            data,
        )
        distinct = json.loads(json.dumps(data))
        distinct["owner_result_ref"] = str(distinct["owner_result_ref"]) + ":distinct"
        expect_runtime_conformance_pass(
            f"operation-key/owner-result distinct positive case {invalid_path.name}",
            enforce_operation_request_key_separation,
            distinct,
        )


def validate_execution_spine_reconstructability(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    data = load_json(RUNTIME_EXECUTION_SPINE_VALID)
    expect_runtime_conformance_pass(
        "execution-spine private-reasoning exclusion",
        enforce_no_private_reasoning,
        data,
    )
    expect_runtime_conformance_pass(
        "execution-spine routing request/result separation",
        enforce_routing_request_result_separation,
        data["routing"],
    )
    expect_runtime_conformance_pass(
        "execution-spine operation-key/owner-result separation",
        enforce_operation_request_key_separation,
        data["routing"],
    )
    if data.get("fixture_level") != "FIXTURE":
        fail("execution-spine conformance data must be explicitly labeled FIXTURE")

    component_schemas = {
        "task": SCHEMAS / "04" / "workflow" / "task-runtime.schema.json",
        "routing": SCHEMAS / "04" / "workflow" / "routing-runtime.schema.json",
        "workflow": SCHEMAS / "04" / "workflow" / "workflow-instance-runtime.schema.json",
        "agent_run_attribution": SCHEMAS / "02" / "agent_organization" / "agent-run-attribution.schema.json",
        "agent_run_attempt": SCHEMAS / "04" / "workflow" / "execution-attempt.schema.json",
        "skill_invocation_attribution": SCHEMAS / "03" / "skills" / "skill-invocation-attribution.schema.json",
        "skill_invocation_attempt": SCHEMAS / "04" / "workflow" / "execution-attempt.schema.json",
        "runtime_outcome": SCHEMAS / "common" / "runtime-operation-outcome.schema.json",
        "event": SCHEMAS / "08" / "observability" / "event.schema.json",
    }
    for key, schema_path in component_schemas.items():
        try:
            validator_for(schema_path, docs, resource_registry).validate(data[key])
        except ValidationError as exc:
            fail(f"execution-spine component {key} failed validation: {exc.message}")

    control_validator = validator_for(
        SCHEMAS / "common" / "runtime-operation-control.schema.json",
        docs,
        resource_registry,
    )
    redelivery = data.get("technical_redelivery", [])
    if len(redelivery) != 2:
        fail("execution-spine fixture must contain two technical redelivery records")
    for control in redelivery:
        try:
            control_validator.validate(control)
        except ValidationError as exc:
            fail(f"technical redelivery operation_control failed validation: {exc.message}")
    if redelivery[0]["operation_request_key"] != redelivery[1]["operation_request_key"]:
        fail("technical redelivery must reuse operation_request_key")
    if redelivery[0]["subject_ref"] != redelivery[1]["subject_ref"]:
        fail("technical redelivery must preserve owner subject identity")
    expect_runtime_conformance_pass(
        "technical redelivery preserves identity without RETRY_OF",
        enforce_redelivery_not_retry,
        {"operation_control": redelivery[0]},
    )

    task_ref = data["task"]["task_ref"]
    routing_ref = data["routing"].get("routing_decision_ref")
    workflow_ref = data["workflow"]["workflow_instance_ref"]
    stage_ref = data["workflow"]["stages"][0]["stage_ref"]
    agent_run_ref = data["agent_run_attribution"]["agent_run_ref"]
    skill_invocation_ref = data["skill_invocation_attribution"]["skill_invocation_ref"]

    consistency_checks = [
        (data["routing"]["task_ref"], task_ref, "routing task"),
        (data["workflow"]["task_ref"], task_ref, "workflow task"),
        (data["workflow"]["routing_decision_ref"], routing_ref, "workflow routing decision"),
        (data["agent_run_attribution"]["task_ref"], task_ref, "Agent Run task"),
        (data["agent_run_attribution"].get("workflow_instance_ref"), workflow_ref, "Agent Run workflow"),
        (data["agent_run_attribution"].get("stage_ref"), stage_ref, "Agent Run stage"),
        (data["agent_run_attempt"]["subject_ref"], agent_run_ref, "Agent Run attempt subject"),
        (data["skill_invocation_attribution"]["agent_run_ref"], agent_run_ref, "Skill Invocation Agent Run"),
        (data["skill_invocation_attribution"]["task_ref"], task_ref, "Skill Invocation task"),
        (data["skill_invocation_attribution"].get("workflow_instance_ref"), workflow_ref, "Skill Invocation workflow"),
        (data["skill_invocation_attribution"].get("stage_ref"), stage_ref, "Skill Invocation stage"),
        (data["skill_invocation_attempt"]["subject_ref"], skill_invocation_ref, "Skill Invocation attempt subject"),
        (data["skill_invocation_attribution"]["context_bundle_refs"][0], data["context_bundle_ref"], "Context Bundle"),
        (data["skill_invocation_attribution"]["skill_result_ref"], data["skill_result_ref"], "Skill Result"),
        (data["runtime_outcome"]["subject_ref"], skill_invocation_ref, "runtime outcome subject"),
        (data["runtime_outcome"]["owner_result_ref"], data["skill_result_ref"], "runtime owner result"),
        (data["event"]["event_id"], data["runtime_outcome"]["event_refs"][0], "Event reference"),
        (data["event"]["task_ref"], task_ref, "Event task"),
        (data["event"]["routing_decision_ref"], routing_ref, "Event routing decision"),
        (data["event"]["workflow_instance_ref"], workflow_ref, "Event workflow"),
        (data["event"]["stage_ref"], stage_ref, "Event stage"),
        (data["event"]["producer_agent_run_ref"], agent_run_ref, "Event Agent Run"),
        (data["event"]["skill_invocation_ref"], skill_invocation_ref, "Event Skill Invocation"),
        (data["event"]["context_bundle_ref"], data["context_bundle_ref"], "Event Context Bundle"),
        (data["event"]["owner_result_ref"], data["skill_result_ref"], "Event owner result"),
    ]
    for actual, expected, label in consistency_checks:
        if actual != expected:
            fail(f"execution-spine reconstructability mismatch for {label}: {actual!r} != {expected!r}")

    redelivery_retry = load_json(RUNTIME_REDELIVERY_AS_RETRY_INVALID)
    try:
        control_validator.validate(redelivery_retry["operation_control"])
        validator_for(RUNTIME_RETRY_SCHEMA, docs, resource_registry).validate(redelivery_retry["retry_provenance"])
    except ValidationError as exc:
        fail(f"redelivery-as-retry negative fixture must be structurally valid: {exc.message}")
    expect_runtime_conformance_reject(
        "technical redelivery represented as workflow retry",
        enforce_redelivery_not_retry,
        redelivery_retry,
    )

    private = load_json(RUNTIME_PRIVATE_REASONING_INVALID)
    expect_runtime_conformance_reject(
        "persisted private reasoning fixture",
        enforce_no_private_reasoning,
        private,
    )


def validate_failure_envelope_version_carriage(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    schema_path = SCHEMAS / "common" / "runtime-failure-envelope.schema.json"
    valid_path = (
        SCHEMAS / "fixtures" / "runtime" / "common"
        / "runtime-failure-envelope.valid.json"
    )
    validator = validator_for(schema_path, docs, resource_registry)
    stored = load_json(valid_path)

    try:
        validator.validate(stored)
    except ValidationError as exc:
        fail(f"stored runtime failure envelope unexpectedly failed: {exc.message}")

    ref = stored.get("runtime_contract_ref")
    version = stored.get("runtime_contract_version")
    if ref not in RUNTIME_CONTRACT_ARTIFACTS:
        fail(f"stored runtime failure envelope has unresolved runtime contract: {ref!r}")
    expected = RUNTIME_CONTRACT_ARTIFACTS[ref][1]
    if version != expected:
        fail(
            "stored runtime failure envelope has unsupported runtime contract "
            f"version: {ref}@{version!r}; supported={expected}"
        )
    print("FOCUSED PASS: stored runtime failure envelope with supported contract metadata")

    for field in ("runtime_contract_ref", "runtime_contract_version"):
        missing = json.loads(json.dumps(stored))
        del missing[field]
        try:
            validator.validate(missing)
        except ValidationError as exc:
            if exc.validator != "required":
                fail(
                    f"runtime failure envelope missing {field} rejected for "
                    f"unexpected reason: {exc.validator}: {exc.message}"
                )
            print(f"FOCUSED REJECT: runtime failure envelope missing {field}")
        else:
            fail(f"runtime failure envelope missing {field} unexpectedly passed")

    unsupported = json.loads(json.dumps(stored))
    unsupported["runtime_contract_version"] = "99.0.0"
    try:
        validator.validate(unsupported)
    except ValidationError as exc:
        fail(
            "unsupported runtime failure envelope contract version should remain "
            f"structurally valid before fail-closed contract resolution: {exc.message}"
        )
    unsupported_ref = unsupported["runtime_contract_ref"]
    expected = RUNTIME_CONTRACT_ARTIFACTS[unsupported_ref][1]
    if unsupported["runtime_contract_version"] == expected:
        fail("unsupported runtime failure envelope contract mutation did not change version")
    print("FOCUSED REJECT: unsupported runtime failure envelope contract version")

    negative_expectations = (
        (
            SCHEMAS / "fixtures" / "runtime" / "common"
            / "runtime-failure-envelope.invalid-security-deny.json",
            "not",
            "failure_code",
            "Security verdict contamination",
        ),
        (
            SCHEMAS / "fixtures" / "runtime" / "common"
            / "runtime-failure-envelope.invalid-quality-fail.json",
            "not",
            "failure_code",
            "Quality verdict contamination",
        ),
        (
            SCHEMAS / "fixtures" / "runtime" / "common"
            / "runtime-failure-envelope.invalid-runtime-error-id.json",
            "additionalProperties",
            None,
            "synthetic runtime error identity",
        ),
    )
    for path, expected_validator, expected_path, label in negative_expectations:
        errors = list(validator.iter_errors(load_json(path)))
        if len(errors) != 1:
            fail(
                f"{label} fixture must reject for exactly one original invariant; "
                f"got {len(errors)} errors"
            )
        exc = errors[0]
        actual_path = "/".join(str(x) for x in exc.absolute_path)
        if exc.validator != expected_validator:
            fail(
                f"{label} fixture rejected for unexpected validator "
                f"{exc.validator!r}: {exc.message}"
            )
        if expected_path is not None and actual_path != expected_path:
            fail(
                f"{label} fixture rejected at unexpected path "
                f"{actual_path!r}: {exc.message}"
            )
        if label == "synthetic runtime error identity" and "runtime_error_id" not in exc.message:
            fail(
                "synthetic runtime error identity fixture did not reject "
                f"runtime_error_id specifically: {exc.message}"
            )
        print(f"FOCUSED REJECT: {label} preserved")


def validate_owner_result_runtime_boundaries(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    outcome_schema = SCHEMAS / "common" / "runtime-operation-outcome.schema.json"
    outcome_validator = validator_for(outcome_schema, docs, resource_registry)
    for valid_path in RUNTIME_OWNER_RESULT_OUTCOME_VALIDS:
        try:
            outcome_validator.validate(load_json(valid_path))
        except ValidationError as exc:
            fail(f"owner-result/technical-outcome positive fixture failed: {valid_path.name}: {exc.message}")
    try:
        outcome_validator.validate(load_json(RUNTIME_OWNER_RESULT_OUTCOME_INVALID))
    except ValidationError:
        pass
    else:
        fail("Quality PASS used as technical execution state unexpectedly passed")

    failure_schema = SCHEMAS / "common" / "runtime-failure-envelope.schema.json"
    failure_validator = validator_for(failure_schema, docs, resource_registry)
    for invalid_path in RUNTIME_OWNER_RESULT_FAILURE_INVALIDS:
        try:
            failure_validator.validate(load_json(invalid_path))
        except ValidationError:
            continue
        fail(f"owner result used as technical runtime failure unexpectedly passed: {invalid_path.name}")


def validate_runtime_event_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validator = validator_for(RUNTIME_EVENT_SCHEMA, docs, resource_registry)
    try:
        validator.validate(load_json(RUNTIME_EVENT_VALID))
    except ValidationError as exc:
        fail(f"positive runtime Event fixture unexpectedly failed: {exc.message}")
    correction_valid = load_json(RUNTIME_EVENT_CORRECTION_VALID)
    try:
        validator.validate(correction_valid)
    except ValidationError as exc:
        fail(f"positive Event correction fixture unexpectedly failed: {exc.message}")
    expect_runtime_conformance_pass(
        "Event correction uses new identity",
        enforce_event_correction_identity,
        correction_valid,
    )
    try:
        validator.validate(load_json(RUNTIME_EVENT_INVALID_CORRECTION))
    except ValidationError:
        pass
    else:
        fail("Event correction without correction_reason unexpectedly passed")

    correction = load_json(RUNTIME_EVENT_INVALID_SAME_CORRECTION)
    try:
        validator.validate(correction)
    except ValidationError as exc:
        fail(f"same-id Event correction fixture must be structurally valid: {exc.message}")
    expect_runtime_conformance_reject(
        "same-id Event correction fixture",
        enforce_event_correction_identity,
        correction,
    )
    expect_runtime_conformance_pass(
        "ordinary Event without correction relation",
        enforce_event_correction_identity,
        load_json(RUNTIME_EVENT_VALID),
    )

    redelivery = [load_json(path) for path in RUNTIME_EVENT_REDELIVERY]
    for data in redelivery:
        try:
            validator.validate(data)
        except ValidationError as exc:
            fail(f"Event redelivery fixture unexpectedly failed: {exc.message}")
    if redelivery[0]["event_id"] != redelivery[1]["event_id"]:
        fail("same logical Event redelivery must preserve event_id in fixture")


def validate_retry_provenance_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validator = validator_for(RUNTIME_RETRY_SCHEMA, docs, resource_registry)
    attempt_validator = validator_for(
        RUNTIME_EXECUTION_ATTEMPT_SCHEMA,
        docs,
        resource_registry,
    )
    for valid_path in RUNTIME_RETRY_VALIDS:
        valid = load_json(valid_path)
        try:
            validator.validate(valid)
        except ValidationError as exc:
            fail(f"positive retry provenance fixture unexpectedly failed: {valid_path.name}: {exc.message}")
        expect_runtime_conformance_pass(
            f"positive retry identity separation {valid_path.name}",
            enforce_retry_identity_separation,
            valid,
        )
    for invalid_path in RUNTIME_RETRY_INVALIDS:
        try:
            validator.validate(load_json(invalid_path))
        except ValidationError:
            continue
        fail(f"negative retry provenance fixture unexpectedly passed: {invalid_path.name}")

    reused = load_json(RUNTIME_RETRY_INVALID_SAME_REF)
    try:
        validator.validate(reused)
    except ValidationError as exc:
        fail(f"retry reused-identity fixture must be structurally valid before semantic validation: {exc.message}")
    expect_runtime_conformance_reject(
        "retry reused-identity fixture",
        enforce_retry_identity_separation,
        reused,
    )

    chain = load_json(RUNTIME_RETRY_CHAIN_VALID)
    predecessor = chain["predecessor_attempt"]
    retry = chain["retry_provenance"]
    successor = chain["successor_attempt"]
    for label, attempt in (
        ("retry-chain predecessor", predecessor),
        ("retry-chain successor", successor),
    ):
        try:
            attempt_validator.validate(attempt)
        except ValidationError as exc:
            fail(f"{label} execution attempt unexpectedly failed: {exc.message}")
    try:
        validator.validate(retry)
    except ValidationError as exc:
        fail(f"retry-chain provenance unexpectedly failed: {exc.message}")
    if predecessor["execution_state"] != "FAILED":
        fail("retry-chain predecessor must be a terminal FAILED execution attempt")
    if predecessor.get("failure_ref") != retry.get("trigger_ref"):
        fail("retry-chain trigger_ref must anchor to predecessor failure_ref")
    if predecessor["subject_ref"] != retry["predecessor_ref"]:
        fail("retry-chain predecessor_ref must match failed predecessor subject_ref")
    if successor["execution_state"] != "CREATED":
        fail("retry-chain successor must start as CREATED")
    if successor["subject_ref"] != retry["successor_ref"]:
        fail("retry-chain successor_ref must match CREATED successor subject_ref")
    expect_runtime_conformance_pass(
        "retry-chain successor/predecessor identity separation",
        enforce_retry_identity_separation,
        retry,
    )


def validate_execution_attempt_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validator = validator_for(RUNTIME_EXECUTION_ATTEMPT_SCHEMA, docs, resource_registry)
    for valid_path in RUNTIME_EXECUTION_ATTEMPT_VALIDS:
        try:
            validator.validate(load_json(valid_path))
        except ValidationError as exc:
            fail(
                f"positive execution-attempt fixture unexpectedly failed "
                f"for {valid_path.name}: {exc.message}"
            )
    for invalid_path in RUNTIME_EXECUTION_ATTEMPT_INVALIDS:
        try:
            validator.validate(load_json(invalid_path))
        except ValidationError:
            continue
        fail(f"negative execution-attempt fixture unexpectedly passed: {invalid_path.name}")


def validate_routing_runtime_semantics(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    schema_path = SCHEMAS / "04" / "workflow" / "routing-runtime.schema.json"
    validator = validator_for(schema_path, docs, resource_registry)
    data = load_json(RUNTIME_ROUTING_INVALID_SAME_KEY)
    try:
        validator.validate(data)
    except ValidationError as exc:
        fail(
            "routing same-key fixture must be structurally valid before semantic "
            f"validation, but failed schema validation: {exc.message}"
        )
    expect_runtime_conformance_reject(
        "routing request-key/result collision fixture",
        enforce_routing_request_result_separation,
        data,
    )
    expect_runtime_conformance_reject(
        "routing request-key/runtime-owner-result collision fixture",
        enforce_operation_request_key_separation,
        data,
    )


def enforce_adapter_failure_request_correlation(data: dict[str, Any]) -> None:
    """A material Adapter Failure must retain its originating request correlation."""
    request = data.get("request")
    failure = data.get("adapter_failure")
    if not isinstance(request, dict) or not isinstance(failure, dict):
        return
    control = request.get("operation_control")
    if not isinstance(control, dict):
        return
    request_key = control.get("operation_request_key")
    failure_key = failure.get("operation_request_key")
    if request_key is None or failure_key is None:
        return
    if request_key != failure_key:
        raise RuntimeConformanceViolation(
            "adapter_failure.operation_request_key must equal "
            "request.operation_control.operation_request_key"
        )


def enforce_resolution_result_separation(data: dict[str, Any]) -> None:
    """A failed Adapter Resolution must not carry a Resolved Adapter View identity."""
    if "adapter_failure" not in data and "failure_code" not in data:
        return
    if "adapter_resolution_id" in json.dumps(data):
        raise RuntimeConformanceViolation(
            "adapter_resolution_id must not appear on a failed Adapter Resolution; "
            "it identifies an immutable Resolved Adapter View only"
        )


def enforce_fallback_not_retry(value: Any, *, path: str = "$") -> None:
    """Fallback is UPOS-11 binding selection and must not borrow UPOS-04 retry semantics."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"relation", "retry_provenance", "successor_ref", "predecessor_ref"}:
                raise RuntimeConformanceViolation(
                    f"UPOS-04 retry provenance must not represent UPOS-11 fallback: {path}.{key}"
                )
            enforce_fallback_not_retry(child, path=f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            enforce_fallback_not_retry(child, path=f"{path}[{index}]")


def enforce_no_provider_execution(value: Any, *, path: str = "$") -> None:
    """Slice 2 stops at representation; provider execution belongs to Phase 6."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key in PROVIDER_EXECUTION_FIELDS:
                raise RuntimeConformanceViolation(
                    f"provider execution field is forbidden in Slice-2 representation: {path}.{key}"
                )
            enforce_no_provider_execution(child, path=f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            enforce_no_provider_execution(child, path=f"{path}[{index}]")


def validate_registry_file_parity(schema_ids: dict[str, Path]) -> None:
    """Bidirectional registry/file parity: neither side may carry an entry the other lacks."""
    registry = load_json(REGISTRY)
    declared = {entry["artifact_path"] for entry in registry["entries"]}
    discovered = {
        str(path.relative_to(ROOT)) for path in sorted(SCHEMAS.rglob("*.schema.json"))
    }
    unregistered = sorted(discovered - declared)
    if unregistered:
        fail(f"schema files are not registered in the Schema Registry: {unregistered}")
    missing = sorted(declared - discovered)
    if missing:
        fail(f"registry entries have no schema file on disk: {missing}")
    print(
        f"Registry/file parity: PASS ({len(declared)} registered, {len(discovered)} discovered)"
    )


def validate_adapter_resolution_contracts(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    validators = {
        key: validator_for(path, docs, resource_registry)
        for key, path in ADAPTER_SCHEMA_PATHS.items()
    }

    # Positive evidence is read from stored fixture content, never manufactured.
    for name, key in ADAPTER_POSITIVE_FIXTURES:
        stored = load_json(ADAPTER_FIXTURES / name)
        for field in ("runtime_contract_ref", "runtime_contract_version", "runtime_schema_version"):
            if field not in stored:
                fail(f"stored Slice-2 fixture {name} is missing required version carriage: {field}")
        problem = resolve_runtime_contract_reference(
            "runtime_contract_ref",
            stored["runtime_contract_ref"],
            stored["runtime_contract_version"],
        )
        if problem is not None:
            fail(f"stored Slice-2 fixture {name}: {problem}")
        try:
            validators[key].validate(stored)
        except ValidationError as exc:
            fail(f"positive Slice-2 fixture unexpectedly failed: {name}: {exc.message}")
    print(f"FOCUSED PASS: {len(ADAPTER_POSITIVE_FIXTURES)} stored Slice-2 positive fixtures")

    for name in ADAPTER_COMPOSITE_FIXTURES:
        data = load_json(ADAPTER_FIXTURES / name)
        if data.get("fixture_level") != "FIXTURE":
            fail(f"Slice-2 composite fixture must be labeled FIXTURE: {name}")
        for member, key in ADAPTER_COMPOSITE_KEYS.items():
            if member not in data:
                continue
            try:
                validators[key].validate(data[member])
            except ValidationError as exc:
                fail(f"Slice-2 composite member {name}:{member} failed: {exc.message}")
        expect_runtime_conformance_pass(
            f"Slice-2 composite fallback/retry separation {name}",
            enforce_fallback_not_retry,
            data,
        )
        expect_runtime_conformance_pass(
            f"Slice-2 composite provider-execution exclusion {name}",
            enforce_no_provider_execution,
            data,
        )
        expect_runtime_conformance_pass(
            f"Slice-2 composite request/result separation {name}",
            enforce_resolution_result_separation,
            data,
        )
        expect_runtime_conformance_pass(
            f"Slice-2 composite failure/request correlation {name}",
            enforce_adapter_failure_request_correlation,
            data,
        )

    mismatch = load_json(ADAPTER_FIXTURES / ADAPTER_COMPOSITE_REQUEST_KEY_MISMATCH)
    for member, key in (("request", "request"), ("adapter_failure", "failure")):
        try:
            validators[key].validate(mismatch[member])
        except ValidationError as exc:
            fail(
                f"Slice-2 request/failure mismatch fixture must be structurally valid "
                f"before correlation validation: {member}: {exc.message}"
            )
    expect_runtime_conformance_reject(
        "Slice-2 failed-resolution request/failure correlation mismatch",
        enforce_adapter_failure_request_correlation,
        mismatch,
    )

    event_validator = validator_for(RUNTIME_EVENT_SCHEMA, docs, resource_registry)
    for name in ADAPTER_EVENT_FIXTURES:
        data = load_json(ADAPTER_FIXTURES / name)
        if data.get("domain_owner_module") != "UPOS-11":
            fail(f"Slice-2 Event fixture must declare UPOS-11 domain ownership: {name}")
        try:
            event_validator.validate(data)
        except ValidationError as exc:
            fail(f"Slice-2 Event fixture unexpectedly failed on the STABLE schema: {name}: {exc.message}")
    print(f"FOCUSED PASS: {len(ADAPTER_EVENT_FIXTURES)} Slice-2 Event fixtures on the unchanged STABLE Event schema")

    # Negative evidence: each fixture must reject once, at the intended keyword.
    for name, key, expected_validator, needle in ADAPTER_NEGATIVE_FIXTURES:
        errors = list(validators[key].iter_errors(load_json(ADAPTER_FIXTURES / name)))
        if len(errors) != 1:
            fail(
                f"Slice-2 negative fixture must reject for exactly one invariant: "
                f"{name}; got {len(errors)} errors"
            )
        exc = errors[0]
        if exc.validator != expected_validator:
            fail(
                f"Slice-2 negative fixture {name} rejected by {exc.validator!r}, "
                f"expected {expected_validator!r}: {exc.message}"
            )
        if needle not in exc.message:
            fail(
                f"Slice-2 negative fixture {name} did not name {needle!r}: {exc.message}"
            )
        print(f"FOCUSED REJECT: {name} [{exc.validator}]")

    # Fail-closed contract resolution, exercised through the enforcing path.
    view = load_json(ADAPTER_FIXTURES / "resolved-adapter-view.valid.json")
    for label, ref, version in (
        ("unknown contract ref", "UPOS-11-DOES-NOT-EXIST", "0.1.0"),
        ("unsupported contract version", view["runtime_contract_ref"], "99.0.0"),
    ):
        if resolve_runtime_contract_reference("runtime_contract_ref", ref, version) is None:
            fail(f"Slice-2 contract resolution accepted {label}: {ref}@{version}")
        print(f"FOCUSED REJECT: Slice-2 {label}")
    if resolve_runtime_contract_reference(
        "runtime_contract_ref", view["runtime_contract_ref"], view["runtime_contract_version"]
    ) is not None:
        fail("Slice-2 stored contract reference unexpectedly failed to resolve")
    print("FOCUSED PASS: Slice-2 stored contract reference resolves")


def validate_fixtures(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    registry_validator = Draft202012Validator(load_json(REGISTRY_SCHEMA))

    try:
        registry_validator.validate(load_json(VALID_FIXTURE))
    except ValidationError as exc:
        fail(f"positive registry fixture unexpectedly failed: {exc.message}")

    try:
        registry_validator.validate(load_json(INVALID_FIXTURE))
    except ValidationError:
        pass
    else:
        fail("negative registry fixture unexpectedly passed")

    for schema_path, valid_path, invalid_path in DOCUMENTATION_SIMPLE_FIXTURES:
        validate_pair(
            schema_path,
            valid_path,
            invalid_path,
            docs,
            resource_registry,
        )

    validate_sot_registry_fixtures(docs, resource_registry)
    validate_project_adapter_fixtures(docs, resource_registry)
    validate_identity_reference_fixtures(docs, resource_registry)
    validate_pair(
        CROSS_MODULE_REFERENCE_SCHEMA,
        CROSS_MODULE_REFERENCE_VALID,
        CROSS_MODULE_REFERENCE_INVALID,
        docs,
        resource_registry,
    )

    for schema_path, valid_path, invalid_path in RUNTIME_COMMON_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)
    validate_failure_envelope_version_carriage(docs, resource_registry)
    validate_owner_result_runtime_boundaries(docs, resource_registry)
    validate_operation_request_key_boundaries(docs, resource_registry)
    validate_execution_spine_reconstructability(docs, resource_registry)

    for schema_path, valid_path, invalid_path in RUNTIME_ATTRIBUTION_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)

    for schema_path, valid_path, invalid_path in RUNTIME_TASK_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)

    for schema_path, valid_path, invalid_path in RUNTIME_ROUTING_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)
    validate_routing_runtime_semantics(docs, resource_registry)

    for schema_path, valid_path, invalid_path in RUNTIME_WORKFLOW_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path, docs, resource_registry)
    validate_execution_attempt_fixtures(docs, resource_registry)
    validate_retry_provenance_fixtures(docs, resource_registry)
    validate_runtime_event_fixtures(docs, resource_registry)
    validate_adapter_resolution_contracts(docs, resource_registry)


def main() -> int:
    schema_ids, docs = load_schema_documents()
    resource_registry = build_resource_registry(docs)
    validate_registry(schema_ids)
    validate_registry_file_parity(schema_ids)
    validate_runtime_contract_references()
    validate_durable_runtime_version_carriage(docs, resource_registry)
    validate_forbidden_identity_properties(docs)
    validate_artist_os_identity_namespace()
    validate_fixtures(docs, resource_registry)

    print("U-POS schema validation: PASS")
    print("Dialect: JSON Schema Draft 2020-12")
    print("Registry: schemas/registry/schema-registry.json")
    print(f"Schema documents: {len(schema_ids)}")
    print("Documentation Authority fixtures: PASS")
    print("Project Manifest / Adapter fixtures: PASS")
    print("Project Adapter direct branch fixtures: PASS")
    print("Artist OS Phase 2C dogfooding: PASS")
    print("Cross-module identity/reference fixtures: PASS")
    print("Canonical cross-schema reference conformance: PASS")
    print("Runtime contract reference/version resolution: PASS")
    print("Durable runtime version carriage/fail-closed validation: PASS")
    print("Identity anti-duplication validation: PASS")
    print("Artist OS namespace compatibility: PASS")
    print("Phase-3 common runtime primitive fixtures: PASS")
    print("Runtime failure envelope version carriage: PASS")
    print("Owner-result/runtime-outcome separation: PASS")
    print("Operation request key / owner result separation: PASS")
    print("Phase-3 execution-spine reconstructability: PASS")
    print("Phase-3 attribution fixtures: PASS")
    print("Phase-3 Task runtime fixtures: PASS")
    print("Phase-3 Routing runtime fixtures: PASS")
    print("Phase-3 Workflow runtime fixtures: PASS")
    print("Phase-3 Execution Attempt fixtures: PASS")
    print("Phase-3 Retry provenance fixtures: PASS")
    print("Phase-3 Event fixtures: PASS")
    print("Phase-3 Slice-2 Adapter Resolution contracts: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
