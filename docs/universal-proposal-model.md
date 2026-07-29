# Modelo Universal da Proposta

O Modelo Universal da Proposta é o objeto central do Motor de Propostas: **todo** documento gerado (HTML, PDF, WhatsApp, e-mail, payload de CRM) é produzido exclusivamente a partir dele, já validado, normalizado e enriquecido (ver fluxo obrigatório em `ARCHITECTURE.md`, seção 3). Nenhum gerador lê dado de nenhuma outra fonte.

Este documento descreve o modelo em nível conceitual — a seção, seu conteúdo e sua responsabilidade. A versão formal e versionada (tipos, obrigatoriedade, validação) será definida em `schemas/proposta.schema.json` no Sprint 1, a partir desta especificação.

## Metadata obrigatória

Todo Modelo Universal da Proposta carrega este bloco, independentemente do que é exibido ao cliente:

| Campo | Responsabilidade |
|---|---|
| `proposal_id` | Identificador único da proposta — chave de rastreamento em qualquer sistema (CRM, logs, suporte). |
| `schema_version` | Versão do schema do Modelo Universal usado para gerar este documento — permite evoluir a estrutura sem quebrar propostas antigas já emitidas/arquivadas. |
| `engine_version` | Versão da plataforma/motor que gerou o documento — útil para depurar problemas específicos de uma versão. |
| `template` | Qual template (por módulo/formato) foi usado para renderizar este documento. |
| `generated_at` | Data/hora de geração do documento. |
| `generated_by` | Processo/sistema que gerou o documento (ex: geração manual, geração assistida por IA, reemissão automática). |
| `consultor` | Referência rápida (nome/id) ao consultor responsável — a ficha completa do consultor vive na seção `consultor` abaixo; este campo existe para rastreamento sem precisar montar o objeto inteiro. |
| `origem` | Canal/origem da solicitação que gerou a proposta (ex: atendimento manual, importação, IA Comercial). |
| `status` | Estado da proposta (ex: rascunho, enviada, aceita, expirada, cancelada). |

Esses campos existem mesmo quando não aparecem no documento visível ao cliente — são o que torna qualquer proposta auditável e rastreável desde o primeiro dia, antes mesmo de existir um CRM.

## Seções do modelo

| Seção | Responsabilidade |
|---|---|
| `metadata` | Rastreabilidade técnica e de processo do documento (ver acima). |
| `empresa` | Dados institucionais da 027 Viagens exibidos no documento (razão social, CNPJ, contatos, logo) — espelha `config/empresa.json`; nunca hardcoded no template. |
| `consultor` | Ficha completa de quem está emitindo a proposta (nome, contato, foto/assinatura) — usada nos blocos de assinatura e contato. |
| `cliente` | Dados de quem recebe a proposta (nome, contato, documento quando aplicável). |
| `passageiros` | Lista de passageiros da viagem, podendo divergir do `cliente` (ex: cliente corporativo cotando para terceiros; viagem em grupo). |
| `viagem` | Destino(s), datas, tipo de viagem (lazer, corporativa, internacional, grupo, religiosa, etc.) — o tipo aqui é o que direciona as regras de negócio e textos aplicáveis (`business-rules.md`). |
| `voos` | Itinerário aéreo: trechos, companhias, horários — já normalizados (nomes de companhias/aeroportos padronizados, ver etapa de Normalização em `ARCHITECTURE.md`). |
| `hospedagem` | Hotéis/acomodações: nome, categoria, regime, datas de check-in/out. |
| `serviços` | Demais serviços inclusos ou opcionais: traslados, passeios, seguro, aluguel de carro — inclusão de opcionais segue as regras de Upsell/Cross-sell (`business-rules.md`). |
| `financeiro` | Valores, forma de pagamento, parcelamento, moeda — calculado por `src/core/` a partir das regras de pagamento/parcelamento. |
| `políticas` | Políticas aplicáveis a esta proposta especificamente (cancelamento, alteração, validade) — resolvidas a partir de `business-rules.md` e `config/politicas.json`, já como texto/condição final aplicável ao caso. |
| `observações` | Observações obrigatórias e observações específicas do caso (ver `business-rules.md`), texto pronto vindo de `content/`. |
| `anexos` | Referências a arquivos/imagens complementares (ex: imagens do destino, PDF de seguro, voucher relacionado). |

## Relação com outras camadas

- **`schemas/proposta.schema.json`** — versão formal deste modelo (Sprint 1), incluindo tipos e obrigatoriedade.
- **`src/models/`** — código que carrega e representa este modelo.
- **`src/core/`** — produz o modelo (valida, normaliza, aplica regra de negócio, enriquece); é a única camada que **escreve** no modelo.
- **`src/generators/propostas/`** e **`templates/propostas/`** — apenas **leem** o modelo já pronto; nunca o alteram nem buscam dado fora dele.
- **`content/` e `config/`** — fontes usadas durante o enriquecimento para preencher `empresa`, `políticas` e `observações` com o texto/dado institucional correto.

## Padrão para futuros módulos

Cada módulo futuro (Motor de Contratos, Motor de Vouchers, etc.) define seu próprio Modelo Universal (`Modelo Universal do Contrato`, `Modelo Universal do Voucher`...), com:

- A mesma metadata obrigatória descrita acima (adaptando `template`/`origem`/`status` ao contexto do módulo).
- Seções próprias do domínio daquele documento, reaproveitando as seções compartilhadas já existentes (`empresa`, `consultor`, `cliente`, `financeiro`) sempre que fizer sentido, em vez de recriá-las.
