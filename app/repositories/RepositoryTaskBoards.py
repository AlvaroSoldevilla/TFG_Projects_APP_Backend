from sqlalchemy import select
from sqlmodel import Session

from app.models.TaskBoards import TaskBoards
from app.schemas.TaskBoard import TaskBoardCreate, TaskBoardUpdate


async def get_all_task_boards(session: Session):
    query = select(TaskBoards)
    task_boards = session.exec(query).scalar().all()

    return [TaskBoards.model_validate(tb) for tb in task_boards]


async def get_task_board_by_id(task_board_id: int, session: Session):
    return session.get(TaskBoards, task_board_id)


async def create_task_board(task_board_data: TaskBoardCreate, session: Session):
    task_board = TaskBoards(**task_board_data.model_dump())
    session.add(task_board)
    session.commit()
    session.refresh(task_board)

    return True


async def update_task_board(task_board_id: int, task_board_update: TaskBoardUpdate, session: Session):
    task_board = session.get(TaskBoards, task_board_id)

    if not task_board:
        return False

    for k, v in task_board_update.model_dump(exclude_unset=True).items():
        setattr(task_board, k, v)

    session.add(task_board)
    session.commit()
    session.refresh(task_board)

    return True


async def delete_task_board(task_board_id: int, session: Session):
    task_board = session.get(TaskBoards, task_board_id)

    if not task_board:
        return False

    session.delete(task_board)
    session.commit()

    return True

