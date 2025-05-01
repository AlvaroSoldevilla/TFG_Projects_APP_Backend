from sqlmodel import Session

import app.repositories.RepositoryTaskDependencies as rtd
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate


def get_all_task_dependencies(session: Session):
    return rtd.get_all_task_dependencies(session)


def get_task_dependency_by_id(task_dependency_id: int, session: Session):
    return rtd.get_task_dependency_by_id(task_dependency_id, session)


def create_task_dependency(task_dependency_data: TaskDependencyCreate, session: Session):
    return rtd.create_task_dependency(task_dependency_data, session)


def update_task_dependency(task_dependency_id: int, task_dependency_update: TaskDependencyUpdate, session: Session):
    return rtd.update_task_dependency(task_dependency_id, task_dependency_update, session)


def delete_task_dependency(task_dependency_id: int, session: Session):
    return rtd.delete_task_dependency(task_dependency_id, session)


def get_dependencies_by_task_id(id_task: int, session: Session):
    dependencies = rtd.get_all_task_dependencies(session)
    return [dependency for dependency in dependencies if dependency.id_task == id_task]
