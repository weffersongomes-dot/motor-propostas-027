"""Trip — Aggregate Root.

Responsabilidade: representa a Viagem (ver docs/glossary.md) — destino,
datas e os componentes concretos (Flight, Accommodation, Service) que
a compõem.

Relacionamentos: agrega `Flight`, `Accommodation` e `Service`.
Referenciada por `ProposalVersion.trip_id`.

Observações: modelada como Aggregate Root independente de `Proposal`
porque uma Viagem continua existindo (o passageiro efetivamente viaja)
mesmo depois de o ciclo comercial da Proposta terminar — módulos
futuros de Operações (Emissão, Itinerário, ver
docs/bounded-context-map.md) devem poder referenciar a Trip sem
depender da Proposal que a originou. `destination` aqui é texto livre;
a classificação formal por dimensões (Destino/Formato/Finalidade/
Produto) vive em `ProposalClassification`, não nesta entidade.
"""

from dataclasses import dataclass, field
from typing import List

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.date_range import DateRange
from src.domain.trip.accommodation import Accommodation
from src.domain.trip.flight import Flight
from src.domain.trip.service import Service


@dataclass
class Trip(BaseEntity):
    destination: str
    date_range: DateRange
    flights: List[Flight] = field(default_factory=list)
    accommodations: List[Accommodation] = field(default_factory=list)
    services: List[Service] = field(default_factory=list)
