# Release Process

## Versões independentes

Spec Version
Business/validation/calculation/schema behavior.

Clause Library Version
Texto jurídico locked.

Application Version
Código do produto.

## SemVer

PATCH
correção técnica que não altera regra/resultado contratual.

MINOR
nova funcionalidade compatível ou novo caminho de UI sem quebra das regras existentes.

MAJOR
mudança de regra contratual, payload incompatível ou alteração estrutural relevante.

Alteração de cláusula locked deve, no mínimo, gerar nova versão da Clause Library.

## Release pré-humana

audit_specs verde;
testes verdes;
build verde;
mocks;
pre-human-report.

## Release de produção

teste humano aprovado;
checklist jurídico aprovado;
logo oficial opcional para funcionalidade, porém recomendado para identidade;
secrets configurados;
smoke test de integrações com dados de teste autorizados;
tag Git;
registro das versões Spec/Clause/App no ambiente.
