# Tipos de Proposta

Mapeamento dos tipos de `Proposta` (ver `glossary.md`) que a plataforma deverá suportar. Nenhum campo abaixo foi confirmado com o negócio — este documento registra **estrutura e perguntas**, não respostas. Onde uma descrição aparece, é apenas a definição genérica do termo no mercado de viagens, não uma regra da 027 Viagens.

A lista de tipos abaixo é o ponto de partida sugerido no planejamento do projeto — ela própria precisa ser validada: pode haver tipos que a 027 não usa, e tipos reais da operação que não estão nesta lista.

> **Pergunta geral (antes de tudo):** esta lista de 10 tipos corresponde a como a 027 Viagens realmente classifica suas propostas hoje? Existe algum tipo usado na prática que não está aqui? Algum destes nunca é usado?

---

## Nacional

- **Descrição:** viagem com destino dentro do território brasileiro.
- **Objetivo:** *a confirmar — o que diferencia comercialmente uma proposta nacional de uma internacional, além do destino?*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - Existe alguma documentação/aviso obrigatório específico para viagem nacional (ex: documento de identidade para menores)?
  - Câmbio/moeda nunca é relevante aqui, correto?
  - Uma viagem nacional pode ter as mesmas particularidades de "Grupos", "Corporativo" etc. simultaneamente? (ver pergunta de sobreposição de tipos, no final deste documento)

## Internacional

- **Descrição:** viagem com destino fora do Brasil.
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar — hipótese de mercado: passaporte, visto, validade mínima de documento, mas precisa ser confirmado como regra real da 027.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - Quais documentos são sempre exigidos/mencionados (passaporte, visto, vacinas)? Varia por destino?
  - Seguro viagem é obrigatório para este tipo? (ver `business-rules.md`, seção Seguros)
  - Como o câmbio/moeda de cobrança é tratado — sempre em reais, ou pode ser cotado na moeda do destino?
  - Existe uma checklist específica de documentação internacional hoje (mesmo que informal)?

## Corporativo

- **Descrição:** viagem contratada por uma empresa (pessoa jurídica), tipicamente para funcionários ou convidados.
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar — hipótese: dados da empresa contratante, centro de custo, política de viagem corporativa.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - `Cliente` (quem contrata/paga) e `Passageiro` (quem viaja) são sempre diferentes aqui? Como isso é tratado hoje?
  - Existe faturamento/nota fiscal com regras próprias para corporativo?
  - Existem condições de pagamento diferenciadas (prazo maior, faturado)?
  - Existe um consultor/atendimento dedicado a contas corporativas?

## Religioso

- **Descrição:** viagem organizada em torno de um roteiro ou motivação religiosa (ex: peregrinação, encontro de grupo religioso).
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - Este tipo está sempre associado a "Grupos", ou pode ser uma viagem individual/religiosa?
  - Existem parcerias fixas (roteiros fechados, lideranças religiosas, operadoras específicas) que deveriam aparecer na proposta?
  - Existe um formato de proposta diferente (ex: foco em roteiro espiritual, menos em "venda") para este tipo?

## Grupos

- **Descrição:** viagem vendida para múltiplos passageiros como um pacote único.
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar — hipótese: número mínimo/máximo de participantes, lista de passageiros, responsável pelo grupo.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - A partir de quantos passageiros uma proposta passa a ser tratada como "Grupo"? (ver `business-rules.md`, seção Grupos)
  - "Grupos" é um tipo independente ou um atributo que pode se combinar com Nacional/Internacional/Religioso/Corporativo? (ver pergunta de sobreposição, no final)
  - Existe um responsável único pelo grupo (quem assina/aprova) mesmo havendo vários passageiros?
  - Existe desconto ou condição comercial padrão por volume?

## Disney

- **Descrição:** viagem com destino/roteiro centrado nos parques Disney (tipicamente Orlando).
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar — hipótese: ingressos de parque, datas de parque específicas, hospedagem dentro/fora do complexo.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - Por que "Disney" é um tipo à parte e não apenas uma viagem Internacional de lazer? Há particularidade comercial suficiente (parceria, comissionamento, pacote fixo) para justificar isso?
  - Existem parceiros/operadoras fixas para esse tipo?
  - Existe um roteiro/checklist padrão (ingressos, datas de parque, transfer) específico?

## Cruzeiros

- **Descrição:** viagem realizada a bordo de um navio de cruzeiro.
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar — hipótese: cabine (em vez de quarto), companhia marítima, portos de embarque/desembarque, escalas.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar — hipótese: "hospedagem" vira "cabine", pode não haver "voos" se o embarque for nacional.*
- **Dúvidas para o negócio:**
  - O Modelo Universal da Proposta (`universal-proposal-model.md`) tem uma seção `hospedagem`; para cruzeiro, isso deveria virar/incluir uma seção de cabine, ou hospedagem serve para ambos com campos diferentes?
  - Existem regras comerciais específicas de cruzeiro (política de cancelamento costuma ser diferente de hotel/aéreo)?

## Individual

- **Descrição:** viagem vendida para um único passageiro ou uma única família/grupo pequeno, sem as características de "Grupos".
- **Objetivo:** *a confirmar — talvez este seja o "tipo padrão" e os demais sejam exceções a ele; precisa confirmar com o negócio.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar.*
- **Dúvidas para o negócio:**
  - "Individual" é realmente um tipo distinto, ou é a ausência dos demais tipos (ou seja, todo tipo tem "Individual" como padrão até que outro se aplique)?

## Incentivo

- **Descrição:** viagem oferecida por uma empresa como prêmio/incentivo a funcionários, parceiros ou clientes (viagem de incentivo corporativo).
- **Objetivo:** *a confirmar.*
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** *a confirmar — como se diferencia de "Corporativo"?*
- **Dúvidas para o negócio:**
  - "Incentivo" e "Corporativo" são tipos diferentes ou "Incentivo" é um subtipo de "Corporativo"?
  - Quem é o `Cliente` neste caso — a empresa que oferece o prêmio, ou o passageiro premiado?
  - Existe um formato de proposta diferenciado (ex: sem preço visível ao passageiro final)?

## Outros

- **Descrição:** categoria residual para propostas que não se encaixam nos tipos acima.
- **Objetivo:** evitar que a plataforma trave diante de um tipo de viagem não previsto.
- **Características:** *a confirmar.*
- **Informações obrigatórias:** *a confirmar.*
- **Informações opcionais:** *a confirmar.*
- **Diferenças em relação aos demais tipos:** por definição, não segue nenhuma regra específica dos demais tipos.
- **Dúvidas para o negócio:**
  - Com que frequência a operação real cai em "Outros"? Se for frequente, é sinal de que falta um tipo nesta lista.
  - Deve haver uma revisão periódica de propostas marcadas como "Outros" para identificar novos tipos a formalizar?

---

## Pergunta estrutural (afeta o Modelo Universal)

Vários tipos acima parecem **combináveis** entre si (ex: um grupo religioso internacional; uma viagem corporativa de incentivo nacional) em vez de mutuamente exclusivos.

> **Pergunta para o negócio:** `Tipo de Proposta` deve ser um valor único por proposta (ex: só "Grupos") ou a proposta pode ter múltiplas classificações simultâneas (ex: "Grupos" + "Internacional" + "Religioso")? Esta resposta muda diretamente como o campo correspondente será modelado em `schemas/proposta.schema.json` no Sprint 1 — **não deve ser decidida sem essa confirmação.**
