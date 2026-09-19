# Observability Bindings

**ID:** UPOS-11-OBB-001  
**Type:** OBSERVABILITY BINDING STANDARD  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** UPOS-008 Observability


## Abstract needs bound by Module 11

```text
project_id resolution
agent_instance_ref/provider runtime binding where configured
Event sink
Event Store
trace exporter/backend
trace propagation carrier
Metric query/backend
projection store
Control Plane datasource/query adapter
provider usage API
pricing source
clock/time source
repository/CI/provider event adapter
queue/capacity signal source
sampling implementation
projection watermark source
security handling enforcement for policy-scoped sensitivity/redaction/access/retention constraints
```

## Boundary

UPOS-008 owns Event, Trace, Span, Metric and projection semantics.

UPOS-011 only selects/configures concrete realizations.

## Metric formula rule

A backend query MUST implement a canonical Metric Definition/version; no dashboard-only hidden formula may become canonical.

## Cost basis

Pricing binding retains:

```text
pricing_source_ref
effective_date/version
currency
provider usage mapping
```

so historical cost can be reproduced.

## Trace compatibility

An OpenTelemetry-compatible adapter MAY be used, but OpenTelemetry is not canonical U-POS ontology.
