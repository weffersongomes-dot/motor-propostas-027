# Roadmap — Motor de Propostas Comerciais (027 Viagens)

Cada sprint entrega um incremento fechado e testável. Sprints seguintes dependem dos anteriores.

## Sprint 0 — Estrutura do projeto

**Objetivo:** organizar o projeto antes de escrever qualquer funcionalidade.

**Entregáveis:**
- Estrutura de diretórios (`assets/`, `docs/`, `prompts/`, `templates/`, `examples/`, `output/`, `scripts/`, `src/`).
- `README.md`, `PRD.md`, `ROADMAP.md`, `CHANGELOG.md`.
- `.gitignore` configurado.

**Critérios de aceite:**
- Repositório clonável com estrutura completa e sem código de funcionalidade.
- Documentação explica visão geral, objetivo, arquitetura e plano de sprints.

---

## Sprint 0.4 — Evolução para Plataforma de Documentos

**Objetivo:** revisar a arquitetura antes de iniciar a implementação funcional, preparando a estrutura para futuros módulos além do Motor de Propostas (contratos, vouchers, itinerários, etc.), sem exigir refatorações grandes depois.

**Entregáveis:**
- Novas camadas: `config/`, `components/`, `content/`, `schemas/`, `tests/`, cada uma documentada.
- `docs/ARCHITECTURE.md` como referência técnica principal.
- `templates/`, `output/` e `src/generators/` reorganizados por módulo (`propostas/` como primeiro módulo).
- ADR [0002](docs/decisoes/0002-evolucao-para-plataforma-de-documentos.md) registrando a decisão.

**Critérios de aceite:**
- Estrutura de pastas suporta um novo tipo de documento sem mover/renomear o que já existe para `propostas/`.
- `docs/ARCHITECTURE.md` documenta módulos, fluxo de dados obrigatório, responsabilidades por camada e estratégia de expansão.
- Ainda nenhum código funcional implementado.

---

## Sprint 0.5 — Engenharia Comercial e Descoberta do Negócio

**Objetivo:** transformar o conhecimento operacional da 027 Viagens (hoje concentrado no proprietário, Wefferson) em documentação técnica, usando um processo estruturado de descoberta de negócio (Business Analysis) e linguagem ubíqua (DDD) — sem escrever nenhum schema ou código.

**Entregáveis:**
- `docs/proposal-types.md` — tipos de proposta suportados, estrutura + perguntas (sem preencher o desconhecido).
- `docs/proposal-lifecycle.md` — ciclo de vida completo, de Lead a Pós-venda.
- `docs/proposal-status.md` — estados possíveis de uma proposta.
- `docs/proposal-actions.md` — ações possíveis sobre uma proposta.
- `docs/proposal-versioning.md` — estratégia de versionamento de propostas.
- `docs/discovery-workshop.md` — roteiro estruturado de entrevistas com o proprietário.
- `docs/glossary.md` — linguagem ubíqua (conceitos de domínio), atualizada continuamente.
- `docs/business-rules.md` reorganizado por Objetivo / Regras conhecidas / Regras pendentes / Perguntas em aberto / Observações.
- ADR [0004](docs/decisoes/0004-sprint-05-engenharia-comercial.md) registrando a decisão.

**Critérios de aceite:**
- Existe um roteiro completo de descoberta, pronto para conduzir com o proprietário.
- Todas as dúvidas do negócio identificadas até aqui estão registradas nos documentos correspondentes, não perdidas em conversa.
- Nenhuma regra de negócio foi inventada ou assumida como definitiva.
- Toda informação pendente está claramente identificada como pendente.
- Nenhum schema (`schemas/proposta.schema.json`) foi criado antes da conclusão desta sprint.

---

## Sprint 1A — Modelagem do Domínio ✅ concluída

**Objetivo:** representar os objetos de domínio da plataforma (as entidades do `docs/domain-map.md`), usando a terminologia definida em `docs/glossary.md` — **sem** validações, obrigatoriedades, enums ou regras de negócio. Só a forma dos conceitos, não o comportamento deles.

**Pré-requisito:** Sprint 0.5 concluída — glossário e mapa de domínio (`docs/domain-map.md`) estáveis o suficiente para nomear os objetos sem ambiguidade.

**Entregáveis:**
- `docs/bounded-context-map.md` — Comercial, Operações, Financeiro, Cadastro: responsabilidades, limites, dependências, comunicação entre contextos.
- Entidades, Value Objects e Aggregates em `src/domain/`, organizados por Bounded Context técnico (`shared/`, `company/`, `customer/`, `supplier/`, `trip/`, `financial/`, `proposal/`) para: Company, Consultant, Customer, Passenger, Supplier, Trip, Flight, Accommodation, Service, Financial, Proposal, ProposalVersion, Metadata — cada um apenas com seus atributos, sem lógica. Aggregate Roots: Company, Customer, Supplier, Trip, Proposal.
- `src/application/` e `src/infrastructure/` criadas vazias, com README explicando o que vão receber.
- Estrutura modular de `schemas/` (por Bounded Context, espelhando `src/domain/`), forma apenas (sem `required`/`enum`).
- Exemplo de dado de entrada em `examples/sprint_1a_domain_example.py`, usando esses objetos, ainda sem validação — executado com sucesso.
- Documentação da decisão de linguagem/stack (Python + `dataclasses`, sem dependências) em [ADR 0006](docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md).

**Critérios de aceite:**
- Todo objeto de domínio usa exatamente os nomes definidos em `docs/glossary.md` (Linguagem Ubíqua) — ✅.
- Nenhuma validação, obrigatoriedade, enum ou regra de negócio presente nesta etapa — isso é responsabilidade da Sprint 1B — ✅.
- Um exemplo de viagem pode ser representado 100% pelos objetos de domínio, sem campos "soltos" fora deles — ✅ (`examples/sprint_1a_domain_example.py`).

---

## Sprint 1B — Invariantes, Validações e Modelo Executável ✅ concluída

**Objetivo:** transformar os objetos "só forma" da Sprint 1A num domínio capaz de proteger sua própria consistência — invariantes por Aggregate, validações estruturais, enums estruturais e estados do modelo, **nesta ordem**, sem nenhuma regra comercial da 027 (essa parte fica para uma sprint futura, quando `business-rules.md` estiver confirmado — ver Sprint 1C abaixo).

**Pré-requisito:** Sprint 1A concluída.

**Entregáveis:**
- Invariantes documentadas e implementadas para os 5 Aggregate Roots (Company, Customer, Supplier, Trip, Proposal) via `__post_init__` + exceções de domínio (`InvariantViolationError`/`StructuralValidationError` em `src/domain/shared/exceptions.py`) e guards reutilizáveis (`src/domain/shared/guards.py`).
- Validações estruturais em todo Value Object do Shared Kernel (Identifier, Email, Phone, Address, DocumentNumber, DateRange, Money) e novos VOs `CountryCode`/`LanguageCode`.
- Enums estruturais: `DocumentType`, `PhoneType`, `Currency` (shared); `PassengerType` (customer); `SupplierCategory` (supplier); `AirportType` (trip); `ProposalDimension`, `ProposalStatus`, `ProposalVersionStatus` (proposal).
- `Proposal` formalizada como Aggregate de Coordenação — [ADR 0007](docs/decisoes/0007-proposal-aggregate-de-coordenacao.md).
- `src/domain/events/` preparada (sem eventos implementados) — lista de eventos previstos documentada.
- [docs/domain-decisions.md](docs/domain-decisions.md) — 9 decisões de modelagem granulares registradas.
- `schemas/` revisado: `required` estrutural e `enum` estrutural adicionados (nunca de negócio).
- `docs/glossary.md`, `docs/bounded-context-map.md`, `docs/universal-proposal-model.md`, `docs/ARCHITECTURE.md`, `README.md` atualizados.
- [ADR 0008](docs/decisoes/0008-sprint-1b-invariantes-e-validacoes.md) — abordagem técnica geral da sprint.
- `examples/domain_example.py` — substitui o exemplo da Sprint 1A; executado com sucesso, incluindo demonstração de rejeição de dado inválido.

**Critérios de aceite:**
- Nenhuma regra comercial da 027 foi implementada — ✅ (`Financial.payment_method` permanece texto livre; valores de `ProposalClassification` continuam sem enum).
- Toda invariante/validação tem correspondência em `schemas/` — ✅.
- Domínio rejeita dado estruturalmente inválido em tempo de construção — ✅ (demonstrado em `examples/domain_example.py`).

---

## Sprint B1 — Descoberta Profunda do Negócio ✅ concluída (estrutura)

**Objetivo:** aprofundar a descoberta da Sprint 0.5 com um método mais rigoroso — entrevistas conduzidas a partir de casos reais ("conte uma venda real"), não perguntas genéricas — e preparar onde esse conhecimento deve ser registrado, antes de qualquer regra virar código. Ver [ADR 0009](docs/decisoes/0009-sprint-b1-descoberta-por-casos-reais.md).

**Pré-requisito:** Sprint 1B concluída (domínio pronto para receber regra real).

**Entregáveis:**
- `docs/business-cases/` — 12 casos iniciais (venda nacional, venda internacional, grupo, viagem religiosa, corporativo, Disney, cancelamento, remarcação, alteração de passageiros, alteração de hotel, alteração de voo, emissão urgente), todos vazios, com template completo (contexto, sequência cronológica, decisões, documentos, aprovações, alterações, retrabalho, comunicação, riscos, problemas, exceções, lições aprendidas, possíveis regras de negócio) e perguntas específicas por tipo de caso.
- `knowledge/` (`suppliers/`, `airlines/`, `hotels/`, `insurance/`, `destinations/`, `payments/`) — estrutura vazia para conhecimento de referência (fornecedores, destinos, pagamentos), distinta das histórias de `business-cases/`.
- `docs/discovery-workshop.md` reestruturado: cada Workshop agora pede casos reais primeiro, perguntas abertas viram sondagem de acompanhamento; novo "Protocolo pós-entrevista" (7 passos, sempre executado ao final de cada sessão).

**Critérios de aceite:**
- Estrutura de `business-cases/` e `knowledge/` existe e está documentada — ✅.
- Nenhum conteúdo foi inventado — todos os 12 casos permanecem "a preencher" até uma entrevista real — ✅.
- Existe um protocolo claro de como transformar uma entrevista em atualização de `business-rules.md`/`proposal-types.md`/`proposal-lifecycle.md`/`domain-decisions.md`/`glossary.md` — ✅.
- **Pendente (fora do escopo desta sprint, é o próximo passo real):** conduzir as entrevistas de fato — nenhum caso foi preenchido ainda.

---

## Sprint 1C — Regras Comerciais (proposta, não iniciada)

**Objetivo:** completar o que a Sprint 1B deliberadamente não fez — validações, obrigatoriedades e enums que dependem de decisão comercial da 027 (formas de pagamento, valores de `ProposalClassification`, política de cancelamento/validade, os 9 estados ricos de `docs/proposal-status.md`).

**Pré-requisito:** ao menos os casos de `docs/business-cases/` relacionados aos Workshops 1 e 2 (venda nacional, venda internacional, cancelamento, remarcação) preenchidos via entrevista real, e as regras correspondentes migradas para `docs/business-rules.md` como "conhecidas" (não pendentes) — ver Protocolo pós-entrevista em `docs/discovery-workshop.md`.

**Nota:** número de sprint provisório — ver recomendação de próximos passos ao final da entrega da Sprint B1.

---

## Sprint 2 — Layout HTML

**Objetivo:** criar o template visual da proposta comercial em HTML.

**Entregáveis:**
- Template HTML em `templates/propostas/html/`, usando dados do modelo da Sprint 1B.
- Uso da identidade visual da 027 Viagens (`assets/logo/`, `assets/imagens/`).
- Proposta de exemplo gerada em `output/propostas/html/` a partir de um dado de `examples/`.

**Critérios de aceite:**
- Proposta renderiza corretamente a partir de um dado de exemplo.
- Layout aprovado visualmente pelo time da 027 Viagens.

---

## Sprint 3 — Geração do PDF

**Objetivo:** gerar PDF profissional em papel timbrado a partir do mesmo conteúdo do HTML.

**Entregáveis:**
- Arte-base do papel timbrado em `assets/papel_timbrado/`.
- Template de PDF em `templates/propostas/pdf/`.
- Gerador de PDF em `src/infrastructure/`.
- PDF de exemplo em `output/propostas/pdf/`.

**Critérios de aceite:**
- PDF gerado é visualmente consistente com o HTML e usa o papel timbrado oficial.
- Conteúdo do PDF é idêntico (mesma fonte de dados) ao da proposta HTML.

---

## Sprint 4 — Prompt Mestre

**Objetivo:** criar um prompt padrão que permita gerar/preencher propostas com apoio de IA a partir de informações em texto livre.

**Entregáveis:**
- Prompt Mestre documentado em `prompts/`.
- Exemplos de entrada em texto livre → saída no modelo de dados da Sprint 1B, em `examples/`.

**Critérios de aceite:**
- Prompt consegue transformar uma descrição em texto livre da viagem em dados estruturados válidos segundo o modelo.
- Resultado é revisável por um humano antes da geração final.

---

## Sprint 5 — Validação automática

**Objetivo:** garantir que dados incompletos ou inconsistentes sejam identificados antes da geração da proposta.

**Entregáveis:**
- Regras de validação em `src/domain/`.
- Mensagens de erro claras indicando o que falta/está incorreto.

**Critérios de aceite:**
- Dados incompletos ou inválidos bloqueiam a geração e indicam claramente o problema.
- Dados válidos passam sem falso-positivo.

---

## Sprint 6 — Integração com Coda

**Objetivo:** permitir que os dados estruturados da proposta alimentem o Coda/CRM.

**Entregáveis:**
- Definição do schema de integração (tabela/API) em `docs/decisoes/`.
- Gerador de payload compatível com Coda em `src/infrastructure/`.

**Critérios de aceite:**
- Dados de uma proposta podem ser enviados/registrados no Coda sem transformação manual.

---

## Sprint 7 — Integração com WhatsApp

**Objetivo:** automatizar o envio (ou preparação de envio) da mensagem de WhatsApp gerada.

**Entregáveis:**
- Definição do método de integração (API oficial do WhatsApp Business vs. link `wa.me`) em `docs/decisoes/`.
- Implementação da geração/envio em `src/infrastructure/`.

**Critérios de aceite:**
- Mensagem gerada pode ser enviada ao cliente com o mínimo de passos manuais possível.

---

## Sprint 8 — Melhorias e IA

**Objetivo:** iterar sobre o sistema já funcionando, incorporando melhorias e uso de IA além do Prompt Mestre.

**Entregáveis:**
- Backlog de melhorias identificadas nos sprints anteriores, priorizado.
- Melhorias de UX/conteúdo com apoio de IA (ex: sugestões de upsell, textos alternativos).

**Critérios de aceite:**
- Melhorias entregues não quebram nenhuma funcionalidade validada nos sprints anteriores.

---

## Visão de longo prazo (pós Motor de Propostas)

Os sprints acima cobrem o **Motor de Propostas** (módulo 1 da Plataforma de Documentos Comerciais — ver `docs/vision.md` e `docs/ARCHITECTURE.md`). Sem compromisso de prazo, e priorizados conforme a necessidade do negócio, os próximos ciclos de desenvolvimento devem cobrir:

**Novos módulos de documento** (mesmo padrão do Motor de Propostas — schema + template + gerador, ver `ARCHITECTURE.md` seção 7):
- Motor de Contratos
- Motor de Vouchers
- Motor de Itinerários
- Confirmações de Reserva
- Recibos
- Checklists do Passageiro
- Relatórios

**Capacidades de plataforma** (consomem o Modelo Universal já produzido pelos módulos de documento):
- CRM
- Portal Administrativo
- Portal do Cliente
- IA Comercial (construída sobre a estrutura preparada em `ai/`)
- Automação de WhatsApp
- Integrações externas (além de Coda)

Cada item desta lista, quando priorizado, ganha seu próprio ciclo de sprints detalhado (objetivo, entregáveis, critérios de aceite), seguindo a mesma estrutura usada acima para o Motor de Propostas.
