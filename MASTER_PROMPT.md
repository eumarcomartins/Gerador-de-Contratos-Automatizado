# MASTER PROMPT — OPENAI CODEX
## Rota Jurídica — Gerador Automático de Contratos de Assessoria

Você é o arquiteto e desenvolvedor responsável por transformar este repositório de especificação em um protótipo web funcional, testado e pronto para teste humano.

O projeto é um gerador determinístico de contratos de Assessoria da Rota Jurídica. Não é um chatbot jurídico e não é um gerador livre de texto.

## 1. OBJETIVO

Construir um ambiente online no qual um Closer:

1. preencha os dados cadastrais do contratante;
2. informe as variáveis comerciais e de escopo;
3. seja impedido de avançar em combinações inválidas;
4. visualize todas as cláusulas acionadas;
5. visualize uma prévia integral do contrato;
6. gere o contrato em formato adequado para assinatura;
7. possa criar o registro correspondente no ClickUp;
8. possa enviar o documento à ZapSign;
9. consiga executar tudo em MOCK MODE durante desenvolvimento e homologação.

O sistema deve ser utilizável por uma pessoa não técnica.

## 2. PRINCÍPIO DE ARQUITETURA

Formulário
→ Contract Schema
→ Validation Engine
→ Business Rules Engine
→ Contract Payload consolidado
→ Clause Resolver determinístico
→ Template Renderer determinístico
→ Final Validator
→ Preview
→ PDF
→ Integrações opcionais

Não use LLM no runtime para:
- escolher cláusulas;
- alterar cláusulas;
- redigir cláusulas;
- corrigir cláusulas;
- interpretar escopo;
- calcular valores;
- decidir validade de combinação;
- decidir signatários.

A IA está sendo usada agora para construir software. O software final não pode depender de interpretação de IA para compor o contrato.

## 3. FONTE DE VERDADE E PRECEDÊNCIA

Leia `START-HERE.md` e `spec/repo-manifest.json`.

A hierarquia obrigatória é:

1. `legal/clause-library.json`
2. `spec/business-rules.json`
3. `spec/validation-rules.json`
4. `spec/calculation-rules.json`
5. `spec/contract-structure.json`
6. `legal/clause-matrix.json`
7. `spec/contract-schema.json`
8. `product/ui-requirements.md`
9. `product/brand-tokens.json`
10. `integrations/*`
11. `tests/*`

Se encontrar conflito:
- não escolha silenciosamente;
- registre `SPEC_CONFLICT`;
- indique os arquivos e IDs conflitantes;
- preserve a regra de maior autoridade.

Se uma regra de negócio ou jurídica necessária estiver ausente:
- registre `SPEC_MISSING`;
- não invente.

## 4. STACK PREFERENCIAL

Use uma stack simples, moderna e adequada à publicação online:

- Next.js com App Router
- TypeScript estrito
- React
- Tailwind CSS
- Zod para schemas de runtime
- React Hook Form para o wizard
- date-fns ou equivalente para datas
- cálculo monetário integral em centavos ou biblioteca decimal segura
- Vitest para unit/integration
- Playwright para E2E
- cobertura compatível com Vitest
- geração de PDF determinística e compatível com serverless

Use versões estáveis e suportadas no momento da implementação.

Use `npm` para simplificar operação local.

Não introduza banco de dados no MVP sem necessidade. O ClickUp será o registro externo quando a integração estiver habilitada. Rascunhos podem permanecer temporariamente em estado de sessão/sessionStorage; não usar localStorage persistente por padrão para PII. Não armazenar segredos no navegador.

## 5. FASES OBRIGATÓRIAS

### Fase 0 — Auditoria da especificação
Antes de codificar:
- leia todos os arquivos;
- gere `docs/traceability-matrix.md`;
- associe cada regra `BR-*`, `VR-*`, `CR-*` e cada cláusula `CL-*` aos testes correspondentes;
- gere `docs/implementation-plan.md`;
- não altere arquivos de especificação.

### Fase 1 — Núcleo de domínio
Implemente primeiro funções puras para:
- validação de payload;
- cálculo de prazo de implantação;
- cálculo do valor total da vigência;
- cálculo do valor nominal da fidelidade;
- cálculo proporcional por mês-calendário;
- cálculo de saldo remanescente de fidelidade;
- resolução de cláusulas;
- resolução de signatários;
- geração do modelo final de contrato.

Nenhum componente React deve conter regra de negócio duplicada.

### Fase 2 — Testes do domínio antes da interface
Implemente `tests/`.

Exija 100% de cobertura de branches, functions, statements e lines dentro do núcleo determinístico que:
- valida combinações;
- calcula valores;
- resolve cláusulas;
- resolve signatários.

### Fase 3 — Interface
Implemente o wizard de `product/ui-requirements.md`.

A interface deve:
- refletir a identidade da Rota Jurídica;
- ser dark mode;
- funcionar em desktop e mobile;
- possuir progresso claro;
- mostrar validações em linguagem humana;
- impedir geração inválida;
- mostrar cláusulas acionadas;
- permitir retorno sem perda de dados;
- oferecer preview antes de qualquer integração externa;
- exigir aprovação humana explícita da minuta antes de qualquer write externo.

### Fase 4 — Renderer
O renderer:
- usa exclusivamente `legal/clause-library.json`;
- respeita `spec/contract-structure.json`;
- aplica condições de `legal/clause-matrix.json`;
- substitui placeholders deterministicamente;
- não altera texto jurídico locked;
- não deixa placeholders não resolvidos;
- preserva numeração;
- produz HTML para preview;
- produz PDF para assinatura.

Validador final deve rejeitar documento se:
- restar `{{placeholder}}`;
- houver cláusula proibida;
- faltar cláusula obrigatória;
- ordem estiver incorreta;
- signatários divergirem;
- cálculos divergirem.

### Fase 5 — Integrações em MOCK MODE
Implemente:
- `ClickUpAdapter`
- `ZapSignAdapter`

Mocks são padrão.

No mock:
- criação ClickUp retorna ID fake previsível;
- ZapSign retorna documento/signatários fake;
- nenhum tráfego externo.

Somente quando `MOCK_MODE=false` e credenciais existirem poderá haver chamada real.

### Fase 6 — Integrações reais
Implemente adapters reais conforme `integrations/`.

Nunca exponha tokens no client bundle.

ClickUp:
- criar task na List configurada;
- registrar resumo/payload conforme mapping;
- guardar ID externo.

ZapSign:
- enviar PDF aprovado;
- criar todos os signatários derivados do payload;
- nunca omitir representante PJ;
- nunca incluir signatário inexistente;
- preparar webhook idempotente.

Não envie documento real durante testes.

### Fase 7 — Gate pré-humano
Execute `tests/pre-human-gate.md`.

Se qualquer item falhar:
- não declare pronto;
- corrija;
- execute novamente.

Crie `artifacts/pre-human-report.md` contendo:
- commit/hash testado;
- comandos;
- lint;
- typecheck;
- unit;
- integração;
- E2E;
- cobertura;
- build;
- cenários válidos;
- inválidos;
- manuais;
- placeholders;
- segredos;
- pendências reais.

## 6. REGRAS DE UX

Siga `product/brand-tokens.json` e `product/ui-requirements.md`.

Não use clichês jurídicos:
- balança;
- martelo;
- colunas clássicas;
- pergaminhos.

A estética deve remeter a software B2B, tecnologia, consultoria, performance e operações.

Identidade:
- azul petróleo Rota;
- preto/cinza escuro;
- branco;
- dourado/amarelo para CTA e destaque.

Tipografia:
- Poppins para títulos;
- DM Sans para corpo.

Use fontes via web quando permitido. Não inclua binários de fonte no repositório.

O logo oficial não está neste pacote.
Até que exista:
- use "ROTA JURÍDICA" como lockup tipográfico;
- não desenhe nova marca;
- não gere isomarca aproximada;
- prepare componentes para SVG oficial.

## 7. FLUXO DO FORMULÁRIO

Comportamentos obrigatórios:
- PF e PJ mutuamente exclusivos;
- PF pode ter múltiplos contratantes;
- cada PF assina;
- PJ permite apenas uma empresa;
- PJ pode ter múltiplos representantes;
- todo representante assina;
- 4+ áreas não gera contrato automático;
- Outro canal exige especificação;
- LP Sim exige quantidade;
- Rota Academy default Sim;
- Flowjuris default Sim;
- vigência somente 3, 6 ou 12;
- fidelidade mínimo 3 e nunca maior que vigência;
- setup cobrado exige forma e data;
- assinatura e início independentes;
- faturamento não altera ciclo contratual.

## 8. QUALIDADE E TESTES

Use:
- fixtures;
- testes de combinações;
- testes de rejeição;
- propriedades/invariantes;
- snapshots apenas onde não mascararem lógica.

A suíte deve provar:
- toda combinação válida resolve cláusulas corretamente;
- inválidas são bloqueadas;
- 4+ áreas => MANUAL_CONTRACT_REQUIRED;
- OTHER exige nome;
- LP não aparece quando ausente;
- LP não é renovada;
- criativos renovam mesma quantidade;
- script de vídeo não consome slot adicional;
- Academy condiciona Consultoria;
- Flowjuris é omitido quando false;
- Flowjuris nunca possui preço individual;
- renovação nunca cria nova fidelidade;
- reajuste só pertence ao período seguinte;
- invoices não alteram vigência;
- proporcionalidade usa dias reais do mês;
- multa moratória = 10%;
- suspensão por inadimplência somente após 10 dias;
- signatários corretos.

## 9. SEGURANÇA

- `.env` no `.gitignore`;
- `.env.example` sem segredos;
- tokens somente no servidor;
- sanitizar entradas no HTML;
- revalidar payload no servidor;
- logar IDs/estados, nunca tokens;
- webhook idempotente;
- não logar contrato completo por padrão;
- mascarar CPF/RG em debug;
- minimizar persistência de dados pessoais.

## 10. CRITÉRIO DE CONCLUSÃO

Só diga "pronto para teste humano" se:
- gate pré-humano 100% aprovado;
- nenhum SPEC_MISSING relevante;
- nenhum SPEC_CONFLICT;
- zero placeholders;
- zero testes pulados;
- mocks usados nos testes;
- build de produção funcionando.

Ausência do logo ou de tokens não bloqueia o protótipo:
- logo => fallback tipográfico;
- integrações => mock mode.

Ao finalizar, apresente:
1. como rodar localmente;
2. como abrir o ambiente;
3. cenários para teste humano;
4. como ativar ClickUp;
5. como ativar ZapSign;
6. quais arquivos exigem revisão jurídica para alteração.


## 11. EXECUÇÃO CONTROLADA NO CODEX

Este repositório contém prompts auxiliares em `prompts/`.

Use-os como checkpoints de trabalho quando for vantajoso dividir a construção em sessões/fases.

Se o ambiente Codex suportar subagentes, após a implementação principal execute revisões paralelas e independentes para:
- integridade da especificação e ausência de regra inventada;
- segurança/PII/secrets;
- lacunas de testes e edge cases;
- acessibilidade e consistência visual.

Aguarde todas as revisões e consolide os achados antes do gate pré-humano.

Nunca permita que um subagente altere `legal/clause-library.json` como “correção automática”.
