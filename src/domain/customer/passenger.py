"""Passenger — Entidade filha do Aggregate `Customer`.

Responsabilidade: representa o Passageiro (ver docs/glossary.md) —
pessoa que efetivamente viaja, associada a uma Trip através da
Proposal.

Relacionamentos: pertence a um `Customer`. Pode ou não ser a mesma
pessoa que o `Customer` (ex: cliente corporativo cotando para
terceiros) — questão em aberto, ver docs/proposal-types.md (Finalidade
= Corporativo/Incentivo).

Observações: nenhuma validação de idade/documento nesta etapa.
"""

from dataclasses import dataclass
from datetime import date

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.document_number import DocumentNumber


@dataclass
class Passenger(BaseEntity):
    name: str
    document_number: DocumentNumber
    birth_date: date
