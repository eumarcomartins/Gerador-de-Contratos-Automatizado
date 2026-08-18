# Human QA Scenarios — roteiro obrigatório

Executar somente depois do gate automatizado verde.

## HQA-01 — PF simples padrão

1 contratante PF; 1 área; Google Ads; sem Landing Page; 10 criativos; Rota Academy Sim; Flowjuris Sim; vigência 3; fidelidade 3; setup isento.

Validar: qualificação singular; 7 dias úteis; LP ausente; Academy/Flowjuris presentes; setup isento; um signatário cliente; nenhum placeholder; bloco final de assinatura com linha, papel, nome e CPF.

## HQA-02 — PF múltiplos

2 contratantes PF; 2 áreas; Google + Meta; 1 Landing Page; 12 criativos; Academy Não; Flowjuris Não; vigência 6; fidelidade 4; setup no cartão.

Validar: duas qualificações; dois blocos de assinatura PF; ordem dos signatários igual ao payload; plural correto; 10 dias úteis; LP presente; Academy/Flowjuris ausentes; setup cartão.

## HQA-03 — PJ com dois representantes

1 PJ; 2 representantes; 3 áreas; Google + Meta + Outro; Outro = Microsoft Ads; 2 Landing Pages; 20 criativos; Academy e Flowjuris Sim; vigência 12; fidelidade 6.

Validar: uma PJ; dois representantes/signatários; dois blocos de representante da Contratante; nenhum bloco de PJ sem pessoa física; outro canal nominal; 15 dias úteis; ordem integral das cláusulas.

## HQA-04 — Contrato manual

4 áreas.

Validar: MANUAL_CONTRACT_REQUIRED; geração bloqueada; ClickUp/ZapSign indisponíveis; dados preenchidos preservados.

## HQA-05 — Datas independentes

Assinatura antes do início; primeira fatura antes ou depois do início.

Validar: fecho usa assinatura; vigência usa início; financeiro não muda vigência; data do fecho aparece alinhada à direita.

## HQA-06 — Renovação

Contrato de 6 meses com 10 criativos e 2 LPs.

Esperado: novo período 6 meses; fidelidade não renasce; criativos = 10; Landing Pages = 0.

## HQA-07 — Proporcionalidade

Mensalidade R$ 3.000; mês de 30 dias; 12 dias de serviço.

Esperado: R$ 1.200.

Repetir fevereiro bissexto e mês de 31 dias.

## HQA-08 — Segurança LIVE

Sem credenciais: LIVE indisponível.

Em MOCK: nenhum request externo.

Em LIVE posterior: confirmação explícita; tokens ausentes de browser/log.

## HQA-09 — Contrato montado ao vivo

Começar novo contrato e preencher devagar:
1. Contratante;
2. 1 área;
3. trocar para 3 áreas;
4. marcar Landing Page;
5. desmarcar Flowjuris;
6. alterar mensalidade.

Validar:
- A4 permanece visível ao lado no desktop;
- contrato aparece desde o início;
- prazo muda de 7 para 15 dias úteis;
- LP entra em tempo real;
- Flowjuris desaparece;
- mensalidade atualiza;
- trecho alterado recebe destaque transitório;
- nenhum placeholder bruto aparece;
- valores pendentes aparecem apenas como marcador visual de interface.

## HQA-10 — Modal de revisão

Com contrato integralmente válido, clicar `REVISAR E GERAR CONTRATO`.

Validar que o modal mostra contratante/signatários; áreas e prazo; canais e teto; LP; criativos; Academy; Flowjuris; datas; vigência/fidelidade; mensalidade; total de referência; cobrança; setup.

Sem marcar o checkbox: Gerar contrato desabilitado.

Após marcar: habilitado.

Confirmar: HUMAN_APPROVED e nenhum ClickUp/ZapSign disparado automaticamente.

## HQA-11 — Alteração depois da aprovação

Após HQA-10, antes de qualquer write externo, alterar a mensalidade.

Validar:
- aprovação anterior deixa de valer;
- PDF não enviado é invalidado;
- preview atualiza;
- sistema exige nova revisão;
- hashes mudam;
- não existe possibilidade de enviar silenciosamente a versão anterior.

## HQA-12 — Fidelidade visual do documento

Gerar contrato final PF e PJ.

Validar visualmente:
- A4;
- margens aproximadamente 25 mm;
- Times New Roman 12 pt;
- corpo justificado;
- entrelinha 1,5;
- título centralizado/negrito/caixa alta;
- títulos de cláusula em negrito;
- data alinhada à direita;
- assinatura conforme modelo;
- CONTRATADA depois dos signatários clientes;
- nenhum skeleton, badge, cor de destaque da UI ou marcador pendente no PDF.
