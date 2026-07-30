"""Número de documento de identificação (CPF, CNPJ, Passaporte...) — Value Object.

Sprint 1B: `type` formalizado como enum estrutural `DocumentType`.
Nenhum algoritmo de dígito verificador (CPF/CNPJ) é implementado — isso
seria uma regra de formato específica de um tipo de documento
brasileiro, mais apropriada para uma validação de aplicação/infra do
que para o Value Object genérico do domínio.
"""

from dataclasses import dataclass

from src.domain.shared.enums import DocumentType
from src.domain.shared.guards import require_instance, require_non_empty_str
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class DocumentNumber(ValueObject):
    type: DocumentType
    value: str

    def __post_init__(self) -> None:
        require_instance(self.type, DocumentType, f"DocumentNumber.type inválido: {self.type!r}")
        require_non_empty_str(self.value, "DocumentNumber.value não pode ser vazio.")
