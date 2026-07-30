"""Service — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa um Serviço da Viagem que não é Voo nem
Hospedagem (traslado, passeio, seguro, aluguel de carro).

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier` por
id.

Observações: `is_optional` é um atributo simples de forma, não uma
regra de Upsell/Cross-sell (docs/business-rules.md) — a lógica de
quando sugerir/precificar um serviço opcional é Sprint 1B.
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.identifier import Identifier


@dataclass
class Service(BaseEntity):
    supplier_id: Identifier
    description: str
    is_optional: bool = False
