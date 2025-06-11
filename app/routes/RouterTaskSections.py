from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate, TaskSectionRead
import app.services.ServiceTaskSections as sts

router = APIRouter(prefix="/task_sections", tags=["Task_Sections"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[TaskSectionRead], status_code=200)
def get_all_task_sections(session: Session = Depends(get_session)):
    return sts.get_all_task_sections(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=TaskSectionRead, status_code=200)
def get_task_section_by_id(id: int, session: Session = Depends(get_session)):
    task_section = sts.get_task_section_by_id(id, session)
    if task_section is None:
        raise HTTPException(status_code=404, detail="TaskSection not found")
    else:
        return task_section


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=TaskSectionRead)
def create_task_section(task_section_data: TaskSectionCreate, session: Session = Depends(get_session)):
    task_section = sts.create_task_section(task_section_data, session)
    if task_section:
        return task_section
    else:
        raise HTTPException(status_code=400, detail="Could not create task section")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_task_section(id: int, task_section_update: TaskSectionUpdate, session: Session = Depends(get_session)):
    if sts.update_task_section(id, task_section_update, session):
        return {"Message": "Task section updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task section")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_task_section(id: int, session: Session = Depends(get_session)):
    if sts.delete_task_section(id, session):
        return {"Message": "Task section deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task section")


# Model Specific endpoints
@router.get("/board/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[TaskSectionRead], status_code=200)
def get_task_sections_by_task_board(id: int, session: Session = Depends(get_session)):
    return sts.get_task_sections_by_task_board(id, session)
