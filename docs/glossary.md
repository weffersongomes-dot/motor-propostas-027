# Glossário — Linguagem Ubíqua (Ubiquitous Language)

Este documento é a **referência oficial da linguagem do domínio** da plataforma (Domain-Driven Design). Todo documento, prompt, schema, código, banco de dados e interface deve usar exatamente os termos definidos aqui — com o mesmo nome e o mesmo significado. Não cunhar sinônimo novo para um conceito já registrado; se um termo parecer insuficiente, corrigir a definição aqui, não criar um termo paralelo.

**Como este documento evolui:** cada termo nasce como rascunho, a partir do que já apareceu nos documentos existentes (`vision.md`, `ARCHITECTURE.md`, `business-rules.md`, `domain-map.md`, `proposal-types.md`) ou do vocabulário natural do setor de turismo. Nenhum termo está confirmado como definição oficial da 027 Viagens até ser validado nos Workshops de Descoberta (`discovery-workshop.md`). Ao validar ou corrigir um termo, atualizar o campo `Status`.

## Estrutura de cada termo

Cada termo é documentado com:

- **Definição oficial** — o que o termo significa, sem ambiguidade.
- **Contexto de uso** — onde/quando o termo se aplica (em qual etapa do ciclo de vida, em qual módulo).
- **Sinônimos aceitos** — palavras que podem ser usadas informalmente com o mesmo significado (quando existirem confirmadamente; a maioria ainda não tem sinônimo confirmado).
- **Termos que não devem ser usados** — palavras que poderiam parecer sinônimos mas devem ser evitadas, para não gerar ambiguidade.
- **Impacto no código e na documentação** — em quais schemas/objetos/documentos este termo deve aparecer literalmente.
- **Status** — Rascunho (hipótese a validar) ou Confirmado (validado com o negócio ou já decidido na arquitetura).

---

### Lead

- **Definição oficial:** pessoa ou empresa que demonstrou interesse em uma viagem, antes de qualquer levantamento de necessidade.
- **Contexto de uso:** primeira etapa do ciclo de vida da proposta (`proposal-lifecycle.md`).
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "interessado", "contato" — até confirmar se a 027 usa um termo próprio.
- **Impacto no código e na documentação:** deve nomear a entidade de origem da `Proposta`, se vier a existir como objeto próprio no domínio (a confirmar na Sprint 1A se Lead vira uma entidade ou é apenas um estado inicial de Cliente).
- **Status:** Rascunho.

### Qualificação

- **Definição oficial:** avaliação de um Lead para decidir se há potencial real de venda antes de seguir para atendimento completo.
- **Contexto de uso:** etapa do ciclo de vida entre Lead e Primeiro contato (`proposal-lifecycle.md`).
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "triagem" (pode ser sinônimo, mas ainda não confirmado como termo real da 027).
- **Impacto no código e na documentação:** pode virar um `status` inicial do Lead, não necessariamente uma entidade própria — decisão da Sprint 1A/1B.
- **Status:** Rascunho.

### Cliente

- **Definição oficial:** pessoa ou empresa que efetivamente contrata uma viagem através da 027 Viagens. Pode ou não coincidir com o(s) `Passageiro(s)`.
- **Contexto de uso:** presente em toda `Proposta`, desde o Levantamento das necessidades.
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "comprador", "contratante" — evitar até confirmar se algum é o termo real usado internamente.
- **Impacto no código e na documentação:** seção `cliente` do Modelo Universal (`universal-proposal-model.md`); entidade própria no `domain-map.md`.
- **Status:** Rascunho.

### Passageiro

- **Definição oficial:** pessoa que efetivamente viaja, associada a uma `Viagem`/`Proposta`. Uma proposta pode ter um ou vários passageiros.
- **Contexto de uso:** seção `passageiros` do Modelo Universal; relevante especialmente quando Finalidade = Corporativo/Incentivo ou Formato = Grupo (`proposal-types.md`), onde Cliente e Passageiro divergem.
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "viajante", "hóspede" — evitar até confirmar.
- **Impacto no código e na documentação:** seção `passageiros` do Modelo Universal; entidade própria no `domain-map.md`.
- **Status:** Rascunho.

### Consultor

- **Definição oficial:** colaborador da 027 Viagens responsável por atender o `Cliente` e conduzir a `Proposta`.
- **Contexto de uso:** presente do Primeiro contato até o Pós-venda; referenciado na `metadata` de toda proposta/documento.
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "vendedor", "agente" — evitar até confirmar se a 027 diferencia esses papéis do Consultor.
- **Impacto no código e na documentação:** seção `consultor` e campo `metadata.consultor` do Modelo Universal.
- **Status:** Rascunho.

### Fornecedor

- **Definição oficial:** empresa parceira que efetivamente presta um serviço concreto da viagem (companhia aérea, hotel, operadora, seguradora).
- **Contexto de uso:** associado a `Voo`, `Hospedagem` e `Serviço` dentro de uma `Viagem` (ver `domain-map.md`).
- **Sinônimos aceitos:** "parceiro" (usado de forma mais ampla em `content/diferenciais/`, mas como conceito de domínio o termo oficial é Fornecedor).
- **Termos que não devem ser usados:** "operadora" como sinônimo genérico de Fornecedor — operadora é *um tipo* de Fornecedor, não o termo geral.
- **Impacto no código e na documentação:** entidade própria no `domain-map.md`; ainda sem seção dedicada confirmada no Modelo Universal (a decidir na Sprint 1A se Fornecedor é uma entidade referenciada ou um texto livre dentro de Voo/Hospedagem/Serviço).
- **Status:** Rascunho.

### Cotação

- **Definição oficial:** levantamento de preços/disponibilidade de uma viagem junto a `Fornecedores`, antes de virar uma `Proposta` formal para o cliente.
- **Contexto de uso:** etapa do ciclo de vida entre Levantamento das necessidades e Proposta (`proposal-lifecycle.md`).
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "orçamento" — evitar até confirmar se é tratado como sinônimo ou como algo diferente na operação real.
- **Impacto no código e na documentação:** pode ou não virar uma entidade própria distinta de `Proposta` — depende da resposta ao Workshop 3 (Operação) sobre se Cotação e Proposta são etapas ou documentos distintos.
- **Status:** Rascunho.

### Proposta

- **Definição oficial:** documento comercial formal enviado ao `Cliente`, representando uma oferta de viagem com preço e condições — o objeto central da plataforma.
- **Contexto de uso:** todo o ciclo de vida (`proposal-lifecycle.md`); todo o Modelo Universal (`universal-proposal-model.md`) descreve uma Proposta.
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "orçamento", "cotação" como sinônimo de Proposta — ver distinção em Cotação, acima.
- **Impacto no código e na documentação:** entidade central em `src/models/` (Sprint 1A) e `schemas/proposta.schema.json` (Sprint 1B); nome de módulo em `ARCHITECTURE.md` ("Motor de Propostas").
- **Status:** Confirmado (é o termo definidor do projeto).

### Destino, Formato, Finalidade, Produto

- **Definição oficial:** as quatro dimensões independentes que classificam uma `Proposta` (ver `proposal-types.md`) — Destino (Nacional/Internacional), Formato (Individual/Grupo), Finalidade (Lazer/Corporativo/Religioso/Incentivo) e Produto (Pacote/Cruzeiro/Disney/Hotel/Aéreo/Personalizado/Outros).
- **Contexto de uso:** classificação da Proposta, usada para selecionar regras de negócio (`business-rules.md`) e textos (`content/`) aplicáveis.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** "Tipo de Proposta" como termo único — foi substituído por estas quatro dimensões combináveis (ver [ADR 0005](decisoes/0005-refinamento-pre-sprint-1a.md)); não usar "categoria" como sinônimo genérico de qualquer uma delas.
- **Impacto no código e na documentação:** cada uma deve aparecer como um atributo próprio (possivelmente multivalorado) do objeto `Proposta`, não como um único campo "tipo".
- **Status:** Confirmado como estrutura (as quatro dimensões); valores dentro de cada dimensão seguem Rascunho.

### Versão (da Proposta)

- **Definição oficial:** um estado específico e imutável de uma `Proposta` num momento do tempo; uma proposta pode ter várias versões ao longo da negociação, sem perder o histórico.
- **Contexto de uso:** toda vez que a oferta ou preço de uma proposta muda (ver `proposal-versioning.md`).
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** "revisão", "rascunho" (ambíguo com o status `Rascunho` da própria proposta).
- **Impacto no código e na documentação:** todo `Documento` gerado referencia uma Versão específica, nunca "a Proposta" genericamente.
- **Status:** Confirmado (estrutura); critério de quando gerar nova versão segue Rascunho.

### Status (da Proposta)

- **Definição oficial:** estado atual de uma `Proposta` dentro do seu ciclo de vida (ver `proposal-status.md`).
- **Contexto de uso:** todo o ciclo de vida; é um atributo da versão mais recente de uma proposta.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** "situação" como sinônimo informal — usar sempre "status".
- **Impacto no código e na documentação:** campo `metadata.status` do Modelo Universal; valores ainda em rascunho em `proposal-status.md`.
- **Status:** Rascunho (valores possíveis ainda não confirmados).

### Aprovação

- **Definição oficial:** momento em que o `Cliente` (ou, internamente, a 027 Viagens) confirma aceite de uma `Proposta`/`Versão`, avançando para pagamento.
- **Contexto de uso:** etapa do ciclo de vida entre Negociação/Ajustes e Pagamento.
- **Sinônimos aceitos:** nenhum confirmado.
- **Termos que não devem ser usados:** "confirmação" como sinônimo — reservar "confirmação" para o contexto de `Emissão`/`Fornecedor`, não de aceite do cliente.
- **Impacto no código e na documentação:** ação `Aprovar` em `proposal-actions.md`; status `Aprovada` em `proposal-status.md`.
- **Status:** Rascunho.

### Pagamento

- **Definição oficial:** confirmação financeira da `Proposta` aprovada, habilitando a `Emissão`.
- **Contexto de uso:** etapa do ciclo de vida entre Aprovação e Emissão.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** —
- **Impacto no código e na documentação:** seção `financeiro` do Modelo Universal; status `Paga`/`Aguardando pagamento` em `proposal-status.md`.
- **Status:** Rascunho.

### Emissão

- **Definição oficial:** ato de efetivamente reservar/confirmar os serviços junto aos `Fornecedores` a partir de uma `Proposta` paga, gerando os documentos finais de viagem (voucher, bilhetes, etc.).
- **Contexto de uso:** etapa do ciclo de vida após Pagamento; ação `Converter em emissão` (`proposal-actions.md`).
- **Sinônimos aceitos:** "reserva" — a confirmar se a 027 distingue "Reserva" de "Emissão" como conceitos diferentes (ver pergunta em aberto abaixo).
- **Termos que não devem ser usados:** não usar "Emissão" para descrever a geração de um documento (HTML/PDF/e-mail) — isso é `Documento`/"gerar", não Emissão.
- **Impacto no código e na documentação:** módulo futuro "Confirmações de Reserva" (`ARCHITECTURE.md`); status `Emitida` em `proposal-status.md`.
- **Status:** Rascunho.

### Documento

- **Definição oficial:** qualquer artefato gerado a partir de uma `Versão` da Proposta (HTML, PDF, WhatsApp, e-mail — ver `ARCHITECTURE.md`).
- **Contexto de uso:** saída dos geradores (`src/generators/`), sempre referenciando uma Versão específica.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** não confundir com "Módulo de documento" (que é um *tipo* de documento como um todo, ex: Propostas, Contratos — ver `ARCHITECTURE.md`); "Documento" no singular é sempre um artefato concreto.
- **Impacto no código e na documentação:** seção `anexos`/geradores do Modelo Universal; termo usado em `universal-proposal-model.md` e `ARCHITECTURE.md`.
- **Status:** Confirmado (arquitetura).

### Empresa

- **Definição oficial:** representa a 027 Viagens em si — dados institucionais (CNPJ, contatos, logo) que aparecem em todo documento emitido.
- **Contexto de uso:** seção `empresa` do Modelo Universal; espelha `config/empresa.json`.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** não usar "Empresa" para se referir ao cliente pessoa jurídica — nesse caso o termo é `Cliente` (corporativo), nunca `Empresa`, que é reservado à 027 Viagens.
- **Impacto no código e na documentação:** seção `empresa` do Modelo Universal; `config/empresa.json`.
- **Status:** Confirmado (arquitetura).

### Viagem

- **Definição oficial:** o conjunto de destino, datas e serviços (`Voo`, `Hospedagem`, `Serviço`) que uma `Proposta` descreve.
- **Contexto de uso:** seção `viagem` do Modelo Universal; associada a `Passageiro(s)`.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** não usar "roteiro" como sinônimo exato — roteiro é o detalhamento textual/dia-a-dia da Viagem, não a entidade em si.
- **Impacto no código e na documentação:** seção `viagem` do Modelo Universal; entidade em `domain-map.md`.
- **Status:** Confirmado (arquitetura).

### Voo, Hospedagem, Serviço

- **Definição oficial:** componentes concretos de uma `Viagem`, cada um fornecido por um `Fornecedor`. Serviço cobre o que não é Voo nem Hospedagem (traslado, passeio, seguro, aluguel de carro).
- **Contexto de uso:** seções próprias do Modelo Universal (`voos`, `hospedagem`, `serviços`).
- **Sinônimos aceitos:** para Produto = Cruzeiro, "Hospedagem" pode precisar de um sinônimo/variação "Cabine" — a confirmar (ver `proposal-types.md`, dimensão Produto).
- **Termos que não devem ser usados:** —
- **Impacto no código e na documentação:** seções `voos`, `hospedagem`, `serviços` do Modelo Universal.
- **Status:** Confirmado (arquitetura), exceto a variação para Cruzeiro (Rascunho).

### Financeiro

- **Definição oficial:** os valores, forma de pagamento e parcelamento associados a uma `Proposta`.
- **Contexto de uso:** seção `financeiro` do Modelo Universal; calculado a partir das Regras Financeiras (`business-rules.md`).
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** —
- **Impacto no código e na documentação:** seção `financeiro` do Modelo Universal.
- **Status:** Confirmado (arquitetura).

### Metadata

- **Definição oficial:** dados de rastreabilidade presentes em toda `Proposta`/`Documento`, existindo mesmo quando não exibidos ao cliente (`proposal_id`, `schema_version`, `engine_version`, `template`, `generated_at`, `generated_by`, `consultor`, `origem`, `status`).
- **Contexto de uso:** bloco obrigatório de todo Modelo Universal (ver `universal-proposal-model.md`).
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** —
- **Impacto no código e na documentação:** bloco `metadata` do Modelo Universal, replicado em todo módulo futuro.
- **Status:** Confirmado (arquitetura).

### Módulo (de documento)

- **Definição oficial:** um tipo de documento comercial suportado pela plataforma (Propostas, Contratos, Vouchers, etc. — ver `ARCHITECTURE.md`).
- **Contexto de uso:** organização de `templates/`, `output/` e `src/generators/`.
- **Sinônimos aceitos:** "Motor de [Módulo]" (ex: "Motor de Propostas") é o nome de produto do módulo.
- **Termos que não devem ser usados:** não confundir com `Documento` (artefato concreto) nem com `Capacidade` (serviço de plataforma).
- **Impacto no código e na documentação:** estrutura de pastas em `ARCHITECTURE.md`.
- **Status:** Confirmado (arquitetura).

### Capacidade (de plataforma)

- **Definição oficial:** serviço da plataforma que consome o Modelo Universal de um ou mais módulos, sem ser ele próprio um tipo de documento (CRM, Notificações, IA Comercial, etc.).
- **Contexto de uso:** ver `ARCHITECTURE.md`, seção Módulos e capacidades.
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** não chamar uma Capacidade de "Módulo" — a distinção existe justamente para não tratá-las como mais um tipo de documento.
- **Impacto no código e na documentação:** seção 2 de `ARCHITECTURE.md`.
- **Status:** Confirmado (arquitetura).

### Modelo Universal

- **Definição oficial:** objeto único e estruturado do qual todo gerador de um módulo depende exclusivamente; para o módulo de Propostas, é o Modelo Universal da Proposta (`universal-proposal-model.md`).
- **Contexto de uso:** centro do fluxo de dados obrigatório (`ARCHITECTURE.md`, seção 3).
- **Sinônimos aceitos:** nenhum.
- **Termos que não devem ser usados:** —
- **Impacto no código e na documentação:** todo schema/objeto de domínio deve ser rastreável a uma seção do Modelo Universal correspondente.
- **Status:** Confirmado (arquitetura).

---

## Termos ainda sem definição — a resolver nos Workshops de Descoberta

- Como a 027 Viagens chama, internamente, cada etapa entre "Lead" e "Emissão"? (os nomes usados são hipótese de mercado, não confirmados)
- Existe distinção formal entre "Cotação" e "Proposta", ou são tratadas como sinônimos na operação atual?
- "Consultor" é o termo usado internamente, ou há outro (ex: "agente de viagens", "vendedor")?
- Existe o conceito de "Reserva" como algo distinto de "Emissão"?
- "Fornecedor" é cadastrado/reaproveitado entre propostas, ou cada cotação trata fornecedores de forma isolada (texto livre)?

## Relação com outros documentos

- `docs/domain-map.md`, `docs/proposal-types.md`, `docs/proposal-lifecycle.md`, `docs/proposal-status.md`, `docs/proposal-actions.md`, `docs/proposal-versioning.md` e `docs/business-rules.md` devem usar exclusivamente os termos definidos aqui.
- `docs/discovery-workshop.md` é a ferramenta usada para confirmar, corrigir ou completar estes termos junto ao proprietário da 027 Viagens.
- A partir da Sprint 1A, `src/models/` deve nomear objetos de domínio exatamente como aqui; a partir da Sprint 1B, `schemas/proposta.schema.json` deve nomear campos da mesma forma — nenhum nome técnico divergente do glossário (ex: não usar `traveler` no schema se o glossário define `Passageiro`).
