# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

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
