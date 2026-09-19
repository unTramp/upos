# Provider Adapter Standard

**ID:** UPOS-11-PAS-001  
**Type:** PROVIDER ADAPTER STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** templates/PROVIDER_ADAPTER_TEMPLATE.md


## Provider Adapter contract

```text
provider_adapter_ref
provider_adapter_version

provider_class
provider_identity_ref

supported_capabilities
support_constraints

configuration_contract_ref
authentication_binding_ref

resource_resolution_interface
operation_execution_interface
event_translation_interface
health_interface

error_normalization_interface
raw_provider_error_ref_support

compatibility_requirements
```

## Capability support states

```text
SUPPORTED
PARTIALLY_SUPPORTED
UNSUPPORTED
UNAVAILABLE
UNKNOWN
```

## Hard boundary

```text
provider supports operation
!= subject is permitted to perform operation
```

UPOS-010 remains required for protected permission semantics.

## Provider independence

Replacing one provider adapter with another SHOULD NOT require changing the owning U-POS module semantics.

## Raw provenance

`raw_provider_error_ref_support` declares whether the adapter can retain a safe reference to the provider-native error/event artifact without copying sensitive raw payloads.

Normalization retains the original provider reference/error/event identifier where safe so future audit can distinguish provider-native data from normalized U-POS projections.
