from sqlalchemy import select
from sqlmodel import Session

from app.models.Concepts import Concepts
from app.schemas.Concept import ConceptCreate, ConceptUpdate


def get_all_concepts(session: Session):
    query = select(Concepts)
    concepts = session.exec(query).scalars().all()

    return [Concepts.model_validate(c) for c in concepts]


def get_concept_by_id(concept_id: int, session: Session):
    return session.get(Concepts, concept_id)


def create_concept(concept_data: ConceptCreate, session: Session):
    concept = Concepts(**concept_data.model_dump())
    session.add(concept)
    session.commit()
    session.refresh(concept)

    return concept


def update_concept(concept_id: int, concept_update: ConceptUpdate, session: Session):
    concept = session.get(Concepts, concept_id)

    if not concept:
        return False

    for k, v in concept_update.model_dump(exclude_unset=True).items():
        setattr(concept, k, v)

    session.add(concept)
    session.commit()
    session.refresh(concept)

    return True


def delete_concept(concept_id: int, session: Session):
    concept = session.get(Concepts, concept_id)

    if not concept:
        return False

    session.delete(concept)
    session.commit()

    return True

