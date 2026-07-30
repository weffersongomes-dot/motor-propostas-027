"""Funções de guarda reutilizáveis para invariantes e validações estruturais.

Existem para que cada Entidade/Value Object não reimplemente a mesma
checagem (ex: "string não vazia") com uma mensagem de erro diferente a
cada vez — mantém `__post_init__` legível e as mensagens consistentes
entre todo o domínio (ver docs/decisoes/0008-sprint-1b-invariantes-e-validacoes.md).

Guards que representam a forma de um valor isolado levantam
`StructuralValidationError`. Guards que representam uma regra sobre a
consistência de um Aggregate (ex: "no máximo uma versão Active")
levantam `InvariantViolationError` — a escolha de qual usar é feita por
quem chama, não por esta função.
"""

from typing import Any, Iterable, Type

from src.domain.shared.exceptions import InvariantViolationError, StructuralValidationError
from src.domain.shared.identifier import Identifier


def require(condition: bool, message: str, *, invariant: bool = False) -> None:
    if not condition:
        raise (InvariantViolationError if invariant else StructuralValidationError)(message)


def require_not_none(value: Any, message: str, *, invariant: bool = False) -> None:
    require(value is not None, message, invariant=invariant)


def require_instance(value: Any, expected_type: Type, message: str) -> None:
    require(isinstance(value, expected_type), message)


def require_non_empty_str(value: Any, message: str) -> None:
    require(isinstance(value, str) and value.strip() != "", message)


def require_identifier(value: Any, message: str) -> None:
    require_instance(value, Identifier, message)


def require_non_empty_collection(value: Iterable, message: str, *, invariant: bool = True) -> None:
    require(value is not None and len(list(value)) > 0, message, invariant=invariant)
