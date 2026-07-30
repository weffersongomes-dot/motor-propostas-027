"""Service — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa um Serviço da Viagem que não é Voo nem
Hospedagem (traslado, passeio, seguro, aluguel de carro).

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier` por
id.

Invariantes (Sprint 1B): `supplier_id` válido; `description` não
vazia.

Observações: `is_optional` é um atributo simples de forma, não uma
regra de Upsell/Cross-sell (docs/business-rules.md) — a lógica de
quando sugerir/precificar um serviço opcional é Sprint 1B+ (quando as
regras comerciais existirem oficialmente).
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.guards import require_identifier, require_non_empty_str
from src.domain.shared.identifier import Identifier


@dataclass
class Service(BaseEntity):
    supplier_id: Identifier
    description: str
    is_optional: bool = False

    def __post_init__(self) -> None:
        super().__post_init__()
        require_identifier(self.supplier_id, "Service.supplier_id requer um Identifier válido.")
        require_non_empty_str(self.description, "Service.description não pode ser vazia.")
