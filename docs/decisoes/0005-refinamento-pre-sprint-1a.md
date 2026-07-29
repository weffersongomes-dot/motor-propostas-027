# 0005 — Refinamento Arquitetural Pré-Sprint 1A

- **Status:** aceita
- **Data:** 2026-07-28

## Contexto

Uma revisão da arquitetura produzida na Sprint 0.5 (ADR [0004](0004-sprint-05-engenharia-comercial.md)), feita antes de iniciar a modelagem técnica, identificou quatro pontos que precisavam ser resolvidos ou refinados antes que o Sprint 1 (Modelo de dados) começasse: (1) o Sprint 1, como planejado, misturava "representar o domínio" com "aplicar regras sobre ele" em uma única etapa; (2) `proposal-types.md` tratava a classificação da proposta como um valor único, quando na prática uma proposta acumula várias classificações independentes ao mesmo tempo (ex: internacional + grupo + religiosa); (3) o ciclo de vida da proposta (`proposal-lifecycle.md`) não tinha uma etapa explícita para avaliar se um lead vale a pena antes do atendimento completo; (4) o glossário (`glossary.md`) já existia, mas não tinha estrutura suficiente para funcionar como Linguagem Ubíqua formal (DDD) — faltava contexto de uso, sinônimos aceitos/proibidos e impacto explícito no código.

## Decisão

1. **Dividir o Sprint 1 em Sprint 1A (Modelagem do Domínio) e Sprint 1B (Evolução do Modelo).** A Sprint 1A representa apenas a forma dos conceitos (Empresa, Cliente, Passageiro, Consultor, Fornecedor, Documento, Proposta, Viagem, Hospedagem, Voo, Serviço, Financeiro, Metadata), sem validação, obrigatoriedade, enum ou regra de negócio. A Sprint 1B adiciona tudo isso, com base nas respostas coletadas na Sprint 0.5. Ver `ROADMAP.md`.
2. **Adotar modelagem por dimensões para a classificação da proposta**, substituindo a ideia de "Tipo de Proposta" único por quatro dimensões independentes e combináveis: Destino, Formato, Finalidade, Produto (ver `proposal-types.md` reescrito).
3. **Incluir a etapa Qualificação** no ciclo de vida da proposta, entre Lead e Primeiro contato (ver `proposal-lifecycle.md` atualizado).
4. **Adotar formalmente a Linguagem Ubíqua (DDD) como padrão do projeto**, evoluindo `glossary.md` para conter, por termo: definição oficial, contexto de uso, sinônimos aceitos, termos proibidos e impacto no código/documentação. Nenhum documento, prompt, schema, código, banco de dados ou interface deve divergir dessa terminologia.

Decisões complementares registradas junto: criação de `docs/domain-map.md` (relacionamento textual entre entidades do domínio); reorganização de `business-rules.md` em quatro grupos (Regras Comerciais, Financeiras, Operacionais, Legais); reorganização de `discovery-workshop.md` em cinco workshops independentes (Atendimento, Financeiro, Operação, Emissão, Pós-venda), cada um com objetivo, participantes, perguntas, documentos atualizados e decisões esperadas.

## Motivo

- Separar "representar o domínio" (Sprint 1A) de "aplicar regra sobre ele" (Sprint 1B) evita que a primeira versão do modelo de dados já nasça acoplada a regras de negócio ainda não confirmadas (`business-rules.md` seguia, e segue, majoritariamente pendente) — o objeto de domínio pode avançar mesmo enquanto o negócio ainda está sendo entrevistado.
- Um "tipo" único de proposta forçaria decisões arbitrárias sempre que uma proposta real combinasse características (ex: escolher entre "Grupo" ou "Religioso" quando é as duas coisas). Modelar por dimensões independentes remove essa falsa exclusividade e evita retrabalho de schema quando a primeira combinação "impossível" aparecer na prática.
- Qualificação como etapa própria reconhece que nem todo Lead merece o mesmo nível de atendimento — sem essa etapa, o ciclo de vida documentado não refletiria uma decisão que provavelmente já acontece na operação, ainda que informalmente.
- Um glossário raso (só "termo → definição") não sustenta Linguagem Ubíqua de verdade: sem "termos proibidos" e "impacto no código", é fácil um documento novo reintroduzir um sinônimo divergente sem perceber. A estrutura mais rica é o que torna o glossário administrável enquanto o projeto cresce.

## Consequências

- `ROADMAP.md`: Sprint 1 não existe mais como etapa única; toda referência futura deve apontar para Sprint 1A ou 1B especificamente.
- `schemas/proposta.schema.json` (Sprint 1B) deve representar Destino/Formato/Finalidade/Produto como atributos próprios e potencialmente multivalorados do objeto `Proposta`, nunca como um único campo "tipo".
- `tests/casos/` deve ser revisado para representar casos como combinações de dimensões, não como tipos isolados.
- Qualquer novo documento de domínio criado a partir de agora deve, antes de introduzir um termo, verificar `glossary.md` e seguir sua estrutura completa (definição, contexto, sinônimos, termos proibidos, impacto).
- Módulos futuros (Contratos, Vouchers, etc.) que exigirem sua própria classificação por múltiplas facetas devem seguir o mesmo padrão de dimensões independentes adotado aqui para Propostas, em vez de reintroduzir um "tipo" único.
