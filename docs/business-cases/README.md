# Business Cases

Cada arquivo nesta pasta representa **uma operação real** da 027 Viagens, contada como história — não uma lista de perguntas abstratas. É o principal instrumento da nova metodologia de descoberta (Sprint B1): em vez de perguntar "como funciona o processo de cancelamento?", pedimos "conte um cancelamento real que aconteceu" e reconstruímos a história inteira.

**Nenhum caso aqui contém conteúdo inventado.** Todos os 12 arquivos iniciais estão vazios — são templates prontos para receber o relato do proprietário (Wefferson) durante os Workshops de Descoberta (`docs/discovery-workshop.md`). Um caso só deixa de ser "a preencher" depois de uma entrevista real.

## Por que casos reais, não perguntas genéricas

Perguntas genéricas ("como funciona X?") tendem a gerar respostas também genéricas, que descrevem o processo idealizado, não o que realmente acontece — exceções, retrabalho e decisões de última hora ficam de fora porque ninguém pensa nelas quando descreve "o processo" em abstrato. Pedir uma história real força esses detalhes a aparecerem, porque uma história tem sequência, tem gente, tem coisa que deu errado.

## Estrutura de cada caso

Todo arquivo segue o mesmo template:

- **Contexto** — como o cliente chegou, o que ele queria.
- **Objetivo do cliente** — o que ele estava tentando resolver com a viagem.
- **Sequência cronológica** — reconstrução passo a passo da história.
- **Decisões tomadas** — quem decidiu o quê, e por quê.
- **Documentos gerados** — quais documentos existiram (proposta, contrato, voucher, comprovante...).
- **Aprovações** — quem precisou aprovar o quê.
- **Alterações** — o que mudou depois de fechado.
- **Retrabalho** — o que precisou ser refeito, e por quê.
- **Comunicação** — como cliente e equipe se falaram (canais, quem falou com quem).
- **Riscos** — o que quase deu errado, ou poderia ter dado.
- **Problemas encontrados** — dificuldades reais enfrentadas no caso.
- **Exceções** — o que fugiu do processo padrão.
- **Lições aprendidas** — o que a 027 aprendeu ou mudaria.
- **Possíveis regras de negócio identificadas** — candidatas a virar entrada confirmada em `docs/business-rules.md`.

Cada arquivo também tem uma seção **Perguntas específicas para este caso**, com ganchos relevantes ao tipo de operação (ex: o caso de Cancelamento pergunta especificamente sobre prazos e percentuais de reembolso).

## Casos iniciais

| Arquivo | Tipo de operação | Workshop relacionado |
|---|---|---|
| `venda-nacional.md` | Venda nacional | Workshop 1 — Atendimento |
| `venda-internacional.md` | Venda internacional | Workshop 1 — Atendimento |
| `grupo.md` | Viagem em grupo | Workshop 3 — Operação |
| `viagem-religiosa.md` | Viagem religiosa | Workshop 3 — Operação |
| `corporativo.md` | Viagem corporativa | Workshop 3 — Operação |
| `disney.md` | Viagem Disney | Workshop 3 — Operação |
| `cancelamento.md` | Cancelamento | Workshop 2 — Financeiro |
| `remarcacao.md` | Remarcação | Workshop 2 — Financeiro |
| `alteracao-passageiros.md` | Alteração de passageiros | Workshop 3 — Operação |
| `alteracao-hotel.md` | Alteração de hotel | Workshop 3 — Operação |
| `alteracao-voo.md` | Alteração de voo | Workshop 3 — Operação |
| `emissao-urgente.md` | Emissão urgente | Workshop 4 — Emissão |

Esta lista não é fechada — se, durante uma entrevista, surgir um tipo de operação real que não está aqui, criar um novo arquivo seguindo o mesmo template, e adicioná-lo a esta tabela.

## O que fazer com um caso preenchido

Depois que um caso é preenchido com uma entrevista real, ele deve alimentar (não substituir) os documentos vivos do projeto — ver o protocolo completo em `docs/discovery-workshop.md`, seção "Protocolo pós-entrevista":

- Regras de negócio identificadas → `docs/business-rules.md` (sai de "pendente" para "conhecida", com referência ao caso de origem).
- Particularidades de tipo de operação → `docs/proposal-types.md`.
- Etapas/exceções do processo → `docs/proposal-lifecycle.md`.
- Decisões de modelagem que o caso sugere → `docs/domain-decisions.md`.
- Termos novos → `docs/glossary.md`.
- Dados de fornecedores/destinos/pagamento mencionados no caso → `knowledge/` (ver `knowledge/README.md`).

Um caso preenchido nunca é apagado depois de "processado" — ele permanece como a evidência/origem da regra, para consulta futura (por que decidimos isso? → vai no caso original).
