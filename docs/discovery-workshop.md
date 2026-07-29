# Workshop de Descoberta — Roteiro de Entrevista

Roteiro estruturado para conduzir o levantamento de conhecimento do negócio com o proprietário da 027 Viagens (Wefferson), hoje a principal fonte de conhecimento operacional da empresa. O objetivo é extrair regras reais, não confirmar suposições já escritas — por isso as perguntas são abertas.

## Como usar este roteiro

- Uma sessão por assunto costuma funcionar melhor que uma sessão única cobrindo tudo — assuntos como Financeiro e Documentação têm profundidade própria.
- Sempre que uma resposta introduzir um termo novo (ex: um nome interno para uma etapa ou papel), registrar em `docs/glossary.md` antes de seguir.
- Sempre que uma resposta confirmar ou corrigir algo já escrito em `proposal-types.md`, `proposal-lifecycle.md`, `proposal-status.md`, `proposal-actions.md` ou `proposal-versioning.md`, atualizar o documento correspondente logo depois da sessão, enquanto está fresco.
- Perguntas de "casos especiais" tendem a render mais regra de negócio real do que perguntas sobre o caso padrão — não pular essa seção.

---

## Atendimento

1. Como um cliente novo chega até a 027 Viagens hoje (canais)?
2. O que você (ou a equipe) precisa saber do cliente antes de começar a montar uma cotação?
3. Existe algum roteiro ou checklist de perguntas que vocês já fazem hoje, mesmo informalmente?
4. Quanto tempo, tipicamente, leva do primeiro contato até a proposta ser enviada?
5. Existe mais de uma pessoa atendendo o mesmo cliente ao mesmo tempo? Como isso é coordenado?
6. O que faz um atendimento ser considerado "bem feito" pela 027, na sua visão?

## Financeiro

1. Quais formas de pagamento vocês aceitam hoje?
2. Como funciona o parcelamento — existe limite de parcelas, juros, ou isso varia por forma de pagamento/valor?
3. Vocês pedem sinal/entrada antes de confirmar (emitir) uma viagem? Qual percentual ou valor típico?
4. Como o câmbio é tratado em propostas internacionais — cobrado em reais, na moeda do destino, com alguma margem?
5. O que acontece se o cliente atrasa um pagamento?
6. Existe desconto padrão, ou todo desconto é negociado caso a caso? Quem pode autorizar desconto?
7. Como emissão e pagamento se relacionam — vocês emitem só com pagamento 100% confirmado, ou existe emissão contra sinal?

## Viagens

1. Quais tipos de viagem vocês mais vendem hoje? (usar como referência a lista de `proposal-types.md`, mas sem induzir a resposta)
2. Existe algum tipo de viagem que a lista de `proposal-types.md` não cobre?
3. O que muda, na prática, entre montar uma proposta nacional e uma internacional?
4. Como funciona uma viagem em grupo — a partir de quantas pessoas isso muda o processo?
5. Existem fornecedores/parceiros fixos que vocês sempre usam? Para quais tipos de viagem?
6. Existe alguma viagem "fora do padrão" que vocês recusam ou tratam de forma totalmente diferente?

## Documentação

1. Quais documentos vocês pedem do cliente, e em que momento do processo?
2. Para viagens internacionais, o que vocês verificam (passaporte, visto, vacina)? Isso muda por destino?
3. Que documentos a 027 entrega ao cliente ao final (voucher, itinerário, bilhete, seguro)?
4. Existe algum documento interno (checklist de emissão, por exemplo) que só a equipe vê?
5. Como esses documentos são organizados/guardados hoje?

## Parcelamentos

1. (Se não coberto em Financeiro) O parcelamento varia por tipo de viagem, valor total, ou cliente?
2. Existe uma tabela de parcelamento que vocês usam como referência, ou é decidido caso a caso?
3. O parcelamento acontece direto com a 027 ou através de operadora/cartão?

## Emissão

1. O que precisa estar 100% resolvido antes de vocês poderem emitir (confirmar) uma viagem?
2. O que pode dar errado nesse momento (fornecedor sem disponibilidade, preço mudou)? Como vocês lidam quando isso acontece?
3. Existe um checklist de itens a conferir antes de emitir? O que tem nele?
4. Quem, na equipe, tem autonomia para emitir?
5. Depois de emitida, uma proposta pode ainda mudar? Em que situação?

## Pós-venda

1. Vocês fazem algum contato com o cliente depois que ele volta da viagem?
2. Existe algum registro de satisfação, reclamação ou indicação gerada?
3. Um cliente que já viajou com vocês recebe algum tratamento diferente numa próxima proposta?

## Exceções

1. Conte uma situação recente em que uma proposta não seguiu o processo normal — o que aconteceu e por quê?
2. O que vocês fazem quando o cliente pede para cancelar depois de já ter pago?
3. Existe alguma situação em que vocês emitem sem seguir todas as etapas normais (urgência, cliente antigo de confiança)?
4. Já aconteceu de uma proposta precisar ser refeita do zero por erro de cotação? O que causou e o que vocês fizeram?

## Casos especiais

1. Viagem religiosa: existe algo particular no processo (parceiros, roteiro fixo, forma de pagamento do grupo)?
2. Viagem corporativa: quem aprova e quem paga costuma ser a mesma pessoa que viaja? Como funciona o faturamento?
3. Viagem de incentivo: como isso é diferente de uma corporativa comum?
4. Cruzeiro: o processo de cotação/emissão muda em relação a um pacote aéreo + hotel?
5. Disney: existe algo específico (ingressos de parque, parceria) que torna esse um fluxo à parte?
6. Existe algum cliente ou tipo de venda que a 027 trata de um jeito totalmente próprio, fora de tudo que já foi perguntado aqui?

---

## Registro dos resultados

Cada sessão deste workshop deve gerar atualizações em pelo menos um destes documentos:

- Respostas que confirmam/corrigem tipos de proposta → `docs/proposal-types.md`
- Respostas sobre o fluxo do processo → `docs/proposal-lifecycle.md`
- Respostas sobre estados/transições → `docs/proposal-status.md`
- Respostas sobre o que pode ser feito com uma proposta → `docs/proposal-actions.md`
- Respostas sobre quando uma mudança gera nova versão → `docs/proposal-versioning.md`
- Qualquer regra comercial concreta → `docs/business-rules.md` (sai de "Regras pendentes" e entra em "Regras conhecidas")
- Qualquer termo novo ou redefinido → `docs/glossary.md`

Uma pergunta só deve ser removida de um documento quando a resposta for registrada em outro — nunca simplesmente apagada.
