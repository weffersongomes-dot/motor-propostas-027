"""ProposalClassification — Value Object.

Representa as quatro dimensões combináveis de docs/proposal-types.md
(Destino, Formato, Finalidade, Produto — nomeadas estruturalmente por
`ProposalDimension`, ver enums.py). Mantido como quatro campos
explícitos (em vez de um `Dict[ProposalDimension, Tuple[str, ...]]`)
por legibilidade e segurança de tipo — são exatamente quatro dimensões,
fixas, confirmadas na Sprint 0.5/ADR 0005; um dicionário genérico só
compensaria se o número de dimensões fosse variável (ver
docs/domain-decisions.md).

Sprint 1B: cada dimensão continua sendo uma tupla de texto livre —
nenhum enum de valores (Nacional/Internacional etc.) ainda, porque
esses valores dependem do Workshop 3 (docs/discovery-workshop.md), não
confirmado. Validação estrutural aqui se limita a garantir que cada
dimensão é de fato uma tupla (imutável, coerente com o VO).
"""

from dataclasses import dataclass
from typing import Tuple

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class ProposalClassification(ValueObject):
    destinations: Tuple[str, ...]
    formats: Tuple[str, ...]
    purposes: Tuple[str, ...]
    products: Tuple[str, ...]

    def __post_init__(self) -> None:
        for field_name in ("destinations", "formats", "purposes", "products"):
            value = getattr(self, field_name)
            if not isinstance(value, tuple):
                raise StructuralValidationError(
                    f"ProposalClassification.{field_name} deve ser uma tupla, recebeu {type(value).__name__}."
                )
