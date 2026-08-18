# Arquitetura de Runtime

UI Wizard
→ POST /api/contracts/validate
→ Domain Validator
→ Rules Engine
→ Consolidated Contract Payload
→ Clause Resolver
→ Renderer
→ Final Integrity Validator
→ HTML Preview / PDF

Após aprovação:
→ ClickUp Adapter
→ ZapSign Adapter

## Módulos sugeridos
src/domain/schema
src/domain/validation
src/domain/rules
src/domain/calculations
src/domain/clauses
src/domain/rendering
src/domain/signers
src/integrations/clickup
src/integrations/zapsign
src/app
src/components

O domínio não importa React, Next.js, ClickUp ou ZapSign.
