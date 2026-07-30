"""Base para Entidades: têm identidade própria, mutáveis, comparadas pelo `id`.

Diferente de um Value Object, duas instâncias de Entidade com os mesmos
atributos mas `id`s diferentes NÃO são iguais — e duas instâncias com o
mesmo `id` são consideradas a mesma entidade mesmo que outros atributos
divirjam (ex: uma versão em memória desatualizada). Essa é a semântica
de identidade do DDD, implementada aqui via `__eq__`/`__hash__`.
"""

from abc import ABC
from dataclasses import dataclass

from src.domain.shared.identifier import Identifier


@dataclass
class BaseEntity(ABC):
    id: Identifier

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
