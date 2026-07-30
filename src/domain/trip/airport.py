"""Aeroporto — Value Object usado por `Flight`.

Sprint 1A: apenas código, nome e cidade, como texto livre. A etapa de
Normalização (docs/ARCHITECTURE.md, seção 3) — que garante que "GRU",
"Guarulhos" e "Aeroporto de Guarulhos" cheguem sempre como uma única
representação canônica — é comportamento, portanto Sprint 1B ou além,
não faz parte desta Entidade/VO em si.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Airport(ValueObject):
    code: str
    name: str
    city: str
