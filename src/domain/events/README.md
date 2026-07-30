# src/domain/events/

Estrutura preparada para Domain Events — **nenhum evento está implementado nesta sprint**, apenas documentado. A base `DomainEvent` (imutável, com `occurred_at`) já existe em [`src/domain/shared/domain_event.py`](../shared/domain_event.py) desde a Sprint 1A.

## Por que existe

Contextos (`docs/bounded-context-map.md`) devem se comunicar sem se acoplar diretamente — Operações reagindo a "Proposta paga", por exemplo, não deveria importar e chamar `Proposal` diretamente. Domain Events são o mecanismo planejado para isso: um contexto publica um evento, outro(s) reagem, sem dependência direta entre Aggregates de contextos diferentes.

## Quando isso será implementado

Quando `src/application/` deixar de estar vazia (ver `src/application/README.md`) — casos de uso vão gerar e despachar eventos; um mecanismo de publicação/assinatura (provavelmente em `src/infrastructure/`) vai entregá-los aos interessados. Nenhuma dessas peças existe ainda.

## Eventos previstos (documentação, não implementação)

| Evento | Contexto que publica | Quando |
|---|---|---|
| `ProposalCreated` | Comercial | Uma nova `Proposal` (com sua primeira `ProposalVersion`) é criada. |
| `ProposalUpdated` | Comercial | Uma nova `ProposalVersion` é adicionada a uma `Proposal` existente. |
| `ProposalApproved` | Comercial | Uma `ProposalVersion` é aprovada pelo cliente (ver `docs/proposal-actions.md`, ação Aprovar). |
| `ProposalRejected` | Comercial | Uma `ProposalVersion` é reprovada (ver `docs/proposal-actions.md`, ação Reprovar). |
| `ProposalExpired` | Comercial | Uma `Proposal`/`ProposalVersion` ultrapassa o prazo de validade sem aprovação (ver `docs/business-rules.md`, Validade de propostas). |
| `TripCreated` | Operações | Uma nova `Trip` é criada. |
| `CustomerRegistered` | Cadastro | Um novo `Customer` é cadastrado. |
| `EmissionCompleted` | Operações | Uma `Proposal` paga é efetivamente emitida junto aos Fornecedores (módulo futuro de Emissão, ainda sem Entidade própria — ver `docs/bounded-context-map.md`, gaps do contexto Operações). |

Esta lista não é definitiva — cada evento só deve ser implementado quando o caso de uso correspondente existir em `src/application/`. Novos eventos identificados devem ser adicionados a esta tabela antes de virarem código, seguindo o mesmo princípio de "documentar antes de implementar" já usado no resto do projeto.
