# Human QA Scenarios — roteiro obrigatório

Executar somente depois do gate automatizado verde.

## HQA-01 — PF simples padrão
1 contratante PF; 1 área; Google Ads; sem Landing Page; 10 criativos; Rota Academy Sim; Flowjuris Sim; vigência 3; fidelidade 3; setup isento.
Validar: qualificação singular, 7 dias úteis, LP ausente, Academy/Flowjuris presentes, setup isento, um signatário cliente, nenhum placeholder.

## HQA-02 — PF múltiplos
2 contratantes PF; 2 áreas; Google + Meta; 1 Landing Page; 12 criativos; Academy Não; Flowjuris Não; vigência 6; fidelidade 4; setup no cartão.
Validar: duas qualificações, dois signatários, plural correto, 10 dias úteis, LP presente, Academy/Flowjuris ausentes, setup cartão.

## HQA-03 — PJ com dois representantes
1 PJ; 2 representantes; 3 áreas; Google + Meta + Outro; Outro = Microsoft Ads; 2 Landing Pages; 20 criativos; Academy e Flowjuris Sim; vigência 12; fidelidade 6.
Validar: uma PJ, dois representantes/signatários, outro canal nominal, 15 dias úteis, ordem integral das cláusulas.

## HQA-04 — Contrato manual
4 áreas.
Validar: MANUAL_CONTRACT_REQUIRED, geração bloqueada, ClickUp/ZapSign indisponíveis.

## HQA-05 — Datas independentes
Assinatura antes do início; primeira fatura antes ou depois do início.
Validar: fecho usa assinatura; vigência usa início; financeiro não muda vigência.

## HQA-06 — Renovação
Contrato de 6 meses com 10 criativos e 2 LPs.
Esperado: novo período 6 meses; fidelidade não renasce; criativos = 10; Landing Pages = 0.

## HQA-07 — Proporcionalidade
Mensalidade R$ 3.000; mês de 30 dias; 12 dias de serviço. Esperado R$ 1.200. Repetir fevereiro bissexto e mês de 31 dias.

## HQA-08 — Segurança LIVE
Sem credenciais: LIVE indisponível. Em MOCK: nenhum request externo. Em LIVE posterior: confirmação explícita e tokens ausentes de browser/log.
