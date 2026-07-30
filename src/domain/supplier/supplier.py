"""Supplier — Aggregate Root.

Responsabilidade: representa o Fornecedor (ver docs/glossary.md) —
empresa parceira que presta um serviço concreto da viagem (companhia
aérea, hotel, operadora, seguradora).

Atributos iniciais: nome, categoria (texto livre nesta etapa — vira
enum na Sprint 1B), e-mail, telefone.

Relacionamentos: referenciado por `Flight.supplier_id`,
`Accommodation.supplier_id` e `Service.supplier_id` — nunca aninhado
dentro deles, porque um mesmo Fornecedor é reaproveitado entre várias
Trips.

Observações: se a 027 Viagens realmente cadastra/reaproveita
fornecedores entre propostas, ou cada cotação trata fornecedores de
forma isolada, é uma pergunta em aberto (ver docs/glossary.md).
"""

from dataclasses import dataclass

from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.email import Email
from src.domain.shared.phone import Phone


@dataclass
class Supplier(BaseEntity):
    name: str
    category: str
    email: Email
    phone: Phone
