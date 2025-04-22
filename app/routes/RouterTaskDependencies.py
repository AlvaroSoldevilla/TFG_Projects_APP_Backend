from fastapi import APIRouter, HTTPException

from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate, TaskDependencyRead
import app.services.ServiceTaskDependencies as std

router = APIRouter(prefix="/task_dependencies", tags=["Task Dependencies"])


# Generic endpoints
@router.get("/", response_model=list[TaskDependencyRead], status_code=200)
async def get_all_task_dependencies():
    return await std.get_all_task_dependencies()


@router.get("/{id}", response_model=TaskDependencyRead, status_code=200)
async def get_task_dependency_by_id(id: int):
    return await std.get_task_dependency_by_id(id)


@router.post("/", status_code=200)
async def create_task_dependency(task_dependency_data: TaskDependencyCreate):
    if await std.create_task_dependency(task_dependency_data):
        return {"Message": "Task dependency created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task dependency")


@router.patch("/{id}", status_code=200)
async def update_task_dependency(id: int, task_dependency_update: TaskDependencyUpdate):
    if await std.update_task_dependency(id, task_dependency_update):
        return {"Message": "Task dependency updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task dependency")


@router.delete("/{id}", status_code=200)
async def delete_task_dependency(id: int):
    if await std.delete_task_dependency(id):
        return {"Message": "Task dependency deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task dependency")


# Model Specific endpoints
@router.get("/task/{id}", response_model=list[TaskDependencyRead], status_code=200)
async def get_task_dependencies_by_task(task_id: int):
    return await std.get_dependencies_by_task_id(task_id)
