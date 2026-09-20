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

PROJECT_ADAPTER_FIXTURES = [
    (
        PROJECT_MANIFEST_SCHEMA,
        SCHEMAS / "fixtures" / "project_adapter" / "project-manifest.valid.json",
        SCHEMAS / "fixtures" / "project_adapter" / "project-manifest.invalid.json",
    ),
]

ARTIST_OS_PROJECT_MANIFEST = SCHEMAS / "dogfooding" / "artist-os" / "project-manifest.json"
ARTIST_OS_PROJECT_ADAPTER = SCHEMAS / "dogfooding" / "artist-os" / "project-adapter.json"

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
    print("Artist OS Phase 2C dogfooding: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
