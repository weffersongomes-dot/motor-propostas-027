"""Exemplo de dado de entrada usando os objetos de domínio da Sprint 1A.

Wire completo: Company -> Consultant, Customer -> Passenger,
Supplier, Trip -> Flight/Accommodation/Service, Proposal ->
ProposalVersion (com Financial e Metadata).

Nenhuma validação é exercitada aqui de propósito — o objetivo é só
confirmar que os objetos de domínio se encaixam estruturalmente,
conforme docs/universal-proposal-model.md e docs/domain-map.md.

Executar com: python examples/sprint_1a_domain_example.py
"""

from datetime import date, datetime
from decimal import Decimal

from src.domain.company.company import Company
from src.domain.company.consultant import Consultant
from src.domain.customer.customer import Customer
from src.domain.customer.passenger import Passenger
from src.domain.financial.financial import Financial
from src.domain.proposal.proposal import Proposal
from src.domain.proposal.proposal_classification import ProposalClassification
from src.domain.proposal.proposal_version import ProposalVersion
from src.domain.shared.address import Address
from src.domain.shared.date_range import DateRange
from src.domain.shared.document_number import DocumentNumber
from src.domain.shared.email import Email
from src.domain.shared.identifier import Identifier
from src.domain.shared.metadata import Metadata
from src.domain.shared.money import Money
from src.domain.shared.phone import Phone
from src.domain.supplier.supplier import Supplier
from src.domain.trip.accommodation import Accommodation
from src.domain.trip.airport import Airport
from src.domain.trip.flight import Flight
from src.domain.trip.service import Service
from src.domain.trip.trip import Trip


def build_example() -> Proposal:
    company = Company(
        id=Identifier("company-027"),
        legal_name="027 Viagens e Turismo Ltda.",
        trade_name="027 Viagens",
        document_number=DocumentNumber(type="CNPJ", value="00.000.000/0001-00"),
        address=Address(
            street="Rua das Palmeiras", number="123", complement="Sala 4",
            neighborhood="Centro", city="Criciúma", state="SC",
            country="Brasil", postal_code="88800-000",
        ),
        email=Email("contato@027viagens.com.br"),
        phone=Phone("+55 48 90000-0000"),
        logo_path="assets/logo/027-viagens.png",
        consultants=[
            Consultant(
                id=Identifier("consultant-1"),
                name="Consultor Exemplo",
                email=Email("consultor@027viagens.com.br"),
                phone=Phone("+55 48 91111-1111"),
            )
        ],
    )

    customer = Customer(
        id=Identifier("customer-1"),
        name="Cliente Exemplo",
        document_number=DocumentNumber(type="CPF", value="000.000.000-00"),
        email=Email("cliente@example.com"),
        phone=Phone("+55 48 92222-2222"),
        passengers=[
            Passenger(
                id=Identifier("passenger-1"),
                name="Passageiro Exemplo",
                document_number=DocumentNumber(type="CPF", value="111.111.111-11"),
                birth_date=date(1990, 1, 1),
            )
        ],
    )

    airline = Supplier(
        id=Identifier("supplier-airline"),
        name="Companhia Aérea Exemplo",
        category="Companhia aérea",
        email=Email("contato@companhia-exemplo.com"),
        phone=Phone("+55 11 93333-3333"),
    )
    hotel = Supplier(
        id=Identifier("supplier-hotel"),
        name="Hotel Exemplo",
        category="Hotel",
        email=Email("contato@hotel-exemplo.com"),
        phone=Phone("+55 11 94444-4444"),
    )

    trip = Trip(
        id=Identifier("trip-1"),
        destination="Orlando, EUA",
        date_range=DateRange(start=date(2026, 12, 10), end=date(2026, 12, 20)),
        flights=[
            Flight(
                id=Identifier("flight-1"),
                supplier_id=airline.id,
                origin=Airport(code="GRU", name="Aeroporto de Guarulhos", city="São Paulo"),
                destination=Airport(code="MCO", name="Orlando International", city="Orlando"),
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
        proposal_id=Identifier("proposal-001"),
        schema_version="0.1.0",
        engine_version="0.1.0",
        template="propostas/html/padrao",
        generated_at=datetime(2026, 7, 29, 10, 0),
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
            total=Money(amount=Decimal("15000.00"), currency="BRL"),
            payment_method="Cartão de crédito",
            installments=10,
        ),
        metadata=metadata,
    )

    return Proposal(id=Identifier("proposal-001"), versions=[version])


if __name__ == "__main__":
    proposal = build_example()
    version = proposal.versions[0]
    print(f"Proposal id: {proposal.id.value}")
    print(f"Versão: {version.version_number}")
    print(f"Classificação: {version.classification}")
    print(f"Financeiro: {version.financial}")
    print(f"Metadata: {version.metadata}")
