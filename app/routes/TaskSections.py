from fastapi import APIRouter, HTTPException

from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate, TaskSectionRead
import app.services.ServiceTaskSections as sts

router = APIRouter(prefix="/task_sections", tags=["Task_Sections"])


# Generic endpoints
@router.get("/", response_model=list[TaskSectionRead], status_code=200)
async def get_all_task_sections():
    return sts.get_all_task_sections()


@router.get("/{id}", response_model=TaskSectionRead, status_code=200)
async def get_task_section_by_id(id: int):
    return sts.get_task_section_by_id(id)


@router.post("/", status_code=200)
async def create_task_section(task_section_data: TaskSectionCreate):
    if sts.create_task_section(task_section_data):
        return {"Message": "Task section created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create task section")


@router.patch("/{id}", status_code=200)
async def update_task_section(id: int, task_section_update: TaskSectionUpdate):
    if sts.update_task_section(id, task_section_update):
        return {"Message": "Task section updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task section")


@router.delete("/{id}", status_code=200)
async def delete_task_section(id: int):
    if sts.delete_task_section(id):
        return {"Message": "Task section deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task section")


# Model Specific endpoints
@router.get("/board/{id}", response_model=list[TaskSectionRead], status_code=200)
async def get_task_sections_by_task_board(id_board: int):
    return sts.get_task_sections_by_task_board(id_board)
