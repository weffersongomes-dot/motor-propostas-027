"""Flight — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa o Voo (ver docs/glossary.md) — um trecho
aéreo da Viagem.

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier`
(companhia aérea) por id, nunca por objeto embutido.

Observações: nenhuma verificação de que `arrival_at` seja posterior a
`departure_at` nesta etapa.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.identifier import Identifier
from src.domain.trip.airport import Airport


@dataclass
class Flight(BaseEntity):
    supplier_id: Identifier
    origin: Airport
    destination: Airport
    departure_at: datetime
    arrival_at: datetime
