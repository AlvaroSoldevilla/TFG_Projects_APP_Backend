import app.repositories.RepositoryTasks as rt
from app.schemas.Task import TaskCreate, TaskUpdate
from app.services.ServiceUsers import get_user_by_id


async def get_all_tasks():
    return await rt.get_all_tasks()


async def get_task_by_id(task_id: int):
    return await rt.get_task_by_id(task_id)


async def create_task(task_data: TaskCreate):
    return await rt.create_task(task_data)


async def update_task(task_id: int, task_update: TaskUpdate):
    return await rt.update_task(task_id, task_update)


async def delete_task(task_id: int):
    return await rt.delete_task(task_id)


async def get_tasks_by_task_section(id_section: int):
    tasks = await get_all_tasks()
    return [task for task in tasks if task.id_section == id_section]


async def get_tasks_by_task_progress(id_progress_section: int):
    tasks = await get_all_tasks()
    return [task for task in tasks if task.id_progress_section == id_progress_section]


async def get_user_assigned_by_task_id(id_task: int):
    task = get_task_by_id(id_task)
    return get_user_by_id(task.id_user_assigned)


async def get_user_created_by_task_id(id_task: int):
    task = get_task_by_id(id_task)
    return get_user_by_id(task.id_user_created)
