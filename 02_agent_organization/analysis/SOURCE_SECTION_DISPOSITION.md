# Frozen Source Structural Section Disposition

**ID:** UPOS-02-AN-006  
**Type:** ANALYSIS / SOURCE MAPPING  
**Status:** ARCHIVED
**Normativity:** EVIDENCE
**Owner:** UPOS-002 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this historical implementation/audit evidence is found factually incorrect; normative changes belong in canonical Module 02 artifacts.
**Related:** `../MODULE_02_TRACEABILITY.md`

> **Historical evidence notice:** This file records the completed UPOS-002 v1.0 decomposition/implementation state at freeze time. It is not timeless normative truth. Current organizational rules are owned by the canonical Module 02 normative artifacts; `MODULE_02_TRACEABILITY.md` remains the canonical coverage artifact.


## Purpose

Classify **all 317 structural Markdown sections** in the frozen design source, including nested headings.

This is stricter than top-level-only mapping.

Statuses:

```text
EXTRACTED_TO_MODULE_02
MIXED_EXTRACTED_AND_DEFERRED
DEFERRED_TO_MODULE
```

For extracted/mixed rows, the table lists the Module 02 requirement IDs that preserve the organizational semantics.

| Source line | Level | Frozen section | Disposition | Owner / deferred owner | Module 02 requirements |
|---:|---:|---|---|---|---|
| 17 | H1 | 0. Executive model | MIXED_EXTRACTED_AND_DEFERRED | 02 organizational model; defer 01/03/04/05/06/07/08/09/10/11 execution semantics | `AGT-REQ-001` |
| 86 | H1 | 1. Relationship to the Documentation Operating Model | MIXED_EXTRACTED_AND_DEFERRED | 02 consumes external truth; 01 owns documentation/SoT/knowledge, 11 owns bindings | `AGT-REQ-001`, `AGT-REQ-002`, `AGT-REQ-005`, `AGT-REQ-075` |
| 136 | H1 | 2. Project Agent Manifest | DEFERRED_TO_MODULE | 11 | — |
| 224 | H1 | 3. Foundational principles | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance/SoD/source-before-inference interface; defer 04 risk, 06 Git, 07 evidence, 09 learning, 10 permissions | `AGT-REQ-001`, `AGT-REQ-004`, `AGT-REQ-005`, `AGT-REQ-027`, `AGT-REQ-033`, `AGT-REQ-035`, `AGT-REQ-036`, `AGT-REQ-037`, `AGT-REQ-055` |
| 226 | H2 | 3.1 Human governance | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-027`, `AGT-REQ-055` |
| 234 | H2 | 3.2 Separation of duties | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-035`, `AGT-REQ-036`, `AGT-REQ-037` |
| 254 | H2 | 3.3 Source of Truth before inference | MIXED_EXTRACTED_AND_DEFERRED | 02 agent source-before-inference; 01 owns SoT resolution semantics | `AGT-REQ-001` |
| 260 | H2 | 3.4 No silent invention | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-004` |
| 291 | H2 | 3.5 Evidence before approval | DEFERRED_TO_MODULE | 07 | — |
| 313 | H2 | 3.6 Least privilege | DEFERRED_TO_MODULE | 10 | — |
| 319 | H2 | 3.7 Small coherent changes | DEFERRED_TO_MODULE | 06 | — |
| 325 | H2 | 3.8 One PR, one intention | DEFERRED_TO_MODULE | 06 | — |
| 331 | H2 | 3.9 One commit, one logical change | DEFERRED_TO_MODULE | 06 | — |
| 337 | H2 | 3.10 No opportunistic refactoring by default | DEFERRED_TO_MODULE | 06 | — |
| 345 | H2 | 3.11 Risk-based governance | DEFERRED_TO_MODULE | 04 | — |
| 353 | H2 | 3.12 Organizational learning over hidden memory | DEFERRED_TO_MODULE | 09 + 01 Knowledge Lifecycle | — |
| 371 | H1 | 4. Core terminology | MIXED_EXTRACTED_AND_DEFERRED | 02 Agent/Orchestrator/Handoff/Run concepts; defer 03 Skill, 04 Workflow/Gate, 05 Memory, 07 Evidence, 10 Guardrail | `AGT-REQ-007`, `AGT-REQ-008`, `AGT-REQ-066` |
| 373 | H2 | Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-007`, `AGT-REQ-008`, `AGT-REQ-066` |
| 377 | H2 | Skill | DEFERRED_TO_MODULE | 03 | — |
| 391 | H2 | Workflow | DEFERRED_TO_MODULE | 04 | — |
| 404 | H2 | Orchestrator | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-007`, `AGT-REQ-008`, `AGT-REQ-066` |
| 408 | H2 | Guardrail | DEFERRED_TO_MODULE | 10/04 | — |
| 412 | H2 | Gate | DEFERRED_TO_MODULE | 07/04 | — |
| 416 | H2 | Handoff | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-007`, `AGT-REQ-008`, `AGT-REQ-066` |
| 420 | H2 | Project Memory | DEFERRED_TO_MODULE | 05/01 | — |
| 424 | H2 | Run | MIXED_EXTRACTED_AND_DEFERRED | 02 identity concept; 04 run lifecycle; 08 telemetry | `AGT-REQ-007`, `AGT-REQ-008`, `AGT-REQ-066` |
| 428 | H2 | Evidence | DEFERRED_TO_MODULE | 07/01 | — |
| 434 | H1 | 5. Universal Agent Contract | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-009`, `AGT-REQ-010`, `AGT-REQ-076`, `AGT-REQ-085`, `AGT-REQ-088` |
| 497 | H1 | 6. Agent identity is not enough | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-008`, `AGT-REQ-009`, `AGT-REQ-011`, `AGT-REQ-085` |
| 521 | H1 | 7. Universal role families | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-013` |
| 559 | H1 | 8. Orchestrator | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-027`, `AGT-REQ-029`, `AGT-REQ-033`, `AGT-REQ-053`, `AGT-REQ-077` |
| 561 | H2 | Mission | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-027`, `AGT-REQ-029`, `AGT-REQ-033`, `AGT-REQ-053`, `AGT-REQ-077` |
| 565 | H2 | Responsibilities | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-027`, `AGT-REQ-029`, `AGT-REQ-033`, `AGT-REQ-053`, `AGT-REQ-077` |
| 583 | H2 | Must not | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-027`, `AGT-REQ-029`, `AGT-REQ-033`, `AGT-REQ-053`, `AGT-REQ-077` |
| 594 | H1 | 9. Product Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-016` |
| 621 | H1 | 10. Domain / Architecture Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-017`, `AGT-REQ-018` |
| 648 | H1 | 11. UX / Product Design Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-019` |
| 671 | H1 | 12. Design System Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-020` |
| 689 | H1 | 13. Implementer Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-021`, `AGT-REQ-029`, `AGT-REQ-035`, `AGT-REQ-079` |
| 718 | H1 | 14. Reviewer Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-022`, `AGT-REQ-029`, `AGT-REQ-080` |
| 749 | H1 | 15. QA Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-023`, `AGT-REQ-029`, `AGT-REQ-080` |
| 773 | H1 | 16. Security Agent | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-024`, `AGT-REQ-029` |
| 798 | H1 | 17. Documentation Guardian | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-025` |
| 821 | H1 | 18. Merge Controller | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-026`, `AGT-REQ-029`, `AGT-REQ-079` |
| 851 | H1 | 19. Skills model | DEFERRED_TO_MODULE | 03 | — |
| 870 | H1 | 20. Skill contract | DEFERRED_TO_MODULE | 03 | — |
| 902 | H1 | 21. Example universal skills | DEFERRED_TO_MODULE | 03 | — |
| 933 | H1 | 22. Workflow contract | DEFERRED_TO_MODULE | 04 | — |
| 954 | H1 | 23. Change classification | DEFERRED_TO_MODULE | 04 | — |
| 971 | H1 | 24. C0 — Micro | DEFERRED_TO_MODULE | 04 | — |
| 996 | H1 | 25. C1 — Small | DEFERRED_TO_MODULE | 04 | — |
| 1018 | H1 | 26. C2 — Standard Feature | DEFERRED_TO_MODULE | 04 | — |
| 1043 | H1 | 27. C3 — Cross-cutting | DEFERRED_TO_MODULE | 04 | — |
| 1070 | H1 | 28. C4 — Architectural | DEFERRED_TO_MODULE | 04 | — |
| 1097 | H1 | 29. C5 — High-risk | DEFERRED_TO_MODULE | 04 | — |
| 1128 | H1 | 30. Risk override rule | DEFERRED_TO_MODULE | 04 | — |
| 1144 | H1 | 31. Context assembly | DEFERRED_TO_MODULE | 05 | — |
| 1165 | H1 | 32. Context assembly order | DEFERRED_TO_MODULE | 05 | — |
| 1182 | H1 | 33. Context budget principle | DEFERRED_TO_MODULE | 05 | — |
| 1198 | H1 | 34. Memory model | DEFERRED_TO_MODULE | 05 | — |
| 1215 | H1 | 35. Project memory sources | DEFERRED_TO_MODULE | 05 | — |
| 1235 | H1 | 36. Learning is not hidden model training | DEFERRED_TO_MODULE | 09 | — |
| 1257 | H1 | 37. Learning promotion model | DEFERRED_TO_MODULE | 09 | — |
| 1290 | H1 | 38. Permissions model | DEFERRED_TO_MODULE | 10 | — |
| 1317 | H1 | 39. Default role permission philosophy | DEFERRED_TO_MODULE | 10 | — |
| 1319 | H2 | Orchestrator | DEFERRED_TO_MODULE | 10 | — |
| 1330 | H2 | Implementer | DEFERRED_TO_MODULE | 10 | — |
| 1342 | H2 | Reviewer | DEFERRED_TO_MODULE | 10 | — |
| 1353 | H2 | QA | DEFERRED_TO_MODULE | 10 | — |
| 1362 | H2 | Merge Controller | DEFERRED_TO_MODULE | 10 | — |
| 1374 | H1 | 40. Human approval model | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance concept; defer 04 risk classes and 10 approval enforcement | `AGT-REQ-036`, `AGT-REQ-055`, `AGT-REQ-083` |
| 1391 | H1 | 41. Recommended adoption mode | DEFERRED_TO_MODULE | 11 | — |
| 1411 | H1 | 42. Planning model | DEFERRED_TO_MODULE | 06 | — |
| 1434 | H1 | 43. Expected commits | DEFERRED_TO_MODULE | 06 | — |
| 1453 | H1 | 44. Git operating principles | DEFERRED_TO_MODULE | 06 | — |
| 1455 | H2 | 44.1 No direct push to protected main | DEFERRED_TO_MODULE | 06 | — |
| 1459 | H2 | 44.2 One branch per coherent task | DEFERRED_TO_MODULE | 06 | — |
| 1474 | H1 | 45. Atomic logical commits | DEFERRED_TO_MODULE | 06 | — |
| 1491 | H1 | 46. Bad commit granularity | DEFERRED_TO_MODULE | 06 | — |
| 1507 | H1 | 47. Bad oversized commit | DEFERRED_TO_MODULE | 06 | — |
| 1528 | H1 | 48. Commit categories | DEFERRED_TO_MODULE | 06 | — |
| 1548 | H1 | 49. Commit message contract | DEFERRED_TO_MODULE | 06 | — |
| 1566 | H1 | 50. Bug-fix commit strategy | DEFERRED_TO_MODULE | 06 | — |
| 1581 | H1 | 51. Review-fix commits | DEFERRED_TO_MODULE | 06 | — |
| 1591 | H1 | 52. PR operating model | DEFERRED_TO_MODULE | 06 | — |
| 1601 | H1 | 53. Good PR | DEFERRED_TO_MODULE | 06 | — |
| 1624 | H1 | 54. Bad PR | DEFERRED_TO_MODULE | 06 | — |
| 1640 | H1 | 55. PR size policy | DEFERRED_TO_MODULE | 06 | — |
| 1656 | H1 | 56. PR description contract | DEFERRED_TO_MODULE | 06 | — |
| 1692 | H1 | 57. Creation loop | DEFERRED_TO_MODULE | 06 | — |
| 1707 | H1 | 58. Verification loop | MIXED_EXTRACTED_AND_DEFERRED | 02 creation/verification separation; defer 07 verification procedure | `AGT-REQ-021`, `AGT-REQ-022`, `AGT-REQ-035`, `AGT-REQ-080` |
| 1723 | H1 | 59. Self-check | DEFERRED_TO_MODULE | 07 | — |
| 1741 | H1 | 60. Independent review protocol | DEFERRED_TO_MODULE | 07 | — |
| 1758 | H1 | 61. Review finding severity | DEFERRED_TO_MODULE | 07 | — |
| 1778 | H1 | 62. Review output contract | DEFERRED_TO_MODULE | 07 | — |
| 1815 | H1 | 63. Reviewer independence | MIXED_EXTRACTED_AND_DEFERRED | 02 Reviewer independence; defer 07 review mechanics | `AGT-REQ-022`, `AGT-REQ-035`, `AGT-REQ-038` |
| 1831 | H1 | 64. QA protocol | DEFERRED_TO_MODULE | 07 | — |
| 1847 | H1 | 65. QA dimensions | DEFERRED_TO_MODULE | 07 | — |
| 1868 | H1 | 66. Documentation gate | DEFERRED_TO_MODULE | 07 | — |
| 1886 | H1 | 67. Architecture gate | DEFERRED_TO_MODULE | 07 | — |
| 1903 | H1 | 68. Security gate | DEFERRED_TO_MODULE | 07 | — |
| 1920 | H1 | 69. Database migration gate | DEFERRED_TO_MODULE | 07 | — |
| 1935 | H1 | 70. Merge readiness | DEFERRED_TO_MODULE | 07 | — |
| 1949 | H1 | 71. Merge authority | DEFERRED_TO_MODULE | 06/10 | — |
| 1966 | H1 | 72. Merge strategy | DEFERRED_TO_MODULE | 06 | — |
| 1982 | H1 | 73. Handoff protocol | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-031`, `AGT-REQ-032`, `AGT-REQ-042`, `AGT-REQ-043`, `AGT-REQ-044`, `AGT-REQ-045`, `AGT-REQ-046` |
| 2027 | H1 | 74. Handoff context minimization | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-042` |
| 2042 | H1 | 75. Guardrails | DEFERRED_TO_MODULE | 10/04 | — |
| 2058 | H1 | 76. Guardrail types | DEFERRED_TO_MODULE | 10/04 | — |
| 2070 | H1 | 77. Escalation model | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-003`, `AGT-REQ-004`, `AGT-REQ-046`, `AGT-REQ-047`, `AGT-REQ-054` |
| 2087 | H1 | 78. Escalation targets | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-031`, `AGT-REQ-032`, `AGT-REQ-046`, `AGT-REQ-047`, `AGT-REQ-054` |
| 2101 | H1 | 79. Failure and recovery | DEFERRED_TO_MODULE | 04 | — |
| 2119 | H1 | 80. Retry policy | DEFERRED_TO_MODULE | 04 | — |
| 2137 | H1 | 81. Scope Guardian | DEFERRED_TO_MODULE | 07 | — |
| 2158 | H1 | 82. Concurrency model | DEFERRED_TO_MODULE | 06 | — |
| 2182 | H1 | 83. Task isolation | DEFERRED_TO_MODULE | 06 | — |
| 2202 | H1 | 84. Shared file collision | DEFERRED_TO_MODULE | 06 | — |
| 2216 | H1 | 85. Workflow — Micro Change | DEFERRED_TO_MODULE | 04 | — |
| 2237 | H1 | 86. Workflow — Bug Fix | DEFERRED_TO_MODULE | 04 | — |
| 2255 | H1 | 87. Workflow — New Feature | DEFERRED_TO_MODULE | 04 | — |
| 2276 | H1 | 88. Workflow — UI Change | DEFERRED_TO_MODULE | 04 | — |
| 2292 | H1 | 89. Workflow — Design System Change | DEFERRED_TO_MODULE | 04 | — |
| 2308 | H1 | 90. Workflow — Architecture Change | DEFERRED_TO_MODULE | 04 | — |
| 2326 | H1 | 91. Workflow — API Change | DEFERRED_TO_MODULE | 04 | — |
| 2341 | H1 | 92. Workflow — Database Migration | DEFERRED_TO_MODULE | 04 | — |
| 2357 | H1 | 93. Workflow — Security Change | DEFERRED_TO_MODULE | 04 | — |
| 2372 | H1 | 94. Workflow — Refactor | DEFERRED_TO_MODULE | 04 | — |
| 2387 | H1 | 95. Workflow — Dependency Upgrade | DEFERRED_TO_MODULE | 04 | — |
| 2401 | H1 | 96. Workflow — Hotfix | DEFERRED_TO_MODULE | 04 | — |
| 2421 | H1 | 97. Workflow — Documentation Change | DEFERRED_TO_MODULE | 04 | — |
| 2436 | H1 | 98. Workflow — Release | DEFERRED_TO_MODULE | 04 | — |
| 2452 | H1 | 99. Observability model | DEFERRED_TO_MODULE | 08 | — |
| 2485 | H1 | 100. Dashboard-ready metrics | DEFERRED_TO_MODULE | 08 | — |
| 2510 | H1 | 101. Do not optimize for activity | DEFERRED_TO_MODULE | 08 | — |
| 2525 | H1 | 102. Quality metrics | DEFERRED_TO_MODULE | 08 | — |
| 2542 | H1 | 103. Agent performance | DEFERRED_TO_MODULE | 08 | — |
| 2559 | H1 | 104. Agent learning record | DEFERRED_TO_MODULE | 09 | — |
| 2583 | H1 | 105. Skill evolution | DEFERRED_TO_MODULE | 09 | — |
| 2604 | H1 | 106. Workflow evolution | DEFERRED_TO_MODULE | 09 | — |
| 2617 | H1 | 107. Agent contract evolution | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-064`, `AGT-REQ-067`, `AGT-REQ-082` |
| 2630 | H1 | 108. Model/provider independence | DEFERRED_TO_MODULE | 11 | — |
| 2648 | H1 | 109. Tool independence | DEFERRED_TO_MODULE | 11 | — |
| 2665 | H1 | 110. Safety around secrets | DEFERRED_TO_MODULE | 10 | — |
| 2683 | H1 | 111. Production access | DEFERRED_TO_MODULE | 10 | — |
| 2695 | H1 | 112. Protected files | DEFERRED_TO_MODULE | 10 | — |
| 2711 | H1 | 113. Definition of Ready — task | DEFERRED_TO_MODULE | 07 | — |
| 2730 | H1 | 114. Definition of Ready — agent execution | DEFERRED_TO_MODULE | 07 | — |
| 2746 | H1 | 115. Definition of Done — implementation | DEFERRED_TO_MODULE | 07 | — |
| 2760 | H1 | 116. Definition of Done — PR | DEFERRED_TO_MODULE | 07 | — |
| 2775 | H1 | 117. Definition of Done — workflow | DEFERRED_TO_MODULE | 07 | — |
| 2788 | H1 | 118. Recommended repository structure | DEFERRED_TO_MODULE | 11 | — |
| 2864 | H1 | 119. Maturity model | DEFERRED_TO_MODULE | 11 | — |
| 2866 | H2 | Level 0 — Single Agent | DEFERRED_TO_MODULE | 11 | — |
| 2870 | H2 | Level 1 — Role Profiles | DEFERRED_TO_MODULE | 11 | — |
| 2874 | H2 | Level 2 — Governed Workflows | DEFERRED_TO_MODULE | 11 | — |
| 2878 | H2 | Level 3 — Orchestrated Team | DEFERRED_TO_MODULE | 11 | — |
| 2882 | H2 | Level 4 — Automated Verification | DEFERRED_TO_MODULE | 11 | — |
| 2886 | H2 | Level 5 — Controlled Autonomy | DEFERRED_TO_MODULE | 11 | — |
| 2890 | H2 | Level 6 — Learning Organization | DEFERRED_TO_MODULE | 11 | — |
| 2898 | H1 | 120. Recommended adoption sequence | DEFERRED_TO_MODULE | 11 | — |
| 2900 | H2 | Stage 1 — Documentation foundation | DEFERRED_TO_MODULE | 11 | — |
| 2904 | H2 | Stage 2 — Project Agent Manifest | DEFERRED_TO_MODULE | 11 | — |
| 2908 | H2 | Stage 3 — Three roles | DEFERRED_TO_MODULE | 11 | — |
| 2920 | H2 | Stage 4 — Add QA and Documentation Guardian | DEFERRED_TO_MODULE | 11 | — |
| 2924 | H2 | Stage 5 — Add specialist agents | DEFERRED_TO_MODULE | 11 | — |
| 2928 | H2 | Stage 6 — Formal workflows | DEFERRED_TO_MODULE | 11 | — |
| 2932 | H2 | Stage 7 — Telemetry | DEFERRED_TO_MODULE | 11 | — |
| 2936 | H2 | Stage 8 — Limited autonomous merge | DEFERRED_TO_MODULE | 11 | — |
| 2942 | H1 | 121. Recommended first implementation | DEFERRED_TO_MODULE | 11 | — |
| 2982 | H1 | 122. Universal Orchestrator algorithm | MIXED_EXTRACTED_AND_DEFERRED | 02 Orchestrator organizational authority; defer 04 routing/state, 05 context, 10 approval gates | `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-077` |
| 3009 | H1 | 123. Authority conflict resolution | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-003`, `AGT-REQ-014`, `AGT-REQ-015`, `AGT-REQ-016`, `AGT-REQ-017`, `AGT-REQ-018`, `AGT-REQ-019`, `AGT-REQ-020`, `AGT-REQ-027`, `AGT-REQ-028`, `AGT-REQ-029`, `AGT-REQ-030`, `AGT-REQ-031`, `AGT-REQ-044`, `AGT-REQ-048` |
| 3028 | H1 | 124. Security veto | MIXED_EXTRACTED_AND_DEFERRED | 02 scoped Security veto semantics; defer 10 security policy/overridability | `AGT-REQ-015`, `AGT-REQ-024`, `AGT-REQ-030`, `AGT-REQ-049`, `AGT-REQ-050`, `AGT-REQ-053`, `AGT-REQ-057` |
| 3038 | H1 | 125. Architecture veto | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-015`, `AGT-REQ-018`, `AGT-REQ-030`, `AGT-REQ-049`, `AGT-REQ-051`, `AGT-REQ-053` |
| 3051 | H1 | 126. Reviewer veto | MIXED_EXTRACTED_AND_DEFERRED | 02 Reviewer blocking authority; defer 07 review criteria/evidence | `AGT-REQ-015`, `AGT-REQ-022`, `AGT-REQ-030`, `AGT-REQ-049`, `AGT-REQ-052`, `AGT-REQ-053` |
| 3072 | H1 | 127. Human override | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Override semantics; defer 10 approval enforcement and 01 durable decision promotion | `AGT-REQ-055`, `AGT-REQ-056`, `AGT-REQ-057` |
| 3091 | H1 | 128. Agent output discipline | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-006`, `AGT-REQ-070` |
| 3107 | H1 | 129. Change Classification output | DEFERRED_TO_MODULE | 04 | — |
| 3137 | H1 | 130. Implementation Plan output | DEFERRED_TO_MODULE | 06 | — |
| 3174 | H1 | 131. Review Result output | DEFERRED_TO_MODULE | 07 | — |
| 3206 | H1 | 132. QA Result output | DEFERRED_TO_MODULE | 07 | — |
| 3232 | H1 | 133. Merge Readiness output | DEFERRED_TO_MODULE | 07 | — |
| 3252 | H1 | 134. Change review feedback loop | MIXED_EXTRACTED_AND_DEFERRED | 02 Implementer↔Reviewer responsibility separation; defer 07 review loop and 06 commit mechanics | `AGT-REQ-021`, `AGT-REQ-022`, `AGT-REQ-038`, `AGT-REQ-054` |
| 3266 | H1 | 135. Oversized PR handling | DEFERRED_TO_MODULE | 06 | — |
| 3281 | H1 | 136. Scope expansion handling | DEFERRED_TO_MODULE | 04/06 | — |
| 3298 | H1 | 137. Unplanned architecture discovery | MIXED_EXTRACTED_AND_DEFERRED | 02 architecture-boundary escalation; defer 04 workflow transition | `AGT-REQ-018`, `AGT-REQ-021`, `AGT-REQ-047`, `AGT-REQ-051` |
| 3313 | H1 | 138. Unplanned product ambiguity | MIXED_EXTRACTED_AND_DEFERRED | 02 product-ambiguity escalation; defer 04 workflow transition | `AGT-REQ-019`, `AGT-REQ-021`, `AGT-REQ-047` |
| 3327 | H1 | 139. Unplanned security concern | DEFERRED_TO_MODULE | 10/04 | — |
| 3333 | H1 | 140. Documentation drift detection | DEFERRED_TO_MODULE | 07/01 | — |
| 3348 | H1 | 141. Agent sandbox hygiene | DEFERRED_TO_MODULE | 06 | — |
| 3368 | H1 | 142. Branch lifetime | DEFERRED_TO_MODULE | 06 | — |
| 3376 | H1 | 143. Stacked PRs | DEFERRED_TO_MODULE | 06 | — |
| 3384 | H1 | 144. Feature flags | DEFERRED_TO_MODULE | 06 | — |
| 3399 | H1 | 145. Rollback thinking | DEFERRED_TO_MODULE | 06 | — |
| 3411 | H1 | 146. Dependency graph awareness | DEFERRED_TO_MODULE | 04 | — |
| 3429 | H1 | 147. Cost awareness | DEFERRED_TO_MODULE | 08/04 | — |
| 3439 | H1 | 148. Latency awareness | DEFERRED_TO_MODULE | 08/04 | — |
| 3457 | H1 | 149. Human attention as scarce resource | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-055`, `AGT-REQ-059` |
| 3474 | H1 | 150. Agent communication rule | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-042`, `AGT-REQ-068` |
| 3482 | H1 | 151. Decision preservation | MIXED_EXTRACTED_AND_DEFERRED | 02 artifact/communication obligation; defer 01 decision/knowledge preservation | `AGT-REQ-005`, `AGT-REQ-006`, `AGT-REQ-025`, `AGT-REQ-045`, `AGT-REQ-067`, `AGT-REQ-068` |
| 3499 | H1 | 152. No circular authority | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-035`, `AGT-REQ-039` |
| 3514 | H1 | 153. Independent model diversity | MIXED_EXTRACTED_AND_DEFERRED | 02 logical role independence; defer 11 provider/model selection | `AGT-REQ-008`, `AGT-REQ-037`, `AGT-REQ-084` |
| 3524 | H1 | 154. Review freshness | DEFERRED_TO_MODULE | 07 | — |
| 3532 | H1 | 155. Merge queue compatibility | DEFERRED_TO_MODULE | 06/11 | — |
| 3538 | H1 | 156. CI as evidence provider | DEFERRED_TO_MODULE | 07 | — |
| 3555 | H1 | 157. Agent-specific test ownership | DEFERRED_TO_MODULE | 07 | — |
| 3577 | H1 | 158. Test integrity | DEFERRED_TO_MODULE | 07 | — |
| 3583 | H1 | 159. Snapshot integrity | DEFERRED_TO_MODULE | 07 | — |
| 3589 | H1 | 160. Security scanner integrity | DEFERRED_TO_MODULE | 07 | — |
| 3595 | H1 | 161. Linter suppression | DEFERRED_TO_MODULE | 07 | — |
| 3601 | H1 | 162. Technical debt creation | DEFERRED_TO_MODULE | 06 | — |
| 3609 | H1 | 163. Technical debt review | DEFERRED_TO_MODULE | 06/09 | — |
| 3623 | H1 | 164. Post-merge verification | DEFERRED_TO_MODULE | 07 | — |
| 3636 | H1 | 165. Post-merge learning trigger | DEFERRED_TO_MODULE | 09 | — |
| 3652 | H1 | 166. Incident integration | DEFERRED_TO_MODULE | 09 | — |
| 3667 | H1 | 167. Dashboard model | DEFERRED_TO_MODULE | 08 | — |
| 3690 | H1 | 168. Agent workload | DEFERRED_TO_MODULE | 08 | — |
| 3709 | H1 | 169. Workflow bottleneck analysis | DEFERRED_TO_MODULE | 08 | — |
| 3724 | H1 | 170. Maturity gates for autonomy | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance boundary; defer 08 reliability evidence, 10 autonomy permissions, 11 project policy | `AGT-REQ-036`, `AGT-REQ-055`, `AGT-REQ-059`, `AGT-REQ-060` |
| 3740 | H1 | 171. Autonomy expansion | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance boundary; defer 08 reliability evidence, 10 autonomy permissions, 11 project policy | `AGT-REQ-036`, `AGT-REQ-055`, `AGT-REQ-059`, `AGT-REQ-060` |
| 3755 | H1 | 172. Project-specific overrides | DEFERRED_TO_MODULE | 11 | — |
| 3769 | H1 | 173. Universal vs project-specific rules | DEFERRED_TO_MODULE | 11 | — |
| 3791 | H1 | 174. Agent manifests should be versioned | DEFERRED_TO_MODULE | 11 | — |
| 3807 | H1 | 175. Governance change workflow | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-060`, `AGT-REQ-064` |
| 3821 | H1 | 176. Universal starter agent set | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-013`, `AGT-REQ-040` |
| 3846 | H1 | 177. Universal full agent set | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-013`, `AGT-REQ-040` |
| 3874 | H1 | 178. Agent composition | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-037`, `AGT-REQ-040` |
| 3896 | H1 | 179. Universal policy files | DEFERRED_TO_MODULE | 11 | — |
| 3913 | H1 | 180. AI Agent README | DEFERRED_TO_MODULE | 11 | — |
| 3927 | H1 | 181. Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | 11 | — |
| 3944 | H1 | 182. Universal file naming | DEFERRED_TO_MODULE | 11 | — |
| 3963 | H1 | 183. Agent contract versioning | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-009`, `AGT-REQ-064`, `AGT-REQ-065` |
| 3975 | H1 | 184. Skill versioning | DEFERRED_TO_MODULE | 03 | — |
| 3981 | H1 | 185. Workflow versioning | DEFERRED_TO_MODULE | 04 | — |
| 3987 | H1 | 186. Telemetry retention | DEFERRED_TO_MODULE | 08 | — |
| 3993 | H1 | 187. Sensitive context policy | DEFERRED_TO_MODULE | 10 | — |
| 3999 | H1 | 188. Secret redaction | DEFERRED_TO_MODULE | 10 | — |
| 4005 | H1 | 189. Auditability | DEFERRED_TO_MODULE | 08/10 | — |
| 4019 | H1 | 190. Reproducibility | DEFERRED_TO_MODULE | 08/07 | — |
| 4035 | H1 | 191. Agent hallucination handling | MIXED_EXTRACTED_AND_DEFERRED | 02 unsupported-claim behavior; defer 01 SoT semantics and 07 verification | `AGT-REQ-001`, `AGT-REQ-002`, `AGT-REQ-004`, `AGT-REQ-005`, `AGT-REQ-006`, `AGT-REQ-071`, `AGT-REQ-075` |
| 4047 | H1 | 192. Missing Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | 02 escalation on missing truth; defer 01 SoT and 05 retrieval/context | `AGT-REQ-002`, `AGT-REQ-003`, `AGT-REQ-004`, `AGT-REQ-071`, `AGT-REQ-075` |
| 4060 | H1 | 193. Stale Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | 02 escalation on stale/conflicting truth; defer 01 SoT and 05 retrieval/context | `AGT-REQ-002`, `AGT-REQ-003`, `AGT-REQ-071`, `AGT-REQ-075` |
| 4072 | H1 | 194. Feature lifecycle integration | DEFERRED_TO_MODULE | 04 | — |
| 4080 | H1 | 195. Agent lifecycle | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-007`, `AGT-REQ-061`, `AGT-REQ-062`, `AGT-REQ-063` |
| 4095 | H1 | 196. Task lifecycle | DEFERRED_TO_MODULE | 04 | — |
| 4114 | H1 | 197. PR lifecycle | DEFERRED_TO_MODULE | 06 | — |
| 4120 | H1 | 198. Agent run lifecycle | MIXED_EXTRACTED_AND_DEFERRED | 02 Agent Run identity distinction; defer 04 Run lifecycle and 08 telemetry | `AGT-REQ-007`, `AGT-REQ-062`, `AGT-REQ-066` |
| 4136 | H1 | 199. Workflow state machine | DEFERRED_TO_MODULE | 04 | — |
| 4142 | H1 | 200. No hidden background authority | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-032`, `AGT-REQ-033`, `AGT-REQ-067`, `AGT-REQ-069` |
| 4148 | H1 | 201. Human pause points | MIXED_EXTRACTED_AND_DEFERRED | 02 human-protected pause concept; defer 04 workflow pause and 10 approvals | `AGT-REQ-047` |
| 4162 | H1 | 202. Plan change protocol | DEFERRED_TO_MODULE | 04 | — |
| 4174 | H1 | 203. Reclassification | DEFERRED_TO_MODULE | 04 | — |
| 4184 | H1 | 204. Risk inheritance | DEFERRED_TO_MODULE | 04 | — |
| 4190 | H1 | 205. Change decomposition | DEFERRED_TO_MODULE | 04 | — |
| 4196 | H1 | 206. Multi-agent code ownership | DEFERRED_TO_MODULE | 06/04 | — |
| 4202 | H1 | 207. Shared contract first | DEFERRED_TO_MODULE | 06/04 | — |
| 4215 | H1 | 208. Reviewer context independence | MIXED_EXTRACTED_AND_DEFERRED | 02 Reviewer organizational independence; defer 05 context assembly and 07 review inputs | `AGT-REQ-022`, `AGT-REQ-041`, `AGT-REQ-078` |
| 4233 | H1 | 209. QA context independence | DEFERRED_TO_MODULE | 05/07 | — |
| 4241 | H1 | 210. Merge Controller context | MIXED_EXTRACTED_AND_DEFERRED | 02 Merge Controller role boundary; defer 05 context and 07 readiness evidence | `AGT-REQ-026`, `AGT-REQ-041`, `AGT-REQ-078` |
| 4249 | H1 | 211. Product Owner context | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance decision recipient; defer 05 decision-context assembly | `AGT-REQ-058`, `AGT-REQ-078` |
| 4266 | H1 | 212. Decision packet | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-058` |
| 4294 | H1 | 213. Do not fake consensus | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-034`, `AGT-REQ-045`, `AGT-REQ-058`, `AGT-REQ-086` |
| 4302 | H1 | 214. Conflict resolution by authority | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-003`, `AGT-REQ-027`, `AGT-REQ-028`, `AGT-REQ-034`, `AGT-REQ-048`, `AGT-REQ-086` |
| 4317 | H1 | 215. Majority voting | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-028`, `AGT-REQ-034`, `AGT-REQ-086` |
| 4323 | H1 | 216. Agent confidence | DEFERRED_TO_MODULE | 07 | — |
| 4331 | H1 | 217. Evidence hierarchy | DEFERRED_TO_MODULE | 07 | — |
| 4350 | H1 | 218. Change evidence bundle | DEFERRED_TO_MODULE | 07 | — |
| 4367 | H1 | 219. Artifact retention | DEFERRED_TO_MODULE | 08/01 | — |
| 4390 | H1 | 220. Privacy of reasoning | DEFERRED_TO_MODULE | 08/10 | — |
| 4398 | H1 | 221. Universal anti-patterns | MIXED_EXTRACTED_AND_DEFERRED | 02 subrules 221.1/221.2/221.8; defer remaining anti-patterns to 03/05/06/07/08 | `AGT-REQ-012`, `AGT-REQ-021`, `AGT-REQ-035`, `AGT-REQ-068`, `AGT-REQ-072` |
| 4400 | H2 | 221.1 Agent swarm without ownership | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-072` |
| 4404 | H2 | 221.2 Self-approval | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-035` |
| 4408 | H2 | 221.3 Every task runs every agent | DEFERRED_TO_MODULE | 04 | — |
| 4412 | H2 | 221.4 Giant context dump | DEFERRED_TO_MODULE | 05 | — |
| 4416 | H2 | 221.5 Prompt duplication | DEFERRED_TO_MODULE | 03/11 | — |
| 4420 | H2 | 221.6 Hidden project memory | MIXED_EXTRACTED_AND_DEFERRED | 02 communication boundary; 01/05 memory | `AGT-REQ-068` |
| 4424 | H2 | 221.7 Activity metrics | DEFERRED_TO_MODULE | 08 | — |
| 4428 | H2 | 221.8 AI-created architecture by accident | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-021` |
| 4432 | H2 | 221.9 Fake review | DEFERRED_TO_MODULE | 07 | — |
| 4436 | H2 | 221.10 Git history as keystroke log | DEFERRED_TO_MODULE | 06 | — |
| 4442 | H1 | 222. Governance health checks | MIXED_EXTRACTED_AND_DEFERRED | 02 scope/role health checks; defer workflow/learning/permission/observability checks to owners | `AGT-REQ-073` |
| 4459 | H1 | 223. Quarterly / milestone review | MIXED_EXTRACTED_AND_DEFERRED | 02 Agent Contract review; defer workflow/risk/telemetry/learning reviews to owners | `AGT-REQ-067`, `AGT-REQ-073` |
| 4475 | H1 | 224. Universal adoption checklist | MIXED_EXTRACTED_AND_DEFERRED | 02 SoD/Role adoption checks; defer manifest/risk/Git/QA/learning/telemetry checks to owners | `AGT-REQ-035`, `AGT-REQ-072` |
| 4494 | H1 | 225. Minimal viable agent system | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-040`, `AGT-REQ-072`, `AGT-REQ-087` |
| 4513 | H1 | 226. Intermediate agent system | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-040`, `AGT-REQ-072`, `AGT-REQ-087` |
| 4531 | H1 | 227. Advanced agent system | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-012`, `AGT-REQ-013`, `AGT-REQ-040`, `AGT-REQ-072`, `AGT-REQ-087` |
| 4550 | H1 | 228. Final operating model | MIXED_EXTRACTED_AND_DEFERRED | 02 organization/authority/SoD/human boundary; defer execution pipeline to owning modules | `AGT-REQ-014`, `AGT-REQ-074`, `AGT-REQ-087` |
| 4600 | H1 | Appendix A — Project Agent Manifest template | DEFERRED_TO_MODULE | 11 | — |
| 4679 | H1 | Appendix B — Agent Contract template | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-009`, `AGT-REQ-010`, `AGT-REQ-088` |
| 4722 | H1 | Appendix C — Skill template | DEFERRED_TO_MODULE | 03 | — |
| 4757 | H1 | Appendix D — Workflow template | DEFERRED_TO_MODULE | 04 | — |
| 4798 | H1 | Appendix E — Change Plan template | DEFERRED_TO_MODULE | 06 | — |
| 4832 | H1 | Appendix F — Handoff template | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-042`, `AGT-REQ-043`, `AGT-REQ-044` |
| 4861 | H1 | Appendix G — Review Result template | DEFERRED_TO_MODULE | 07 | — |
| 4905 | H1 | Appendix H — QA Result template | DEFERRED_TO_MODULE | 07 | — |
| 4929 | H1 | Appendix I — Merge Readiness template | DEFERRED_TO_MODULE | 07 | — |
| 4957 | H1 | Appendix J — Risk Classification Matrix | DEFERRED_TO_MODULE | 04 | — |
| 4970 | H1 | Appendix K — Permission Matrix example | DEFERRED_TO_MODULE | 10 | — |
| 4985 | H1 | Appendix L — Git Policy starter | DEFERRED_TO_MODULE | 06 | — |
| 5021 | H1 | Appendix M — Review Policy starter | DEFERRED_TO_MODULE | 07 | — |
| 5048 | H1 | Appendix N — Human Approval Policy starter | MIXED_EXTRACTED_AND_DEFERRED | 02 Human Governance concept; defer concrete approval policy to 10 | `AGT-REQ-055` |
| 5073 | H1 | Appendix O — Example New Feature workflow | DEFERRED_TO_MODULE | 04 | — |
| 5115 | H1 | Appendix P — Example Bug Fix workflow | DEFERRED_TO_MODULE | 04 | — |
| 5140 | H1 | Appendix Q — Example Architecture Change workflow | DEFERRED_TO_MODULE | 04 | — |
| 5174 | H1 | Appendix R — Learning Record template | DEFERRED_TO_MODULE | 09 | — |
| 5202 | H1 | Appendix S — Telemetry schema starter | DEFERRED_TO_MODULE | 08 | — |
| 5229 | H1 | Appendix T — Adoption directive for an existing project | DEFERRED_TO_MODULE | 11 | — |
| 5279 | H1 | Final principles | MIXED_EXTRACTED_AND_DEFERRED | 02 principles 2/3/8/10; defer principles 1/4/5/6/7/9 to 01/04/06/07/09/11 | `AGT-REQ-001`, `AGT-REQ-005`, `AGT-REQ-009`, `AGT-REQ-027`, `AGT-REQ-035`, `AGT-REQ-074`, `AGT-REQ-075`, `AGT-REQ-085` |
| 5281 | H2 | 1 | MIXED_EXTRACTED_AND_DEFERRED | 02 external-truth invariant; 01 source truth | `AGT-REQ-001`, `AGT-REQ-075` |
| 5285 | H2 | 2 | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-027` |
| 5289 | H2 | 3 | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-035` |
| 5293 | H2 | 4 | DEFERRED_TO_MODULE | 04 | — |
| 5297 | H2 | 5 | DEFERRED_TO_MODULE | 06 | — |
| 5301 | H2 | 6 | DEFERRED_TO_MODULE | 07 | — |
| 5305 | H2 | 7 | DEFERRED_TO_MODULE | 09/01 | — |
| 5309 | H2 | 8 | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-009`, `AGT-REQ-085` |
| 5313 | H2 | 9 | DEFERRED_TO_MODULE | 11/10 | — |
| 5317 | H2 | 10 | EXTRACTED_TO_MODULE_02 | 02 | `AGT-REQ-074` |

## Coverage

```text
FROZEN STRUCTURAL SECTIONS = 317
MODULE-02 OR MIXED STRUCTURAL SECTIONS = 94
UNMAPPED MODULE-02 STRUCTURAL SECTIONS = 0
```

All fully deferred rows retain an explicit downstream/upstream owner instead of being copied into Module 02.
