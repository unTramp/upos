# Schema URI & Reference Conventions

**ID:** UPOS-SCHEMA-URIREF-001  
**Phase:** 2A  
**Status:** CANDIDATE  
**Baseline:** U-POS v1.0.0  
**Last reviewed:** 2026-09-20

## 1. Purpose

Define stable machine identities for schema documents and cross-schema references without coupling U-POS semantics to GitHub paths, branches, or local filesystem layout.

## 2. Canonical schema identity

Every U-POS JSON Schema document MUST have a JSON Schema Draft 2020-12 declaration and a canonical absolute U-POS schema URI.

~~~text
$schema = https://json-schema.org/draft/2020-12/schema
$id     = urn:upos:schema:<owner-namespace>:<schema-name>:<schema-version>
~~~

Examples:

~~~text
urn:upos:schema:common:schema-registry:0.1.0
urn:upos:schema:01:documentation:source-of-truth-entry:0.1.0
urn:upos:schema:04:workflow:task:0.1.0
urn:upos:schema:11:project-adapter:project-manifest:0.1.0
~~~

The URI identifies the serialization contract, not a U-POS domain object.

## 3. Owner namespace mapping

~~~text
upos.common.*                 ↔ urn:upos:schema:common:...
upos.01.documentation.*       ↔ urn:upos:schema:01:documentation:...
upos.02.agent_organization.*  ↔ urn:upos:schema:02:agent-organization:...
upos.03.skills.*              ↔ urn:upos:schema:03:skills:...
upos.04.workflow.*            ↔ urn:upos:schema:04:workflow:...
upos.05.context_memory.*      ↔ urn:upos:schema:05:context-memory:...
upos.06.engineering.*         ↔ urn:upos:schema:06:engineering:...
upos.07.quality.*             ↔ urn:upos:schema:07:quality:...
upos.08.observability.*       ↔ urn:upos:schema:08:observability:...
upos.09.learning.*            ↔ urn:upos:schema:09:learning:...
upos.10.security.*            ↔ urn:upos:schema:10:security:...
upos.11.project_adapter.*     ↔ urn:upos:schema:11:project-adapter:...
~~~

These are schema namespaces only. They do not change semantic ownership defined by U-POS modules.

## 4. Cross-schema references

Cross-file references MUST use the exact canonical schema URI. Local references inside the same schema MAY use a local fragment such as #/$defs/....

A fragment MAY target a definition inside a canonical schema URI.

## 5. Prohibited stable reference forms

Stable U-POS schemas MUST NOT use cross-schema references based on GitHub branch URLs, mutable main/HEAD URLs, absolute filesystem paths, developer-machine paths, or unversioned remote URLs.

Relative cross-file references are also prohibited for stable contracts.

## 6. Offline resolution

Canonical URNs MUST resolve through the local Schema Registry / validator mapping. Runtime validation MUST NOT require network access to GitHub.

## 7. Version binding

A cross-schema reference names an exact schema version. A compatibility resolver MAY substitute only after explicit compatibility evaluation. Silent substitution is forbidden.

## 8. Artifact path vs identity

~~~text
artifact_path != schema identity
~~~

Moving a file without changing its serialization contract does not by itself require a new schema URI.

## 9. Registry consistency

For every registered schema:

~~~text
registry.schema_uri = artifact.$id
~~~

The validator MUST reject mismatch, duplicate schema URI, unresolved canonical references, or unsupported external reference forms.
