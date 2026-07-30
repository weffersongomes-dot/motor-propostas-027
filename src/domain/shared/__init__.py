"""Shared Kernel — elementos usados por todos os Bounded Contexts.

Contém apenas o que é verdadeiramente comum (Identifier, BaseEntity,
ValueObject, DomainEvent, Money, Metadata e VOs genéricos como
Email/Phone/Address/DocumentNumber/DateRange). Regra de negócio
específica de um contexto nunca deve entrar aqui — ver
docs/ARCHITECTURE.md e docs/decisoes/0006-sprint-1a-modelagem-de-dominio.md.
"""
