# UI Requirements — Rota Contract Generator

## Objetivo

Ambiente interno para o Closer configurar, revisar e gerar contratos de Assessoria com baixa fricção, alta segurança e compreensão imediata do efeito contratual de cada escolha.

A interface não é apenas um formulário. Ela deve funcionar como um **construtor visual de contrato em tempo real**.

## Direção visual

Seguir `brand-tokens.json` e o Manual de Marca.

A interface deve parecer software B2B de operações, consultoria, performance e tecnologia — não site jurídico tradicional.

Base:
- dark mode;
- azul petróleo;
- cards;
- espaço negativo generoso;
- Poppins em títulos;
- DM Sans no corpo;
- dourado somente para CTA, estado ativo, progresso e alertas estratégicos;
- ícones lineares;
- nada de balança, martelo, colunas ou pergaminhos.

## Arquitetura principal — Desktop

Header compacto:
- fallback textual ROTA JURÍDICA;
- "Gerador de Contratos";
- badge "Assessoria";
- indicador MOCK/LIVE persistente.

Corpo principal em duas colunas persistentes.

### Coluna esquerda — Configuração

Largura alvo aproximada: 40% a 45%.

Contém:
- wizard;
- campos da etapa;
- validações;
- helpers;
- navegação Voltar/Continuar;
- resumo compacto de valores derivados quando pertinente.

### Coluna direita — Contrato em construção

Largura alvo aproximada: 55% a 60%.

Contém:
- folha A4 branca;
- contrato integral renderizado pelo motor determinístico;
- rolagem própria;
- indicação "Contrato em construção";
- progresso de configuração;
- botão para abrir preview em tela cheia;
- destaque transitório do trecho afetado pela última decisão do Closer.

O preview deve permanecer visível durante todas as etapas do formulário em desktop, não apenas na etapa final.

## Preview vivo

Toda alteração relevante no formulário deve percorrer o mesmo pipeline determinístico do documento final:

estado do formulário → normalização parcial → validação disponível → regras aplicáveis → cláusulas resolvíveis → placeholders resolvíveis → preview parcial.

O preview não pode possuir um segundo conjunto de regras implementado na UI.

O preview parcial deve:
- incluir apenas cláusulas cuja condição já possa ser determinada;
- atualizar automaticamente cláusulas condicionais;
- atualizar valores, datas e quantidades imediatamente quando válidos;
- não inventar valores para campos ainda não preenchidos;
- nunca exibir `{{PLACEHOLDER}}` ao Closer.

Quando uma informação necessária ainda não estiver disponível, usar marcador visual de interface, fora do texto jurídico definitivo, como "Aguardando mensalidade", "Aguardando data de início" ou skeleton discreto.

Esses marcadores não podem fazer parte do HTML/PDF final do contrato.

### Destaque de mudança

Quando uma resposta adiciona/remove cláusula, altera prazo, valor, signatário ou placeholder preenchido, o trecho afetado deve receber destaque visual discreto por aproximadamente 1,5 a 3 segundos e, quando possível, ser trazido para a área visível do preview sem deslocamento agressivo.

O destaque pertence apenas à interface e nunca ao PDF.

Exemplos:
- Flowjuris Sim → cláusula aparece e é destacada;
- Flowjuris Não → cláusula desaparece;
- 3 áreas → prazo passa para 15 dias úteis;
- Landing Page Sim → cláusula de LP entra;
- alteração da mensalidade → cláusula financeira é atualizada.

## Progresso da configuração

Mostrar no topo do preview percentual de configuração e grupos completos/pendentes, por exemplo:
- ✓ Contratante
- ✓ Escopo
- ○ Vigência
- ○ Financeiro

O percentual mede somente preenchimento/validade dos campos necessários, nunca qualidade jurídica.

## Mobile e telas estreitas

Uma coluna.

Usar alternância:
- Preenchimento
- Contrato

O formulário permanece o fluxo principal. O preview abre em painel dedicado com zoom e rolagem. Não tentar exibir formulário e A4 lado a lado em largura insuficiente.

## Etapa 1 — Contratante

PF ou PJ.

PF:
- quantidade de contratantes;
- preencher cada pessoa integralmente, uma por vez;
- "Contratante 1 de N";
- cada PF deve aparecer também no bloco de assinatura do preview assim que seus dados mínimos estiverem válidos.

PJ:
- dados da única PJ;
- quantidade de representantes;
- preencher cada representante integralmente, uma por vez;
- badge "Signatário obrigatório";
- cada representante deve aparecer no bloco de assinatura do preview.

## Etapa 2 — Escopo

- quantidade de áreas;
- canais de mídia;
- Outro abre texto obrigatório;
- teto mensal;
- LP Sim/Não;
- quantidade de LP se Sim;
- quantidade total de criativos;
- Rota Academy default Sim;
- Flowjuris default Sim.

Se áreas >=4, mostrar "Este escopo exige elaboração manual do contrato." Permitir preservar/copiar dados preenchidos, mas bloquear geração automática.

## Etapa 3 — Vigência

- data de assinatura;
- data de início;
- vigência 3/6/12;
- fidelidade numérica.

Helper: "Mínimo de 3 meses e nunca acima da vigência."

## Etapa 4 — Financeiro

- mensalidade;
- forma de pagamento;
- primeira fatura;
- dia recorrente;
- setup Cobrado/Isento;
- se Cobrado: forma e data.

Mostrar:
- valor total de referência da vigência;
- valor nominal da fidelidade;
- setup;
- prazo de implantação derivado.

## Etapa 5 — Revisão

A revisão não substitui o preview vivo. Ela é o gate formal antes de congelar a minuta.

Disponibilizar:
1. Dados;
2. Cláusulas acionadas;
3. Contrato integral em tela cheia.

Em Cláusulas acionadas, listar IDs e nomes sem edição e permitir navegar até o trecho correspondente no preview.

Destaques de negócio:
- Flowjuris incluído/omitido;
- Rota Academy incluída/omitida;
- Landing Pages — entrega inicial;
- Criativos — X por período;
- prazo de implantação;
- teto de mídia;
- vigência/fidelidade;
- mensalidade/setup.

## Modal obrigatório — Revisar e gerar contrato

O CTA principal antes da geração deve ser **REVISAR E GERAR CONTRATO**.

Ao clicar, abrir modal amplo de revisão com todas as decisões variáveis relevantes.

O modal deve apresentar, no mínimo:
- tipo e nome do contratante;
- PFs ou representantes que assinarão;
- quantidade de áreas;
- prazo de implantação;
- canais de mídia;
- teto mensal de mídia;
- Landing Pages incluídas e quantidade;
- quantidade de criativos por período;
- Rota Academy;
- Flowjuris;
- data de assinatura;
- data de início;
- vigência;
- fidelidade;
- mensalidade;
- valor total de referência da vigência inicial;
- forma de pagamento;
- primeira fatura;
- vencimento recorrente;
- setup;
- forma/data do setup quando cobrado.

Valores condicionais ausentes devem aparecer como "Não incluído" ou "Não aplicável", nunca ser omitidos de forma ambígua.

Ao final:

`[ ] Confirmo que revisei os dados e as condições acima.`

O botão **GERAR CONTRATO** permanece desabilitado até payload válido, contrato integral renderizado sem erro e checkbox marcado.

## Snapshot de aprovação

No momento da confirmação:
- calcular/registrar `payload_hash`;
- calcular/registrar `render_hash`;
- associar ambos à aprovação;
- registrar timestamp técnico;
- transicionar para `HUMAN_APPROVED`.

A aprovação vale apenas para aquela combinação exata de payload + documento renderizado.

Se qualquer campo que afete contrato, signatários, cálculo ou conteúdo for alterado depois:
- invalidar imediatamente a aprovação;
- invalidar PDF ainda não enviado;
- remover estado `HUMAN_APPROVED`;
- exigir nova revisão no modal;
- gerar novos hashes.

Depois de um write externo, alterações não podem modificar silenciosamente o documento já registrado/enviado. Mudança posterior exige fluxo explícito de nova revisão/versão.

## Geração e integrações

Após `HUMAN_APPROVED`:
1. gerar/congelar PDF;
2. permitir criação/simulação no ClickUp;
3. preparar signatários;
4. permitir envio/simulação à ZapSign.

MOCK MODE:
- "Simular criação no ClickUp";
- "Simular envio à ZapSign".

LIVE MODE:
- confirmar antes de cada write externo;
- exibir destino e documento/hashes;
- nunca enviar automaticamente ao confirmar o modal de geração.

O botão "Gerar contrato" gera/congela o documento. Ele não deve, por si só, criar tarefa ou enviar para assinatura.

## Validação

Erros:
- junto ao campo;
- resumo no topo quando necessário;
- português simples;
- códigos internos de `validation-rules.json`.

Nunca apagar dados ao voltar.

## Preview/PDF

- papel A4;
- fundo branco;
- fidelidade visual ao documento final;
- numeração preservada;
- sem edição inline;
- formatação definida em `contract-document-style.md`.

## Segurança visual

LIVE MODE deve ser impossível de confundir com MOCK MODE. Ações externas permanecem indisponíveis antes de `HUMAN_APPROVED`.
