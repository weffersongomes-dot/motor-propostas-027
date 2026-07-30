"""Identificador único de uma Entidade — Value Object.

Sprint 1B: validação estrutural mínima (não vazio). Nenhuma regra de
formato específico (ex: exigir UUID) é imposta — isso seria decisão de
infraestrutura/aplicação, não do domínio.

Não usa `src/domain/shared/guards.py` de propósito: guards.py depende
de `Identifier` para `require_identifier`, então `Identifier` valida a
si mesmo diretamente para evitar import circular.
"""

from dataclasses import dataclass

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Identifier(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or self.value.strip() == "":
            raise StructuralValidationError("Identifier requer um 'value' não vazio.")
