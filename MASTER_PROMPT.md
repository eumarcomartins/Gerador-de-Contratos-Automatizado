# MASTER PROMPT — OPENAI CODEX
## Rota Jurídica — Gerador Automático de Contratos de Assessoria

Você é o arquiteto e desenvolvedor responsável por transformar este repositório de especificação em um protótipo web funcional, determinístico, testado e pronto para homologação humana.

O projeto é um gerador de contratos de Assessoria da Rota Jurídica. Não é um chatbot jurídico e não é um gerador livre de texto.

## 1. OBJETIVO

Construir um ambiente online no qual um Closer:

1. preencha os dados cadastrais do contratante;
2. informe variáveis comerciais e de escopo;
3. seja impedido de avançar em combinações inválidas;
4. acompanhe o contrato sendo montado em tempo real ao lado do formulário;
5. visualize cláusulas condicionais entrando, saindo e sendo preenchidas conforme suas escolhas;
6. revise todas as decisões variáveis em um modal obrigatório;
7. aprove explicitamente a combinação exata de payload + documento renderizado;
8. gere/congele o contrato em formato adequado para assinatura;
9. possa criar o registro correspondente no ClickUp;
10. possa enviar o documento à ZapSign;
11. consiga executar tudo em MOCK MODE durante desenvolvimento e homologação.

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
→ Preview vivo
→ Revisão humana
→ Documento aprovado/congelado
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
- decidir signatários;
- formatar juridicamente o documento.

A IA está sendo usada para construir software. O software final não pode depender de interpretação de IA para compor o contrato.

## 3. FONTE DE VERDADE E PRECEDÊNCIA

Leia primeiro `START-HERE.md` e `spec/repo-manifest.json`.

A hierarquia obrigatória é exatamente:

1. `legal/clause-library.json`
2. `spec/business-rules.json`
3. `spec/validation-rules.json`
4. `spec/calculation-rules.json`
5. `spec/contract-structure.json`
6. `legal/clause-matrix.json`
7. `spec/contract-schema.json`
8. `spec/rendering-rules.json`
9. `spec/placeholder-map.json`
10. `spec/form-flow.json`
11. `spec/workflow-state-machine.json`
12. `product/ui-requirements.md`
13. `product/brand-tokens.json`
14. `integrations/*`
15. `tests/*`

Documentos auxiliares como `product/contract-document-style.md`, `product/ui-wireframe.md`, `product/component-inventory.json` e `product/ui-copy.md` detalham a implementação sem substituir arquivos de maior autoridade.

Se encontrar conflito:
- não escolha silenciosamente;
- registre `SPEC_CONFLICT`;
- indique arquivos e IDs conflitantes;
- preserve a regra de maior autoridade;
- não avance até o bloqueio ser resolvido quando ele afetar o MVP.

Se regra de negócio ou jurídica necessária estiver ausente:
- registre `SPEC_MISSING`;
- não invente.

## 4. STACK PREFERENCIAL

Use stack simples, moderna e adequada à publicação online:

- Next.js com App Router;
- TypeScript estrito;
- React;
- Tailwind CSS;
- Zod para schemas de runtime;
- React Hook Form para o wizard;
- date-fns ou equivalente para datas;
- cálculo monetário integral em centavos ou biblioteca decimal segura;
- Vitest para unit/integration;
- Playwright para E2E;
- cobertura compatível com Vitest;
- geração de PDF determinística e compatível com serverless.

Use versões estáveis e suportadas no momento da implementação.

Use `npm` para simplificar operação local.

Não introduza banco de dados no MVP sem necessidade. Rascunhos podem permanecer temporariamente em estado de sessão/sessionStorage. Não usar localStorage persistente por padrão para PII. Não armazenar segredos no navegador.

## 5. FASES OBRIGATÓRIAS

### Fase 0 — Auditoria da especificação

Antes de codificar:
- leia todos os arquivos obrigatórios;
- execute `python tools/audit_specs.py`;
- exija `Errors: 0`;
- gere/atualize `docs/traceability-matrix.md`;
- associe cada regra `BR-*`, `VR-*`, `CR-*` e cada cláusula `CL-*` aos testes correspondentes;
- gere/atualize `docs/implementation-plan.md`;
- verifique `SPEC_MISSING` e `SPEC_CONFLICT`;
- não altere a biblioteca jurídica para facilitar implementação.

Não avance para a Fase 1 enquanto houver bloqueio.

### Fase 1 — Núcleo de domínio

Implemente primeiro funções puras para:
- validação de payload;
- cálculo de prazo de implantação;
- cálculo do valor total de referência da vigência;
- cálculo do valor nominal da fidelidade;
- cálculo proporcional por mês-calendário;
- cálculo de saldo remanescente de fidelidade;
- resolução de cláusulas;
- resolução de signatários;
- geração de `payload_hash`;
- geração do modelo renderizável do contrato.

Nenhum componente React deve conter regra de negócio duplicada.

### Fase 2 — Testes do domínio antes da interface

Implemente os casos e invariantes definidos em `tests/`.

Exija 100% de cobertura de branches, functions, statements e lines dentro do núcleo determinístico que valida combinações, calcula valores, resolve cláusulas e resolve signatários.

### Fase 3 — Interface e preview vivo

Implemente o wizard conforme `spec/form-flow.json` e `product/ui-requirements.md`.

Requisitos obrigatórios:
- identidade Rota em dark mode no aplicativo;
- desktop com formulário à esquerda e A4 ao vivo à direita;
- preview persistente desde o primeiro passo;
- preview usando o mesmo domínio/resolver/renderer do documento final;
- nenhuma regra contratual duplicada na UI;
- nenhum `{{PLACEHOLDER}}` jurídico bruto mostrado ao Closer;
- dados ainda pendentes representados apenas por marcadores UI-only;
- alteração de cláusula/valor/prazo/signatário com destaque transitório no preview;
- mobile com alternância `Preenchimento | Contrato`;
- progresso claro de configuração;
- cláusulas acionadas navegáveis para o trecho correspondente;
- tela cheia para leitura integral do contrato.

A etapa de revisão deve possuir CTA `REVISAR E GERAR CONTRATO`.

O modal obrigatório deve listar todas as decisões variáveis previstas em `spec/form-flow.json` e exigir checkbox de confirmação.

A confirmação deve registrar a aprovação da combinação exata de:
- `payload_hash`;
- `render_hash`;
- timestamp de aprovação.

Qualquer alteração contratual posterior antes de write externo deve invalidar a aprovação e eventual PDF não enviado.

Confirmar o modal nunca cria tarefa no ClickUp nem envia documento à ZapSign.

### Fase 4 — Renderer e PDF

O renderer:
- usa exclusivamente `legal/clause-library.json` para texto jurídico;
- respeita `spec/contract-structure.json`;
- aplica condições de `legal/clause-matrix.json`;
- substitui placeholders deterministicamente;
- não altera texto jurídico locked;
- preserva numeração;
- produz HTML do preview e PDF final a partir da mesma base estrutural.

Siga obrigatoriamente `product/contract-document-style.md`.

O documento final deve seguir, entre outros requisitos:
- A4;
- margens aproximadas de 25 mm;
- Times New Roman 12 pt;
- corpo justificado;
- entrelinha 1,5;
- título centralizado, em caixa alta e negrito;
- títulos de cláusula em negrito;
- data final alinhada à direita;
- blocos de assinatura conforme `spec/rendering-rules.json`;
- nenhum bloco automático de testemunhas nesta versão.

Validador final deve rejeitar documento se:
- restar placeholder;
- restar skeleton/marcador UI-only;
- houver cláusula proibida;
- faltar cláusula obrigatória;
- ordem estiver incorreta;
- texto locked divergir;
- signatários divergirem;
- cálculos divergirem;
- `render_hash` não corresponder à aprovação humana corrente.

### Fase 5 — Integrações em MOCK MODE

Implemente:
- `ClickUpAdapter`;
- `ZapSignAdapter`.

Mocks são padrão.

No mock:
- ClickUp retorna ID fake previsível;
- ZapSign retorna documento/signatários fake;
- nenhum tráfego externo.

### Fase 6 — Integrações reais

Implemente adapters reais conforme `integrations/` somente após homologação adequada.

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

Depois de write externo, alteração no formulário não pode modificar silenciosamente o registro/documento já criado. Mudança exige fluxo explícito de nova revisão/versão.

### Fase 7 — Gate pré-humano

Execute integralmente `tests/pre-human-gate.md`.

Se qualquer item falhar:
- não declare pronto;
- corrija;
- execute novamente.

Crie `artifacts/pre-human-report.md` contendo commit/hash testado, comandos, lint, typecheck, unit, integração, E2E, cobertura, build, cenários válidos/inválidos/manuais, preview, aprovação, placeholders, segurança e pendências reais.

## 6. REGRAS DE UX

Siga `product/brand-tokens.json`, `product/design-system.md`, `product/ui-requirements.md`, `product/ui-wireframe.md` e `product/ui-copy.md`.

Não use clichês jurídicos: balança, martelo, colunas clássicas ou pergaminhos.

A estética do **aplicativo** deve remeter a software B2B, tecnologia, consultoria, performance e operações.

Identidade do aplicativo:
- azul petróleo Rota;
- preto/cinza escuro;
- branco;
- dourado/amarelo para CTA/destaque;
- Poppins nos títulos;
- DM Sans no corpo.

A estética do **documento contratual** é separada e definida em `product/contract-document-style.md`.

O logo oficial ainda não está no pacote. Até que exista:
- use `ROTA JURÍDICA` como lockup tipográfico;
- não desenhe nova marca;
- não gere isomarca aproximada;
- prepare componentes para SVG oficial.

## 7. FLUXO DO FORMULÁRIO

Comportamentos obrigatórios:
- PF e PJ mutuamente exclusivos;
- PF pode ter múltiplos contratantes e cada PF assina;
- PJ permite apenas uma empresa;
- PJ pode ter múltiplos representantes e todo representante assina;
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

A fonte detalhada do fluxo é `spec/form-flow.json`.

## 8. QUALIDADE E TESTES

Use casos curados, testes de combinações, rejeição, propriedades/invariantes e snapshots apenas onde não mascararem lógica.

A suíte deve provar, entre outros:
- combinações válidas resolvem cláusulas corretamente;
- inválidas são bloqueadas;
- 4+ áreas => MANUAL_CONTRACT_REQUIRED;
- OTHER exige nome;
- LP condicional e sem renovação automática;
- criativos renovam mesma quantidade;
- Academy condiciona Consultoria;
- Flowjuris é omitido quando false e não possui preço individual;
- fidelidade não renova;
- reajuste só pertence ao período seguinte;
- faturamento não altera vigência;
- proporcionalidade usa dias reais do mês;
- multa moratória = 10%;
- suspensão por inadimplência somente após 10 dias;
- signatários corretos;
- preview vivo correto;
- modal obrigatório correto;
- aprovação por hashes correta;
- alteração posterior invalida aprovação;
- gerar contrato não dispara integração;
- PDF respeita formatação documental e não contém artefatos da UI.

Execute também `tests/ui-behavior-cases.json`.

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

Só diga `pronto para teste humano` se:
- gate pré-humano 100% aprovado;
- nenhum SPEC_MISSING relevante;
- nenhum SPEC_CONFLICT;
- zero placeholders no documento final;
- zero artefatos UI-only no PDF;
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

O repositório contém prompts auxiliares em `prompts/`.

Use-os como checkpoints de trabalho e não atravesse gates silenciosamente.

Se o ambiente Codex suportar revisões/subagentes, após a implementação principal execute revisões independentes para:
- integridade da especificação e ausência de regra inventada;
- segurança/PII/secrets;
- lacunas de testes/edge cases;
- acessibilidade e consistência visual;
- fidelidade do preview/PDF ao renderer.

Nunca permita que um agente altere `legal/clause-library.json` como correção automática.
