"""Quantia monetária associada a uma moeda — Value Object.

Sprint 1B: `currency` formalizado como enum estrutural `Currency`
(conjunto pequeno e deliberadamente incompleto — ver enums.py).
`amount` deve ser um `Decimal` (consistência de tipo); nenhum limite de
sinal é imposto — um valor negativo pode representar um crédito/estorno
legítimo, e restringir isso seria uma regra de negócio, não estrutural.
"""

from dataclasses import dataclass
from decimal import Decimal

from src.domain.shared.enums import Currency
from src.domain.shared.guards import require_instance
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Money(ValueObject):
    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        require_instance(self.amount, Decimal, f"Money.amount deve ser Decimal, recebeu {type(self.amount).__name__}.")
        require_instance(self.currency, Currency, f"Money.currency inválido: {self.currency!r}")
