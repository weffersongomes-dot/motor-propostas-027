"""Financial — Value Object.

Responsabilidade: representa o Financeiro (ver docs/glossary.md) — os
valores, forma de pagamento e parcelamento de uma ProposalVersion.

Invariantes (Sprint 1B): `total` presente; `installments` inteiro
positivo (>= 1) — sanidade numérica estrutural, não limite comercial de
parcelamento (isso é `docs/business-rules.md`, seção Parcelamentos,
ainda pendente).

Observações: `payment_method` permanece texto livre de propósito —
**não** vira enum nesta sprint, porque as formas de pagamento aceitas
pela 027 são uma Regra Comercial ainda 100% pendente (ver
docs/business-rules.md, "Regras de pagamento") — transformar isso em
enum antes da confirmação violaria a ordem de implementação desta
sprint (Regras Comerciais só quando existirem oficialmente).
"""

from dataclasses import dataclass

from src.domain.shared.exceptions import StructuralValidationError
from src.domain.shared.guards import require_instance
from src.domain.shared.money import Money
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Financial(ValueObject):
    total: Money
    payment_method: str
    installments: int

    def __post_init__(self) -> None:
        require_instance(self.total, Money, "Financial.total é obrigatório.")
        if not isinstance(self.installments, int) or self.installments < 1:
            raise StructuralValidationError(
                f"Financial.installments deve ser um inteiro >= 1, recebeu {self.installments!r}."
            )
