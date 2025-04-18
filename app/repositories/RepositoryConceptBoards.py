from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.ConceptBoards import ConceptBoards
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate


async def get_all_concept_boards(session: Session = Depends(get_session())):
    query = select(ConceptBoards)
    concept_board = session.exec(query).scalar().all()

    return [ConceptBoards.model_validate(cb) for cb in concept_board]


async def get_concept_board_by_id(concept_board_id: int, session: Session = Depends(get_session())):
    return session.get(ConceptBoards, concept_board_id)


async def create_concept_board(concept_board_data: ConceptBoardCreate, session: Session = Depends(get_session())):
    concept_board = ConceptBoards(**concept_board_data.model_dump())
    session.add(concept_board)
    session.commit()
    session.refresh(concept_board)

    return True


async def update_concept_board(concept_board_id: int, concept_board_update: ConceptBoardUpdate, session: Session = Depends(get_session())):
    concept_board = session.get(ConceptBoards, concept_board_id)

    if not concept_board:
        return False

    concept_board_dict = concept_board_update.model_dump(exclude_unset=True)

    for k, v in concept_board_dict.items():
        setattr(concept_board, k, v)

    session.add(concept_board)
    session.commit()
    session.refresh(concept_board)

    return True


async def delete_concept_board(concept_board_id: int, session: Session = Depends(get_session())):
    concept_board = session.get(ConceptBoards, concept_board_id)

    if not concept_board:
        return False

    session.delete(concept_board)
    session.commit()

    return True
