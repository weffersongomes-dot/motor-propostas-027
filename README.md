# Motor de Propostas Comerciais — 027 Viagens

Sistema para geração automatizada de propostas comerciais de viagem: a partir dos dados de uma viagem, produz proposta em HTML, PDF em papel timbrado, mensagem de WhatsApp, e-mail de envio e dados estruturados para integração futura com CRM.

## Visão geral

Hoje, montar uma proposta comercial na 027 Viagens é um processo manual: reunir informações da viagem, formatar texto, montar PDF, escrever mensagem de WhatsApp e e-mail — tudo repetido a cada cliente. O Motor de Propostas centraliza essa lógica: os dados da viagem entram uma única vez e todos os formatos de saída são gerados de forma consistente, padronizada e rápida.

## Objetivo

Reduzir o tempo e o retrabalho na emissão de propostas comerciais, garantindo padronização visual e de conteúdo, e preparar a base para automações futuras (CRM, WhatsApp, IA).

## Arquitetura proposta

Arquitetura modular, separando claramente **dados de entrada**, **regras de negócio** e **apresentação**:

```
Entrada de dados (dados da viagem)
        │
        ▼
  src/models/        → valida e estrutura os dados da proposta
        │
        ▼
  src/core/          → regras de negócio (cálculos, validações, nomenclatura)
        │
        ▼
  src/generators/    → um gerador por formato de saída
        │
        ├── generator_html.*      → templates/html/      → output/html/
        ├── generator_pdf.*       → templates/pdf/       → output/pdf/
        ├── generator_whatsapp.*  → templates/whatsapp/
        ├── generator_email.*     → templates/email/
        └── generator_crm.*       → dados estruturados (JSON) → output/json/
```

Cada gerador consome o mesmo objeto de proposta (vindo de `src/models/`) e é responsável apenas pela apresentação no seu formato — a regra de negócio (o "o quê") fica em `src/core/`, nunca duplicada entre os geradores.

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
├── PRD.md                 → requisitos do produto
├── ROADMAP.md             → plano de sprints
├── CHANGELOG.md           → histórico de mudanças
├── .gitignore
├── assets/
│   ├── logo/              → logomarca da 027 Viagens
│   ├── imagens/           → imagens usadas nas propostas (destinos, hotéis, etc.)
│   └── papel_timbrado/    → arte-base do papel timbrado para o PDF
├── docs/
│   └── decisoes/          → registro de decisões técnicas importantes (ADRs)
├── prompts/                → prompts (ex: "Prompt Mestre" de geração assistida por IA)
├── templates/
│   ├── html/               → template da proposta em HTML
│   ├── pdf/                → template do PDF em papel timbrado
│   ├── whatsapp/            → template da mensagem de WhatsApp
│   └── email/               → template do e-mail de envio
├── examples/                → exemplos de entrada/saída para referência e testes
├── output/                  → saídas geradas (não versionado — ver .gitignore)
│   ├── html/
│   ├── pdf/
│   └── json/
├── scripts/                 → scripts utilitários (setup, geração em lote, etc.)
└── src/
    ├── models/              → estrutura/validação dos dados da proposta
    ├── core/                → regras de negócio (separadas da apresentação)
    ├── generators/           → geradores de cada formato de saída
    └── utils/                → funções auxiliares compartilhadas
```

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

Detalhes de objetivos, entregáveis e critérios de aceite de cada sprint estão em [ROADMAP.md](ROADMAP.md).

## Instruções para desenvolvimento

> Ambiente de desenvolvimento (linguagem, dependências, comandos de setup) será definido no Sprint 1, junto com o modelo de dados. Por ora, o projeto contém apenas estrutura e documentação.

Convenções a seguir em todo o projeto:

- **Arquitetura modular** — cada módulo com responsabilidade única.
- **Sem duplicação de código** — regra de negócio vive em um único lugar (`src/core/`).
- **Decisões importantes documentadas** em `docs/decisoes/`.
- **Separação entre regra de negócio e apresentação** — `src/core/` nunca deve conter HTML/texto de template; `templates/` nunca deve conter lógica de cálculo ou validação.
- **Nomes claros** para arquivos e diretórios, em português, consistentes com o domínio do negócio (viagem, proposta, cliente).
- Toda mudança relevante deve ser registrada em [CHANGELOG.md](CHANGELOG.md).

## Documentos do projeto

- [PRD.md](PRD.md) — requisitos completos do produto
- [ROADMAP.md](ROADMAP.md) — plano de sprints detalhado
- [CHANGELOG.md](CHANGELOG.md) — histórico de mudanças
