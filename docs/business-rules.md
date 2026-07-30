# Regras de Negócio — 027 Viagens

Este documento centraliza **todas as regras comerciais conhecidas** da 027 Viagens — o objetivo é que nenhuma regra de negócio fique escondida dentro do código. As 16 seções originais permanecem, agora organizadas em **quatro grupos** (Comerciais, Financeiras, Operacionais, Legais), conforme decidido na revisão arquitetural pré-Sprint 1A (ver [ADR 0005](decisoes/0005-refinamento-pre-sprint-1a.md)). Cada seção individual segue a mesma estrutura: **Objetivo**, **Regras conhecidas**, **Regras pendentes**, **Perguntas em aberto** e **Observações**.

Nenhuma regra aqui foi inventada ou presumida como fato. Uma regra só sai de "Regras pendentes"/"Perguntas em aberto" e entra em "Regras conhecidas" depois de confirmada com o time comercial da 027 Viagens (ver processo em `docs/discovery-workshop.md`).

> Como usar: toda regra registrada aqui deve, mais cedo ou tarde, ter uma implementação correspondente em `src/domain/` (comportamento/validação de uma Entidade) ou `src/application/` (regra que envolve mais de um Aggregate) e, quando for texto voltado ao cliente, um texto correspondente em `content/`. Se uma regra muda aqui, o código e o conteúdo devem mudar junto. Termos usados nesta seção devem ser consistentes com `docs/glossary.md`.

---

# Regras Comerciais

Regras sobre como a 027 Viagens negocia, precifica sua oferta comercial e se diferencia — o que é oferecido e em que condições, independentemente de execução financeira ou operacional.

## Políticas comerciais

- **Objetivo:** definir a postura geral de negociação e a governança de exceções da 027 Viagens.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** postura geral de atendimento; validade da agência para negociar condições fora do padrão; hierarquia de aprovação para exceções.
- **Perguntas em aberto:** ver Workshop 1 (Atendimento) em `discovery-workshop.md`.
- **Observações:** —

## Validade de propostas

- **Objetivo:** definir por quanto tempo uma proposta emitida permanece válida e o que acontece após expirar.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** prazo padrão de validade; se varia por Destino/Formato/Finalidade/Produto (ver `proposal-types.md`) ou valor; se há recotação automática ou reenvio manual ao expirar.
- **Perguntas em aberto:** ver `proposal-status.md` (status Expirada) e Workshop 2 (Financeiro) em `discovery-workshop.md`.
- **Observações:** afeta diretamente o status `Expirada` em `proposal-status.md` — **recomenda-se priorizar esta seção antes do Sprint 1B.**

## Diferenciais

- **Objetivo:** definir quais diferenciais da 027 Viagens devem aparecer em cada proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** diferenciais fixos (aparecem em toda proposta) vs. diferenciais específicos por combinação de dimensões (`proposal-types.md`).
- **Perguntas em aberto:** ver Workshop 1 (Atendimento) em `discovery-workshop.md`.
- **Observações:** ligado a `content/diferenciais/`.

## Serviços opcionais

- **Objetivo:** definir quais serviços podem ser oferecidos como opcionais e como são precificados.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de opcionais possíveis (passeios, traslados extras, upgrade); forma de precificação/adição ao financeiro.
- **Perguntas em aberto:** ver Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** —

## Upsell

- **Objetivo:** definir critérios para sugerir um upgrade dentro da proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** critério/momento de sugerir upgrade de categoria de hotel, classe aérea, pacote de seguro mais completo.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — natural de explorar quando a IA Comercial (`ai/`) for priorizada.
- **Observações:** ligado à seleção automática de textos por combinação de dimensões descrita em `ARCHITECTURE.md`.

## Cross-sell

- **Objetivo:** definir quais serviços complementares devem ser sugeridos junto da proposta principal.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de serviços complementares (seguro, passeios, aluguel de carro, chip internacional) e critério de sugestão.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — mesma observação de Upsell.
- **Observações:** —

---

# Regras Financeiras

Regras sobre dinheiro: como se cobra, como se parcela, e o que acontece financeiramente quando algo é cancelado.

## Regras de pagamento

- **Objetivo:** definir formas de pagamento aceitas e condições financeiras gerais.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** formas de pagamento aceitas (Pix, cartão, boleto, transferência); prazos; sinal/entrada mínima; moeda de cobrança quando Destino = Internacional.
- **Perguntas em aberto:** ver Workshop 2 (Financeiro) em `discovery-workshop.md`.
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1B** — afeta diretamente a seção `financeiro` do Modelo Universal (`universal-proposal-model.md`).

## Parcelamentos

- **Objetivo:** definir limites e condições de parcelamento.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** número máximo de parcelas por forma de pagamento; se há juros/taxa; se o limite varia por valor total ou tipo de cliente.
- **Perguntas em aberto:** ver Workshop 2 (Financeiro) em `discovery-workshop.md`.
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1B.**

## Cancelamentos

- **Objetivo:** definir prazos, percentuais de reembolso e taxas em caso de cancelamento.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** prazos/percentuais de reembolso por antecedência; taxas de fornecedores repassadas; diferença entre cancelar proposta não paga vs. viagem já confirmada.
- **Perguntas em aberto:** ver Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** liga-se diretamente ao status `Cancelada` em `proposal-status.md`; pode ter implicação legal (direito de arrependimento/consumidor) além da financeira — ver seção Legal abaixo.

---

# Regras Operacionais

Regras sobre como a operação lida com a execução prática da viagem — o que muda conforme o tipo de operação, independentemente de preço ou política comercial.

## Bagagens

- **Objetivo:** definir como a franquia de bagagem é informada e cobrada.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** franquia padrão por companhia/Produto (`proposal-types.md`); regras de bagagem extra; se isso entra automaticamente como observação na proposta.
- **Perguntas em aberto:** ver Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** —

## Grupos

- **Objetivo:** definir a partir de quando uma viagem é tratada como Formato = Grupo e quais regras se aplicam.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** número mínimo de passageiros para ser "Grupo"; desconto por volume; exigências específicas de documentação/pagamento.
- **Perguntas em aberto:** ver `proposal-types.md` (dimensão Formato) e Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** relevante para o caso de teste "grupo" em `tests/casos/`.

## Viagens internacionais

- **Objetivo:** definir documentação e avisos obrigatórios quando Destino = Internacional.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** documentação obrigatória a mencionar (passaporte, visto, validade mínima); avisos padrão sobre câmbio; relação com a política de Seguros abaixo.
- **Perguntas em aberto:** ver `proposal-types.md` (dimensão Destino) e Workshop 4 (Emissão) em `discovery-workshop.md`.
- **Observações:** relevante para o caso de teste "internacional" em `tests/casos/`.

## Viagens religiosas

- **Objetivo:** definir particularidades quando Finalidade = Religioso.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** roteiros fixos; parcerias com grupos/lideranças religiosas; condições comerciais específicas.
- **Perguntas em aberto:** ver `proposal-types.md` (dimensão Finalidade) e Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** relevante para o caso de teste "religioso" em `tests/casos/`.

## Corporativo

- **Objetivo:** definir diferenças de atendimento/condições quando Finalidade = Corporativo.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** prazos de pagamento diferenciados; relação entre `Cliente` (empresa) e `Passageiro` (funcionário) — ver `domain-map.md`. Faturamento/nota fiscal está registrado também em Regras Legais, abaixo.
- **Perguntas em aberto:** ver `proposal-types.md` (dimensão Finalidade) e Workshop 3 (Operação) em `discovery-workshop.md`.
- **Observações:** relevante para o caso de teste "corporativa" em `tests/casos/`.

---

# Regras Legais

Regras ligadas a obrigações legais/regulatórias e a avisos que protegem a 027 Viagens e o cliente — não são escolha comercial, são exigência (documental, fiscal ou de comunicação obrigatória).

## Seguros

- **Objetivo:** definir quando o seguro viagem é obrigatório ou opcional, e como entra no financeiro da proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** obrigatoriedade quando Destino = Internacional; fornecedores parceiros; cobertura mínima recomendada/exigida.
- **Perguntas em aberto:** ver `proposal-types.md` (dimensão Destino) e Workshop 4 (Emissão) em `discovery-workshop.md`.
- **Observações:** —

## Observações obrigatórias

- **Objetivo:** definir quais avisos devem constar em toda proposta, independentemente da combinação de dimensões.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de avisos obrigatórios hoje só presentes na memória de quem redige manualmente (ex: "valores sujeitos a disponibilidade"); obrigações fiscais (nota fiscal, faturamento — ver Corporativo, acima) quando aplicável.
- **Perguntas em aberto:** ver Workshop 4 (Emissão) em `discovery-workshop.md`.
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1B** — afeta a seção `observações` do Modelo Universal.

---

## Status de preenchimento

| Grupo | Seção | Regras conhecidas | Prioridade antes do Sprint 1B |
|---|---|---|---|
| Comercial | Políticas comerciais | Nenhuma | Baixa |
| Comercial | Validade de propostas | Nenhuma | **Alta** |
| Comercial | Diferenciais | Nenhuma | Média |
| Comercial | Serviços opcionais | Nenhuma | Baixa |
| Comercial | Upsell | Nenhuma | Baixa (pós Sprint 1) |
| Comercial | Cross-sell | Nenhuma | Baixa (pós Sprint 1) |
| Financeira | Regras de pagamento | Nenhuma | **Alta** |
| Financeira | Parcelamentos | Nenhuma | **Alta** |
| Financeira | Cancelamentos | Nenhuma | **Alta** |
| Operacional | Bagagens | Nenhuma | Baixa |
| Operacional | Grupos | Nenhuma | Média |
| Operacional | Viagens internacionais | Nenhuma | Média |
| Operacional | Viagens religiosas | Nenhuma | Baixa |
| Operacional | Corporativo | Nenhuma | Média |
| Legal | Seguros | Nenhuma | Média |
| Legal | Observações obrigatórias | Nenhuma | **Alta** |

Todas as seções seguem 100% pendentes de definição com o time comercial da 027 Viagens. As de prioridade **Alta** (Validade, Pagamento, Parcelamentos, Cancelamentos, Observações obrigatórias) afetam diretamente campos do Modelo Universal da Proposta (`docs/universal-proposal-model.md`) e devem ser cobertas no Workshop de Descoberta antes do Sprint 1B — a Sprint 1A (Modelagem do Domínio) não depende dessas respostas, pois não envolve regras nem obrigatoriedade.
