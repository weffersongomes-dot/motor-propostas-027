"""Aeroporto — Value Object usado por `Flight`.

Sprint 1B: `type` (`AirportType`) formalizado como enum estrutural;
`code`/`name`/`city` validados como não vazios. A etapa de Normalização
(docs/ARCHITECTURE.md, seção 3) — que garante que "GRU", "Guarulhos" e
"Aeroporto de Guarulhos" cheguem sempre como uma única representação
canônica — continua sendo comportamento de uma camada futura, não
desta Entidade/VO.
"""

from dataclasses import dataclass

from src.domain.shared.guards import require_instance, require_non_empty_str
from src.domain.shared.value_object import ValueObject
from src.domain.trip.enums import AirportType


@dataclass(frozen=True)
class Airport(ValueObject):
    code: str
    name: str
    city: str
    type: AirportType

    def __post_init__(self) -> None:
        require_non_empty_str(self.code, "Airport.code não pode ser vazio.")
        require_non_empty_str(self.name, "Airport.name não pode ser vazio.")
        require_non_empty_str(self.city, "Airport.city não pode ser vazio.")
        require_instance(self.type, AirportType, f"Airport.type inválido: {self.type!r}")
