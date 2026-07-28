# content/

Centraliza **todos os textos institucionais e comerciais** do sistema — o conteúdo editorial, separado de dados (`config/`) e de código (`src/`).

## O que entra aqui

- `politicas/` — texto completo de políticas (cancelamento, reembolso, alterações).
- `mensagens/` — mensagens padrão usadas em múltiplos formatos (avisos, lembretes).
- `emails/` — assunto e corpo-modelo dos e-mails de envio (proposta, confirmação, etc.).
- `whatsapp/` — modelos de mensagem de WhatsApp.
- `faq/` — perguntas frequentes que podem ser anexadas a um documento.
- `diferenciais/` — textos de venda sobre diferenciais da 027 Viagens, usados na composição das propostas.
- `textos_comerciais/` — demais textos comerciais reaproveitáveis (aberturas, CTAs, textos por tipo de viagem).

## O que **não** entra aqui

- Dados institucionais estruturados (CNPJ, telefone, Pix) — isso é `config/`.
- Lógica de **quando** usar cada texto (ex: "se for viagem internacional, incluir aviso de passaporte") — essa decisão é regra de negócio e vive em `src/core/`. Aqui fica só o texto em si; a escolha de qual texto usar é feita pelo core.

## Formato

Textos em Markdown ou JSON (a definir no Sprint 1), organizados por categoria e, quando fizer sentido, por tipo de viagem (corporativa, lazer, internacional, grupo, religioso, Disney, cruzeiro — os mesmos tipos usados em `tests/casos/`).

## Por que existe

Hoje, textos comerciais e institucionais são redigidos manualmente a cada proposta. Centralizá-los permite que o time de atendimento (perfil não-técnico) revise e atualize a redação sem tocar em código, e garante que a mesma política ou o mesmo diferencial seja descrito com as mesmas palavras em todos os documentos.
