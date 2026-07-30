"""Trip — Aggregate Root.

Responsabilidade: representa a Viagem (ver docs/glossary.md) — destino,
datas, os passageiros que efetivamente viajam, e os componentes
concretos (Flight, Accommodation, Service) que a compõem.

Relacionamentos: agrega `Flight`, `Accommodation` e `Service`.
Referenciada por `ProposalVersion.trip_id`. Referencia `Passenger` por
id (`passenger_ids`) — não os possui: `Passenger` continua pertencendo
ao Aggregate `Customer` (ver docs/domain-decisions.md, "Passenger
pertence ao Customer ou à Trip?").

Invariantes (Sprint 1B):
- `destination` não vazio; `date_range` presente.
- **possui ao menos um Passageiro** (`passenger_ids` não vazio) — do
  exemplo do briefing, implementado via referência, não posse.
- **NÃO implementa** "sempre pertence a uma Proposal" — decisão
  deliberada, documentada em docs/domain-decisions.md: Trip é Aggregate
  Root independente (ver ADR 0006) justamente para poder existir além
  do ciclo comercial da Proposal que a originou (módulos futuros de
  Operações vão referenciar a Trip diretamente).

`destination` aqui é texto livre; a classificação formal por dimensões
(Destino/Formato/Finalidade/Produto) vive em `ProposalClassification`,
não nesta entidade.
"""

from dataclasses import dataclass, field
from typing import List

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.date_range import DateRange
from src.domain.shared.guards import require_instance, require_non_empty_collection, require_non_empty_str
from src.domain.shared.identifier import Identifier
from src.domain.trip.accommodation import Accommodation
from src.domain.trip.flight import Flight
from src.domain.trip.service import Service


@dataclass
class Trip(BaseEntity):
    destination: str
    date_range: DateRange
    passenger_ids: List[Identifier] = field(default_factory=list)
    flights: List[Flight] = field(default_factory=list)
    accommodations: List[Accommodation] = field(default_factory=list)
    services: List[Service] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.destination, "Trip.destination não pode ser vazio.")
        require_instance(self.date_range, DateRange, "Trip.date_range é obrigatório.")
        require_non_empty_collection(self.passenger_ids, "Trip requer ao menos um Passageiro (passenger_ids).")
