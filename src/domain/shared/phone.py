"""Número de telefone — Value Object.

Sprint 1A: apenas o valor de texto, sem formatação/DDI/validação —
isso é Sprint 1B.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Phone(ValueObject):
    value: str
