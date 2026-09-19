# Universal Project Operating System (U-POS)

U-POS is a governed, provider-neutral operating system for AI-assisted product and software engineering.

This repository contains the **U-POS v1 modular architecture baseline**. The architecture stage is frozen; runtime implementation is intentionally separate and follows the frozen contracts.

## Release state

| Module | Domain | State |
|---|---|---|
| 01 | Documentation System | Stable baseline v1.2 |
| 02 | Agent Organization | FROZEN v1.0 |
| 03 | Skills System | FROZEN v1.0 |
| 04 | Workflow Engine | FROZEN v1.0 |
| 05 | Context & Memory | FROZEN v1.0 |
| 06 | Engineering Governance | FROZEN v1.0 |
| 07 | Quality System | FROZEN v1.0 |
| 08 | Observability | FROZEN v1.0 |
| 09 | Learning System | FROZEN v1.0 |
| 10 | Security & Permissions | FROZEN v1.0 |
| 11 | Project Adapter | FROZEN v1.0 |

## Repository layout

```text
00_system/                  release/freeze metadata and global registries
01_documentation_system/   governed project truth/documentation system
02_agent_organization/     roles, authority, SoD, handoffs, human governance
03_skills_system/          reusable bounded procedures/capabilities
04_workflow_engine/        work classification, routing and orchestration
05_context_memory/         context retrieval/assembly and runtime memory
06_engineering_governance/ Git/change/commit/PR/merge mechanics
07_quality_system/         evidence, findings, assessment, verdicts, readiness
08_observability/          events, traces, metrics, audit/read models
09_learning_system/        evidence-driven governed system improvement
10_security_permissions/   permissions, grants, protected actions, secrets
11_project_adapter/        project/provider/runtime bindings
legacy_sources/            immutable decomposition/design inputs
distributions/             portable Single-File transports
audit/releases/            release/freeze evidence
tools/                     non-semantic repository validation tooling
```

## Frozen-baseline rule

Modules 02–11 are frozen at v1.0. Module 01 remains at its own stable v1.2 lifecycle. Semantic changes require a reviewed new version; they must never be introduced as silent edits to the current baseline.

Run the repository integrity check before accepting changes:

```bash
python3 tools/verify_frozen_baseline.py
```

## Next implementation phase

Development after tag `v1.0.0` starts outside the frozen module directories, beginning with the machine-readable schema/identity/interface layer. Runtime code must consume these contracts rather than redefine them.

Recommended first development branch:

```text
feat/schema-registry-v1
```

## Release evidence

Start with:

1. `00_system/UPOS_V1_FREEZE_MANIFEST.md`
2. `audit/releases/v1.0.0/GLOBAL_SYSTEM_AUDIT.md`
3. `audit/releases/v1.0.0/GLOBAL_INTERFACE_RECONCILIATION.md`
4. `00_system/GLOBAL_OWNERSHIP_MATRIX.md`
5. `00_system/GLOBAL_IDENTITY_REFERENCE_REGISTRY.md`
6. `audit/releases/v1.0.0/FINAL_MECHANICAL_VALIDATION.md`

The original final package ZIP should be attached to the GitHub Release for `v1.0.0`, not committed to Git history.
