# Regras de Negócio — 027 Viagens

Este documento centraliza **todas as regras comerciais conhecidas** da 027 Viagens — o objetivo é que nenhuma regra de negócio fique escondida dentro do código. Cada seção abaixo é um "recipiente": onde a regra já é conhecida, ela é registrada; onde ainda não foi definida, fica marcada como **pendente**, para ser preenchida junto com o time comercial antes (ou durante) o Sprint 1.

Nenhuma regra aqui foi inventada — este documento não deve conter suposições apresentadas como fato. Regras pendentes devem ser validadas com o time comercial da 027 Viagens antes de virarem código em `src/core/`.

> Como usar: toda regra registrada aqui deve, mais cedo ou mais tarde, ter uma implementação correspondente em `src/core/` e, quando for texto voltado ao cliente, um texto correspondente em `content/`. Se uma regra muda aqui, o código e o conteúdo devem mudar junto.

## Políticas comerciais

*Pendente.* Deve cobrir: postura geral de atendimento, validade da agência para negociar condições fora do padrão, hierarquia de aprovação para exceções.

## Validade de propostas

*Pendente.* Deve cobrir: por quantos dias uma proposta emitida permanece válida, o que acontece após expirar (recotação automática? reenvio manual?), se a validade varia por tipo de viagem ou de valor.

## Regras de pagamento

*Pendente.* Deve cobrir: formas de pagamento aceitas (Pix, cartão, boleto, transferência), prazos, sinal/entrada mínima, moeda de cobrança em viagens internacionais.

## Parcelamentos

*Pendente.* Deve cobrir: número máximo de parcelas por forma de pagamento, se há juros ou taxa por parcelamento, se o limite varia por valor total da viagem ou por tipo de cliente.

## Diferenciais

*Pendente.* Deve cobrir: quais diferenciais da 027 Viagens devem aparecer em toda proposta (ex: atendimento personalizado, parcerias, suporte 24h), e quais são específicos por tipo de viagem — ligado a `content/diferenciais/`.

## Seguros

*Pendente.* Deve cobrir: quando o seguro viagem é obrigatório (ex: viagens internacionais) vs. opcional, fornecedores parceiros, cobertura mínima recomendada, como o valor do seguro entra no financeiro da proposta.

## Bagagens

*Pendente.* Deve cobrir: franquia padrão informada por tipo de viagem/companhia aérea, regras de bagagem extra, como isso é comunicado na proposta (inclusão automática de aviso?).

## Grupos

*Pendente.* Deve cobrir: a partir de quantos passageiros uma viagem é tratada como "grupo", regras de desconto por grupo, exigências específicas de documentação/pagamento para grupos — relevante para o caso de teste "grupo" em `tests/casos/`.

## Viagens internacionais

*Pendente.* Deve cobrir: documentação obrigatória a mencionar (passaporte, visto, validade mínima do passaporte), avisos padrão sobre câmbio/moeda, política de seguro (ver seção Seguros) — relevante para o caso de teste "internacional" em `tests/casos/`.

## Viagens religiosas

*Pendente.* Deve cobrir: particularidades desse tipo de pacote (ex: roteiros fixos, parcerias com grupos/lideranças religiosas, condições comerciais específicas) — relevante para o caso de teste "religioso" em `tests/casos/`.

## Corporativo

*Pendente.* Deve cobrir: diferenças de atendimento/condições para clientes pessoa jurídica, faturamento, prazos de pagamento diferenciados, emissão de nota fiscal — relevante para o caso de teste "corporativa" em `tests/casos/`.

## Cancelamentos

*Pendente.* Deve cobrir: prazos e percentuais de reembolso por antecedência de cancelamento, taxas de fornecedores repassadas, diferença de política entre proposta ainda não paga vs. viagem já confirmada.

## Observações obrigatórias

*Pendente.* Deve cobrir: quais avisos/observações são obrigatórios em toda proposta, independentemente do tipo de viagem (ex: "valores sujeitos a disponibilidade", "sujeito a confirmação"), e que hoje talvez só existam na memória de quem redige manualmente.

## Serviços opcionais

*Pendente.* Deve cobrir: quais serviços podem ser oferecidos como opcionais dentro da proposta (passeios, traslados extras, upgrade de categoria) e como são precificados/adicionados ao financeiro.

## Upsell

*Pendente.* Deve cobrir: em que momento e sob que critério a proposta deve sugerir um upgrade (categoria de hotel, classe aérea, pacote de seguro mais completo) — ligado à seleção automática de textos por tipo de viagem descrita em `ARCHITECTURE.md`.

## Cross-sell

*Pendente.* Deve cobrir: quais serviços complementares devem ser sugeridos junto da proposta principal (seguro, passeios, aluguel de carro, chip internacional) e sob que critério.

---

## Status de preenchimento

| Seção | Status |
|---|---|
| Políticas comerciais | Pendente |
| Validade de propostas | Pendente |
| Regras de pagamento | Pendente |
| Parcelamentos | Pendente |
| Diferenciais | Pendente |
| Seguros | Pendente |
| Bagagens | Pendente |
| Grupos | Pendente |
| Viagens internacionais | Pendente |
| Viagens religiosas | Pendente |
| Corporativo | Pendente |
| Cancelamentos | Pendente |
| Observações obrigatórias | Pendente |
| Serviços opcionais | Pendente |
| Upsell | Pendente |
| Cross-sell | Pendente |

Todas as seções estão pendentes de definição com o time comercial da 027 Viagens. Recomenda-se preencher ao menos **Validade de propostas**, **Regras de pagamento/Parcelamentos** e **Observações obrigatórias** antes do Sprint 1, já que essas regras afetam diretamente os campos do Modelo Universal da Proposta (`docs/universal-proposal-model.md`).
