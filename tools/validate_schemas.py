#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY_SCHEMA = SCHEMAS / "meta" / "schema-registry.schema.json"
REGISTRY = SCHEMAS / "registry" / "schema-registry.json"
VALID_FIXTURE = SCHEMAS / "fixtures" / "registry.valid.json"
INVALID_FIXTURE = SCHEMAS / "fixtures" / "registry.invalid.json"

DOCUMENTATION_FIXTURES = [
    (
        SCHEMAS / "01" / "documentation" / "document-manifest.schema.json",
        SCHEMAS / "fixtures" / "documentation" / "document-manifest.valid.json",
        SCHEMAS / "fixtures" / "documentation" / "document-manifest.invalid.json",
    ),
    (
        SCHEMAS / "01" / "documentation" / "source-of-truth-entry.schema.json",
        SCHEMAS / "fixtures" / "documentation" / "source-of-truth-entry.valid.json",
        SCHEMAS / "fixtures" / "documentation" / "source-of-truth-entry.invalid.json",
    ),
]

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


def validate_schema_documents() -> dict[str, Path]:
    schema_files = sorted(SCHEMAS.rglob("*.schema.json"))
    if not schema_files:
        fail("no JSON Schema documents found")

    ids: dict[str, Path] = {}
    loaded: list[tuple[Path, dict[str, Any]]] = []

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
        loaded.append((path, schema))

    for path, schema in loaded:
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

    return ids


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


def validate_pair(schema_path: Path, valid_path: Path, invalid_path: Path) -> None:
    validator = Draft202012Validator(
        load_json(schema_path),
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )

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
        fail(
            f"negative fixture unexpectedly passed for {schema_path.relative_to(ROOT)}"
        )


def validate_fixtures() -> None:
    validator = Draft202012Validator(load_json(REGISTRY_SCHEMA))

    try:
        validator.validate(load_json(VALID_FIXTURE))
    except ValidationError as exc:
        fail(f"positive registry fixture unexpectedly failed: {exc.message}")

    try:
        validator.validate(load_json(INVALID_FIXTURE))
    except ValidationError:
        pass
    else:
        fail("negative registry fixture unexpectedly passed")

    for schema_path, valid_path, invalid_path in DOCUMENTATION_FIXTURES:
        validate_pair(schema_path, valid_path, invalid_path)


def main() -> int:
    schema_ids = validate_schema_documents()
    validate_registry(schema_ids)
    validate_fixtures()
    print("U-POS schema validation: PASS")
    print("Dialect: JSON Schema Draft 2020-12")
    print("Registry: schemas/registry/schema-registry.json")
    print(f"Schema documents: {len(schema_ids)}")
    print(f"Domain fixture pairs: {len(DOCUMENTATION_FIXTURES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
