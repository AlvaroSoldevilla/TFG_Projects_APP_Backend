from sqlmodel import Session

import app.repositories.RepositoryConceptBoards as rcb
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate


def get_all_concept_boards(session: Session):
    return rcb.get_all_concept_boards(session)


def get_concept_board_by_id(concept_board_id: int, session: Session):
    return rcb.get_concept_board_by_id(concept_board_id, session)


def create_concept_board(concept_board_data: ConceptBoardCreate, session: Session):
    return rcb.create_concept_board(concept_board_data, session)


def update_concept_board(concept_board_id: int, concept_board_update: ConceptBoardUpdate, session: Session):
    return rcb.update_concept_board(concept_board_id, concept_board_update, session)


def delete_concept_board(concept_board_id: int, session: Session):
    return rcb.delete_concept_board(concept_board_id, session)


def get_concept_boards_by_concept(id_concept: int, session: Session):
    concept_boards = rcb.get_all_concept_boards(session)
    return [concept_board for concept_board in concept_boards if concept_board.id_concept == id_concept]
