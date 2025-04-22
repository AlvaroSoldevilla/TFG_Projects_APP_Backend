import app.repositories.RepositoryConceptBoards as rcb
from app.schemas.ConceptBoard import ConceptBoardCreate, ConceptBoardUpdate


async def get_all_concept_boards():
    return await rcb.get_all_concept_boards()


async def get_concept_board_by_id(concept_board_id: int):
    return await rcb.get_concept_board_by_id(concept_board_id)


async def create_concept_board(concept_board_data: ConceptBoardCreate):
    return await rcb.create_concept_board(concept_board_data)


async def update_concept_board(concept_board_id: int, concept_board_update: ConceptBoardUpdate):
    return await rcb.update_concept_board(concept_board_id, concept_board_update)


async def delete_concept_board(concept_board_id: int):
    return await rcb.delete_concept_board(concept_board_id)


async def get_concept_boards_by_concept(id_concept: int):
    concept_boards = await rcb.get_all_concept_boards()
    return [concept_board for concept_board in concept_boards if concept_board.id_concept == id_concept]
