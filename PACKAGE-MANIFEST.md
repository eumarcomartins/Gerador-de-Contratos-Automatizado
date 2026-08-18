# PACKAGE MANIFEST — Rota Contract Generator v1.0.0

## Entrada para o Codex

`CODEX_START_PROMPT.txt` — texto curto para colar na primeira conversa.
`MASTER_PROMPT.md` — instrução detalhada de implementação.
`AGENTS.md` — regras persistentes do repositório.
`START-HERE.md` — mapa inicial.
`CODEX-RUNBOOK.md` — instruções para Marco operar o pacote.

## Especificação determinística

`spec/contract-schema.json` — input oficial.
`spec/derived-contract-schema.json` — output derivado.
`spec/form-flow.json` — ordem/visibilidade dos campos.
`spec/rendering-rules.json` — gramática, plural, datas, dinheiro, assinaturas.
`spec/business-rules.json` — regras de negócio.
`spec/validation-rules.json` — bloqueios/erros.
`spec/error-codes.json` — catálogo de erros.
`spec/calculation-rules.json` — fórmulas.
`spec/contract-structure.json` — ordem fixa das cláusulas.
`spec/contract-payload.example.json` — exemplo de input + derivados.
`spec/data-dictionary.md` — dicionário humano.

## Jurídico

`legal/clause-library.json` — biblioteca canônica e locked.
`legal/clause-library.md` — leitura humana da biblioteca.
`legal/clause-matrix.json` — acionamento.
`legal/clause-provenance.json` — origem/base de cada cláusula.
`legal/contract-variables-map.md` — mapeamento textual.
`legal/legal-sources.md` — fontes oficiais.

## Produto/UI

`product/brand-tokens.json` — tokens da identidade Rota.
`product/design-system.md` — aplicação visual.
`product/ui-requirements.md` — requisitos de tela.
`product/ui-copy.md` — textos de interface.

## Integrações

`integrations/api-contract.md` — contratos de adapters.
`integrations/integrations.md` — requisitos gerais.
`integrations/clickup-field-map.example.json` — mapeamento base.
`integrations/clickup-payload.example.json` — payload exemplo.
`integrations/zapsign-signers-map.json` — regra de signatários.
`integrations/zapsign-payload.example.json` — payload exemplo.

## Testes

`tests/cases-valid.json` — cenários válidos.
`tests/cases-invalid.json` — cenários inválidos/manuais.
`tests/expected-clause-sets.json` — oráculo de cláusulas.
`tests/formatting-cases.json` — português/renderização.
`tests/property-invariants.json` — invariantes.
`tests/coverage-matrix.csv` — mapa inicial regra→teste.
`tests/test-plan.md` — estratégia.
`tests/pre-human-gate.md` — gate obrigatório.
`tests/human-qa-scenarios.md` — roteiro humano.
`tests/human-qa-checklist.md` — checklist humano.
`tests/fixtures/` — cargas reutilizáveis.

## Segurança, arquitetura e governança

`docs/runtime-architecture.md`
`docs/security-requirements.md`
`docs/versioning.md`
`docs/acceptance-criteria.md`
`docs/decision-register.md`
`docs/source-provenance.md`
`docs/codex-implementation-checklist.md`

## Auditoria

`tools/audit_specs.py` — linter/auditor do pacote.
`audit/spec-audit-report.md` — resultado executado antes da entrega.
`checksums.sha256` — hashes dos ativos.

## Materiais de origem

`source-materials/[ASS] [MODEL] [PF].md`
`source-materials/[ASS] [MODEL] [PJ].md`
`source-materials/Manual-de-Marca-Rota-Juridica.txt`

## Ativo ainda necessário

Logo oficial SVG/PNG. Sua ausência não bloqueia o protótipo; o sistema deve usar fallback tipográfico sem tentar recriar a marca.

## Prompts por fase

`prompts/00-spec-audit.md`
`prompts/01-domain-engine.md`
`prompts/02-test-hardening.md`
`prompts/03-ui.md`
`prompts/04-renderer-pdf.md`
`prompts/05-mock-integrations.md`
`prompts/06-pre-human-gate.md`
`prompts/07-live-after-approval.md`

## Workflow e implantação

`spec/workflow-state-machine.json`
`product/contract-document-style.md`
`docs/deployment-requirements.md`
`docs/non-goals.md`

## Controle de mudança e produção

`legal/CHANGE-POLICY.md`
`legal/legal-review-checklist.md`
`docs/release-process.md`
`docs/codex-usage-notes.md`

## UI e homologação

`product/component-inventory.json`
`product/ui-wireframe.md`
`tests/human-qa-report-template.md`
`NEEDED-FROM-MARCO.md`
