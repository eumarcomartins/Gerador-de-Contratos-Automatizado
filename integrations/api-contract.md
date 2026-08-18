# Integration Contract — Mock First

## Regra absoluta

O protótipo deve funcionar integralmente sem ClickUp e sem ZapSign reais.

`MOCK_MODE=true` é o padrão.

Nenhum teste automatizado pode executar write externo.

## ClickUpAdapter

Interface conceitual:

```ts
interface ClickUpAdapter {
  createContractTask(input: ClickUpContractTaskInput): Promise<ClickUpContractTaskResult>
}
```

Entrada mínima:
contractId
clientDisplayName
product
payloadSummary
payloadJson
renderHash
specVersion
clauseLibraryVersion
generationMode

Saída:
externalTaskId
externalTaskUrl quando disponível
createdAt
mode MOCK | LIVE

Live:
criar a tarefa na List configurada por `CLICKUP_LIST_ID`.
usar credencial somente no servidor.
mapear Custom Fields por `clickup-field-map.example.json`.
antes de habilitar LIVE, descobrir/validar os IDs reais dos Custom Fields e substituir o arquivo exemplo por configuração local/segura.

## ZapSignAdapter

Interface conceitual:

```ts
interface ZapSignAdapter {
  createDocument(input: ZapSignDocumentInput): Promise<ZapSignDocumentResult>
}
```

Entrada mínima:
contractId
documentFile
documentHash
signers
signatureDate
clientDisplayName

Saída:
externalDocumentId
signers
status
createdAt
mode MOCK | LIVE

Regras:
o arquivo enviado é o PDF final já aprovado;
o adapter não pode alterar cláusulas;
PF: um signatário por contratante;
PJ: um signatário por representante;
representante da CONTRATADA conforme configuração interna;
webhooks devem ser idempotentes;
persistir IDs externos e status, nunca token.

## Idempotência

Use `contractId + renderHash` como chave lógica para impedir envio duplicado acidental.

Quando uma mesma combinação já tiver sido enviada:
bloquear novo write por padrão;
permitir nova versão somente mediante ação explícita de regeneração/versionamento.

## Confirmação LIVE

Antes de cada write externo em modo LIVE, a UI deve exibir:
destino;
nome do cliente;
número de signatários;
hash/versão;
ação que será realizada.

Exigir confirmação explícita.
