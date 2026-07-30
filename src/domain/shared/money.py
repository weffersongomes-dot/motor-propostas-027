"""Quantia monetária associada a uma moeda — Value Object.

Sprint 1A: apenas a forma (quantia + moeda). Regras de arredondamento,
conversão de câmbio ou operações aritméticas (somar, multiplicar) são
comportamento de domínio e ficam para a Sprint 1B, quando as Regras
Financeiras (docs/business-rules.md) estiverem confirmadas.
"""

from dataclasses import dataclass
from decimal import Decimal

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Money(ValueObject):
    amount: Decimal
    currency: str
