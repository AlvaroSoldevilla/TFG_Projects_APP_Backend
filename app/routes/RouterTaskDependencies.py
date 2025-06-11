from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate, TaskDependencyRead
import app.services.ServiceTaskDependencies as std

router = APIRouter(prefix="/task_dependencies", tags=["Task Dependencies"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[TaskDependencyRead], status_code=200)
def get_all_task_dependencies(session: Session = Depends(get_session)):
    return std.get_all_task_dependencies(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=TaskDependencyRead, status_code=200)
def get_task_dependency_by_id(id: int, session: Session = Depends(get_session)):
    task_dependency = std.get_task_dependency_by_id(id, session)
    if task_dependency is None:
        raise HTTPException(status_code=404, detail="TaskDependency not found")
    else:
        return task_dependency


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=TaskDependencyRead)
def create_task_dependency(task_dependency_data: TaskDependencyCreate, session: Session = Depends(get_session)):
    task_dependency = std.create_task_dependency(task_dependency_data, session)
    if task_dependency:
        return task_dependency
    else:
        raise HTTPException(status_code=400, detail="Could not create task dependency")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_task_dependency(id: int, task_dependency_update: TaskDependencyUpdate, session: Session = Depends(get_session)):
    if std.update_task_dependency(id, task_dependency_update, session):
        return {"Message": "Task dependency updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update task dependency")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_task_dependency(id: int, session: Session = Depends(get_session)):
    if std.delete_task_dependency(id, session):
        return {"Message": "Task dependency deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete task dependency")


# Model Specific endpoints
@router.get("/task/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[TaskDependencyRead], status_code=200)
def get_task_dependencies_by_task(id: int, session: Session = Depends(get_session)):
    return std.get_dependencies_by_task_id(id, session)
