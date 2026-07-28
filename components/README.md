# components/

Biblioteca de **blocos visuais reutilizáveis** usados para montar os templates de qualquer tipo de documento (proposta, e futuramente contrato, voucher, itinerário, etc.).

## O que entra aqui

Fragmentos de apresentação, sem regra de negócio nenhuma — apenas recebem dados já prontos (vindos do modelo único, ver `docs/ARCHITECTURE.md`) e os exibem:

- Cabeçalho institucional
- Rodapé
- Bloco de voo
- Bloco de hotel
- Bloco financeiro (valores, parcelamento)
- Bloco de assinatura
- QR Code
- Bloco de diferenciais
- Bloco de observações

## Organização

Componentes visuais existem por formato, porque HTML e PDF têm marcações diferentes mesmo representando o mesmo bloco:

```
components/
├── html/     → partials HTML (ex: incluídos via Jinja2 nos templates de templates/*/html/)
└── pdf/      → partials equivalentes para o template de PDF
```

WhatsApp e e-mail são baseados em texto, não em blocos visuais — fragmentos de texto reutilizáveis (saudação, assinatura em texto, etc.) ficam em `content/`, não aqui.

## Regra de ouro

Um componente recebe dados e devolve apresentação. Nunca calcula, nunca decide, nunca valida — isso é responsabilidade de `src/core/`. Se um componente "precisa pensar", a lógica pertence ao core, não ao componente.

## Por que existe

Qualquer novo tipo de documento (contrato, voucher, itinerário) reaproveita os mesmos blocos (cabeçalho, bloco de voo, assinatura, etc.) em vez de recriá-los — reduz duplicação e mantém consistência visual entre todos os documentos da 027 Viagens.
