# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

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
