# Domain Decisions

Registra decisões de modelagem de domínio que não justificam uma ADR própria (mudanças arquiteturais menores, granulares, específicas de uma Entidade/Value Object) — para decisões maiores, ver `docs/decisoes/`. Cada entrada segue: contexto, decisão, justificativa, impacto, data.

---

## Proposal referencia Trip/Customer via ProposalVersion, não diretamente

- **Contexto:** o briefing da Sprint 1B listava invariantes como "Proposal sempre possui um Customer" e "sempre possui uma Trip" assumindo que `Proposal` teria referências diretas a eles.
- **Decisão:** essas invariantes são garantidas em `ProposalVersion` (que carrega `customer_id`/`trip_id`), não em `Proposal` (que permanece deliberadamente magra — só `id`, `status` e `versions`, ver ADR 0006 e ADR 0007).
- **Justificativa:** `Proposal` é um Aggregate de Coordenação (ADR 0007); todo conteúdo real de uma proposta pertence a uma versão específica (snapshot), consistente com `docs/proposal-versioning.md`. Exigir `customer_id` em `Proposal` duplicaria a referência já presente em cada versão e criaria a pergunta "e se a versão 2 tiver um cliente diferente da versão 1?" sem necessidade.
- **Impacto:** `Proposal.__post_init__` não valida cliente/viagem; `ProposalVersion.__post_init__` sim. Qualquer leitura de "quem é o cliente desta proposta" deve passar pela versão corrente, não pela Proposal.
- **Data:** 2026-07-30.

## Trip não exige pertencer a uma Proposal

- **Contexto:** o briefing sugeria "Trip sempre pertence a uma Proposal" como invariante hipotética.
- **Decisão:** não implementada. `Trip` continua sendo um Aggregate Root independente, referenciado por `ProposalVersion.trip_id`, nunca o contrário.
- **Justificativa:** já decidido na ADR 0006 — uma Viagem continua existindo (o passageiro efetivamente viaja) depois que o ciclo comercial da Proposta termina; módulos futuros de Operações (Emissão, Itinerário) precisam poder referenciar a Trip sem depender da Proposal de origem. Inverter isso agora contradiria essa decisão já registrada.
- **Impacto:** nenhuma validação cruzada entre `Trip` e `Proposal`/`ProposalVersion` existe ou deve existir no domínio nesta sprint.
- **Data:** 2026-07-30.

## Passenger pertence ao Customer; Trip referencia Passenger por id

- **Contexto:** o briefing listava "Trip sempre possui ao menos um Passageiro" como invariante, mas na Sprint 1A `Passenger` só existia como filho de `Customer` — `Trip` não tinha nenhum campo de passageiros.
- **Decisão:** `Passenger` continua pertencendo ao Aggregate `Customer` (seu cadastro/roster). `Trip` ganhou um novo campo `passenger_ids: List[Identifier]` — quais passageiros (já cadastrados em algum Customer) efetivamente viajam nesta Trip específica — e a invariante "ao menos um passageiro" foi implementada sobre esse campo.
- **Justificativa:** um Customer pode ter vários Passageiros cadastrados (família, funcionários de uma empresa) sem que todos viajem em toda Trip — a lista de quem viaja é, portanto, uma característica da Trip, não do Customer; mas a *posse* (quem cadastrou/mantém os dados do passageiro) continua sendo do Customer, evitando duplicar a entidade Passenger em dois Aggregates.
- **Impacto:** `Trip.passenger_ids` é campo novo (não existia na Sprint 1A) — muda a assinatura de construção de `Trip`. `examples/` foi atualizado.
- **Data:** 2026-07-30.

## CountryCode e LanguageCode: Value Object com validação de formato, não Enum fechado

- **Contexto:** o briefing listava `CountryCode` e `Language` entre os "enums estruturais" esperados.
- **Decisão:** implementados como Value Objects (`CountryCode`, `LanguageCode`) validados por formato (ISO 3166-1 alpha-2 / ISO 639-1), não como `Enum` Python com todos os valores possíveis.
- **Justificativa:** país e idioma são listas de referência grandes (~190 e ~180 valores) e mutáveis — um Enum fechado exigiria alterar código para adicionar um país, o que não é uma regra de negócio, é dado de referência. `Currency`, por comparação, ficou como Enum fechado porque uma agência de viagens lida na prática com um conjunto pequeno e estável de moedas.
- **Impacto:** `Address.country` usa `CountryCode`. `LanguageCode` foi criado mas **não está em uso** em nenhuma Entidade ainda — preparado para quando um campo de idioma preferido for necessário (ex: Notification Engine, Customer Portal).
- **Data:** 2026-07-30.

## Metadata.status permanece texto livre; ProposalVersion.status é o novo estado tipado

- **Contexto:** a Sprint 1A já tinha `Metadata.status: str` (herdado de `docs/universal-proposal-model.md`). A Sprint 1B pede um "Estado do Modelo" tipado para `ProposalVersion` (Draft/Active/Archived).
- **Decisão:** `Metadata.status` continua `str`, sem mudança de tipo. `ProposalVersion` ganhou um campo novo e independente, `status: ProposalVersionStatus` (enum), que é a fonte de verdade estrutural do estado da versão.
- **Justificativa:** tipar `Metadata.status` como `ProposalVersionStatus` acoplaria o Shared Kernel ao vocabulário do módulo Propostas — exatamente o tipo de contaminação que a revisão do Shared Kernel desta sprint (item 9 do briefing) deveria evitar (um módulo futuro de Contratos teria estados diferentes de Draft/Active/Archived). Manter os dois campos, com papéis diferentes e documentados, evita a escolha pior (contaminar o VO compartilhado) sem recriar o problema original da Sprint 1A (duas fontes de verdade) — porque agora estão claramente distintos: `ProposalVersion.status` é estrutural/tipado; `metadata.status` é um rótulo genérico de rastreamento, cuja sincronização com o status estrutural é responsabilidade de uma camada de aplicação futura, não do domínio.
- **Impacto:** `ProposalVersion` tem um campo a mais desde esta sprint. Documentação (`ARCHITECTURE.md`, `universal-proposal-model.md`) deve deixar clara a distinção para não confundir os dois "status".
- **Data:** 2026-07-30.

## Metadata.proposal_id renomeado para subject_id

- **Contexto:** revisão do Shared Kernel (item 9 do briefing) — `Metadata`, um Value Object pensado para ser reutilizado por todos os módulos futuros, tinha um campo chamado `proposal_id`.
- **Decisão:** renomeado para `subject_id`.
- **Justificativa:** um nome de campo específico do módulo Propostas dentro de um VO genérico é exatamente o tipo de vazamento que a revisão deveria encontrar e corrigir (ver critério explícito do briefing: "caso algum objeto pertença claramente a um contexto específico, removê-lo do Shared Kernel" — aqui o objeto inteiro continua compartilhado, mas um *campo* seu não deveria ter nome específico de contexto).
- **Impacto:** `docs/universal-proposal-model.md` foi atualizado para refletir o novo nome. Qualquer código futuro que use Metadata deve usar `subject_id`, não `proposal_id`.
- **Data:** 2026-07-30.

## ProposalClassification mantém quatro campos explícitos, não um dicionário por ProposalDimension

- **Contexto:** a Sprint 1B introduziu `ProposalDimension` (enum nomeando Destino/Formato/Finalidade/Produto). Era possível refatorar `ProposalClassification` para `Dict[ProposalDimension, Tuple[str, ...]]`.
- **Decisão:** mantidos os quatro campos explícitos (`destinations`, `formats`, `purposes`, `products`) da Sprint 1A.
- **Justificativa:** existem exatamente quatro dimensões, fixas e já confirmadas (ADR 0005) — um dicionário genérico só compensaria se o número de dimensões fosse variável ou desconhecido, o que não é o caso. Campos explícitos são mais legíveis, mais seguros em tipo (erros de chave errada viram erro em tempo de execução com dict, erro estático com atributo) e mais simples de validar individualmente.
- **Impacto:** `ProposalDimension` existe como tipo nomeado (documentação/uso futuro em código de aplicação que precise iterar dimensões genericamente), mas não é usado como chave dentro de `ProposalClassification`.
- **Data:** 2026-07-30.

## Financial.payment_method e Supplier vs. Financial: o que virou enum e o que não virou

- **Contexto:** tanto `payment_method` (Financial) quanto `category` (Supplier) eram texto livre na Sprint 1A, ambos com comentário "vira enum na Sprint 1B".
- **Decisão:** `Supplier.category` virou enum (`SupplierCategory`). `Financial.payment_method` **não** virou enum — continua texto livre.
- **Justificativa:** categorias de fornecedor (companhia aérea, hotel, operadora, seguradora) são um fato estrutural do setor de turismo, o mesmo em qualquer agência — não dependem de decisão comercial da 027. Formas de pagamento aceitas são, ao contrário, uma Regra Comercial explícita e ainda 100% pendente em `docs/business-rules.md` ("Regras de pagamento") — transformar isso em enum antes da confirmação do negócio inverteria a ordem de implementação exigida por esta sprint (Regras Comerciais são a última etapa, "somente quando existirem oficialmente").
- **Impacto:** nenhuma mudança de tipo em `Financial.payment_method`. Fica registrado como pendência explícita para quando `business-rules.md` (grupo Financeiro) for preenchido.
- **Data:** 2026-07-30.

## Código em inglês, Linguagem Ubíqua em português: mapeamento 1:1, não identidade literal

- **Contexto:** `docs/glossary.md` define a Linguagem Ubíqua em português (Proposta, Cliente, Passageiro...), refletindo o vocabulário real do negócio da 027 Viagens. O código (`src/domain/`), desde a Sprint 1A, usa identificadores em inglês (`Proposal`, `Customer`, `Passenger`...) — convenção seguida também pelos próprios exemplos de entidade dados nos briefings das Sprints 1A e 1B. A diretriz desta sprint pede "Linguagem Ubíqua, utilizando exclusivamente os termos definidos em `docs/glossary.md`" — o que, lido ao pé da letra, tensiona com nomes de classe em inglês.
- **Decisão:** manter identificadores de código em inglês (idiomático para Python, consistente com os exemplos explícitos do briefing), com **mapeamento 1:1 documentado** para o termo em português do glossário no docstring de cada Entidade/VO (ex: `Passenger` = `Passageiro`, `Trip` = `Viagem`). "Exclusividade" da Linguagem Ubíqua é satisfeita no nível conceitual — um único significado canônico por conceito, nunca dois nomes diferentes para a mesma coisa — não como identidade literal de string entre código e glossário.
- **Justificativa:** forçar nomes de classe em português criaria fricção real (bibliotecas, convenções, ferramentas do ecossistema Python assumem inglês) sem ganho correspondente — o que a Linguagem Ubíqua realmente previne é *ambiguidade de significado* entre negócio e código, não a escolha de idioma dos identificadores. O risco genuíno (código e negócio usando termos diferentes *para conceitos diferentes*, ou pior, o mesmo termo para coisas diferentes) é mitigado pelo mapeamento explícito e documentado, não pela tradução literal.
- **Impacto:** todo docstring de Entidade/VO em `src/domain/` deve citar o termo correspondente do glossário (já feito desde a Sprint 1A/1B). Nenhum nome de classe deve divergir conceitualmente do termo mapeado — isso sim seria uma violação real da Linguagem Ubíqua.
- **Data:** 2026-07-30.

## Passenger ganhou passenger_type; nenhuma checagem cruzada com birth_date

- **Contexto:** `PassengerType` (Adulto/Criança/Bebê) foi adicionado como enum estrutural.
- **Decisão:** `Passenger.passenger_type` é um campo obrigatório novo, mas nenhuma validação cruza `passenger_type` com `birth_date` (ex: impedir alguém de 40 anos marcado como Bebê).
- **Justificativa:** essa checagem cruzaria dois campos estruturais para aplicar o que seria, na prática, uma regra de negócio (que faixa etária corresponde a qual categoria) — decisão que depende de definição comercial/operacional da 027, não de estrutura.
- **Impacto:** os dois campos podem, hoje, ficar estruturalmente inconsistentes entre si sem erro — aceitável para esta sprint, a ser resolvido quando a regra existir.
- **Data:** 2026-07-30.
