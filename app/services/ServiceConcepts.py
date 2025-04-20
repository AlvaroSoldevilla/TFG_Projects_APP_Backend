import app.repositories.RepositoryConcepts as rc
from app.schemas.Concept import ConceptCreate, ConceptUpdate


async def get_all_concepts():
    return rc.get_all_concepts()


async def get_concept_by_id(concept_id: int):
    return rc.get_concept_by_id(concept_id)


async def create_concept(concept_data: ConceptCreate):
    return rc.create_concept(concept_data)


async def update_concept(concept_id: int, concept_update: ConceptUpdate):
    return rc.update_concept(concept_id, concept_update)


async def delete_concept(concept_id: int):
    return rc.delete_concept(concept_id)


async def get_concept_boards_by_project(id_project: int):
    concepts = rc.get_all_concepts()
    return [concept for concept in concepts if concept.id_project == id_project]
