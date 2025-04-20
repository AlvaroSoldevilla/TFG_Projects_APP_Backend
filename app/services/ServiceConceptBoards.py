import app.repositories.RepositoryConceptBoards as rcb
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate, ConceptBoardReadExtended


async def get_all_concept_boards():
    return rcb.get_all_concept_boards()


async def get_concept_board_by_id(concept_board_id: int):
    return rcb.get_concept_board_by_id(concept_board_id)


async def create_concept_board(concept_board_data: ConceptBoardCreate):
    return rcb.create_concept_board(concept_board_data)


async def update_concept_board(concept_board_id: int, concept_board_update: ConceptBoardUpdate):
    return rcb.update_concept_board(concept_board_id, concept_board_update)


async def delete_concept_board(concept_board_id: int):
    return rcb.delete_concept_board(concept_board_id)


async def get_concept_boards_by_concept(id_concept: int):
    concept_boards = rcb.get_all_concept_boards()
    return [concept_board for concept_board in concept_boards if concept_board.id_concept == id_concept]


async def get_display_concept_board(id_board: int):
    concept_board = rcb.get_concept_board_by_id(id_board)
    if concept_board is not None:
        display_board = ConceptBoardReadExtended(**concept_board.model_dump())

        if concept_board.id_parent != concept_board.id:
            display_board.parent_board = rcb.get_concept_board_by_id(concept_board.id_parent)

        display_board.children_board = [children_board for children_board in rcb.get_all_concept_boards() if children_board.id_parent == concept_board.id]

        return display_board
    else:
        return None
