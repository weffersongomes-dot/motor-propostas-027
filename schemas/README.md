# schemas/

Define os **modelos JSON** (JSON Schema) que descrevem formalmente cada estrutura de dados usada pela plataforma. É a fonte de verdade sobre "quais campos existem, quais tipos têm, quais são obrigatórios" — tanto para humanos quanto para validação automática (Sprint 5).

## O que entra aqui

- `proposta.schema.json` — estrutura completa de uma proposta comercial (o "modelo único" do fluxo de dados, ver `docs/ARCHITECTURE.md`).
- `cliente.schema.json` — dados do cliente.
- `viagem.schema.json` — destino, datas, serviços inclusos.
- `pagamento.schema.json` — valores, forma de pagamento, parcelamento.
- `empresa.schema.json` — espelha a forma de `config/empresa.json`, para validação.

À medida que novos módulos da plataforma forem adicionados (contrato, voucher, itinerário, confirmação de reserva, recibo, checklist do passageiro, relatório), cada um ganha seu próprio schema aqui — reaproveitando os schemas menores já existentes (`cliente`, `viagem`, `pagamento`) sempre que possível.

## Relação com `src/models/`

`schemas/` descreve a estrutura (o "contrato de dados"); `src/models/` é o código que carrega, lê e (no Sprint 5) valida os dados contra esses schemas. Schema muda → validação em `src/models/` deve refletir a mudança.

## Por que existe

Ter os schemas isolados, versionados e documentados torna qualquer novo formato de saída ou integração (Coda, CRM, WhatsApp Business API) capaz de saber exatamente o que esperar dos dados, sem precisar ler código Python para descobrir a estrutura.
