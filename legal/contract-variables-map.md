# Mapa de Variáveis e Cláusulas — Assessoria

| Campo | Cláusula/Bloco afetado | Observação |
|---|---|---|
| contractor_type | Preâmbulo + assinaturas | PF/PJ excludentes |
| individual_contractors[] | Preâmbulo PF + assinaturas | Todos assinam |
| legal_entity | Preâmbulo PJ | Apenas uma PJ |
| legal_entity.representatives[] | Preâmbulo PJ + assinaturas | Todos assinam |
| communication.whatsapp_main | 2.3 | Um contato principal |
| scope.areas_count | 1 e 4 | 1/2/3 automáticos; 4+ manual |
| scope.media_channels[] | 2.4 | Multi-seleção |
| scope.other_media_channel | 2.4 | Só se OTHER |
| scope.media_cap_brl | 2.4 | Teto global mensal |
| scope.landing_page_included | 2.5 | Controla inclusão |
| scope.landing_pages_quantity | 2.5 | Entrega inicial; não renova |
| scope.creatives_quantity | 2.6 | Slots por período; renova na mesma quantidade |
| scope.rota_academy_included | 2.7 | Default Sim; inclui Consultoria |
| scope.flowjuris_included | 2.8 | Default Sim |
| dates.service_start_date | 5 | Base do ciclo contratual |
| term.term_months | 5 e 9 | 3, 6 ou 12 |
| term.fidelity_months | 5 e 10 | Mín. 3; máx. vigência |
| commercial.monthly_fee_brl | 9 e 10 | Mensalidade |
| dates.first_invoice_date | 9 | Financeiro, sem efeito na vigência |
| payment.recurring_due_day | 9 | Financeiro |
| payment.method | 9 | Boleto/PIX ou cartão recorrente |
| setup.status | 9.2 | Cobrado/Isento |
| setup.payment_method | 9.2 | Condicional |
| setup.payment_date | 9.2 | Condicional |
| dates.signature_date | Fecho | Informada pelo Closer |
