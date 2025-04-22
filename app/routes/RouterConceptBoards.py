from fastapi import APIRouter, HTTPException

from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate, ConceptBoardRead
import app.services.ServiceConceptBoards as scb

router = APIRouter(prefix="/concept_boards", tags=["Concept Boards"])


# Generic endpoints
@router.get("/", response_model=list[ConceptBoardRead], status_code=200)
async def get_all_concept_boards():
    return await scb.get_all_concept_boards()


@router.get("/{id}", response_model=ConceptBoardRead, status_code=200)
async def get_concept_board_by_id(id: int):
    return await scb.get_concept_board_by_id(id)


@router.post("/", status_code=200)
async def create_concept_board(concept_board_data: ConceptBoardCreate):
    if await scb.create_concept_board(concept_board_data):
        return {"Message": "Concept board created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create concept board")


@router.patch("/{id}", status_code=200)
async def update_concept_board(id: int, concept_board_update: ConceptBoardUpdate):
    if await scb.update_concept_board(id, concept_board_update):
        return {"Message": "Concept board updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept board")


@router.delete("/{id}", status_code=200)
async def delete_concept_board(id: int):
    if await scb.delete_concept_board(id):
        return {"Message": "Concept board deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept board")


# Model Specific endpoints
@router.get("/concept/{id}", response_model=list[ConceptBoardRead], status_code=200)
async def get_concept_boards_by_concept(id_concept: int):
    return await scb.get_concept_boards_by_concept(id_concept)
