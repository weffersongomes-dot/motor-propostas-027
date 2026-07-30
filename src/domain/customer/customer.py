"""Customer — Aggregate Root.

Responsabilidade: representa o Cliente (ver docs/glossary.md) — pessoa
ou empresa que contrata a viagem, podendo ou não coincidir com os
Passageiros.

Atributos iniciais: nome, documento, e-mail, telefone, endereço
(opcional) e a lista de Passageiros cadastrados por este cliente.

Relacionamentos: agrega `Passenger`. Referenciado por
`ProposalVersion.customer_id`.

Invariantes (Sprint 1B):
- possui identidade única — garantido por `BaseEntity` (Identifier
  válido); unicidade *global* (não existir outro Customer com o mesmo
  id no sistema) é responsabilidade de um repositório, que não existe
  nesta sprint (ver docs/domain-decisions.md).
- `name`/`document_number`/`email`/`phone` obrigatórios.
- **pode existir sem propostas** — não há, e não deve haver, nenhuma
  checagem aqui exigindo que o Customer esteja associado a uma
  Proposal; é o próprio Aggregate Proposal que referencia Customer, não
  o contrário.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from src.domain.customer.passenger import Passenger
from src.domain.shared.address import Address
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.email import Email
from src.domain.shared.guards import require_instance, require_non_empty_str
from src.domain.shared.phone import Phone


@dataclass
class Customer(BaseEntity):
    name: str
    document_number: DocumentNumber
    email: Email
    phone: Phone
    address: Optional[Address] = None
    passengers: List[Passenger] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.name, "Customer.name não pode ser vazio.")
        require_instance(self.document_number, DocumentNumber, "Customer.document_number é obrigatório.")
        require_instance(self.email, Email, "Customer.email é obrigatório.")
        require_instance(self.phone, Phone, "Customer.phone é obrigatório.")
