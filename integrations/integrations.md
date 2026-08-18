# Integrações Externas

Verificação documental pública: 18/08/2026.

## Regra

O MVP deve funcionar integralmente em MOCK MODE.
Nenhuma credencial real é necessária para desenvolvimento, testes ou primeiro teste humano.

## ClickUp

Destino esperado:
Space: Administrativo
Folder: Jurídico
List: Cadastro

Secrets/configuração:
`CLICKUP_API_TOKEN`
`CLICKUP_LIST_ID`

Capacidades oficiais verificadas:
criar tarefa em uma List pela API;
enviar campos customizados na criação;
consultar Custom Fields disponíveis em uma List.

Endpoints de referência verificados:
`POST https://api.clickup.com/api/v2/list/{list_id}/task`
`GET https://api.clickup.com/api/v2/list/{list_id}/field`

Adapter:
`ClickUpAdapter.createContractTask(...)`

Requisitos:
server-only;
idempotência por `contract_id + render_hash`;
registrar ID retornado;
nunca logar token;
IDs reais de Custom Fields vêm de configuração;
usar `check_required_custom_fields` quando a configuração real exigir validação dos campos obrigatórios.

Antes de LIVE MODE, o Codex deve abrir novamente a documentação oficial e conferir os schemas vigentes.

## ZapSign

Secrets/configuração:
`ZAPSIGN_API_TOKEN`
`ZAPSIGN_WEBHOOK_SECRET` quando aplicável.

Capacidades oficiais verificadas:
criação de documento para assinatura a partir de arquivo;
adição/configuração de signatários;
consulta de documento/status;
webhooks de eventos de documento/assinatura.

Adapter:
`ZapSignAdapter.createDocument(...)`

Signatários:
PF => todos os contratantes.
PJ => todos os representantes.
CONTRATADA => signatário fixo configurado no servidor.

Requisitos:
upload somente do PDF final aprovado;
registrar document token/id;
registrar signer tokens/ids;
webhook idempotente;
nunca enviar documento em teste automatizado;
não transformar nomes de eventos ou payloads documentados em constantes eternas sem uma camada de adapter.

Antes de LIVE MODE, o Codex deve conferir a documentação oficial vigente da ZapSign.

## Modo LIVE

Toda chamada externa depende de:
`MOCK_MODE=false`;
credenciais presentes;
estado `HUMAN_APPROVED` alcançado;
confirmação explícita do usuário;
idempotency guard aprovado.

## Estados

A fonte de verdade é `spec/workflow-state-machine.json`.
