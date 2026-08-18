# Decision Register — Assessoria v1.0.0

Este arquivo registra decisões de negócio aprovadas durante o mapeamento. Ele serve para evitar que futuras alterações sejam confundidas com regras históricas.

## Contratante

PF e PJ são fluxos mutuamente exclusivos.
PF pode conter múltiplos contratantes e todos assinam.
PJ aceita uma única pessoa jurídica e múltiplos representantes.
Todo representante informado assina.
Mais de uma PJ exige contrato manual.

## Escopo

O Closer informa apenas quantidade de áreas: 1, 2 ou 3.
4 ou mais áreas exige contrato manual.
Canais são multi-seleção.
Outro canal exige especificação.
O teto de mídia é global entre todos os canais.
Acima do teto exige negociação entre as partes.

Landing Pages são opcionais, com quantidade.
Landing Pages são entregas da implantação inicial e não se renovam automaticamente.

Criativos são uma quantidade total por período contratual.
Peça estática = 1 slot.
Vídeo = 1 slot.
Roteiro e edição integram o próprio slot do vídeo.
A renovação repõe a mesma quantidade de criativos do período anterior, salvo ajuste expresso.

Rota Academy vem Sim por padrão.
Se incluída, Consultoria Comercial Remota também é incluída, sem limite contratual de frequência.

Flowjuris vem Sim por padrão.
Durante a Assessoria, está embutido na mensalidade, sem preço individual.
Inclui acesso, trilha de implementação/uso, apoio inicial de configuração e suporte a dúvidas de uso.
Encerrada a Assessoria, encerra-se a disponibilização incluída.
Se não houver contratação separada, há 7 dias para o próprio cliente exportar dados.
Depois, não há obrigação contratual de manter, exportar, restaurar ou reativar, ressalvadas obrigações legais de conservação.

Mensuração: atualização semanal + checkpoint mensal.

## Prazos

Contagem a partir do Onboarding.
1 área = 7 dias úteis.
2 áreas = 10 dias úteis.
3 áreas = 15 dias úteis.
Canais e quantidade de LPs não alteram o prazo por si.
Dependências do cliente suspendem/reprogramam prazos afetados.

## Vigência

Vigência: 3, 6 ou 12 meses.
Fidelidade: livre em meses, mínimo 3, máximo igual à vigência.
Renovação automática por igual período.
Fidelidade não renasce na renovação.
Após fidelidade, rescisão com aviso prévio de 30 dias.
Encerramento imediato sem aviso: valor substitutivo de uma mensalidade, além das obrigações vencidas/proporcionais.
Nova condição comercial somente para o próximo período renovado, com aviso mínimo de 30 dias.

## Financeiro

Mensalidade informada pelo Closer.
Primeira fatura e vencimento recorrente podem divergir.
Datas de faturamento não determinam ciclo de prestação.
Pagamento: boleto/PIX ou cartão recorrente.

Setup operacional: R$ 1.000.
Cobrado ou Isento.
Se cobrado: boleto/PIX junto da mensalidade ou cartão em até 12x, com encargos da operadora suportados pelo cliente.
Data do setup informada pelo Closer.

Inadimplência:
multa moratória 10%;
juros 1% ao mês pro rata die;
IPCA após 30 dias;
suspensão após 10 dias;
medidas de cobrança após 20 dias;
prazo adicional de 5 dias úteis após notificação antes de rescisão motivada apenas por inadimplência.

Proporcionalidade em mês parcial:
mensalidade ÷ dias totais do mês × dias de serviço no mesmo mês.

Multa durante fidelidade:
20% do saldo remanescente de obrigações do período de fidelidade.
Histórico de pagamento não é proxy de tempo de serviço consumido.

## Datas

Data de assinatura é informada pelo Closer.
Data de início é informada pelo Closer.
São independentes.
Data de geração é metadado técnico.

## Integrações

ClickUp e ZapSign devem operar primeiro em MOCK.
Credenciais nunca entram no repositório.
