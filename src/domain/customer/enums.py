"""Enums estruturais do contexto Cadastro/Comercial (Customer).

`PassengerType` classifica o passageiro por faixa etária estrutural
(adulto/criança/bebê) — uma categoria universal do setor de viagens,
não uma política comercial específica da 027 (que ainda não definiu,
por exemplo, regras de desconto por faixa etária — isso é Regra
Comercial, ver docs/business-rules.md).
"""

from enum import Enum


class PassengerType(Enum):
    ADULT = "ADULT"
    CHILD = "CHILD"
    INFANT = "INFANT"
