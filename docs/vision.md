# Visão — Plataforma de Documentos Comerciais (027 Viagens)

Este documento é a referência de mais alto nível do projeto. Qualquer pessoa (ou IA) que venha a desenvolver aqui deve conseguir ler só este arquivo e entender por que o projeto existe, para quem, e o que nunca pode ser sacrificado no caminho.

## Qual problema a plataforma resolve

Cada documento comercial que a 027 Viagens emite para um cliente — hoje, principalmente a proposta comercial — é montado manualmente: os mesmos dados da viagem são reescritos em formatos diferentes (texto de proposta, PDF, mensagem de WhatsApp, e-mail), a cada vez, por uma pessoa. Isso custa tempo, é sujeito a erro e a inconsistência entre documentos, e não deixa rastro estruturado que possa alimentar um CRM ou uma automação depois.

A plataforma resolve isso transformando "montar um documento comercial" em "descrever a viagem/cliente uma vez, gerar tudo automaticamente" — para a proposta primeiro, e para qualquer outro documento comercial da agência depois.

## Quem utilizará o sistema

- **Equipe comercial/atendimento da 027 Viagens** (perfil não-técnico) — hoje monta propostas manualmente; passa a alimentar dados uma vez e receber todos os formatos prontos.
- **Gestão da 027 Viagens** — passa a ter dados estruturados de cada proposta/documento emitido, hoje inexistentes, como base para relatórios e CRM.
- **Sistemas automatizados (futuro)** — CRM, automações de WhatsApp, portais — consumindo o Modelo Universal de cada documento (ver `ARCHITECTURE.md`) em vez de dado solto.
- **Desenvolvedores futuros (humanos ou IA)** — este e os demais documentos em `docs/` existem para que qualquer pessoa nova consiga contribuir sem depender de conhecimento tácito de quem construiu o sistema.

## Qual transformação ela entrega

De um processo manual, repetitivo e sem rastro, para um motor onde:

- Um único conjunto de dados gera todos os formatos de saída de um documento, sempre consistentes entre si;
- Toda regra comercial usada na geração está documentada (`business-rules.md`), não escondida em código;
- Todo documento gerado carrega metadata que permite auditoria e rastreabilidade, mesmo antes de existir um CRM;
- A base de dados de cada proposta (e, depois, de cada documento) já nasce estruturada e pronta para alimentar CRM, automações e relatórios.

## Visão para os próximos cinco anos

O Motor de Propostas é o primeiro módulo de uma **Plataforma de Documentos Comerciais** completa da 027 Viagens. A expectativa de evolução, sem compromisso de prazo, é:

1. **Motor de Propostas** consolidado como base (módulo 1, foco atual).
2. Novos **módulos de documento** cobrindo o ciclo de vida completo da venda: Contratos, Vouchers, Itinerários, Confirmações de Reserva, Recibos, Checklists do Passageiro, Relatórios.
3. **Capacidades de plataforma** construídas sobre o Modelo Universal já existente: CRM, Notificações, Automação de WhatsApp, IA Comercial, Portal Administrativo, Portal do Cliente, Integrações externas.
4. A plataforma se torna o sistema de registro central da operação comercial da 027 Viagens — todo documento emitido, toda regra aplicada e todo dado de cliente/viagem passam por ela, com histórico auditável.

Nenhum desses passos deve exigir redesenhar o que já existe — é essa a razão de existir da arquitetura descrita em `ARCHITECTURE.md`.

## Princípios que nunca poderão ser quebrados

Estes princípios são o critério de aceite implícito de qualquer mudança futura, de qualquer módulo, feita por qualquer pessoa ou IA:

1. **Fonte única de dados** — todo documento gerado nasce de um único Modelo Universal, validado e enriquecido. Nenhum gerador ou template busca dado fora dele, nem direto do usuário.
2. **Regra de negócio nunca vive em template** — HTML, PDF, WhatsApp e e-mail apenas apresentam. Decisão e cálculo vivem em `src/domain/`.
3. **Nada institucional fixo em código** — dados da empresa (`config/`) e textos institucionais (`content/`) são editáveis sem deploy e sem tocar em código.
4. **Nenhuma regra comercial escondida** — toda regra usada na geração de um documento está documentada em `business-rules.md` antes ou junto de virar código.
5. **Módulos não se acoplam entre si** — um módulo de documento (proposta, contrato, voucher...) nunca depende de outro módulo, só das camadas compartilhadas.
6. **Todo documento é rastreável** — metadata obrigatória (`proposal_id`, `schema_version`, `generated_at`, `generated_by`, `status`, etc.) existe em todo documento gerado, mesmo quando não exibida ao cliente.
7. **Crescer não é refatorar** — adicionar um novo módulo ou capacidade segue a estratégia de expansão documentada em `ARCHITECTURE.md`, sem mover ou reescrever o que já está em produção.
