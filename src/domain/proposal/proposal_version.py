"""ProposalVersion — Entidade filha do Aggregate `Proposal`.

Responsabilidade: representa uma Versão (ver docs/glossary.md e
docs/proposal-versioning.md) — um snapshot completo e imutável de uma
Proposta num determinado momento (ex: "001.2").

Relacionamentos: pertence a uma `Proposal`; referencia `Company`,
`Customer`, `Trip` e `Consultant` por id (nunca embutidos); carrega seu
próprio `ProposalClassification`, `Financial` e `Metadata`.

Invariantes (Sprint 1B):
- `version_number` não vazio; `company_id`/`customer_id`/`trip_id`/
  `consultant_id` válidos — é aqui, e não em `Proposal`, que se
  garantem "sempre possui um Customer"/"sempre possui uma Trip" do
  briefing (ver docs/domain-decisions.md sobre por que essas
  invariantes vivem na Versão, não na Proposal).
- `classification`/`financial`/`metadata` presentes — "sempre possui
  Metadata" do briefing.
- `status` (`ProposalVersionStatus`) presente e válido.

Observações: `status` aqui é o estado *estrutural tipado* desta versão
(Draft/Active/Archived). É diferente de `metadata.status` (texto livre,
genérico entre módulos) — ver docstring de `Metadata` e
docs/domain-decisions.md para a distinção completa. O critério de
quando uma mudança gera uma nova ProposalVersion (em vez de atualizar a
atual) é uma regra de negócio — Sprint 1B+ com `business-rules.md`
confirmado, ver docs/proposal-versioning.md.
"""

from dataclasses import dataclass

from src.domain.financial.financial import Financial
from src.domain.proposal.enums import ProposalVersionStatus
from src.domain.proposal.proposal_classification import ProposalClassification
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.guards import require_identifier, require_instance, require_non_empty_str
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
    status: ProposalVersionStatus

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.version_number, "ProposalVersion.version_number não pode ser vazio.")
        require_identifier(self.company_id, "ProposalVersion.company_id requer um Identifier válido.")
        require_identifier(self.customer_id, "ProposalVersion.customer_id requer um Identifier válido.")
        require_identifier(self.trip_id, "ProposalVersion.trip_id requer um Identifier válido.")
        require_identifier(self.consultant_id, "ProposalVersion.consultant_id requer um Identifier válido.")
        require_instance(self.classification, ProposalClassification, "ProposalVersion.classification é obrigatório.")
        require_instance(self.financial, Financial, "ProposalVersion.financial é obrigatório.")
        require_instance(self.metadata, Metadata, "ProposalVersion.metadata é obrigatório.")
        require_instance(self.status, ProposalVersionStatus, f"ProposalVersion.status inválido: {self.status!r}")
