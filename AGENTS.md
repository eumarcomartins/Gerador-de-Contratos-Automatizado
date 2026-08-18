# AGENTS.md — Rota Contract Generator

## Mission
Build a deterministic contract-generation web application for Rota Jurídica. Repository specifications are authoritative. Do not invent business, legal, financial, contractual, UI, or integration rules.

## Read first
Read START-HERE.md, spec/repo-manifest.json, all files under spec/, legal/, product/, integrations/ and tests/ before implementation.

## Non-negotiable rules
- Runtime contract composition must be deterministic.
- Never use an LLM to choose, rewrite, summarize, translate, or improvise legal clauses.
- Never alter `legal/clause-library.json` unless the user explicitly requests a legal-text change.
- Missing rule => `SPEC_MISSING`.
- Conflicting rules => `SPEC_CONFLICT`.
- 4+ areas => manual contract; never auto-generate.
- External integrations default to mocks.
- Never send real ZapSign documents or create real ClickUp tasks during automated tests.
- Money calculations must avoid binary floating-point errors.
- Internal dates use ISO `YYYY-MM-DD`; display uses pt-BR.
- Contractual cycle is based on `service_start_date`, never invoice dates.
- Secrets are server-only.

## Quality gate
Before declaring ready for human testing, pass formatting, lint, typecheck, unit, integration, E2E, build, secrets scan and the exact gate in `tests/pre-human-gate.md`. Create `artifacts/pre-human-report.md`.

## Architecture
Prefer pure domain functions and adapters. UI components cannot duplicate business rules. Maintain traceability from rule IDs to tests.
