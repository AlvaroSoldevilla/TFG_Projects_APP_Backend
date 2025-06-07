from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Task import TaskCreate, TaskUpdate, TaskRead
from app.schemas.User import UserRead
import app.services.ServiceTasks as st

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Generic endpoints
@router.get("", dependencies=[Depends(JWTBearer())], response_model=list[TaskRead], status_code=200)
def get_all_tasks(session: Session = Depends(get_session)):
    return st.get_all_tasks(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=TaskRead, status_code=200)
def get_task_by_id(id: int, session: Session = Depends(get_session)):
    return st.get_task_by_id(id, session)


@router.post("", dependencies=[Depends(JWTBearer())], status_code=200, response_model=TaskRead)
def create_task(task_data: TaskCreate, session: Session = Depends(get_session)):
    task = st.create_task(task_data, session)
    if task:
        return task
    else:
        raise HTTPException(status_code=400, detail="Could not create task")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_task(id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    if st.update_task(id, task_update, session):
        return {"Message": "Task updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_task(id: int, session: Session = Depends(get_session)):
    if st.delete_task(id, session):
        return {"Message": "Task deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task")


# Model Specific endpoints
@router.get("/section/{id}", dependencies=[Depends(JWTBearer())], response_model=list[TaskRead], status_code=200)
def get_tasks_by_task_section(id: int, session: Session = Depends(get_session)):
    return st.get_tasks_by_task_section(id, session)


@router.get("/progress/{id}", dependencies=[Depends(JWTBearer())], response_model=list[TaskRead], status_code=200)
def get_tasks_by_task_section(id: int, session: Session = Depends(get_session)):
    return st.get_tasks_by_task_progress(id, session)


@router.get("/parent/{id}", dependencies=[Depends(JWTBearer())], response_model=list[TaskRead], status_code=200)
def get_tasks_by_parent(id: int, session: Session = Depends(get_session)):
    return st.get_tasks_by_parent(id, session)


@router.get("/user/created/{id}", dependencies=[Depends(JWTBearer())], response_model=UserRead, status_code=200)
def get_user_created_task(id: int, session: Session = Depends(get_session)):
    return st.get_user_created_by_task_id(id, session)


@router.get("/user/assigned/{id}", dependencies=[Depends(JWTBearer())], response_model=UserRead, status_code=200)
def get_user_assigned_to_task(id: int, session: Session = Depends(get_session)):
    return st.get_user_assigned_by_task_id(id, session)

