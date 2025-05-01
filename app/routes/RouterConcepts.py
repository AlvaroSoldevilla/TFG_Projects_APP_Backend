from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Concept import ConceptCreate, ConceptUpdate, ConceptRead
import app.services.ServiceConcepts as sc

router = APIRouter(prefix="/concepts", tags=["Concepts"])


# Generic endpoints
@router.get("/", response_model=list[ConceptRead], status_code=200)
def get_all_concepts(session: Session = Depends(get_session)):
    return sc.get_all_concepts(session)


@router.get("/{id}", response_model=ConceptRead, status_code=200)
def get_concept_by_id(id: int, session: Session = Depends(get_session)):
    return sc.get_concept_by_id(id, session)


@router.post("/", status_code=200)
def create_concept(concept_data: ConceptCreate, session: Session = Depends(get_session)):
    if sc.create_concept(concept_data, session):
        return {"Message": "Concept created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create concept")


@router.patch("/{id}", status_code=200)
def update_concept(id: int, concept_update: ConceptUpdate, session: Session = Depends(get_session)):
    if sc.update_concept(id, concept_update, session):
        return {"Message": "Concept updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept")


@router.delete("/{id}", status_code=200)
def delete_concept(id: int, session: Session = Depends(get_session)):
    if sc.delete_concept(id, session):
        return {"Message": "Concept deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept")


# Model Specific endpoints
@router.get("/project/{id}", response_model=list[ConceptRead], status_code=200)
def get_concepts_by_project(id_project: int, session: Session = Depends(get_session)):
    return sc.get_concept_boards_by_project(id_project, session)
