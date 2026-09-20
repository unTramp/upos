# Artist OS — Phase 2B Dogfooding Instance

**Purpose:** validate U-POS Documentation Authority schemas against a real AI-native project.  
**Target project:** `unTramp/artistos`  
**Audited adoption branch:** `feat/upos-adoption`  
**Branch head inspected:** `d8f5a4295952ec9f462649c366e451e7188fefd8`  
**Audit baseline recorded by Artist OS:** `main@94ff0e0219bd441b02044f419528b7243b9b318f`  
**U-POS baseline:** `v1.0.0`

## Evidence sources

The instance below is derived from Artist OS repository evidence, especially:

- `.upos/SOURCE_OF_TRUTH_MAP.md`
- `.upos/audit/DOCUMENT_INVENTORY.md`
- `.upos/audit/CONFLICT_REGISTER.md`
- `.upos/PROJECT_ADAPTER.md`
- current document headers in the audited branch

No Artist OS product semantics are promoted into universal U-POS semantics.

## Mapping rule

Artist OS audit labels such as:

~~~text
CANONICAL
NORMATIVE_COMPANION
TEMPORARY PLAN
HISTORICAL EVIDENCE
~~~

are intentionally NOT added as new U-POS `normativity` enum values.

They are decomposed across existing UPOS-01 axes:

~~~text
canonicality        → Source-of-Truth Registry scope/owner/source
current lifecycle   → status
normative weight    → normativity
time horizon        → lifetime
document function   → type
~~~

Examples:

~~~text
MASTER v1.4
→ type MASTER
→ status ACTIVE
→ normativity NORMATIVE
→ lifetime STABLE
→ canonical via Source-of-Truth registry

MASTER v1.3
→ type MASTER
→ status SUPERSEDED
→ normativity INFORMATIVE
→ lifetime HISTORICAL

AR-001…AR-062 companion file
→ type CONTRACT
→ status ACTIVE
→ normativity NORMATIVE
→ lifetime STABLE
→ scoped companion authority

UI redesign implementation plan
→ type PLAN
→ status ACTIVE
→ normativity INFORMATIVE
→ lifetime TEMPORARY

completion reports
→ type REPORT
→ status ACTIVE
→ normativity EVIDENCE
→ lifetime HISTORICAL
~~~

This decomposition is the dogfooding result: no new universal enum was required.

## Known active metadata conflicts

Artist OS audit records:

- stale v1.3 self-header claiming Current Master Source of Truth;
- stale AR file header claiming PROPOSED/v1.3 authoritative;
- freeze decision header still saying READY FOR HUMAN MERGE although merge condition is fulfilled.

The dogfooding instance expresses current authority through the registry overlay without rewriting historical source text.

## Conflict behavior

The `product.domain_model` scope intentionally has two ACTIVE NORMATIVE sources under the same owner:

- MASTER v1.4;
- AR companion contracts.

This is allowed because UPOS-01 permits ACTIVE normative source(s), plural.

The validator emits a review warning but does not invent an SOT-C4 conflict unless the underlying claims actually disagree.
