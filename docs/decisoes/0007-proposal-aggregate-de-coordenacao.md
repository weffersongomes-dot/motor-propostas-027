# 0007 — Proposal como Aggregate Root de Coordenação

- **Status:** aceita
- **Data:** 2026-07-30

## Contexto

Durante a revisão arquitetural da Sprint 1B foi identificado um risco: à medida que a plataforma evolui (novos módulos, novas regras comerciais, novos comportamentos), `Proposal` é o Aggregate com maior gravidade natural para acumular responsabilidade — é o objeto central do módulo mais desenvolvido, referenciado por praticamente tudo. Sem uma regra explícita, é fácil `Proposal` crescer para "possuir" Customer, Trip, Company diretamente (em vez de referenciá-los), acumulando lógica de todos os contextos e se tornando um objeto monolítico — o oposto do baixo acoplamento que a arquitetura busca (ver `docs/bounded-context-map.md`, `docs/ARCHITECTURE.md`).

## Decisão

`Proposal` é formalizado como um **Aggregate Root de Coordenação**:

- Referencia outros Aggregates (`Company`, `Customer`, `Trip`, `Consultant`) exclusivamente por `Identifier`, nunca os possui nem os contém embutidos.
- Não é proprietária de todo o domínio — cada Aggregate (`Company`, `Customer`, `Supplier`, `Trip`) continua responsável por sua própria consistência interna, independente de `Proposal`.
- O conteúdo comercial real de uma proposta (cliente, viagem, classificação, financeiro, metadata) vive em `ProposalVersion`, nunca em `Proposal` diretamente — `Proposal` em si contém apenas `id`, `status` (estado estrutural da proposta como um todo) e o histórico de `versions`.
- Qualquer invariante que precise "saber sobre" outro Aggregate (ex: "sempre possui um Customer") é responsabilidade de `ProposalVersion` — que tem a referência — não de `Proposal`.

## Motivo

- Evita que `Proposal` se torne um "God Object": à medida que Contratos, Vouchers e outros módulos forem adicionados, cada um deve poder coordenar os mesmos Aggregates compartilhados (Company, Customer, Supplier) sem depender de `Proposal` nem competir com ela por responsabilidade sobre esses dados.
- Mantém a garantia já registrada na ADR 0006 (Trip como Aggregate independente) e na ADR 0005 (Proposal não tem "tipo" único, tem dimensões) — coordenação por referência é consistente com essas decisões anteriores, não uma peça nova solta.
- Um Aggregate de Coordenação é, por definição, mais barato de evoluir: adicionar um novo tipo de referência (ex: `insurance_policy_id` numa futura ProposalVersion) não exige tocar em `Customer`, `Trip` ou `Company`.

## Consequências

- Nenhum método futuro em `Proposal`/`ProposalVersion` deve mutar diretamente um `Customer`, `Trip`, `Company` ou `Supplier` — qualquer mudança nesses Aggregates deve passar pelo próprio Aggregate (via seu repositório, quando existir, numa sprint de infraestrutura futura).
- Regras de negócio que envolvam mais de um Aggregate (ex: "não aprovar Proposal sem Trip com ao menos um voo confirmado") pertencem a `src/application/` (orquestração), não a `Proposal` diretamente — consistente com a divisão de camadas já documentada em `ARCHITECTURE.md`.
- Módulos futuros (Motor de Contratos, Motor de Vouchers) devem seguir o mesmo padrão: um Aggregate de Coordenação próprio, referenciando por id, nunca reimplementando ou possuindo os Aggregates de Cadastro/Financeiro já existentes.
