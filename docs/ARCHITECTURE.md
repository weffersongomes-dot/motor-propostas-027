# Arquitetura — Plataforma de Documentos Comerciais (027 Viagens)

Este documento é a referência técnica principal do projeto. Qualquer decisão de implementação deve ser compatível com o que está descrito aqui; qualquer mudança relevante de arquitetura deve atualizar este documento e registrar o porquê em `docs/decisoes/`.

## 1. Visão geral

O projeto deixou de ser apenas um "gerador de propostas" para ser concebido como uma **Plataforma de Documentos Comerciais da 027 Viagens**. A plataforma existe para transformar dados de uma viagem/cliente em qualquer documento comercial ou institucional que a operação precise emitir — sempre a partir da mesma base de dados, das mesmas regras de negócio e dos mesmos blocos visuais.

O **Motor de Propostas** é o primeiro módulo dessa plataforma. Os módulos seguintes reaproveitam a mesma arquitetura, sem exigir refatoração do que já existe.

## 2. Módulos

| Módulo | Status |
|---|---|
| Motor de Propostas | Em planejamento (Sprint 1 em diante) |
| Motor de Contratos | Futuro |
| Motor de Vouchers | Futuro |
| Motor de Itinerários | Futuro |
| Confirmações de Reserva | Futuro |
| Recibos | Futuro |
| Checklists do Passageiro | Futuro |
| Relatórios | Futuro |
| Documentos institucionais (outros) | Futuro |

Cada módulo é, na prática, **um novo tipo de documento**: um schema (`schemas/`), um conjunto de templates por formato (`templates/<modulo>/`), geradores próprios (`src/generators/<modulo>/`) e, quando necessário, regras de negócio específicas em `src/core/`. Módulos **não** se comunicam diretamente entre si — todos dependem apenas das camadas compartilhadas (`config/`, `components/`, `content/`, `src/core/`, `src/models/`).

## 3. Fluxo de dados obrigatório

Todo documento gerado pela plataforma — de qualquer módulo — segue exatamente este fluxo, sem exceção:

```
Entrada dos dados
        ↓
Validação
        ↓
Regras de negócio
        ↓
Enriquecimento dos dados
        ↓
Modelo único do documento (JSON)
        ↓
├── HTML
├── PDF
├── WhatsApp
├── E-mail
└── CRM / Coda
```

- **Entrada dos dados** — dados brutos da viagem/cliente/pagamento, no formato descrito em `schemas/`.
- **Validação** — `src/core/` confere completude e consistência contra o schema correspondente. Dado inválido interrompe o fluxo com mensagem clara (não avança "quebrado").
- **Regras de negócio** — cálculos, parcelamento, política aplicável, seleção automática de textos por tipo de viagem — tudo centralizado em `src/core/`.
- **Enriquecimento dos dados** — junção com informações de `config/` (dados institucionais) e `content/` (textos institucionais/comerciais escolhidos pelas regras de negócio), formando o conjunto completo de dados que o documento final vai exibir.
- **Modelo único do documento (JSON)** — a única fonte de verdade a partir daqui. Nenhum gerador busca dado em outro lugar além deste modelo já validado e enriquecido.
- **Saídas** — cada gerador (`src/generators/<modulo>/`) apenas apresenta o modelo único no seu formato, usando `templates/<modulo>/<formato>/` e os blocos de `components/`.

Se um gerador precisar de um dado que não está no modelo único, o problema está em uma etapa anterior (enriquecimento incompleto) — nunca se resolve buscando o dado direto na origem dentro do gerador.

## 4. Responsabilidades de cada camada

| Camada | Responsabilidade | Não deve conter |
|---|---|---|
| `schemas/` | Definir a estrutura formal de cada tipo de dado (proposta, cliente, viagem, pagamento, empresa, e futuros documentos) | Lógica, texto, apresentação |
| `config/` | Dados institucionais/comerciais fixos da empresa (CNPJ, contatos, pagamento, políticas) | Dados de um cliente específico; texto longo (isso é `content/`) |
| `content/` | Textos institucionais e comerciais (políticas por extenso, e-mails-modelo, WhatsApp-modelo, FAQ, diferenciais) | Dados estruturados (isso é `config/`); lógica de quando usar cada texto (isso é `src/core/`) |
| `src/models/` | Carregar e representar os dados (schemas em código), validar contra `schemas/` | Regra de negócio, apresentação |
| `src/core/` | Toda a inteligência: cálculos, parcelamento, validações, regras comerciais, seleção automática de textos/diferenciais por tipo de viagem | HTML, CSS, texto de WhatsApp/e-mail, qualquer marcação de apresentação |
| `components/` | Blocos de apresentação reutilizáveis (cabeçalho, rodapé, bloco de voo, bloco de hotel, bloco financeiro, assinatura, QR code, diferenciais, observações), por formato | Cálculo, decisão, validação |
| `templates/<modulo>/<formato>/` | Composição final de um documento num formato, a partir de `components/` e do modelo único | Regra de negócio, dado institucional fixo |
| `src/generators/<modulo>/` | Orquestrar: pegar o modelo único, montar o template certo, produzir o artefato final (arquivo HTML/PDF, texto de WhatsApp/e-mail, payload JSON) | Cálculo ou validação (chama `src/core/`, não reimplementa) |
| `output/<modulo>/<formato>/` | Artefatos gerados (não versionado — dados de cliente) | — |
| `prompts/` | Prompts para geração/preenchimento assistido por IA (ex: Prompt Mestre) | — |
| `examples/` | Exemplos de entrada/saída para referência | — |
| `tests/` | Casos de teste com viagens fictícias, cobrindo cenários reais do negócio | — |

## 5. Estrutura de pastas

```
motor-propostas-027/
├── README.md
├── PRD.md
├── ROADMAP.md
├── CHANGELOG.md
├── .gitignore
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
│   └── decisoes/                  → ADRs (decisões técnicas registradas)
├── examples/                      → exemplos de entrada/saída
├── output/                        → artefatos gerados, por módulo e formato (não versionado)
│   └── propostas/
│       ├── html/
│       ├── pdf/
│       └── json/
├── prompts/                       → Prompt Mestre e afins
├── schemas/                       → modelos JSON (proposta, cliente, viagem, pagamento, empresa...)
├── scripts/                       → scripts utilitários
├── src/
│   ├── models/                    → carregamento/validação dos dados (compartilhado entre módulos)
│   ├── core/                      → regras de negócio (compartilhado entre módulos)
│   ├── generators/
│   │   └── propostas/             → Motor de Propostas (módulo 1)
│   └── utils/
├── templates/
│   └── propostas/                 → templates do Motor de Propostas, por formato
│       ├── html/
│       ├── pdf/
│       ├── whatsapp/
│       └── email/
└── tests/
    └── casos/                     → viagens fictícias para teste
```

Um novo módulo (ex: Motor de Contratos) adiciona `templates/contratos/`, `src/generators/contratos/`, `schemas/contrato.schema.json`, conteúdo próprio em `content/` e casos próprios em `tests/casos/` — sem alterar nada do que já existe para `propostas/`.

## 6. Estratégia de expansão

Para adicionar um novo tipo de documento à plataforma:

1. Definir o schema em `schemas/<documento>.schema.json`, reaproveitando `cliente`, `viagem`, `pagamento`, `empresa` sempre que possível.
2. Adicionar regras de negócio específicas (se houver) em `src/core/`, sem duplicar as já existentes.
3. Criar `templates/<documento>/<formato>/`, reaproveitando `components/` já existentes; criar novos componentes apenas se o documento exigir um bloco visual inédito.
4. Criar `src/generators/<documento>/`, seguindo o mesmo fluxo de dados obrigatório (seção 3).
5. Adicionar textos institucionais/comerciais específicos em `content/`.
6. Adicionar casos de teste fictícios em `tests/casos/`.
7. Documentar a decisão em `docs/decisoes/` se houver qualquer desvio ou extensão do padrão.

Nenhum passo acima exige alterar módulos já existentes — é isso que garante crescimento sem grandes refatorações.

## 7. Boas práticas adotadas

- **Modelo único como contrato entre camadas** — geradores e templates só conhecem o modelo já validado/enriquecido, nunca a origem bruta dos dados.
- **Templates sem lógica** — HTML, PDF, WhatsApp e e-mail apenas apresentam; qualquer decisão ("mostrar isso se...", "calcular aquilo...") pertence a `src/core/`.
- **Nada institucional fixo no código** — CNPJ, contatos, formas de pagamento, políticas e textos vivem em `config/` e `content/`, editáveis sem tocar em código.
- **Baixo acoplamento entre módulos** — um módulo de documento não depende de outro, apenas das camadas compartilhadas.
- **Alta coesão por camada** — cada pasta tem uma responsabilidade única (ver seção 4).
- **Reutilização por padrão** — `components/`, `content/` e as partes de `schemas/` comuns a todos os documentos (cliente, viagem, pagamento, empresa) existem justamente para não recriar a cada módulo novo.
- **Decisões registradas** — mudanças arquiteturais relevantes viram um ADR em `docs/decisoes/`, não só uma conversa perdida.
- **Preparação para integrações futuras** — o "Modelo único do documento (JSON)" é, por construção, o payload que qualquer integração futura (Coda, CRM, WhatsApp Business API) vai consumir; nenhuma integração deve exigir mudar a estrutura interna dos módulos.
