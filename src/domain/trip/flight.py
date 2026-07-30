"""Flight — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa o Voo (ver docs/glossary.md) — um trecho
aéreo da Viagem.

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier`
(companhia aérea) por id, nunca por objeto embutido.

Invariantes (Sprint 1B): `supplier_id` válido; `origin`/`destination`
presentes; `arrival_at` posterior a `departure_at` — mesma lógica
estrutural de `DateRange`, aplicada aqui porque Flight usa dois
`datetime` soltos em vez de um `DateRange` (voo tem hora, não só data).
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.guards import require_identifier, require_instance
from src.domain.shared.identifier import Identifier
from src.domain.trip.airport import Airport


@dataclass
class Flight(BaseEntity):
    supplier_id: Identifier
    origin: Airport
    destination: Airport
    departure_at: datetime
    arrival_at: datetime

    def __post_init__(self) -> None:
        super().__post_init__()
        require_identifier(self.supplier_id, "Flight.supplier_id requer um Identifier válido.")
        require_instance(self.origin, Airport, "Flight.origin é obrigatório.")
        require_instance(self.destination, Airport, "Flight.destination é obrigatório.")
        if self.arrival_at < self.departure_at:
            raise StructuralValidationError(
                f"Flight inválido: arrival_at ({self.arrival_at}) é anterior a departure_at ({self.departure_at})."
            )
