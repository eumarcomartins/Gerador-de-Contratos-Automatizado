# Gate Pré-Humano

O Codex não pode liberar o produto sem TODOS os itens.

## Spec
[ ] `python tools/audit_specs.py` com 0 erros
[ ] clause hashes íntegros
[ ] placeholder map completo
[ ] state machine testada
[ ] todos os `required_assets` de `spec/repo-manifest.json` presentes

## Build
[ ] instalação limpa
[ ] lint
[ ] typecheck
[ ] build de produção

## Domínio
[ ] 100% statements
[ ] 100% branches
[ ] 100% functions
[ ] 100% lines
[ ] regras BR rastreadas
[ ] regras VR testadas
[ ] regras CR testadas

## Cenários
[ ] cases-valid aprovados
[ ] cases-invalid rejeitados com código esperado
[ ] formatting-cases aprovados
[ ] calculation-cases aprovados
[ ] renewal-cases aprovados
[ ] ui-behavior-cases aprovados
[ ] expected-clause-sets exatos
[ ] MANUAL_CONTRACT_REQUIRED para 4+ áreas
[ ] property tests >=1000 válidos
[ ] property tests >=1000 inválidos/mutados

## Preview vivo
[ ] preview A4 visível desde o início em desktop
[ ] preview usa o mesmo motor determinístico do documento final
[ ] cláusulas condicionais entram/saem em tempo real
[ ] valores derivados atualizam em tempo real
[ ] mudança relevante destaca temporariamente o trecho afetado
[ ] nenhum `{{PLACEHOLDER}}` bruto é mostrado ao Closer
[ ] pendências usam marcadores UI-only
[ ] mobile alterna entre Preenchimento e Contrato

## Revisão e aprovação
[ ] CTA `REVISAR E GERAR CONTRATO`
[ ] modal resume todas as decisões variáveis
[ ] checkbox obrigatório
[ ] botão Gerar contrato bloqueado sem confirmação
[ ] HUMAN_APPROVED registra payload_hash + render_hash
[ ] alteração posterior invalida aprovação
[ ] alteração posterior invalida PDF não enviado
[ ] gerar contrato não dispara ClickUp/ZapSign automaticamente

## Contrato
[ ] zero placeholders
[ ] ordem validada
[ ] cláusulas locked idênticas à biblioteca
[ ] LP condicional correta
[ ] LP não renova
[ ] criativos renovam mesma quantidade
[ ] Flowjuris sem preço individual
[ ] Academy condiciona consultoria
[ ] multa 10%
[ ] suspensão após 10 dias
[ ] aviso 30 dias
[ ] fidelidade não renova
[ ] reajuste apenas próximo período
[ ] signatários corretos

## Formatação documental
[ ] A4
[ ] margens ~25 mm
[ ] Times New Roman 12 pt
[ ] corpo justificado
[ ] entrelinha 1,5
[ ] título centralizado/negrito/caixa alta
[ ] títulos de cláusula em negrito
[ ] fecho/data alinhado à direita
[ ] um bloco por PF signatário
[ ] um bloco por representante PJ
[ ] bloco da CONTRATADA ao final
[ ] assinatura com linha + papel + nome + CPF/CNPJ
[ ] nenhum bloco de testemunha automático
[ ] PDF sem skeletons/destaques/marcadores de pendência

## Segurança
[ ] MOCK_MODE=true por padrão
[ ] nenhum segredo versionado
[ ] nenhum token no client
[ ] nenhum request real em teste
[ ] revalidação server-side
[ ] campos sanitizados
[ ] logs mascarados

## E2E
[ ] PF simples
[ ] PF múltiplo
[ ] PJ
[ ] PJ múltiplos representantes
[ ] condicionais
[ ] bloqueios
[ ] preview vivo
[ ] modal de revisão
[ ] invalidação de aprovação
[ ] PDF
[ ] mock ClickUp
[ ] mock ZapSign

## Relatório
[ ] artifacts/pre-human-report.md criado
