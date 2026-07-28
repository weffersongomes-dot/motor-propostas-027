# 0001 — Estrutura inicial do projeto

- **Status:** aceita
- **Data:** 2026-07-28

## Contexto

O projeto parte de um repositório vazio. A estrutura de diretórios sugerida no briefing inicial cobria as áreas principais (assets, docs, prompts, templates, examples, output, scripts, src), mas não detalhava como organizar internamente `templates/`, `output/` e `src/` — que precisam suportar múltiplos formatos de saída (HTML, PDF, WhatsApp, e-mail, JSON) sem duplicar regra de negócio entre eles.

## Decisão

- Subdividir `templates/` e `output/` por formato de saída (`html/`, `pdf/`, `whatsapp/`, `email/`; e `html/`, `pdf/`, `json/` em `output/`).
- Subdividir `src/` em `models/` (estrutura de dados da proposta), `core/` (regras de negócio), `generators/` (um gerador por formato) e `utils/` (funções auxiliares).
- Adicionar `docs/decisoes/` para registrar decisões técnicas como esta.
- Ignorar o conteúdo de `output/` no Git (mantendo apenas `.gitkeep`), pois propostas geradas contêm dados de clientes.

## Motivo

- Evita que regra de negócio (cálculos, validações, nomenclatura) seja duplicada entre os diferentes geradores de saída — cada gerador em `src/generators/` deve apenas apresentar os dados vindos de `src/core/`/`src/models/`, nunca recalculá-los.
- Mantém a promessa do PRD de "separar regras de negócio da apresentação" de forma concreta na estrutura de pastas, não só como princípio abstrato.
- Prepara o projeto para crescer (novos formatos de saída, novas integrações) sem precisar reorganizar pastas já existentes.

## Consequências

- Qualquer novo formato de saída deve seguir o mesmo padrão: uma subpasta em `templates/`, um gerador em `src/generators/`, e (se aplicável) uma subpasta em `output/`.
- Decisões de stack (linguagem, biblioteca de PDF, etc.) ficam para o Sprint 1, documentadas em um novo registro nesta mesma pasta.
