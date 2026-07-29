# ai/

Preparação de estrutura para a futura capacidade de **IA Comercial** da plataforma (ver `docs/ARCHITECTURE.md` e `docs/vision.md`). Nesta etapa, apenas os diretórios existem — nenhuma implementação, integração ou chamada a modelo de IA acontece aqui ainda.

## O que vai entrar em cada pasta

- **`prompts/`** — prompts de produto usados por funcionalidades de IA (ex: geração assistida de proposta a partir de texto livre — diferente do "Prompt Mestre" operacional que já vive em `/prompts` na raiz, que é sobre o preenchimento de dados, não sobre a inteligência comercial da plataforma).
- **`personas/`** — definições de persona/tom de voz que a IA deve assumir em cada contexto (ex: consultor de viagens, atendimento pós-venda).
- **`validators/`** — regras usadas para validar saídas geradas por IA antes de chegarem a um documento final (ex: conferir que uma sugestão de upsell respeita `docs/business-rules.md`).
- **`instructions/`** — instruções de sistema/comportamento reutilizadas por diferentes funcionalidades de IA da plataforma.
- **`knowledge/`** — base de conhecimento consultada pela IA (ex: diferenciais, políticas, FAQ) — quando implementada, deve referenciar `content/` como fonte, não duplicar o texto.

## Relação com o resto da plataforma

Qualquer funcionalidade de IA construída aqui deve seguir o mesmo princípio do restante da arquitetura: consumir o Modelo Universal e as camadas compartilhadas (`config/`, `content/`, `business-rules.md`), nunca decidir regra de negócio por conta própria à revelia do que está documentado.

## Por que existe desde já

Reservar esses diretórios agora evita que, quando a IA Comercial for implementada (ver `ROADMAP.md`), prompts/personas/validações fiquem espalhados improvisadamente dentro de `src/` ou `prompts/`. A pasta existe vazia de propósito — a implementação virá em sprint dedicado.
