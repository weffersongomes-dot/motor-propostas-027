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

## Sprint 0.5 — Evolução para Plataforma de Documentos

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

## Sprint 1 — Modelo de dados

**Objetivo:** definir a estrutura única de dados que alimenta todos os geradores de saída.

**Entregáveis:**
- Definição do schema da "proposta" (campos, tipos, obrigatoriedade) em `src/models/`.
- Exemplo de dado de entrada válido em `examples/`.
- Documentação da decisão de linguagem/stack em `docs/decisoes/`.

**Critérios de aceite:**
- Um exemplo de viagem pode ser representado 100% pelo modelo de dados, sem campos "soltos" fora dele.
- Modelo documentado e revisável sem depender de código.

---

## Sprint 2 — Layout HTML

**Objetivo:** criar o template visual da proposta comercial em HTML.

**Entregáveis:**
- Template HTML em `templates/html/`, usando dados do modelo do Sprint 1.
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
- Exemplos de entrada em texto livre → saída no modelo de dados do Sprint 1, em `examples/`.

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
