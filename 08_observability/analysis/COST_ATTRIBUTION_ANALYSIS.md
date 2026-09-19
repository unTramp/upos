# Cost Attribution Analysis

**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Lifetime:** HISTORICAL

## Decision

UPOS-008 owns usage/cost attribution semantics; UPOS-011 binds provider usage/pricing/clock APIs.

Required provenance:

```text
raw usage
unit
provider binding ref
price basis ref/version/effective date
currency
calculation method
```

No global usage-record ID is required in v1.

## Additional safeguard

Do not aggregate multiple currencies without an explicit FX basis/effective timestamp.

Do not double-count parent and child provider billing scopes.

Historical incurred cost is not silently recomputed at current prices.
