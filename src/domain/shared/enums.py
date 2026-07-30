"""Enums estruturais compartilhados entre Bounded Contexts.

Apenas classificações universais do domínio (não regras comerciais da
027 Viagens) — ver docs/decisoes/0008-sprint-1b-invariantes-e-validacoes.md
sobre o critério usado para decidir o que vira enum nesta sprint.

`Currency` usa um conjunto pequeno e deliberadamente não-exaustivo
(diferente de um país/idioma, uma agência de viagens lida com poucas
moedas na prática) — `OTHER` é a válvula de escape até o Sprint 1B+
confirmar quais moedas a 027 realmente opera.
"""

from enum import Enum


class DocumentType(Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"
    PASSPORT = "PASSPORT"
    RG = "RG"
    OTHER = "OTHER"


class PhoneType(Enum):
    MOBILE = "MOBILE"
    LANDLINE = "LANDLINE"
    WHATSAPP = "WHATSAPP"
    OTHER = "OTHER"


class Currency(Enum):
    BRL = "BRL"
    USD = "USD"
    EUR = "EUR"
    OTHER = "OTHER"
