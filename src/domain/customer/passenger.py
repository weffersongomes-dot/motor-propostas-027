"""Passenger — Entidade filha do Aggregate `Customer`.

Responsabilidade: representa o Passageiro (ver docs/glossary.md) —
pessoa que efetivamente viaja. Pertence ao `Customer` que o cadastrou;
é referenciado (por id) pela `Trip` em que efetivamente viaja — ver
docs/domain-decisions.md sobre por que "pertencer" (Customer) e
"viajar em" (Trip) são relações diferentes.

Invariantes (Sprint 1B): `name` não vazio; `document_number` presente;
`birth_date` presente; `passenger_type` presente e válido.

Observações: nenhuma verificação de que `passenger_type` seja
consistente com `birth_date` (ex: alguém com 40 anos marcado como
INFANT) — isso cruzaria dado estrutural com regra de negócio, fora do
escopo desta sprint.
"""

from dataclasses import dataclass
from datetime import date

from src.domain.customer.enums import PassengerType
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.guards import require_instance, require_non_empty_str, require_not_none


@dataclass
class Passenger(BaseEntity):
    name: str
    document_number: DocumentNumber
    birth_date: date
    passenger_type: PassengerType

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.name, "Passenger.name não pode ser vazio.")
        require_instance(self.document_number, DocumentNumber, "Passenger.document_number é obrigatório.")
        require_not_none(self.birth_date, "Passenger.birth_date é obrigatório.")
        require_instance(self.passenger_type, PassengerType, f"Passenger.passenger_type inválido: {self.passenger_type!r}")
