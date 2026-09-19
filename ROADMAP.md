# U-POS Implementation Roadmap

The modular architecture is frozen at repository tag `v1.0.0`. The next work is implementation of the frozen contracts, not creation of additional architecture modules.

## Phase 2 — Schema / Identity / Interface Layer

Target branch: `feat/schema-registry-v1`

Deliverables:

- canonical schema registry;
- stable identity/reference schemas;
- cross-module interface schemas;
- JSON Schema / YAML representations where appropriate;
- schema versioning and compatibility rules;
- conformance validation tooling;
- examples that are explicitly non-normative.

The schema layer MUST encode frozen semantics and MUST NOT invent an independent domain model.

## Phase 3 — Runtime Contracts

- runtime interfaces for Tasks, Workflows, Agent Runs, Skills, Context, Engineering, Quality, Security and Adapter resolution;
- persistence boundaries;
- error/result contracts;
- lifecycle/event emission interfaces.

## Phase 4 — Orchestrator / Execution Runtime

- request intake;
- classification/routing;
- context assembly coordination;
- governed role/skill execution;
- gate/transition handling;
- recovery/escalation.

## Phase 5 — Observability Runtime

- Event Store;
- trace propagation/storage;
- metric derivation;
- audit/provenance projections;
- operational read models.

## Phase 6 — Concrete Provider / Project Adapters

- repository/GitHub adapter;
- filesystem/runtime adapter;
- CI/test adapters;
- model/tool adapters;
- identity/IAM/secret bindings;
- example project manifest.

## Phase 7 — Control Plane

- query/API layer;
- work/task timeline;
- agents/capacity;
- Quality/Reviews/QA;
- governance/security;
- costs;
- audit/provenance;
- learning;
- system health.

Each phase must consume the frozen module contracts and pass ownership/traceability review before the next phase is considered stable.
