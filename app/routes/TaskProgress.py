from fastapi import APIRouter, HTTPException

from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate, TaskProgressRead
import app.services.ServiceTaskProgress as stp

router = APIRouter(prefix="/task_progresss", tags=["Task Progresss"])


# Generic endpoints
@router.get("/", response_model=list[TaskProgressRead], status_code=200)
async def get_all_task_progress():
    return stp.get_all_task_progress()


@router.get("/{id}", response_model=TaskProgressRead, status_code=200)
async def get_task_progress_by_id(id: int):
    return stp.get_task_progress_by_id(id)


@router.post("/", status_code=200)
async def create_task_progress(task_progress_data: TaskProgressCreate):
    if stp.create_task_progress(task_progress_data):
        return {"Message": "Task progress created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task progress")


@router.patch("/{id}", status_code=200)
async def update_task_progress(id: int, task_progress_update: TaskProgressUpdate):
    if stp.update_task_progress(id, task_progress_update):
        return {"Message": "Task progress updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task progress")


@router.delete("/{id}", status_code=200)
async def delete_task_progress(id: int):
    if stp.delete_task_progress(id):
        return {"Message": "Task progress deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task progress")


# Model Specific endpoints
@router.get("/section/{id}", response_model=TaskProgressRead, status_code=200)
async def get_task_progress_by_task_section(id_section: int):
    return stp.get_task_progress_by_task_section(id_section)
