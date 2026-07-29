# Regras de Negócio — 027 Viagens

Este documento centraliza **todas as regras comerciais conhecidas** da 027 Viagens — o objetivo é que nenhuma regra de negócio fique escondida dentro do código. Cada seção segue a mesma estrutura: **Objetivo** (por que essa regra existe/importa), **Regras conhecidas** (confirmadas com o negócio), **Regras pendentes** (ainda não definidas), **Perguntas em aberto** (o que precisa ser perguntado — ver `discovery-workshop.md`) e **Observações**.

Nenhuma regra aqui foi inventada ou presumida como fato. Uma regra só sai de "Regras pendentes"/"Perguntas em aberto" e entra em "Regras conhecidas" depois de confirmada com o time comercial da 027 Viagens (ver processo em `docs/discovery-workshop.md`).

> Como usar: toda regra registrada aqui deve, mais cedo ou mais tarde, ter uma implementação correspondente em `src/core/` e, quando for texto voltado ao cliente, um texto correspondente em `content/`. Se uma regra muda aqui, o código e o conteúdo devem mudar junto. Termos usados nesta seção devem ser consistentes com `docs/glossary.md`.

---

## Políticas comerciais

- **Objetivo:** definir a postura geral de negociação e a governança de exceções da 027 Viagens.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** postura geral de atendimento; validade da agência para negociar condições fora do padrão; hierarquia de aprovação para exceções.
- **Perguntas em aberto:** ver seção Atendimento em `discovery-workshop.md`.
- **Observações:** —

## Validade de propostas

- **Objetivo:** definir por quanto tempo uma proposta emitida permanece válida e o que acontece após expirar.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** prazo padrão de validade; se varia por tipo de viagem ou valor; se há recotação automática ou reenvio manual ao expirar.
- **Perguntas em aberto:** ver `proposal-status.md` (status Expirada) e `discovery-workshop.md`, seção Financeiro.
- **Observações:** afeta diretamente o status `Expirada` em `proposal-status.md` — **recomenda-se priorizar esta seção antes do Sprint 1.**

## Regras de pagamento

- **Objetivo:** definir formas de pagamento aceitas e condições financeiras gerais.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** formas de pagamento aceitas (Pix, cartão, boleto, transferência); prazos; sinal/entrada mínima; moeda de cobrança em viagens internacionais.
- **Perguntas em aberto:** ver `discovery-workshop.md`, seção Financeiro (perguntas 1–4, 7).
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1** — afeta diretamente a seção `financeiro` do Modelo Universal (`universal-proposal-model.md`).

## Parcelamentos

- **Objetivo:** definir limites e condições de parcelamento.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** número máximo de parcelas por forma de pagamento; se há juros/taxa; se o limite varia por valor total ou tipo de cliente.
- **Perguntas em aberto:** ver `discovery-workshop.md`, seção Parcelamentos.
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1.**

## Diferenciais

- **Objetivo:** definir quais diferenciais da 027 Viagens devem aparecer em cada proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** diferenciais fixos (aparecem em toda proposta) vs. diferenciais específicos por tipo de viagem.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda no roteiro — sugerir incluir em uma futura rodada do workshop, seção Atendimento.
- **Observações:** ligado a `content/diferenciais/`.

## Seguros

- **Objetivo:** definir quando o seguro viagem é obrigatório ou opcional, e como entra no financeiro da proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** obrigatoriedade por tipo de viagem (ex: internacional); fornecedores parceiros; cobertura mínima recomendada.
- **Perguntas em aberto:** ver `proposal-types.md` (tipo Internacional) e `discovery-workshop.md`, seção Casos especiais.
- **Observações:** —

## Bagagens

- **Objetivo:** definir como a franquia de bagagem é informada e cobrada.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** franquia padrão por tipo de viagem/companhia; regras de bagagem extra; se isso entra automaticamente como observação na proposta.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — sugerir incluir na seção Viagens de uma futura rodada.
- **Observações:** —

## Grupos

- **Objetivo:** definir a partir de quando uma viagem é tratada como "grupo" e quais regras se aplicam.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** número mínimo de passageiros para ser "Grupo"; desconto por volume; exigências específicas de documentação/pagamento.
- **Perguntas em aberto:** ver `proposal-types.md` (tipo Grupos) e `discovery-workshop.md`, seção Viagens (pergunta 4).
- **Observações:** relevante para o caso de teste "grupo" em `tests/casos/`.

## Viagens internacionais

- **Objetivo:** definir documentação e avisos obrigatórios para viagens ao exterior.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** documentação obrigatória a mencionar (passaporte, visto, validade mínima); avisos padrão sobre câmbio; relação com a política de Seguros acima.
- **Perguntas em aberto:** ver `proposal-types.md` (tipo Internacional) e `discovery-workshop.md`, seção Documentação.
- **Observações:** relevante para o caso de teste "internacional" em `tests/casos/`.

## Viagens religiosas

- **Objetivo:** definir particularidades de pacotes religiosos.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** roteiros fixos; parcerias com grupos/lideranças religiosas; condições comerciais específicas.
- **Perguntas em aberto:** ver `proposal-types.md` (tipo Religioso) e `discovery-workshop.md`, seção Casos especiais (pergunta 1).
- **Observações:** relevante para o caso de teste "religioso" em `tests/casos/`.

## Corporativo

- **Objetivo:** definir diferenças de atendimento/condições para clientes pessoa jurídica.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** faturamento; prazos de pagamento diferenciados; emissão de nota fiscal; relação entre `Cliente` (empresa) e `Passageiro` (funcionário).
- **Perguntas em aberto:** ver `proposal-types.md` (tipo Corporativo) e `discovery-workshop.md`, seção Casos especiais (pergunta 2).
- **Observações:** relevante para o caso de teste "corporativa" em `tests/casos/`.

## Cancelamentos

- **Objetivo:** definir prazos, percentuais de reembolso e taxas em caso de cancelamento.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** prazos/percentuais de reembolso por antecedência; taxas de fornecedores repassadas; diferença entre cancelar proposta não paga vs. viagem já confirmada.
- **Perguntas em aberto:** ver `discovery-workshop.md`, seção Exceções (pergunta 2).
- **Observações:** liga-se diretamente ao status `Cancelada` em `proposal-status.md`.

## Observações obrigatórias

- **Objetivo:** definir quais avisos devem constar em toda proposta, independentemente do tipo de viagem.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de avisos obrigatórios hoje só presentes na memória de quem redige manualmente (ex: "valores sujeitos a disponibilidade").
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — sugerir incluir na seção Documentação de uma futura rodada.
- **Observações:** **recomenda-se priorizar esta seção antes do Sprint 1** — afeta a seção `observações` do Modelo Universal.

## Serviços opcionais

- **Objetivo:** definir quais serviços podem ser oferecidos como opcionais e como são precificados.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de opcionais possíveis (passeios, traslados extras, upgrade); forma de precificação/adição ao financeiro.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — sugerir incluir na seção Viagens de uma futura rodada.
- **Observações:** —

## Upsell

- **Objetivo:** definir critérios para sugerir um upgrade dentro da proposta.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** critério/momento de sugerir upgrade de categoria de hotel, classe aérea, pacote de seguro mais completo.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — natural de explorar quando a IA Comercial (`ai/`) for priorizada.
- **Observações:** ligado à seleção automática de textos por tipo de viagem descrita em `ARCHITECTURE.md`.

## Cross-sell

- **Objetivo:** definir quais serviços complementares devem ser sugeridos junto da proposta principal.
- **Regras conhecidas:** nenhuma confirmada ainda.
- **Regras pendentes:** lista de serviços complementares (seguro, passeios, aluguel de carro, chip internacional) e critério de sugestão.
- **Perguntas em aberto:** nenhuma pergunta dedicada ainda — mesma observação de Upsell.
- **Observações:** —

---

## Status de preenchimento

| Seção | Regras conhecidas | Prioridade antes do Sprint 1 |
|---|---|---|
| Políticas comerciais | Nenhuma | Baixa |
| Validade de propostas | Nenhuma | **Alta** |
| Regras de pagamento | Nenhuma | **Alta** |
| Parcelamentos | Nenhuma | **Alta** |
| Diferenciais | Nenhuma | Média |
| Seguros | Nenhuma | Média |
| Bagagens | Nenhuma | Baixa |
| Grupos | Nenhuma | Média |
| Viagens internacionais | Nenhuma | Média |
| Viagens religiosas | Nenhuma | Baixa |
| Corporativo | Nenhuma | Média |
| Cancelamentos | Nenhuma | **Alta** |
| Observações obrigatórias | Nenhuma | **Alta** |
| Serviços opcionais | Nenhuma | Baixa |
| Upsell | Nenhuma | Baixa (pós Sprint 1) |
| Cross-sell | Nenhuma | Baixa (pós Sprint 1) |

Todas as seções seguem 100% pendentes de definição com o time comercial da 027 Viagens. As de prioridade **Alta** (Validade, Pagamento, Parcelamentos, Cancelamentos, Observações obrigatórias) afetam diretamente campos do Modelo Universal da Proposta (`docs/universal-proposal-model.md`) e devem ser cobertas no Workshop de Descoberta antes do Sprint 1.
