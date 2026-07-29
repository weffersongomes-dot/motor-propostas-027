# Classificação da Proposta — Modelo por Dimensões

> **Revisão:** a versão anterior deste documento tratava "Tipo de Proposta" como um valor único (Nacional, Internacional, Corporativo, Religioso, Grupos, Disney, Cruzeiros, Individual, Incentivo, Outros), mutuamente exclusivos. A revisão arquitetural identificou que isso mistura conceitos independentes — uma proposta pode ser **Internacional + Grupo + Religiosa** ao mesmo tempo. Esta decisão está registrada em [ADR 0005](decisoes/0005-refinamento-pre-sprint-1a.md).

Uma `Proposta` (ver `glossary.md`) não tem um "tipo" único. Ela é classificada em **quatro dimensões independentes**, e pode assumir um ou mais valores em cada uma. Nenhum valor abaixo está confirmado com o negócio — este documento registra estrutura e perguntas, como no levantamento original.

## As quatro dimensões

| Dimensão | Pergunta que responde | Valores previstos |
|---|---|---|
| **Destino** | Para onde? | Nacional, Internacional |
| **Formato** | Para quantas pessoas, vendido como quê? | Individual, Grupo |
| **Finalidade** | Por que a viagem existe? | Lazer, Corporativo, Religioso, Incentivo |
| **Produto** | O que exatamente está sendo vendido? | Pacote, Cruzeiro, Disney, Hotel, Aéreo, Personalizado, Outros |

Uma proposta real é a combinação de (ao menos) um valor de cada dimensão — por exemplo: *Internacional + Grupo + Religioso + Pacote*, ou *Nacional + Individual + Lazer + Aéreo*. As regras de negócio (`business-rules.md`), textos (`content/`) e diferenciais aplicáveis a uma proposta podem depender de qualquer combinação dessas dimensões, não de um "tipo" isolado.

> **Pergunta geral:** essas quatro dimensões e seus valores cobrem como a 027 Viagens realmente pensa uma venda? Falta alguma dimensão (ex: "Duração", "Sazonalidade")? Algum valor deveria estar em outra dimensão?

---

## Dimensão: Destino

- **Nacional** — viagem com destino dentro do território brasileiro.
- **Internacional** — viagem com destino fora do Brasil.

**Dúvidas para o negócio:**
- Documentação/avisos obrigatórios variam por Destino (ex: passaporte, visto, seguro) — que particularidades entram na proposta em cada caso? (ver `business-rules.md`, Viagens internacionais/Seguros)
- Câmbio/moeda de cobrança: sempre em reais, mesmo para Internacional?
- Uma viagem pode ter trechos Nacionais e Internacionais na mesma proposta (ex: voo doméstico de conexão)? Isso muda a classificação de Destino da proposta inteira?

## Dimensão: Formato

- **Individual** — vendida para uma pessoa ou família/grupo pequeno.
- **Grupo** — vendida para múltiplos passageiros como um pacote único.

**Dúvidas para o negócio:**
- A partir de quantos passageiros uma proposta passa a ser "Grupo"? (ver `business-rules.md`, Grupos)
- "Grupo" sempre implica um responsável único pelo grupo (quem assina/aprova), mesmo com vários passageiros?
- Existe desconto ou condição comercial padrão associada a Formato = Grupo?

## Dimensão: Finalidade

- **Lazer** — viagem motivada por descanso/turismo pessoal.
- **Corporativo** — viagem contratada por uma empresa (pessoa jurídica).
- **Religioso** — viagem organizada em torno de um roteiro ou motivação religiosa.
- **Incentivo** — viagem oferecida por uma empresa como prêmio a funcionários/parceiros/clientes.

**Dúvidas para o negócio:**
- `Cliente` (quem contrata/paga) e `Passageiro` (quem viaja) são sempre diferentes quando Finalidade = Corporativo ou Incentivo? (ver `domain-map.md`)
- "Incentivo" é tratado como uma variação de "Corporativo" na prática, ou são comercialmente muito diferentes (ex: quem vê o preço)?
- Existem parcerias fixas (roteiros, lideranças) associadas a Finalidade = Religioso?
- Existe faturamento/nota fiscal com regras próprias quando Finalidade = Corporativo? (ver `business-rules.md`, Corporativo)

## Dimensão: Produto

- **Pacote** — combinação fechada de serviços (aéreo + hospedagem + traslados, por exemplo).
- **Cruzeiro** — viagem a bordo de um navio.
- **Disney** — roteiro centrado nos parques Disney.
- **Hotel** — apenas hospedagem.
- **Aéreo** — apenas passagem aérea.
- **Personalizado** — combinação sob medida, fora de um pacote fechado.
- **Outros** — categoria residual.

**Dúvidas para o negócio:**
- "Disney" continua justificando ser um valor próprio de Produto (em vez de, por exemplo, um Pacote com característica de Finalidade = Lazer)? Há particularidade comercial suficiente (parceria, comissionamento)?
- Para Produto = Cruzeiro, a seção `hospedagem` do Modelo Universal (`universal-proposal-model.md`) precisa virar/incluir uma seção de cabine — confirmar antes do Sprint 1B.
- Uma proposta pode combinar mais de um valor de Produto (ex: Aéreo + Hotel vendidos separadamente, mas na mesma proposta)? Isso é "Pacote" por definição, ou pode ser listado como Produto múltiplo?
- Com que frequência a operação real cai em Produto = Outros? Se for frequente, falta um valor nesta lista.

---

## Impacto na modelagem (Sprint 1A/1B)

- **Sprint 1A (Modelagem do Domínio):** o objeto `Proposta` deve representar as quatro dimensões como atributos próprios (ex: uma lista/conjunto por proposta), sem ainda validar quais combinações são permitidas.
- **Sprint 1B (Evolução do Modelo):** é onde entram os enums de cada dimensão e as regras de combinação (ex: "Formato = Grupo exige um campo de responsável pelo grupo"), a partir das respostas obtidas no Workshop de Descoberta (`discovery-workshop.md`).

## Relação com outros documentos

- `docs/business-rules.md` — regras que dependem de combinações de dimensões (ex: Seguros para Destino = Internacional) devem referenciar a dimensão e o valor específico, não mais um "tipo" solto.
- `docs/glossary.md` — os termos "Destino", "Formato", "Finalidade" e "Produto" e seus valores devem ser adicionados como conceitos de domínio.
- `tests/casos/` — os casos fictícios (corporativa, lazer, internacional, grupo, religioso, Disney, cruzeiro) devem ser revistos como combinações de dimensões, não como tipos isolados (ex: o caso "grupo religioso internacional" passa a ser um único caso de teste combinando três dimensões, não três casos separados).
