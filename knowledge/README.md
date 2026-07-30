# knowledge/

Base de conhecimento operacional da 027 Viagens — dados de referência sobre fornecedores, destinos e formas de pagamento que a operação usa no dia a dia. **Estrutura preparada nesta sprint; nenhum conteúdo foi preenchido ainda.**

## Diferença em relação a `docs/business-cases/`

- `docs/business-cases/` guarda **histórias** (como uma venda específica aconteceu).
- `knowledge/` guarda **fatos de referência reutilizáveis** que aparecem repetidamente nessas histórias (ex: "a 027 sempre usa a Seguradora X para viagens internacionais" é conhecimento; "neste caso específico usamos a Seguradora X porque..." é um business case).

Quando um business case menciona um fornecedor, destino ou forma de pagamento relevante, os dados de referência (não a história) devem ser extraídos para cá.

## Diferença em relação a `src/domain/supplier/`

`src/domain/supplier/supplier.py` é a **estrutura** de um Fornecedor (nome, categoria, contato — ver `SupplierCategory`). `knowledge/` é o **conteúdo** — quais fornecedores específicos a 027 realmente usa, suas particularidades, condições negociadas. Um dia, `knowledge/` pode alimentar dados iniciais de `Supplier` (via seed/importação), mas isso é trabalho de uma sprint de infraestrutura futura, não desta.

## Subpastas

- **`suppliers/`** — fornecedores gerais que não se encaixam nas categorias mais específicas abaixo (operadoras, receptivos, guias).
- **`airlines/`** — companhias aéreas parceiras/mais usadas: rotas, política de bagagem observada na prática, contatos.
- **`hotels/`** — hotéis/redes parceiras: categorias, condições negociadas, particularidades.
- **`insurance/`** — seguradoras parceiras: coberturas, quando é obrigatório oferecer (ver `docs/business-rules.md`, Seguros).
- **`destinations/`** — informações específicas de destino (documentação exigida, sazonalidade, particularidades logísticas) que se repetem entre propostas.
- **`payments/`** — formas de pagamento aceitas na prática, gateways/processadoras usadas, particularidades observadas (ver `docs/business-rules.md`, Regras de pagamento — quando confirmado).

## Como preencher

Conteúdo entra aqui a partir dos Workshops de Descoberta (`docs/discovery-workshop.md`) e dos `docs/business-cases/` já processados — nunca inventado. Cada subpasta deve, quando começar a receber conteúdo, adotar um arquivo por fornecedor/destino/forma de pagamento (ex: `knowledge/airlines/latam.md`), não um único arquivo genérico.
