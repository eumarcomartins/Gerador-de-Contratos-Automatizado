# Spec Audit Report — entrega inicial

Data da auditoria: 2026-08-18T17:40:25

Comando:

```bash
python tools/audit_specs.py
```

Resultado:

```text
# SPEC AUDIT
[OK] 31 arquivos JSON parseados.
[OK] Clause IDs únicos.
[OK] Clause matrix cobre exatamente a biblioteca.
[OK] Contract structure cobre exatamente a biblioteca.
[OK] Guardas de português canônico aprovadas.
[OK] 31 placeholders canônicos encontrados.
[OK] 12 casos válidos únicos.
[OK] Derivados básicos dos casos válidos conferidos.
[OK] 14 casos inválidos/manuais referenciam fixtures válidas.
[OK] Expected clause sets cobrem todos os casos válidos.
[OK] Arquivos obrigatórios presentes.
[WARN] Logo oficial não fornecido; fallback tipográfico deve ser usado: assets/logo-horizontal.svg, assets/logo-mark.svg, assets/favicon.svg

Errors: 0 | Warnings: 1
```

Exit code: 0

## Interpretação

Erros: 0 esperados para liberação do pacote.

Advertência conhecida: os arquivos oficiais do logotipo ainda não foram fornecidos. O protótipo deve usar o fallback tipográfico e não pode recriar a marca por aproximação.
