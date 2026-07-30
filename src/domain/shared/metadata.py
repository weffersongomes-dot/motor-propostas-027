"""Metadata obrigatória de toda Proposta/Documento — Value Object.

Espelha o bloco de metadata definido em docs/universal-proposal-model.md
(campos: schema_version, engine_version, template, generated_at,
generated_by, consultor, origem, status). Modelada como Value Object,
não Entidade: dois blocos de metadata com os mesmos valores representam
a mesma informação de rastreabilidade — não têm identidade própria
distinta do que carregam.

Sprint 1B — revisão de Shared Kernel: o campo que em `universal-proposal-model.md`
e na Sprint 1A se chamava `proposal_id` foi renomeado para `subject_id`.
Justificativa: um campo chamado `proposal_id` dentro de um Value Object
pensado para ser reutilizado por *todos* os módulos futuros (Contratos,
Vouchers...) é contaminação do Shared Kernel com vocabulário específico
do módulo Propostas — ver docs/domain-decisions.md. `subject_id` é o id
do que quer que esta metadata descreva, qualquer que seja o módulo.

`status` permanece texto livre de propósito — módulos diferentes terão
vocabulários de status diferentes; o estado estrutural *tipado* de uma
Proposta vive em `ProposalVersion.status` (ver
src/domain/proposal/proposal_version.py e docs/domain-decisions.md),
não aqui.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.shared.guards import require_identifier, require_non_empty_str, require_not_none
from src.domain.shared.identifier import Identifier
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Metadata(ValueObject):
    subject_id: Identifier
    schema_version: str
    engine_version: str
    template: str
    generated_at: datetime
    generated_by: str
    consultant_id: Identifier
    origin: str
    status: str

    def __post_init__(self) -> None:
        require_identifier(self.subject_id, "Metadata.subject_id requer um Identifier válido.")
        require_identifier(self.consultant_id, "Metadata.consultant_id requer um Identifier válido.")
        require_non_empty_str(self.schema_version, "Metadata.schema_version não pode ser vazio.")
        require_non_empty_str(self.engine_version, "Metadata.engine_version não pode ser vazio.")
        require_non_empty_str(self.template, "Metadata.template não pode ser vazio.")
        require_non_empty_str(self.generated_by, "Metadata.generated_by não pode ser vazio.")
        require_non_empty_str(self.origin, "Metadata.origin não pode ser vazio.")
        require_non_empty_str(self.status, "Metadata.status não pode ser vazio.")
        require_not_none(self.generated_at, "Metadata.generated_at é obrigatório.")
