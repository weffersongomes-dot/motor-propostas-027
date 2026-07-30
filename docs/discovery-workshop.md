# Workshops de Descoberta

Roteiro estruturado para levantar o conhecimento operacional da 027 Viagens com o proprietário (Wefferson), hoje a principal fonte desse conhecimento. O levantamento é dividido em **cinco workshops independentes** (mesma organização por assunto desde a Sprint 0.5), cada um podendo ser conduzido em uma sessão própria.

> **Mudança de método (Sprint B1):** a partir de agora, cada workshop é conduzido **a partir de casos reais**, não de uma lista de perguntas abertas. Em vez de perguntar "como funciona o processo de X?", pedimos "conte uma [operação real] que aconteceu" e reconstruímos a história inteira em `docs/business-cases/`. Perguntas genéricas continuam existindo neste documento, mas como **sondagem de acompanhamento** — usadas para preencher lacunas que a história não cobriu sozinha, nunca como ponto de partida.

## Por que mudar de método

Perguntas abertas genéricas tendem a produzir descrições do processo *idealizado* — a pessoa entrevistada descreve como as coisas deveriam funcionar, não necessariamente como aconteceram da última vez. Pedir uma história real força a aparecerem os detalhes que fazem a diferença para modelar o domínio: a exceção que ninguém tinha mencionado, o retrabalho que consumiu uma tarde, a aprovação informal que só aconteceu porque o cliente é conhecido. Ver `docs/business-cases/README.md` para o raciocínio completo.

## Como conduzir cada sessão

1. **Escolha 1–2 casos** do workshop (ver tabela abaixo), correspondentes a arquivos em `docs/business-cases/`.
2. **Peça a história completa**, sem interromper no início: "conte uma [tipo de operação] real que você lembra — do começo ao fim, ou até onde a história chegou."
3. **Enquanto ouve, preencha ao vivo** as seções do arquivo de caso (Contexto, Sequência cronológica, Decisões, Documentos, Aprovações, Alterações, Retrabalho, Comunicação, Riscos, Problemas, Exceções).
4. **Só depois de a história terminar**, use as perguntas de sondagem deste documento para cobrir o que não apareceu sozinho.
5. **Ao final da sessão**, execute o Protocolo pós-entrevista (abaixo) antes de encerrar — não deixar para depois.

## Protocolo pós-entrevista

Toda sessão, de qualquer workshop, termina executando estes passos, nesta ordem:

1. **Fechar o(s) arquivo(s) de caso** em `docs/business-cases/` — todas as seções preenchidas (ou explicitamente marcadas como "não perguntado nesta sessão", nunca deixadas ambíguas entre "vazio por esquecimento" e "vazio porque não se aplica").
2. **Atualizar `docs/business-rules.md`** — toda regra identificada na seção "Possíveis regras de negócio" do caso que for confirmada (não hipotética) migra de "Regras pendentes"/"Perguntas em aberto" para "Regras conhecidas", com referência ao caso de origem (ex: "confirmado no caso `business-cases/cancelamento.md`").
3. **Atualizar `docs/proposal-types.md`** — se o caso confirmar ou corrigir algo sobre as dimensões Destino/Formato/Finalidade/Produto.
4. **Atualizar `docs/proposal-lifecycle.md`** — se o caso revelar uma etapa, exceção ou responsável não documentado.
5. **Atualizar `docs/domain-decisions.md`** — se o caso sugerir uma decisão de modelagem (ex: "remarcação parece ser sempre uma nova versão, nunca uma proposta nova" vira uma entrada aqui antes de virar código).
6. **Atualizar `docs/glossary.md`** — todo termo novo usado pelo entrevistado que ainda não está no glossário.
7. **Extrair para `knowledge/`** — se o caso mencionar um fornecedor, destino ou forma de pagamento específico com informação reutilizável (ver `knowledge/README.md`).

Nenhum passo é opcional "se der tempo" — uma sessão sem os 7 passos é uma sessão incompleta, mesmo que a história tenha sido bem contada.

---

## Workshop 1 — Atendimento

- **Objetivo:** entender como um lead chega, como é qualificado e atendido até a proposta ser enviada — a parte inicial do ciclo de vida (`proposal-lifecycle.md`, etapas Lead a Proposta).
- **Participantes:** proprietário (Wefferson) e, se houver, quem faz atendimento direto ao cliente.
- **Casos reais a pedir:** `docs/business-cases/venda-nacional.md`, `docs/business-cases/venda-internacional.md`.
- **Perguntas de sondagem (usar depois da história, para preencher lacunas):**
  1. Existe uma etapa de Qualificação separada do Primeiro contato, ou elas acontecem juntas? O que faz um lead ser "qualificado"?
  2. Existe algum roteiro ou checklist de perguntas que vocês já fazem hoje, mesmo informalmente?
  3. Existe mais de uma pessoa atendendo o mesmo cliente ao mesmo tempo? Como isso é coordenado?
  4. Quais diferenciais da 027 Viagens você espera que apareçam em toda proposta?
- **Documentos atualizados ao final:** ver Protocolo pós-entrevista, com foco em `proposal-lifecycle.md` (etapas Lead, Qualificação, Primeiro contato, Levantamento das necessidades) e `business-rules.md` (grupo Comercial: Políticas comerciais, Diferenciais).
- **Decisões esperadas:** se Qualificação é uma etapa própria ou parte do Primeiro contato; critério de qualificação de lead; lista de diferenciais fixos da 027.

## Workshop 2 — Financeiro

- **Objetivo:** entender formas de pagamento, parcelamento, câmbio, validade e cancelamento — a base das Regras Financeiras (`business-rules.md`).
- **Participantes:** proprietário (Wefferson) e, se houver, responsável financeiro.
- **Casos reais a pedir:** `docs/business-cases/cancelamento.md`, `docs/business-cases/remarcacao.md`.
- **Perguntas de sondagem:**
  1. Quais formas de pagamento vocês aceitam hoje, e existe limite/juros de parcelamento?
  2. O limite/condição de parcelamento varia por Destino, Formato, Finalidade ou Produto (`proposal-types.md`), ou é sempre igual?
  3. Vocês pedem sinal/entrada antes de confirmar (emitir) uma viagem? Qual percentual ou valor típico?
  4. Como o câmbio é tratado em propostas com Destino = Internacional?
  5. Existe desconto padrão, ou todo desconto é negociado caso a caso? Quem pode autorizar desconto?
  6. Por quanto tempo uma proposta enviada permanece válida antes de precisar ser recotada?
- **Documentos atualizados ao final:** ver Protocolo pós-entrevista, com foco em `business-rules.md` (grupo Financeira: Regras de pagamento, Parcelamentos, Cancelamentos; Validade de propostas no grupo Comercial), `proposal-status.md` (status Expirada, Cancelada), `proposal-actions.md` (avaliar se "Remarcar" precisa virar ação própria — ver `business-cases/remarcacao.md`).
- **Decisões esperadas:** política de parcelamento a ser implementada; regra de sinal mínimo; política de cancelamento/reembolso; prazo de validade padrão de proposta; se remarcação é ação distinta de editar/cancelar.

## Workshop 3 — Operação

- **Objetivo:** entender as particularidades de cada combinação de dimensões da proposta (`proposal-types.md`: Destino, Formato, Finalidade, Produto), documentação exigida, e como exceções/alterações são tratadas na prática.
- **Participantes:** proprietário (Wefferson) e quem monta cotações/roteiros no dia a dia.
- **Casos reais a pedir:** `docs/business-cases/grupo.md`, `docs/business-cases/viagem-religiosa.md`, `docs/business-cases/corporativo.md`, `docs/business-cases/disney.md`, `docs/business-cases/alteracao-passageiros.md`, `docs/business-cases/alteracao-hotel.md`, `docs/business-cases/alteracao-voo.md`. (Sete casos — pode exigir mais de uma sessão; priorizar Grupo e Corporativo primeiro.)
- **Perguntas de sondagem:**
  1. Existem fornecedores/parceiros fixos que vocês sempre usam? Para quais combinações de dimensão?
  2. Existe alguma combinação "fora do padrão" que vocês recusam ou tratam de forma totalmente diferente?
  3. Para Destino = Internacional, o que vocês verificam (passaporte, visto, vacina)? Isso muda por destino específico?
  4. Como funciona a franquia de bagagem informada ao cliente — varia por companhia/Produto?
  5. Finalidade = Incentivo: como isso é diferente de Corporativo comum?
  6. Produto = Cruzeiro: o processo de cotação muda em relação a um pacote aéreo + hotel? (nenhum caso dedicado ainda — considerar criar `business-cases/cruzeiro.md` se relevante)
  7. Já aconteceu de uma proposta precisar ser refeita do zero por erro de cotação? O que causou e o que vocês fizeram?
- **Documentos atualizados ao final:** ver Protocolo pós-entrevista, com foco em `proposal-types.md` (as quatro dimensões e seus valores), `business-rules.md` (grupo Operacional), `domain-map.md` (se surgir novo relacionamento), `tests/casos/` (casos fictícios revisados como combinações de dimensões).
- **Decisões esperadas:** valores finais de cada dimensão de `proposal-types.md`; regras operacionais por combinação; lista de casos de teste representativos.

## Workshop 4 — Emissão

- **Objetivo:** entender o que precisa estar resolvido para emitir uma viagem, documentação legal/seguro e o checklist interno — inclusive sob pressão de prazo.
- **Participantes:** proprietário (Wefferson) e quem executa a emissão.
- **Casos reais a pedir:** `docs/business-cases/emissao-urgente.md`.
- **Perguntas de sondagem:**
  1. Existe um checklist de itens a conferir antes de emitir? O que tem nele?
  2. Quem, na equipe, tem autonomia para emitir?
  3. Quando o seguro viagem é obrigatório vs. opcional? Existe cobertura mínima exigida?
  4. Existem avisos/observações que devem constar em toda proposta, independentemente do caso?
  5. Existe alguma obrigação fiscal (nota fiscal, faturamento) a cumprir na emissão, especialmente em Finalidade = Corporativo?
- **Documentos atualizados ao final:** ver Protocolo pós-entrevista, com foco em `proposal-lifecycle.md` (etapas Aprovação, Pagamento, Emissão, Entrega dos documentos), `proposal-actions.md` (ação Converter em emissão), `business-rules.md` (grupo Legal: Seguros, Observações obrigatórias).
- **Decisões esperadas:** checklist oficial de emissão; regra de obrigatoriedade de seguro; lista de observações obrigatórias.

## Workshop 5 — Pós-venda

- **Objetivo:** entender o que acontece depois que o passageiro viaja, e se isso deveria ser rastreado pela plataforma.
- **Participantes:** proprietário (Wefferson).
- **Casos reais a pedir:** nenhum caso dedicado ainda em `docs/business-cases/` — ao conduzir este workshop, considerar se um caso de pós-venda/reclamação/indicação real merece virar arquivo novo na pasta.
- **Perguntas de sondagem:**
  1. Vocês fazem algum contato com o cliente depois que ele volta da viagem?
  2. Existe algum registro de satisfação, reclamação ou indicação gerada?
  3. Um cliente que já viajou com vocês recebe algum tratamento diferente numa próxima proposta?
  4. A 027 Viagens presta algum suporte ativo durante a viagem (emergência, reemissão)? Isso deveria gerar registro no histórico da proposta?
- **Documentos atualizados ao final:** ver Protocolo pós-entrevista, com foco em `proposal-lifecycle.md` (etapas Viagem, Pós-venda), `glossary.md` (ex: "Indicação", "Cliente recorrente").
- **Decisões esperadas:** se pós-venda entra no escopo da plataforma em uma sprint próxima ou fica para uma capacidade futura (ver `ARCHITECTURE.md`, capacidades de plataforma).

---

## Registro dos resultados

Cada workshop deve gerar atualizações nos documentos listados em sua própria seção, seguindo o Protocolo pós-entrevista — nunca ficar só na ata da conversa ou só no arquivo de caso. Uma pergunta só deve ser removida de um documento quando a resposta for registrada em outro — nunca simplesmente apagada.
