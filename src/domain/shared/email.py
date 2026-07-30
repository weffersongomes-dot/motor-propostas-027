"""Endereço de e-mail — Value Object.

Sprint 1A: apenas o valor de texto. Validação de formato é Sprint 1B.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Email(ValueObject):
    value: str
