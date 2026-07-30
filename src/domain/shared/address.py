"""Endereço postal — Value Object.

Sprint 1B: `country` formalizado como `CountryCode` (VO validado por
formato, não enum fechado — ver country_code.py). Campos de texto
continuam livres; nenhum é tratado como opcional/obrigatório em nível
de negócio aqui — só `street`/`city`/`postal_code` são exigidos como
não vazios, por serem o mínimo estrutural de um endereço utilizável.
"""

from dataclasses import dataclass

from src.domain.shared.country_code import CountryCode
from src.domain.shared.guards import require_non_empty_str
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Address(ValueObject):
    street: str
    number: str
    complement: str
    neighborhood: str
    city: str
    state: str
    country: CountryCode
    postal_code: str

    def __post_init__(self) -> None:
        require_non_empty_str(self.street, "Address.street não pode ser vazio.")
        require_non_empty_str(self.city, "Address.city não pode ser vazio.")
        require_non_empty_str(self.postal_code, "Address.postal_code não pode ser vazio.")
