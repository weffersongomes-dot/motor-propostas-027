# Ciclo de Vida da Proposta

Documenta o percurso completo de uma `Proposta` (ver `glossary.md`), do primeiro interesse do cliente até o pós-venda. A sequência abaixo é a hipótese de referência usada para estruturar a descoberta — **não é o fluxo confirmado da 027 Viagens**. Cada etapa deve ser validada, corrigida ou removida no Workshop de Descoberta (`discovery-workshop.md`).

```
Lead
  ↓
Qualificação
  ↓
Primeiro contato
  ↓
Levantamento das necessidades
  ↓
Cotação
  ↓
Proposta
  ↓
Negociação
  ↓
Ajustes
  ↓
Aprovação
  ↓
Pagamento
  ↓
Emissão
  ↓
Entrega dos documentos
  ↓
Viagem
  ↓
Pós-venda
```

> **Pergunta geral:** este fluxo linear corresponde à realidade? Alguma etapa nunca acontece, acontece fora de ordem, ou existe alguma etapa importante da operação que não está listada aqui?

---

## Lead

- **Objetivo:** *a confirmar.*
- **Entrada:** *a confirmar — de onde vêm os leads (indicação, redes sociais, site, telefone)?*
- **Saída:** *a confirmar.*
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar — existe algum registro do lead hoje (planilha, CRM informal)?*
- **Possíveis exceções:** *a confirmar.*
- **Dúvidas abertas:**
  - Todo lead passa, obrigatoriamente, por `Qualificação`, ou alguns já entram direto em "Primeiro contato" (ex: indicação de cliente antigo)?
  - Como/onde o lead é registrado hoje?

## Qualificação

- **Objetivo:** avaliar, antes de investir tempo em atendimento completo, se o `Lead` tem potencial real de virar venda (interesse genuíno, orçamento compatível, prazo viável).
- **Entrada:** um `Lead` recém-registrado.
- **Saída:** decisão de seguir para `Primeiro contato` ou descartar/arquivar o lead.
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar — existe algum critério/checklist de qualificação hoje, mesmo informal?*
- **Possíveis exceções:** lead claramente fora do perfil de atendimento da 027 (ex: destino/orçamento incompatível); lead duplicado (já é cliente).
- **Dúvidas abertas:**
  - Essa etapa existe hoje como um passo separado, ou a qualificação acontece dentro do próprio Primeiro contato?
  - Existem critérios objetivos de qualificação (ex: orçamento mínimo, prazo mínimo até a viagem), ou é sempre julgamento do consultor?
  - Um lead "desqualificado" é descartado, arquivado para retomar depois, ou redirecionado (ex: para outro produto/consultor)?

## Primeiro contato

- **Objetivo:** *a confirmar.*
- **Entrada:** um `Lead` já qualificado.
- **Saída:** *a confirmar.*
- **Responsável:** *a confirmar — sempre o `Consultor`, ou a triagem da Qualificação já define quem assume?*
- **Documentos envolvidos:** *a confirmar.*
- **Possíveis exceções:** *a confirmar — lead que não responde, número errado, etc.*
- **Dúvidas abertas:**
  - Qual canal é usado (WhatsApp, telefone, e-mail, presencial)?
  - Existe um tempo-limite/SLA esperado de resposta?

## Levantamento das necessidades

- **Objetivo:** *a confirmar.*
- **Entrada:** contato já estabelecido com o `Cliente`.
- **Saída:** *a confirmar — informações suficientes para iniciar uma `Cotação`?*
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar — existe um roteiro/formulário de perguntas usado hoje?*
- **Possíveis exceções:** cliente sem destino definido, cliente pedindo sugestão em vez de já ter escolha.
- **Dúvidas abertas:**
  - Existe uma lista fixa de perguntas feitas ao cliente nesta etapa? (se sim, deve alimentar `discovery-workshop.md` e, depois, o Modelo Universal)
  - Nesta etapa já se sabe o `Tipo de Proposta` (ver `proposal-types.md`), ou isso só fica claro depois?

## Cotação

- **Objetivo:** *a confirmar.*
- **Entrada:** necessidades levantadas do `Cliente`.
- **Saída:** preços/disponibilidade junto a `Fornecedores`.
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar — cotações de fornecedores são anexadas/guardadas?*
- **Possíveis exceções:** fornecedor sem disponibilidade, preço expira antes da proposta ser fechada.
- **Dúvidas abertas:**
  - "Cotação" é uma etapa interna (não vista pelo cliente) ou o cliente já recebe algo nesta fase?
  - Quanto tempo uma cotação de fornecedor costuma ficar válida? Isso afeta a validade da `Proposta` final (ver `business-rules.md`)?

## Proposta

- **Objetivo:** *a confirmar.*
- **Entrada:** cotação(ões) já levantada(s).
- **Saída:** documento formal enviado ao `Cliente` (HTML/PDF/WhatsApp/e-mail — ver `ARCHITECTURE.md`).
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** a própria `Proposta`, em seus formatos de saída.
- **Possíveis exceções:** *a confirmar.*
- **Dúvidas abertas:**
  - Uma proposta sempre nasce a partir de uma cotação formal, ou o consultor pode montar a proposta direto em casos simples?
  - Neste momento a proposta já recebe um `proposal_id` e `Versão` 1? (ver `proposal-versioning.md`)

## Negociação

- **Objetivo:** *a confirmar.*
- **Entrada:** `Proposta` enviada.
- **Saída:** *a confirmar — aceite, pedido de ajuste, ou recusa.*
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar — negociação é registrada em algum lugar, ou fica só na conversa?*
- **Possíveis exceções:** cliente some, cliente negocia com outro consultor da mesma agência.
- **Dúvidas abertas:**
  - O que pode ser negociado (preço, forma de pagamento, itens inclusos)? Existe alçada/limite para o consultor conceder desconto sozinho?

## Ajustes

- **Objetivo:** *a confirmar.*
- **Entrada:** pedido de mudança vindo da negociação.
- **Saída:** proposta revisada — gera nova `Versão`? (ver `proposal-versioning.md`)
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar.*
- **Possíveis exceções:** ajuste exige nova cotação com fornecedor (preço muda).
- **Dúvidas abertas:**
  - Todo ajuste gera uma nova versão da proposta, ou pequenos ajustes só atualizam a versão atual? (pergunta central de `proposal-versioning.md`)

## Aprovação

- **Objetivo:** *a confirmar.*
- **Entrada:** proposta (ajustada ou não) aceita pelo `Cliente`.
- **Saída:** *a confirmar.*
- **Responsável:** *a confirmar — aprovação é só do cliente, ou também existe aprovação interna da 027 (ex: desconto acima da alçada)?*
- **Documentos envolvidos:** *a confirmar — existe confirmação por escrito (e-mail, WhatsApp, assinatura)?*
- **Possíveis exceções:** aprovação parcial (aprova o roteiro, não o seguro, por exemplo).
- **Dúvidas abertas:**
  - Como a aprovação do cliente é registrada hoje (nada formal, print de conversa, assinatura de contrato)?

## Pagamento

- **Objetivo:** *a confirmar.*
- **Entrada:** proposta aprovada.
- **Saída:** confirmação financeira que libera a `Emissão`.
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** comprovante de pagamento, condições de parcelamento (ver `business-rules.md`).
- **Possíveis exceções:** pagamento parcial (sinal), atraso, pagamento em múltiplas formas.
- **Dúvidas abertas:**
  - A emissão só ocorre com pagamento 100% confirmado, ou existe emissão contra sinal + parcelas futuras?

## Emissão

- **Objetivo:** *a confirmar.*
- **Entrada:** pagamento confirmado.
- **Saída:** reservas/serviços efetivamente confirmados junto aos `Fornecedores`.
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** voucher, bilhetes, confirmações de reserva (módulos futuros da plataforma, ver `ARCHITECTURE.md`).
- **Possíveis exceções:** fornecedor sem disponibilidade no momento da emissão (preço/cotação já não vale mais).
- **Dúvidas abertas:**
  - Existe um checklist interno de emissão hoje (o PRD original já menciona isso como saída esperada da plataforma)? Qual o conteúdo desse checklist?

## Entrega dos documentos

- **Objetivo:** *a confirmar.*
- **Entrada:** serviços emitidos.
- **Saída:** cliente de posse de todos os documentos da viagem.
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** vouchers, bilhetes, seguro, roteiro/itinerário.
- **Possíveis exceções:** documento de fornecedor atrasa.
- **Dúvidas abertas:**
  - Existe um canal/formato padrão de entrega (pasta digital, e-mail único, impresso)?

## Viagem

- **Objetivo:** período em que o passageiro efetivamente viaja — a plataforma tem alguma responsabilidade ativa nesta etapa?
- **Entrada:** documentos entregues.
- **Saída:** retorno do passageiro.
- **Responsável:** *a confirmar — existe suporte da 027 durante a viagem (emergência, reemissão)?*
- **Documentos envolvidos:** *a confirmar.*
- **Possíveis exceções:** imprevistos durante a viagem que exigem suporte da agência.
- **Dúvidas abertas:**
  - A 027 Viagens presta algum suporte ativo durante a viagem? Isso deveria gerar registro na proposta/histórico?

## Pós-venda

- **Objetivo:** *a confirmar.*
- **Entrada:** retorno do passageiro.
- **Saída:** *a confirmar — feedback, indicação, nova venda?*
- **Responsável:** *a confirmar.*
- **Documentos envolvidos:** *a confirmar.*
- **Possíveis exceções:** reclamação, pedido de reembolso pós-viagem.
- **Dúvidas abertas:**
  - Existe um processo de pós-venda hoje (pesquisa de satisfação, contato programado)? Isso deveria ser rastreado na plataforma?

---

## Observação transversal

Todas as etapas acima devem, eventualmente, corresponder a um `Status da Proposta` (`proposal-status.md`) e serem acionáveis por uma ou mais `Ação sobre a Proposta` (`proposal-actions.md`). Ao validar este ciclo de vida com o negócio, revisar os outros dois documentos juntos para manter os três consistentes.
