"""Consultant — Entidade filha do Aggregate `Company`.

Responsabilidade: representa o colaborador (Consultor, ver
docs/glossary.md) que atende o Cliente e conduz a Proposta.

Relacionamentos: pertence a uma `Company`; referenciado por
`ProposalVersion.consultant_id` e por `Metadata.consultant_id`.

Observações: por ora existe um único papel "Consultor" — se a 027
distingue outros papéis (vendedor, agente) é uma pergunta aberta do
Workshop 1 (docs/discovery-workshop.md).
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.email import Email
from src.domain.shared.phone import Phone


@dataclass
class Consultant(BaseEntity):
    name: str
    email: Email
    phone: Phone
