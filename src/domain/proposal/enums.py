"""Enums estruturais do contexto Comercial (Proposal).

`ProposalDimension` nomeia as quatro dimensões de classificação
confirmadas em docs/proposal-types.md e ADR 0005 (Destino, Formato,
Finalidade, Produto) — a existência das quatro dimensões é estrutural
e já confirmada; os *valores* dentro de cada uma (Nacional/
Internacional, Individual/Grupo...) continuam pendentes de negócio, por
isso não viram enum ainda (ver `ProposalClassification`).

`ProposalStatus` e `ProposalVersionStatus` são os "Estados do Modelo"
desta sprint — representam apenas a posição estrutural no ciclo de
vida (rascunho/publicada/fechada; rascunho/ativa/arquivada), não o
fluxo comercial completo de docs/proposal-status.md (que tem 9 estados
mais ricos, dependentes de regra de negócio, e continua sendo a
referência para quando o comportamento for implementado).
"""

from enum import Enum


class ProposalDimension(Enum):
    DESTINATION = "DESTINATION"
    FORMAT = "FORMAT"
    PURPOSE = "PURPOSE"
    PRODUCT = "PRODUCT"


class ProposalStatus(Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    CLOSED = "CLOSED"


class ProposalVersionStatus(Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
