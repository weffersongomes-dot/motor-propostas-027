"""Company — Aggregate Root.

Responsabilidade: representa a 027 Viagens (Empresa, ver
docs/glossary.md) — dados institucionais que aparecem em todo
documento emitido pela plataforma.

Atributos iniciais: razão social, nome fantasia, documento (CNPJ),
endereço, e-mail, telefone, caminho do logo, e a lista de Consultores
que trabalham na empresa.

Relacionamentos: agrega `Consultant` (a 027 Viagens tem N consultores).
Referenciada por `ProposalVersion.company_id`.

Invariantes (Sprint 1B): `legal_name`/`trade_name`/`logo_path` não
vazios; `document_number`/`address`/`email`/`phone` presentes.
`consultants` pode ser vazia (uma empresa recém-cadastrada pode ainda
não ter consultores atribuídos).

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
from src.domain.shared.guards import require_instance, require_non_empty_str
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

    def __post_init__(self) -> None:
        super().__post_init__()
        require_non_empty_str(self.legal_name, "Company.legal_name não pode ser vazio.")
        require_non_empty_str(self.trade_name, "Company.trade_name não pode ser vazio.")
        require_non_empty_str(self.logo_path, "Company.logo_path não pode ser vazio.")
        require_instance(self.document_number, DocumentNumber, "Company.document_number é obrigatório.")
        require_instance(self.address, Address, "Company.address é obrigatório.")
        require_instance(self.email, Email, "Company.email é obrigatório.")
        require_instance(self.phone, Phone, "Company.phone é obrigatório.")
