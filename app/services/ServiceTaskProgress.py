from sqlmodel import Session

import app.repositories.RepositoryTaskProgress as rtp
from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate


async def get_all_task_progress(session: Session):
    return await rtp.get_all_task_progress(session)


async def get_task_progress_by_id(task_progress_id: int, session: Session):
    return await rtp.get_task_progress_by_id(task_progress_id, session)


async def create_task_progress(task_progress_data: TaskProgressCreate, session: Session):
    return await rtp.create_task_progress(task_progress_data, session)


async def update_task_progress(task_progress_id: int, task_progress_update: TaskProgressUpdate, session: Session):
    return await rtp.update_task_progress(task_progress_id, task_progress_update, session)


async def delete_task_progress(task_progress_id: int, session: Session):
    return await rtp.delete_task_progress(task_progress_id, session)


async def get_task_progress_by_task_section(id_section: int, session: Session):
    task_progress = await rtp.get_all_task_progress(session)
    return [single_task_progress for single_task_progress in task_progress if task_progress.id_section == id_section]
