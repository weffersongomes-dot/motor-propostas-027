"""Intervalo entre duas datas — Value Object.

Usado por Trip (datas da viagem) e Accommodation (check-in/check-out).
Sprint 1A: nenhuma verificação de que `end` seja posterior a `start` —
isso é uma regra de negócio, portanto Sprint 1B.
"""

from dataclasses import dataclass
from datetime import date

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class DateRange(ValueObject):
    start: date
    end: date
