from sqlmodel import Session

import app.repositories.RepositoryConcepts as rc
from app.schemas.Concept import ConceptCreate, ConceptUpdate


def get_all_concepts(session: Session):
    return rc.get_all_concepts(session)


def get_concept_by_id(concept_id: int, session: Session):
    return rc.get_concept_by_id(concept_id, session)


def create_concept(concept_data: ConceptCreate, session: Session):
    return rc.create_concept(concept_data, session)


def update_concept(concept_id: int, concept_update: ConceptUpdate, session: Session):
    return rc.update_concept(concept_id, concept_update, session)


def delete_concept(concept_id: int, session: Session):
    return rc.delete_concept(concept_id, session)


def get_concept_boards_by_project(id_project: int, session: Session):
    concepts = rc.get_all_concepts(session)
    return [concept for concept in concepts if concept.id_project == id_project]
