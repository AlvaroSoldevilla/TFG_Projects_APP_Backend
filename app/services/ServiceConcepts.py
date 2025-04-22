import app.repositories.RepositoryConcepts as rc
from app.schemas.Concept import ConceptCreate, ConceptUpdate


async def get_all_concepts():
    return await rc.get_all_concepts()


async def get_concept_by_id(concept_id: int):
    return await rc.get_concept_by_id(concept_id)


async def create_concept(concept_data: ConceptCreate):
    return await rc.create_concept(concept_data)


async def update_concept(concept_id: int, concept_update: ConceptUpdate):
    return await rc.update_concept(concept_id, concept_update)


async def delete_concept(concept_id: int):
    return await rc.delete_concept(concept_id)


async def get_concept_boards_by_project(id_project: int):
    concepts = await rc.get_all_concepts()
    return [concept for concept in concepts if concept.id_project == id_project]
