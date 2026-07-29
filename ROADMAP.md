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

## Sprint 1A — Modelagem do Domínio

**Objetivo:** representar os objetos de domínio da plataforma (as entidades do `docs/domain-map.md`), usando a terminologia definida em `docs/glossary.md` — **sem** validações, obrigatoriedades, enums ou regras de negócio. Só a forma dos conceitos, não o comportamento deles.

**Pré-requisito:** Sprint 0.5 concluída — glossário e mapa de domínio (`docs/domain-map.md`) estáveis o suficiente para nomear os objetos sem ambiguidade.

**Entregáveis:**
- Objetos de domínio em `src/models/` para: Empresa, Cliente, Passageiro, Consultor, Fornecedor, Documento, Proposta, Viagem, Hospedagem, Voo, Serviço, Financeiro, Metadata — cada um apenas com seus atributos, sem lógica.
- Exemplo de dado de entrada em `examples/`, usando esses objetos, ainda sem validação.
- Documentação da decisão de linguagem/stack em `docs/decisoes/`.

**Critérios de aceite:**
- Todo objeto de domínio usa exatamente os nomes definidos em `docs/glossary.md` (Linguagem Ubíqua).
- Nenhuma validação, obrigatoriedade, enum ou regra de negócio presente nesta etapa — isso é responsabilidade da Sprint 1B.
- Um exemplo de viagem pode ser representado 100% pelos objetos de domínio, sem campos "soltos" fora deles.

---

## Sprint 1B — Evolução do Modelo

**Objetivo:** adicionar aos objetos de domínio da Sprint 1A tudo que os torna um schema utilizável de verdade: validações, obrigatoriedades, enums, restrições, regras comerciais, financeiras e operacionais — com base no que for confirmado na Sprint 0.5 (tipos de proposta por dimensão, ciclo de vida, status, ações, versionamento, `business-rules.md`).

**Pré-requisito:** Sprint 1A concluída; perguntas críticas do negócio (ver `docs/business-rules.md`, grupos Comerciais/Financeiras/Operacionais/Legais) respondidas o suficiente para que o Modelo Universal da Proposta represente a operação real.

**Entregáveis:**
- Schema formal da proposta (`schemas/proposta.schema.json`), com tipos, obrigatoriedade, enums e restrições, derivado dos objetos de domínio da Sprint 1A e de `docs/universal-proposal-model.md` já validado com as respostas da Sprint 0.5.
- Validações correspondentes em `src/core/`.

**Critérios de aceite:**
- Todo campo obrigatório, enum e restrição tem lastro em uma regra registrada (não pendente) em `docs/business-rules.md`.
- Modelo documentado e revisável sem depender de código.

---

## Sprint 2 — Layout HTML

**Objetivo:** criar o template visual da proposta comercial em HTML.

**Entregáveis:**
- Template HTML em `templates/html/`, usando dados do modelo da Sprint 1B.
- Uso da identidade visual da 027 Viagens (`assets/logo/`, `assets/imagens/`).
- Proposta de exemplo gerada em `output/html/` a partir de um dado de `examples/`.

**Critérios de aceite:**
- Proposta renderiza corretamente a partir de um dado de exemplo.
- Layout aprovado visualmente pelo time da 027 Viagens.

---

## Sprint 3 — Geração do PDF

**Objetivo:** gerar PDF profissional em papel timbrado a partir do mesmo conteúdo do HTML.

**Entregáveis:**
- Arte-base do papel timbrado em `assets/papel_timbrado/`.
- Template de PDF em `templates/pdf/`.
- Gerador de PDF em `src/generators/`.
- PDF de exemplo em `output/pdf/`.

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
- Regras de validação em `src/core/`.
- Mensagens de erro claras indicando o que falta/está incorreto.

**Critérios de aceite:**
- Dados incompletos ou inválidos bloqueiam a geração e indicam claramente o problema.
- Dados válidos passam sem falso-positivo.

---

## Sprint 6 — Integração com Coda

**Objetivo:** permitir que os dados estruturados da proposta alimentem o Coda/CRM.

**Entregáveis:**
- Definição do schema de integração (tabela/API) em `docs/decisoes/`.
- Gerador de payload compatível com Coda em `src/generators/`.

**Critérios de aceite:**
- Dados de uma proposta podem ser enviados/registrados no Coda sem transformação manual.

---

## Sprint 7 — Integração com WhatsApp

**Objetivo:** automatizar o envio (ou preparação de envio) da mensagem de WhatsApp gerada.

**Entregáveis:**
- Definição do método de integração (API oficial do WhatsApp Business vs. link `wa.me`) em `docs/decisoes/`.
- Implementação da geração/envio em `src/generators/`.

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
