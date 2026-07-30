"""Identificador único de uma Entidade — Value Object.

Sprint 1A: apenas um invólucro (wrapper) sobre um valor de texto.
Nenhuma regra de geração/formato (ex: exigir UUID) é imposta aqui —
isso é uma decisão de infraestrutura/aplicação para uma sprint futura.
"""

from dataclasses import dataclass

from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Identifier(ValueObject):
    value: str
