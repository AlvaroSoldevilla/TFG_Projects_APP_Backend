from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Concept import ConceptCreate, ConceptUpdate, ConceptRead
import app.services.ServiceConcepts as sc

router = APIRouter(prefix="/concepts", tags=["Concepts"])


# Generic endpoints
@router.get("/", dependencies=[Depends(JWTBearer())], response_model=list[ConceptRead], status_code=200)
def get_all_concepts(session: Session = Depends(get_session)):
    return sc.get_all_concepts(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=ConceptRead, status_code=200)
def get_concept_by_id(id: int, session: Session = Depends(get_session)):
    return sc.get_concept_by_id(id, session)


@router.post("/", dependencies=[Depends(JWTBearer())], status_code=200, response_model=ConceptRead)
def create_concept(concept_data: ConceptCreate, session: Session = Depends(get_session)):
    concept = sc.create_concept(concept_data, session)
    if concept:
        return concept
    else:
        raise HTTPException(status_code=400, detail="Could not create concept")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_concept(id: int, concept_update: ConceptUpdate, session: Session = Depends(get_session)):
    if sc.update_concept(id, concept_update, session):
        return {"Message": "Concept updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_concept(id: int, session: Session = Depends(get_session)):
    if sc.delete_concept(id, session):
        return {"Message": "Concept deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept")


# Model Specific endpoints
@router.get("/project/{id}", dependencies=[Depends(JWTBearer())], response_model=list[ConceptRead], status_code=200)
def get_concepts_by_project(id: int, session: Session = Depends(get_session)):
    return sc.get_concept_boards_by_project(id, session)
