from sqlalchemy import select
from sqlmodel import Session

from app.models.TaskProgress import TaskProgress
from app.schemas.TaskProgress import TaskProgressCreate, TaskProgressUpdate


def get_all_task_progress(session: Session):
    query = select(TaskProgress)
    progress_sections = session.exec(query).scalars().all()

    return [TaskProgress.model_validate(tp) for tp in progress_sections]


def get_task_progress_by_id(task_progress_id: int, session: Session):
    return session.get(TaskProgress, task_progress_id)


def create_task_progress(task_progress_data: TaskProgressCreate, session: Session):
    task_progress = TaskProgress(**task_progress_data.model_dump())
    session.add(task_progress)
    session.commit()
    session.refresh(task_progress)

    return True


def update_task_progress(task_progress_id: int, task_progress_update: TaskProgressUpdate, session: Session):
    task_progress = session.get(TaskProgress, task_progress_id)

    if not task_progress:
        return False

    for k, v in task_progress_update.model_dump(exclude_unset=True).items():
        setattr(task_progress, k, v)

    session.add(task_progress)
    session.commit()
    session.refresh(task_progress)

    return True


def delete_task_progress(task_progress_id: int, session: Session):
    task_progress = session.get(TaskProgress, task_progress_id)

    if not task_progress:
        return False

    session.delete(task_progress)
    session.commit()

    return True
