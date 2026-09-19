# Binding Resolution Standard

**ID:** UPOS-11-BRS-001  
**Type:** RESOLUTION STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Resolution flow

```text
abstract requirement
→ determine project/repository/environment/operation scope
→ collect matching ACTIVE bindings
→ evaluate applicability
→ apply deterministic precedence
→ check compatibility
→ discover provider capability
→ evaluate required external security decision refs where applicable
→ validate concrete target
→ produce Resolved Binding
```

## Precedence

From broadest to narrowest:

```text
organization default
< project
< repository
< environment
< operation
< execution-scoped override
```

More specific scope wins only where both bindings are semantically compatible and the override is permitted.

Equal-specificity incompatible matches:

```text
→ BINDING_AMBIGUOUS / BINDING_CONFLICT
```

No implicit “last configuration wins”.

## Fallback

Fallback is allowed only when an explicit fallback chain exists and upstream policy permits equivalence.

Protected actions MUST NOT silently fall back.

Fallback attribution records:

```text
requested_binding_ref
resolved_binding_ref
fallback_reason
actual_provider_adapter_ref/version
```

## Result

A successful resolution produces an immutable item in the Resolved Adapter View.

Resolution does not make the concrete provider/project state canonical domain truth.
