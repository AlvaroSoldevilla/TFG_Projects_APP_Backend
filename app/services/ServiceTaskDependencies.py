import app.repositories.RepositoryTaskDependencies as rtd
from app.schemas.TaskDependency import TaskDependencyCreate, TaskDependencyUpdate


async def get_all_task_dependencies():
    return rtd.get_all_task_dependencies()


async def get_task_dependency_by_id(task_dependency_id: int):
    return rtd.get_task_dependency_by_id(task_dependency_id)


async def create_task_dependency(task_dependency_data: TaskDependencyCreate):
    return rtd.create_task_dependency(task_dependency_data)


async def update_task_dependency(task_dependency_id: int, task_dependency_update: TaskDependencyUpdate):
    return rtd.update_task_dependency(task_dependency_id, task_dependency_update)


async def delete_task_dependency(task_dependency_id: int):
    return rtd.delete_task_dependency(task_dependency_id)


async def get_dependencies_by_task_id(id_task: int):
    dependencies = rtd.get_all_task_dependencies()
    return [dependency for dependency in dependencies if dependency.id_task == id_task]
