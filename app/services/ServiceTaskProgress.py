import app.repositories.RepositoryTaskProgress as rtp
from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate


async def get_all_task_progress():
    return rtp.get_all_task_progress()


async def get_task_progress_by_id(task_progress_id: int):
    return rtp.get_task_progress_by_id(task_progress_id)


async def create_task_progress(task_progress_data: TaskProgressCreate):
    return rtp.create_task_progress(task_progress_data)


async def update_task_progress(task_progress_id: int, task_progress_update: TaskProgressUpdate):
    return rtp.update_task_progress(task_progress_id, task_progress_update)


async def delete_task_progress(task_progress_id: int):
    return rtp.delete_task_progress(task_progress_id)


async def get_task_progress_by_task_section(id_section: int):
    task_progress = rtp.get_all_task_progress()
    return [single_task_progress for single_task_progress in task_progress if task_progress.id_section == id_section]
