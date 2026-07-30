"""Base para Domain Events — apenas estrutura, nenhum evento concreto ainda.

Domain Events serão o mecanismo de comunicação entre Bounded Contexts
(ver docs/bounded-context-map.md) a partir de uma sprint futura, quando
`src/application/` existir de fato. Nesta sprint, apenas a forma base é
preparada — nenhum evento concreto (ex: "PropostaAprovada") é criado.
"""

from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DomainEvent(ABC):
    occurred_at: datetime
