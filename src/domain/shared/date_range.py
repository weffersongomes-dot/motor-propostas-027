"""Intervalo entre duas datas — Value Object.

Usado por Trip (datas da viagem) e Accommodation (check-in/check-out).
Sprint 1B: `end` deve ser igual ou posterior a `start` — é uma
invariante estrutural do próprio conceito de intervalo (um intervalo
"invertido" não representa nada), não uma regra de negócio.
"""

from dataclasses import dataclass
from datetime import date

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class DateRange(ValueObject):
    start: date
    end: date

    def __post_init__(self) -> None:
        if self.end < self.start:
            raise StructuralValidationError(
                f"DateRange inválido: end ({self.end}) é anterior a start ({self.start})."
            )
