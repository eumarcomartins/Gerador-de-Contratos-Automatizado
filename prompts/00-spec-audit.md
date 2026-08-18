# Fase 0 — Auditoria

Leia AGENTS.md, MASTER_PROMPT.md e toda a especificação.

Execute `python tools/audit_specs.py`.

Crie `docs/traceability-matrix.md` e `docs/implementation-plan.md`.

Não escreva aplicação ainda.

Confirme:
zero SPEC_CONFLICT;
zero SPEC_MISSING que bloqueie o MVP;
todas as regras BR/VR/CR ligadas a casos de teste;
todas as cláusulas CL presentes em library/matrix/structure;
todos os placeholders mapeados.

Se houver erro, corrija apenas a implementação/documentação gerada por você. Não altere especificações sem autorização.
