# src/application/

Camada de aplicação (Clean Architecture / Use Cases) — **vazia nesta sprint**. Orquestra o domínio (`src/domain/`) para executar um caso de uso completo (ex: "Gerar Proposta", "Aprovar Proposta"), mas não contém regra de negócio nem detalhe técnico.

## O que vai entrar aqui (Sprint 1B em diante)

- Casos de uso (ex: `criar_proposta.py`, `aprovar_proposta.py`, `gerar_documento.py`), cada um orquestrando entidades/agregados de `src/domain/` e chamando `src/infrastructure/` para efeitos colaterais (persistência, geração de arquivo).
- Validações que dependem de mais de um Bounded Context (ex: "não aprovar proposta sem Cliente e Viagem completos") — regra de orquestração, não regra de uma única entidade.
- Publicação de Domain Events (`src/domain/shared/domain_event.py`) para comunicação entre contextos.

## Regra de dependência

`src/application/` pode depender de `src/domain/`. `src/domain/` nunca depende de `src/application/` — a dependência é sempre de fora para dentro (ver `docs/ARCHITECTURE.md`).
