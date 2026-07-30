"""ProposalClassification — Value Object.

Não faz parte da lista de exemplos original da Sprint 1A, mas é
necessário para representar fielmente docs/proposal-types.md: uma
Proposta não tem um "tipo" único, e sim quatro dimensões
independentes e combináveis (Destino, Formato, Finalidade, Produto).
Esta decisão de modelagem está registrada em
docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md.

Sprint 1A: cada dimensão é uma tupla de texto livre (nenhum enum ainda
— os valores possíveis de cada dimensão só são restringidos na Sprint
1B, com base no que for confirmado no Workshop 3 de
docs/discovery-workshop.md).
"""

from dataclasses import dataclass
from typing import Tuple

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class ProposalClassification(ValueObject):
    destinations: Tuple[str, ...]
    formats: Tuple[str, ...]
    purposes: Tuple[str, ...]
    products: Tuple[str, ...]
