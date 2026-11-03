# Verification matrix
Inspected historical release record: 2026-10-02, isolated PostgreSQL gate; 45 test files / 166 tests, 18 migrations, Next type generation, TypeScript, ESLint, build and 26/26 Playwright role/public-account journeys.

The record verifies the application build, not external provider operation or production readiness. This document does not invent names for the 26 historical cases. A named, sanitized per-case inventory remains to be exported from the original test source before describing this file as a complete journey list.

| Architectural area | Public reference coverage | Private evidence category |
|---|---|---|
| Reservation completion | Unit test | Historical integrated gate |
| Cancellation and expiry | Unit test | Historical integrated gate |
| Duplicate terminal events | Unit test | Historical integrated gate |
| Conflicting terminal events | Unit test | Historical integrated gate |
| Member / professional / admin access | Design boundary only | Historical browser matrix |
| EN/ES interface and account entry | Design boundary only | Historical browser matrix |
| Encryption and provider signatures | Design boundary only | Requires original implementation review |

Public tests are not substitutes for the 166 private tests and 26 browser journeys.
