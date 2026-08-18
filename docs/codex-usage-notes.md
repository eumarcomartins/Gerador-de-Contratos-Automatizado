# Codex Usage Notes

## AGENTS.md

O repositório contém `AGENTS.md` na raiz para manter instruções persistentes do projeto.

## Como trabalhar

Criar checkpoint Git antes de mudanças grandes.
Trabalhar por fases.
Executar testes após cada fase.
Manter instruções de “done” verificáveis.
Não depender de uma única conversa longa: os arquivos do repositório são a memória durável do projeto.

## Cloud

Se usar Codex cloud, configurar ambiente do repositório e secrets somente quando chegar a hora do LIVE.
O primeiro ciclo deve funcionar sem secrets externos.

## Revisão

Após concluir implementação, realizar revisão separada de:
segurança;
aderência à especificação;
testes;
UI/acessibilidade.

Se subagentes estiverem disponíveis, podem ser usados para essas revisões independentes, aguardando todos antes da consolidação.
