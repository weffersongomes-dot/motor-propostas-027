"""Proposal — Aggregate Root.

Responsabilidade: representa a Proposta (ver docs/glossary.md) — o
objeto comercial central da plataforma. É apenas a identidade estável
(`id`, ex: "001") e o histórico de Versões; todo o conteúdo real
(cliente, viagem, financeiro, classificação) vive em cada
`ProposalVersion`.

Relacionamentos: agrega `ProposalVersion` (relação linear, sem
ramificação — ver docs/proposal-versioning.md).

Observações: nenhum método de "aprovar", "cancelar" ou "criar nova
versão" existe nesta etapa — são comportamentos de domínio (Sprint 1B)
que vão orquestrar as regras de docs/proposal-actions.md e
docs/proposal-status.md.
"""

from dataclasses import dataclass, field
from typing import List

from src.domain.proposal.proposal_version import ProposalVersion
from src.domain.shared.base_entity import BaseEntity


@dataclass
class Proposal(BaseEntity):
    versions: List[ProposalVersion] = field(default_factory=list)
