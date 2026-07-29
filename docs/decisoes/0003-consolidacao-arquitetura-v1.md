# 0003 — Consolidação da Arquitetura v1.0

- **Status:** aceita
- **Data:** 2026-07-28

## Contexto

Com a estrutura de pastas e o `ARCHITECTURE.md` já definidos (ADRs [0001](0001-estrutura-inicial-do-projeto.md) e [0002](0002-evolucao-para-plataforma-de-documentos.md)), faltava consolidar a fundação da plataforma antes do Sprint 1: documentar a visão de produto de forma independente da arquitetura técnica, estruturar onde as regras comerciais da 027 Viagens vão viver, especificar formalmente o objeto central do Motor de Propostas, e formalizar uma etapa de normalização de dados que ainda não estava explícita no fluxo.

## Decisão

- Criar `docs/vision.md` — problema, público, transformação entregue, visão de 5 anos e princípios inquebráveis, como referência independente de código para qualquer pessoa (ou IA) que entre no projeto.
- Criar `docs/business-rules.md` — recipiente estruturado para todas as regras comerciais conhecidas da 027 Viagens, com seções explicitamente marcadas como pendentes onde a regra ainda não foi definida, em vez de inventadas.
- Criar `docs/universal-proposal-model.md` — especificação do Modelo Universal da Proposta (12 seções + metadata obrigatória), a fonte única de dados que todo gerador do Motor de Propostas deve consumir.
- Atualizar `docs/ARCHITECTURE.md`: adicionar a etapa **Normalização** ao fluxo de dados obrigatório (entre Validação e Regras de negócio); adicionar a seção **Modelo Universal da Proposta**; separar "módulos de documento" de "capacidades de plataforma" na lista de módulos futuros (CRM, Notificações, Automação de WhatsApp, IA Comercial, Portal Administrativo, Portal do Cliente, Integrações externas).
- Criar a estrutura `ai/` (prompts, personas, validators, instructions, knowledge) como preparação para a futura capacidade de IA Comercial — sem nenhuma implementação.
- Atualizar `ROADMAP.md` com uma seção de visão de longo prazo, listando módulos e capacidades esperados após o Motor de Propostas.

## Motivo

- Separar "visão de produto" (`vision.md`) de "arquitetura técnica" (`ARCHITECTURE.md`) evita que os princípios inquebráveis do projeto fiquem implícitos ou dependam de interpretar código/estrutura de pastas.
- Registrar regras comerciais mesmo incompletas (`business-rules.md`) impede que a primeira implementação do Sprint 1 acabe "descobrindo" regras de negócio ad-hoc dentro do código, contrariando o princípio de que nenhuma regra de negócio fica escondida.
- Formalizar o Modelo Universal da Proposta antes do Sprint 1 dá ao time uma especificação para revisar e aprovar antes de ela virar `schemas/proposta.schema.json` em código — mais barato corrigir agora do que depois de implementado.
- A etapa de Normalização evita que regras de negócio precisem lidar com variações de representação do mesmo dado (ex: nomes de aeroporto/companhia aérea escritos de formas diferentes), o que geraria lógica condicional desnecessária espalhada pelo core.
- Distinguir "módulo de documento" de "capacidade de plataforma" evita tratar CRM/Portal/IA como se fossem "mais um tipo de documento" — são serviços que consomem o Modelo Universal, não produtores de documento no mesmo sentido que Propostas/Contratos/Vouchers.
- Preparar `ai/` desde já evita que, quando a IA Comercial for implementada, prompts/personas/validações fiquem espalhados improvisadamente dentro de `src/` ou `prompts/`.

## Consequências

- `schemas/proposta.schema.json` (Sprint 1) deve ser derivado de `docs/universal-proposal-model.md`, mantendo os mesmos nomes de seção e a mesma metadata obrigatória.
- Qualquer regra de negócio implementada em `src/core/` a partir do Sprint 1 deve ter uma entrada correspondente (preenchida, não mais "pendente") em `docs/business-rules.md`.
- Módulos e capacidades futuros devem ser posicionados corretamente como um ou outro na tabela de `ARCHITECTURE.md` (seção 2), e capacidades de plataforma nunca devem exigir que um módulo de documento saiba de sua existência.
