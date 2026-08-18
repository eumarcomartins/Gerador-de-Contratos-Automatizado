# Contract Document Style

A interface segue a identidade escura da Rota. O contrato em preview/PDF deve seguir apresentação jurídica sóbria e reproduzível, inspirada diretamente nos modelos originais de Assessoria fornecidos pela Rota.

Este arquivo controla **apresentação**, não conteúdo jurídico. O texto vem exclusivamente de `legal/clause-library.json` e das regras determinísticas.

## Princípio de fidelidade

Preview e PDF devem compartilhar a mesma árvore renderizada e os mesmos estilos-base.

A visualização A4 no front deve representar fielmente o documento que será congelado para assinatura.

Nenhum componente da UI pode alterar texto, numeração, ordem, capitalização jurídica ou conteúdo dos blocos de assinatura.

## Página

Formato: A4.

Fundo: branco.

Texto: preto.

Margens: aproximadamente **25 mm em todos os lados**, reproduzindo o modelo de origem (1418 twips ≈ 25 mm).

Quando houver header/footer técnico, manter distância aproximada de 12,5 mm da borda e conteúdo discreto.

Não usar fundos coloridos, cards, ícones ou elementos de branding dentro do corpo jurídico.

## Tipografia do contrato

Fonte-base: **Times New Roman**.

Tamanho-base: **12 pt**.

Entrelinha: **1,5**.

Cor: preto.

Corpo: alinhamento **justificado**.

O front-end continua usando Poppins/DM Sans. Essas fontes não substituem Times New Roman dentro da folha contratual.

## Título do contrato

- caixa alta;
- Times New Roman 12 pt;
- negrito;
- centralizado;
- entrelinha 1,5;
- sem edição ou abreviação pelo renderer.

Abaixo do título, pode ser mantido separador horizontal fino e neutro, coerente com o modelo original.

## Preâmbulo e qualificação

- Times New Roman 12 pt;
- justificado;
- entrelinha 1,5;
- blocos separados por respiro vertical;
- sem tabelas, cards ou colunas.

PF e PJ seguem a qualificação determinística definida nos specs.

## Considerações

Título `CONSIDERAÇÕES` em negrito.

Texto das considerações em corpo normal, justificado.

## Cláusulas

Títulos principais:
- numeração preservada;
- caixa alta conforme biblioteca;
- negrito;
- 12 pt;
- alinhamento justificado/à esquerda conforme comportamento do texto corrido.

Subcláusulas:
- numeração exatamente como renderizada pela biblioteca;
- corpo 12 pt;
- justificado;
- entrelinha 1,5.

Listas alfabéticas:
- preservar `a)`, `b)`, `c)` quando existentes;
- aplicar recuo consistente;
- não converter automaticamente para bullets gráficos.

Não acrescentar ícones, checks, caixas de destaque ou visual law no PDF desta versão, salvo decisão posterior expressa.

## Espaçamento

O modelo original usa corpo contínuo com entrelinha 1,5 e pouco espaçamento automático após parágrafos.

Implementação recomendada:
- `line-height: 1.5`;
- margem após parágrafo próxima de zero;
- respiro explícito entre blocos jurídicos principais;
- evitar páginas artificialmente longas por margens excessivas entre parágrafos.

## Quebras de página

Evitar:
- título principal de cláusula isolado no fim da página;
- linha de assinatura separada do nome/identificador correspondente;
- quebra entre papel do signatário e seus dados.

Permitir bloco completo de assinaturas em nova página quando não couber com integridade.

## Fecho

O fecho usa a data de assinatura do instrumento.

Formato:
`Uberlândia/MG, D de mês de AAAA.`

Alinhamento: **à direita**.

Manter respiro vertical antes dos blocos de assinatura.

## Blocos de assinatura

A assinatura visual deve seguir a lógica do modelo original:
1. linha de assinatura;
2. papel da parte;
3. nome;
4. CPF ou CNPJ;
5. informação de representação quando aplicável.

A linha deve ser visualmente equivalente a aproximadamente 38 caracteres de sublinhado ou a uma borda horizontal de largura consistente.

### PF

Criar **um bloco para cada contratante PF**, na mesma ordem do payload.

```text
______________________________________
Contratante
[NOME COMPLETO]
CPF n.º [CPF]
```

Todos os PFs cadastrados são signatários.

### PJ

A pessoa jurídica é a CONTRATANTE e todos os representantes cadastrados são signatários.

Criar **um bloco para cada representante**, na ordem do payload.

```text
______________________________________
Representante da Contratante
[NOME COMPLETO]
CPF n.º [CPF]
Em nome de [RAZÃO SOCIAL]
```

Não criar bloco de assinatura separado para a PJ sem pessoa física signatária.

### CONTRATADA

Criar um bloco final para a CONTRATADA:

```text
______________________________________
Contratada
MARCIEL E GONÇALVES NEGÓCIOS DIGITAIS LTDA
CNPJ n.º 35.059.080/0001-35
Representante: RODRIGO MARCIEL ELIAS
```

O bloco da CONTRATADA vem depois de todos os blocos da CONTRATANTE.

### Layout com múltiplos signatários

Prioridade: legibilidade e associação inequívoca entre linha e signatário.

No PDF:
- usar uma coluna como comportamento de segurança;
- duas colunas somente se cada bloco permanecer íntegro e a ordem de leitura ficar inequívoca;
- nunca comprimir fonte para acomodar assinaturas.

## Testemunhas

Não criar blocos de testemunhas automaticamente nesta versão.

Se futuramente houver regra expressa para testemunhas, ela deverá entrar como mudança de especificação.

## Rodapé técnico

Pode conter discretamente:
- `contract_id`;
- versão da especificação;
- número da página.

Não exibir payload completo, CPF/RG, tokens, IDs secretos ou hashes completos de integração.

## Preview incompleto

Durante o preenchimento, a folha pode exibir marcadores de interface para dados ainda pendentes.

Esses marcadores:
- não fazem parte do texto jurídico;
- devem ser visualmente distinguíveis;
- desaparecem quando o dado é preenchido;
- impedem `HUMAN_APPROVED` enquanto obrigatórios.

## PDF final

O PDF final somente pode ser produzido quando payload válido, todos os placeholders resolvidos, cláusulas/signatários corretos e revisão humana confirmada.

O PDF final não contém skeletons, marcadores de pendência ou destaque temporário do preview.
