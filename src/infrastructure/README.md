# src/infrastructure/

Camada de infraestrutura (Clean Architecture) — **vazia nesta sprint**. É onde detalhes técnicos concretos vivem: geração de HTML/PDF, leitura de `templates/`/`content/`/`config/`, persistência, e futuras integrações externas (Coda, WhatsApp).

## O que vai entrar aqui (a partir da Sprint 2/3, e integrações do Sprint 6/7)

- Implementações concretas dos geradores por módulo (`src/generators/propostas/` da estrutura original passa a viver logicamente aqui, ex: `infrastructure/generators/propostas/`), lendo `templates/`, `components/` e `content/`.
- Adaptadores de persistência, se/quando a plataforma passar a ter banco de dados (ver `ARCHITECTURE.md`, Sprint 6+).
- Clientes de integração externa (Coda, WhatsApp Business API).

## Regra de dependência

`src/infrastructure/` pode depender de `src/domain/` e `src/application/`. Nem `src/domain/` nem `src/application/` devem depender de `src/infrastructure/` — é essa direção de dependência (de fora para dentro) que mantém o domínio livre de detalhe técnico (ver `docs/ARCHITECTURE.md`).
