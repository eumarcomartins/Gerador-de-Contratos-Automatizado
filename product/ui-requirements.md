# UI Requirements — Rota Contract Generator

## Objetivo
Ambiente interno para Closer gerar e revisar contratos de Assessoria com baixa fricção e alta segurança.

## Direção visual
Seguir `brand-tokens.json` e o Manual de Marca.
A interface deve parecer software B2B de operações/consultoria, não site jurídico tradicional.

Base:
- dark mode;
- azul petróleo;
- cards;
- espaço negativo generoso;
- Poppins em títulos;
- DM Sans no corpo;
- dourado somente para CTA, estado ativo e alertas estratégicos;
- ícones lineares.

## Desktop
Header compacto:
- fallback textual ROTA JURÍDICA;
- "Gerador de Contratos";
- badge "Assessoria";
- indicador MOCK/LIVE persistente.

Corpo:
- wizard principal;
- resumo lateral em tempo real;
- etapa final 50/50 entre revisão e preview.

## Mobile
Uma coluna.
Resumo em drawer/accordion.
CTA principal sem cobrir conteúdo.

## Etapa 1 — Contratante
PF ou PJ.

PF:
- quantidade de contratantes;
- preencher cada pessoa integralmente, uma por vez;
- "Contratante 1 de N".

PJ:
- dados da única PJ;
- quantidade de representantes;
- preencher cada representante integralmente, um por vez;
- badge "Signatário obrigatório".

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

Se áreas >=4:
mostrar:
"Este escopo exige elaboração manual do contrato."
Permitir salvar/copiar dados, mas não gerar automaticamente.

## Etapa 3 — Vigência
- data de assinatura;
- data de início;
- vigência 3/6/12;
- fidelidade numérica.

Helper:
"Mínimo 3 meses e nunca acima da vigência."

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
- setup.

## Etapa 5 — Revisão
Abas:
1. Dados
2. Cláusulas acionadas
3. Prévia do contrato

Cláusulas:
listar IDs e nomes; sem edição do texto.

Destaques:
- Flowjuris incluído;
- Rota Academy incluída;
- Landing Page — entrega inicial;
- Criativos — X por período.

## Etapa 6 — Geração
- Gerar PDF
- Criar no ClickUp
- Enviar à assinatura

MOCK MODE:
"Simular criação no ClickUp"
"Simular envio à ZapSign"

LIVE MODE:
confirmar antes de cada write externo.

## Validação
Erros:
- junto ao campo;
- resumo no topo;
- português simples;
- códigos internos de validation-rules.json.

Nunca apagar dados ao voltar.

## Preview
- papel A4;
- fundo branco;
- tipografia jurídica legível;
- numeração preservada;
- sem edição inline no MVP.

## Segurança visual
LIVE MODE deve ser impossível de confundir com MOCK MODE.
