"""País — Value Object, validado por formato, não por enum fechado.

Decisão deliberada (ver docs/domain-decisions.md): país é uma lista de
referência grande (~190 valores) e mutável ao longo do tempo — um Enum
Python fechado ficaria desatualizado e exigiria alterar código para um
caso que não é uma regra de negócio, é só um dado de referência. Em vez
disso, valida-se apenas a *forma* (código ISO 3166-1 alpha-2: duas
letras maiúsculas), igual a um Value Object comum.
"""

import re
from dataclasses import dataclass

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject

_ISO_3166_ALPHA_2 = re.compile(r"^[A-Z]{2}$")


@dataclass(frozen=True)
class CountryCode(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not _ISO_3166_ALPHA_2.match(self.value):
            raise StructuralValidationError(
                f"CountryCode inválido: {self.value!r} — esperado código ISO 3166-1 alpha-2 (ex: 'BR')."
            )
