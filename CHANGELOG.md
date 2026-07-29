# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

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
