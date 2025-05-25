from sqlmodel import Session

import app.repositories.RepositoryTaskProgress as rtp
from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate


def get_all_task_progress(session: Session):
    return rtp.get_all_task_progress(session)


def get_task_progress_by_id(task_progress_id: int, session: Session):
    return rtp.get_task_progress_by_id(task_progress_id, session)


def create_task_progress(task_progress_data: TaskProgressCreate, session: Session):
    return rtp.create_task_progress(task_progress_data, session)


def update_task_progress(task_progress_id: int, task_progress_update: TaskProgressUpdate, session: Session):
    return rtp.update_task_progress(task_progress_id, task_progress_update, session)


def delete_task_progress(task_progress_id: int, session: Session):
    return rtp.delete_task_progress(task_progress_id, session)


def get_task_progress_by_task_section(id_section: int, session: Session):
    task_progress = rtp.get_all_task_progress(session)
    return [single_task_progress for single_task_progress in task_progress if single_task_progress.id_section == id_section]
