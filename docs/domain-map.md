# Mapa de Domínio

Representação textual dos principais conceitos do domínio (ver `docs/glossary.md` para a definição de cada termo) e como eles se relacionam. Não é um schema — é o mapa que qualquer schema futuro (Sprint 1A/1B) deve respeitar. Sem diagramas complexos, propositalmente: se a relação não pode ser dita numa frase simples, o conceito provavelmente ainda não está claro o suficiente.

## Relacionamento principal

```
Empresa
   │
   │ emprega
   ▼
Consultor
   │
   │ atende
   ▼
Cliente
   │
   │ possui
   ▼
Passageiros
   │
   │ participam de
   ▼
Viagem
   │
   │ envolve
   ▼
Voos, Hospedagem, Serviços  ←── prestados por ──  Fornecedor
   │
   │ geram
   ▼
Proposta
   │
   │ possui
   ▼
Versões
   │
   │ geram
   ▼
Documentos (HTML, PDF, WhatsApp, E-mail)
   │
   │ resultam em
   ▼
Emissão
```

## Entidades principais

| Entidade | Responsabilidade |
|---|---|
| **Empresa** | Representa a 027 Viagens em si — dados institucionais que aparecem em todo documento emitido. |
| **Consultor** | Colaborador que atende o Cliente e conduz a Proposta do início ao fim. |
| **Cliente** | Pessoa ou empresa que contrata a viagem; pode ou não coincidir com os Passageiros. |
| **Passageiro** | Pessoa que efetivamente viaja; associada a uma Viagem/Proposta. |
| **Fornecedor** | Empresa parceira que presta um serviço concreto da viagem (companhia aérea, hotel, operadora, seguradora). |
| **Viagem** | O conjunto de destino, datas e serviços que a Proposta descreve. |
| **Voo, Hospedagem, Serviço** | Componentes concretos da Viagem, cada um fornecido por um Fornecedor. |
| **Proposta** | Documento comercial central, agregando Cliente, Passageiros, Viagem e Financeiro em uma oferta. |
| **Versão** | Um estado específico e imutável da Proposta ao longo do tempo (ver `proposal-versioning.md`). |
| **Documento** | Qualquer artefato gerado a partir de uma Versão (HTML, PDF, WhatsApp, e-mail — ver `ARCHITECTURE.md`). |
| **Emissão** | Resultado de uma Proposta paga e confirmada junto aos Fornecedores — o fim do ciclo de venda, início do ciclo da Viagem em si. |
| **Financeiro** | Os valores, forma de pagamento e parcelamento associados à Proposta. |
| **Metadata** | Dados de rastreabilidade presentes em toda Proposta/Documento, independentemente do que é exibido ao cliente (ver `universal-proposal-model.md`). |

## Dependências entre entidades

- **Proposta depende de** Cliente, Passageiro(s) e Viagem já existirem (ainda que informalmente, na conversa com o cliente) — não existe Proposta "vazia" de conteúdo.
- **Viagem depende de** ao menos um componente concreto (Voo, Hospedagem ou Serviço) para fazer sentido como oferta.
- **Voo/Hospedagem/Serviço dependem de** um Fornecedor associado — ainda que o Fornecedor específico só seja definido na Cotação.
- **Versão depende de** uma Proposta já criada; não existe Versão solta.
- **Documento depende de** uma Versão específica (nunca "a Proposta" de forma genérica — ver `proposal-versioning.md`).
- **Emissão depende de** uma Versão aprovada e paga.
- **Metadata acompanha** toda Proposta e todo Documento, desde a criação — não é opcional nem calculada depois.

## Observações

- Este mapa usa a hipótese (ainda não confirmada, ver `discovery-workshop.md`) de que Cliente e Passageiro podem ser pessoas diferentes — importante para os casos Corporativo e Incentivo (ver `proposal-types.md`).
- Fornecedor aparece como uma entidade própria, não apenas um texto livre dentro de Voo/Hospedagem/Serviço — isso é uma decisão de modelagem (Sprint 1A), a confirmar se faz sentido operacionalmente (ex: a 027 realmente cadastra/reaproveita fornecedores entre propostas, ou cada cotação é isolada?).
- Este mapa cobre apenas o módulo **Propostas**. Módulos futuros (Contratos, Vouchers, etc. — ver `ARCHITECTURE.md`) terão entidades próprias, mas devem reaproveitar Empresa, Cliente, Passageiro, Consultor, Fornecedor e Financeiro em vez de recriá-los.
- Qualquer novo relacionamento identificado durante o Workshop de Descoberta (`discovery-workshop.md`) deve ser adicionado aqui antes de virar código na Sprint 1A/1B.
