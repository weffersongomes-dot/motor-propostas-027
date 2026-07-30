# 0009 — Sprint B1: Descoberta por Casos Reais

- **Status:** aceita
- **Data:** 2026-07-30

## Contexto

A Sprint 0.5 (ADR 0004) e o refinamento pré-Sprint 1A (ADR 0005) produziram um roteiro de descoberta (`docs/discovery-workshop.md`) baseado em perguntas abertas genéricas ("como funciona X?"). Na prática, perguntas desse tipo tendem a gerar descrições do processo idealizado, não do que realmente acontece — exceções, retrabalho, aprovações informais e decisões de última hora ficam de fora porque raramente vêm à mente quando alguém descreve "o processo" em abstrato. Como o modelo executável (Sprint 1A/1B) já está pronto para receber regra de negócio real, mas nenhuma regra real foi confirmada ainda, o risco de continuar com perguntas genéricas é reunir informação insuficiente para a Sprint 1C.

## Decisão

- Trocar o método de descoberta: cada Workshop passa a ser conduzido **a partir de casos reais** ("conte uma venda real que aconteceu"), reconstruindo a história completa antes de qualquer pergunta abstrata — que passam a ser sondagem de acompanhamento, não ponto de partida.
- Criar `docs/business-cases/` — um arquivo por operação real, com 12 casos iniciais (venda nacional, venda internacional, grupo, viagem religiosa, corporativo, Disney, cancelamento, remarcação, alteração de passageiros, alteração de hotel, alteração de voo, emissão urgente), todos vazios, prontos para receber relato.
- Criar `knowledge/` (`suppliers/`, `airlines/`, `hotels/`, `insurance/`, `destinations/`, `payments/`) — estrutura vazia para conhecimento de referência (não histórias) sobre fornecedores, destinos e pagamentos, extraído dos casos processados.
- Formalizar um **Protocolo pós-entrevista** em `discovery-workshop.md`: toda sessão termina atualizando `business-rules.md`, `proposal-types.md`, `proposal-lifecycle.md`, `domain-decisions.md`, `glossary.md` e, quando aplicável, `knowledge/` — nesta ordem, sempre, não como tarefa opcional.

## Motivo

- Uma história real força detalhes concretos a aparecer (datas, valores, quem decidiu o quê) que uma resposta abstrata naturalmente omite — é o mesmo raciocínio por trás de técnicas de entrevista comportamental em Business Analysis (perguntar por um exemplo específico em vez de uma opinião geral).
- Separar "história" (`business-cases/`) de "fato de referência reutilizável" (`knowledge/`) evita que um documento vire confuso — um caso conta o que aconteceu numa venda específica; `knowledge/` guarda o que é verdade em geral (ex: qual seguradora a 027 usa).
- Formalizar o protocolo pós-entrevista evita o risco observado nas sprints anteriores de descoberta ficar "só na conversa" — cada sessão agora tem uma saída obrigatória e verificável (arquivos atualizados), não apenas uma ata informal.

## Consequências

- `docs/discovery-workshop.md` não lista mais perguntas abertas como primeira ação de cada Workshop — quem conduzir uma sessão sem pedir um caso primeiro está desviando do método definido aqui.
- Novos tipos de operação real que aparecerem durante as entrevistas (ex: um caso de Cruzeiro, mencionado mas sem arquivo dedicado ainda) devem virar novo arquivo em `business-cases/`, seguindo o mesmo template — a lista de 12 casos iniciais não é fechada.
- `knowledge/` só deve receber conteúdo quando um caso processado o justificar — nunca preenchido preventivamente com suposições.
- A Sprint 1C (Regras Comerciais, ver ROADMAP) passa a depender explicitamente de casos processados via este método, não apenas de perguntas respondidas — critério de pronto mais rigoroso que o da Sprint 0.5.
