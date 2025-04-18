from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Tasks import Tasks
from app.schemas.Task import TaskCreate, TaskUpdate


async def get_all_tasks(session: Session = Depends(get_session())):
    query = select(Tasks)
    tasks = session.exec(query).scalar().all()

    return [Tasks.model_validate(t) for t in tasks]


async def get_task_by_id(task_id: int, session: Session = Depends(get_session())):
    return session.get(Tasks, task_id)


async def create_task(task_data: TaskCreate, session: Session = Depends(get_session())):
    task = Tasks(**task_data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)

    return True


async def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session())):
    task = session.get(Tasks, task_id)

    if not task:
        return False

    for k, v in task_update.model_dump(exclude_unset=True).items():
        setattr(task, k, v)

    session.add(task)
    session.commit()
    session.refresh(task)

    return True


async def delete_task(task_id: int, session: Session = Depends(get_session())):
    task = session.get(Tasks, task_id)

    if not task:
        return False

    session.delete(task)
    session.commit()

    return True
