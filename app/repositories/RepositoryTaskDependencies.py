from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.TaskDependencies import TaskDependencies
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate


async def get_all_task_dependencies(session: Session = Depends(get_session())):
    query = select(TaskDependencies)
    task_dependencies = session.exec(query).scalar().all()

    return [TaskDependencies.model_validate(td) for td in task_dependencies]


async def get_task_dependency_by_id(task_dependency_id: int, session: Session = Depends(get_session())):
    return session.get(TaskDependencies, task_dependency_id)


async def create_task_dependency(task_dependency_data: TaskDependencyCreate, session: Session = Depends(get_session())):
    task_dependency = TaskDependencies(**task_dependency_data.model_dump())
    session.add(task_dependency)
    session.commit()
    session.refresh(task_dependency)

    return True


async def update_task_dependency(task_dependency_id: int, task_dependency_update: TaskDependencyUpdate, session: Session = Depends(get_session())):
    task_dependency = session.get(TaskDependencies, task_dependency_id)

    if not task_dependency:
        return False

    for k, v in task_dependency_update.model_dump(exclude_unset=True).items():
        setattr(task_dependency, k, v)

    session.add(task_dependency)
    session.commit()
    session.refresh(task_dependency)

    return True


async def delete_task_dependency(task_dependency_id: int, session: Session = Depends(get_session())):
    task_dependency = session.get(TaskDependencies, task_dependency_id)

    if not task_dependency:
        return False

    session.delete(task_dependency)
    session.commit()

    return True

