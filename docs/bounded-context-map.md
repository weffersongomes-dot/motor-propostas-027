# Mapa de Bounded Contexts

Identifica os principais Bounded Contexts (DDD) da Plataforma de Documentos Comerciais da 027 Viagens — fronteiras de significado e responsabilidade, não apenas pastas de código. Um Bounded Context é onde um termo da Linguagem Ubíqua (`docs/glossary.md`) tem um único significado consistente; fora dele, o mesmo termo pode significar algo diferente ou nem existir.

> **Nota importante:** os quatro Bounded Contexts abaixo (nível de negócio) **não são 1:1** com as pastas técnicas de `src/domain/` (nível de código: `company/`, `customer/`, `supplier/`, `trip/`, `financial/`, `proposal/`, `shared/`). Isso é esperado nesta fase: as pastas técnicas são organizadas por cluster de Entidade/Aggregate para manter baixo acoplamento no código; os Bounded Contexts de negócio agrupam por capacidade — um mesmo Bounded Context pode abranger mais de uma pasta técnica. A tabela "Mapeamento técnico", ao final de cada contexto, deixa essa relação explícita.

## Comercial

- **Responsabilidade:** captar, qualificar e negociar com o cliente até a proposta ser aprovada — cobre `Lead`, `Cliente`, `Consultor`, `Cotação`, `Proposta`.
- **Limites:** termina quando a proposta é aprovada e paga; a partir daí, a responsabilidade passa ao contexto Operações (emissão) — o Comercial não executa a viagem.
- **Dependências:** depende de Cadastro (para saber quem é o Cliente/Fornecedor) e de Financeiro (para saber condições de pagamento aplicáveis).
- **Mapeamento técnico:** `src/domain/proposal/` (`Proposal`, `ProposalVersion`, `ProposalClassification`) + `src/domain/customer/` (`Customer`, na parte de relacionamento comercial) + `Consultant` (fisicamente em `src/domain/company/`, conceitualmente pertence a este contexto).
- **Gaps conhecidos (ainda não modelados):** `Lead` e `Cotação` não existem como Entidades próprias ainda — hoje só aparecem em `docs/proposal-lifecycle.md`. Se o Workshop de Descoberta confirmar que precisam de identidade/persistência própria (e não apenas um estado inicial de `Proposal`), viram Entidades numa sprint futura.

## Operações

- **Responsabilidade:** executar a viagem depois da venda — cobre `Emissão`, `Voucher`, `Itinerário`, `Seguro`, `Documentos`.
- **Limites:** começa quando uma `ProposalVersion` é paga; termina no Pós-venda (`docs/proposal-lifecycle.md`). Não decide preço nem condição comercial — apenas executa o que o Comercial fechou.
- **Dependências:** depende do Comercial (recebe a Proposta aprovada) e de Cadastro (Fornecedores que efetivamente prestam o serviço).
- **Mapeamento técnico:** `src/domain/trip/` (`Trip`, `Flight`, `Accommodation`, `Service`) cobre hoje a parte de *planejamento* da viagem. `Emissão`, `Voucher`, `Itinerário` (como artefato) e `Seguro` (como produto contratado, distinto do Fornecedor "seguradora") ainda **não têm Entidade própria** — são módulos futuros de documento (ver `ARCHITECTURE.md`, seção 2).
- **Gaps conhecidos:** este é o contexto com mais lacuna de modelagem hoje — proposital, já que a Sprint 1A cobre só o módulo Propostas.

## Financeiro

- **Responsabilidade:** valores, condições de pagamento e (futuramente) comissionamento — cobre `Pagamento`, `Parcelamento`, `Comissão`.
- **Limites:** calcula e representa condições financeiras; não decide política comercial (isso é Comercial) nem executa a cobrança de fato (isso seria uma integração de Infraestrutura futura, ex: gateway de pagamento).
- **Dependências:** depende do Comercial (uma condição financeira só existe associada a uma `ProposalVersion`).
- **Mapeamento técnico:** `src/domain/financial/` (`Financial`, Value Object).
- **Gaps conhecidos:** `Comissão` (do consultor ou de parceiros) não está modelada ainda — não apareceu em nenhum documento de descoberta até aqui; é uma pergunta a incluir num futuro Workshop de Descoberta se for relevante para a 027.

## Cadastro

- **Responsabilidade:** dados de referência que existem independentemente de qualquer proposta específica — cobre `Empresa`, `Passageiro`, `Fornecedor` (e, por extensão, `Cliente` e `Consultor`, como dados cadastrais).
- **Limites:** é o contexto mais estável — dados aqui mudam com pouca frequência e são reaproveitados por todos os outros contextos via referência (`Identifier`), nunca copiados.
- **Dependências:** nenhuma — é a base sobre a qual os demais contextos se apoiam.
- **Mapeamento técnico:** `src/domain/company/` (`Company`, `Consultant`), `src/domain/customer/` (`Customer`, `Passenger` — cadastro; o uso comercial de `Customer` é compartilhado com o contexto Comercial, ver acima), `src/domain/supplier/` (`Supplier`).

## Comunicação entre contextos

- Contextos se comunicam **por referência de identidade** (`Identifier`), nunca embutindo o objeto de outro contexto dentro do seu próprio Aggregate — é por isso que `ProposalVersion` (Comercial) guarda `customer_id`, `trip_id`, `company_id`, `consultant_id` em vez de conter `Customer`/`Trip`/`Company`/`Consultant` completos.
- A comunicação orientada a eventos (um contexto reagindo a algo que aconteceu em outro — ex: Operações reagindo a "Proposta paga") está preparada estruturalmente (`src/domain/shared/domain_event.py`), mas **nenhum evento concreto existe ainda** — isso é trabalho de uma sprint futura, quando `src/application/` deixar de estar vazio.
- Nenhum contexto deve importar uma Entidade interna de outro contexto para modificá-la diretamente — só o próprio contexto muta suas Entidades.

## Relação com outros documentos

- `docs/glossary.md` — todo termo usado aqui deve ser consistente com a Linguagem Ubíqua ali definida.
- `docs/domain-map.md` — relacionamento entre entidades dentro de um contexto (mais granular que este documento, que é sobre fronteiras entre contextos).
- `docs/ARCHITECTURE.md` — módulos de documento e capacidades de plataforma (visão de produto) versus Bounded Contexts (visão de domínio) — os módulos futuros de documento (Contratos, Vouchers) tendem a viver dentro do contexto Operações ou Comercial, dependendo do que representam.
