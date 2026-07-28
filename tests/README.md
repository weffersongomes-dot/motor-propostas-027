# tests/

Testes automatizados da plataforma, usando **viagens fictícias** como casos de teste — cobrindo os cenários reais que a 027 Viagens atende, não apenas casos triviais.

## Estrutura

```
tests/
└── casos/           → um arquivo de dados fictício por cenário de viagem, no formato de schemas/proposta.schema.json
```

Cenários iniciais previstos (Sprint 1 em diante, conforme o modelo de dados for definido):

- Viagem corporativa
- Viagem de lazer
- Viagem internacional
- Viagem em grupo
- Viagem religiosa
- Viagem Disney
- Cruzeiro

Cada caso deve exercitar particularidades do cenário (ex: viagem internacional → exige passaporte/visto; grupo → múltiplos passageiros; cruzeiro → cabines em vez de quartos), forçando a arquitetura a lidar com a variação real do negócio, não só o caminho feliz.

## O que testar

- **Validação** (`src/core/`) — dados incompletos/inconsistentes de cada cenário são rejeitados com mensagem clara.
- **Regras de negócio** — cálculo de valores, parcelamento, seleção automática de textos/diferenciais por tipo de viagem.
- **Geradores** — HTML, PDF, WhatsApp, e-mail e JSON gerados a partir de um mesmo caso são consistentes entre si.

## Por que existe

Testar apenas com dados "perfeitos" esconde bugs que só aparecem com casos reais (viagem internacional, grupo grande, cruzeiro). Ter os 7 cenários documentados desde já também serve como especificação viva do que o sistema precisa suportar.
