# UI Wireframe — referência textual

## Desktop — fluxo principal

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ ROTA JURÍDICA   Gerador de Contratos   ASSESSORIA                68% configurado   [ MOCK ]  │
└───────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────┬──────────────────────────────────────────────────────┐
│ CONFIGURAÇÃO ~42%                      │ CONTRATO EM CONSTRUÇÃO ~58%                          │
│                                        │                                                      │
│ 1 Contratante                          │ ┌──────────────────────────────────────────────────┐ │
│ 2 Escopo                               │ │                   FOLHA A4                       │ │
│ 3 Vigência                             │ │                                                  │ │
│ 4 Financeiro                           │ │ CONTRATO DE PRESTAÇÃO...                         │ │
│ 5 Revisão                              │ │                                                  │ │
│                                        │ │ Preâmbulo preenchido conforme o formulário      │ │
│ [Card da etapa atual]                  │ │                                                  │ │
│                                        │ │ 1. OBJETO DO CONTRATO                           │ │
│ Campos                                 │ │ ...                                              │ │
│ Campos condicionais                    │ │                                                  │ │
│ Validações                             │ │ [trecho alterado recebe destaque temporário]     │ │
│                                        │ │                                                  │ │
│                                        │ │ 2. ...                                           │ │
│ Voltar                    Continuar    │ └──────────────────────────────────────────────────┘ │
│                                        │     Abrir em tela cheia                            │
└────────────────────────────────────────┴──────────────────────────────────────────────────────┘
```

O preview permanece visível durante todo o wizard.

## Comportamento incremental

```text
Closer marca Landing Page = Sim
           ↓
motor determinístico recalcula
           ↓
CL-2-5-LANDING-PAGE entra
           ↓
preview rola suavemente até 2.5
           ↓
trecho recebe destaque temporário
```

Se um dado ainda não existir:

```text
Mensalidade: [não preenchida]

Preview:
┌──────────────────────────────────────┐
│ 9. PREÇO E PAGAMENTO                 │
│ [ Aguardando mensalidade ]           │
└──────────────────────────────────────┘
```

Esse marcador não pertence ao contrato final.

## Revisão

A etapa Revisão mantém o contrato visível e oferece:

```text
[DADOS] [CLÁUSULAS ACIONADAS] [CONTRATO EM TELA CHEIA]
```

Em Cláusulas acionadas, clicar em uma cláusula navega até ela no preview.

## CTA final

```text
┌────────────────────────────────────────────────────────────┐
│                  REVISAR E GERAR CONTRATO                  │
└────────────────────────────────────────────────────────────┘
```

## Modal de revisão

```text
┌─────────────────────────────────────────────────────────────────────┐
│ CONFIRA AS CONDIÇÕES DO CONTRATO                              [X]  │
├─────────────────────────────────────────────────────────────────────┤
│ Contratante              SOCIEDADE EXEMPLO DE ADVOCACIA             │
│ Signatários              ANA EXEMPLO · BRUNO EXEMPLO                │
│ Áreas                    2                                          │
│ Prazo implantação        10 dias úteis                              │
│ Canais                   Google Ads · Meta Ads                      │
│ Teto de mídia            R$ 5.000,00/mês                            │
│ Landing Pages            1 — entrega inicial                       │
│ Criativos                12 por período                             │
│ Rota Academy             Incluída                                   │
│ Flowjuris                Incluído                                   │
│ Vigência                 6 meses                                    │
│ Fidelidade               3 meses                                    │
│ Mensalidade              R$ 2.297,00                               │
│ Valor ref. vigência      R$ 13.782,00                              │
│ Setup                    Isento                                     │
│ Início                   01/09/2026                                 │
│ Primeira fatura          05/09/2026                                 │
│ Recorrência              Dia 05                                     │
├─────────────────────────────────────────────────────────────────────┤
│ [ ] Confirmo que revisei os dados e as condições acima.             │
│                                                                     │
│ [Voltar e corrigir]                             [GERAR CONTRATO]    │
└─────────────────────────────────────────────────────────────────────┘
```

`GERAR CONTRATO` fica desabilitado até checkbox + validação integral.

## Após a aprovação

```text
HUMAN_APPROVED
      ↓
PDF congelado
      ↓
[Simular/Criar no ClickUp]
      ↓
[Simular/Enviar à ZapSign]
```

Confirmar a revisão **não** envia nada externamente.

## Alteração após aprovação

```text
HUMAN_APPROVED
      ↓
Closer altera mensalidade
      ↓
aprovação invalidada
PDF anterior invalidado se ainda não enviado
novos payload_hash + render_hash
      ↓
REVISAR E GERAR CONTRATO novamente
```

Depois de write externo, alteração exige nova revisão/versão explícita.

## Mobile

```text
[ Preenchimento | Contrato ]
```

Uma coluna.
Stepper compacto.
Preview em painel próprio com zoom/scroll.
Resumo em accordion.
CTA abaixo do conteúdo.
Nenhuma tentativa de miniaturizar duas colunas lado a lado.
