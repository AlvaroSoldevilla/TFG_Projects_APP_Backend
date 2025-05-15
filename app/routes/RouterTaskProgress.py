from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate, TaskProgressRead
import app.services.ServiceTaskProgress as stp

router = APIRouter(prefix="/task_progress", tags=["Task Progress"])


# Generic endpoints
@router.get("/", response_model=list[TaskProgressRead], status_code=200)
def get_all_task_progress(session: Session = Depends(get_session)):
    return stp.get_all_task_progress(session)


@router.get("/{id}", response_model=TaskProgressRead, status_code=200)
def get_task_progress_by_id(id: int, session: Session = Depends(get_session)):
    return stp.get_task_progress_by_id(id, session)


@router.post("/", status_code=200)
def create_task_progress(task_progress_data: TaskProgressCreate, session: Session = Depends(get_session)):
    if stp.create_task_progress(task_progress_data, session):
        return {"Message": "Task progress created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task progress")


@router.patch("/{id}", status_code=200)
def update_task_progress(id: int, task_progress_update: TaskProgressUpdate, session: Session = Depends(get_session)):
    if stp.update_task_progress(id, task_progress_update, session):
        return {"Message": "Task progress updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task progress")


@router.delete("/{id}", status_code=200)
def delete_task_progress(id: int, session: Session = Depends(get_session)):
    if stp.delete_task_progress(id, session):
        return {"Message": "Task progress deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task progress")


# Model Specific endpoints
@router.get("/section/{id}", response_model=list[TaskProgressRead], status_code=200)
def get_task_progress_by_task_section(id: int, session: Session = Depends(get_session)):
    return stp.get_task_progress_by_task_section(id, session)
