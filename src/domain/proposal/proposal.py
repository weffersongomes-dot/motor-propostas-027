"""Proposal — Aggregate Root de Coordenação (ver ADR 0007).

Responsabilidade: representa a Proposta (ver docs/glossary.md) — a
identidade estável (`id`, ex: "001"), seu status estrutural, e o
histórico de Versões. Proposal **coordena** os demais Aggregates
(Company, Customer, Trip) por referência — não é proprietária deles, e
todo o conteúdo real (cliente, viagem, financeiro, classificação) vive
em cada `ProposalVersion`, nunca em Proposal diretamente. Ver ADR 0007
para a formalização completa deste princípio.

Relacionamentos: agrega `ProposalVersion` (relação linear, sem
ramificação — ver docs/proposal-versioning.md).

Invariantes (Sprint 1B):
- `status` (`ProposalStatus`) presente e válido — "Estado do Modelo"
  desta sprint (Draft/Published/Closed).
- **sempre possui ao menos uma ProposalVersion** (`versions` não
  vazio) — do exemplo do briefing "sempre possui uma ProposalVersion
  ativa", implementado aqui como limite inferior estrutural (ter
  versão) mais o limite superior abaixo (nunca mais de uma Active ao
  mesmo tempo). Exigir que *sempre* exista uma versão com status
  ACTIVE seria forte demais para uma Proposal recém-criada, cujas
  versões podem começar todas em Draft — fica registrado como decisão
  em docs/domain-decisions.md, não implementado nesta sprint.
- **no máximo uma ProposalVersion com status ACTIVE simultaneamente**
  — invariante que atravessa o Aggregate inteiro (não uma única
  versão): duas versões "correntes" ao mesmo tempo seriam ambíguas.

Observações: nenhum método de "aprovar", "cancelar" ou "criar nova
versão" existe nesta etapa — são comportamentos de domínio (Sprint
1B+/regra comercial) que vão orquestrar as regras de
docs/proposal-actions.md e docs/proposal-status.md.
"""

from dataclasses import dataclass, field
from typing import List

from src.domain.proposal.enums import ProposalStatus, ProposalVersionStatus
from src.domain.proposal.proposal_version import ProposalVersion
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.exceptions import InvariantViolationError
from src.domain.shared.guards import require_instance, require_non_empty_collection


@dataclass
class Proposal(BaseEntity):
    status: ProposalStatus
    versions: List[ProposalVersion] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        require_instance(self.status, ProposalStatus, f"Proposal.status inválido: {self.status!r}")
        require_non_empty_collection(self.versions, "Proposal requer ao menos uma ProposalVersion.")
        active_versions = [v for v in self.versions if v.status == ProposalVersionStatus.ACTIVE]
        if len(active_versions) > 1:
            raise InvariantViolationError(
                f"Proposal não pode ter mais de uma ProposalVersion ACTIVE simultaneamente "
                f"(encontradas {len(active_versions)})."
            )
