from fastapi import APIRouter, HTTPException

from app.schemas.Task import TaskCreate, TaskUpdate, TaskRead
from app.schemas.User import UserRead
import app.services.ServiceTasks as st

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Generic endpoints
@router.get("/", response_model=list[TaskRead], status_code=200)
async def get_all_tasks():
    return await st.get_all_tasks()


@router.get("/{id}", response_model=TaskRead, status_code=200)
async def get_task_by_id(id: int):
    return await st.get_task_by_id(id)


@router.post("/", status_code=200)
async def create_task(task_data: TaskCreate):
    if await st.create_task(task_data):
        return {"Message": "Task created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task")


@router.patch("/{id}", status_code=200)
async def update_task(id: int, task_update: TaskUpdate):
    if await st.update_task(id, task_update):
        return {"Message": "Task updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task")


@router.delete("/{id}", status_code=200)
async def delete_task(id: int):
    if await st.delete_task(id):
        return {"Message": "Task deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task")


# Model Specific endpoints
@router.get("/section/{id}", response_model=list[TaskRead], status_code=200)
async def get_tasks_by_task_section(id_section: int):
    return await st.get_tasks_by_task_section(id_section)


@router.get("/progress/{id}", response_model=list[TaskRead], status_code=200)
async def get_tasks_by_task_section(id_progress: int):
    return await st.get_tasks_by_task_section(id_progress)


@router.get("/user/created/{id}", response_model=UserRead, status_code=200)
async def get_user_created_task(id_task: int):
    return await st.get_user_created_by_task_id(id_task)


@router.get("/user/assigned_to/{id}", response_model=UserRead, status_code=200)
async def get_user_assigned_to_task(id_task: int):
    return await st.get_user_assigned_by_task_id(id_task)
