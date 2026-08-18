# Test Plan

## Objetivo
Provar que o gerador é determinístico e que nenhum caminho altera cláusulas, cálculos ou signatários fora da especificação.

## Camadas
1. Schema tests.
2. Business validation tests para VR-*.
3. Calculation tests para CR-* com meses de 28/29/30/31 dias e valores com centavos.
4. Clause resolver: conjunto e ordem exatos.
5. Signers: PF 1/2/3; PJ 1/2/3 representantes.
6. Renderer: zero placeholders, pt-BR, texto locked, hash estável.
7. Integration tests: mocks only.
8. E2E: principais caminhos e bloqueios.

## Cobertura obrigatória no núcleo determinístico
100% statements
100% branches
100% functions
100% lines

## Property tests
Usar `property-invariants.json`.
Rodar ao menos 1.000 payloads válidos e 1.000 mutados/inválidos por execução com seed registrada.
