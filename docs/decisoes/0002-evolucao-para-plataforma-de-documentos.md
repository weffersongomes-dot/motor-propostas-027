# 0002 — Evolução para Plataforma de Documentos Comerciais

- **Status:** aceita
- **Data:** 2026-07-28

## Contexto

O projeto foi planejado inicialmente (ADR [0001](0001-estrutura-inicial-do-projeto.md)) como um "Motor de Propostas Comerciais". Antes de iniciar a implementação funcional, ficou claro que a 027 Viagens vai precisar, no futuro, gerar outros tipos de documento além da proposta: contratos, vouchers, itinerários, confirmações de reserva, recibos, checklists do passageiro, relatórios e outros documentos institucionais. Todos esses documentos compartilham a mesma necessidade: partir de dados de viagem/cliente e gerar HTML, PDF, WhatsApp, e-mail e dados estruturados para CRM.

## Decisão

- Reposicionar o projeto como uma **Plataforma de Documentos Comerciais**, da qual o **Motor de Propostas** é o primeiro módulo.
- Adicionar as camadas `config/`, `components/`, `content/`, `schemas/` e `tests/`, cada uma com responsabilidade única e documentada (ver `README.md` de cada pasta e `docs/ARCHITECTURE.md`).
- Reorganizar `templates/`, `output/` e `src/generators/` para serem **aninhados por módulo/tipo de documento** (`templates/propostas/`, `output/propostas/`, `src/generators/propostas/`) em vez de flat — preparando a estrutura para novos módulos sem mover ou renomear o que já existe.
- Formalizar o **fluxo de dados obrigatório** (entrada → validação → regras de negócio → enriquecimento → modelo único JSON → saídas) como regra de arquitetura, documentado em `docs/ARCHITECTURE.md`.

## Motivo

- Adicionar um novo módulo (ex: Motor de Contratos) não deve exigir mover pastas já existentes — daí a decisão de já nascer com `templates/<modulo>/`, `output/<modulo>/` e `src/generators/<modulo>/`, em vez de fazer essa migração depois, sob risco de quebrar o que já estiver em produção.
- Separar `config/` (dados institucionais) de `content/` (textos institucionais) evita que a mesma informação apareça hardcoded em múltiplos templates e formatos — mudança de política ou de CNPJ passa a ser um único ponto de edição.
- `components/` isola blocos visuais reutilizáveis entre módulos (cabeçalho, assinatura, QR code, etc.), reduzindo duplicação à medida que novos tipos de documento forem adicionados.
- `schemas/` formaliza o "contrato de dados" entre as camadas, permitindo validação automática (Sprint 5) e servindo de referência para integrações futuras (Coda, CRM).
- `tests/` com viagens fictícias (corporativa, lazer, internacional, grupo, religioso, Disney, cruzeiro) garante que a arquitetura seja validada contra a variação real do negócio, não só o caminho feliz.

## Consequências

- O PRD e o ROADMAP originais continuam válidos para o Motor de Propostas (módulo 1); a visão de produto em `README.md`/`PRD.md` foi atualizada para deixar explícito que esse é o primeiro módulo de uma plataforma maior.
- Nenhum código funcional existia antes desta mudança, então a reorganização de pastas não exigiu refatoração de lógica — apenas de estrutura.
- Módulos futuros (contratos, vouchers, etc.) devem seguir a "Estratégia de expansão" descrita em `docs/ARCHITECTURE.md` (seção 6), sem exceção.
