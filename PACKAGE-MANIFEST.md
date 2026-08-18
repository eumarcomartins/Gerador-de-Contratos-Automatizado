# PACKAGE MANIFEST — Rota Contract Generator v1.0.0

Este manifesto descreve os ativos versionados no repositório para o produto ASSESSORIA.

## Entrada para o Codex

`CODEX_START_PROMPT.txt` — prompt curto de início.
`MASTER_PROMPT.md` — instrução completa de implementação.
`AGENTS.md` — regras persistentes do repositório.
`START-HERE.md` — mapa e ordem de leitura.
`CODEX-RUNBOOK.md` — operação do projeto no Codex.
`NEEDED-FROM-MARCO.md` — insumos necessários somente nas etapas posteriores.

## Especificação determinística

`spec/repo-manifest.json`
`spec/contract-schema.json`
`spec/derived-contract-schema.json`
`spec/form-flow.json`
`spec/rendering-rules.json`
`spec/placeholder-map.json`
`spec/business-rules.json`
`spec/validation-rules.json`
`spec/error-codes.json`
`spec/calculation-rules.json`
`spec/contract-structure.json`
`spec/workflow-state-machine.json`
`spec/contract-payload.example.json`
`spec/data-dictionary.md`

## Jurídico

`legal/clause-library.json` — biblioteca canônica e locked.
`legal/clause-hashes.json` — integridade SHA-256 dos textos jurídicos locked.
`legal/clause-library.md`
`legal/clause-matrix.json`
`legal/clause-provenance.json`
`legal/contract-variables-map.md`
`legal/legal-sources.md`
`legal/CHANGE-POLICY.md`
`legal/legal-review-checklist.md`

## Produto e UI

`product/brand-tokens.json`
`product/design-system.md`
`product/ui-requirements.md`
`product/ui-copy.md`
`product/component-inventory.json`
`product/ui-wireframe.md`
`product/contract-document-style.md`

A especificação de UI exige preview vivo persistente no desktop e modal obrigatório de revisão antes de `HUMAN_APPROVED`.

## Integrações

`integrations/api-contract.md`
`integrations/integrations.md`
`integrations/clickup-field-map.example.json`
`integrations/clickup-payload.example.json`
`integrations/zapsign-signers-map.json`
`integrations/zapsign-payload.example.json`

## Testes e gates

`tests/cases-valid.json` — casos válidos curados.
`tests/cases-invalid.json` — casos inválidos/manuais.
`tests/calculation-cases.json`
`tests/renewal-cases.json`
`tests/expected-clause-sets.json`
`tests/expected-clause-sets.md`
`tests/formatting-cases.json`
`tests/property-invariants.json`
`tests/property-generators.json`
`tests/ui-behavior-cases.json` — preview vivo, revisão, aprovação e invalidação.
`tests/coverage-matrix.csv`
`tests/test-plan.md`
`tests/pre-human-gate.md`
`tests/human-qa-scenarios.md`
`tests/human-qa-checklist.md`
`tests/human-qa-report-template.md`

Não existe diretório `tests/fixtures/` versionado nesta versão. Os casos reutilizáveis estão nos arquivos JSON acima.

## Arquitetura, segurança e governança

`docs/runtime-architecture.md`
`docs/security-requirements.md`
`docs/versioning.md`
`docs/acceptance-criteria.md`
`docs/decision-register.md`
`docs/source-provenance.md`
`docs/codex-implementation-checklist.md`
`docs/codex-usage-notes.md`
`docs/deployment-requirements.md`
`docs/non-goals.md`
`docs/release-process.md`

## Prompts por fase

`prompts/00-spec-audit.md`
`prompts/01-domain-engine.md`
`prompts/02-test-hardening.md`
`prompts/03-ui.md`
`prompts/04-renderer-pdf.md`
`prompts/05-mock-integrations.md`
`prompts/06-pre-human-gate.md`
`prompts/07-live-after-approval.md`

## Auditoria

`tools/audit_specs.py` é o auditor versionado e deve ser executado no HEAD em uso.

Além das verificações jurídicas/estruturais, o auditor confere todos os `required_assets` declarados em `spec/repo-manifest.json`.

Relatórios de auditoria e checksums do repositório inteiro são artefatos derivados e não são mantidos como fonte versionada. O Git identifica a versão integral do repositório e `legal/clause-hashes.json` protege especificamente os textos jurídicos locked.

O gate pré-humano deverá gerar `artifacts/pre-human-report.md` no momento correto.

## Materiais de origem sanitizados

`source-materials/ASS-MODEL-PF-REDACTED.md`
`source-materials/ASS-MODEL-PJ-REDACTED.md`
`source-materials/Manual-de-Marca-Rota-Juridica.txt`
`source-materials/README.md`

Contratos-modelo com dados pessoais reais de clientes não devem ser versionados.

A especificação de apresentação do contrato em `product/contract-document-style.md` foi calibrada a partir da estrutura visual dos modelos originais fornecidos, sem versionar dados pessoais reais.

## Ativo visual pendente

Logo oficial SVG/PNG. Sua ausência não bloqueia o protótipo. Até seu fornecimento, o front-end deve usar o fallback tipográfico previsto na especificação sem recriar a marca.
