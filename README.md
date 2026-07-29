# Plataforma de Documentos Comerciais — 027 Viagens

Plataforma para geração automatizada dos documentos comerciais da 027 Viagens. O primeiro módulo é o **Motor de Propostas**: a partir dos dados de uma viagem, produz proposta em HTML, PDF em papel timbrado, mensagem de WhatsApp, e-mail de envio e dados estruturados para integração futura com CRM/Coda. A arquitetura é preparada para, no futuro, gerar também contratos, vouchers, itinerários, confirmações de reserva, recibos, checklists do passageiro, relatórios e outros documentos institucionais — sem exigir grandes refatorações.

## Visão geral

Hoje, montar uma proposta comercial na 027 Viagens é um processo manual: reunir informações da viagem, formatar texto, montar PDF, escrever mensagem de WhatsApp e e-mail — tudo repetido a cada cliente. O mesmo acontece, em menor escala, com outros documentos (contratos, vouchers, confirmações). A plataforma centraliza essa lógica: os dados da viagem entram uma única vez, passam por validação e regras de negócio comuns, e todo documento — de qualquer tipo — é gerado de forma consistente, padronizada e rápida.

## Objetivo

Reduzir o tempo e o retrabalho na emissão de documentos comerciais, garantindo padronização visual e de conteúdo, e preparar a base para automações futuras (CRM, WhatsApp, IA) e para novos tipos de documento além da proposta.

## Arquitetura proposta

Arquitetura modular, com separação rígida entre **dados de entrada**, **regras de negócio** e **apresentação**, e um fluxo de dados obrigatório para todo documento gerado:

```
Entrada → Validação → Normalização → Regras de negócio → Enriquecimento → Modelo Universal → Geradores → PDF / HTML / WhatsApp / E-mail / CRM
```

A descrição completa da arquitetura — módulos, camadas, responsabilidades e estratégia de expansão para novos tipos de documento — está em **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**, a referência técnica principal do projeto. A visão de produto por trás dessa arquitetura está em [docs/vision.md](docs/vision.md); as regras comerciais conhecidas em [docs/business-rules.md](docs/business-rules.md); e a especificação do objeto central do Motor de Propostas em [docs/universal-proposal-model.md](docs/universal-proposal-model.md).

## Tecnologias sugeridas

A definir com mais detalhe no Sprint 1/2, mas a direção proposta é:

- **Linguagem:** Python (bom suporte a geração de PDF/HTML, fácil de rodar em automações e scripts)
- **Templates HTML:** Jinja2
- **Geração de PDF:** WeasyPrint (HTML/CSS → PDF, aproveita o mesmo template do papel timbrado) ou similar
- **Dados estruturados:** JSON (compatível com integração futura via API com Coda)
- **Sem banco de dados nesta fase** — persistência simples em arquivo; banco de dados entra quando houver integração real (Sprint 6+)

Essas escolhas serão revisitadas e confirmadas no Sprint 1, quando o modelo de dados for definido.

## Estrutura de pastas

```
motor-propostas-027/
├── README.md              → este arquivo
├── PRD.md                 → requisitos do produto (Motor de Propostas, módulo 1)
├── ROADMAP.md             → plano de sprints
├── CHANGELOG.md           → histórico de mudanças
├── .gitignore
├── ai/                    → preparação para IA Comercial (sem implementação ainda)
├── assets/
│   ├── logo/              → logomarca da 027 Viagens
│   ├── imagens/           → imagens usadas nos documentos (destinos, hotéis, etc.)
│   └── papel_timbrado/    → arte-base do papel timbrado para o PDF
├── config/                → dados institucionais (CNPJ, contatos, pagamento, políticas) — nunca hardcoded
├── components/            → blocos visuais reutilizáveis (cabeçalho, bloco de voo, assinatura, etc.), por formato
├── content/               → textos institucionais/comerciais (políticas, e-mails-modelo, FAQ, diferenciais)
├── docs/
│   ├── ARCHITECTURE.md    → referência técnica principal
│   ├── vision.md          → problema, público, visão de 5 anos, princípios inquebráveis
│   ├── business-rules.md  → regras comerciais conhecidas da 027 Viagens
│   ├── universal-proposal-model.md → especificação do Modelo Universal da Proposta
│   └── decisoes/          → registro de decisões técnicas importantes (ADRs)
├── examples/              → exemplos de entrada/saída para referência e testes
├── output/                → saídas geradas, por módulo e formato (não versionado — ver .gitignore)
│   └── propostas/
├── prompts/               → prompts (ex: "Prompt Mestre" de geração assistida por IA)
├── schemas/               → modelos JSON dos dados (proposta, cliente, viagem, pagamento, empresa...)
├── scripts/               → scripts utilitários (setup, geração em lote, etc.)
├── src/
│   ├── models/            → carregamento/validação dos dados, compartilhado entre módulos
│   ├── core/              → regras de negócio, compartilhado entre módulos
│   ├── generators/
│   │   └── propostas/     → geradores do Motor de Propostas (módulo 1)
│   └── utils/             → funções auxiliares compartilhadas
├── templates/
│   └── propostas/         → templates do Motor de Propostas, por formato (html, pdf, whatsapp, email)
└── tests/
    └── casos/             → viagens fictícias para teste (corporativa, lazer, internacional, grupo, religioso, Disney, cruzeiro)
```

Detalhes de cada camada, incluindo como adicionar um novo tipo de documento sem refatorar os módulos existentes, estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Roadmap resumido

| Sprint | Foco |
|---|---|
| 0 | Estrutura do projeto e documentação |
| 1 | Modelo de dados da proposta |
| 2 | Layout HTML da proposta |
| 3 | Geração do PDF em papel timbrado |
| 4 | Prompt Mestre (geração assistida por IA) |
| 5 | Validação automática dos dados |
| 6 | Integração com Coda |
| 7 | Integração com WhatsApp |
| 8 | Melhorias e IA |

Detalhes de objetivos, entregáveis e critérios de aceite de cada sprint estão em [ROADMAP.md](ROADMAP.md). O Roadmap cobre o Motor de Propostas (módulo 1); módulos futuros (contratos, vouchers, etc.) terão seu próprio ciclo de sprints quando priorizados.

## Instruções para desenvolvimento

> Ambiente de desenvolvimento (linguagem, dependências, comandos de setup) será definido no Sprint 1, junto com o modelo de dados. Por ora, o projeto contém apenas estrutura e documentação.

Convenções a seguir em todo o projeto:

- **Arquitetura modular** — cada módulo de documento (proposta, contrato, voucher...) é independente dos demais, dependendo só das camadas compartilhadas (`config/`, `components/`, `content/`, `src/core/`, `src/models/`).
- **Sem duplicação de código** — regra de negócio vive em um único lugar (`src/core/`).
- **Decisões importantes documentadas** em `docs/decisoes/`.
- **Separação entre regra de negócio e apresentação** — `src/core/` nunca deve conter HTML/texto de template; `templates/` e `components/` nunca devem conter lógica de cálculo ou validação.
- **Nada institucional fixo no código** — dados da empresa em `config/`, textos institucionais em `content/`.
- **Fluxo de dados obrigatório** — todo documento segue entrada → validação → regras de negócio → enriquecimento → modelo único → saídas (ver `docs/ARCHITECTURE.md`).
- **Nomes claros** para arquivos e diretórios, em português, consistentes com o domínio do negócio (viagem, proposta, cliente).
- Toda mudança relevante deve ser registrada em [CHANGELOG.md](CHANGELOG.md).

## Documentos do projeto

- [docs/vision.md](docs/vision.md) — visão de produto, público e princípios inquebráveis
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — arquitetura completa da plataforma
- [docs/business-rules.md](docs/business-rules.md) — regras comerciais conhecidas da 027 Viagens
- [docs/universal-proposal-model.md](docs/universal-proposal-model.md) — especificação do Modelo Universal da Proposta
- [PRD.md](PRD.md) — requisitos completos do produto (Motor de Propostas)
- [ROADMAP.md](ROADMAP.md) — plano de sprints detalhado
- [CHANGELOG.md](CHANGELOG.md) — histórico de mudanças
