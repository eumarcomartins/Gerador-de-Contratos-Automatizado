# Fase 4 — Renderer e PDF

Renderer 100% determinístico.

Leia:
- `legal/clause-library.json`
- `legal/clause-hashes.json`
- `legal/clause-matrix.json`
- `spec/contract-structure.json`
- `spec/placeholder-map.json`
- `spec/rendering-rules.json`
- `product/contract-document-style.md`

O preview vivo e o PDF final devem compartilhar o mesmo renderer/base estrutural.

Formatação do documento:
- A4;
- aproximadamente 25 mm de margem;
- Times New Roman 12 pt;
- corpo justificado;
- entrelinha 1,5;
- título centralizado, caixa alta e negrito;
- títulos de cláusula em negrito;
- data final alinhada à direita;
- blocos de assinatura conforme `spec/rendering-rules.json` e `product/contract-document-style.md`.

Durante preview incompleto:
- permitir apenas marcadores UI-only;
- nunca mostrar placeholder jurídico bruto.

No PDF final:
- zero marcadores;
- zero skeletons;
- zero destaques temporários;
- zero placeholders.

Rejeite:
- placeholders restantes;
- conjunto de cláusulas divergente;
- ordem divergente;
- texto locked alterado;
- signatários inconsistentes;
- documento cujo `render_hash` não corresponda à aprovação humana corrente.

Execute todos os testes de formatação, cláusulas e comportamento de preview/assinatura aplicáveis.
