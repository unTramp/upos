# Quality Bindings

**ID:** UPOS-11-QB-001  
**Type:** QUALITY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-007 Quality System


## Purpose

Bind abstract Quality evidence/check requirements to concrete project tools and artifacts.

Examples:

```text
unit test evidence → command binding
static analysis evidence → analyzer binding
browser validation → test provider
coverage evidence → coverage artifact adapter
visual evidence → screenshot/comparison provider
```

## Project-specific threshold

A value such as a coverage threshold MAY appear in a binding only when backed by:

```text
canonical_policy_ref
canonical_policy_version/revision
```

UPOS-011 never invents the threshold.

## Result normalization

Provider-native test/check results MAY be normalized into UPOS-006/007-consumable refs while preserving raw provider result provenance.

```text
provider result != Quality Verdict
```
