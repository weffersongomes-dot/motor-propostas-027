# PRD — Motor de Propostas Comerciais (027 Viagens)

## 1. Problema

A criação de propostas comerciais na 027 Viagens é hoje um processo manual e repetitivo: para cada viagem cotada, é necessário montar o texto da proposta, formatar um PDF, escrever uma mensagem de WhatsApp e um e-mail de envio — tudo isso a partir das mesmas informações básicas (destino, datas, valores, serviços inclusos, etc.), refeito do zero a cada vez.

Isso gera:
- Retrabalho e perda de tempo em tarefas repetitivas;
- Inconsistência visual e de conteúdo entre propostas;
- Risco de erros de digitação/cálculo ao reescrever os mesmos dados em formatos diferentes;
- Dificuldade de rastrear/organizar propostas emitidas para uso futuro (CRM, histórico, relatórios).

## 2. Objetivo do produto

Criar um motor que, a partir de um único conjunto de dados sobre uma viagem, gere automaticamente todos os artefatos necessários para propor e fechar a venda:

1. Proposta comercial em HTML;
2. PDF profissional em papel timbrado;
3. Mensagem de WhatsApp para envio ao cliente;
4. E-mail de envio da proposta;
5. Dados estruturados para integração futura com Coda/CRM;
6. Nome de arquivo padronizado;
7. Checklist interno para emissão.

## 3. Público-alvo

- **Usuário primário:** equipe comercial/atendimento da 027 Viagens (perfil não-técnico), que hoje monta propostas manualmente.
- **Usuário secundário (futuro):** sistemas automatizados (CRM/Coda, automações de WhatsApp) consumindo os dados estruturados gerados pelo motor.

## 4. Funcionalidades

> Nesta primeira etapa (Sprint 0) nenhuma funcionalidade é implementada — apenas planejada. Implementação ocorre a partir do Sprint 1.

- Cadastro/entrada dos dados de uma viagem (formulário, planilha ou arquivo estruturado — a definir).
- Geração da proposta em HTML a partir de um template padrão.
- Geração do PDF em papel timbrado a partir do mesmo conteúdo.
- Geração de mensagem de WhatsApp pronta para envio (texto curto, com link/resumo da proposta).
- Geração de e-mail de envio (assunto + corpo) pronto para copiar/enviar.
- Geração de dados estruturados (JSON) representando a proposta, prontos para integração futura com Coda/CRM.
- Geração de nome de arquivo padronizado para a proposta (ex: `2026-07-28_Cliente_Destino_v1`).
- Geração de checklist interno de emissão (itens a conferir antes de enviar a proposta ao cliente).

## 5. Entradas

Dados mínimos necessários sobre a viagem para gerar uma proposta (estrutura final será definida no Sprint 1):

- Dados do cliente (nome, contato);
- Destino(s) e datas (ida/volta);
- Serviços inclusos (hospedagem, passagens, traslados, passeios, seguro, etc.);
- Valores (por pessoa, total, forma de pagamento, condições);
- Observações/condições comerciais (validade da proposta, política de cancelamento, etc.);
- Responsável comercial pela proposta (quem está emitindo).

## 6. Saídas

| Saída | Formato | Descrição |
|---|---|---|
| Proposta HTML | `.html` | Proposta comercial visualizável no navegador |
| Proposta PDF | `.pdf` | Versão em papel timbrado, pronta para envio/impressão |
| Mensagem WhatsApp | texto | Mensagem curta para envio direto ao cliente |
| E-mail | texto/HTML | Assunto + corpo do e-mail de envio da proposta |
| Dados estruturados | `.json` | Representação estruturada da proposta para integração com Coda/CRM |
| Nome do arquivo | string | Nome padronizado para salvar/organizar a proposta |
| Checklist de emissão | texto/lista | Itens internos a conferir antes de enviar a proposta |

## 7. Regras de negócio

> Regras detalhadas (cálculo de valores, formatos de data, validade da proposta, regras de nomenclatura de arquivo, etc.) serão definidas e documentadas no Sprint 1, junto ao modelo de dados. Aqui ficam os princípios gerais:

- Todos os formatos de saída devem ser gerados a partir de uma **única fonte de verdade** (o objeto/dados da proposta) — nunca digitados ou mantidos separadamente.
- Nome de arquivo, dados do JSON e conteúdo exibido devem sempre ser consistentes entre si.
- Regras de negócio (cálculos, validações, nomenclatura) ficam isoladas de templates/apresentação, permitindo reuso entre os diferentes geradores.
- Toda proposta gerada deve ser rastreável (identificador único, data de emissão, responsável).

## 8. Critérios de sucesso

- Uma proposta completa (todos os 7 artefatos) pode ser gerada a partir de um único conjunto de dados de entrada, sem retrabalho manual.
- Os diferentes formatos de saída (HTML, PDF, WhatsApp, e-mail) são visualmente e textualmente consistentes entre si.
- Tempo de emissão de uma proposta reduzido de forma significativa em relação ao processo manual atual.
- Estrutura do projeto permite adicionar novos formatos de saída ou integrações (Coda, WhatsApp, IA) sem redesenhar o sistema.
- Documentação suficiente para que outra pessoa (ou uma IA) consiga entender e evoluir o projeto sem depender de conhecimento tácito.

## 9. Requisitos funcionais

- RF01 — O sistema deve receber dados de uma viagem em um formato estruturado definido.
- RF02 — O sistema deve gerar uma proposta em HTML a partir de um template padrão.
- RF03 — O sistema deve gerar um PDF em papel timbrado a partir do mesmo conteúdo da proposta.
- RF04 — O sistema deve gerar uma mensagem de WhatsApp de envio.
- RF05 — O sistema deve gerar um e-mail de envio (assunto + corpo).
- RF06 — O sistema deve gerar dados estruturados (JSON) representando a proposta.
- RF07 — O sistema deve gerar um nome de arquivo padronizado para a proposta.
- RF08 — O sistema deve gerar um checklist interno de itens a conferir antes da emissão.
- RF09 — O sistema deve permitir reaproveitar o mesmo conjunto de dados para gerar todos os formatos de saída, sem retrabalho.

## 10. Requisitos não funcionais

- RNF01 — Arquitetura modular, com regras de negócio separadas da apresentação.
- RNF02 — Código e estrutura preparados para futura integração com APIs externas (Coda, WhatsApp) e banco de dados, sem exigir reescrita da base.
- RNF03 — Documentação clara o suficiente para retomada do projeto por outra pessoa ou IA.
- RNF04 — Nomes de arquivos, pastas e módulos claros e consistentes com o domínio do negócio.
- RNF05 — Sem duplicação de regras entre os diferentes geradores de saída.
- RNF06 — Dados sensíveis de clientes (nas saídas geradas) não devem ser versionados no Git.

## 11. Backlog inicial

- [ ] Definir o modelo de dados da proposta (campos, tipos, obrigatoriedade) — Sprint 1.
- [ ] Definir template visual da proposta HTML — Sprint 2.
- [ ] Escolher e validar ferramenta de geração de PDF a partir de HTML/CSS — Sprint 3.
- [ ] Desenhar o papel timbrado (arte-base) em `assets/papel_timbrado/` — Sprint 3.
- [ ] Criar o "Prompt Mestre" para geração assistida por IA da proposta — Sprint 4.
- [ ] Definir regras de validação automática dos dados de entrada — Sprint 5.
- [ ] Mapear estrutura de integração com Coda (schema de tabela/API) — Sprint 6.
- [ ] Mapear formato de integração com WhatsApp (API oficial vs. link `wa.me`) — Sprint 7.
- [ ] Levantar oportunidades de uso de IA para melhorar textos/sugestões de venda — Sprint 8.
