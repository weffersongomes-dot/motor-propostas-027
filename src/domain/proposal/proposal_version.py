"""ProposalVersion — Entidade filha do Aggregate `Proposal`.

Responsabilidade: representa uma Versão (ver docs/glossary.md e
docs/proposal-versioning.md) — um snapshot completo e imutável de uma
Proposta num determinado momento (ex: "001.2").

Relacionamentos: pertence a uma `Proposal`; referencia `Company`,
`Customer`, `Trip` e `Consultant` por id (nunca embutidos); carrega seu
próprio `ProposalClassification`, `Financial` e `Metadata`.

Observações: `status` não existe como campo próprio aqui — vive em
`metadata.status`, para não haver duas fontes de verdade sobre o
estado da versão (ver docs/universal-proposal-model.md). O critério de
quando uma mudança gera uma nova ProposalVersion (em vez de atualizar
a atual) é uma regra de negócio — Sprint 1B, ver
docs/proposal-versioning.md.
"""

from dataclasses import dataclass

from src.domain.financial.financial import Financial
from src.domain.proposal.proposal_classification import ProposalClassification
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.identifier import Identifier
from src.domain.shared.metadata import Metadata


@dataclass
class ProposalVersion(BaseEntity):
    version_number: str
    company_id: Identifier
    customer_id: Identifier
    trip_id: Identifier
    consultant_id: Identifier
    classification: ProposalClassification
    financial: Financial
    metadata: Metadata
