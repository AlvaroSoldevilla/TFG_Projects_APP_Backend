from sqlmodel import Session

import app.repositories.RepositoryTaskBoards as rtb
from app.schemas.TaskBoard import TaskBoardCreate, TaskBoardUpdate


def get_all_task_boards(session: Session):
    return rtb.get_all_task_boards(session)


def get_task_board_by_id(task_board_id: int, session: Session):
    return rtb.get_task_board_by_id(task_board_id, session)


def create_task_board(task_board_data: TaskBoardCreate, session: Session):
    return rtb.create_task_board(task_board_data, session)


def update_task_board(task_board_id: int, task_board_update: TaskBoardUpdate, session: Session):
    return rtb.update_task_board(task_board_id, task_board_update, session)


def delete_task_board(task_board_id: int, session: Session):
    return rtb.delete_task_board(task_board_id, session)


def get_task_boards_by_project(id_project: int, session: Session):
    task_boards = rtb.get_all_task_boards(session)
    return [task_board for task_board in task_boards if task_board.id_project == id_project]
