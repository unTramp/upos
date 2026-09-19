# Project Adapter Lifecycle and Versioning

**ID:** UPOS-11-LCV-001  
**Type:** LIFECYCLE / VERSIONING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Project Adapter version

Material semantic mapping/configuration changes increment `project_adapter_version`.

## Manifest version

Project Manifest identity is:

```text
project_id + manifest_version
```

Material manifest binding changes create a new version.

## Binding lifecycle

```text
DRAFT
ACTIVE
DEPRECATED
RETIRED
SUPERSEDED
```

## Historical reconstruction

An execution should remain attributable to the effective manifest/adapter/provider-adapter versions used.

Historical results are not rewritten when a newer adapter version becomes active.

## Provider adapter lifecycle

Provider Adapter versions may be upgraded independently if interface compatibility remains valid.

No silent material provider-adapter upgrade is allowed.

## Migration

Binding/provider format migration must preserve:

```text
old binding ref/version
migration relation
new binding ref/version
```

and support historical interpretation.
