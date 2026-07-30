"""Accommodation — Entidade filha do Aggregate `Trip`.

Responsabilidade: representa a Hospedagem (ver docs/glossary.md) —
hotel/acomodação da Viagem.

Relacionamentos: pertence a uma `Trip`; referencia um `Supplier`
(hotel/operadora) por id.

Observações: para Produto = Cruzeiro (docs/proposal-types.md), esta
entidade pode precisar de uma variação/sinônimo "Cabine" — ver
docs/glossary.md, ainda em rascunho.
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.date_range import DateRange
from src.domain.shared.identifier import Identifier


@dataclass
class Accommodation(BaseEntity):
    supplier_id: Identifier
    name: str
    category: str
    date_range: DateRange
