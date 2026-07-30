"""Metadata obrigatória de toda Proposta/Documento — Value Object.

Espelha o bloco de metadata definido em docs/universal-proposal-model.md
(proposal_id, schema_version, engine_version, template, generated_at,
generated_by, consultor, origem, status). Modelada como Value Object,
não Entidade: dois blocos de metadata com os mesmos valores representam
a mesma informação de rastreabilidade — não têm identidade própria
distinta do que carregam (ver docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md).

`consultant_id` aqui é uma referência rápida para rastreamento, redundante
de propósito com o `consultant_id` em ProposalVersion — ver
docs/universal-proposal-model.md.
"""

from dataclasses import dataclass
from datetime import datetime

from src.domain.shared.identifier import Identifier
from src.domain.shared.value_object import ValueObject


@dataclass(frozen=True)
class Metadata(ValueObject):
    proposal_id: Identifier
    schema_version: str
    engine_version: str
    template: str
    generated_at: datetime
    generated_by: str
    consultant_id: Identifier
    origin: str
    status: str
