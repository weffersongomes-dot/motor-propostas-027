# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Added (Sprint 1A — Modelagem do Domínio)
- `docs/bounded-context-map.md` — quatro Bounded Contexts (Comercial, Operações, Financeiro, Cadastro): responsabilidades, limites, dependências, comunicação e mapeamento para os módulos técnicos de `src/domain/`.
- `src/domain/` — primeira implementação de código do projeto: Shared Kernel (`BaseEntity`, `ValueObject`, `Identifier`, `DomainEvent`, `Money`, `Email`, `Phone`, `Address`, `DocumentNumber`, `DateRange`, `Metadata`) e Entidades/Value Objects/Aggregates por Bounded Context — `company/` (Company, Consultant), `customer/` (Customer, Passenger), `supplier/` (Supplier), `trip/` (Trip, Flight, Accommodation, Service, Airport), `financial/` (Financial), `proposal/` (Proposal, ProposalVersion, ProposalClassification). Aggregate Roots: Company, Customer, Supplier, Trip, Proposal. Zero validação, obrigatoriedade, enum ou regra de negócio, conforme escopo da sprint.
- `src/application/` e `src/infrastructure/` criadas vazias, cada uma com README explicando o que vão receber e a regra de dependência (Clean Architecture).
- `examples/sprint_1a_domain_example.py` — exemplo executável que instancia e encadeia todos os objetos de domínio; executado com sucesso.
- `schemas/` reorganizado em estrutura modular por Bounded Context (`shared/`, `company/`, `customer/`, `supplier/`, `trip/`, `financial/`, `proposal/`), com um arquivo por Entidade/Value Object, reaproveitando `$ref` — forma apenas (`type`/`properties`), sem `required`/`enum` nesta sprint.
- ADR [0006](docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md) registrando: confirmação de Python como stack; Aggregate Roots definidos/estendidos; classificação de Metadata e Financial como Value Objects (não Entidades); novo Value Object `ProposalClassification`; extensões pontuais aos exemplos do briefing (Airport, schemas adicionais); estrutura Sprint 1A dos schemas.

### Changed (Sprint 1A — Modelagem do Domínio)
- `src/core/`, `src/models/`, `src/generators/`, `src/utils/` (vazias desde a criação) removidas e substituídas por `src/domain/`, `src/application/`, `src/infrastructure/`.
- `docs/ARCHITECTURE.md`, `README.md` e `ROADMAP.md` atualizados para descrever a nova estrutura de `src/` e `schemas/`, e para referenciar `docs/bounded-context-map.md`.
- `ROADMAP.md`: Sprint 1A marcada como concluída, com entregáveis finais; Sprint 1B detalhada com o que falta adicionar aos mesmos arquivos (não criar novos).

### Added (Refinamento arquitetural pré-Sprint 1A)
- `docs/domain-map.md` — representação textual das entidades do domínio (Empresa, Consultor, Cliente, Passageiro, Fornecedor, Viagem, Proposta, Versão, Documento, Emissão, Financeiro, Metadata) e seus relacionamentos/dependências.
- ADR [0005](docs/decisoes/0005-refinamento-pre-sprint-1a.md) registrando: divisão do Sprint 1 em 1A/1B, modelagem de proposta por dimensões, etapa de Qualificação, adoção formal da Linguagem Ubíqua.

### Changed (Refinamento arquitetural pré-Sprint 1A)
- `ROADMAP.md`: Sprint 1 dividida em **Sprint 1A — Modelagem do Domínio** (objetos de domínio, sem validação/regra/enum) e **Sprint 1B — Evolução do Modelo** (validações, obrigatoriedades, enums, regras).
- `docs/proposal-types.md` reescrito: "Tipo de Proposta" único substituído por quatro dimensões combináveis — Destino, Formato, Finalidade, Produto — já que uma proposta pode ser, por exemplo, Internacional + Grupo + Religiosa simultaneamente.
- `docs/proposal-lifecycle.md`: nova etapa **Qualificação** entre Lead e Primeiro contato.
- `docs/business-rules.md` reorganizado em quatro grupos: Regras Comerciais, Regras Financeiras, Regras Operacionais e Regras Legais (as 16 seções originais mantidas, apenas reagrupadas).
- `docs/discovery-workshop.md` reestruturado em cinco workshops independentes (Atendimento, Financeiro, Operação, Emissão, Pós-venda), cada um com objetivo, participantes, perguntas, documentos atualizados ao final e decisões esperadas.
- `docs/glossary.md` evoluído para funcionar explicitamente como Linguagem Ubíqua (DDD): cada termo agora tem definição oficial, contexto de uso, sinônimos aceitos, termos proibidos e impacto no código/documentação.
- `docs/ARCHITECTURE.md` e `README.md` atualizados com referências a `domain-map.md` e à divisão Sprint 1A/1B.

### Added (Sprint 0.5 — Engenharia Comercial e Descoberta do Negócio)
- `docs/glossary.md` — linguagem ubíqua (DDD): conceitos de domínio da 027 Viagens (Lead, Cliente, Passageiro, Consultor, Fornecedor, Cotação, Proposta, Versão, Status, Aprovação, Emissão, etc.), a validar com o negócio.
- `docs/proposal-types.md` — estrutura + perguntas para os 10 tipos de proposta previstos (Nacional, Internacional, Corporativo, Religioso, Grupos, Disney, Cruzeiros, Individual, Incentivo, Outros), incluindo pergunta estrutural sobre tipos combináveis.
- `docs/proposal-lifecycle.md` — ciclo de vida hipotético de Lead a Pós-venda, com objetivo/entrada/saída/responsável/documentos/exceções/dúvidas por etapa.
- `docs/proposal-status.md` — 9 status hipotéticos da proposta, com transições e ações permitidas/proibidas.
- `docs/proposal-actions.md` — 11 ações possíveis sobre uma proposta (criar, editar, duplicar, atualizar, recalcular, reenviar, cancelar, aprovar, reprovar, converter em emissão, arquivar).
- `docs/proposal-versioning.md` — estratégia de versionamento (`001` → `001.1` → `001.2`), critério de nova versão vs. atualização in-place, rastreabilidade e relacionamento entre versões.
- `docs/discovery-workshop.md` — roteiro de entrevista estruturado por assunto (Atendimento, Financeiro, Viagens, Documentação, Parcelamentos, Emissão, Pós-venda, Exceções, Casos especiais).
- ADR [0004](docs/decisoes/0004-sprint-05-engenharia-comercial.md) registrando a decisão de inserir esta sprint de descoberta antes do Sprint 1.
- Sprint 0.5 (Engenharia Comercial) no `ROADMAP.md`, com pré-requisito explícito para o Sprint 1.

### Changed
- Sprint anteriormente chamada "0.5 — Evolução para Plataforma de Documentos" renomeada para **Sprint 0.4** no `ROADMAP.md`, para liberar o número "0.5" para a Sprint de Engenharia Comercial.
- `docs/business-rules.md` reorganizado: cada seção agora segue Objetivo / Regras conhecidas / Regras pendentes / Perguntas em aberto / Observações, com tabela de prioridade antes do Sprint 1.
- `docs/ARCHITECTURE.md` e `README.md` atualizados com links para os novos documentos de descoberta.

### Added (consolidação da arquitetura v1.0)
- `docs/vision.md` — problema resolvido, público-alvo, transformação entregue, visão de 5 anos e princípios inquebráveis da plataforma.
- `docs/business-rules.md` — documento estruturado para centralizar todas as regras comerciais da 027 Viagens (políticas, pagamento, parcelamento, diferenciais, seguros, bagagens, grupos, internacional, religioso, corporativo, cancelamentos, observações obrigatórias, opcionais, upsell, cross-sell), hoje pendente de preenchimento com o time comercial.
- `docs/universal-proposal-model.md` — especificação do Modelo Universal da Proposta (metadata, empresa, consultor, cliente, passageiros, viagem, voos, hospedagem, serviços, financeiro, políticas, observações, anexos) e sua metadata obrigatória.
- Seção "Modelo Universal da Proposta" e etapa "Normalização" no fluxo de dados obrigatório em `docs/ARCHITECTURE.md`; distinção entre "módulos de documento" e "capacidades de plataforma".
- Estrutura `ai/` (prompts, personas, validators, instructions, knowledge) preparada para a futura capacidade de IA Comercial — sem implementação.
- Seção "Visão de longo prazo" no `ROADMAP.md`, cobrindo módulos e capacidades pós Motor de Propostas.
- ADR [0003](docs/decisoes/0003-consolidacao-arquitetura-v1.md) registrando esta consolidação.

### Changed
- Projeto reposicionado como **Plataforma de Documentos Comerciais** da 027 Viagens, com o Motor de Propostas como primeiro módulo (ver ADR [0002](docs/decisoes/0002-evolucao-para-plataforma-de-documentos.md)).
- `templates/`, `output/` e `src/generators/` reorganizados por módulo (`propostas/` como primeiro módulo), preparando a estrutura para novos tipos de documento sem refatoração futura.
- `README.md` e `PRD.md` atualizados para refletir a visão de plataforma.

### Added
- Novas camadas de arquitetura: `config/`, `components/` (html, pdf), `content/` (políticas, mensagens, e-mails, whatsapp, faq, diferenciais, textos comerciais), `schemas/` e `tests/` (casos), cada uma com README explicando finalidade.
- `docs/ARCHITECTURE.md` como referência técnica principal (módulos, fluxo de dados obrigatório, responsabilidades por camada, estratégia de expansão, boas práticas).
- Sprint 0.5 no `ROADMAP.md`, cobrindo esta evolução de arquitetura.
- Estrutura inicial de diretórios do projeto (`assets/`, `docs/`, `prompts/`, `templates/`, `examples/`, `output/`, `scripts/`, `src/`).
- `README.md` com visão geral, objetivo, arquitetura proposta, tecnologias sugeridas e instruções de desenvolvimento.
- `PRD.md` com problema, objetivo, público-alvo, funcionalidades, entradas/saídas, regras de negócio, critérios de sucesso, requisitos e backlog inicial.
- `ROADMAP.md` com plano de 9 sprints (Sprint 0 a Sprint 8), cada um com objetivo, entregáveis e critérios de aceite.
- `.gitignore` inicial.

[Unreleased]: https://github.com/weffersongomes-dot/motor-propostas-027/compare/main...HEAD
