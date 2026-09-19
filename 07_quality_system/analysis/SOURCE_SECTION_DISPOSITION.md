# Frozen Source Section Disposition

**ID:** UPOS-07-AN-003  
**Type:** ANALYSIS / SOURCE DISPOSITION  
**Status:** ARCHIVED  
**Normativity:** EVIDENCE  
**Owner:** UPOS-007 Implementation  
**Version:** 1.0.0  
**Lifetime:** HISTORICAL  
**Created:** 2026-09-19  
**Last reviewed:** 2026-09-19  
**Review trigger:** Re-open only if this point-in-time decomposition/audit evidence is found factually incorrect; normative changes belong in canonical Module 07 artifacts.  
**Related:** ../MODULE_07_TRACEABILITY.md

> **Historical evidence notice:** This file records the completed UPOS-007 v1.0 decomposition/implementation/audit state at freeze time. It is not timeless normative truth. Current Quality semantics are owned by canonical Module 07 normative artifacts; `MODULE_07_TRACEABILITY.md` remains the canonical coverage artifact.


**Frozen structural headings inspected:** 318  
**Directly extracted to Module 07:** 43  
**Mixed Quality sections:** 20

| Source unit | Line | Level | Section | Disposition | Remaining/deferred ownership |
|---|---:|---:|---|---|---|
| SRC-001 | 1 | 1 | Universal AI Agent Operating Model v1.0 | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-002 | 17 | 1 | 0. Executive model | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-003 | 86 | 1 | 1. Relationship to the Documentation Operating Model | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-004 | 136 | 1 | 2. Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-005 | 224 | 1 | 3. Foundational principles | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-006 | 226 | 2 | 3.1 Human governance | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-007 | 234 | 2 | 3.2 Separation of duties | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-008 | 254 | 2 | 3.3 Source of Truth before inference | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-009 | 260 | 2 | 3.4 No silent invention | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-010 | 291 | 2 | 3.5 Evidence before approval | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-011 | 313 | 2 | 3.6 Least privilege | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-012 | 319 | 2 | 3.7 Small coherent changes | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-013 | 325 | 2 | 3.8 One PR, one intention | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-014 | 331 | 2 | 3.9 One commit, one logical change | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-015 | 337 | 2 | 3.10 No opportunistic refactoring by default | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-016 | 345 | 2 | 3.11 Risk-based governance | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-017 | 353 | 2 | 3.12 Organizational learning over hidden memory | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-018 | 371 | 1 | 4. Core terminology | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-019 | 373 | 2 | Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-020 | 377 | 2 | Skill | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-021 | 391 | 2 | Workflow | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-022 | 404 | 2 | Orchestrator | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-023 | 408 | 2 | Guardrail | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-024 | 412 | 2 | Gate | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-025 | 416 | 2 | Handoff | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-026 | 420 | 2 | Project Memory | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-027 | 424 | 2 | Run | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-028 | 428 | 2 | Evidence | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-029 | 434 | 1 | 5. Universal Agent Contract | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-030 | 497 | 1 | 6. Agent identity is not enough | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-031 | 521 | 1 | 7. Universal role families | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-032 | 559 | 1 | 8. Orchestrator | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-033 | 561 | 2 | Mission | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-034 | 565 | 2 | Responsibilities | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-035 | 583 | 2 | Must not | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-036 | 594 | 1 | 9. Product Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-037 | 621 | 1 | 10. Domain / Architecture Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-038 | 648 | 1 | 11. UX / Product Design Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-039 | 671 | 1 | 12. Design System Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-040 | 689 | 1 | 13. Implementer Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-041 | 718 | 1 | 14. Reviewer Agent | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-042 | 749 | 1 | 15. QA Agent | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-043 | 773 | 1 | 16. Security Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-044 | 798 | 1 | 17. Documentation Guardian | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-045 | 821 | 1 | 18. Merge Controller | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-046 | 851 | 1 | 19. Skills model | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-047 | 870 | 1 | 20. Skill contract | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-048 | 902 | 1 | 21. Example universal skills | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-049 | 933 | 1 | 22. Workflow contract | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-050 | 954 | 1 | 23. Change classification | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-051 | 971 | 1 | 24. C0 — Micro | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-052 | 996 | 1 | 25. C1 — Small | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-053 | 1018 | 1 | 26. C2 — Standard Feature | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-054 | 1043 | 1 | 27. C3 — Cross-cutting | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-055 | 1070 | 1 | 28. C4 — Architectural | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-056 | 1097 | 1 | 29. C5 — High-risk | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-057 | 1128 | 1 | 30. Risk override rule | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-058 | 1144 | 1 | 31. Context assembly | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-059 | 1165 | 1 | 32. Context assembly order | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-060 | 1182 | 1 | 33. Context budget principle | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-061 | 1198 | 1 | 34. Memory model | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-062 | 1215 | 1 | 35. Project memory sources | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-063 | 1235 | 1 | 36. Learning is not hidden model training | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-064 | 1257 | 1 | 37. Learning promotion model | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-065 | 1290 | 1 | 38. Permissions model | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-066 | 1317 | 1 | 39. Default role permission philosophy | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-067 | 1319 | 2 | Orchestrator | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-068 | 1330 | 2 | Implementer | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-069 | 1342 | 2 | Reviewer | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-070 | 1353 | 2 | QA | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-071 | 1362 | 2 | Merge Controller | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-072 | 1374 | 1 | 40. Human approval model | MIXED_EXTRACTED_AND_DEFERRED | UPOS-010 / UPOS-002 |
| SRC-073 | 1391 | 1 | 41. Recommended adoption mode | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-074 | 1411 | 1 | 42. Planning model | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-075 | 1434 | 1 | 43. Expected commits | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-076 | 1453 | 1 | 44. Git operating principles | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-077 | 1455 | 2 | 44.1 No direct push to protected main | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-078 | 1459 | 2 | 44.2 One branch per coherent task | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-079 | 1474 | 1 | 45. Atomic logical commits | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-080 | 1491 | 1 | 46. Bad commit granularity | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-081 | 1507 | 1 | 47. Bad oversized commit | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-082 | 1528 | 1 | 48. Commit categories | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-083 | 1548 | 1 | 49. Commit message contract | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-084 | 1566 | 1 | 50. Bug-fix commit strategy | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-085 | 1581 | 1 | 51. Review-fix commits | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-086 | 1591 | 1 | 52. PR operating model | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-087 | 1601 | 1 | 53. Good PR | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-088 | 1624 | 1 | 54. Bad PR | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-089 | 1640 | 1 | 55. PR size policy | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-090 | 1656 | 1 | 56. PR description contract | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-091 | 1692 | 1 | 57. Creation loop | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-092 | 1707 | 1 | 58. Verification loop | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-093 | 1723 | 1 | 59. Self-check | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-094 | 1741 | 1 | 60. Independent review protocol | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-095 | 1758 | 1 | 61. Review finding severity | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-096 | 1778 | 1 | 62. Review output contract | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-097 | 1815 | 1 | 63. Reviewer independence | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-098 | 1831 | 1 | 64. QA protocol | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-099 | 1847 | 1 | 65. QA dimensions | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-100 | 1868 | 1 | 66. Documentation gate | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-101 | 1886 | 1 | 67. Architecture gate | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-102 | 1903 | 1 | 68. Security gate | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-103 | 1920 | 1 | 69. Database migration gate | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-104 | 1935 | 1 | 70. Merge readiness | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-105 | 1949 | 1 | 71. Merge authority | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-106 | 1966 | 1 | 72. Merge strategy | MIXED_EXTRACTED_AND_DEFERRED | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-107 | 1982 | 1 | 73. Handoff protocol | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-108 | 2027 | 1 | 74. Handoff context minimization | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-109 | 2042 | 1 | 75. Guardrails | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-110 | 2058 | 1 | 76. Guardrail types | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-111 | 2070 | 1 | 77. Escalation model | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-112 | 2087 | 1 | 78. Escalation targets | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-113 | 2101 | 1 | 79. Failure and recovery | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-114 | 2119 | 1 | 80. Retry policy | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-115 | 2137 | 1 | 81. Scope Guardian | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-116 | 2158 | 1 | 82. Concurrency model | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-117 | 2182 | 1 | 83. Task isolation | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-118 | 2202 | 1 | 84. Shared file collision | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-119 | 2216 | 1 | 85. Workflow — Micro Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-120 | 2237 | 1 | 86. Workflow — Bug Fix | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-121 | 2255 | 1 | 87. Workflow — New Feature | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-122 | 2276 | 1 | 88. Workflow — UI Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-123 | 2292 | 1 | 89. Workflow — Design System Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-124 | 2308 | 1 | 90. Workflow — Architecture Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-125 | 2326 | 1 | 91. Workflow — API Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-126 | 2341 | 1 | 92. Workflow — Database Migration | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-127 | 2357 | 1 | 93. Workflow — Security Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-128 | 2372 | 1 | 94. Workflow — Refactor | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-129 | 2387 | 1 | 95. Workflow — Dependency Upgrade | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-130 | 2401 | 1 | 96. Workflow — Hotfix | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-131 | 2421 | 1 | 97. Workflow — Documentation Change | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-132 | 2436 | 1 | 98. Workflow — Release | MIXED_EXTRACTED_AND_DEFERRED | UPOS-004 |
| SRC-133 | 2452 | 1 | 99. Observability model | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-134 | 2485 | 1 | 100. Dashboard-ready metrics | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-135 | 2510 | 1 | 101. Do not optimize for activity | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-136 | 2525 | 1 | 102. Quality metrics | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-137 | 2542 | 1 | 103. Agent performance | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-138 | 2559 | 1 | 104. Agent learning record | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-139 | 2583 | 1 | 105. Skill evolution | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-140 | 2604 | 1 | 106. Workflow evolution | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-141 | 2617 | 1 | 107. Agent contract evolution | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-142 | 2630 | 1 | 108. Model/provider independence | DEFERRED_TO_MODULE | UPOS-011 |
| SRC-143 | 2648 | 1 | 109. Tool independence | DEFERRED_TO_MODULE | UPOS-011 |
| SRC-144 | 2665 | 1 | 110. Safety around secrets | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-145 | 2683 | 1 | 111. Production access | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-146 | 2695 | 1 | 112. Protected files | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-147 | 2711 | 1 | 113. Definition of Ready — task | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-148 | 2730 | 1 | 114. Definition of Ready — agent execution | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-149 | 2746 | 1 | 115. Definition of Done — implementation | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-150 | 2760 | 1 | 116. Definition of Done — PR | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-151 | 2775 | 1 | 117. Definition of Done — workflow | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-152 | 2788 | 1 | 118. Recommended repository structure | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-153 | 2864 | 1 | 119. Maturity model | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-154 | 2866 | 2 | Level 0 — Single Agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-155 | 2870 | 2 | Level 1 — Role Profiles | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-156 | 2874 | 2 | Level 2 — Governed Workflows | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-157 | 2878 | 2 | Level 3 — Orchestrated Team | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-158 | 2882 | 2 | Level 4 — Automated Verification | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-159 | 2886 | 2 | Level 5 — Controlled Autonomy | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-160 | 2890 | 2 | Level 6 — Learning Organization | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-161 | 2898 | 1 | 120. Recommended adoption sequence | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-162 | 2900 | 2 | Stage 1 — Documentation foundation | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-163 | 2904 | 2 | Stage 2 — Project Agent Manifest | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-164 | 2908 | 2 | Stage 3 — Three roles | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-165 | 2920 | 2 | Stage 4 — Add QA and Documentation Guardian | MIXED_EXTRACTED_AND_DEFERRED | UPOS-01 |
| SRC-166 | 2924 | 2 | Stage 5 — Add specialist agents | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-167 | 2928 | 2 | Stage 6 — Formal workflows | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-168 | 2932 | 2 | Stage 7 — Telemetry | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-169 | 2936 | 2 | Stage 8 — Limited autonomous merge | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-170 | 2942 | 1 | 121. Recommended first implementation | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-171 | 2982 | 1 | 122. Universal Orchestrator algorithm | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-172 | 3009 | 1 | 123. Authority conflict resolution | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-173 | 3028 | 1 | 124. Security veto | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-174 | 3038 | 1 | 125. Architecture veto | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-175 | 3051 | 1 | 126. Reviewer veto | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-176 | 3072 | 1 | 127. Human override | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-177 | 3091 | 1 | 128. Agent output discipline | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-178 | 3107 | 1 | 129. Change Classification output | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-179 | 3137 | 1 | 130. Implementation Plan output | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-180 | 3174 | 1 | 131. Review Result output | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-181 | 3206 | 1 | 132. QA Result output | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-182 | 3232 | 1 | 133. Merge Readiness output | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-183 | 3252 | 1 | 134. Change review feedback loop | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-184 | 3266 | 1 | 135. Oversized PR handling | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-185 | 3281 | 1 | 136. Scope expansion handling | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-186 | 3298 | 1 | 137. Unplanned architecture discovery | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-187 | 3313 | 1 | 138. Unplanned product ambiguity | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-188 | 3327 | 1 | 139. Unplanned security concern | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-189 | 3333 | 1 | 140. Documentation drift detection | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-190 | 3348 | 1 | 141. Agent sandbox hygiene | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-191 | 3368 | 1 | 142. Branch lifetime | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-192 | 3376 | 1 | 143. Stacked PRs | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-193 | 3384 | 1 | 144. Feature flags | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-194 | 3399 | 1 | 145. Rollback thinking | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-195 | 3411 | 1 | 146. Dependency graph awareness | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-196 | 3429 | 1 | 147. Cost awareness | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-197 | 3439 | 1 | 148. Latency awareness | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-198 | 3457 | 1 | 149. Human attention as scarce resource | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-199 | 3474 | 1 | 150. Agent communication rule | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-200 | 3482 | 1 | 151. Decision preservation | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-201 | 3499 | 1 | 152. No circular authority | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-202 | 3514 | 1 | 153. Independent model diversity | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-203 | 3524 | 1 | 154. Review freshness | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-204 | 3532 | 1 | 155. Merge queue compatibility | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-205 | 3538 | 1 | 156. CI as evidence provider | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-206 | 3555 | 1 | 157. Agent-specific test ownership | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-207 | 3577 | 1 | 158. Test integrity | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-208 | 3583 | 1 | 159. Snapshot integrity | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-209 | 3589 | 1 | 160. Security scanner integrity | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-210 | 3595 | 1 | 161. Linter suppression | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-211 | 3601 | 1 | 162. Technical debt creation | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-212 | 3609 | 1 | 163. Technical debt review | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-213 | 3623 | 1 | 164. Post-merge verification | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-214 | 3636 | 1 | 165. Post-merge learning trigger | MIXED_EXTRACTED_AND_DEFERRED | UPOS-009 / UPOS-01 |
| SRC-215 | 3652 | 1 | 166. Incident integration | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-216 | 3667 | 1 | 167. Dashboard model | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-217 | 3690 | 1 | 168. Agent workload | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-218 | 3709 | 1 | 169. Workflow bottleneck analysis | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-219 | 3724 | 1 | 170. Maturity gates for autonomy | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-220 | 3740 | 1 | 171. Autonomy expansion | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-221 | 3755 | 1 | 172. Project-specific overrides | DEFERRED_TO_MODULE | UPOS-011 |
| SRC-222 | 3769 | 1 | 173. Universal vs project-specific rules | DEFERRED_TO_MODULE | UPOS-011 |
| SRC-223 | 3791 | 1 | 174. Agent manifests should be versioned | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-224 | 3807 | 1 | 175. Governance change workflow | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-225 | 3821 | 1 | 176. Universal starter agent set | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-226 | 3846 | 1 | 177. Universal full agent set | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-227 | 3874 | 1 | 178. Agent composition | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-228 | 3896 | 1 | 179. Universal policy files | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-229 | 3913 | 1 | 180. AI Agent README | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-230 | 3927 | 1 | 181. Compatibility with AGENTS.md / tool-specific files | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-231 | 3944 | 1 | 182. Universal file naming | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-232 | 3963 | 1 | 183. Agent contract versioning | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-233 | 3975 | 1 | 184. Skill versioning | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-234 | 3981 | 1 | 185. Workflow versioning | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-235 | 3987 | 1 | 186. Telemetry retention | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-236 | 3993 | 1 | 187. Sensitive context policy | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-237 | 3999 | 1 | 188. Secret redaction | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-238 | 4005 | 1 | 189. Auditability | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-239 | 4019 | 1 | 190. Reproducibility | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-240 | 4035 | 1 | 191. Agent hallucination handling | MIXED_EXTRACTED_AND_DEFERRED | UPOS-002 |
| SRC-241 | 4047 | 1 | 192. Missing Source of Truth | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-242 | 4060 | 1 | 193. Stale Source of Truth | DEFERRED_TO_MODULE | UPOS-01 |
| SRC-243 | 4072 | 1 | 194. Feature lifecycle integration | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-244 | 4080 | 1 | 195. Agent lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-245 | 4095 | 1 | 196. Task lifecycle | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-246 | 4114 | 1 | 197. PR lifecycle | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-247 | 4120 | 1 | 198. Agent run lifecycle | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-248 | 4136 | 1 | 199. Workflow state machine | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-249 | 4142 | 1 | 200. No hidden background authority | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-250 | 4148 | 1 | 201. Human pause points | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-251 | 4162 | 1 | 202. Plan change protocol | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-252 | 4174 | 1 | 203. Reclassification | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-253 | 4184 | 1 | 204. Risk inheritance | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-254 | 4190 | 1 | 205. Change decomposition | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-255 | 4196 | 1 | 206. Multi-agent code ownership | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-256 | 4202 | 1 | 207. Shared contract first | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-257 | 4215 | 1 | 208. Reviewer context independence | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-258 | 4233 | 1 | 209. QA context independence | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-259 | 4241 | 1 | 210. Merge Controller context | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-260 | 4249 | 1 | 211. Product Owner context | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-261 | 4266 | 1 | 212. Decision packet | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-262 | 4294 | 1 | 213. Do not fake consensus | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-263 | 4302 | 1 | 214. Conflict resolution by authority | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-264 | 4317 | 1 | 215. Majority voting | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-265 | 4323 | 1 | 216. Agent confidence | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-266 | 4331 | 1 | 217. Evidence hierarchy | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-267 | 4350 | 1 | 218. Change evidence bundle | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-268 | 4367 | 1 | 219. Artifact retention | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-269 | 4390 | 1 | 220. Privacy of reasoning | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-270 | 4398 | 1 | 221. Universal anti-patterns | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-271 | 4400 | 2 | 221.1 Agent swarm without ownership | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-272 | 4404 | 2 | 221.2 Self-approval | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-273 | 4408 | 2 | 221.3 Every task runs every agent | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-274 | 4412 | 2 | 221.4 Giant context dump | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-275 | 4416 | 2 | 221.5 Prompt duplication | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-276 | 4420 | 2 | 221.6 Hidden project memory | DEFERRED_TO_MODULE | UPOS-005 |
| SRC-277 | 4424 | 2 | 221.7 Activity metrics | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-278 | 4428 | 2 | 221.8 AI-created architecture by accident | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-279 | 4432 | 2 | 221.9 Fake review | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-280 | 4436 | 2 | 221.10 Git history as keystroke log | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-281 | 4442 | 1 | 222. Governance health checks | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-282 | 4459 | 1 | 223. Quarterly / milestone review | MIXED_EXTRACTED_AND_DEFERRED | Cross-cutting / owning module |
| SRC-283 | 4475 | 1 | 224. Universal adoption checklist | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-284 | 4494 | 1 | 225. Minimal viable agent system | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-285 | 4513 | 1 | 226. Intermediate agent system | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-286 | 4531 | 1 | 227. Advanced agent system | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-287 | 4550 | 1 | 228. Final operating model | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-288 | 4600 | 1 | Appendix A — Project Agent Manifest template | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-289 | 4679 | 1 | Appendix B — Agent Contract template | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-290 | 4722 | 1 | Appendix C — Skill template | DEFERRED_TO_MODULE | UPOS-003 |
| SRC-291 | 4757 | 1 | Appendix D — Workflow template | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-292 | 4798 | 1 | Appendix E — Change Plan template | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-293 | 4832 | 1 | Appendix F — Handoff template | DEFERRED_TO_MODULE | UPOS-002 |
| SRC-294 | 4861 | 1 | Appendix G — Review Result template | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-295 | 4905 | 1 | Appendix H — QA Result template | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-296 | 4929 | 1 | Appendix I — Merge Readiness template | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-297 | 4957 | 1 | Appendix J — Risk Classification Matrix | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-298 | 4970 | 1 | Appendix K — Permission Matrix example | DEFERRED_TO_MODULE | UPOS-010 / UPOS-002 |
| SRC-299 | 4985 | 1 | Appendix L — Git Policy starter | DEFERRED_TO_MODULE | UPOS-006 / UPOS-007 where evidence semantics apply |
| SRC-300 | 5021 | 1 | Appendix M — Review Policy starter | EXTRACTED_TO_MODULE_07 | UPOS-007 |
| SRC-301 | 5048 | 1 | Appendix N — Human Approval Policy starter | MIXED_EXTRACTED_AND_DEFERRED | UPOS-010 / UPOS-002 |
| SRC-302 | 5073 | 1 | Appendix O — Example New Feature workflow | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-303 | 5115 | 1 | Appendix P — Example Bug Fix workflow | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-304 | 5140 | 1 | Appendix Q — Example Architecture Change workflow | DEFERRED_TO_MODULE | UPOS-004 |
| SRC-305 | 5174 | 1 | Appendix R — Learning Record template | DEFERRED_TO_MODULE | UPOS-009 / UPOS-01 |
| SRC-306 | 5202 | 1 | Appendix S — Telemetry schema starter | DEFERRED_TO_MODULE | UPOS-008 |
| SRC-307 | 5229 | 1 | Appendix T — Adoption directive for an existing project | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-308 | 5279 | 1 | Final principles | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-309 | 5281 | 2 | 1 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-310 | 5285 | 2 | 2 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-311 | 5289 | 2 | 3 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-312 | 5293 | 2 | 4 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-313 | 5297 | 2 | 5 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-314 | 5301 | 2 | 6 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-315 | 5305 | 2 | 7 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-316 | 5309 | 2 | 8 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-317 | 5313 | 2 | 9 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
| SRC-318 | 5317 | 2 | 10 | OUTSIDE_MODULE_07 | Cross-cutting / owning module |
