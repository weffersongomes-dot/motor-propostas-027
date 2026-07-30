# schemas/

Define os **modelos JSON** (JSON Schema) que descrevem formalmente cada estrutura de dados usada pela plataforma. É a fonte de verdade sobre "quais campos existem, quais tipos têm" — e, a partir da Sprint 1B, também "quais são obrigatórios, quais têm valores restritos (enum)".

## Organização modular (desde a Sprint 1A)

Em vez de um único schema gigante, `schemas/` é organizado **por Bounded Context/entidade**, espelhando `src/domain/` (ver `docs/bounded-context-map.md` e `docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md`):

```
schemas/
├── shared/       → Value Objects/estruturas comuns: identifier, money, email, phone,
│                    address, document-number, date-range, metadata
├── company/       → company, consultant
├── customer/       → customer, passenger
├── supplier/        → supplier
├── trip/              → trip, flight, accommodation, service, airport
├── financial/          → financial
└── proposal/            → proposal, proposal-version, proposal-classification
```

Cada schema usa `$ref` para reaproveitar os de `shared/` e de outros contextos (ex: `proposal-version.schema.json` referencia `financial/financial.schema.json` e `shared/metadata.schema.json`) — em vez de duplicar a mesma forma em vários lugares.

**Sprint 1A:** cada schema tem apenas `type`/`properties` (a forma), sem `required` nem `enum` — reflete exatamente as entidades/Value Objects de `src/domain/`, que nesta etapa também não têm validação nem obrigatoriedade. Cada arquivo tem um campo `$comment` deixando isso explícito.

**Sprint 1B:** os mesmos arquivos ganham `required`, `enum` e outras restrições, a partir do que for confirmado em `docs/business-rules.md`. Não se cria um schema novo — evolui-se o existente.

## O que vai continuar entrando aqui

À medida que novos módulos da plataforma forem adicionados (Contratos, Vouchers, Itinerários, Confirmações de Reserva, Recibos, Checklists do Passageiro, Relatórios), cada um ganha sua própria pasta aqui — reaproveitando os schemas de `shared/`, `customer/`, `company/`, `supplier/` e `financial/` sempre que possível, em vez de recriá-los (mesmo princípio de `ARCHITECTURE.md`, seção 7 — Estratégia de expansão).

## Relação com `src/domain/`

`schemas/` descreve a estrutura (o "contrato de dados") de forma independente de linguagem; `src/domain/` é o código Python que representa essas mesmas estruturas como Entidades e Value Objects. Os dois devem evoluir juntos — mudou um atributo em `src/domain/proposal/proposal_version.py`, muda `schemas/proposal/proposal-version.schema.json` (e vice-versa).

## Por que existe

Ter os schemas isolados, modulares e documentados torna qualquer novo formato de saída ou integração (Coda, CRM, WhatsApp Business API) capaz de saber exatamente o que esperar dos dados, sem precisar ler código Python para descobrir a estrutura — e permite evoluir um módulo (ex: Financeiro) sem re-publicar o schema inteiro da plataforma.
