# Ações sobre a Proposta

Mapeamento das ações possíveis sobre uma `Proposta` (ver `glossary.md`). Como em `proposal-status.md`, esta é uma lista hipotética de trabalho, a validar com o negócio.

---

## Criar

- **Objetivo:** iniciar uma nova `Proposta` a partir de dados levantados do cliente.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** levantamento de necessidades concluído (ver `proposal-lifecycle.md`).
- **Consequências:** nova proposta em status `Rascunho`, `Versão` 1.
- **Impacto no histórico:** cria o registro inicial.

## Editar

- **Objetivo:** alterar dados de uma proposta existente.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta em status que permita edição (ver `proposal-status.md`).
- **Consequências:** *a confirmar — gera nova versão sempre, ou só em certos status?* (pergunta central de `proposal-versioning.md`)
- **Impacto no histórico:** *a confirmar.*

## Duplicar

- **Objetivo:** criar uma nova proposta a partir de uma existente (mesmo cliente ou não), útil para recotação ou casos semelhantes.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta original existente, de qualquer status.
- **Consequências:** nova `Proposta` independente (novo `proposal_id`), não uma nova versão da original.
- **Impacto no histórico:** a nova proposta referencia a original como origem, mas tem histórico próprio.

## Atualizar

- **Objetivo:** *a confirmar — em que isso difere de "Editar"? Pode ser "atualizar dados de contato" sem gerar nova versão comercial, por exemplo.*
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** *a confirmar.*
- **Consequências:** *a confirmar.*
- **Impacto no histórico:** *a confirmar.*
- **Dúvida central:** o negócio distingue "Editar" (muda a oferta) de "Atualizar" (muda dado cadastral), ou são a mesma ação com nomes diferentes na lista original do briefing?

## Recalcular

- **Objetivo:** reprocessar os valores financeiros da proposta (ex: após mudança de câmbio, desconto, ou serviço adicional).
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta com dados suficientes para novo cálculo.
- **Consequências:** *a confirmar — atualiza a versão atual ou gera nova versão?*
- **Impacto no histórico:** *a confirmar.*

## Reenviar

- **Objetivo:** enviar novamente um documento já gerado (ex: cliente perdeu o e-mail).
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta já enviada ao menos uma vez.
- **Consequências:** nenhuma mudança de conteúdo, apenas reenvio.
- **Impacto no histórico:** registra novo evento de envio, sem gerar nova versão.

## Cancelar

- **Objetivo:** encerrar a proposta sem conversão em venda.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta em qualquer status não-final (ver `proposal-status.md`).
- **Consequências:** proposta move para status `Cancelada`.
- **Impacto no histórico:** motivo do cancelamento deve ser registrado — *a confirmar se isso é obrigatório e qual o motivo padrão a coletar.*

## Aprovar

- **Objetivo:** registrar o aceite do cliente (ou aprovação interna, se aplicável).
- **Quem pode executar:** *a confirmar — ação disparada pelo consultor ao registrar aceite do cliente, ou existe autoaprovação pelo próprio cliente (portal futuro)?*
- **Pré-requisitos:** proposta em status `Enviada` ou `Em negociação`.
- **Consequências:** proposta move para status `Aprovada`.
- **Impacto no histórico:** registra quem aprovou e quando.

## Reprovar

- **Objetivo:** registrar que o cliente recusou a proposta.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta enviada.
- **Consequências:** *a confirmar — vai para `Cancelada`, ou existe um status "Recusada" próprio? (ver pergunta em `proposal-status.md`)*
- **Impacto no histórico:** motivo da reprovação, se coletado.

## Converter em emissão

- **Objetivo:** transformar uma proposta paga em uma emissão efetiva junto aos fornecedores.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta em status `Paga`.
- **Consequências:** gera o(s) documento(s) de emissão (módulo futuro — Confirmações de Reserva, Vouchers, etc., ver `ARCHITECTURE.md`); proposta move para status `Emitida`.
- **Impacto no histórico:** vincula a proposta ao(s) documento(s) de emissão gerados.

## Arquivar

- **Objetivo:** remover uma proposta do fluxo ativo de trabalho sem excluí-la.
- **Quem pode executar:** *a confirmar.*
- **Pré-requisitos:** proposta em status final (`Emitida`, `Cancelada`, `Expirada`).
- **Consequências:** proposta sai de visualizações operacionais ativas, mas permanece consultável.
- **Impacto no histórico:** nenhuma perda de dado — arquivar não é excluir.

---

## Perguntas em aberto (transversais)

- Esta lista de ações cobre tudo que a operação faz hoje com uma proposta? Falta alguma (ex: "aplicar desconto", "trocar consultor responsável")?
- Existe controle de permissão por papel (consultor, gestor, financeiro) sobre quem pode executar cada ação, ou hoje qualquer um da equipe faz tudo?
- Toda ação relevante deve gerar um registro de auditoria (quem, quando, o quê)? Isso se conecta à metadata obrigatória do Modelo Universal (`universal-proposal-model.md`).
