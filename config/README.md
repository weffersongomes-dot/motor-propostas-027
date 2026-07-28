# config/

Guarda todas as **informações institucionais e comerciais da 027 Viagens** que hoje ficam soltas ou repetidas manualmente em cada proposta. Nada disso deve ser digitado dentro de código ou de template — sempre lido a partir daqui.

## O que entra aqui

- Dados da empresa: razão social, CNPJ, endereço, contatos, redes sociais.
- Identidade visual: caminho do logo, cores institucionais (referência para `assets/`).
- Formas de pagamento e regras de parcelamento aceitas.
- Políticas padrão (cancelamento, reembolso, validade de proposta).
- Observações padrão que aparecem em todo documento (rodapés legais, avisos).

## O que **não** entra aqui

- Dados de uma viagem/cliente específico (isso é entrada, vem do usuário — ver `schemas/proposta.schema.json`).
- Texto longo institucional (políticas completas, FAQ, e-mails-modelo) — isso vive em `content/`. Aqui ficam os *dados* (ex: "parcelamento em até 12x"), lá ficam os *textos* que explicam esses dados ao cliente.

## Formato

Arquivos de configuração em JSON (ex: `empresa.json`, `pagamento.json`, `politicas.json`), consumidos por `src/core/` e por `components/` na montagem de qualquer documento. Serão criados a partir do Sprint 1, quando o modelo de dados for definido.

## Por que existe

Se o CNPJ, o Pix da empresa ou a política de cancelamento mudar, a correção deve acontecer em **um único lugar**, refletindo automaticamente em todos os formatos de saída (HTML, PDF, WhatsApp, e-mail) e em todos os tipos de documento (proposta, contrato, voucher, etc.) — nunca exigir buscar e trocar em vários templates.
