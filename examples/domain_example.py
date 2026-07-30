"""Exemplo executável do domínio — reflete o estado atual da modelagem.

Substitui examples/sprint_1a_domain_example.py (Sprint 1A, "forma
apenas"). Agora que o domínio valida a si mesmo (Sprint 1B), este
arquivo demonstra dois cenários:

1. `build_valid_example()` — um wire completo e válido, igual em
   espírito ao da Sprint 1A, mas usando os novos campos/enums
   estruturais (passenger_ids, passenger_type, Phone.type,
   Address.country, Proposal.status, ProposalVersion.status).
2. `demonstrate_invariant_enforcement()` — tenta construir objetos
   estruturalmente inválidos de propósito, prova que o domínio rejeita
   cada um com a exceção correta (StructuralValidationError /
   InvariantViolationError).

Executar com: python examples/domain_example.py
"""

from datetime import date, datetime
from decimal import Decimal

from src.domain.company.company import Company
from src.domain.company.consultant import Consultant
from src.domain.customer.customer import Customer
from src.domain.customer.enums import PassengerType
from src.domain.customer.passenger import Passenger
from src.domain.financial.financial import Financial
from src.domain.proposal.enums import ProposalStatus, ProposalVersionStatus
from src.domain.proposal.proposal import Proposal
from src.domain.proposal.proposal_classification import ProposalClassification
from src.domain.proposal.proposal_version import ProposalVersion
from src.domain.shared.address import Address
from src.domain.shared.country_code import CountryCode
from src.domain.shared.date_range import DateRange
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.email import Email
from src.domain.shared.enums import Currency, DocumentType, PhoneType
from src.domain.shared.exceptions import DomainError
from src.domain.shared.identifier import Identifier
from src.domain.shared.metadata import Metadata
from src.domain.shared.money import Money
from src.domain.shared.phone import Phone
from src.domain.supplier.enums import SupplierCategory
from src.domain.supplier.supplier import Supplier
from src.domain.trip.accommodation import Accommodation
from src.domain.trip.airport import Airport
from src.domain.trip.enums import AirportType
from src.domain.trip.flight import Flight
from src.domain.trip.service import Service
from src.domain.trip.trip import Trip


def build_valid_example() -> Proposal:
    company = Company(
        id=Identifier("company-027"),
        legal_name="027 Viagens e Turismo Ltda.",
        trade_name="027 Viagens",
        document_number=DocumentNumber(type=DocumentType.CNPJ, value="00.000.000/0001-00"),
        address=Address(
            street="Rua das Palmeiras", number="123", complement="Sala 4",
            neighborhood="Centro", city="Criciúma", state="SC",
            country=CountryCode("BR"), postal_code="88800-000",
        ),
        email=Email("contato@027viagens.com.br"),
        phone=Phone(type=PhoneType.WHATSAPP, value="+55 48 90000-0000"),
        logo_path="assets/logo/027-viagens.png",
        consultants=[
            Consultant(
                id=Identifier("consultant-1"),
                name="Consultor Exemplo",
                email=Email("consultor@027viagens.com.br"),
                phone=Phone(type=PhoneType.MOBILE, value="+55 48 91111-1111"),
            )
        ],
    )

    passenger = Passenger(
        id=Identifier("passenger-1"),
        name="Passageiro Exemplo",
        document_number=DocumentNumber(type=DocumentType.CPF, value="111.111.111-11"),
        birth_date=date(1990, 1, 1),
        passenger_type=PassengerType.ADULT,
    )

    customer = Customer(
        id=Identifier("customer-1"),
        name="Cliente Exemplo",
        document_number=DocumentNumber(type=DocumentType.CPF, value="000.000.000-00"),
        email=Email("cliente@example.com"),
        phone=Phone(type=PhoneType.MOBILE, value="+55 48 92222-2222"),
        passengers=[passenger],
    )

    airline = Supplier(
        id=Identifier("supplier-airline"),
        name="Companhia Aérea Exemplo",
        category=SupplierCategory.AIRLINE,
        email=Email("contato@companhia-exemplo.com"),
        phone=Phone(type=PhoneType.LANDLINE, value="+55 11 93333-3333"),
    )
    hotel = Supplier(
        id=Identifier("supplier-hotel"),
        name="Hotel Exemplo",
        category=SupplierCategory.HOTEL,
        email=Email("contato@hotel-exemplo.com"),
        phone=Phone(type=PhoneType.LANDLINE, value="+55 11 94444-4444"),
    )

    trip = Trip(
        id=Identifier("trip-1"),
        destination="Orlando, EUA",
        date_range=DateRange(start=date(2026, 12, 10), end=date(2026, 12, 20)),
        passenger_ids=[passenger.id],
        flights=[
            Flight(
                id=Identifier("flight-1"),
                supplier_id=airline.id,
                origin=Airport(code="GRU", name="Aeroporto de Guarulhos", city="São Paulo", type=AirportType.INTERNATIONAL),
                destination=Airport(code="MCO", name="Orlando International", city="Orlando", type=AirportType.INTERNATIONAL),
                departure_at=datetime(2026, 12, 10, 22, 0),
                arrival_at=datetime(2026, 12, 11, 6, 0),
            )
        ],
        accommodations=[
            Accommodation(
                id=Identifier("accommodation-1"),
                supplier_id=hotel.id,
                name="Resort Exemplo",
                category="4 estrelas",
                date_range=DateRange(start=date(2026, 12, 11), end=date(2026, 12, 20)),
            )
        ],
        services=[
            Service(
                id=Identifier("service-1"),
                supplier_id=hotel.id,
                description="Traslado aeroporto-hotel",
                is_optional=False,
            )
        ],
    )

    metadata = Metadata(
        subject_id=Identifier("proposal-001"),
        schema_version="0.2.0",
        engine_version="0.2.0",
        template="propostas/html/padrao",
        generated_at=datetime(2026, 7, 30, 10, 0),
        generated_by="exemplo-manual",
        consultant_id=company.consultants[0].id,
        origin="exemplo",
        status="rascunho",
    )

    version = ProposalVersion(
        id=Identifier("proposal-001-v1"),
        version_number="001.1",
        company_id=company.id,
        customer_id=customer.id,
        trip_id=trip.id,
        consultant_id=company.consultants[0].id,
        classification=ProposalClassification(
            destinations=("Internacional",),
            formats=("Individual",),
            purposes=("Lazer",),
            products=("Disney",),
        ),
        financial=Financial(
            total=Money(amount=Decimal("15000.00"), currency=Currency.BRL),
            payment_method="Cartão de crédito",
            installments=10,
        ),
        metadata=metadata,
        status=ProposalVersionStatus.ACTIVE,
    )

    return Proposal(id=Identifier("proposal-001"), status=ProposalStatus.DRAFT, versions=[version])


def demonstrate_invariant_enforcement() -> None:
    """Prova que o domínio rejeita dado estruturalmente inválido."""
    attempts = [
        ("Identifier vazio", lambda: Identifier("")),
        ("Email sem formato válido", lambda: Email("nao-e-um-email")),
        ("DateRange com fim antes do início", lambda: DateRange(start=date(2026, 1, 10), end=date(2026, 1, 1))),
        (
            "Trip sem nenhum passageiro",
            lambda: Trip(
                id=Identifier("trip-invalido"),
                destination="Destino Exemplo",
                date_range=DateRange(start=date(2026, 1, 1), end=date(2026, 1, 5)),
                passenger_ids=[],
            ),
        ),
    ]
    for label, attempt in attempts:
        try:
            attempt()
        except DomainError as error:
            print(f"[OK] rejeitado como esperado — {label}: {error}")
        else:
            print(f"[FALHA] deveria ter sido rejeitado — {label}")


if __name__ == "__main__":
    proposal = build_valid_example()
    version = proposal.versions[0]
    print(f"Proposal id: {proposal.id.value} — status: {proposal.status.value}")
    print(f"Versão: {version.version_number} — status: {version.status.value}")
    print(f"Classificação: {version.classification}")
    print(f"Financeiro: {version.financial}")
    print(f"Metadata: {version.metadata}")
    print()
    print("Demonstração de rejeição de dado inválido:")
    demonstrate_invariant_enforcement()
