#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY_SCHEMA = SCHEMAS / "meta" / "schema-registry.schema.json"
REGISTRY = SCHEMAS / "registry" / "schema-registry.json"
VALID_FIXTURE = SCHEMAS / "fixtures" / "registry.valid.json"
INVALID_FIXTURE = SCHEMAS / "fixtures" / "registry.invalid.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_schema_documents() -> None:
    schema_files = sorted(SCHEMAS.rglob("*.schema.json"))
    if not schema_files:
        fail("no JSON Schema documents found")

    for path in schema_files:
        schema = load_json(path)
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(f"{path.relative_to(ROOT)} does not pin JSON Schema Draft 2020-12")
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            fail(f"invalid JSON Schema {path.relative_to(ROOT)}: {exc.message}")


def validate_registry() -> None:
    schema = load_json(REGISTRY_SCHEMA)
    validator = Draft202012Validator(schema)
    registry = load_json(REGISTRY)

    try:
        validator.validate(registry)
    except ValidationError as exc:
        location = "/".join(str(x) for x in exc.absolute_path) or "<root>"
        fail(f"registry validation failed at {location}: {exc.message}")

    seen = set()
    for entry in registry["entries"]:
        key = (entry["schema_key"], entry["schema_version"])
        if key in seen:
            fail(f"duplicate registry key/version: {key[0]}@{key[1]}")
        seen.add(key)

        artifact = ROOT / entry["artifact_path"]
        if not artifact.is_file():
            fail(f"registered schema artifact missing: {entry['artifact_path']}")

        for ref in entry["normative_source_refs"]:
            source = ROOT / ref
            if not source.is_file():
                fail(f"normative source ref missing for {entry['schema_key']}: {ref}")

        deps = set(entry["reference_dependencies"])
        if entry["schema_key"] in deps:
            fail(f"schema cannot depend on itself: {entry['schema_key']}")


def validate_fixtures() -> None:
    schema = load_json(REGISTRY_SCHEMA)
    validator = Draft202012Validator(schema)

    try:
        validator.validate(load_json(VALID_FIXTURE))
    except ValidationError as exc:
        fail(f"positive fixture unexpectedly failed: {exc.message}")

    try:
        validator.validate(load_json(INVALID_FIXTURE))
    except ValidationError:
        pass
    else:
        fail("negative fixture unexpectedly passed")


def main() -> int:
    validate_schema_documents()
    validate_registry()
    validate_fixtures()
    print("U-POS schema validation: PASS")
    print("Dialect: JSON Schema Draft 2020-12")
    print("Registry: schemas/registry/schema-registry.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
