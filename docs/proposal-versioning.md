# Estratégia de Versionamento da Proposta

Diferente dos demais documentos desta sprint, este é um documento de **projeto/design**, não só de descoberta: define como o histórico de mudanças de uma `Proposta` será preservado. Ainda assim, pontos que dependem de decisão do negócio estão marcados como tal — não devem ser fixados em código antes de confirmados.

## Formato de identificação

```
Proposta 001
  ↓
  001.1
  ↓
  001.2
  ↓
  001.3
```

- `001` — o **identificador da proposta** (`proposal_id`, ver `universal-proposal-model.md`). Estável durante todo o ciclo de vida, mesmo com múltiplas versões.
- `.1`, `.2`, `.3` — o **número da versão** dentro daquela proposta. Cada versão representa um estado completo e íntegro da proposta naquele momento (não um diff/patch).

Toda versão anterior permanece acessível e imutável após a criação da próxima — versionar nunca sobrescreve.

## Quando criar uma nova versão vs. quando apenas atualizar

Esta é a decisão mais sensível do documento e **depende de confirmação do negócio** (ver `discovery-workshop.md`, seção Emissão/Financeiro). Proposta de critério, a validar:

- **Gera nova versão** — qualquer mudança que altere o que foi *oferecido* ou *seu preço/condição*: itens inclusos, valores, forma de pagamento, roteiro, datas. Em outras palavras, qualquer mudança que o cliente precisaria ver de novo para decidir se aceita.
- **Não gera nova versão (atualização in-place)** — correção de dado que não muda a oferta em si: erro de digitação em nome, correção de contato, correção de metadata técnica.

> **Pergunta para o negócio:** este corte faz sentido na prática, ou existe um caso em que uma mudança "pequena" (ex: trocar o nome do hotel por outro de categoria equivalente) deveria ou não gerar nova versão? Vale revisar com exemplos reais de propostas já feitas.

## Como manter o histórico

- Cada versão é um snapshot completo do Modelo Universal da Proposta (não apenas os campos alterados) — evita ambiguidade sobre "qual era o estado completo da versão 001.2".
- A versão mais recente é a única editável; versões anteriores são somente leitura.
- Toda versão carrega, na sua metadata (`universal-proposal-model.md`), `generated_at` e `generated_by` próprios — o histórico de versões é, por construção, um histórico de "quem gerou o quê e quando".
- O motivo da nova versão (ex: "ajuste de preço solicitado pelo cliente", "correção de roteiro") deve ser registrado — *a confirmar se isso é texto livre do consultor ou um motivo padronizado (lista fechada)*.

## Rastreabilidade

- Toda versão referencia o `proposal_id` comum e o número da versão anterior (ex: `001.2` referencia `001.1`), formando uma cadeia navegável do início ao fim.
- O `status` (ver `proposal-status.md`) é um atributo da versão mais recente — versões antigas mantêm o status que tinham quando deixaram de ser a versão corrente (ex: `001.1` pode ter ficado "Em negociação" antes de `001.2` ser aprovada).
- Qualquer documento gerado (PDF, HTML, envio de WhatsApp/e-mail) deve registrar exatamente qual versão foi usada para gerá-lo — nunca "a proposta" genericamente.

## Relacionamento entre versões

- Relação **linear** dentro de uma mesma proposta: `001.1 → 001.2 → 001.3`, sempre uma sucessora por vez (sem ramificações/branches).
- Relação **de origem** entre propostas diferentes: quando uma proposta é duplicada (`proposal-actions.md`, ação Duplicar) para virar uma proposta nova, a nova proposta referencia a original como origem, mas começa sua própria cadeia de versões (`002.1`, não `001.4`).

> **Pergunta para o negócio:** existe algum caso real em que a proposta precisaria "ramificar" (duas propostas alternativas sendo negociadas ao mesmo tempo, ex: "opção econômica" vs. "opção premium" para o mesmo cliente)? Se sim, isso muda o modelo de linear para ramificado, e precisa ser decidido antes do Sprint 1.

## Relação com Status e Ações

- A ação `Editar` (`proposal-actions.md`) é a principal geradora de nova versão, conforme o critério acima.
- A ação `Recalcular` pode ou não gerar nova versão, dependendo se o novo cálculo muda a oferta ao cliente — mesma pergunta em aberto.
- O `status` "Aprovada" (`proposal-status.md`) deveria "travar" a versão aprovada — qualquer mudança posterior é obrigatoriamente uma nova versão, nunca uma edição da versão já aprovada. Isso preserva o que o cliente efetivamente aceitou.
