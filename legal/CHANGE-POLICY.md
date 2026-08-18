# Política de Alteração da Biblioteca Jurídica

`legal/clause-library.json` é conteúdo locked.

## Alteração permitida somente quando

há decisão explícita da Rota para mudar uma regra/cláusula; e
a alteração é deliberada, não uma “correção automática” do Codex.

## Processo

1. identificar a cláusula `CL-*`;
2. registrar a razão da alteração;
3. alterar `clause-library.json`;
4. revisar português e coerência jurídica;
5. atualizar `clause-library.md`;
6. atualizar `clause-provenance.json`;
7. aumentar a versão da biblioteca;
8. recalcular `clause-hashes.json` de forma intencional;
9. atualizar testes afetados;
10. executar `python tools/audit_specs.py`;
11. executar suíte automatizada completa;
12. registrar a mudança no histórico/release.

## Proibido

Codex modificar uma cláusula porque “acha melhor”.
Renderer corrigir gramática em runtime.
LLM reescrever trecho locked.
Atualizar hashes automaticamente em CI após detectar divergência.
Ocultar divergência de hash.

A divergência de hash deve falhar o gate.
