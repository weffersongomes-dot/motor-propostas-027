# 0004 — Sprint 0.5: Engenharia Comercial e Descoberta do Negócio

- **Status:** aceita
- **Data:** 2026-07-28

## Contexto

A arquitetura técnica e o Modelo Universal da Proposta (ADRs [0001](0001-estrutura-inicial-do-projeto.md)–[0003](0003-consolidacao-arquitetura-v1.md)) foram desenhados com base em suposições razoáveis de mercado, não em conhecimento confirmado da operação real da 027 Viagens. O proprietário (Wefferson) é hoje a principal — e praticamente única — fonte desse conhecimento, que existe apenas na cabeça dele e na prática do dia a dia, não em documento algum.

Prosseguir direto para o Sprint 1 (schema `schemas/proposta.schema.json`) sem esse levantamento arriscaria embutir no schema suposições de mercado genéricas em vez de regras reais da 027 Viagens — indo contra o princípio "nenhuma regra de negócio escondida" já registrado em `vision.md`.

## Decisão

- Inserir uma nova sprint, **Sprint 0.5 — Engenharia Comercial e Descoberta do Negócio**, entre a arquitetura já consolidada e o Sprint 1, dedicada exclusivamente a levantamento de negócio (Business Analysis) — nenhum schema ou código é produzido nela.
- Renomear a sprint de evolução arquitetural anterior, que também usava o número "0.5", para **Sprint 0.4**, liberando "Sprint 0.5" para esta etapa de descoberta, conforme nomeada explicitamente.
- Adotar Domain-Driven Design (DDD) como abordagem: manter um glossário de linguagem ubíqua (`docs/glossary.md`) desde o início da descoberta, para que negócio e tecnologia usem exatamente os mesmos termos daqui em diante.
- Produzir cinco documentos de descoberta de negócio (`proposal-types.md`, `proposal-lifecycle.md`, `proposal-status.md`, `proposal-actions.md`, `proposal-versioning.md`), todos estruturados como "estrutura + perguntas", nunca "regras assumidas como fato".
- Produzir um roteiro estruturado de entrevistas (`discovery-workshop.md`), organizado por assunto, para conduzir a descoberta com o proprietário.
- Reorganizar `business-rules.md` no formato Objetivo / Regras conhecidas / Regras pendentes / Perguntas em aberto / Observações, tornando explícito o que é fato confirmado e o que é lacuna.

## Motivo

- Descoberta antes de modelagem é o princípio central de DDD: o schema técnico deve nascer *depois* de o domínio estar entendido e nomeado, não antes.
- Registrar "estrutura + perguntas" em vez de preencher informação desconhecida evita o maior risco desta etapa: regra de negócio inventada silenciosamente virar "fato" só porque ficou escrita num documento com aparência de definitivo.
- Um glossário único (`glossary.md`) evita que os cinco documentos de descoberta, o `business-rules.md` e o futuro schema usem sinônimos divergentes para o mesmo conceito (ex: "cotação" vs. "orçamento", "consultor" vs. "vendedor") — reduz retrabalho de tradução entre negócio e código mais tarde.
- Um roteiro de entrevista estruturado por assunto (`discovery-workshop.md`) torna a descoberta repetível e revisitável — não depende de "lembrar de perguntar" no momento da conversa.

## Consequências

- O Sprint 1 (Modelo de dados) passa a ter como pré-requisito explícito a conclusão desta sprint — ver `ROADMAP.md`.
- `schemas/proposta.schema.json`, quando criado, deve derivar de `universal-proposal-model.md` já ajustado pelas respostas obtidas nesta sprint, usando os mesmos nomes definidos em `glossary.md`.
- Perguntas de alta prioridade (validade de proposta, pagamento, parcelamento, cancelamento, observações obrigatórias — ver `business-rules.md`) devem ser respondidas antes de qualquer campo correspondente ser fixado no schema.
- Novos módulos de documento futuros (Contratos, Vouchers, etc.) devem passar por um processo de descoberta equivalente antes de seu próprio schema ser definido, seguindo o mesmo padrão desta sprint.
