"""Endereço postal — Value Object.

Sprint 1A: apenas os campos que compõem um endereço. Nenhum campo é
tratado como opcional/obrigatório aqui — essa decisão (ex: complemento
pode faltar, país pode ter default "Brasil") é Sprint 1B.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Address(ValueObject):
    street: str
    number: str
    complement: str
    neighborhood: str
    city: str
    state: str
    country: str
    postal_code: str
