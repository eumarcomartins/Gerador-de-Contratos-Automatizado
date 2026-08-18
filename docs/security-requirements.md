# Security Requirements

1. CPF, RG, endereço e e-mail têm exposição mínima.
2. Tokens ClickUp/ZapSign nunca vão ao browser.
3. Revalidar payload no servidor.
4. Sanitizar texto livre no preview HTML.
5. Não inserir HTML de usuário diretamente.
6. Não logar contrato integral em produção por padrão.
7. Mascarar CPF/RG em debug.
8. Webhooks idempotentes.
9. Ações LIVE exigem confirmação explícita.
10. Testes usam mocks.
11. `.env` nunca versionado.
12. Produzir SHA-256 de payload normalizado + versões + cláusulas selecionadas como `render_hash`.
13. Documento enviado à assinatura é imutável; alteração exige novo render/hash.
