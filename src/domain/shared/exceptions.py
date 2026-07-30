"""Exceções de domínio — a única forma de sinalizar inconsistência estrutural.

Duas categorias, propositalmente distintas:

- `InvariantViolationError` — uma invariante de um Aggregate foi violada
  (ex: Proposal com mais de uma ProposalVersion Active ao mesmo tempo).
- `StructuralValidationError` — um valor não atende ao formato/forma
  mínima esperada (ex: Identifier vazio, DateRange com fim antes do
  início).

Nenhuma das duas representa uma regra comercial da 027 Viagens — isso é
Sprint 1B "quando as regras existirem oficialmente" (ver
docs/business-rules.md) ou além.
"""


class DomainError(Exception):
    """Base para todo erro levantado pela camada de domínio."""


class InvariantViolationError(DomainError):
    """Uma invariante estrutural de um Aggregate Root foi violada."""


class StructuralValidationError(DomainError):
    """Um valor não atende ao formato estrutural mínimo esperado."""
