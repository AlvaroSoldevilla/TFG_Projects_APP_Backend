from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Concepts import Concepts
from app.schemas.Concept import ConceptCreate, ConceptUpdate


async def get_all_concepts(session: Session = Depends(get_session())):
    query = select(Concepts)
    concepts = session.exec(query).scalar().all()

    return [Concepts.model_validate(c) for c in concepts]


async def get_concept_by_id(concept_id: int, session: Session = Depends(get_session())):
    return session.get(Concepts, concept_id)


async def create_concept(concept_data: ConceptCreate, session: Session = Depends(get_session())):
    concept = Concepts(**concept_data.model_dump())
    session.add(concept)
    session.commit()
    session.refresh(concept)

    return True


async def update_concept(concept_id: int, concept_update: ConceptUpdate, session: Session = Depends(get_session())):
    concept = session.get(Concepts, concept_id)

    if not concept:
        return False

    for k, v in concept_update.model_dump(exclude_unset=True).items():
        setattr(concept, k, v)

    session.add(concept)
    session.commit()
    session.refresh(concept)

    return True


async def delete_concept(concept_id: int, session: Session = Depends(get_session())):
    concept = session.get(Concepts, concept_id)

    if not concept:
        return False

    session.delete(concept)
    session.commit()

    return True

