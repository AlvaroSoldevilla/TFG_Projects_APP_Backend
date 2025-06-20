from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate, ConceptBoardRead
import app.services.ServiceConceptBoards as scb

router = APIRouter(prefix="/concept_boards", tags=["Concept Boards"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[ConceptBoardRead], status_code=200)
def get_all_concept_boards(session: Session = Depends(get_session)):
    return scb.get_all_concept_boards(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=ConceptBoardRead, status_code=200)
def get_concept_board_by_id(id: int, session: Session = Depends(get_session)):
    concept_board = scb.get_concept_board_by_id(id, session)
    if concept_board is None:
        raise HTTPException(status_code=404, detail="ConceptBoard not found")
    else:
        return concept_board


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=ConceptBoardRead)
def create_concept_board(concept_board_data: ConceptBoardCreate, session: Session = Depends(get_session)):
    concept_board = scb.create_concept_board(concept_board_data, session)
    if concept_board:
        return concept_board
    else:
        raise HTTPException(status_code=400, detail="Could not create concept board")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_concept_board(id: int, concept_board_update: ConceptBoardUpdate, session: Session = Depends(get_session)):
    if scb.update_concept_board(id, concept_board_update, session):
        return {"Message": "Concept board updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept board")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_concept_board(id: int, session: Session = Depends(get_session)):
    if scb.delete_concept_board(id, session):
        return {"Message": "Concept board deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept board")


# Model Specific endpoints
@router.get("/concept/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[ConceptBoardRead], status_code=200)
def get_concept_boards_by_concept(id: int, session: Session = Depends(get_session)):
    return scb.get_concept_boards_by_concept(id, session)
