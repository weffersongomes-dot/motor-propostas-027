# Arquitetura — Plataforma de Documentos Comerciais (027 Viagens)

Este documento é a referência técnica principal do projeto. Qualquer decisão de implementação deve ser compatível com o que está descrito aqui; qualquer mudança relevante de arquitetura deve atualizar este documento e registrar o porquê em `docs/decisoes/`.

Documentos relacionados: [`vision.md`](vision.md) (por que o projeto existe e princípios inquebráveis), [`glossary.md`](glossary.md) (Linguagem Ubíqua — conceitos de domínio, no padrão DDD), [`bounded-context-map.md`](bounded-context-map.md) (fronteiras de responsabilidade entre os contextos de negócio: Comercial, Operações, Financeiro, Cadastro), [`domain-map.md`](domain-map.md) (relacionamento entre as entidades do domínio), [`domain-decisions.md`](domain-decisions.md) (decisões de modelagem granulares, sem ADR própria), [`business-rules.md`](business-rules.md) (regras comerciais da 027 Viagens, organizadas em Comerciais/Financeiras/Operacionais/Legais) e [`universal-proposal-model.md`](universal-proposal-model.md) (especificação completa do Modelo Universal da Proposta, seção 4 abaixo), além dos documentos de descoberta de negócio — [`proposal-types.md`](proposal-types.md) (classificação por dimensões), [`proposal-lifecycle.md`](proposal-lifecycle.md), [`proposal-status.md`](proposal-status.md), [`proposal-actions.md`](proposal-actions.md), [`proposal-versioning.md`](proposal-versioning.md) e [`discovery-workshop.md`](discovery-workshop.md) — produzidos na Sprint 0.5 (Engenharia Comercial) antes de qualquer schema ser definido. A plataforma segue Domain-Driven Design: o domínio (glossário + mapa de domínio + regras) é descoberto e nomeado antes de qualquer modelagem técnica (ver [ADR 0005](decisoes/0005-refinamento-pre-sprint-1a.md)).

## 1. Visão geral

O projeto deixou de ser apenas um "gerador de propostas" para ser concebido como uma **Plataforma de Documentos Comerciais da 027 Viagens**. A plataforma existe para transformar dados de uma viagem/cliente em qualquer documento comercial ou institucional que a operação precise emitir — sempre a partir da mesma base de dados, das mesmas regras de negócio e dos mesmos blocos visuais.

O **Motor de Propostas** é o primeiro módulo dessa plataforma. Os módulos e capacidades seguintes reaproveitam a mesma arquitetura, sem exigir refatoração do que já existe. Ver [`vision.md`](vision.md) para a visão de produto de longo prazo por trás dessa decisão.

## 2. Módulos e capacidades

A plataforma distingue dois tipos de peça, porque cada um cresce de um jeito diferente:

- **Módulos de documento** — geram um artefato (HTML/PDF/WhatsApp/e-mail/JSON) a partir de um modelo de dados próprio. Seguem sempre o padrão schema + template + gerador descrito na seção 7 (Estratégia de expansão).
- **Capacidades de plataforma** — não são "um documento", são um serviço que consome e/ou alimenta os módulos de documento (ex: um CRM não gera um PDF, ele guarda e consulta propostas já geradas).

| Módulo de documento | Status |
|---|---|
| Motor de Propostas | Em desenvolvimento — domínio modelado (1A) e validado (1B) |
| Motor de Contratos | Futuro |
| Motor de Vouchers | Futuro |
| Motor de Itinerários | Futuro |
| Confirmações de Reserva | Futuro |
| Recibos | Futuro |
| Checklists do Passageiro | Futuro |
| Relatórios | Futuro |
| Documentos institucionais (outros) | Futuro |

| Capacidade de plataforma | Status |
|---|---|
| CRM | Futuro |
| Notificações | Futuro |
| Automação de WhatsApp | Futuro |
| IA Comercial | Futuro |
| Portal Administrativo | Futuro |
| Portal do Cliente | Futuro |
| Integrações externas (Coda e outras) | Futuro |

Cada módulo de documento é, na prática, **um novo tipo de documento**: Entidades/Value Objects em `src/domain/<contexto>/`, um schema (`schemas/<contexto>/`), um conjunto de templates por formato (`templates/<modulo>/`) e geradores próprios em `src/infrastructure/`. Módulos **não** se comunicam diretamente entre si — todos dependem apenas das camadas compartilhadas (`config/`, `components/`, `content/`, `src/domain/shared/`, e os Bounded Contexts de Cadastro/Financeiro quando aplicável — ver `bounded-context-map.md`).

Capacidades de plataforma consomem o mesmo Modelo Universal (seção 4) que os módulos de documento produzem — por exemplo, o CRM recebe o Modelo Universal da Proposta já pronto, nunca monta sua própria versão dos dados.

## 3. Fluxo de dados obrigatório

Todo documento gerado pela plataforma — de qualquer módulo — segue exatamente este fluxo, sem exceção:

```
Entrada
        ↓
Validação
        ↓
Normalização
        ↓
Regras de negócio
        ↓
Enriquecimento
        ↓
Modelo Universal (da Proposta, do Contrato, ...)
        ↓
Geradores
        ↓
├── PDF
├── HTML
├── WhatsApp
├── E-mail
└── CRM
```

- **Entrada** — dados brutos da viagem/cliente/pagamento, no formato descrito em `schemas/`.
- **Validação** — `src/domain/` (Sprint 1B em diante) confere completude e consistência contra o schema correspondente. Dado inválido interrompe o fluxo com mensagem clara (não avança "quebrado").
- **Normalização** — antes de qualquer regra de negócio rodar, os dados são padronizados: abreviações, nomes de companhias aéreas, nomes de aeroportos, estados, cidades, moedas, datas, telefones, documentos. Nenhuma regra de negócio deve trabalhar com dado não normalizado — é essa etapa que garante, por exemplo, que "GRU", "Guarulhos" e "Aeroporto de Guarulhos" cheguem às regras de negócio como uma única representação canônica.
- **Regras de negócio** — cálculos, parcelamento, política aplicável, seleção automática de textos por tipo de viagem — tudo centralizado como comportamento das Entidades em `src/domain/` (a partir da Sprint 1B), com as regras conhecidas documentadas em [`business-rules.md`](business-rules.md).
- **Enriquecimento** — junção com informações de `config/` (dados institucionais) e `content/` (textos institucionais/comerciais escolhidos pelas regras de negócio), formando o conjunto completo de dados que o documento final vai exibir.
- **Modelo Universal** — a única fonte de verdade a partir daqui. Para o módulo de Propostas, é o Modelo Universal da Proposta (seção 4). Nenhum gerador busca dado em outro lugar além deste modelo já validado, normalizado e enriquecido — **nenhum gerador pode buscar dados diretamente do usuário/origem**.
- **Geradores** — cada gerador (`src/infrastructure/`, por módulo) apenas apresenta o Modelo Universal no seu formato, usando `templates/<modulo>/<formato>/` e os blocos de `components/`.

Se um gerador precisar de um dado que não está no Modelo Universal, o problema está em uma etapa anterior (enriquecimento incompleto) — nunca se resolve buscando o dado direto na origem dentro do gerador.

## 4. Modelo Universal da Proposta

Todo documento gerado pelo Motor de Propostas — em qualquer formato — é produzido exclusivamente a partir de um único objeto estruturado: o **Modelo Universal da Proposta**. Nenhum gerador (HTML, PDF, WhatsApp, e-mail, CRM) lê dado de nenhuma outra fonte; todos consomem exclusivamente este modelo, já validado, normalizado e enriquecido pelas etapas anteriores.

A especificação completa (seções, campos, responsabilidade de cada uma) está em [`docs/universal-proposal-model.md`](universal-proposal-model.md). Em resumo, o modelo é composto por: `metadata`, `empresa`, `consultor`, `cliente`, `passageiros`, `viagem`, `voos`, `hospedagem`, `serviços`, `financeiro`, `políticas`, `observações` e `anexos`.

Todo Modelo Universal carrega um bloco de **metadata obrigatória**, presente mesmo quando não exibida ao cliente: `proposal_id`, `schema_version`, `engine_version`, `template`, `generated_at`, `generated_by`, `consultor`, `origem`, `status`. Essa metadata é o que permite rastrear, auditar e depurar qualquer documento emitido pela plataforma, independentemente do formato de saída.

Cada módulo futuro (Motor de Contratos, Motor de Vouchers, etc.) terá seu próprio Modelo Universal (`Modelo Universal do Contrato`, `Modelo Universal do Voucher`...), seguindo exatamente o mesmo princípio: um objeto único, com a mesma metadata obrigatória, do qual todos os geradores daquele módulo dependem exclusivamente.

## 5. Responsabilidades de cada camada

| Camada | Responsabilidade | Não deve conter |
|---|---|---|
| `schemas/` | Definir a estrutura formal de cada Entidade/Value Object, por Bounded Context (ver `bounded-context-map.md`) | Lógica, texto, apresentação |
| `config/` | Dados institucionais/comerciais fixos da empresa (CNPJ, contatos, pagamento, políticas) | Dados de um cliente específico; texto longo (isso é `content/`) |
| `content/` | Textos institucionais e comerciais (políticas por extenso, e-mails-modelo, WhatsApp-modelo, FAQ, diferenciais) | Dados estruturados (isso é `config/`); lógica de quando usar cada texto (isso é `src/domain/`) |
| `src/domain/` | Entidades, Value Objects, Aggregates — com invariantes estruturais e validações de forma desde a Sprint 1B (ver ADR 0008) — organizado por Bounded Context, com `shared/` para o que é verdadeiramente comum (ver ADR 0006) | Persistência, geração de HTML/PDF, chamadas a serviços externos, qualquer detalhe de infraestrutura, e (ainda) regra comercial da 027 — só entra quando `business-rules.md` estiver confirmado |
| `src/application/` | Casos de uso que orquestram o domínio (ex: "Aprovar Proposta") — vazio até uma sprint futura | Regra de negócio de uma única Entidade (isso é `src/domain/`), detalhe técnico (isso é `src/infrastructure/`) |
| `components/` | Blocos de apresentação reutilizáveis (cabeçalho, rodapé, bloco de voo, bloco de hotel, bloco financeiro, assinatura, QR code, diferenciais, observações), por formato | Cálculo, decisão, validação |
| `templates/<modulo>/<formato>/` | Composição final de um documento num formato, a partir de `components/` e do Modelo Universal | Regra de negócio, dado institucional fixo |
| `src/infrastructure/` | Geradores concretos por módulo (leem `templates/`/`content/`/`config/`, escrevem em `output/`), persistência (quando existir) e integrações externas (Coda, WhatsApp) — vazio até uma sprint futura | Regra de negócio (chama `src/domain/`/`src/application/`, não reimplementa) |
| `output/<modulo>/<formato>/` | Artefatos gerados (não versionado — dados de cliente) | — |
| `prompts/` | Prompts operacionais para geração/preenchimento assistido por IA (ex: Prompt Mestre) | — |
| `ai/` | Preparação para a capacidade de IA Comercial: prompts de produto, personas, validadores, instruções e base de conhecimento (ver `ai/README.md`) — estrutura vazia por enquanto | Implementação funcional (ainda) |
| `examples/` | Exemplos de entrada/saída para referência | — |
| `tests/` | Casos de teste com viagens fictícias, cobrindo cenários reais do negócio | — |

## 6. Estrutura de pastas

```
motor-propostas-027/
├── README.md
├── PRD.md
├── ROADMAP.md
├── CHANGELOG.md
├── .gitignore
├── ai/                             → preparação para IA Comercial (sem implementação ainda)
│   ├── prompts/
│   ├── personas/
│   ├── validators/
│   ├── instructions/
│   └── knowledge/
├── assets/                        → logo, imagens, papel timbrado
│   ├── logo/
│   ├── imagens/
│   └── papel_timbrado/
├── config/                        → dados institucionais (JSON), sem texto longo
├── components/                    → blocos visuais reutilizáveis, por formato
│   ├── html/
│   └── pdf/
├── content/                       → textos institucionais/comerciais
│   ├── politicas/
│   ├── mensagens/
│   ├── emails/
│   ├── whatsapp/
│   ├── faq/
│   ├── diferenciais/
│   └── textos_comerciais/
├── docs/
│   ├── ARCHITECTURE.md            → este documento
│   ├── vision.md                  → problema, público, visão de 5 anos, princípios inquebráveis
│   ├── glossary.md                → Linguagem Ubíqua (conceitos de domínio, DDD)
│   ├── bounded-context-map.md     → fronteiras entre contextos de negócio (Comercial/Operações/Financeiro/Cadastro)
│   ├── domain-map.md              → relacionamento entre as entidades do domínio
│   ├── domain-decisions.md        → decisões de modelagem granulares (sem ADR própria)
│   ├── business-rules.md          → regras comerciais (Comerciais/Financeiras/Operacionais/Legais)
│   ├── universal-proposal-model.md → especificação do Modelo Universal da Proposta
│   ├── proposal-types.md          → tipos de proposta suportados (descoberta de negócio)
│   ├── proposal-lifecycle.md      → ciclo de vida da proposta (descoberta de negócio)
│   ├── proposal-status.md         → estados possíveis da proposta (descoberta de negócio)
│   ├── proposal-actions.md        → ações possíveis sobre a proposta (descoberta de negócio)
│   ├── proposal-versioning.md     → estratégia de versionamento da proposta
│   ├── discovery-workshop.md      → roteiro de entrevistas com o negócio
│   └── decisoes/                  → ADRs (decisões técnicas registradas)
├── examples/                      → exemplos de entrada/saída
├── output/                        → artefatos gerados, por módulo e formato (não versionado)
│   └── propostas/
│       ├── html/
│       ├── pdf/
│       └── json/
├── prompts/                       → Prompt Mestre e afins
├── schemas/                       → JSON Schema modular, por Bounded Context (ver schemas/README.md)
│   ├── shared/                    → Identifier, Money, Email, Phone, Address, DocumentNumber, DateRange, Metadata
│   ├── company/, customer/, supplier/, trip/, financial/, proposal/
├── scripts/                       → scripts utilitários
├── src/
│   ├── domain/                    → Entidades, Value Objects e Aggregates, por Bounded Context — validados (Sprint 1B)
│   │   ├── shared/                → Shared Kernel (BaseEntity, ValueObject, Identifier, DomainEvent, exceptions, guards, Money, Metadata...)
│   │   ├── events/                → estrutura preparada para Domain Events (sem eventos implementados, ver src/domain/events/README.md)
│   │   ├── company/, customer/, supplier/, trip/, financial/, proposal/
│   ├── application/               → casos de uso (vazio nesta sprint, ver src/application/README.md)
│   └── infrastructure/            → geradores, persistência, integrações (vazio nesta sprint, ver src/infrastructure/README.md)
├── templates/
│   └── propostas/                 → templates do Motor de Propostas, por formato
│       ├── html/
│       ├── pdf/
│       ├── whatsapp/
│       └── email/
└── tests/
    └── casos/                     → viagens fictícias para teste
```

Um novo módulo (ex: Motor de Contratos) adiciona `templates/contratos/`, `src/domain/contract/` (novo Bounded Context técnico, se necessário), um gerador correspondente em `src/infrastructure/`, `schemas/contract/`, conteúdo próprio em `content/` e casos próprios em `tests/casos/` — sem alterar nada do que já existe para `propostas/`.

## 7. Estratégia de expansão

Para adicionar um novo tipo de documento à plataforma:

1. Modelar as Entidades/Value Objects/Aggregates do novo documento em `src/domain/<contexto>/`, reaproveitando `src/domain/shared/`, `company/`, `customer/`, `supplier/`, `financial/` sempre que possível (ver ADR 0006).
2. Definir o schema correspondente em `schemas/<contexto>/`, espelhando o domínio, reaproveitando `schemas/shared/` e os demais contextos já existentes.
3. Definir o Modelo Universal do novo documento seguindo o mesmo padrão da seção 4 (mesma metadata obrigatória, mesma regra de fonte única).
4. Adicionar regras de negócio específicas (se houver) como comportamento das Entidades em `src/domain/` ou como caso de uso em `src/application/`, sem duplicar as já existentes; documentar em `business-rules.md`.
5. Criar `templates/<documento>/<formato>/`, reaproveitando `components/` já existentes; criar novos componentes apenas se o documento exigir um bloco visual inédito.
6. Criar o gerador correspondente em `src/infrastructure/`, seguindo o mesmo fluxo de dados obrigatório (seção 3).
7. Adicionar textos institucionais/comerciais específicos em `content/`.
8. Adicionar casos de teste fictícios em `tests/casos/`.
9. Documentar a decisão em `docs/decisoes/` se houver qualquer desvio ou extensão do padrão.

Para adicionar uma capacidade de plataforma (CRM, Notificações, IA Comercial, portais, integrações externas): ela consome o Modelo Universal de um ou mais módulos de documento já existentes — nunca deve exigir que um módulo de documento saiba da existência da capacidade.

Nenhum passo acima exige alterar módulos já existentes — é isso que garante crescimento sem grandes refatorações.

## 8. Boas práticas adotadas

- **Modelo Universal como contrato entre camadas** — geradores e templates só conhecem o modelo já validado/normalizado/enriquecido, nunca a origem bruta dos dados.
- **Templates sem lógica** — HTML, PDF, WhatsApp e e-mail apenas apresentam; qualquer decisão ("mostrar isso se...", "calcular aquilo...") pertence a `src/domain/`.
- **Nada institucional fixo no código** — CNPJ, contatos, formas de pagamento, políticas e textos vivem em `config/` e `content/`, editáveis sem tocar em código.
- **Nenhuma regra de negócio escondida no código** — toda regra comercial conhecida é documentada em `business-rules.md` antes (ou junto) de virar código em `src/domain/`.
- **Domínio isolado de infraestrutura (Clean Architecture)** — `src/domain/` nunca importa de `src/application/` ou `src/infrastructure/`; a dependência é sempre de fora para dentro (ver ADR 0006).
- **Dados sempre normalizados antes de decisões** — nenhuma regra de negócio roda sobre dado bruto/não padronizado.
- **Baixo acoplamento entre módulos e capacidades** — um módulo de documento não depende de outro nem de nenhuma capacidade de plataforma; capacidades dependem do Modelo Universal, não do módulo em si.
- **Alta coesão por camada** — cada pasta tem uma responsabilidade única (ver seção 5).
- **Reutilização por padrão** — `components/`, `content/` e as partes de `schemas/` comuns a todos os documentos (cliente, viagem, pagamento, empresa) existem justamente para não recriar a cada módulo novo.
- **Decisões registradas** — mudanças arquiteturais relevantes viram um ADR em `docs/decisoes/`, não só uma conversa perdida.
- **Preparação para integrações futuras** — o Modelo Universal é, por construção, o payload que qualquer integração futura (Coda, CRM, WhatsApp Business API, IA Comercial) vai consumir; nenhuma integração deve exigir mudar a estrutura interna dos módulos.
