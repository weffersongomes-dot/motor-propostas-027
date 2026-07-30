"""Número de documento de identificação (CPF, CNPJ, Passaporte...) — Value Object.

Sprint 1A: `type` é texto livre (ex: "CPF", "CNPJ", "Passaporte"), não
um enum — restringir os valores possíveis é Sprint 1B.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class DocumentNumber(ValueObject):
    type: str
    value: str
