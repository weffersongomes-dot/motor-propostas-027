"""Shared Kernel — elementos usados por todos os Bounded Contexts.

Contém apenas o que é verdadeiramente comum: BaseEntity, ValueObject,
Identifier, DomainEvent, exceções de domínio, guards de validação, e os
Value Objects/enums genéricos (Money, Email, Phone, Address,
DocumentNumber, DateRange, CountryCode, LanguageCode, Metadata,
DocumentType, PhoneType, Currency).

Revisão Sprint 1B (ver docs/decisoes/0008-sprint-1b-invariantes-e-validacoes.md
e docs/domain-decisions.md): `Metadata.proposal_id` foi renomeado para
`subject_id` por depender de vocabulário do módulo Propostas dentro de
um objeto pensado para ser genérico. Nenhum outro objeto foi removido
desta pasta — todos os demais são reaproveitados por mais de um
contexto (Company, Customer, Supplier usam Email/Phone/Address/
DocumentNumber; Financial usa Money; todo módulo futuro usará
Metadata/Identifier/BaseEntity/DomainEvent).
"""
