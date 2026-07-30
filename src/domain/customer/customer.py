"""Customer — Aggregate Root.

Responsabilidade: representa o Cliente (ver docs/glossary.md) — pessoa
ou empresa que contrata a viagem, podendo ou não coincidir com os
Passageiros.

Atributos iniciais: nome, documento, e-mail, telefone, endereço
(opcional) e a lista de Passageiros associados a este cliente.

Relacionamentos: agrega `Passenger`. Referenciado por
`ProposalVersion.customer_id`.

Observações: modelado como Aggregate Root porque um Cliente tem
existência e ciclo de vida independentes de qualquer Proposta
específica (o mesmo cliente pode gerar várias propostas ao longo do
tempo) — ver docs/domain-map.md.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from src.domain.customer.passenger import Passenger
from src.domain.shared.address import Address
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.email import Email
from src.domain.shared.phone import Phone


@dataclass
class Customer(BaseEntity):
    name: str
    document_number: DocumentNumber
    email: Email
    phone: Phone
    address: Optional[Address] = None
    passengers: List[Passenger] = field(default_factory=list)
