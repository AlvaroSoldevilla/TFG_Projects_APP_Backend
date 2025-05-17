from sqlalchemy import select
from sqlmodel import Session

from app.models.TaskDependencies import TaskDependencies
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate


def get_all_task_dependencies(session: Session):
    query = select(TaskDependencies)
    task_dependencies = session.exec(query).scalars().all()

    return [TaskDependencies.model_validate(td) for td in task_dependencies]


def get_task_dependency_by_id(task_dependency_id: int, session: Session):
    return session.get(TaskDependencies, task_dependency_id)


def create_task_dependency(task_dependency_data: TaskDependencyCreate, session: Session):
    task_dependency = TaskDependencies(**task_dependency_data.model_dump())
    session.add(task_dependency)
    session.commit()
    session.refresh(task_dependency)

    return task_dependency


def update_task_dependency(task_dependency_id: int, task_dependency_update: TaskDependencyUpdate, session: Session):
    task_dependency = session.get(TaskDependencies, task_dependency_id)

    if not task_dependency:
        return False

    for k, v in task_dependency_update.model_dump(exclude_unset=True).items():
        setattr(task_dependency, k, v)

    session.add(task_dependency)
    session.commit()
    session.refresh(task_dependency)

    return True


def delete_task_dependency(task_dependency_id: int, session: Session):
    task_dependency = session.get(TaskDependencies, task_dependency_id)

    if not task_dependency:
        return False

    session.delete(task_dependency)
    session.commit()

    return True

