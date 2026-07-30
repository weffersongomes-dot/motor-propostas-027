"""Accommodation — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa a Hospedagem (ver docs/glossary.md) —
hotel/acomodação da Viagem.

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier`
(hotel/operadora) por id.

Invariantes (Sprint 1B): `supplier_id` válido; `name`/`category` não
vazios; `date_range` presente (valida `end >= start` sozinho).

Observações: para Produto = Cruzeiro (docs/proposal-types.md), esta
entidade pode precisar de uma variação/sinônimo "Cabine" — ver
docs/glossary.md, ainda em rascunho.
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.date_range import DateRange
from src.domain.shared.guards import require_identifier, require_instance, require_non_empty_str
from src.domain.shared.identifier import Identifier


@dataclass
class Accommodation(BaseEntity):
    supplier_id: Identifier
    name: str
    category: str
    date_range: DateRange

    def __post_init__(self) -> None:
        super().__post_init__()
        require_identifier(self.supplier_id, "Accommodation.supplier_id requer um Identifier válido.")
        require_non_empty_str(self.name, "Accommodation.name não pode ser vazio.")
        require_non_empty_str(self.category, "Accommodation.category não pode ser vazio.")
        require_instance(self.date_range, DateRange, "Accommodation.date_range é obrigatório.")
