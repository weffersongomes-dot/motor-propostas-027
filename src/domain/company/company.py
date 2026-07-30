"""Company — Aggregate Root.

Responsabilidade: representa a 027 Viagens (Empresa, ver
docs/glossary.md) — dados institucionais que aparecem em todo
documento emitido pela plataforma.

Atributos iniciais: razão social, nome fantasia, documento (CNPJ),
endereço, e-mail, telefone, caminho do logo, e a lista de Consultores
que trabalham na empresa.

Relacionamentos: agrega `Consultant` (a 027 Viagens tem N consultores).
Referenciada por `ProposalVersion.company_id`.

Observações: hoje existe uma única `Company` na plataforma (a própria
027 Viagens) — o desenho como Aggregate Root, e não como um Value
Object fixo em `config/`, prepara o terreno para o dia em que a
plataforma precisar representar mais de uma empresa (ex: uma marca
irmã), sem redesenho.
"""

from dataclasses import dataclass, field
from typing import List

from src.domain.company.consultant import Consultant
from src.domain.shared.address import Address
from src.domain.shared.base_entity import BaseEntity
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.email import Email
from src.domain.shared.phone import Phone


@dataclass
class Company(BaseEntity):
    legal_name: str
    trade_name: str
    document_number: DocumentNumber
    address: Address
    email: Email
    phone: Phone
    logo_path: str
    consultants: List[Consultant] = field(default_factory=list)
