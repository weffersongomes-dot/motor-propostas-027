"""Enums estruturais do contexto Cadastro (Supplier).

`SupplierCategory` classifica o tipo de parceiro — categorias
universais do setor de turismo (toda agência lida com companhias
aéreas, hotéis, operadoras, seguradoras), não uma política comercial
específica da 027. Extensão além do exemplo literal do briefing da
Sprint 1B, mas já prometida no docstring de `supplier.py` desde a
Sprint 1A — ver docs/decisoes/0008-sprint-1b-invariantes-e-validacoes.md.
"""

from enum import Enum


class SupplierCategory(Enum):
    AIRLINE = "AIRLINE"
    HOTEL = "HOTEL"
    OPERATOR = "OPERATOR"
    INSURER = "INSURER"
    OTHER = "OTHER"
