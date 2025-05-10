from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Task import TaskCreate, TaskUpdate, TaskRead
from app.schemas.User import UserRead
import app.services.ServiceTasks as st

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Generic endpoints
@router.get("/", response_model=list[TaskRead], status_code=200)
def get_all_tasks(session: Session = Depends(get_session)):
    return st.get_all_tasks(session)


@router.get("/{id}", response_model=TaskRead, status_code=200)
def get_task_by_id(id: int, session: Session = Depends(get_session)):
    return st.get_task_by_id(id, session)


@router.post("/", status_code=200)
def create_task(task_data: TaskCreate, session: Session = Depends(get_session)):
    if st.create_task(task_data, session):
        return {"Message": "Task created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task")


@router.patch("/{id}", status_code=200)
def update_task(id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    if st.update_task(id, task_update, session):
        return {"Message": "Task updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task")


@router.delete("/{id}", status_code=200)
def delete_task(id: int, session: Session = Depends(get_session)):
    if st.delete_task(id, session):
        return {"Message": "Task deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task")


# Model Specific endpoints
@router.get("/section/{id}", response_model=list[TaskRead], status_code=200)
def get_tasks_by_task_section(id_section: int, session: Session = Depends(get_session)):
    return st.get_tasks_by_task_section(id_section, session)


@router.get("/progress/{id}", response_model=list[TaskRead], status_code=200)
def get_tasks_by_task_section(id_progress: int, session: Session = Depends(get_session)):
    return st.get_tasks_by_task_section(id_progress, session)


@router.get("/user/created/{id}", response_model=UserRead, status_code=200)
def get_user_created_task(id_task: int, session: Session = Depends(get_session)):
    return st.get_user_created_by_task_id(id_task, session)


@router.get("/user/assigned/{id}", response_model=UserRead, status_code=200)
def get_user_assigned_to_task(id_task: int, session: Session = Depends(get_session)):
    return st.get_user_assigned_by_task_id(id_task, session)
