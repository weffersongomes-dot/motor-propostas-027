# Status da Proposta

Estados possíveis de uma `Proposta` (ver `glossary.md`). A lista abaixo é uma **hipótese inicial de trabalho**, derivada do ciclo de vida sugerido em `proposal-lifecycle.md` — nenhum fluxo aqui está definitivo. Deve ser validada, corrigida e completada no Workshop de Descoberta (`discovery-workshop.md`).

> **Pergunta geral:** a 027 Viagens já usa algum nome/conceito de status hoje (mesmo que informal, tipo "em aberto", "fechada", "perdida")? Esses nomes devem substituir os desta lista.

---

## Rascunho

- **Significado:** proposta em elaboração, ainda não enviada ao cliente.
- **Quando entra:** ao iniciar a criação de uma nova `Proposta` (ação `criar`, ver `proposal-actions.md`).
- **Quando sai:** ao ser enviada ao cliente.
- **Ações permitidas:** editar, recalcular, excluir.
- **Ações proibidas:** aprovar, converter em emissão.
- **Observações:** *a confirmar — existe uma etapa de revisão interna antes do envio (ex: outro consultor ou gestor revisa)?*

## Enviada

- **Significado:** proposta formalmente enviada ao cliente, aguardando retorno.
- **Quando entra:** logo após o envio (HTML/PDF/WhatsApp/e-mail).
- **Quando sai:** ao receber retorno do cliente (negociação, aprovação, recusa) ou ao expirar.
- **Ações permitidas:** reenviar, duplicar, editar (gera nova versão? ver `proposal-versioning.md`).
- **Ações proibidas:** *a confirmar.*
- **Observações:** *a confirmar — existe algum prazo padrão de acompanhamento após o envio?*

## Em negociação

- **Significado:** cliente retornou pedindo ajustes ou negociando condições.
- **Quando entra:** ao receber retorno do cliente pedindo mudança.
- **Quando sai:** ao chegar em uma versão aprovada, ou ao ser encerrada sem sucesso.
- **Ações permitidas:** editar, recalcular, duplicar.
- **Ações proibidas:** converter em emissão.
- **Observações:** *a confirmar — quantas rodadas de negociação costumam acontecer na prática?*

## Aprovada

- **Significado:** cliente aceitou os termos da proposta (ver `proposal-lifecycle.md`, etapa Aprovação).
- **Quando entra:** ao registrar o aceite do cliente.
- **Quando sai:** ao confirmar pagamento (avança) ou ao ser cancelada antes do pagamento.
- **Ações permitidas:** *a confirmar.*
- **Ações proibidas:** editar livremente (deveria exigir nova versão em vez de alterar a aprovada?).
- **Observações:** *a confirmar — como o aceite é registrado (ver dúvida equivalente em `proposal-lifecycle.md`)?*

## Aguardando pagamento

- **Significado:** proposta aprovada, aguardando confirmação financeira.
- **Quando entra:** logo após aprovação.
- **Quando sai:** ao confirmar pagamento (total ou parcial suficiente, conforme regra a definir) ou expirar.
- **Ações permitidas:** *a confirmar.*
- **Ações proibidas:** *a confirmar.*
- **Observações:** *a confirmar — este status é necessário como estado próprio, ou "Aprovada" já cobre isso até o pagamento?*

## Paga

- **Significado:** pagamento confirmado, pronta para emissão.
- **Quando entra:** confirmação financeira.
- **Quando sai:** ao ser emitida.
- **Ações permitidas:** converter em emissão.
- **Ações proibidas:** editar valores sem novo processo de ajuste/estorno.
- **Observações:** *a confirmar — pagamento parcial (sinal) já move a proposta para este status, ou só pagamento integral?*

## Emitida

- **Significado:** serviços confirmados junto aos fornecedores; documentos finais gerados.
- **Quando entra:** conclusão da etapa de Emissão.
- **Quando sai:** *a confirmar — existe status posterior (ex: "Em viagem", "Concluída"), ou "Emitida" é o status final?*
- **Ações permitidas:** arquivar, consultar histórico.
- **Ações proibidas:** editar, recalcular, aprovar novamente.
- **Observações:** *a confirmar.*

## Cancelada

- **Significado:** proposta encerrada sem conversão em venda, em qualquer ponto do fluxo.
- **Quando entra:** *a confirmar — cancelamento pode ocorrer a partir de quais status?*
- **Quando sai:** estado final (não sai).
- **Ações permitidas:** consultar histórico, duplicar (nova proposta a partir da cancelada).
- **Ações proibidas:** qualquer edição, aprovação, emissão.
- **Observações:** *a confirmar — cancelamento antes vs. depois do pagamento tem consequências diferentes (ver `business-rules.md`, seção Cancelamentos)?*

## Expirada

- **Significado:** proposta que ultrapassou seu prazo de validade sem aprovação.
- **Quando entra:** automaticamente, ao passar da data de validade (ver `business-rules.md`, seção Validade de propostas).
- **Quando sai:** estado final, ou pode ser reaberta/recotada?
- **Ações permitidas:** duplicar/recotar.
- **Ações proibidas:** aprovar, converter em emissão sem antes recotar.
- **Observações:** *a confirmar — existe expiração automática hoje, ou é sempre um julgamento manual do consultor?*

---

## Perguntas em aberto (transversais a todos os status)

- Esta lista de 9 status corresponde à realidade, ou a operação usa menos/mais estados?
- Existe transição que deveria ser proibida e não está marcada como tal acima?
- Deve existir um status para "perdida"/"recusada" explicitamente diferente de "Cancelada" e "Expirada"?
- Quem tem permissão para mudar cada status manualmente (ver também `proposal-actions.md`)?
