from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.TaskBoard import TaskBoardCreate, TaskBoardUpdate, TaskBoardRead
import app.services.ServiceTaskBoards as stb

router = APIRouter(prefix="/task_boards", tags=["Task Boards"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[TaskBoardRead], status_code=200)
def get_all_task_boards(session: Session = Depends(get_session)):
    return stb.get_all_task_boards(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=TaskBoardRead, status_code=200)
def get_task_board_by_id(id: int, session: Session = Depends(get_session)):
    task_board = stb.get_task_board_by_id(id, session)
    if task_board is None:
        raise HTTPException(status_code=404, detail="TaskBoard not found")
    else:
        return task_board


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=TaskBoardRead)
def create_task_board(task_board_data: TaskBoardCreate, session: Session = Depends(get_session)):
    task_board = stb.create_task_board(task_board_data, session)
    if task_board:
        return task_board
    else:
        raise HTTPException(status_code=400, detail="Could not create task board")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_task_board(id: int, task_board_update: TaskBoardUpdate, session: Session = Depends(get_session)):
    if stb.update_task_board(id, task_board_update, session):
        return {"Message": "Task board updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task board")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_task_board(id: int, session: Session = Depends(get_session)):
    if stb.delete_task_board(id, session):
        return {"Message": "Task board deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task board")


# Model Specific endpoints
@router.get("/project/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[TaskBoardRead], status_code=200)
def get_task_boards_by_project(id: int, session: Session = Depends(get_session)):
    return stb.get_task_boards_by_project(id, session)
