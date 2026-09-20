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

BINDING_SCHEMA = SCHEMAS / "11" / "project-adapter" / "binding.schema.json"
PROJECT_MANIFEST_SCHEMA = SCHEMAS / "11" / "project-adapter" / "project-manifest.schema.json"
PROJECT_ADAPTER_SCHEMA = SCHEMAS / "11" / "project-adapter" / "project-adapter.schema.json"

PROJECT_ADAPTER_SIMPLE_FIXTURES = [
    (
        BINDING_SCHEMA,
        SCHEMAS / "fixtures" / "project-adapter" / "binding.valid.json",
        SCHEMAS / "fixtures" / "project-adapter" / "binding.invalid.json",
    ),
    (
        PROJECT_MANIFEST_SCHEMA,
        SCHEMAS / "fixtures" / "project-adapter" / "project-manifest.valid.json",
        SCHEMAS / "fixtures" / "project-adapter" / "project-manifest.invalid.json",
    ),
    (
        PROJECT_ADAPTER_SCHEMA,
        SCHEMAS / "fixtures" / "project-adapter" / "project-adapter.valid.json",
        SCHEMAS / "fixtures" / "project-adapter" / "project-adapter.invalid.json",
    ),
]

PROJECT_ADAPTER_VALID = SCHEMAS / "fixtures" / "project-adapter" / "project-adapter.valid.json"
PROJECT_ADAPTER_INVALID_MISMATCH = SCHEMAS / "fixtures" / "project-adapter" / "project-adapter.invalid-project-mismatch.json"
PROJECT_MANIFEST_VALID = SCHEMAS / "fixtures" / "project-adapter" / "project-manifest.valid.json"

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

        for dep in entry["reference_dependencies"]:
            if dep == entry["schema_key"]:
                fail(f"schema cannot depend on itself: {entry['schema_key']}")
            if dep not in keys:
                fail(f"unresolved registry dependency for {entry['schema_key']}: {dep}")


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



def validate_project_adapter_cross_object(
    docs: dict[str, dict[str, Any]],
    resource_registry: Registry,
) -> None:
    manifest_validator = validator_for(PROJECT_MANIFEST_SCHEMA, docs, resource_registry)
    adapter_validator = validator_for(PROJECT_ADAPTER_SCHEMA, docs, resource_registry)

    manifest = load_json(PROJECT_MANIFEST_VALID)
    adapter = load_json(PROJECT_ADAPTER_VALID)

    manifest_validator.validate(manifest)
    adapter_validator.validate(adapter)

    errors: list[str] = []
    if adapter["project_id"] != adapter["manifest_ref"]["project_id"]:
        errors.append("adapter project_id != adapter manifest_ref.project_id")
    if adapter["project_id"] != manifest["project"]["project_id"]:
        errors.append("adapter project_id != manifest project.project_id")
    if adapter["project_adapter_version"] != manifest["project_adapter_version"]:
        errors.append("adapter project_adapter_version != manifest project_adapter_version")
    if adapter["manifest_ref"]["manifest_version"] != manifest["manifest_version"]:
        errors.append("adapter manifest_ref.manifest_version != manifest manifest_version")
    if errors:
        fail("Project Adapter/Manifest composite identity validation failed: " + "; ".join(errors))

    mismatch = load_json(PROJECT_ADAPTER_INVALID_MISMATCH)
    adapter_validator.validate(mismatch)
    mismatch_errors = []
    if mismatch["project_id"] != mismatch["manifest_ref"]["project_id"]:
        mismatch_errors.append("adapter project_id != adapter manifest_ref.project_id")
    if not mismatch_errors:
        fail("negative Project Adapter project mismatch fixture unexpectedly passed")

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

    for schema_path, valid_path, invalid_path in PROJECT_ADAPTER_SIMPLE_FIXTURES:
        validate_pair(
            schema_path,
            valid_path,
            invalid_path,
            docs,
            resource_registry,
        )

    validate_project_adapter_cross_object(docs, resource_registry)


def main() -> int:
    schema_ids, docs = load_schema_documents()
    resource_registry = build_resource_registry(docs)
    validate_registry(schema_ids)
    validate_fixtures(docs, resource_registry)

    print("U-POS schema validation: PASS")
    print("Dialect: JSON Schema Draft 2020-12")
    print("Registry: schemas/registry/schema-registry.json")
    print(f"Schema documents: {len(schema_ids)}")
    print("Documentation Authority fixtures: PASS")
    print("Project Manifest / Adapter fixtures: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
