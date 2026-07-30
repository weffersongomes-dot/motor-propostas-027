"""Consultant — Entidade filha do Aggregate `Company`.

Responsabilidade: representa o colaborador (Consultor, ver
docs/glossary.md) que atende o Cliente e conduz a Proposta.

Relacionamentos: pertence a uma `Company`; referenciado por
`ProposalVersion.consultant_id` e por `Metadata.consultant_id`.

Invariantes (Sprint 1B): `name` não vazio; `email`/`phone` presentes
(cada um valida seu próprio formato).

Observações: por ora existe um único papel "Consultor" — se a 027
distingue outros papéis (vendedor, agente) é uma pergunta aberta do
Workshop 1 (docs/discovery-workshop.md).
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.email import Email
from src.domain.shared.guards import require_instance, require_non_empty_str
from src.domain.shared.phone import Phone


@dataclass
class Consultant(BaseEntity):
    name: str
    email: Email
    phone: Phone

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.name, "Consultant.name não pode ser vazio.")
        require_instance(self.email, Email, "Consultant.email é obrigatório.")
        require_instance(self.phone, Phone, "Consultant.phone é obrigatório.")
