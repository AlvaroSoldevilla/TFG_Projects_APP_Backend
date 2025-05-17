from sqlalchemy import select
from sqlmodel import Session

from app.models.ConceptBoards import ConceptBoards
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate


def get_all_concept_boards(session: Session):
    query = select(ConceptBoards)
    concept_board = session.exec(query).scalars().all()

    return [ConceptBoards.model_validate(cb) for cb in concept_board]


def get_concept_board_by_id(concept_board_id: int, session: Session):
    return session.get(ConceptBoards, concept_board_id)


def create_concept_board(concept_board_data: ConceptBoardCreate, session: Session):
    concept_board = ConceptBoards(**concept_board_data.model_dump())
    session.add(concept_board)
    session.commit()
    session.refresh(concept_board)

    return concept_board


def update_concept_board(concept_board_id: int, concept_board_update: ConceptBoardUpdate, session: Session):
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


def delete_concept_board(concept_board_id: int, session: Session):
    concept_board = session.get(ConceptBoards, concept_board_id)

    if not concept_board:
        return False

    session.delete(concept_board)
    session.commit()

    return True
