from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate, ConceptBoardRead
import app.services.ServiceConceptBoards as scb

router = APIRouter(prefix="/concept_boards", tags=["Concept Boards"])


# Generic endpoints
@router.get("/", response_model=list[ConceptBoardRead], status_code=200)
def get_all_concept_boards(session: Session = Depends(get_session)):
    return scb.get_all_concept_boards(session)


@router.get("/{id}", response_model=ConceptBoardRead, status_code=200)
def get_concept_board_by_id(id: int, session: Session = Depends(get_session)):
    return scb.get_concept_board_by_id(id, session)


@router.post("/", status_code=200)
def create_concept_board(concept_board_data: ConceptBoardCreate, session: Session = Depends(get_session)):
    if scb.create_concept_board(concept_board_data, session):
        return {"Message": "Concept board created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create concept board")


@router.patch("/{id}", status_code=200)
def update_concept_board(id: int, concept_board_update: ConceptBoardUpdate, session: Session = Depends(get_session)):
    if scb.update_concept_board(id, concept_board_update, session):
        return {"Message": "Concept board updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept board")


@router.delete("/{id}", status_code=200)
def delete_concept_board(id: int, session: Session = Depends(get_session)):
    if scb.delete_concept_board(id, session):
        return {"Message": "Concept board deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept board")


# Model Specific endpoints
@router.get("/concept/{id}", response_model=list[ConceptBoardRead], status_code=200)
def get_concept_boards_by_concept(id_concept: int, session: Session = Depends(get_session)):
    return scb.get_concept_boards_by_concept(id_concept, session)
