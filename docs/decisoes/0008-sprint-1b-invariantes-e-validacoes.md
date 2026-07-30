# 0008 — Sprint 1B: Invariantes, Validações e Modelo Executável

- **Status:** aceita
- **Data:** 2026-07-30

## Contexto

A Sprint 1B exigia transformar o modelo de domínio "só forma" da Sprint 1A em um domínio capaz de proteger sua própria consistência: invariantes por Aggregate, validações estruturais, enums estruturais e estados do modelo — nesta ordem, e explicitamente sem regra comercial da 027 Viagens (que continua pendente em `docs/business-rules.md`). Isso exigiu decisões técnicas sobre *como* implementar validação em Python usando apenas a biblioteca padrão (ADR 0006), e decisões de modelagem sobre *o que* é estrutural versus comercial em cada campo.

## Decisões

### 1. Mecanismo de validação: exceções de domínio + guards, sem framework

Criadas duas exceções em `src/domain/shared/exceptions.py`: `InvariantViolationError` (uma invariante de Aggregate foi violada) e `StructuralValidationError` (um valor não tem a forma mínima esperada) — ambas herdam de `DomainError`. Criado `src/domain/shared/guards.py` com funções pequenas e reutilizáveis (`require`, `require_not_none`, `require_instance`, `require_non_empty_str`, `require_identifier`, `require_non_empty_collection`) usadas em `__post_init__` de cada Entidade/VO. Nenhuma biblioteca externa foi introduzida — consistente com a decisão de stack da ADR 0006 (Python, apenas biblioteca padrão).

### 2. `BaseEntity.__post_init__` valida `id`; subclasses chamam `super().__post_init__()`

Centraliza a checagem "todo Entidade tem um `Identifier` válido" em um único lugar (`src/domain/shared/base_entity.py`), evitando repetição. Toda subclasse que define seu próprio `__post_init__` chama `super().__post_init__()` primeiro.

### 3. Critério para "isso vira enum agora" vs. "isso continua texto livre"

Um campo virou `Enum` fechado nesta sprint apenas quando a classificação é **estrutural/universal do setor** (não depende de decisão comercial da 027 e é um conjunto pequeno e estável): `DocumentType`, `PhoneType`, `Currency`, `SupplierCategory`, `PassengerType`, `AirportType`, mais os "Estados do Modelo" `ProposalStatus`/`ProposalVersionStatus` e o nomeador `ProposalDimension`. Um campo **não** virou enum quando depende de Regra Comercial ainda pendente em `business-rules.md` — caso notável: `Financial.payment_method` permanece texto livre (formas de pagamento aceitas pela 027 ainda não foram confirmadas). Ver `docs/domain-decisions.md` para o raciocínio caso a caso.

### 4. Referências de grande volume/voláteis viram Value Object com validação de formato, não Enum

`CountryCode` e `LanguageCode` (exemplos do briefing como "enums estruturais") foram implementados como Value Objects validados por formato (ISO 3166-1 alpha-2 / ISO 639-1), não como `Enum` Python com todos os valores. Justificativa completa em `docs/domain-decisions.md`. `Currency`, por ter um conjunto pequeno e realista para uma agência de viagens, permaneceu como `Enum` fechado.

### 5. Revisão do Shared Kernel: um achado, uma correção

A revisão (item 9 do briefing) encontrou um vazamento: `Metadata.proposal_id`, dentro de um Value Object pensado para todos os módulos futuros, carregava um nome específico do módulo Propostas. Corrigido para `Metadata.subject_id`. Nenhum outro objeto de `src/domain/shared/` foi considerado específico de contexto o suficiente para ser removido — todos (Identifier, BaseEntity, ValueObject, DomainEvent, exceptions, guards, Money, Email, Phone, Address, DocumentNumber, DateRange, CountryCode, LanguageCode, Metadata, DocumentType, PhoneType, Currency) são reaproveitados por mais de um Bounded Context. Detalhe completo em `docs/domain-decisions.md`.

### 6. `Proposal` como Aggregate de Coordenação

Formalizado em ADR [0007](0007-proposal-aggregate-de-coordenacao.md) — decisão separada desta por ser suficientemente relevante (risco de longo prazo para toda a plataforma) para justificar sua própria ADR, conforme pedido explicitamente no briefing.

### 7. `src/domain/events/` preparado, sem eventos implementados

Estrutura e documentação de eventos futuros (`ProposalCreated`, `ProposalUpdated`, `ProposalApproved`, `ProposalRejected`, `ProposalExpired`, `TripCreated`, `CustomerRegistered`, `EmissionCompleted`) em `src/domain/events/README.md`. A base `DomainEvent` permanece em `src/domain/shared/` (Sprint 1A) por ser um primitivo verdadeiramente compartilhado.

## Consequências

- Toda instanciação de Entidade/VO no domínio agora pode levantar `StructuralValidationError`/`InvariantViolationError` — código que constrói objetos de domínio (exemplos, futuros casos de uso em `src/application/`) deve estar preparado para isso.
- `examples/` foi atualizado para refletir os novos campos obrigatórios (`Trip.passenger_ids`, `Passenger.passenger_type`, `Phone.type`, `Proposal.status`, `ProposalVersion.status`, `Address.country` como `CountryCode`, `Money.currency`/`DocumentNumber.type` como enum).
- `schemas/` foi atualizado em paralelo (ver seção correspondente do CHANGELOG) para não divergir do domínio — `required` estrutural e `enum` estrutural adicionados, nenhuma regra comercial.
- Sprint 1B+ (quando `business-rules.md` for preenchido) deve revisitar especificamente `Financial.payment_method`, os valores de `ProposalClassification` (ainda texto livre) e os 9 status ricos de `docs/proposal-status.md` (ainda não implementados — `ProposalStatus`/`ProposalVersionStatus` desta sprint são deliberadamente mais simples, só o "esqueleto" estrutural).
