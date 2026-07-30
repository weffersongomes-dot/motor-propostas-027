"""Base para Value Objects: sem identidade própria, imutáveis, comparados por valor.

Toda subclasse deve ser declarada como `@dataclass(frozen=True)` — é o
`frozen=True` que dá a imutabilidade e a igualdade por valor (campo a
campo), não esta classe base em si.
"""

from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject(ABC):
    """Marcador para Value Objects do domínio. Sem atributos próprios."""
