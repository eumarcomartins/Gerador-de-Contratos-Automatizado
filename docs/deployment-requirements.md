# Deployment & Environment Requirements

## Ambientes

LOCAL
STAGING
PRODUCTION

## Regra de exposição

O protótipo contém dados pessoais e contratuais.
Não publicar um ambiente acessível anonimamente na internet.

Em STAGING, usar proteção de acesso fornecida pela plataforma de hospedagem ou mecanismo equivalente.
Em PRODUCTION, exigir autenticação compatível com o ambiente interno da empresa antes de disponibilizar a ferramenta a usuários reais.

## MOCK/LIVE

LOCAL: MOCK por padrão.
STAGING: MOCK por padrão.
PRODUCTION: LIVE somente após homologação.

O modo deve ser exibido de forma persistente na UI.

## Dados locais

No MVP, evitar persistência de rascunhos em banco.
Preferir estado de sessão/sessionStorage para conveniência temporária.
Fornecer ação “Limpar dados desta minuta”.
Não persistir CPF/RG indefinidamente no navegador.

## Secrets

Somente no ambiente server-side.
Nunca usar prefixo de variável que exponha token ao bundle do navegador.
Nunca versionar `.env`.

## Observabilidade

Logs técnicos:
contract_id;
estado do workflow;
IDs externos;
timestamps;
erros sanitizados;
hash da versão.

Não registrar por padrão:
CPF completo;
RG completo;
contrato integral;
tokens;
payload integral com PII.

## Backups

A especificação/versionamento fica no Git.
Documentos assinados e registros operacionais seguem as políticas das plataformas integradas e as definições futuras de armazenamento da Rota.
