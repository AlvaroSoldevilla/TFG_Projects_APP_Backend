from sqlmodel import Session

import app.repositories.RepositoryConcepts as rc
from app.schemas.Concept import ConceptCreate, ConceptUpdate


async def get_all_concepts(session: Session):
    return await rc.get_all_concepts(session)


async def get_concept_by_id(concept_id: int, session: Session):
    return await rc.get_concept_by_id(concept_id, session)


async def create_concept(concept_data: ConceptCreate, session: Session):
    return await rc.create_concept(concept_data, session)


async def update_concept(concept_id: int, concept_update: ConceptUpdate, session: Session):
    return await rc.update_concept(concept_id, concept_update, session)


async def delete_concept(concept_id: int, session: Session):
    return await rc.delete_concept(concept_id, session)


async def get_concept_boards_by_project(id_project: int, session: Session):
    concepts = await rc.get_all_concepts(session)
    return [concept for concept in concepts if concept.id_project == id_project]
