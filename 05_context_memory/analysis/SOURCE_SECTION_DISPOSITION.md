# Frozen Source Section Disposition

**ID:** UPOS-05-AN-003  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-005 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 05 artifacts.  
**Related:** ../MODULE_05_TRACEABILITY.md

> **Historical evidence notice:** This file records the UPOS-005 v1.0 decomposition/design state at implementation time. It is not timeless normative truth. Current Context & Memory semantics are owned by canonical Module 05 normative artifacts; `MODULE_05_TRACEABILITY.md` is the canonical coverage artifact after implementation.


**Frozen structural headings inspected:** 504  
**Extracted directly to Module 05:** 15  
**Mixed Context/Memory sections:** 46  
**Outside Module 05:** 443

`MIXED_EXTRACTED_AND_DEFERRED` means only Context/Memory semantics are extracted; remaining semantics stay with the indicated owner(s).

| Source unit | Line | Level | Section | Disposition | Remaining/deferred ownership |
|---|---:|---:|---|---|---|
| SRC-001 | 1 | 1 | Universal AI Agent Operating Model v1.0 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-002 | 17 | 1 | 0. Executive model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-001 |
| SRC-003 | 86 | 1 | 1. Relationship to the Documentation Operating Model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-001 |
| SRC-004 | 136 | 1 | 2. Project Agent Manifest | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-005 | 151 | 1 | Project Agent Manifest | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-006 | 224 | 1 | 3. Foundational principles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-007 | 226 | 2 | 3.1 Human governance | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-008 | 234 | 2 | 3.2 Separation of duties | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-009 | 254 | 2 | 3.3 Source of Truth before inference | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-010 | 260 | 2 | 3.4 No silent invention | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-011 | 291 | 2 | 3.5 Evidence before approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-012 | 313 | 2 | 3.6 Least privilege | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-013 | 319 | 2 | 3.7 Small coherent changes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-014 | 325 | 2 | 3.8 One PR, one intention | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-015 | 331 | 2 | 3.9 One commit, one logical change | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-016 | 337 | 2 | 3.10 No opportunistic refactoring by default | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-017 | 345 | 2 | 3.11 Risk-based governance | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-018 | 353 | 2 | 3.12 Organizational learning over hidden memory | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-019 | 371 | 1 | 4. Core terminology | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-020 | 373 | 2 | Agent | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-021 | 377 | 2 | Skill | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-022 | 391 | 2 | Workflow | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-023 | 404 | 2 | Orchestrator | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-024 | 408 | 2 | Guardrail | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-025 | 412 | 2 | Gate | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-026 | 416 | 2 | Handoff | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-027 | 420 | 2 | Project Memory | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-028 | 424 | 2 | Run | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-029 | 428 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-030 | 434 | 1 | 5. Universal Agent Contract | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-031 | 441 | 1 | Agent — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-032 | 443 | 2 | Identity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-033 | 446 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-034 | 449 | 2 | Owns | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-035 | 452 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-036 | 455 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-037 | 458 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-038 | 461 | 2 | Optional sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-039 | 464 | 2 | Tools | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-040 | 467 | 2 | Permissions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-041 | 470 | 2 | Skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-042 | 473 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-043 | 476 | 2 | Process | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-044 | 479 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-045 | 482 | 2 | Quality gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-046 | 485 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-047 | 488 | 2 | Handoffs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-048 | 491 | 2 | Prohibited behavior | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-049 | 497 | 1 | 6. Agent identity is not enough | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-050 | 521 | 1 | 7. Universal role families | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-051 | 559 | 1 | 8. Orchestrator | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-052 | 561 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-053 | 565 | 2 | Responsibilities | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-054 | 583 | 2 | Must not | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-055 | 594 | 1 | 9. Product Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-056 | 621 | 1 | 10. Domain / Architecture Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-057 | 648 | 1 | 11. UX / Product Design Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-058 | 671 | 1 | 12. Design System Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-059 | 689 | 1 | 13. Implementer Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-060 | 718 | 1 | 14. Reviewer Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-061 | 749 | 1 | 15. QA Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-062 | 773 | 1 | 16. Security Agent | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-063 | 798 | 1 | 17. Documentation Guardian | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-064 | 821 | 1 | 18. Merge Controller | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-065 | 851 | 1 | 19. Skills model | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-066 | 870 | 1 | 20. Skill contract | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-067 | 875 | 1 | Skill — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-068 | 877 | 2 | Purpose | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-069 | 879 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-070 | 881 | 2 | Preconditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-071 | 883 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-072 | 885 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-073 | 887 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-074 | 889 | 2 | Quality criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-075 | 891 | 2 | Failure modes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-076 | 893 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-077 | 895 | 2 | Applicable roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-078 | 897 | 2 | Applicable risk classes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-079 | 902 | 1 | 21. Example universal skills | MIXED_EXTRACTED_AND_DEFERRED | UPOS-003 |
| SRC-080 | 933 | 1 | 22. Workflow contract | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-081 | 954 | 1 | 23. Change classification | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-082 | 971 | 1 | 24. C0 — Micro | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-083 | 996 | 1 | 25. C1 — Small | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-084 | 1018 | 1 | 26. C2 — Standard Feature | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-085 | 1043 | 1 | 27. C3 — Cross-cutting | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 |
| SRC-086 | 1070 | 1 | 28. C4 — Architectural | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-087 | 1097 | 1 | 29. C5 — High-risk | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-088 | 1128 | 1 | 30. Risk override rule | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-089 | 1144 | 1 | 31. Context assembly | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-090 | 1165 | 1 | 32. Context assembly order | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-091 | 1182 | 1 | 33. Context budget principle | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-092 | 1198 | 1 | 34. Memory model | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-093 | 1215 | 1 | 35. Project memory sources | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-094 | 1235 | 1 | 36. Learning is not hidden model training | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-001 / UPOS-009 |
| SRC-095 | 1257 | 1 | 37. Learning promotion model | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-096 | 1290 | 1 | 38. Permissions model | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-097 | 1317 | 1 | 39. Default role permission philosophy | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-098 | 1319 | 2 | Orchestrator | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-099 | 1330 | 2 | Implementer | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-100 | 1342 | 2 | Reviewer | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-101 | 1353 | 2 | QA | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-102 | 1362 | 2 | Merge Controller | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-103 | 1374 | 1 | 40. Human approval model | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-104 | 1391 | 1 | 41. Recommended adoption mode | OUTSIDE_MODULE_05 | UPOS-010 / UPOS-002 |
| SRC-105 | 1411 | 1 | 42. Planning model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-004 |
| SRC-106 | 1434 | 1 | 43. Expected commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-107 | 1453 | 1 | 44. Git operating principles | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-108 | 1455 | 2 | 44.1 No direct push to protected main | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-109 | 1459 | 2 | 44.2 One branch per coherent task | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-110 | 1474 | 1 | 45. Atomic logical commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-111 | 1491 | 1 | 46. Bad commit granularity | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-112 | 1507 | 1 | 47. Bad oversized commit | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-113 | 1528 | 1 | 48. Commit categories | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-114 | 1548 | 1 | 49. Commit message contract | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-115 | 1566 | 1 | 50. Bug-fix commit strategy | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-116 | 1581 | 1 | 51. Review-fix commits | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-117 | 1591 | 1 | 52. PR operating model | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-118 | 1601 | 1 | 53. Good PR | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-119 | 1624 | 1 | 54. Bad PR | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-120 | 1640 | 1 | 55. PR size policy | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-004 |
| SRC-121 | 1656 | 1 | 56. PR description contract | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-122 | 1661 | 2 | Why | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-123 | 1663 | 2 | What | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-124 | 1665 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-125 | 1667 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-126 | 1669 | 2 | Risk class | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-127 | 1671 | 2 | Architecture/domain impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-128 | 1673 | 2 | API/data impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-129 | 1675 | 2 | UX/design impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-130 | 1677 | 2 | Security/privacy impact | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-131 | 1679 | 2 | Test evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-132 | 1681 | 2 | QA evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-133 | 1683 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-134 | 1685 | 2 | Rollback | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-135 | 1687 | 2 | Known limitations | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-136 | 1692 | 1 | 57. Creation loop | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-137 | 1707 | 1 | 58. Verification loop | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-138 | 1723 | 1 | 59. Self-check | OUTSIDE_MODULE_05 | UPOS-006 / UPOS-004 |
| SRC-139 | 1741 | 1 | 60. Independent review protocol | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-140 | 1758 | 1 | 61. Review finding severity | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-141 | 1778 | 1 | 62. Review output contract | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-142 | 1815 | 1 | 63. Reviewer independence | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-143 | 1831 | 1 | 64. QA protocol | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-144 | 1847 | 1 | 65. QA dimensions | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-145 | 1868 | 1 | 66. Documentation gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-146 | 1886 | 1 | 67. Architecture gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-147 | 1903 | 1 | 68. Security gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-148 | 1920 | 1 | 69. Database migration gate | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-149 | 1935 | 1 | 70. Merge readiness | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-150 | 1949 | 1 | 71. Merge authority | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-151 | 1966 | 1 | 72. Merge strategy | OUTSIDE_MODULE_05 | UPOS-007 / UPOS-006 / UPOS-010 |
| SRC-152 | 1982 | 1 | 73. Handoff protocol | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-153 | 2027 | 1 | 74. Handoff context minimization | EXTRACTED_TO_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-154 | 2042 | 1 | 75. Guardrails | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-155 | 2058 | 1 | 76. Guardrail types | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-156 | 2070 | 1 | 77. Escalation model | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-157 | 2087 | 1 | 78. Escalation targets | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-158 | 2101 | 1 | 79. Failure and recovery | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-159 | 2119 | 1 | 80. Retry policy | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-004 / UPOS-005 |
| SRC-160 | 2137 | 1 | 81. Scope Guardian | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-161 | 2158 | 1 | 82. Concurrency model | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-162 | 2182 | 1 | 83. Task isolation | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-163 | 2202 | 1 | 84. Shared file collision | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-164 | 2216 | 1 | 85. Workflow — Micro Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-165 | 2237 | 1 | 86. Workflow — Bug Fix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-166 | 2255 | 1 | 87. Workflow — New Feature | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-167 | 2276 | 1 | 88. Workflow — UI Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-168 | 2292 | 1 | 89. Workflow — Design System Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-169 | 2308 | 1 | 90. Workflow — Architecture Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-170 | 2326 | 1 | 91. Workflow — API Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-171 | 2341 | 1 | 92. Workflow — Database Migration | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-172 | 2357 | 1 | 93. Workflow — Security Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-173 | 2372 | 1 | 94. Workflow — Refactor | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-174 | 2387 | 1 | 95. Workflow — Dependency Upgrade | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-175 | 2401 | 1 | 96. Workflow — Hotfix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-176 | 2421 | 1 | 97. Workflow — Documentation Change | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-177 | 2436 | 1 | 98. Workflow — Release | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-178 | 2452 | 1 | 99. Observability model | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-179 | 2485 | 1 | 100. Dashboard-ready metrics | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-180 | 2510 | 1 | 101. Do not optimize for activity | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-181 | 2525 | 1 | 102. Quality metrics | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-182 | 2542 | 1 | 103. Agent performance | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-183 | 2559 | 1 | 104. Agent learning record | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-184 | 2583 | 1 | 105. Skill evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-185 | 2604 | 1 | 106. Workflow evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-186 | 2617 | 1 | 107. Agent contract evolution | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-187 | 2630 | 1 | 108. Model/provider independence | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-188 | 2648 | 1 | 109. Tool independence | MIXED_EXTRACTED_AND_DEFERRED | UPOS-011 |
| SRC-189 | 2665 | 1 | 110. Safety around secrets | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-190 | 2683 | 1 | 111. Production access | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-191 | 2695 | 1 | 112. Protected files | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-192 | 2711 | 1 | 113. Definition of Ready — task | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-193 | 2730 | 1 | 114. Definition of Ready — agent execution | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 / 005 / 006 / 007 |
| SRC-194 | 2746 | 1 | 115. Definition of Done — implementation | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-195 | 2760 | 1 | 116. Definition of Done — PR | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-196 | 2775 | 1 | 117. Definition of Done — workflow | OUTSIDE_MODULE_05 | UPOS-004 / 005 / 006 / 007 |
| SRC-197 | 2788 | 1 | 118. Recommended repository structure | MIXED_EXTRACTED_AND_DEFERRED | UPOS-011 / cross-cutting |
| SRC-198 | 2864 | 1 | 119. Maturity model | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-199 | 2866 | 2 | Level 0 — Single Agent | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-200 | 2870 | 2 | Level 1 — Role Profiles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-201 | 2874 | 2 | Level 2 — Governed Workflows | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-202 | 2878 | 2 | Level 3 — Orchestrated Team | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-203 | 2882 | 2 | Level 4 — Automated Verification | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-204 | 2886 | 2 | Level 5 — Controlled Autonomy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-205 | 2890 | 2 | Level 6 — Learning Organization | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-206 | 2898 | 1 | 120. Recommended adoption sequence | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-207 | 2900 | 2 | Stage 1 — Documentation foundation | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-208 | 2904 | 2 | Stage 2 — Project Agent Manifest | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-209 | 2908 | 2 | Stage 3 — Three roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-210 | 2920 | 2 | Stage 4 — Add QA and Documentation Guardian | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-211 | 2924 | 2 | Stage 5 — Add specialist agents | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-212 | 2928 | 2 | Stage 6 — Formal workflows | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-213 | 2932 | 2 | Stage 7 — Telemetry | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-214 | 2936 | 2 | Stage 8 — Limited autonomous merge | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-215 | 2942 | 1 | 121. Recommended first implementation | OUTSIDE_MODULE_05 | UPOS-011 / cross-cutting |
| SRC-216 | 2982 | 1 | 122. Universal Orchestrator algorithm | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 005 |
| SRC-217 | 3009 | 1 | 123. Authority conflict resolution | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-218 | 3028 | 1 | 124. Security veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-219 | 3038 | 1 | 125. Architecture veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-220 | 3051 | 1 | 126. Reviewer veto | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-221 | 3072 | 1 | 127. Human override | OUTSIDE_MODULE_05 | UPOS-002 / 010 |
| SRC-222 | 3091 | 1 | 128. Agent output discipline | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-223 | 3107 | 1 | 129. Change Classification output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-224 | 3137 | 1 | 130. Implementation Plan output | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-225 | 3174 | 1 | 131. Review Result output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-226 | 3206 | 1 | 132. QA Result output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-227 | 3232 | 1 | 133. Merge Readiness output | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-228 | 3252 | 1 | 134. Change review feedback loop | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-229 | 3266 | 1 | 135. Oversized PR handling | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-230 | 3281 | 1 | 136. Scope expansion handling | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-231 | 3298 | 1 | 137. Unplanned architecture discovery | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-232 | 3313 | 1 | 138. Unplanned product ambiguity | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-233 | 3327 | 1 | 139. Unplanned security concern | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-234 | 3333 | 1 | 140. Documentation drift detection | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 / 007 / 010 |
| SRC-235 | 3348 | 1 | 141. Agent sandbox hygiene | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-236 | 3368 | 1 | 142. Branch lifetime | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-237 | 3376 | 1 | 143. Stacked PRs | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-238 | 3384 | 1 | 144. Feature flags | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-239 | 3399 | 1 | 145. Rollback thinking | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-240 | 3411 | 1 | 146. Dependency graph awareness | OUTSIDE_MODULE_05 | UPOS-006 / 004 |
| SRC-241 | 3429 | 1 | 147. Cost awareness | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-242 | 3439 | 1 | 148. Latency awareness | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-243 | 3457 | 1 | 149. Human attention as scarce resource | OUTSIDE_MODULE_05 | UPOS-008 / 004 / 001 / 005 |
| SRC-244 | 3474 | 1 | 150. Agent communication rule | MIXED_EXTRACTED_AND_DEFERRED | UPOS-008 / 004 / 001 / 005 |
| SRC-245 | 3482 | 1 | 151. Decision preservation | MIXED_EXTRACTED_AND_DEFERRED | UPOS-008 / 004 / 001 / 005 |
| SRC-246 | 3499 | 1 | 152. No circular authority | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-247 | 3514 | 1 | 153. Independent model diversity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-248 | 3524 | 1 | 154. Review freshness | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-249 | 3532 | 1 | 155. Merge queue compatibility | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-250 | 3538 | 1 | 156. CI as evidence provider | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-251 | 3555 | 1 | 157. Agent-specific test ownership | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-252 | 3577 | 1 | 158. Test integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-253 | 3583 | 1 | 159. Snapshot integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-254 | 3589 | 1 | 160. Security scanner integrity | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-255 | 3595 | 1 | 161. Linter suppression | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-256 | 3601 | 1 | 162. Technical debt creation | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-257 | 3609 | 1 | 163. Technical debt review | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-258 | 3623 | 1 | 164. Post-merge verification | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-259 | 3636 | 1 | 165. Post-merge learning trigger | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-260 | 3652 | 1 | 166. Incident integration | OUTSIDE_MODULE_05 | UPOS-002 / 006 / 007 / 009 |
| SRC-261 | 3667 | 1 | 167. Dashboard model | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-262 | 3690 | 1 | 168. Agent workload | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-263 | 3709 | 1 | 169. Workflow bottleneck analysis | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-264 | 3724 | 1 | 170. Maturity gates for autonomy | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-265 | 3740 | 1 | 171. Autonomy expansion | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-266 | 3755 | 1 | 172. Project-specific overrides | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-267 | 3769 | 1 | 173. Universal vs project-specific rules | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-268 | 3791 | 1 | 174. Agent manifests should be versioned | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-269 | 3807 | 1 | 175. Governance change workflow | OUTSIDE_MODULE_05 | UPOS-002 / 009 / 010 / 011 |
| SRC-270 | 3821 | 1 | 176. Universal starter agent set | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-271 | 3846 | 1 | 177. Universal full agent set | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-272 | 3874 | 1 | 178. Agent composition | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-273 | 3896 | 1 | 179. Universal policy files | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 003 / 004 |
| SRC-274 | 3913 | 1 | 180. AI Agent README | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-275 | 3927 | 1 | 181. Compatibility with AGENTS.md / tool-specific files | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 003 / 004 |
| SRC-276 | 3944 | 1 | 182. Universal file naming | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-277 | 3963 | 1 | 183. Agent contract versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-278 | 3975 | 1 | 184. Skill versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-279 | 3981 | 1 | 185. Workflow versioning | OUTSIDE_MODULE_05 | UPOS-002 / 003 / 004 |
| SRC-280 | 3987 | 1 | 186. Telemetry retention | OUTSIDE_MODULE_05 | UPOS-008 / 010 |
| SRC-281 | 3993 | 1 | 187. Sensitive context policy | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-282 | 3999 | 1 | 188. Secret redaction | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-283 | 4005 | 1 | 189. Auditability | OUTSIDE_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-284 | 4019 | 1 | 190. Reproducibility | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-285 | 4035 | 1 | 191. Agent hallucination handling | OUTSIDE_MODULE_05 | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-286 | 4047 | 1 | 192. Missing Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-287 | 4060 | 1 | 193. Stale Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-010 / UPOS-008 / UPOS-001 |
| SRC-288 | 4072 | 1 | 194. Feature lifecycle integration | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-289 | 4080 | 1 | 195. Agent lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-290 | 4095 | 1 | 196. Task lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-291 | 4114 | 1 | 197. PR lifecycle | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-292 | 4120 | 1 | 198. Agent run lifecycle | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / 004 / 006 |
| SRC-293 | 4136 | 1 | 199. Workflow state machine | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-294 | 4142 | 1 | 200. No hidden background authority | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-295 | 4148 | 1 | 201. Human pause points | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-296 | 4162 | 1 | 202. Plan change protocol | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-297 | 4174 | 1 | 203. Reclassification | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-298 | 4184 | 1 | 204. Risk inheritance | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-299 | 4190 | 1 | 205. Change decomposition | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-300 | 4196 | 1 | 206. Multi-agent code ownership | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-301 | 4202 | 1 | 207. Shared contract first | OUTSIDE_MODULE_05 | UPOS-002 / 004 / 006 |
| SRC-302 | 4215 | 1 | 208. Reviewer context independence | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-303 | 4233 | 1 | 209. QA context independence | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-304 | 4241 | 1 | 210. Merge Controller context | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-305 | 4249 | 1 | 211. Product Owner context | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-306 | 4266 | 1 | 212. Decision packet | EXTRACTED_TO_MODULE_05 | UPOS-005 / UPOS-002 / UPOS-007 |
| SRC-307 | 4271 | 1 | Decision Required | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-308 | 4273 | 2 | Question | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-309 | 4275 | 2 | Why now | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-310 | 4277 | 2 | Option A | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-311 | 4279 | 2 | Option B | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-312 | 4281 | 2 | Trade-offs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-313 | 4283 | 2 | Risk | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-314 | 4285 | 2 | Reversibility | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-315 | 4287 | 2 | Recommended next step | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-316 | 4289 | 2 | Decision owner | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-317 | 4294 | 1 | 213. Do not fake consensus | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-318 | 4302 | 1 | 214. Conflict resolution by authority | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-319 | 4317 | 1 | 215. Majority voting | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-320 | 4323 | 1 | 216. Agent confidence | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-321 | 4331 | 1 | 217. Evidence hierarchy | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-322 | 4350 | 1 | 218. Change evidence bundle | OUTSIDE_MODULE_05 | UPOS-002 / UPOS-007 / UPOS-001 |
| SRC-323 | 4367 | 1 | 219. Artifact retention | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-008 / UPOS-010 |
| SRC-324 | 4390 | 1 | 220. Privacy of reasoning | MIXED_EXTRACTED_AND_DEFERRED | UPOS-005 / UPOS-008 / UPOS-010 |
| SRC-325 | 4398 | 1 | 221. Universal anti-patterns | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-326 | 4400 | 2 | 221.1 Agent swarm without ownership | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-327 | 4404 | 2 | 221.2 Self-approval | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-328 | 4408 | 2 | 221.3 Every task runs every agent | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-329 | 4412 | 2 | 221.4 Giant context dump | EXTRACTED_TO_MODULE_05 | Cross-cutting anti-patterns |
| SRC-330 | 4416 | 2 | 221.5 Prompt duplication | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-331 | 4420 | 2 | 221.6 Hidden project memory | EXTRACTED_TO_MODULE_05 | Cross-cutting anti-patterns |
| SRC-332 | 4424 | 2 | 221.7 Activity metrics | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-333 | 4428 | 2 | 221.8 AI-created architecture by accident | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-334 | 4432 | 2 | 221.9 Fake review | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-335 | 4436 | 2 | 221.10 Git history as keystroke log | OUTSIDE_MODULE_05 | Cross-cutting anti-patterns |
| SRC-336 | 4442 | 1 | 222. Governance health checks | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-337 | 4459 | 1 | 223. Quarterly / milestone review | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-338 | 4475 | 1 | 224. Universal adoption checklist | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting governance |
| SRC-339 | 4494 | 1 | 225. Minimal viable agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-340 | 4513 | 1 | 226. Intermediate agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-341 | 4531 | 1 | 227. Advanced agent system | OUTSIDE_MODULE_05 | Cross-cutting governance |
| SRC-342 | 4550 | 1 | 228. Final operating model | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting governance |
| SRC-343 | 4600 | 1 | Appendix A — Project Agent Manifest template | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-344 | 4603 | 1 | Project Agent Manifest | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-345 | 4608 | 2 | Project | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-346 | 4614 | 2 | Sources of Truth | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-347 | 4631 | 2 | Commands | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-348 | 4644 | 2 | Git | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-349 | 4651 | 2 | Risk-sensitive areas | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-350 | 4660 | 2 | Human approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-351 | 4668 | 2 | Protected paths | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-352 | 4672 | 2 | Agent runtime notes | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-353 | 4679 | 1 | Appendix B — Agent Contract template | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-354 | 4682 | 1 | Agent — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-355 | 4687 | 2 | Identity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-356 | 4689 | 2 | Mission | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-357 | 4691 | 2 | Owns | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-358 | 4693 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-359 | 4695 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-360 | 4697 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-361 | 4699 | 2 | Tools | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-362 | 4701 | 2 | Permissions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-363 | 4703 | 2 | Skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-364 | 4705 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-365 | 4707 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-366 | 4709 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-367 | 4711 | 2 | Quality gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-368 | 4713 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-369 | 4715 | 2 | Handoffs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-370 | 4717 | 2 | Prohibited behavior | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-371 | 4722 | 1 | Appendix C — Skill template | OUTSIDE_MODULE_05 | UPOS-003 |
| SRC-372 | 4725 | 1 | Skill — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-373 | 4730 | 2 | Purpose | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-374 | 4732 | 2 | Inputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-375 | 4734 | 2 | Preconditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-376 | 4736 | 2 | Sources | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-377 | 4738 | 2 | Procedure | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-378 | 4744 | 2 | Outputs | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-379 | 4746 | 2 | Quality criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-380 | 4748 | 2 | Failure modes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-381 | 4750 | 2 | Escalation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-382 | 4752 | 2 | Roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-383 | 4757 | 1 | Appendix D — Workflow template | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-384 | 4760 | 1 | Workflow — <Name> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-385 | 4765 | 2 | Trigger | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-386 | 4767 | 2 | Applicable risk classes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-387 | 4769 | 2 | Entry conditions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-388 | 4771 | 2 | Required roles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-389 | 4773 | 2 | Required skills | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-390 | 4775 | 2 | Required sources | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-391 | 4777 | 2 | Steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-392 | 4783 | 2 | Parallel steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-393 | 4785 | 2 | Gates | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-394 | 4787 | 2 | Human approvals | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-395 | 4789 | 2 | Failure handling | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-396 | 4791 | 2 | Completion criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-397 | 4793 | 2 | Telemetry | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-398 | 4798 | 1 | Appendix E — Change Plan template | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-399 | 4801 | 1 | Change Plan — <Task> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-400 | 4803 | 2 | Goal | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-401 | 4805 | 2 | Risk class | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-402 | 4807 | 2 | Source of Truth | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-403 | 4809 | 2 | Affected domains | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-404 | 4811 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-405 | 4813 | 2 | Non-scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-406 | 4815 | 2 | Implementation steps | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-407 | 4817 | 2 | Tests | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-408 | 4819 | 2 | Expected commits | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-409 | 4821 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-410 | 4823 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-411 | 4825 | 2 | Rollback | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-412 | 4827 | 2 | Open questions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-413 | 4832 | 1 | Appendix F — Handoff template | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-414 | 4835 | 1 | Handoff | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-415 | 4840 | 2 | Task | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-416 | 4842 | 2 | Context | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting |
| SRC-417 | 4844 | 2 | Canonical sources | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-418 | 4846 | 2 | Decisions already made | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-419 | 4848 | 2 | Constraints | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-420 | 4850 | 2 | Open questions | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-421 | 4852 | 2 | Expected output | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-422 | 4854 | 2 | Authority | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-423 | 4856 | 2 | Prohibited changes | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-424 | 4861 | 1 | Appendix G — Review Result template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-425 | 4864 | 1 | Review Result | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-426 | 4868 | 2 | Scope | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-427 | 4871 | 2 | Correctness | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-428 | 4874 | 2 | Architecture | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-429 | 4877 | 2 | Domain semantics | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-430 | 4880 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-431 | 4883 | 2 | Testing | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-432 | 4886 | 2 | UX / Accessibility | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-433 | 4889 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-434 | 4892 | 2 | Findings | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-435 | 4894 | 3 | BLOCKING | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-436 | 4896 | 3 | MAJOR | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-437 | 4898 | 3 | MINOR | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-438 | 4900 | 3 | NIT | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-439 | 4905 | 1 | Appendix H — QA Result template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-440 | 4908 | 1 | QA Result | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-441 | 4912 | 2 | Acceptance criteria | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-442 | 4914 | 2 | Scenarios executed | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-443 | 4916 | 2 | Negative scenarios | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-444 | 4918 | 2 | Regression coverage | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-445 | 4920 | 2 | Failures | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-446 | 4922 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-447 | 4924 | 2 | Residual risk | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-448 | 4929 | 1 | Appendix I — Merge Readiness template | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-449 | 4932 | 1 | Merge Readiness | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-450 | 4936 | 2 | CI | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-451 | 4938 | 2 | Review | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-452 | 4940 | 2 | QA | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-453 | 4942 | 2 | Security | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-454 | 4944 | 2 | Architecture | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-455 | 4946 | 2 | Documentation | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-456 | 4948 | 2 | Branch status | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-457 | 4950 | 2 | Human approval | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-458 | 4952 | 2 | Missing requirements | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-459 | 4957 | 1 | Appendix J — Risk Classification Matrix | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-460 | 4970 | 1 | Appendix K — Permission Matrix example | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-461 | 4985 | 1 | Appendix L — Git Policy starter | OUTSIDE_MODULE_05 | UPOS-006 |
| SRC-462 | 4988 | 1 | Git Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-463 | 4990 | 2 | Protected branches | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-464 | 4994 | 2 | Branches | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-465 | 4998 | 2 | Commits | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-466 | 5006 | 2 | Pull Requests | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-467 | 5010 | 2 | Review | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-468 | 5014 | 2 | Merge | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-469 | 5021 | 1 | Appendix M — Review Policy starter | OUTSIDE_MODULE_05 | UPOS-007 |
| SRC-470 | 5024 | 1 | Review Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-471 | 5026 | 2 | Reviewer objective | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-472 | 5030 | 2 | Severity | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-473 | 5037 | 2 | Independence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-474 | 5041 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-475 | 5048 | 1 | Appendix N — Human Approval Policy starter | OUTSIDE_MODULE_05 | UPOS-010 |
| SRC-476 | 5051 | 1 | Human Approval Policy | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-477 | 5073 | 1 | Appendix O — Example New Feature workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-478 | 5115 | 1 | Appendix P — Example Bug Fix workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-479 | 5140 | 1 | Appendix Q — Example Architecture Change workflow | OUTSIDE_MODULE_05 | UPOS-004 |
| SRC-480 | 5174 | 1 | Appendix R — Learning Record template | OUTSIDE_MODULE_05 | UPOS-009 |
| SRC-481 | 5177 | 1 | Learning — <Title> | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-482 | 5179 | 2 | Trigger | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-483 | 5181 | 2 | Evidence | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-484 | 5183 | 2 | Root cause | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-485 | 5185 | 2 | Why systemic | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-486 | 5187 | 2 | New rule | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-487 | 5189 | 2 | Updated skill | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-488 | 5191 | 2 | Updated workflow | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-489 | 5193 | 2 | New test / guardrail | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-490 | 5195 | 2 | Owner | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-491 | 5197 | 2 | Status | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-492 | 5202 | 1 | Appendix S — Telemetry schema starter | OUTSIDE_MODULE_05 | UPOS-008 |
| SRC-493 | 5229 | 1 | Appendix T — Adoption directive for an existing project | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting adoption |
| SRC-494 | 5279 | 1 | Final principles | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-495 | 5281 | 2 | 1 | OUTSIDE_MODULE_05 | UPOS-001 |
| SRC-496 | 5285 | 2 | 2 | OUTSIDE_MODULE_05 | UPOS-011 |
| SRC-497 | 5289 | 2 | 3 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-498 | 5293 | 2 | 4 | OUTSIDE_MODULE_05 | Cross-cutting |
| SRC-499 | 5297 | 2 | 5 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-500 | 5301 | 2 | 6 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-501 | 5305 | 2 | 7 | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-502 | 5309 | 2 | 8 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-503 | 5313 | 2 | 9 | OUTSIDE_MODULE_05 | UPOS-002 |
| SRC-504 | 5317 | 2 | 10 | OUTSIDE_MODULE_05 | UPOS-002 |
