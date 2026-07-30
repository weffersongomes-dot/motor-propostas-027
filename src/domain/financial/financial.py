"""Financial — Value Object.

Responsabilidade: representa o Financeiro (ver docs/glossary.md) — os
valores, forma de pagamento e parcelamento de uma ProposalVersion.

Observações: modelado como Value Object, não Entidade — dado o mesmo
total, forma de pagamento e parcelas, dois blocos financeiros
representam a mesma condição comercial; não têm identidade própria
independente da ProposalVersion a que pertencem (ver
docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md). `payment_method`
é texto livre nesta etapa — vira enum na Sprint 1B, com base nas
Regras Financeiras (docs/business-rules.md).
"""

from dataclasses import dataclass

from src.domain.shared.money import Money
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Financial(ValueObject):
    total: Money
    payment_method: str
    installments: int
