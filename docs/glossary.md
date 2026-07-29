# Glossário — Linguagem Ubíqua (DDD)

Este documento registra os **conceitos de domínio** da operação comercial da 027 Viagens, com uma definição única para cada termo. A partir daqui, todos os documentos, schemas, regras de negócio e código devem usar exatamente estes nomes e estes significados — é essa consistência que reduz ambiguidade entre negócio e tecnologia (Domain-Driven Design).

**Como este documento evolui:** cada termo abaixo nasce como rascunho, a partir do que já apareceu nos documentos existentes (`vision.md`, `ARCHITECTURE.md`, `business-rules.md`) ou do vocabulário natural do setor de turismo. Nenhum termo aqui está confirmado como definição oficial da 027 Viagens até ser validado no Workshop de Descoberta (`discovery-workshop.md`). Ao validar ou corrigir um termo, atualize a linha `Status`.

## Como usar

- Se um documento novo (ou um schema, no Sprint 1) precisar de um conceito que não está aqui, ele deve ser adicionado a este glossário **antes** de ser usado — não cunhar sinônimos.
- Se dois documentos usarem palavras diferentes para a mesma coisa (ex: "cotação" e "orçamento"), isso é um sinal de que o glossário precisa resolver a ambiguidade, não que os dois termos podem conviver.

## Conceitos centrais

| Termo | Definição (rascunho) | Status |
|---|---|---|
| **Lead** | Pessoa ou empresa que demonstrou interesse em uma viagem, antes de qualquer levantamento de necessidade. | Rascunho — confirmar se a 027 usa este termo ou outro (ex: "interessado", "contato") |
| **Cliente** | Pessoa ou empresa que efetivamente contrata uma viagem através da 027 Viagens. Pode ser o mesmo `Passageiro` ou não (ex: empresa contratando para funcionários). | Rascunho |
| **Passageiro** | Pessoa que efetivamente viaja, associada a uma `Proposta`/`Emissão`. Uma proposta pode ter um ou vários passageiros. | Rascunho |
| **Consultor** | Colaborador da 027 Viagens responsável por atender o `Cliente` e conduzir a `Proposta`. | Rascunho — confirmar se existe outro papel (ex: "vendedor", "agente") tratado como sinônimo ou como algo diferente |
| **Fornecedor** | Empresa parceira que efetivamente presta um serviço da viagem (companhia aérea, hotel, operadora, seguradora). | Rascunho — sem detalhamento; ver perguntas em `discovery-workshop.md` |
| **Cotação** | Levantamento de preços/disponibilidade de uma viagem junto a fornecedores, antes de virar uma `Proposta` formal para o cliente. | Rascunho — confirmar se "Cotação" e "Proposta" são etapas distintas ou o mesmo documento em estágios diferentes |
| **Proposta** | Documento comercial formal enviado ao `Cliente`, representando uma oferta de viagem com preço e condições — o objeto central da plataforma (ver `universal-proposal-model.md`). | Rascunho |
| **Tipo de Proposta** | Classificação de uma `Proposta` conforme a natureza da viagem (Nacional, Internacional, Corporativo, Religioso, Grupos, Disney, Cruzeiros, Individual, Incentivo, Outros — ver `proposal-types.md`). | Rascunho — lista inicial a validar |
| **Versão da Proposta** | Estado específico de uma `Proposta` num momento do tempo; uma proposta pode ter várias versões ao longo da negociação, sem perder o histórico (ver `proposal-versioning.md`). | Rascunho |
| **Status da Proposta** | Estado atual de uma `Proposta` dentro do seu ciclo de vida (ver `proposal-status.md`). | Rascunho |
| **Aprovação** | Momento em que o `Cliente` (ou, internamente, a 027 Viagens) confirma aceite de uma `Proposta`/`Versão`, avançando para pagamento. | Rascunho — confirmar se há aprovação interna (ex: alçada de desconto) além da aprovação do cliente |
| **Pagamento** | Confirmação financeira da `Proposta` aprovada, habilitando a `Emissão`. | Rascunho |
| **Emissão** | Ato de efetivamente reservar/confirmar os serviços junto aos `Fornecedores` a partir de uma `Proposta` paga, gerando os documentos finais de viagem (voucher, bilhetes, etc.). | Rascunho |
| **Módulo (de documento)** | Um tipo de documento comercial suportado pela plataforma (Propostas, Contratos, Vouchers, etc. — ver `ARCHITECTURE.md`). | Confirmado (arquitetura) |
| **Capacidade (de plataforma)** | Serviço da plataforma que consome o Modelo Universal de um ou mais módulos, sem ser ele próprio um tipo de documento (CRM, Notificações, IA Comercial, etc.). | Confirmado (arquitetura) |
| **Modelo Universal** | Objeto único e estruturado do qual todo gerador de um módulo depende exclusivamente (ver `ARCHITECTURE.md` e `universal-proposal-model.md`). | Confirmado (arquitetura) |

## Termos ainda sem definição — a resolver no Workshop de Descoberta

- Como a 027 Viagens chama, internamente, cada etapa entre "Lead" e "Emissão"? (os nomes acima são hipótese de mercado, não confirmados)
- Existe distinção formal entre "Cotação" e "Proposta", ou são tratadas como sinônimos na operação atual?
- "Consultor" é o termo usado internamente, ou há outro (ex: "agente de viagens", "vendedor")?
- Existe o conceito de "Reserva" como algo distinto de "Emissão"?
- Como a 027 Viagens se refere a uma viagem em grupo — "Grupo" é um `Tipo de Proposta` ou um atributo de qualquer tipo (ex: um grupo pode ser corporativo, religioso, etc. ao mesmo tempo)?

## Relação com outros documentos

- `docs/proposal-types.md`, `docs/proposal-lifecycle.md`, `docs/proposal-status.md`, `docs/proposal-actions.md`, `docs/proposal-versioning.md` e `docs/business-rules.md` devem usar exclusivamente os termos definidos aqui.
- `docs/discovery-workshop.md` é a ferramenta usada para confirmar, corrigir ou completar estes termos junto ao proprietário da 027 Viagens.
- Ao chegar no Sprint 1, `schemas/proposta.schema.json` deve nomear campos e objetos usando estes mesmos termos — nenhum nome técnico divergente do glossário (ex: não usar `traveler` no schema se o glossário define `Passageiro`).
