from sqlalchemy import select
from sqlmodel import Session

from app.models.Tasks import Tasks
from app.schemas.Task import TaskCreate, TaskUpdate


def get_all_tasks(session: Session):
    query = select(Tasks)
    tasks = session.exec(query).scalars().all()

    return [Tasks.model_validate(t) for t in tasks]


def get_task_by_id(task_id: int, session: Session):
    return session.get(Tasks, task_id)


def create_task(task_data: TaskCreate, session: Session):
    task = Tasks(**task_data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)

    return task


def update_task(task_id: int, task_update: TaskUpdate, session: Session):
    task = session.get(Tasks, task_id)

    if not task:
        return False

    for k, v in task_update.model_dump(exclude_unset=True).items():
        setattr(task, k, v)

    session.add(task)
    session.commit()
    session.refresh(task)

    return True


def delete_task(task_id: int, session: Session):
    task = session.get(Tasks, task_id)

    if not task:
        return False

    session.delete(task)
    session.commit()

    return True
