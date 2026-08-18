# Contract Document Style

A interface segue a identidade escura da Rota. O contrato gerado, porém, deve priorizar legibilidade jurídica e impressão.

## Página

A4.
Fundo branco.
Texto preto.
Margens consistentes entre 18 mm e 22 mm.
Sem elementos decorativos que disputem atenção com o conteúdo jurídico.

## Tipografia

Usar fonte de alta legibilidade com suporte completo a caracteres pt-BR.
O PDF não depende dos arquivos Poppins/DM Sans do front-end.
Não empacotar arquivos de fonte proprietários no repositório.

Corpo: aproximadamente 10,5–11,5 pt.
Entrelinha confortável.
Títulos de cláusulas em negrito.
Numeração preservada exatamente pelo renderer.

## Cabeçalho

No MVP, não é obrigatório usar logo.
Quando o arquivo oficial estiver disponível, a aplicação pode inserir o logo conforme configuração, sem alterar o texto das cláusulas.

## Rodapé

Pode conter:
identificador interno do contrato;
versão da especificação;
número de página.

Não exibir tokens, IDs secretos ou payload completo.

## Preview

O preview deve representar fielmente o PDF final.
Nenhuma edição inline de cláusulas no MVP.

## Quebras de página

Evitar título de cláusula isolado no fim da página quando tecnicamente possível.
Blocos de assinatura podem iniciar em nova página se necessário.
