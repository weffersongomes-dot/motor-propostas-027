# Workshops de Descoberta

Roteiro estruturado para levantar o conhecimento operacional da 027 Viagens com o proprietário (Wefferson), hoje a principal fonte desse conhecimento. Em vez de uma lista única de perguntas, o levantamento é dividido em **cinco workshops independentes**, cada um podendo ser conduzido em uma sessão própria, na ordem que fizer sentido para a agenda do negócio.

## Como usar este roteiro

- Cada workshop pode ser conduzido isoladamente — não é preciso completar todos em sequência única, mas os workshops 1 e 2 tendem a render as respostas mais urgentes para o Sprint 1B (ver `business-rules.md`).
- Sempre que uma resposta introduzir um termo novo (ex: nome interno de uma etapa ou papel), registrar em `docs/glossary.md` antes de seguir.
- Ao final de cada workshop, atualizar imediatamente os documentos listados em "Documentos atualizados ao final" — enquanto a conversa está fresca, não depois.
- Perguntas sobre exceções e casos especiais tendem a render mais regra de negócio real do que perguntas sobre o caminho padrão — não pular essas partes dentro de cada workshop.

---

## Workshop 1 — Atendimento

- **Objetivo:** entender como um lead chega, como é qualificado e atendido até a proposta ser enviada — a parte inicial do ciclo de vida (`proposal-lifecycle.md`, etapas Lead a Proposta).
- **Participantes:** proprietário (Wefferson) e, se houver, quem faz atendimento direto ao cliente.
- **Perguntas:**
  1. Como um cliente novo chega até a 027 Viagens hoje (canais)?
  2. Existe uma etapa de Qualificação separada do Primeiro contato, ou elas acontecem juntas? O que faz um lead ser "qualificado"?
  3. O que você (ou a equipe) precisa saber do cliente antes de começar a montar uma cotação?
  4. Existe algum roteiro ou checklist de perguntas que vocês já fazem hoje, mesmo informalmente?
  5. Quanto tempo, tipicamente, leva do primeiro contato até a proposta ser enviada?
  6. Existe mais de uma pessoa atendendo o mesmo cliente ao mesmo tempo? Como isso é coordenado?
  7. O que faz um atendimento ser considerado "bem feito" pela 027, na sua visão?
  8. Quais diferenciais da 027 Viagens você espera que apareçam em toda proposta?
- **Documentos atualizados ao final:** `proposal-lifecycle.md` (etapas Lead, Qualificação, Primeiro contato, Levantamento das necessidades), `business-rules.md` (grupo Comercial: Políticas comerciais, Diferenciais), `glossary.md`.
- **Decisões esperadas:** se Qualificação é uma etapa própria ou parte do Primeiro contato; critério de qualificação de lead; lista de diferenciais fixos da 027.

## Workshop 2 — Financeiro

- **Objetivo:** entender formas de pagamento, parcelamento, câmbio e cancelamento — a base das Regras Financeiras (`business-rules.md`).
- **Participantes:** proprietário (Wefferson) e, se houver, responsável financeiro.
- **Perguntas:**
  1. Quais formas de pagamento vocês aceitam hoje?
  2. Como funciona o parcelamento — existe limite de parcelas, juros, ou isso varia por forma de pagamento/valor?
  3. O limite/condição de parcelamento varia por Destino, Formato, Finalidade ou Produto (`proposal-types.md`), ou é sempre igual?
  4. Vocês pedem sinal/entrada antes de confirmar (emitir) uma viagem? Qual percentual ou valor típico?
  5. Como o câmbio é tratado em propostas com Destino = Internacional — cobrado em reais, na moeda do destino, com alguma margem?
  6. O que acontece se o cliente atrasa um pagamento?
  7. Existe desconto padrão, ou todo desconto é negociado caso a caso? Quem pode autorizar desconto?
  8. Por quanto tempo uma proposta enviada permanece válida antes de precisar ser recotada?
  9. Quais são os prazos e percentuais de reembolso em caso de cancelamento? Isso muda se a viagem já foi paga ou emitida?
- **Documentos atualizados ao final:** `business-rules.md` (grupo Financeira: Regras de pagamento, Parcelamentos, Cancelamentos; e Validade de propostas no grupo Comercial), `universal-proposal-model.md` (seção `financeiro`), `proposal-status.md` (status Expirada, Cancelada).
- **Decisões esperadas:** política de parcelamento a ser implementada; regra de sinal mínimo; política de cancelamento/reembolso; prazo de validade padrão de proposta.

## Workshop 3 — Operação

- **Objetivo:** entender as particularidades de cada combinação de dimensões da proposta (`proposal-types.md`: Destino, Formato, Finalidade, Produto), documentação exigida, e como exceções são tratadas na prática.
- **Participantes:** proprietário (Wefferson) e quem monta cotações/roteiros no dia a dia.
- **Perguntas:**
  1. Quais combinações de Destino/Formato/Finalidade/Produto vocês mais vendem hoje?
  2. O que muda, na prática, entre montar uma proposta com Destino = Nacional e uma com Destino = Internacional?
  3. A partir de quantos passageiros uma viagem passa a ser tratada como Formato = Grupo? O que muda no processo a partir daí?
  4. Existem fornecedores/parceiros fixos que vocês sempre usam? Para quais combinações de dimensão?
  5. Existe alguma combinação "fora do padrão" que vocês recusam ou tratam de forma totalmente diferente?
  6. Quais documentos vocês pedem do cliente, e em que momento do processo?
  7. Para Destino = Internacional, o que vocês verificam (passaporte, visto, vacina)? Isso muda por destino específico?
  8. Como funciona a franquia de bagagem informada ao cliente — varia por companhia/Produto?
  9. Finalidade = Religioso: existe algo particular no processo (parceiros, roteiro fixo, forma de pagamento do grupo)?
  10. Finalidade = Corporativo: quem aprova e quem paga costuma ser a mesma pessoa que viaja? Como funciona o faturamento?
  11. Finalidade = Incentivo: como isso é diferente de Corporativo comum?
  12. Produto = Cruzeiro: o processo de cotação muda em relação a um pacote aéreo + hotel?
  13. Produto = Disney: existe algo específico (ingressos de parque, parceria) que torna esse um fluxo à parte?
  14. Conte uma situação recente em que uma proposta não seguiu o processo normal — o que aconteceu e por quê?
  15. Já aconteceu de uma proposta precisar ser refeita do zero por erro de cotação? O que causou e o que vocês fizeram?
  16. Existe algum cliente ou venda que a 027 trata de um jeito totalmente próprio, fora de tudo que já foi perguntado?
- **Documentos atualizados ao final:** `proposal-types.md` (as quatro dimensões e seus valores), `business-rules.md` (grupo Operacional: Bagagens, Grupos, Viagens internacionais, Viagens religiosas, Corporativo), `domain-map.md` (se surgir novo relacionamento), `tests/casos/` (casos fictícios revisados como combinações de dimensões).
- **Decisões esperadas:** valores finais de cada dimensão de `proposal-types.md`; regras operacionais por combinação; lista de casos de teste representativos.

## Workshop 4 — Emissão

- **Objetivo:** entender o que precisa estar resolvido para emitir uma viagem, documentação legal/seguro e o checklist interno.
- **Participantes:** proprietário (Wefferson) e quem executa a emissão.
- **Perguntas:**
  1. O que precisa estar 100% resolvido antes de vocês poderem emitir (confirmar) uma viagem?
  2. O que pode dar errado nesse momento (fornecedor sem disponibilidade, preço mudou)? Como vocês lidam quando isso acontece?
  3. Existe um checklist de itens a conferir antes de emitir? O que tem nele?
  4. Quem, na equipe, tem autonomia para emitir?
  5. Depois de emitida, uma proposta pode ainda mudar? Em que situação?
  6. Que documentos a 027 entrega ao cliente ao final (voucher, itinerário, bilhete, seguro)?
  7. Quando o seguro viagem é obrigatório vs. opcional? Existe cobertura mínima exigida?
  8. Existem avisos/observações que devem constar em toda proposta, independentemente do caso (ex: "sujeito a disponibilidade")?
  9. Existe alguma obrigação fiscal (nota fiscal, faturamento) a cumprir na emissão, especialmente em Finalidade = Corporativo?
- **Documentos atualizados ao final:** `proposal-lifecycle.md` (etapas Aprovação, Pagamento, Emissão, Entrega dos documentos), `proposal-actions.md` (ação Converter em emissão), `business-rules.md` (grupo Legal: Seguros, Observações obrigatórias).
- **Decisões esperadas:** checklist oficial de emissão; regra de obrigatoriedade de seguro; lista de observações obrigatórias.

## Workshop 5 — Pós-venda

- **Objetivo:** entender o que acontece depois que o passageiro viaja, e se isso deveria ser rastreado pela plataforma.
- **Participantes:** proprietário (Wefferson).
- **Perguntas:**
  1. Vocês fazem algum contato com o cliente depois que ele volta da viagem?
  2. Existe algum registro de satisfação, reclamação ou indicação gerada?
  3. Um cliente que já viajou com vocês recebe algum tratamento diferente numa próxima proposta?
  4. A 027 Viagens presta algum suporte ativo durante a viagem (emergência, reemissão)? Isso deveria gerar registro no histórico da proposta?
- **Documentos atualizados ao final:** `proposal-lifecycle.md` (etapas Viagem, Pós-venda), `glossary.md` (se surgir conceito novo, ex: "Indicação", "Cliente recorrente").
- **Decisões esperadas:** se pós-venda entra no escopo da plataforma já na Sprint 1B ou fica para um módulo/capacidade futura (ver `ARCHITECTURE.md`, capacidades de plataforma).

---

## Registro dos resultados

Cada workshop deve gerar atualizações nos documentos listados em sua própria seção "Documentos atualizados ao final" — nunca ficar só na ata da conversa. Uma pergunta só deve ser removida de um documento quando a resposta for registrada em outro — nunca simplesmente apagada.
