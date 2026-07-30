"""Número de telefone — Value Object.

Sprint 1B: `type` (PhoneType — móvel, fixo, WhatsApp) formalizado como
enum estrutural; `value` validado por formato básico (dígitos, e
opcionalmente espaços, hífen, parênteses e um "+" inicial) — sem exigir
DDI/DDD específico, isso é infraestrutura/regra de negócio.
"""

import re
from dataclasses import dataclass

from src.domain.shared.enums import PhoneType
from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.guards import require_instance
from src.domain.shared.value_object import ValueObject

_BASIC_PHONE_FORMAT = re.compile(r"^\+?[\d\s().-]{6,}$")


@dataclass(frozen=True)
class Phone(ValueObject):
    type: PhoneType
    value: str

    def __post_init__(self) -> None:
        require_instance(self.type, PhoneType, f"Phone.type inválido: {self.type!r}")
        if not isinstance(self.value, str) or not _BASIC_PHONE_FORMAT.match(self.value):
            raise StructuralValidationError(f"Phone com formato inválido: {self.value!r}")
