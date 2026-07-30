"""Endereço de e-mail — Value Object.

Sprint 1B: validação de formato *básico* (contém "@" e um "." depois
dele) — não é uma validação RFC 5322 completa, é uma checagem
estrutural mínima de forma, não uma regra de negócio.
"""

import re
from dataclasses import dataclass

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject

_BASIC_EMAIL_FORMAT = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True)
class Email(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not _BASIC_EMAIL_FORMAT.match(self.value):
            raise StructuralValidationError(f"Email com formato inválido: {self.value!r}")
