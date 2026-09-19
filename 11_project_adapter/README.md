# UPOS-011 Project Adapter

**ID:** UPOS-11-README-001  
**Type:** MODULE ENTRY POINT  
**Status:** ACTIVE  
**Normativity:** NORMATIVE  
**Owner:** UPOS-011 Project Adapter  
**Version:** 1.0.0  
**Lifetime:** STABLE  
**Created:** 2026-09-20  
**Last reviewed:** 2026-09-20  
**Related:** —


## Purpose

UPOS-011 is the anti-corruption/binding layer between universal U-POS semantics and a concrete project/provider/runtime.

```text
U-POS universal semantics
+ Project Adapter
+ Project Manifest
+ Project Knowledge
= configured U-POS for one project
```

## Canonical boundary

```text
UPOS-011 OWNS:
BINDING
RESOLUTION
VALIDATION
ADAPTER CONTRACTS

UPOS-011 DOES NOT OWN:
DOMAIN SEMANTICS
```

Changing project or provider SHOULD primarily change Project Adapter bindings, not Modules 01–10.

## Current release state

```text
UPOS-011 INTERNAL IMPLEMENTATION = COMPLETE
UPOS-011 INTERFACE STATUS = INTERFACE_STABLE

UPOS-008 reconciliation = COMPLETE
UPOS-009 reconciliation = COMPLETE
UPOS-010 reconciliation = COMPLETE

GLOBAL 008–011 semantic convergence = COMPLETE
UPOS-011 FREEZE = FROZEN v1.0
```

The coordinated UPOS-008–011 reconciliation and same-baseline validation are complete. Further semantic change requires a new reviewed version.

## Interpretation rule

This Single-File package is a transport bundle. Each embedded virtual file remains logically independent.

`analysis/` is point-in-time implementation/reconciliation evidence. Normative authority remains with ACTIVE/NORMATIVE artifacts.

`MODULE_11_TRACEABILITY.md` is the active Module-11 source-coverage artifact.
