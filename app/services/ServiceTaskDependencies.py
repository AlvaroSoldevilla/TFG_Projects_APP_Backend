from sqlmodel import Session

import app.repositories.RepositoryTaskDependencies as rtd
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate


async def get_all_task_dependencies(session: Session):
    return await rtd.get_all_task_dependencies(session)


async def get_task_dependency_by_id(task_dependency_id: int, session: Session):
    return await rtd.get_task_dependency_by_id(task_dependency_id, session)


async def create_task_dependency(task_dependency_data: TaskDependencyCreate, session: Session):
    return await rtd.create_task_dependency(task_dependency_data, session)


async def update_task_dependency(task_dependency_id: int, task_dependency_update: TaskDependencyUpdate, session: Session):
    return await rtd.update_task_dependency(task_dependency_id, task_dependency_update, session)


async def delete_task_dependency(task_dependency_id: int, session: Session):
    return await rtd.delete_task_dependency(task_dependency_id, session)


async def get_dependencies_by_task_id(id_task: int, session: Session):
    dependencies = await rtd.get_all_task_dependencies(session)
    return [dependency for dependency in dependencies if dependency.id_task == id_task]
