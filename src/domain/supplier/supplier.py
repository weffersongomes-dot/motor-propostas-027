"""Supplier — Aggregate Root.

Responsabilidade: representa o Fornecedor (ver docs/glossary.md) —
empresa parceira que presta um serviço concreto da viagem.

Atributos iniciais: nome, categoria (`SupplierCategory`, enum
estrutural desde a Sprint 1B), e-mail, telefone.

Relacionamentos: referenciado por `Flight.supplier_id`,
`Accommodation.supplier_id` e `Service.supplier_id` — nunca aninhado
dentro deles, porque um mesmo Fornecedor é reaproveitado entre várias
Trips.

Invariantes (Sprint 1B): `name` não vazio; `category` válida;
`email`/`phone` presentes.

Observações: se a 027 Viagens realmente cadastra/reaproveita
fornecedores entre propostas, ou cada cotação trata fornecedores de
forma isolada, é uma pergunta em aberto (ver docs/glossary.md).
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.email import Email
from src.domain.shared.guards import require_instance, require_non_empty_str
from src.domain.shared.phone import Phone
from src.domain.supplier.enums import SupplierCategory


@dataclass
class Supplier(BaseEntity):
    name: str
    category: SupplierCategory
    email: Email
    phone: Phone

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.name, "Supplier.name não pode ser vazio.")
        require_instance(self.category, SupplierCategory, f"Supplier.category inválida: {self.category!r}")
        require_instance(self.email, Email, "Supplier.email é obrigatório.")
        require_instance(self.phone, Phone, "Supplier.phone é obrigatório.")
