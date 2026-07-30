# 0006 — Sprint 1A: Modelagem de Domínio

- **Status:** aceita
- **Data:** 2026-07-29

## Contexto

A Sprint 1A exigia representar os objetos de domínio da plataforma (Company, Customer, Passenger, Consultant, Supplier, Proposal, ProposalVersion, Trip, Flight, Accommodation, Service, Financial, Metadata) sem validação, obrigatoriedade, enum ou regra de negócio, organizados por Bounded Context, com um Bounded Context Map, Value Objects, Aggregate Roots e uma estrutura modular de schemas. Isso é a primeira sprint com código de fato — várias decisões de engenharia precisaram ser tomadas para transformar o que estava só em documentação (`vision.md`, `glossary.md`, `domain-map.md`, `proposal-types.md`) em objetos concretos.

## Decisões

### 1. Linguagem e stack: Python, biblioteca padrão apenas

Confirma a direção já sugerida em `README.md`: **Python**, usando `dataclasses` da biblioteca padrão para Entidades e Value Objects — nenhuma dependência externa (sem framework de validação, sem ORM). Justificativa: nenhuma dependência é necessária para "apenas representar a forma dos conceitos"; introduzir uma biblioteca de validação (ex: Pydantic) nesta sprint seria adiantar comportamento que pertence à Sprint 1B. `dataclass(frozen=True)` dá exatamente a semântica de Value Object (imutável, igualdade por valor) sem código adicional; `dataclass` mutável + `__eq__`/`__hash__` customizados em `BaseEntity` dá a semântica de Entidade (igualdade por identidade).

### 2. Estrutura `src/domain/`, `src/application/`, `src/infrastructure/` substitui `src/core/`, `src/models/`, `src/generators/`, `src/utils/`

A estrutura definida nas ADRs [0001](0001-estrutura-inicial-do-projeto.md)/[0002](0002-evolucao-para-plataforma-de-documentos.md) (core/models/generators/utils) foi removida e substituída pela organização em camadas do Clean Architecture (domain/application/infrastructure), com `domain/` subdividido por Bounded Context. Como nenhum código havia sido escrito nessas pastas antigas (só `.gitkeep`), a substituição não exigiu migração — apenas atualização de `ARCHITECTURE.md`. `application/` e `infrastructure/` ficam vazias nesta sprint, com README explicando o que cada uma vai receber (mesmo padrão já usado para `ai/` na Sprint 0.5).

### 3. Aggregate Roots: Company, Customer, Supplier, Trip e Proposal

A hipótese inicial do briefing (Proposal, Customer, Trip) foi confirmada e **estendida** com Company e Supplier, que precisavam de um lar por eliminação (nenhuma outra Entidade os contém):

- **Company** — Aggregate Root; agrega `Consultant` (a 027 Viagens emprega N consultores). Justificativa para ser Root e não um Value Object fixo em `config/`: prepara terreno para múltiplas empresas na plataforma no futuro, sem redesenho.
- **Customer** — Aggregate Root; agrega `Passenger`. Justificativa: um Cliente tem ciclo de vida independente de qualquer Proposta específica.
- **Supplier** — Aggregate Root, standalone; referenciado por id a partir de `Flight`, `Accommodation`, `Service`. Justificativa: o mesmo Fornecedor é reaproveitado entre várias Trips — nunca deveria ser copiado/aninhado.
- **Trip** — Aggregate Root; agrega `Flight`, `Accommodation`, `Service`. Justificativa: uma Viagem continua existindo depois que o ciclo comercial da Proposta termina (o passageiro efetivamente viaja); módulos futuros de Operações (Emissão, Itinerário — ver `bounded-context-map.md`) devem poder referenciar a Trip sem depender da Proposal de origem.
- **Proposal** — Aggregate Root; agrega `ProposalVersion`. Deliberadamente magra: só `id` e a lista de versões — todo conteúdo real (cliente, viagem, financeiro, classificação) vive em cada `ProposalVersion`, consistente com `docs/proposal-versioning.md` ("cada versão é um snapshot completo").

Todos os Aggregates se referenciam exclusivamente por `Identifier`, nunca por objeto aninhado entre si (só dentro do próprio Aggregate) — ver `docs/bounded-context-map.md`, seção Comunicação entre contextos.

### 4. Metadata e Financial modelados como Value Objects, não Entidades

O briefing listava "Metadata" e "Financial" na seção de Entidades, mas ambos foram implementados como Value Objects (`@dataclass(frozen=True)`), porque nenhum dos dois tem identidade própria distinta do que carregam: dois blocos de metadata ou financeiro com os mesmos valores representam a mesma informação. Ambos ficam aninhados dentro de `ProposalVersion` (que sim tem identidade). `Metadata` vive em `src/domain/shared/` por ser potencialmente reaproveitada por módulos futuros (Contratos, Vouchers); `Financial` vive em `src/domain/financial/` por ser específica do conteúdo comercial de uma proposta.

### 5. Novo Value Object: `ProposalClassification`

Não estava na lista de exemplos do briefing, mas é necessário para representar `docs/proposal-types.md` (ADR [0005](0005-refinamento-pre-sprint-1a.md)): uma Proposta não tem um tipo único, tem quatro dimensões combináveis. Modelado como Value Object com quatro tuplas de texto livre (`destinations`, `formats`, `purposes`, `products`) — sem enum, conforme a restrição desta sprint; os valores possíveis de cada dimensão são restringidos na Sprint 1B.

### 6. `ProposalVersion` sem campo `status` próprio

`status` vive exclusivamente em `metadata.status`, evitando duas fontes de verdade sobre o estado de uma versão — consistente com `docs/universal-proposal-model.md`.

### 7. Extensões pontuais aos exemplos do briefing

- `Airport` (Value Object) foi criado em `src/domain/trip/`, usado por `Flight` — não estava na lista de VOs do briefing, mas é necessário para representar origem/destino de um voo.
- `schemas/company/consultant.schema.json`, `schemas/trip/airport.schema.json` e `schemas/proposal/proposal-classification.schema.json` foram adicionados além do exemplo literal de estrutura de schemas do briefing, para manter o princípio "um arquivo por Entidade/VO, reaproveitado via `$ref`" de forma consistente — em vez de embutir Consultant/Airport/ProposalClassification inline nos schemas que os usam.
- `schemas/shared/` foi criado (não estava no exemplo do briefing) espelhando `src/domain/shared/`, para os VOs verdadeiramente comuns (`Identifier`, `Money`, `Email`, `Phone`, `Address`, `DocumentNumber`, `DateRange`, `Metadata`), evitando duplicar a mesma forma em múltiplos schemas de contexto.

### 8. Schemas Sprint 1A: forma apenas, com `$comment` explícito

Todo arquivo em `schemas/` tem `type`/`properties` mas nenhum `required` nem `enum` nesta sprint — e um campo `$comment` deixando isso explícito, para que a Sprint 1B saiba exatamente o que falta adicionar em cada arquivo (não criar novos arquivos, evoluir os existentes).

## Consequências

- `docs/ARCHITECTURE.md`, `README.md` e `ROADMAP.md` foram atualizados para descrever `src/domain/application/infrastructure` no lugar da estrutura antiga.
- A Sprint 1B deve adicionar, aos mesmos arquivos já criados (Python e JSON Schema): validações, obrigatoriedades, enums (incluindo os valores de `ProposalClassification`), e os métodos de comportamento de domínio (ex: `Proposal.aprovar()`, `Proposal.nova_versao()`) que ainda não existem.
- Módulos futuros de documento (Contratos, Vouchers) devem seguir o mesmo padrão de Aggregate/Value Object/Entidade e reaproveitar `src/domain/shared/`, `src/domain/company/`, `src/domain/customer/`, `src/domain/supplier/`, `src/domain/financial/` em vez de recriá-los.
- `Lead`, `Cotação`, `Emissão`, `Voucher`, `Itinerário` (como artefato), `Seguro` (como produto) e `Comissão` seguem sem Entidade própria — gaps documentados em `docs/bounded-context-map.md`, a resolver em sprints futuras conforme priorização.
