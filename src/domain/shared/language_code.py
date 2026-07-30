"""Idioma — Value Object, validado por formato (mesma lógica de CountryCode).

Preparado para uso futuro (ex: idioma preferido de um Customer em
Notification Engine/Customer Portal) — nenhuma Entidade usa este VO
ainda nesta sprint, ver docs/domain-decisions.md.
"""

import re
from dataclasses import dataclass

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject

_ISO_639_1 = re.compile(r"^[a-z]{2}$")


@dataclass(frozen=True)
class LanguageCode(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not _ISO_639_1.match(self.value):
            raise StructuralValidationError(
                f"LanguageCode inválido: {self.value!r} — esperado código ISO 639-1 (ex: 'pt')."
            )
