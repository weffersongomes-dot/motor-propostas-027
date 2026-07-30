"""Domain Events da plataforma — estrutura preparada, nenhum evento implementado ainda.

`DomainEvent` (a base) vive em `src/domain/shared/domain_event.py`,
por ser um primitivo verdadeiramente compartilhado por qualquer evento
futuro de qualquer contexto. Esta pasta (`src/domain/events/`) é onde
os eventos *concretos* de cada contexto serão implementados quando
`src/application/` deixar de estar vazia — ver README.md nesta pasta
para a lista de eventos previstos e docs/bounded-context-map.md para
como eventos vão comunicar contextos entre si.
"""
