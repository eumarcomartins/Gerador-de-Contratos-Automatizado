# CODEX RUNBOOK — como usar este pacote

## Opção recomendada: repositório Git + Codex

1. Extraia o ZIP.
2. Crie um repositório Git privado.
3. Faça o commit inicial dos arquivos deste pacote.
4. Abra o repositório no Codex.
5. Cole integralmente o conteúdo de `CODEX_START_PROMPT.txt`.
6. Não forneça credenciais reais na primeira execução.
7. Deixe `MOCK_MODE=true`.
8. Exija que o Codex conclua a Fase 0 antes de implementar.

O Codex deve ler `AGENTS.md` automaticamente como orientação persistente do repositório; o prompt inicial reforça a sequência de leitura.

## Primeiro checkpoint esperado do Codex

Antes de UI:
`docs/traceability-matrix.md`
`docs/implementation-plan.md`
resultado de `python tools/audit_specs.py`

Nenhum `SPEC_CONFLICT`.
Nenhum `SPEC_MISSING` que afete o MVP.

## Segundo checkpoint

Núcleo de domínio implementado.
Testes unitários e de regra verdes.
Cobertura do núcleo determinístico conforme `MASTER_PROMPT.md`.

## Terceiro checkpoint

Wizard e preview.
MOCK ClickUp.
MOCK ZapSign.
PDF.

## Quarto checkpoint

Gate automatizado completo.
`artifacts/pre-human-report.md`.

Somente então começar `tests/human-qa-scenarios.md`.

## Credenciais que serão necessárias apenas para LIVE

ClickUp API Token
ClickUp List ID
IDs reais dos Custom Fields usados na List

ZapSign API Token
Configuração/URL do webhook quando o ambiente público existir

Nunca cole esses valores em Markdown, JSON versionado ou conversa que vá para Git.
Use secrets/env do ambiente.

## Logo

O pacote contém a identidade visual, mas não contém os arquivos oficiais do logotipo.
Quando disponíveis, adicionar:
`assets/logo-horizontal.svg`
`assets/logo-mark.svg`
`assets/favicon.svg`

O protótipo não deve recriar o logo.
Até lá, usa lockup tipográfico.

## Publicação

Para homologação, use um ambiente separado de produção e mantenha MOCK ativo.
Depois que a versão humana for aprovada, configure secrets e habilite integrações reais de forma controlada.
