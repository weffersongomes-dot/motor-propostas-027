"""Enums estruturais do contexto Operações (Trip).

`AirportType` classifica um aeroporto como doméstico ou internacional
— fato estrutural sobre o aeroporto em si, não uma política comercial.
"""

from enum import Enum


class AirportType(Enum):
    DOMESTIC = "DOMESTIC"
    INTERNATIONAL = "INTERNATIONAL"
