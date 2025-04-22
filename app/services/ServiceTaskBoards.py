import app.repositories.RepositoryTaskBoards as rtb
from app.schemas.TaskBoard import TaskBoardCreate, TaskBoardUpdate


async def get_all_task_boards():
    return await rtb.get_all_task_boards()


async def get_task_board_by_id(task_board_id: int):
    return await rtb.get_task_board_by_id(task_board_id)


async def create_task_board(task_board_data: TaskBoardCreate):
    return await rtb.create_task_board(task_board_data)


async def update_task_board(task_board_id: int, task_board_update: TaskBoardUpdate):
    return await rtb.update_task_board(task_board_id, task_board_update)


async def delete_task_board(task_board_id: int):
    return await rtb.delete_task_board(task_board_id)


async def get_task_boards_by_project(id_project: int):
    task_boards = await rtb.get_all_task_boards()
    return [task_board for task_board in task_boards if task_board.id_project == id_project]
