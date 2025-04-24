from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.TaskBoard import TaskBoardCreate, TaskBoardUpdate, TaskBoardRead
import app.services.ServiceTaskBoards as stb

router = APIRouter(prefix="/task_boards", tags=["Task Boards"])


# Generic endpoints
@router.get("/", response_model=list[TaskBoardRead], status_code=200)
async def get_all_task_boards(session: Session = Depends(get_session)):
    return await stb.get_all_task_boards(session)


@router.get("/{id}", response_model=TaskBoardRead, status_code=200)
async def get_task_board_by_id(id: int, session: Session = Depends(get_session)):
    return await stb.get_task_board_by_id(id, session)


@router.post("/", status_code=200)
async def create_task_board(task_board_data: TaskBoardCreate, session: Session = Depends(get_session)):
    if await stb.create_task_board(task_board_data, session):
        return {"Message": "Task board created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task board")


@router.patch("/{id}", status_code=200)
async def update_task_board(id: int, task_board_update: TaskBoardUpdate, session: Session = Depends(get_session)):
    if await stb.update_task_board(id, task_board_update, session):
        return {"Message": "Task board updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task board")


@router.delete("/{id}", status_code=200)
async def delete_task_board(id: int, session: Session = Depends(get_session)):
    if await stb.delete_task_board(id, session):
        return {"Message": "Task board deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task board")


# Model Specific endpoints
@router.get("/project/{id}", response_model=TaskBoardRead, status_code=200)
async def get_task_boards_by_project(id_project: int, session: Session = Depends(get_session)):
    return await stb.get_task_boards_by_project(id_project, session)
