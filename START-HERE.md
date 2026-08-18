# Rota Contract Generator — START HERE

Pacote de especificação para prototipação do Gerador de Contratos de Assessoria da Rota Jurídica no OpenAI Codex.

Versão da especificação: 1.0.0
Data de consolidação: 18/08/2026
Produto coberto: ASSESSORIA

## Como usar no Codex

1. Descompacte este repositório em uma pasta própria.
2. Inicialize Git antes de começar.
3. Abra a pasta raiz no Codex.
4. O Codex lerá automaticamente `AGENTS.md`.
5. Na primeira tarefa, cole o conteúdo de `CODEX_START_PROMPT.txt`; ele direcionará o Codex ao `MASTER_PROMPT.md` e aos demais ativos.
6. Não forneça tokens reais de ClickUp ou ZapSign no primeiro ciclo.
7. O protótipo deve rodar em `MOCK_MODE=true` até passar pelo gate automatizado e pelo teste humano.
8. Só depois configure as credenciais reais descritas em `.env.example`.

## Fonte de verdade

1. `legal/clause-library.json`
2. `spec/business-rules.json`
3. `spec/validation-rules.json`
4. `spec/calculation-rules.json`
5. `spec/contract-structure.json`
6. `legal/clause-matrix.json`
7. `spec/contract-schema.json`
8. `spec/rendering-rules.json`
9. `spec/placeholder-map.json`
10. `spec/form-flow.json`
11. `spec/workflow-state-machine.json`
12. `product/ui-requirements.md`
13. `product/brand-tokens.json`
14. `integrations/*`
15. `tests/*`

Se houver conflito, registrar `SPEC_CONFLICT` e obedecer ao arquivo de maior autoridade.

## Regra central

A IA não decide conteúdo jurídico em runtime.

Formulário → Validação → Regras → Contract Payload → Clause Resolver → Renderer → Validação final → Preview/PDF.

O runtime não pode reescrever, resumir, melhorar ou reinterpretar cláusulas.

## Ativo visual pendente

O Manual de Marca foi incorporado aos tokens visuais.

O arquivo oficial do logotipo não foi localizado. Antes de publicar, adicionar preferencialmente:

`assets/logo-horizontal.svg`
`assets/logo-mark.svg`
`assets/favicon.svg`

Enquanto estiverem ausentes, usar apenas o nome tipográfico "ROTA JURÍDICA", sem inventar ou redesenhar a marca.
